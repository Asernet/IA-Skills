---
name: context-fundamentals
description: Usa questa skill per comprendere e spiegare finestre di contesto, architetture di agenti e meccanismi di attenzione.
---

# Fondamenti di Context Engineering

Il contesto è lo stato completo disponibile a un modello linguistico al momento dell'inferenza. Include tutto ciò a cui il modello può prestare attenzione quando genera risposte: istruzioni di sistema, definizioni dei tool, documenti recuperati, cronologia messaggi e output dei tool. Comprendere i fondamenti del contesto è prerequisito per un context engineering efficace.

## Quando Attivare

Attiva questa skill quando:

- Progetti nuovi sistemi agenzia o modifichi architetture esistenti
- Esegui il debug di comportamenti inaspettati dell'agente che possono relazionarsi al contesto
- Ottimizzi l'uso del contesto per ridurre costi token o migliorare le performance
- Fai onboarding di nuovi membri del team ai concetti di context engineering
- Revisioni decisioni di design relative al contesto

## Concetti Chiave

Il contesto comprende diverse componenti distinte, ognuna con caratteristiche e vincoli diversi. Il meccanismo di attenzione crea un budget finito che vincola l'uso efficace del contesto. La progressive disclosure (divulgazione progressiva) gestisce questo vincolo caricando informazioni solo quando necessario. La disciplina ingegneristica è curare il più piccolo set di token ad alto segnale che raggiunge i risultati desiderati.

## Argomenti Dettagliati

### L'Anatomia del Contesto

**System Prompts (Prompt di Sistema)**
I prompt di sistema stabiliscono l'identità fondamentale dell'agente, i vincoli e le linee guida comportamentali. Vengono caricati una volta all'inizio della sessione e tipicamente persistono per tutta la conversazione. I prompt di sistema dovrebbero essere estremamente chiari e usare linguaggio semplice e diretto alla giusta altitudine per l'agente.

La giusta altitudine bilancia due modalità di fallimento. A un estremo, gli ingegneri codificano logica complessa e fragile che crea fragilità e carico di manutenzione. All'altro estremo, gli ingegneri forniscono guida vaga di alto livello che fallisce nel dare segnali concreti per gli output desiderati o assume falsamente contesto condiviso. L'altitudine ottimale trova un equilibrio: abbastanza specifica da guidare il comportamento efficacemente, eppure abbastanza flessibile da fornire euristiche forti.

Organizza i prompt in sezioni distinte usando tagging XML o intestazioni Markdown per delineare informazioni di background, istruzioni, guida tool e descrizione output. La formattazione esatta conta meno man mano che i modelli diventano più capaci, ma la chiarezza strutturale rimane preziosa.

**Tool Definitions (Definizioni Tool)**
Le definizioni dei tool specificano le azioni che un agente può intraprendere. Ogni tool include un nome, descrizione, parametri e formato di ritorno. Le definizioni dei tool vivono vicino all'inizio del contesto dopo la serializzazione, tipicamente prima o dopo il prompt di sistema.

Le descrizioni dei tool collettivamente guidano il comportamento dell'agente. Descrizioni povere forzano gli agenti a indovinare; descrizioni ottimizzate includono contesto d'uso, esempi e default. Il principio di consolidamento afferma che se un ingegnere umano non può dire definitivamente quale tool dovrebbe essere usato in una data situazione, non ci si può aspettare che un agente faccia meglio.

**Retrieved Documents (Documenti Recuperati)**
I documenti recuperati forniscono conoscenza specifica del dominio, materiali di riferimento o informazioni rilevanti per il task. Gli agenti usano retrieval augmented generation per tirare documenti rilevanti nel contesto a runtime piuttosto che pre-caricare tutte le informazioni possibili.

L'approccio just-in-time mantiene identificatori leggeri (percorsi file, query memorizzate, web link) e usa questi riferimenti per caricare dati nel contesto dinamicamente. Questo rispecchia la cognizione umana: generalmente non memorizziamo interi corpus di informazioni ma piuttosto usiamo organizzazione esterna e sistemi di indicizzazione per recuperare informazioni rilevanti su richiesta.

**Message History (Cronologia Messaggi)**
La cronologia messaggi contiene la conversazione tra l'utente e l'agente, incluse query precedenti, risposte e ragionamento. Per task a lungo orizzonte, la cronologia messaggi può crescere fino a dominare l'uso del contesto.

