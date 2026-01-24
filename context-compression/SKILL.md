---
name: context-compression
description: Usa questa skill per comprimere il contesto, riassumere la cronologia, ridurre l'uso di token o gestire sessioni lunghe.
---

# Strategie di Compressione del Contesto

Quando le sessioni dell'agente generano milioni di token di cronologia della conversazione, la compressione diventa obbligatoria. L'approccio ingenuo è la compressione aggressiva per minimizzare i token per richiesta. Il target di ottimizzazione corretto è token per task: token totali consumati per completare un task, inclusi i costi di re-fetching quando la compressione perde informazioni critiche.

## Quando Attivare

Attiva questa skill quando:

- Le sessioni dell'agente superano i limiti della finestra di contesto
- I codebase superano le finestre di contesto (sistemi 5M+ token)
- Progetti strategie di riassunto della conversazione
- Esegui il debug di casi in cui gli agenti "dimenticano" quali file hanno modificato
- Costruisci framework di valutazione per la qualità della compressione

## Concetti Chiave

La compressione del contesto scambia il risparmio di token con la perdita di informazioni. Esistono tre approcci pronti per la produzione:

1. **Anchored Iterative Summarization (Riassunto Iterativo Ancorato)**: Mantieni riassunti strutturati e persistenti con sezioni esplicite per l'intento della sessione, modifiche ai file, decisioni e prossimi passi. Quando scatta la compressione, riassumi solo lo span appena troncato e uniscilo al riassunto esistente. La struttura forza la preservazione dedicando sezioni a tipi specifici di informazioni.

2. **Opaque Compression (Compressione Opaca)**: Produci rappresentazioni compresse ottimizzate per la fedeltà di ricostruzione. Raggiunge i rapporti di compressione più alti (99%+) ma sacrifica l'interpretabilità. Non puoi verificare cosa è stato preservato.

3. **Regenerative Full Summary (Riassunto Completo Rigenerativo)**: Genera riassunti strutturati dettagliati ad ogni compressione. Produce output leggibile ma può perdere dettagli attraverso cicli di compressione ripetuti dovuti alla rigenerazione completa piuttosto che all'unione incrementale.

L'insight critico: la struttura forza la preservazione. Sezioni dedicate agiscono come checklist che il riassumitore deve popolare, prevenendo la deriva silenziosa delle informazioni.

## Argomenti Dettagliati

### Perché i Token-Per-Task Contano

Le metriche di compressione tradizionali puntano ai token-per-richiesta. Questa è l'ottimizzazione sbagliata. Quando la compressione perde dettagli critici come percorsi file o messaggi di errore, l'agente deve recuperare nuovamente le informazioni, riesplorare approcci e sprecare token per recuperare il contesto.

La metrica giusta è token-per-task: token totali consumati dall'inizio del task al completamento. Una strategia di compressione che risparmia lo 0.5% in più di token ma causa il 20% in più di re-fetching costa di più complessivamente.

### Il Problema dell'Artifact Trail

L'integrità dell'Artifact Trail è la dimensione più debole attraverso tutti i metodi di compressione, con punteggi di 2.2-2.5 su 5.0 nelle valutazioni. Anche il riassunto strutturato con sezioni file esplicite fatica a mantenere il tracciamento completo dei file attraverso sessioni lunghe.

Gli agenti di coding devono sapere:

- Quali file sono stati creati
- Quali file sono stati modificati e cosa è cambiato
- Quali file sono stati letti ma non cambiati
- Nomi funzioni, nomi variabili, messaggi di errore

Questo problema richiede probabilmente una gestione specializzata oltre il riassunto generale: un indice artefatti separato o un tracciamento esplicito dello stato dei file nello scaffolding dell'agente.

### Sezioni Riassunto Strutturato

Riassunti strutturati efficaci includono sezioni esplicite:

```markdown
## Intento Sessione

[Cosa l'utente sta cercando di realizzare]

## File Modificati

- auth.controller.ts: Fixed JWT token generation
- config/redis.ts: Updated connection pooling
- tests/auth.test.ts: Added mock setup for new config

## Decisioni Prese

- Usando Redis connection pool invece di connessioni per-request
- Logica di retry con exponential backoff per fallimenti transitori

## Stato Corrente

- 14 test passati, 2 falliti
- Rimanente: mock setup per test session service

## Prossimi Passi

1. Fix rimanenti fallimenti test
2. Esegui suite test completa
3. Aggiorna documentazione
```

