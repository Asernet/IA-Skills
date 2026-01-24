---
name: project-development
description: Usa questa skill per avviare progetti LLM, pipeline batch, o strutturare architetture di progetti basati su agenti.
---

# Metodologia Sviluppo Progetti

Questa skill copre i principi per identificare task adatti al processamento LLM, progettare architetture di progetto efficaci e iterare rapidamente usando sviluppo assistito da agenti. La metodologia si applica sia che si costruisca una pipeline di processamento batch, un sistema di ricerca multi-agente o un'applicazione agente interattiva.

## Quando Attivare

Attiva questa skill quando:

- Avvii un nuovo progetto che potrebbe beneficiare dal processamento LLM
- Valuti se un task è ben adatto per agenti contro codice tradizionale
- Progetti l'architettura per un'applicazione potenziata da LLM
- Pianifichi una pipeline di processamento batch con output strutturati
- Scegli tra approcci singolo-agente e multi-agente
- Stimi costi e tempistiche per progetti pesanti su LLM

## Concetti Chiave

### Riconoscimento Fit Task-Modello

Non ogni problema beneficia dal processamento LLM. Il primo passo in ogni progetto è valutare se le caratteristiche del task si allineano con i punti di forza dell'LLM. Questa valutazione dovrebbe accadere prima di scrivere qualsiasi codice.

**Task adatti a LLM condividono queste caratteristiche:**

| Caratteristica                      | Perché Funziona                                                     |
| ----------------------------------- | ------------------------------------------------------------------- |
| Sintesi attraverso fonti            | LLM eccellono nel combinare informazioni da input multipli          |
| Giudizio soggettivo con rubriche    | LLM gestiscono grading, valutazione e classificazione con criteri   |
| Output linguaggio naturale          | Quando l'obiettivo è testo leggibile da umani, non dati strutturati |
| Tolleranza errore                   | Fallimenti individuali non rompono il sistema complessivo           |
| Processamento batch                 | Nessuno stato conversazionale richiesto tra elementi                |
| Conoscenza dominio in addestramento | Il modello ha già contesto rilevante                                |

**Task non adatti a LLM condividono queste caratteristiche:**

| Caratteristica                  | Perché Fallisce                                            |
| ------------------------------- | ---------------------------------------------------------- |
| Calcolo preciso                 | Matematica, conteggio e algoritmi esatti sono inaffidabili |
| Requisiti real-time             | Latenza LLM è troppo alta per risposte sub-secondo         |
| Requisiti accuratezza perfetta  | Rischio allucinazione rende accuratezza 100% impossibile   |
| Dipendenza dati proprietari     | Il modello manca del contesto necessario                   |
| Dipendenze sequenziali          | Ogni passo dipende pesantemente dal risultato precedente   |
| Requisiti output deterministici | Stesso input deve produrre output identico                 |

La valutazione dovrebbe accadere attraverso prototipazione manuale: prendi un esempio rappresentativo e testalo direttamente con il modello target prima di costruire qualsiasi automazione.

### Il Passo Prototipo Manuale

Prima di investire in automazione, valida il fit task-modello con un test manuale. Copia un input rappresentativo nell'interfaccia modello. Valuta la qualità dell'output. Questo richiede minuti e previene ore di sviluppo sprecato.

Questa validazione risponde a domande critiche:

- Il modello ha la conoscenza richiesta per questo task?
- Può il modello produrre output nel formato di cui hai bisogno?
- Quale livello di qualità dovresti aspettarti a scala?
- Ci sono modalità di fallimento ovvie da indirizzare?

Se il prototipo manuale fallisce, il sistema automatizzato fallirà. Se ha successo, hai una baseline per confronto e un template per il design del prompt.

### Architettura Pipeline

Progetti LLM beneficiano da architetture pipeline a stadi dove ogni stadio è:

- **Discreto**: Confini chiari tra stadi
- **Idempotente**: Rieseguire produce lo stesso risultato
- **Cachable**: Risultati intermedi persistono su disco
- **Indipendente**: Ogni stadio può girare separatamente

**La struttura pipeline canonica:**

```
acquire → prepare → process → parse → render
```

1. **Acquire**: Recupera dati grezzi da fonti (API, file, database)
2. **Prepare**: Trasforma dati in formato prompt
3. **Process**: Esegui chiamate LLM (il passo costoso, non-deterministico)
4. **Parse**: Estrai dati strutturati da output LLM
5. **Render**: Genera output finali (report, file, visualizzazioni)

Stadi 1, 2, 4 e 5 sono deterministici. Stadio 3 è non-deterministico e costoso. Questa separazione permette di rieseguire lo stadio LLM costoso solo quando necessario, mentre iteri velocemente su parsing e rendering.

### File System come Macchina a Stati

Usa il file system per tracciare lo stato della pipeline piuttosto che database o strutture in-memory. Ogni unità di processamento ottiene una directory. Ogni completamento stadio è marcato dall'esistenza del file.

