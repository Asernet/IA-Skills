---
name: tool-design
description: Usa questa skill per progettare tool per agenti, definire interfacce o consolidare strumenti esistenti.
---

# Design Tool per Agenti

I tool sono il meccanismo primario attraverso cui gli agenti interagiscono con il mondo. Definiscono il contratto tra sistemi deterministici e agenti non-deterministici. A differenza delle API software tradizionali progettate per sviluppatori, le API tool devono essere progettate per modelli linguistici che ragionano su intenti, inferiscono valori parametri e generano chiamate da richieste linguaggio naturale. Un cattivo design tool crea modalità di fallimento che nessuna quantità di prompt engineering può fixare. Un design tool efficace segue principi specifici che tengono conto di come gli agenti percepiscono e usano i tool.

## Quando Attivare

Attiva questa skill quando:

- Crei nuovi tool per sistemi agente
- Debugghi fallimenti o misuso relativi ai tool
- Ottimizzi set tool esistenti per performance agente migliori
- Progetti API tool da zero
- Valuti tool terze parti per integrazione agente
- Standardizzi convenzioni tool attraverso una codebase

## Concetti Core

I tool sono contratti tra sistemi deterministici e agenti non-deterministici. Il principio di consolidamento afferma che se un ingegnere umano non può dire definitivamente quale tool dovrebbe essere usato in una data situazione, non ci si può aspettare che un agente faccia meglio. Descrizioni tool efficaci sono prompt engineering che forma il comportamento agente.

Principi chiave includono: descrizioni chiare che rispondono a cosa, quando e cosa ritorna; formati risposta che bilanciano completezza ed efficienza token; messaggi errore che abilitano recupero; e convenzioni consistenti che riducono carico cognitivo.

## Argomenti Dettagliati

### L'Interfaccia Tool-Agente

**Tool come Contratti**
I tool sono contratti tra sistemi deterministici e agenti non-deterministici. Quando gli umani chiamano API, capiscono il contratto e fanno richieste appropriate. Gli agenti devono inferire il contratto da descrizioni e generare chiamate che combaciano formati attesi.

Questa differenza fondamentale richiede di ripensare il design API. Il contratto deve essere non ambiguo, gli esempi devono illustrare pattern attesi, e i messaggi errore devono guidare la correzione. Ogni ambiguità nelle definizioni tool diventa una potenziale modalità di fallimento.

**Descrizione Tool come Prompt**
Le descrizioni tool sono caricate nel contesto agente e collettivamente guidano il comportamento. Le descrizioni non sono solo documentazione—sono prompt engineering che forma come gli agenti ragionano sull'uso tool.

Descrizioni povere come "Cerca nel database" con nomi parametri criptici costringono gli agenti a indovinare. Descrizioni ottimizzate includono contesto d'uso, esempi e default. La descrizione risponde: cosa fa il tool, quando usarlo e cosa produce.

**Namespacing e Organizzazione**
Mentre le collezioni tool crescono, l'organizzazione diventa critica. Namespacing raggruppa tool correlati sotto prefissi comuni, aiutando gli agenti a selezionare tool appropriati al momento giusto.

### Il Principio di Consolidamento

**Tool Comprensivi Singoli**
Il principio di consolidamento afferma che se un ingegnere umano non può dire definitivamente quale tool dovrebbe essere usato in una data situazione, non ci si può aspettare che un agente faccia meglio. Questo porta a una preferenza per singoli tool comprensivi su tool stretti multipli.

Invece di implementare list_users, list_events, e create_event, implementa schedule_event che trova disponibilità e pianifica. Il tool comprensivo gestisce l'intero workflow internamente piuttosto che richiedere agli agenti di incatenare chiamate multiple.

**Perché il Consolidamento Funziona**
Il consolidamento riduce consumo token eliminando descrizioni ridondanti. Elimina ambiguità avendo un tool che copre ogni workflow. Riduce complessità selezione tool restringendo il set tool effettivo.

### Riduzione Architettonica

Il principio di consolidamento, portato al suo estremo logico, porta alla riduzione architettonica: rimuovere la maggior parte dei tool specializzati in favore di capacità primitive, general-purpose. Prove di produzione mostrano che questo approccio può sovraperformare architetture multi-tool sofisticate.

**Il Pattern Agente File System**
Invece di costruire tool personalizzati per esplorazione dati, lookup schema e validazione query, fornisci accesso diretto al file system attraverso un singolo tool esecuzione comando. L'agente usa utility Unix standard (grep, cat, find, ls) per esplorare, capire e operare sul tuo sistema.

**Smetti di Vincolare il Ragionamento**
Un anti-pattern comune è costruire tool per "proteggere" il modello dalla complessità. Pre-filtrare contesto, vincolare opzioni, avvolgere interazioni in logica validazione. Questi guardrail spesso diventano passività mentre i modelli migliorano.

La domanda da fare: i tuoi tool stanno abilitando nuove capacità, o stanno vincolando ragionamento che il modello potrebbe gestire da solo?

### Tool Description Engineering

