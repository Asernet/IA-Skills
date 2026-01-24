---
name: context-optimization
description: Usa questa skill per ottimizzare l'uso del contesto, ridurre i costi dei token e migliorare l'efficienza.
---

# Tecniche di Ottimizzazione del Contesto

L'ottimizzazione del contesto estende la capacità effettiva delle finestre di contesto limitate attraverso compressione strategica, mascheramento, caching e partizionamento. L'obiettivo non è aumentare magicamente le finestre di contesto ma fare un uso migliore della capacità disponibile. Un'ottimizzazione efficace può raddoppiare o triplicare la capacità effettiva del contesto senza richiedere modelli più grandi o contesti più lunghi.

## Quando Attivare

Attiva questa skill quando:

- I limiti di contesto vincolano la complessità del task
- Ottimizzi per la riduzione dei costi (meno token = costi inferiori)
- Riduci la latenza per lunghe conversazioni
- Implementi sistemi di agenti a lungo termine (long-running)
- Hai bisogno di gestire documenti o conversazioni più grandi
- Costruisci sistemi in produzione su scala

## Concetti Chiave

L'ottimizzazione del contesto estende la capacità effettiva attraverso quattro strategie primarie: compattazione (riassumere contenuti contesto vicino ai limiti), mascheramento osservazioni (sostituire output prolissi con riferimenti), ottimizzazione KV-cache (riutilizzare calcoli cachati), e partizionamento contesto (dividere il lavoro attraverso contesti isolati).

L'insight chiave è che la qualità del contesto conta più della quantità. L'ottimizzazione preserva il segnale riducendo il rumore. L'arte sta nel selezionare cosa tenere rispetto a cosa scartare, e quando applicare ogni tecnica.

## Argomenti Dettagliati

### Strategie di Compattazione

**Cos'è la Compattazione**
La compattazione è la pratica di riassumere i contenuti del contesto quando ci si avvicina ai limiti, poi reinizializzare una nuova finestra di contesto con il riassunto. Questo distilla i contenuti di una finestra di contesto in modo ad alta fedeltà, abilitando l'agente a continuare con minima degradazione delle performance.

La compattazione serve tipicamente come prima leva nell'ottimizzazione del contesto. L'arte sta nel selezionare cosa tenere rispetto a cosa scartare.

**Implementazione Compattazione**
La compattazione funziona identificando sezioni che possono essere compresse, generando riassunti che catturano punti essenziali, e sostituendo il contenuto completo con riassunti. La priorità per la compressione va agli output tool (sostituisci con riassunti), vecchi turni (riassumi conversazione iniziale), documenti recuperati (riassumi se esistono versioni recenti), e mai comprimere il prompt di sistema.

**Generazione Riassunto**
Riassunti efficaci preservano elementi diversi a seconda del tipo di messaggio:

Output Tool: Preserva scoperte chiave, metriche e conclusioni. Rimuovi output grezzo prolisso.

Turni Conversazionali: Preserva decisioni chiave, impegni e cambi di contesto. Rimuovi riempitivi e botta-e-risposta.

Documenti Recuperati: Preserva fatti chiave e affermazioni. Rimuovi prove di supporto ed elaborazione.

### Mascheramento Osservazioni

**Il Problema delle Osservazioni**
Gli output dei tool possono comprendere l'80%+ dell'uso dei token nelle traiettorie degli agenti. Molto di questo è output prolisso che ha già servito il suo scopo. Una volta che un agente ha usato un output tool per prendere una decisione, mantenere l'output completo fornisce valore decrescente mentre consuma contesto significativo.

Il mascheramento osservazioni sostituisce output tool prolissi con riferimenti compatti. L'informazione rimane accessibile se necessaria ma non consuma contesto continuamente.

**Selezione Strategia Mascheramento**
Non tutte le osservazioni dovrebbero essere mascherate ugualmente:

Mai mascherare: Osservazioni critiche per il task corrente, osservazioni dal turno più recente, osservazioni usate nel ragionamento attivo.

Considera mascheramento: Osservazioni da 3+ turni fa, output prolissi con punti chiave estraibili, osservazioni il cui scopo è stato servito.

Maschera sempre: Output ripetuti, header/footer standard (boilerplate), output già riassunti nella conversazione.

### Ottimizzazione KV-Cache

**Comprendere la KV-Cache**
La KV-cache memorizza tensori Key e Value calcolati durante l'inferenza, crescendo linearmente con la lunghezza della sequenza. Caching della KV-cache attraverso richieste che condividono prefissi identici evita il ricalcolo.