```
data/{id}/
├── raw.json         # stadio acquire completo
├── prompt.md        # stadio prepare completo
├── response.md      # stadio process completo
├── parsed.json      # stadio parse completo
```

Per controllare se un elemento necessita processamento: controlla se il file output esiste. Per rieseguire uno stadio: cancella il suo file output e file a valle. Per debuggare: leggi i file intermedi direttamente.

Questo pattern fornisce:

- Idempotenza naturale (esistenza file blocca esecuzione)
- Debugging facile (tutto lo stato è leggibile da umano)
- Parallelizzazione semplice (ogni directory è indipendente)
- Caching banale (file persistono attraverso esecuzioni)

### Design Output Strutturato

Quando gli output LLM devono essere parsati programmaticamente, il design del prompt determina direttamente l'affidabilità del parsing. Il prompt deve specificare requisiti di formato esatti con esempi.

**Specifica struttura efficace include:**

1. **Marker sezione**: Header espliciti o prefissi per parsing
2. **Esempi formato**: Mostra esattamente come dovrebbe apparire l'output
3. **Disclosure razionale**: "Parserò questo programmaticamente"
4. **Valori vincolati**: Opzioni enumerate, range punteggio, formati

Il codice di parsing deve gestire variazioni graziosamente. Gli LLM non seguono istruzioni perfettamente. Costruisci parser che:

- Usano pattern regex flessibili abbastanza da gestire variazioni formattazione minori
- Forniscono default sensati quando sezioni mancano
- Loggano fallimenti parsing per revisione successiva piuttosto che crashare

### Sviluppo Assistito da Agente

Modelli moderni capaci di agente possono accelerare lo sviluppo significativamente. Il pattern è:

1. Descrivi l'obiettivo del progetto e vincoli
2. Lascia che l'agente generi implementazione iniziale
3. Testa e itera su fallimenti specifici
4. Raffina prompt e architettura basato su risultati

Questo riguarda l'iterazione rapida: genera, testa, fixa, ripeti. L'agente gestisce boilerplate e struttura iniziale mentre tu ti concentri su requisiti dominio-specifici e casi limite.

### Stima Costi e Scala

Il processamento LLM ha costi prevedibili che dovrebbero essere stimati prima di iniziare. La formula:

```
Costo totale = (elementi × token_per_elemento × prezzo_per_token) + overhead API
```

Per processamento batch:

- Stima token input per elemento (prompt + contesto)
- Stima token output per elemento (lunghezza risposta tipica)
- Moltiplica per conteggio elementi
- Aggiungi 20-30% buffer per ritentativi e fallimenti

Traccia costi effettivi durante sviluppo. Se i costi superano stime significativamente, rivaluta l'approccio. Considera:

- Ridurre lunghezza contesto attraverso troncamento
- Usare modelli più piccoli per elementi più semplici
- Cachare e riusare risultati parziali
- Processamento parallelo per ridurre tempo wall-clock (non costo token)

## Argomenti Dettagliati

### Scegliere Architettura Singolo vs Multi-Agente

Pipeline singolo-agente funzionano per:

- Processamento batch con elementi indipendenti
- Task dove elementi non interagiscono
- Gestione costi e complessità più semplice

Architetture multi-agente funzionano per:

- Esplorazione parallela di aspetti diversi
- Task che eccedono capacità singola finestra contesto
- Quando sub-agenti specializzati migliorano qualità

La ragione primaria per multi-agente è isolamento contesto, non antropomorfizzazione ruolo. I sub-agenti ottengono finestre contesto fresche per subtask focalizzati. Questo previene degradazione contesto su task a lunga esecuzione.

### Riduzione Architettonica

Inizia con architettura minima. Aggiungi complessità solo quando provato necessario. Prove di produzione mostrano che rimuovere tool specializzati spesso migliora performance.

**Quando la riduzione sovraperforma la complessità:**

- Il tuo layer dati è ben documentato e consistentemente strutturato
- Il modello ha capacità di ragionamento sufficiente
- I tuoi tool specializzati stavano vincolando piuttosto che abilitando
- Stai spendendo più tempo a mantenere impalcatura che a migliorare risultati

**Quando la complessità è necessaria:**

- I tuoi dati sottostanti sono disordinati, inconsistenti o documentati male
- Il dominio richiede conoscenza specializzata che il modello manca
- Vincoli sicurezza richiedono limitazione capacità agente
- Operazioni sono veramente complesse e beneficiano da workflow strutturati

### Iterazione e Refactoring

Aspettati di rifattorizzare. Sistemi agente di produzione a scala richiedono iterazioni architetturali multiple.

Costruisci per il cambiamento:

- Mantieni architettura semplice e non opinionata
- Testa attraverso punti di forza modello per verificare che la tua imbracatura non stia limitando performance
- Progetta sistemi che beneficiano da miglioramenti modello piuttosto che bloccare in limitazioni

