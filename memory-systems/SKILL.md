---
name: memory-systems
description: Usa questa skill per implementare memoria per agenti, persistenza tra sessioni o knowledge graph.
---

# Design di Sistemi di Memoria

La memoria fornisce il layer di persistenza che permette agli agenti di mantenere continuità attraverso le sessioni e ragionare sulla conoscenza accumulata. Gli agenti semplici si basano interamente sul contesto per la memoria, perdendo tutto lo stato quando le sessioni finiscono. Gli agenti sofisticati implementano architetture di memoria a strati che bilanciano bisogni di contesto immediato con ritenzione conoscenza a lungo termine. L'evoluzione da vector store a knowledge graph a temporal knowledge graph rappresenta un crescente investimento nella memoria strutturata per migliorato retrieval e ragionamento.

## Quando Attivare

Attiva questa skill quando:

- Costruisci agenti che devono persistere attraverso le sessioni
- Hai bisogno di mantenere consistenza entità attraverso conversazioni
- Implementi ragionamento su conoscenza accumulata
- Progetti sistemi che imparano da interazioni passate
- Crei knowledge base che crescono nel tempo
- Costruisci sistemi temporal-aware che tracciano cambiamenti di stato

## Concetti Chiave

La memoria esiste su uno spettro dal contesto immediato allo storage permanente. A un estremo, la memoria di lavoro nella finestra di contesto fornisce accesso a latenza zero ma svanisce quando le sessioni finiscono. All'altro estremo, lo storage permanente persiste indefinitamente ma richiede retrieval per entrare nel contesto.

I vector store semplici mancano di struttura relazionale e temporale. I knowledge graph preservano le relazioni per il ragionamento. I temporal knowledge graph aggiungono periodi di validità per query time-aware. Le scelte di implementazione dipendono dalla complessità della query, vincoli infrastruttura e requisiti di accuratezza.

## Argomenti Dettagliati

### Fondamenti Architettura Memoria

**Lo Spettro Contesto-Memoria**
Architetture efficaci usano layer multipli lungo questo spettro.

Lo spettro include memoria di lavoro (finestra contesto, latenza zero, volatile), memoria a breve termine (session-persistent, ricercabile, volatile), memoria a lungo termine (cross-session persistent, strutturata, semi-permanente), e memoria permanente (archivio, interrogabile, permanente). Ogni layer ha diverse caratteristiche di latenza, capacità e persistenza.

**Perché i Vector Store Semplici Non Bastano**
Il Vector RAG fornisce retrieval semantico incorporando query e documenti in uno spazio di embedding condiviso. La ricerca di similarità recupera i documenti più semanticamente simili. Questo funziona bene per il recupero documenti ma manca di struttura per la memoria agente.

I vector store perdono informazioni di relazione. Se un agente impara che "Cliente X ha acquistato Prodotto Y in Data Z", un vector store può recuperare questo fatto se chiesto direttamente. Ma non può rispondere "Quali prodotti hanno comprato anche i clienti che hanno acquistato Prodotto Y?" perché la struttura di relazione non è preservata.

I vector store faticano anche con la validità temporale. I fatti cambiano nel tempo, ma i vector store non forniscono meccanismo per distinguere "fatto corrente" da "fatto obsoleto" eccetto attraverso metadati espliciti e filtraggio.

**Il Passaggio a Memoria Basata su Grafo**
I knowledge graph preservano relazioni tra entità. Invece di chunk di documenti isolati, i grafi codificano che Entità A ha Relazione R con Entità B. Questo abilita query che attraversano relazioni piuttosto che solo similarità.

I temporal knowledge graph aggiungono periodi di validità ai fatti. Ogni fatto ha un timestamp "valido da" e opzionalmente "valido fino a". Questo abilita query time-travel che ricostruiscono la conoscenza a punti specifici nel tempo.

### Architettura Layer Memoria

**Layer 1: Memoria di Lavoro**
La memoria di lavoro è la finestra di contesto stessa. Fornisce accesso immediato alle informazioni correntemente processate ma ha capacità limitata e svanisce quando le sessioni finiscono.

**Layer 2: Memoria a Breve Termine**
La memoria a breve termine persiste attraverso la sessione corrente ma non attraverso le sessioni. Fornisce capacità di ricerca e recupero senza la latenza dello storage permanente.

Implementazioni comuni includono database session-scoped che persistono fino a fine sessione, storage file-system in directory sessione designate, e cache in-memory con chiave ID sessione.

**Layer 3: Memoria a Lungo Termine**
La memoria a lungo termine persiste attraverso le sessioni indefinitamente. Abilita gli agenti ad imparare da interazioni passate e costruire conoscenza nel tempo.

