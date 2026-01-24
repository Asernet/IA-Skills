---
name: context-degradation
description: Usa questa skill per diagnosticare problemi di contesto, 'lost-in-middle', o degradazione delle performance dell'agente.
---

# Pattern di Degradazione del Contesto

I modelli linguistici esibiscono pattern di degradazione prevedibili all'aumentare della lunghezza del contesto. Comprendere questi pattern è essenziale per diagnosticare fallimenti e progettare sistemi resilienti. La degradazione del contesto non è uno stato binario ma un continuum di degradazione delle performance che si manifesta in diversi modi distinti.

## Quando Attivare

Attiva questa skill quando:

- Le performance dell'agente degradano inaspettatamente durante lunghe conversazioni
- Esegui il debug di casi in cui gli agenti producono output errati o irrilevanti
- Progetti sistemi che devono gestire grandi contesti in modo affidabile
- Valuti scelte di context engineering per sistemi in produzione
- Investighi fenomeni "lost in middle" negli output dell'agente
- Analizzi fallimenti relativi al contesto nel comportamento dell'agente

## Concetti Chiave

La degradazione del contesto si manifesta attraverso diversi pattern distinti. Il fenomeno lost-in-middle causa meno attenzione alle informazioni nel centro del contesto. Il context poisoning si verifica quando gli errori si compongono attraverso riferimenti ripetuti. La context distraction accade quando informazioni irrilevanti sopraffanno il contenuto rilevante. La context confusion sorge quando il modello non può determinare quale contesto si applica. Il context clash si sviluppa quando informazioni accumulate confliggono direttamente.

Questi pattern sono prevedibili e possono essere mitigati attraverso pattern architetturali come compattazione, mascheramento, partizionamento e isolamento.

## Argomenti Dettagliati

### Il Fenomeno Lost-in-Middle

Il pattern di degradazione più ben documentato è l'effetto "lost-in-middle", dove i modelli dimostrano curve di attenzione a forma di U. Le informazioni all'inizio e alla fine del contesto ricevono attenzione affidabile, mentre le informazioni sepolte nel mezzo soffrono di un'accuratezza di recall drammaticamente ridotta.

**Evidenza Empirica**
La ricerca dimostra che le informazioni rilevanti piazzate nel mezzo del contesto sperimentano un'accuratezza di recall inferiore del 10-40% rispetto alle stesse informazioni all'inizio o alla fine. Questo non è un fallimento del modello ma una conseguenza delle meccaniche di attenzione e delle distribuzioni dei dati di training.

I modelli allocano massiccia attenzione al primo token (spesso il token BOS) per stabilizzare gli stati interni. Questo crea un "pozzo di attenzione" (attention sink) che assorbe il budget di attenzione. Man mano che il contesto cresce, il budget limitato viene stirato, e i token centrali falliscono nell'ottenere sufficiente peso di attenzione per un retrieval affidabile.

**Implicazioni Pratiche**
Progetta il posizionamento del contesto con i pattern di attenzione in mente. Piazza informazioni critiche all'inizio o alla fine del contesto. Considera se l'informazione sarà interrogata direttamente o deve supportare il ragionamento—se l'ultimo, il posizionamento conta meno ma la qualità complessiva del segnale conta di più.

Per lunghi documenti o conversazioni, usa strutture di riassunto che fanno emergere informazioni chiave in posizioni favorite dall'attenzione. Usa intestazioni di sezione esplicite e transizioni per aiutare i modelli a navigare la struttura.

### Context Poisoning

Il context poisoning si verifica quando allucinazioni, errori o informazioni non corrette entrano nel contesto e si compongono attraverso riferimenti ripetuti. Una volta avvelenato, il contesto crea loop di feedback che rinforzano credenze non corrette.

**Come Avviene il Poisoning**
Il poisoning tipicamente entra attraverso tre percorsi. Primo, gli output dei tool possono contenere errori o formati inaspettati che i modelli accettano come verità di base (ground truth). Secondo, i documenti recuperati possono contenere informazioni non corrette o obsolete che i modelli incorporano nel ragionamento. Terzo, riassunti generati dal modello o output intermedi possono introdurre allucinazioni che persistono nel contesto.

L'effetto composito è severo. Se la sezione obiettivi di un agente diventa avvelenata, sviluppa strategie che richiedono sforzo sostanziale per essere disfatte. Ogni decisione successiva fa riferimento al contenuto avvelenato, rinforzando assunzioni non corrette.

**Rilevamento e Recupero**
Guarda per sintomi inclusi qualità dell'output degradata su task che precedentemente avevano successo, disallineamento dei tool dove gli agenti chiamano tool o parametri sbagliati, e allucinazioni che persistono nonostante tentativi di correzione. Quando questi sintomi appaiono, considera il context poisoning.