## Guida Pratica

### Template Pianificazione Progetto

1. **Analisi Task**
   - Qual è l'input? Qual è l'output desiderato?
   - È sintesi, generazione, classificazione o analisi?
   - Quale tasso errore è accettabile?
   - Qual è il valore per completamento di successo?

2. **Validazione Manuale**
   - Testa un esempio con modello target
   - Valuta qualità output e formato
   - Identifica modalità fallimento
   - Stima token per elemento

3. **Selezione Architettura**
   - Singola pipeline vs multi-agente
   - Tool richiesti e sorgenti dati
   - Strategia storage e caching
   - Approccio parallelizzazione

4. **Stima Costi**
   - Elementi × token × prezzo
   - Tempo sviluppo
   - Requisiti infrastruttura
   - Costi operativi in corso

5. **Piano Sviluppo**
   - Implementazione stadio-per-stadio
   - Strategia testing per stadio
   - Milestone iterazione
   - Approccio deployment

### Anti-Pattern da Evitare

**Saltare validazione manuale**: Costruire automazione prima di verificare che il modello può fare il task spreca tempo significativo quando l'approccio è fondamentalmente viziato.

**Pipeline monolitiche**: Combinare tutti gli stadi in un solo script rende debugging e iterazione difficili. Separa stadi con output intermedi persistenti.

**Sovra-vincolare il modello**: Aggiungere guardrails, pre-filtraggio e logica validazione che il modello potrebbe gestire da solo. Testa se la tua impalcatura aiuta o ferisce.

**Ignorare costi fino alla produzione**: Costi token compongono velocemente a scala. Stima e traccia dall'inizio.

**Requisiti parsing perfetti**: Aspettarsi che LLM seguano istruzioni formato perfettamente. Costruisci parser robusti che gestiscono variazioni.

**Ottimizzazione prematura**: Aggiungere caching, parallelizzazione e ottimizzazione prima che la pipeline base funzioni correttamente.

## Esempi

**Esempio 1: Pipeline Analisi Batch (Karpathy's HN Time Capsule)**

Task: Analizza 930 discussioni HN di 10 anni fa con grading col senno di poi.

Architettura:

- Pipeline 5-stadi: fetch → prompt → analyze → parse → render
- Stato file system: data/{date}/{item_id}/ con file output stadio
- Output strutturato: 6 sezioni con requisiti formato espliciti
- Esecuzione parallela: 15 worker per chiamate LLM

Risultati: $58 costo totale, ~1 ora esecuzione, output HTML statico.

**Esempio 2: Riduzione Architettonica (Vercel d0)**

Task: Agente Text-to-SQL per analytics interni.

Prima: 17 tool specializzati, 80% tasso successo, 274s esecuzione media.

Dopo: 2 tool (bash + SQL), 100% tasso successo, 77s esecuzione media.

Insight chiave: Il layer semantico era già buona documentazione. Claude aveva solo bisogno di accesso per leggere file direttamente.

## Linee Guida

1. Valida fit task-modello con prototipazione manuale prima di costruire automazione
2. Struttura pipeline come stadi discreti, idempotenti, cachable
3. Usa il file system per gestione stato e debugging
4. Progetta prompt per output strutturati, parsabili con esempi formato espliciti
5. Inizia con architettura minima; aggiungi complessità solo quando provato necessario
6. Stima costi presto e traccia attraverso sviluppo
7. Costruisci parser robusti che gestiscono variazioni output LLM
8. Aspettati e pianifica per iterazioni architetturali multiple
9. Testa se l'impalcatura aiuta o vincola performance modello
10. Usa sviluppo assistito da agente per iterazione rapida su implementazione

## Integrazione

Questa skill si connette a:

- context-fundamentals - Comprendere vincoli contesto per design prompt
- tool-design - Progettare tool per sistemi agente dentro pipeline
- multi-agent-patterns - Quando usare multi-agente vs pipeline singole
- evaluation - Valutare output pipeline e performance agente
- context-compression - Gestire contesto quando le pipeline eccedono i limiti

## Riferimenti

Riferimenti interni:

- [Case Studies](./references/case-studies.md) - Karpathy HN Capsule, Vercel d0, Manus patterns
- [Pipeline Patterns](./references/pipeline-patterns.md) - Guida architettura pipeline dettagliata

Skill correlate in questa collezione:

- tool-design - Architettura tool e pattern riduzione
- multi-agent-patterns - Quando usare architetture multi-agente
- evaluation - Framework valutazione output

Risorse esterne:

- Karpathy's HN Time Capsule project: https://github.com/karpathy/hn-time-capsule
- Vercel d0 architectural reduction: https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools
- Manus context engineering: Peak Ji's blog on context engineering lessons
- Anthropic multi-agent research: How we built our multi-agent research system