Questa struttura previene la perdita silenziosa di percorsi file o decisioni perché ogni sezione deve essere indirizzata esplicitamente.

### Strategie di Trigger Compressione

Quando attivare la compressione conta tanto quanto come comprimere:

| Strategia            | Punto Trigger                            | Trade-off                                    |
| -------------------- | ---------------------------------------- | -------------------------------------------- |
| Soglia fissa         | 70-80% utilizzo contesto                 | Semplice ma può comprimere troppo presto     |
| Finestra scorrevole  | Mantieni ultimi N turni + riassunto      | Dimensione contesto prevedibile              |
| Basata su importanza | Comprimi prima sezioni a bassa rilevanza | Complessa ma preserva il segnale             |
| Confine task         | Comprimi a completamenti logici task     | Riassunti puliti ma tempistica imprevedibile |

L'approccio a finestra scorrevole con riassunti strutturati fornisce il miglior bilanciamento di prevedibilità e qualità per la maggior parte dei casi d'uso di agenti di coding.

### Valutazione Probe-Based

Metriche tradizionali come ROUGE o similarità di embedding falliscono nel catturare la qualità funzionale della compressione. Un riassunto può avere un alto punteggio sulla sovrapposizione lessicale ma perdere l'unico percorso file di cui l'agente ha bisogno.

La valutazione basata su probe misura direttamente la qualità funzionale facendo domande dopo la compressione:

| Tipo Probe   | Cosa Testa             | Domanda Esempio                              |
| ------------ | ---------------------- | -------------------------------------------- |
| Recall       | Ritenzione fattuale    | "Qual era il messaggio di errore originale?" |
| Artifact     | Tracciamento file      | "Quali file abbiamo modificato?"             |
| Continuation | Pianificazione task    | "Cosa dovremmo fare dopo?"                   |
| Decision     | Catena di ragionamento | "Cosa abbiamo deciso sul problema Redis?"    |

Se la compressione ha preservato l'informazione giusta, l'agente risponde correttamente. Se no, indovina o allucina.

### Dimensioni di Valutazione

Sei dimensioni catturano la qualità della compressione per agenti di coding:

1. **Accuratezza**: I dettagli tecnici sono corretti? Percorsi file, nomi funzioni, codici errore.
2. **Consapevolezza Contesto**: La risposta riflette lo stato corrente della conversazione?
3. **Artifact Trail**: L'agente sa quali file sono stati letti o modificati?
4. **Completezza**: La risposta indirizza tutte le parti della domanda?
5. **Continuità**: Il lavoro può continuare senza recuperare nuovamente informazioni?
6. **Rispetto Istruzioni**: La risposta rispetta i vincoli dichiarati?

L'accuratezza mostra la variazione maggiore tra metodi di compressione (gap di 0.6 punti). L'artifact trail è universalmente debole (range 2.2-2.5).

## Guida Pratica

### Workflow di Compressione a Tre Fasi

Per grandi codebase o sistemi di agenti che superano le finestre di contesto, applica la compressione attraverso tre fasi:

1. **Fase Ricerca**: Produci un documento di ricerca da diagrammi di architettura, documentazione e interfacce chiave. Comprimi l'esplorazione in un'analisi strutturata di componenti e dipendenze. Output: singolo documento di ricerca.

2. **Fase Pianificazione**: Converti la ricerca in specifica di implementazione con firme di funzione, definizioni di tipo e flusso dati. Un codebase di 5M token si comprime a circa 2,000 parole di specifica.

3. **Fase Implementazione**: Esegui contro la specifica. Il contesto rimane focalizzato sulla specifica piuttosto che sull'esplorazione grezza del codebase.

### Usare Artefatti Esempio come Semi

Quando fornito con un esempio di migrazione manuale o PR di riferimento, usalo come template per comprendere il pattern target. L'esempio rivela vincoli che l'analisi statica non può far emergere: quali invarianti devono reggere, quali servizi si rompono con i cambiamenti, e come appare una migrazione pulita.

Questo è particolarmente importante quando l'agente non può distinguere la complessità essenziale (requisiti di business) dalla complessità accidentale (workaround legacy). L'artefatto esempio codifica quella distinzione.

### Implementare Anchored Iterative Summarization

1. Definisci sezioni di riassunto esplicite che corrispondono ai bisogni del tuo agente
2. Al primo trigger di compressione, riassumi la cronologia troncata in sezioni
3. Alle compressioni successive, riassumi solo il nuovo contenuto troncato
4. Unisci il nuovo riassunto nelle sezioni esistenti piuttosto che rigenerare
5. Traccia quale informazione è arrivata da quale ciclo di compressione per il debug