Il prefix caching riusa blocchi KV attraverso richieste con prefissi identici usando block matching basato su hash. Questo riduce drammaticamente costo e latenza per richieste con prefissi comuni come prompt di sistema.

**Pattern Ottimizzazione Cache**
Ottimizza per il caching riordinando elementi del contesto per massimizzare i cache hit. Piazza elementi stabili prima (prompt di sistema, definizioni tool), poi elementi frequentemente riusati, poi elementi unici per ultimi.

Progetta prompt per massimizzare la stabilità della cache: evita contenuto dinamico come timestamp, usa formattazione consistente, mantieni struttura stabile attraverso le sessioni.

### Partizionamento Contesto

**Partizionamento Sub-Agent**
La forma più aggressiva di ottimizzazione del contesto è partizionare il lavoro attraverso sub-agenti con contesti isolati. Ogni sub-agente opera in un contesto pulito focalizzato sul suo subtask senza portare contesto accumulato da altri subtask.

Questo approccio raggiunge la separazione delle responsabilità—il contesto di ricerca dettagliato rimane isolato dentro i sub-agenti mentre il coordinatore si focalizza su sintesi e analisi.

**Aggregazione Risultati**
Aggrega risultati da subtask partizionati validando che tutte le partizioni siano completate, unendo risultati compatibili, e riassumendo se ancora troppo grandi.

### Gestione Budget

**Allocazione Budget Contesto**
Progetta budget di contesto espliciti. Alloca token alle categorie: prompt di sistema, definizioni tool, documenti recuperati, cronologia messaggi e buffer riservato. Monitora l'uso contro il budget e attiva l'ottimizzazione quando ci si avvicina ai limiti.

**Ottimizzazione Trigger-Based**
Monitora segnali per trigger di ottimizzazione: utilizzo token sopra 80%, indicatori di degradazione, e cali di performance. Applica tecniche di ottimizzazione appropriate basate sulla composizione del contesto.

## Guida Pratica

### Framework Decisionale Ottimizzazione

Quando ottimizzare:

- Utilizzo contesto supera 70%
- Qualità risposta degrada man mano che le conversazioni si estendono
- Costi aumentano dovuto a contesti lunghi
- Latenza aumenta con lunghezza conversazione

Cosa applicare:

- Output tool dominano: mascheramento osservazioni
- Documenti recuperati dominano: riassunto o partizionamento
- Cronologia messaggi domina: compattazione con riassunto
- Componenti multipli: combina strategie

### Considerazioni Performance

La compattazione dovrebbe raggiungere 50-70% riduzione token con meno del 5% degradazione qualità. Il mascheramento dovrebbe raggiungere 60-80% riduzione in osservazioni mascherate. L'ottimizzazione cache dovrebbe raggiungere 70%+ hit rate per carichi di lavoro stabili.

Monitora e itera su strategie di ottimizzazione basate su efficacia misurata.

## Esempi

**Esempio 1: Trigger Compattazione**

```python
if context_tokens / context_limit > 0.8:
    context = compact_context(context)
```

**Esempio 2: Mascheramento Osservazioni**

```python
if len(observation) > max_length:
    ref_id = store_observation(observation)
    return f"[Obs:{ref_id} elided. Key: {extract_key(observation)}]"
```

**Esempio 3: Ordinamento Cache-Friendly**

```python
# Stable content first
context = [system_prompt, tool_definitions]  # Cacheable
context += [reused_templates]  # Reusable
context += [unique_content]  # Unique
```

## Linee Guida

1. Misura prima di ottimizzare—conosci il tuo stato attuale
2. Applica compattazione prima del mascheramento quando possibile
3. Progetta per stabilità cache con prompt consistenti
4. Partiziona prima che il contesto diventi problematico
5. Monitora efficacia ottimizzazione nel tempo
6. Bilancia risparmio token contro preservazione qualità
7. Testa ottimizzazione a scala di produzione
8. Implementa degradazione aggraziata per casi limite

## Integrazione

Questa skill costruisce su context-fundamentals e context-degradation. Si connette a:

- **multi-agent-patterns** - Partizionamento come isolamento
- **evaluation** - Misurare efficacia ottimizzazione
- **memory-systems** - Offloadare contesto in memoria

## Riferimenti

Riferimento interno:

- [Optimization Techniques Reference](./references/optimization_techniques.md) - Riferimento tecnico dettagliato
- [Context Optimization Guidelines](./references/optimization_guidelines.md) - Linee guida

Skill correlate in questa collezione:

- context-fundamentals - Basi contesto
- context-degradation - Comprendere quando ottimizzare
- evaluation - Misurare ottimizzazione

Risorse esterne:

- Research on context window limitations
- KV-cache optimization techniques
- Production engineering guides