Il recupero richiede la rimozione o sostituzione del contenuto avvelenato. Questo può coinvolgere il troncamento del contesto a prima del punto di poisoning, notando esplicitamente il poisoning nel contesto e chiedendo una rivalutazione, o riavviando con contesto pulito e preservando solo informazioni verificate.

### Context Distraction

La context distraction emerge quando il contesto cresce così tanto che i modelli si sovra-focalizzano sulle informazioni fornite a spese della loro conoscenza di training. Il modello presta attenzione a tutto nel contesto indipendentemente dalla rilevanza, e questo crea pressione per usare le informazioni fornite anche quando la conoscenza interna è più accurata.

**L'Effetto Distrattore**
La ricerca mostra che anche un singolo documento irrilevante nel contesto riduce le performance su task che coinvolgono documenti rilevanti. Distrattori multipli compongono la degradazione. L'effetto non riguarda il rumore in termini assoluti ma l'allocazione dell'attenzione—informazioni irrilevanti competono con informazioni rilevanti per un budget di attenzione limitato.

I modelli non hanno un meccanismo per "saltare" contesto irrilevante. Devono prestare attenzione a tutto ciò che è fornito, e questo obbligo crea distrazione anche quando l'informazione irrilevante chiaramente non è utile.

**Strategie di Mitigazione**
Mitiga la distrazione attraverso un'attenta curatela di ciò che entra nel contesto. Applica filtro di rilevanza prima di caricare documenti recuperati. Usa namespace e organizzazione per rendere le sezioni irrilevanti facili da ignorare strutturalmente. Considera se l'informazione ha veramente bisogno di essere nel contesto o può essere accessibile attraverso chiamate tool.

### Context Confusion

La context confusion sorge quando informazioni irrilevanti influenzano le risposte in modi che degradano la qualità. Questo è correlato alla distrazione ma distinto—la confusione riguarda l'influenza del contesto sul comportamento del modello piuttosto che l'allocazione dell'attenzione.

Se metti qualcosa nel contesto, il modello deve prestarvi attenzione. Il modello può incorporare informazioni irrilevanti, usare definizioni tool inappropriate, o applicare vincoli che venivano da contesti diversi. La confusione è specialmente problematica quando il contesto contiene tipi di task multipli o quando si passa tra task all'interno di una singola sessione.

**Segni di Confusione**
Guarda per risposte che indirizzano l'aspetto sbagliato di una query, chiamate tool che sembrano appropriate per un task diverso, o output che mischiano requisiti da fonti multiple. Questi indicano confusione su quale contesto si applica alla situazione corrente.

**Soluzioni Architetturali**
Le soluzioni architetturali includono segmentazione esplicita dei task dove task diversi ottengono finestre di contesto diverse, transizioni chiare tra contesti task, e gestione dello stato che isola il contesto per obiettivi diversi.

### Context Clash

Il context clash si sviluppa quando informazioni accumulate confliggono direttamente, creando una guida contraddittoria che fa deragliare il ragionamento. Questo differisce dal poisoning dove un pezzo di informazione è non corretto—nel clash, più pezzi corretti di informazione si contraddicono a vicenda.

**Fonti di Clash**
Il clash sorge comunemente da retrieval multi-sorgente dove diverse fonti hanno informazioni contraddittorie, conflitti di versione dove informazioni obsolete e correnti appaiono entrambe nel contesto, e conflitti di prospettiva dove punti di vista diversi sono validi ma incompatibili.

**Approcci di Risoluzione**
Gli approcci di risoluzione includono marcatura esplicita del conflitto che identifica contraddizioni e richiede chiarimenti, regole di priorità che stabiliscono quale fonte ha la precedenza, e filtro di versione che esclude informazioni obsolete dal contesto.

### Benchmark Empirici e Soglie

La ricerca fornisce dati concreti sui pattern di degradazione che informano le decisioni di design.

**Risultati Benchmark RULER**
Il benchmark RULER consegna risultati che fanno riflettere: solo il 50% dei modelli che dichiarano contesto 32K+ mantengono performance soddisfacenti a 32K token. GPT-5.2 mostra la minore degradazione tra i modelli attuali, mentre molti perdono ancora 30+ punti a contesti estesi. Punteggi quasi perfetti su semplici test needle-in-haystack non si traducono in comprensione reale a lungo contesto.