### Quando Usare Ogni Approccio

**Usa anchored iterative summarization quando:**

- Le sessioni sono lunghe (100+ messaggi)
- Il tracciamento file conta (coding, debugging)
- Devi verificare cosa è stato preservato

**Usa opaque compression quando:**

- Risparmio massimo di token richiesto
- Le sessioni sono relativamente brevi
- I costi di re-fetching sono bassi

**Usa regenerative summaries quando:**

- L'interpretabilità del riassunto è critica
- Le sessioni hanno confini di fase chiari
- La revisione completa del contesto è accettabile ad ogni compressione

### Considerazioni Rapporto Compressione

| Metodo             | Rapporto Compressione | Punteggio Qualità | Trade-off                                        |
| ------------------ | --------------------- | ----------------- | ------------------------------------------------ |
| Anchored Iterative | 98.6%                 | 3.70              | Miglior qualità, compressione leggermente minore |
| Regenerative       | 98.7%                 | 3.44              | Buona qualità, compressione moderata             |
| Opaque             | 99.3%                 | 3.35              | Miglior compressione, perdita qualità            |

Lo 0.7% di token addizionali mantenuti dal riassunto strutturato compra 0.35 punti qualità. Per qualsiasi task dove i costi di re-fetching contano, questo trade-off favorisce approcci strutturati.

## Esempi

**Esempio 1: Debugging Session Compression**

Contesto originale (89,000 token, 178 messaggi):

- Errore 401 su endpoint /api/auth/login
- Tracciato attraverso auth controller, middleware, session store
- Trovata connessione Redis stantia
- Fixato connection pooling, aggiunta logica retry
- 14 test passati, 2 falliti

Riassunto strutturato dopo compressione:

```markdown
## Intento Sessione

Debug errore 401 Unauthorized su /api/auth/login nonostante credenziali valide.

## Causa Radice

Connessione Redis stantia nel session store. JWT generato correttamente ma la sessione non poteva essere persistita.

## File Modificati

- auth.controller.ts: Nessun cambiamento (read only)
- middleware/cors.ts: Nessun cambiamento (esaminato)
- config/redis.ts: Fixata configurazione connection pooling
- services/session.service.ts: Aggiunta logica retry per fallimenti transitori
- tests/auth.test.ts: Aggiornato mock setup

## Stato Test

14 passati, 2 falliti (problemi mock setup)

## Prossimi Passi

1. Fix fallimenti test rimanenti (mock session service)
2. Esegui suite test completa
3. Deploy in staging
```

## Linee Guida

1. Ottimizza per token-per-task, non token-per-richiesta
2. Usa riassunti strutturati con sezioni esplicite per tracciamento file
3. Attiva compressione al 70-80% utilizzo contesto
4. Implementa unione incrementale piuttosto che rigenerazione completa
5. Testa qualità compressione con valutazione probe-based
6. Traccia artifact trail separatamente se il tracciamento file è critico
7. Accetta rapporti di compressione leggermente inferiori per migliore ritenzione qualità
8. Monitora frequenza re-fetching come segnale qualità compressione

## Integrazione

Questa skill si connette a diverse altre nella collezione:

- **context-degradation** - La compressione è una strategia di mitigazione per la degradazione
- **context-optimization** - La compressione è una tecnica di ottimizzazione tra le tante
- **evaluation** - La valutazione probe-based si applica al testing della compressione
- **memory-systems** - La compressione si relaziona ai pattern di memoria scratchpad e riassunto

## Riferimenti

Riferimento interno:

- [Evaluation Framework Reference](./references/evaluation-framework.md) - Tipi probe dettagliati e rubriche di scoring

Skill correlate in questa collezione:

- context-degradation - Capire cosa previene la compressione
- context-optimization - Strategie di ottimizzazione più ampie
- evaluation - Costruire framework di valutazione

Risorse esterne:

- Factory Research: Evaluating Context Compression for AI Agents (December 2025)
- Research on LLM-as-judge evaluation methodology (Zheng et al., 2023)
- Netflix Engineering: "The Infinite Software Crisis" - Three-phase workflow and context compression at scale (AI Summit 2025)

---

## Skill Metadata

**Created**: 2025-12-22
**Last Updated**: 2025-12-26
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 1.1.0