**Struttura Descrizione**
Descrizioni tool efficaci rispondono a quattro domande:

Cosa fa il tool? Descrizione chiara, specifica di funzionalità. Evita linguaggio vago come "aiuta con" o "può essere usato per." Dichiara esattamente cosa compie il tool.

Quando dovrebbe essere usato? Trigger e contesti specifici. Includi sia trigger diretti ("Utente chiede prezzi") e segnali indiretti ("Bisogno tassi mercati correnti").

Quali input accetta? Descrizioni parametri con tipi, vincoli e default. Spiega cosa controlla ogni parametro.

Cosa ritorna? Formato output e struttura. Includi esempi di risposte di successo e condizioni errore.

**Selezione Parametro Default**
I default dovrebbero riflettere casi d'uso comuni. Riducono carico agente eliminando specifica parametri non necessaria. Prevengono errori da parametri omessi.

### Ottimizzazione Formato Risposta

La dimensione risposta tool impatta significativamente l'uso contesto. Implementare opzioni formato risposta dà agli agenti controllo su verbosità.

Formato conciso ritorna solo campi essenziali, appropriato per conferma o informazioni base. Formato dettagliato ritorna oggetti completi con tutti i campi, appropriato quando contesto pieno è necessario per decisioni.

### Design Messaggio Errore

Messaggi errore servono due audience: sviluppatori che debuggano problemi e agenti che recuperano da fallimenti. Per agenti, i messaggi errore devono essere azionabili. Devono dire all'agente cosa è andato storto e come correggerlo.

Progetta messaggi errore che abilitano recupero. Per errori ritentabili, includi guida retry. Per errori input, includi formato corretto. Per dati mancanti, includi cosa serve.

### Requisiti Naming Tool MCP

Quando usi tool MCP (Model Context Protocol), usa sempre nomi tool completamente qualificati per evitare errori "tool not found".

Formato: `ServerName:tool_name`

```python
# Corretto: Nomi completamente qualificati
"Usa il tool BigQuery:bigquery_schema per recuperare schemi tabella."
"Usa il tool GitHub:create_issue per creare issue."

# Scorretto: Nomi non qualificati
"Usa il tool bigquery_schema..."  # Può fallire con server multipli
```

Senza il prefisso server, gli agenti potrebbero fallire nel localizzare i tool, specialmente quando server MCP multipli sono disponibili. Stabilisci convenzioni naming che includono contesto server in tutti i riferimenti tool.

### Usare Agenti per Ottimizzare Tool

Claude può ottimizzare i propri tool. Quando dato un tool e modalità fallimento osservate, diagnostica problemi e suggerisce miglioramenti.

**Il Pattern Agente Tool-Testing**:

```python
def optimize_tool_description(tool_spec, failure_examples):
    """
    Usa un agente per analizzare fallimenti tool e migliorare descrizioni.
    """
    prompt = f"""
    Analizza questa specifica tool e i fallimenti osservati.

    Tool: {tool_spec}

    Identifica:
    1. Perché gli agenti stanno fallendo con questo tool
    2. Quale informazione manca dalla descrizione
    3. Quali ambiguità causano uso scorretto

    Proponi una descrizione tool migliorata che indirizza questi problemi.
    """

    return get_agent_response(prompt)
```

## Guida Pratica

### Anti-Pattern da Evitare

Descrizioni vaghe: "Cerca nel database per informazioni cliente" lascia troppe domande senza risposta.

Nomi parametri criptici: Parametri nominati x, val, o param1 costringono agenti a indovinare significato.

Gestione errore mancante: Tool che falliscono con errori generici non forniscono guida recupero.

Naming inconsistente: Usare id in alcuni tool, identifier in altri, e customer_id in alcuni crea confusione.

### Framework Selezione Tool

Quando progetti collezioni tool:

1. Identifica workflow distinti che gli agenti devono compiere
2. Raggruppa azioni correlate in tool comprensivi
3. Assicura che ogni tool abbia uno scopo chiaro, non ambiguo
4. Documenta casi errore e percorsi recupero
5. Testa con interazioni agente reali

## Linee Guida

1. Scrivi descrizioni che rispondono a cosa, quando e cosa ritorna
2. Usa consolidamento per ridurre ambiguità
3. Implementa opzioni formato risposta per efficienza token
4. Progetta messaggi errore per recupero agente
5. Stabilisci e segui convenzioni naming consistenti
6. Limita conteggio tool e usa namespacing per organizzazione
7. Testa design tool con interazioni agente reali
8. Itera basato su modalità fallimento osservate
9. Chiediti se ogni tool abilita o vincola il modello
10. Preferisci tool primitivi, general-purpose su wrapper specializzati
11. Investi in qualità documentazione su sofisticazione tooling
12. Costruisci architetture minime che beneficiano da miglioramenti modello

## Integrazione

Questa skill si connette a:

- context-fundamentals - Come i tool interagiscono col contesto
- multi-agent-patterns - Tool specializzati per agente
- evaluation - Valutare efficacia tool