La cronologia messaggi serve come memoria scratchpad dove gli agenti tracciano il progresso, mantengono lo stato del task e preservano il ragionamento attraverso i turni. Una gestione efficace della cronologia messaggi è critica per il completamento di task a lungo orizzonte.

**Tool Outputs (Output dei Tool)**
Gli output dei tool sono i risultati delle azioni dell'agente: contenuti file, risultati di ricerca, output esecuzione comandi, risposte API e dati simili. Gli output dei tool comprendono la maggioranza dei token nelle traiettorie tipiche degli agenti, con ricerche che mostrano che le osservazioni (output tool) possono raggiungere l'83.9% dell'uso totale del contesto.

Gli output dei tool consumano contesto sia che siano rilevanti per le decisioni correnti o meno. Questo crea pressione per strategie come mascheramento delle osservazioni, compattazione e ritenzione selettiva dei risultati tool.

### Finestre di Contesto e Meccaniche di Attenzione

**Il Vincolo del Budget di Attenzione**
I modelli linguistici processano i token attraverso meccanismi di attenzione che creano relazioni a coppie tra tutti i token nel contesto. Per n token, questo crea n² relazioni che devono essere calcolate e memorizzate. All'aumentare della lunghezza del contesto, l'abilità del modello di catturare queste relazioni si stira.

I modelli sviluppano pattern di attenzione da distribuzioni di dati di training dove predominano sequenze più brevi. Questo significa che i modelli hanno meno esperienza con e meno parametri specializzati per dipendenze context-wide. Il risultato è un "budget di attenzione" che si esaurisce man mano che il contesto cresce.

**Position Encoding e Context Extension**
L'interpolazione del position encoding permette ai modelli di gestire sequenze più lunghe adattandole a contesti originariamente addestrati più piccoli. Tuttavia, questo adattamento introduce degradazione nella comprensione della posizione del token. I modelli rimangono altamente capaci a contesti più lunghi ma mostrano precisione ridotta per recupero informazioni e ragionamento a lungo raggio rispetto alle performance su contesti più brevi.

**Il Principio della Progressive Disclosure**
La progressive disclosure gestisce il contesto efficientemente caricando informazioni solo quando necessario. All'avvio, gli agenti caricano solo nomi skill e descrizioni—sufficiente per sapere quando una skill potrebbe essere rilevante. Il contenuto completo carica solo quando una skill è attivata per task specifici.

Questo approccio mantiene gli agenti veloci mentre dà loro accesso a più contesto su richiesta. Il principio si applica a livelli multipli: selezione skill, caricamento documenti e anche recupero risultati tool.

### Qualità del Contesto vs Quantità del Contesto

L'assunzione che finestre di contesto più grandi risolvano problemi di memoria è stata empiricamente smentita. Il context engineering significa trovare il più piccolo set possibile di token ad alto segnale che massimizzano la probabilità di risultati desiderati.

Diversi fattori creano pressione per l'efficienza del contesto. Il costo di processamento cresce sproporzionatamente con la lunghezza del contesto—non solo il doppio del costo per il doppio dei token, ma esponenzialmente di più in tempo e risorse di calcolo. Le performance del modello degradano oltre certe lunghezze di contesto anche quando la finestra tecnicamente supporta più token. Input lunghi rimangono costosi anche con prefix caching.

Il principio guida è l'informatività sopra l'esaustività. Includi ciò che conta per la decisione in mano, escludi ciò che non conta, e progetta sistemi che possono accedere a informazioni addizionali su richiesta.

### Contesto come Risorsa Finita

Il contesto deve essere trattato come una risorsa finita con ritorni marginali decrescenti. Come gli umani con memoria di lavoro limitata, i modelli linguistici hanno un budget di attenzione a cui attingere quando fanno parsing di grandi volumi di contesto.

Ogni nuovo token introdotto esaurisce questo budget di una certa quantità. Questo crea il bisogno di un'attenta curatela dei token disponibili. Il problema ingegneristico è ottimizzare l'utilità contro i vincoli intrinseci.

Il context engineering è iterativo e la fase di curatela accade ogni volta che decidi cosa passare al modello. Non è un esercizio di scrittura prompt una tantum ma una disciplina continua di gestione del contesto.

## Guida Pratica

### Accesso Basato su File-System