**Soglie di Degradazione Specifiche per Modello**
| Modello | Insorgenza Degradazione | Degradazione Severa | Note |
|-------|-------------------|-------------------|-------|
| GPT-5.2 | ~64K token | ~200K token | Miglior resistenza alla degradazione complessiva con thinking mode |
| Claude Opus 4.5 | ~100K token | ~180K token | Finestra contesto 200K, forte gestione attenzione |
| Claude Sonnet 4.5 | ~80K token | ~150K token | Ottimizzato per agenti e task di coding |
| Gemini 3 Pro | ~500K token | ~800K token | Finestra contesto 1M, multimodalità nativa |
| Gemini 3 Flash | ~300K token | ~600K token | Velocità 3x di Gemini 2.5, 81.2% MMMU-Pro |

### Scoperte Controintuitive

La ricerca rivela diversi pattern controintuitivi che sfidano le assunzioni sulla gestione del contesto.

**Haystack Mescolati Superano Quelli Coerenti**
Studi hanno trovato che haystack mescolati (incoerenti) producono performance migliori di quelli logicamente coerenti. Questo suggerisce che il contesto coerente può creare false associazioni che confondono il retrieval, mentre il contesto incoerente forza i modelli a basarsi sull'exact matching.

**Singoli Distrattori Hanno Impatto Smisurato**
Anche un singolo documento irrilevante riduce le performance significativamente. L'effetto non è proporzionale alla quantità di rumore ma segue una funzione a gradino dove la presenza di qualsiasi distrattore innesca la degradazione.

**Correlazione Similarità Needle-Question**
Minore similarità tra coppie needle e question mostra degradazione più veloce con la lunghezza del contesto. Task che richiedono inferenza attraverso contenuti dissimili sono particolarmente vulnerabili.

## Guida Pratica

### L'Approccio a Quattro Secchi (Four-Bucket Approach)

Quattro strategie indirizzano diversi aspetti della degradazione del contesto:

**Write (Scrivi)**: Salva il contesto fuori dalla finestra usando scratchpad, file system o storage esterno. Questo mantiene il contesto attivo snello preservando l'accesso alle informazioni.

**Select (Seleziona)**: Tira il contesto rilevante nella finestra attraverso retrieval, filtro e prioritizzazione. Questo indirizza la distrazione escludendo informazioni irrilevanti.

**Compress (Comprimi)**: Riduci i token preservando le informazioni attraverso riassunto, astrazione e mascheramento delle osservazioni. Questo estende la capacità effettiva del contesto.

**Isolate (Isola)**: Spacca il contesto attraverso sub-agenti o sessioni per prevenire che ogni singolo contesto cresca abbastanza da degradare. Questa è la strategia più aggressiva ma spesso la più efficace.

## Esempi

**Esempio 1: Rilevare Degradazione**

```yaml
# Context grows during long conversation
turn_1: 1000 tokens
turn_5: 8000 tokens
turn_10: 25000 tokens
turn_20: 60000 tokens (degradation begins)
turn_30: 90000 tokens (significant degradation)
```

**Esempio 2: Mitigare Lost-in-Middle**

```markdown
# Organize context with critical info at edges

[CURRENT TASK] # At start

- Goal: Generate quarterly report
- Deadline: End of week

[DETAILED CONTEXT] # Middle (less attention)

- 50 pages of data
- Multiple analysis sections
- Supporting evidence

[KEY FINDINGS] # At end

- Revenue up 15%
- Costs down 8%
- Growth in Region A
```

## Linee Guida

1. Monitora la correlazione tra lunghezza contesto e performance durante lo sviluppo
2. Piazza informazioni critiche all'inizio o alla fine del contesto
3. Implementa trigger di compattazione prima che la degradazione diventi severa
4. Valida i documenti recuperati per l'accuratezza prima di aggiungerli al contesto
5. Usa il versioning per prevenire che informazioni obsolete causino clash
6. Segmenta i task per prevenire context confusion attraverso obiettivi diversi
7. Progetta per una degradazione aggraziata (graceful degradation) piuttosto che assumere condizioni perfette
8. Testa con contesti progressivamente più grandi per trovare soglie di degradazione

## Integrazione

Questa skill costruisce su context-fundamentals e dovrebbe essere studiata dopo aver compreso i concetti base del contesto. Si connette a:

- **context-optimization** - Tecniche per mitigare la degradazione
- **multi-agent-patterns** - Usare l'isolamento per prevenire la degradazione
- **evaluation** - Misurare e rilevare la degradazione in produzione

## Riferimenti

Riferimento interno:

- [Degradation Patterns Reference](./references/patterns.md) - Riferimento tecnico dettagliato

Skill correlate in questa collezione:

- context-fundamentals - Basi del contesto
- context-optimization - Tecniche di mitigazione
- evaluation - Rilevamento e misurazione

Risorse esterne:

- Research on attention mechanisms and context window limitations
- Studies on the "lost-in-middle" phenomenon
- Production engineering guides from AI labs