Implementazioni variano da semplici store chiave-valore a sofisticati graph database. La scelta dipende dalla complessità delle relazioni da modellare.

**Layer 4: Memoria Entità**
La memoria entità traccia specificamente informazioni su entità (persone, luoghi, concetti, oggetti) per mantenere consistenza. Questo crea un knowledge graph rudimentale dove le entità sono riconosciute attraverso interazioni multiple.

Mantiene identità entità tracciando che "Mario Rossi" menzionato in una conversazione è la stessa persona in un'altra. Mantiene proprietà entità memorizzando fatti scoperti su entità nel tempo.

**Layer 5: Temporal Knowledge Graphs**
I temporal knowledge graph estendono la memoria entità con periodi di validità espliciti. I fatti non sono solo veri o falsi ma veri durante range di tempo specifici.

Abilita query come "Qual era l'indirizzo dell'utente in Data X?" recuperando fatti validi durante quel range di date. Previene clash di contesto quando informazioni obsolete contraddicono nuovi dati.

### Pattern Implementazione Memoria

**Pattern 1: File-System-as-Memory**
Il file system stesso può servire come layer di memoria. Questo pattern è semplice, richiede zero infrastruttura addizionale, e abilita lo stesso caricamento just-in-time che rende efficace il contesto basato su file-system.

Implementazione usa la gerarchia file system per organizzazione. Usa convenzioni di naming che trasmettono significato. Memorizza fatti in formati strutturati (JSON, YAML). Usa timestamp in nomi file o metadati per tracciamento temporale.

**Pattern 2: Vector RAG con Metadati**
Vector store arricchiti con metadati ricchi forniscono ricerca semantica con capacità di filtraggio.

Implementazione incorpora fatti o documenti e memorizza con metadati inclusi tag entità, validità temporale, attribuzione fonte e punteggi confidenza.

**Pattern 3: Knowledge Graph**
I knowledge graph modellano esplicitamente entità e relazioni. Implementazione definisce tipi entità e tipi relazione, usa graph database o storage property graph.

**Pattern 4: Temporal Knowledge Graph**
Aggiunge periodi di validità, abilitando query time-travel.

### Pattern Retrieval Memoria

**Retrieval Semantico**
Recupera ricordi semanticamente simili alla query corrente usando ricerca similarità embedding.

**Retrieval Basato su Entità**
Recupera tutti i ricordi relativi a entità specifiche attraversando relazioni grafo.

**Retrieval Temporale**
Recupera ricordi validi a tempo specifico o entro range temporale usando filtri periodo validità.

### Consolidamento Memoria

Le memorie si accumulano nel tempo e richiedono consolidamento per prevenire crescita illimitata e rimuovere informazioni obsolete.

**Processo Consolidamento**
Identifica fatti obsoleti, unisci fatti correlati, aggiorna periodi validità, archivia o cancella fatti obsoleti, e ricostruisci indici.

## Guida Pratica

### Integrazione con Contesto

Le memorie devono integrarsi con sistemi di contesto per essere utili. Usa caricamento memoria just-in-time per recuperare ricordi rilevanti quando necessario. Usa iniezione strategica per piazzare ricordi in posizioni favorite dall'attenzione.

### Selezione Sistema Memoria

Scegli architettura memoria basata sui requisiti:

- Bisogni persistenza semplici: Memoria File-system
- Bisogni ricerca semantica: Vector RAG con metadati
- Bisogni ragionamento relazione: Knowledge graph
- Bisogni validità temporale: Temporal knowledge graph

## Esempi

**Esempio 1: Tracciamento Entità**

```python
# Track entity across conversations
def remember_entity(entity_id, properties):
    memory.store({
        "type": "entity",
        "id": entity_id,
        "properties": properties,
        "last_updated": now()
    })

def get_entity(entity_id):
    return memory.retrieve_entity(entity_id)
```

## Linee Guida

1. Combacia architettura memoria ai requisiti query
2. Implementa progressive disclosure per accesso memoria
3. Usa validità temporale per prevenire conflitti informazioni obsolete
4. Consolida memorie periodicamente per prevenire crescita illimitata
5. Progetta per fallimenti retrieval memoria graziosamente
6. Considera implicazioni privacy della memoria persistente
7. Implementa backup e recovery per memorie critiche
8. Monitora crescita memoria e performance nel tempo

## Integrazione

Questa skill costruisce su context-fundamentals. Si connette a:

- **multi-agent-patterns** - Memoria condivisa attraverso agenti
- **context-optimization** - Caricamento contesto basato su memoria
- **evaluation** - Valutare qualità memoria