Gli agenti con accesso al filesystem possono usare la progressive disclosure naturalmente. Memorizza materiali di riferimento, documentazione e dati esternamente. Carica file solo quando necessario usando operazioni filesystem standard. Questo pattern evita di riempire il contesto con informazioni che potrebbero non essere rilevanti.

Il file system stesso fornisce struttura che gli agenti possono navigare. Le dimensioni dei file suggeriscono complessità; le convenzioni di naming suggeriscono lo scopo; i timestamp servono come proxy per la rilevanza. I metadati dei riferimenti file forniscono un meccanismo per raffinare efficientemente il comportamento.

### Strategie Ibride

Gli agenti più efficaci impiegano strategie ibride. Pre-carica un po' di contesto per velocità (come file CLAUDE.md o regole progetto), ma abilita l'esplorazione autonoma per contesto addizionale quando necessario. Il confine decisionale dipende dalle caratteristiche del task e dalle dinamiche del contesto.

Per contesti con contenuto meno dinamico, pre-caricare di più all'inizio ha senso. Per informazioni che cambiano rapidamente o altamente specifiche, il caricamento just-in-time evita contesto stantio.

### Budgeting del Contesto

Progetta con budget di contesto espliciti in mente. Conosci il limite di contesto effettivo per il tuo modello e task. Monitora l'uso del contesto durante lo sviluppo. Implementa trigger di compattazione a soglie appropriate. Progetta sistemi assumendo che il contesto degraderà piuttosto che sperare che non lo faccia.

Un effective context budgeting richiede di comprendere non solo i conteggi grezzi dei token ma anche i pattern di distribuzione dell'attenzione. Il centro del contesto riceve meno attenzione dell'inizio e della fine. Piazza informazioni critiche in posizioni favorite dall'attenzione.

## Esempi

**Esempio 1: Organizzare Prompt di Sistema**

```markdown
<BACKGROUND_INFORMATION>
You are a Python expert helping a development team.
Current project: Data processing pipeline in Python 3.9+
</BACKGROUND_INFORMATION>

<INSTRUCTIONS>
- Write clean, idiomatic Python code
- Include type hints for function signatures
- Add docstrings for public functions
- Follow PEP 8 style guidelines
</INSTRUCTIONS>

<TOOL_GUIDANCE>
Use bash for shell operations, python for code tasks.
File operations should use pathlib for cross-platform compatibility.
</TOOL_GUIDANCE>

<OUTPUT_DESCRIPTION>
Provide code blocks with syntax highlighting.
Explain non-obvious decisions in comments.
</OUTPUT_DESCRIPTION>
```

**Esempio 2: Caricamento Documenti Progressivo**

```markdown
# Instead of loading all documentation at once:

# Step 1: Load summary

docs/api_summary.md # Lightweight overview

# Step 2: Load specific section as needed

docs/api/endpoints.md # Only when API calls needed
docs/api/authentication.md # Only when auth context needed
```

## Linee Guida

1. Tratta il contesto come una risorsa finita con ritorni decrescenti
2. Piazza informazioni critiche in posizioni favorite dall'attenzione (inizio e fine)
3. Usa progressive disclosure per differire il caricamento finché necessario
4. Organizza prompt di sistema con confini di sezione chiari
5. Monitora l'uso del contesto durante lo sviluppo
6. Implementa trigger di compattazione al 70-80% di utilizzo
7. Progetta per la degradazione del contesto piuttosto che sperare di evitarla
8. Preferisci contesto più piccolo ad alto segnale rispetto a contesto più grande a basso segnale

## Integrazione

Questa skill fornisce contesto fondamentale su cui tutte le altre skill costruiscono. Dovrebbe essere studiata prima di esplorare:

- **context-degradation** - Comprendere come il contesto fallisce
- **context-optimization** - Tecniche per estendere la capacità del contesto
- **multi-agent-patterns** - Come l'isolamento del contesto abilita sistemi multi-agente
- **tool-design** - Come le definizioni dei tool interagiscono con il contesto

## Riferimenti

Riferimento interno:

- [Context Components Reference](./references/context-components.md) - Riferimento tecnico dettagliato
- [Context Fundamentals Reference](./references/fundamentals.md) - Concetti base

Skill correlate in questa collezione:

- context-degradation - Comprendere pattern di fallimento contesto
- context-optimization - Tecniche per uso efficiente del contesto

Risorse esterne:

- Research on transformer attention mechanisms
- Production engineering guides from leading AI labs
- Framework documentation on context window management
