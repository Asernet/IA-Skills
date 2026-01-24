---
name: multi-agent-patterns
description: Usa questa skill per progettare sistemi multi-agente, pattern supervisore, swarm o coordinamento tra agenti.
---

# Pattern Architetturali Multi-Agente

Le architetture multi-agente distribuiscono il lavoro attraverso istanze multiple di modelli linguistici, ognuna con la propria finestra di contesto. Quando ben progettata, questa distribuzione abilita capacità oltre i limiti del singolo agente. Quando progettata male, introduce overhead di coordinamento che nega i benefici. L'insight critico è che i sub-agenti esistono primariamente per isolare il contesto, non per antropomorfizzare la divisione dei ruoli.

## Quando Attivare

Attiva questa skill quando:

- I limiti di contesto del singolo agente vincolano la complessità del task
- I task si decompongono naturalmente in subtask paralleli
- Diversi subtask richiedono diversi set di tool o prompt di sistema
- Costruisci sistemi che devono gestire domini multipli simultaneamente
- Scali capacità agente oltre i limiti del singolo contesto
- Progetti sistemi agente di produzione con componenti specializzati multipli

## Concetti Chiave

I sistemi multi-agente indirizzano le limitazioni di contesto del singolo agente attraverso la distribuzione. Esistono tre pattern dominanti: supervisore/orchestratore per controllo centralizzato, peer-to-peer/swarm per handoff flessibili, e gerarchico per astrazione a strati. Il principio di design critico è l'isolamento del contesto—i sub-agenti esistono primariamente per partizionare il contesto piuttosto che per simulare ruoli organizzativi.

Sistemi multi-agente efficaci richiedono protocolli di coordinamento espliciti, meccanismi di consenso che evitano la sicofania, e attenta attenzione alle modalità di fallimento inclusi colli di bottiglia, divergenza e propagazione errori.

## Argomenti Dettagliati

### Perché Architetture Multi-Agente

**Il Collo di Bottiglia del Contesto**
I singoli agenti affrontano soffitti intrinseci nella capacità di ragionamento, gestione contesto e coordinamento tool. Man mano che i task crescono in complessità, le finestre di contesto si riempiono con storia accumulata, documenti recuperati e output tool. La performance degrada secondo pattern prevedibili: l'effetto lost-in-middle, scarsità di attenzione e avvelenamento del contesto.

Le architetture multi-agente indirizzano queste limitazioni partizionando il lavoro attraverso finestre di contesto multiple. Ogni agente opera in un contesto pulito focalizzato sul suo subtask. I risultati si aggregano a un layer di coordinamento senza che alcun singolo contesto porti l'intero carico.

**La Realtà dell'Economia dei Token**
I sistemi multi-agente consumano significativamente più token degli approcci a singolo agente. Dati di produzione mostrano:

| Architettura            | Moltiplicatore Token | Caso d'Uso                      |
| ----------------------- | -------------------- | ------------------------------- |
| Chat agente singolo     | 1× baseline          | Query semplici                  |
| Agente singolo con tool | ~4× baseline         | Task con uso tool               |
| Sistema multi-agente    | ~15× baseline        | Ricerca complessa/coordinamento |

Ricerche sulla valutazione BrowseComp hanno trovato che tre fattori spiegano il 95% della varianza di performance: uso token (80% della varianza), numero di chiamate tool e scelta modello. Questo valida l'approccio multi-agente di distribuire lavoro attraverso agenti con finestre di contesto separate per aggiungere capacità di ragionamento parallelo.

Criticamente, aggiornare a modelli migliori spesso fornisce guadagni di performance maggiori che raddoppiare i budget di token. Claude Sonnet 4.5 ha mostrato guadagni maggiori che raddoppiare token su versioni Sonnet precedenti. La thinking mode di GPT-5.2 sovraperforma similarmente aumenti grezzi di token. Questo suggerisce che la selezione del modello e l'architettura multi-agente sono strategie complementari.

**L'Argomento Parallelizzazione**
Molti task contengono subtask parallelizzabili che un singolo agente deve eseguire sequenzialmente. Un task di ricerca potrebbe richiedere di cercare fonti indipendenti multiple, analizzare documenti diversi o confrontare approcci concorrenti. Un singolo agente processa questi sequenzialmente, accumulando contesto ad ogni passo.

Le architetture multi-agente assegnano ogni subtask a un agente dedicato con un contesto fresco. Tutti gli agenti lavorano simultaneamente, poi ritornano risultati a un coordinatore. Il tempo totale nel mondo reale si avvicina alla durata del subtask più lungo piuttosto che alla somma di tutti i subtask.

**L'Argomento Specializzazione**
Task diversi beneficiano da configurazioni agente diverse: diversi prompt di sistema, diversi set di tool, diverse strutture di contesto. Un agente general-purpose deve portare tutte le configurazioni possibili nel contesto. Agenti specializzati portano solo ciò di cui hanno bisogno.

Le architetture multi-agente abilitano la specializzazione senza esplosione combinatoria. Il coordinatore instrada ad agenti specializzati; ogni agente opera con contesto snello ottimizzato per il suo dominio.

### Pattern Architetturali

**Pattern 1: Supervisore/Orchestratore**
Il pattern supervisore piazza un agente centrale al controllo, delegando a specialisti e sintetizzando risultati. Il supervisore mantiene lo stato globale e la traiettoria, decompone obiettivi utente in subtask, e instrada a lavoratori appropriati.

```
User Query -> Supervisore -> [Specialista, Specialista, Specialista] -> Aggregazione -> Output Finale
```

Quando usare: Task complessi con chiara decomposizione, task che richiedono coordinamento attraverso domini, task dove la supervisione umana è importante.

Vantaggi: Stretto controllo sul workflow, più facile implementare interventi human-in-the-loop, assicura aderenza a piani predefiniti.

Svantaggi: Il contesto del supervisore diventa collo di bottiglia, fallimenti del supervisore si propagano a tutti i lavoratori, problema "gioco del telefono" dove i supervisori parafrasano risposte sub-agente scorrettamente.

**Il Problema e Soluzione Gioco del Telefono**
Benchmark LangGraph hanno trovato che architetture supervisore inizialmente performavano il 50% peggio delle versioni ottimizzate dovuto al problema "gioco del telefono" dove i supervisori parafrasano risposte sub-agente scorrettamente, perdendo fedeltà.

Il fix: implementa un tool `forward_message` permettendo ai sub-agenti di passare risposte direttamente agli utenti:

```python
def forward_message(message: str, to_user: bool = True):
    """
    Inoltra risposta sub-agente direttamente all'utente senza sintesi supervisore.

    Usa quando:
    - Risposta sub-agente è finale e completa
    - Sintesi supervisore perderebbe dettagli importanti
    - Formato risposta deve essere preservato esattamente
    """
    if to_user:
        return {"type": "direct_response", "content": message}
    return {"type": "supervisor_input", "content": message}
```

Con questo pattern, le architetture swarm sovraperformano leggermente i supervisori perché i sub-agenti rispondono direttamente agli utenti, eliminando errori di traduzione.

Nota implementazione: Implementa meccanismi di pass-through diretto permettendo ai sub-agenti di passare risposte direttamente agli utenti piuttosto che attraverso sintesi supervisore quando appropriato.

**Pattern 2: Peer-to-Peer/Swarm**
Il pattern peer-to-peer rimuove il controllo centrale, permettendo agli agenti di comunicare direttamente basandosi su protocolli predefiniti. Qualsiasi agente può trasferire il controllo a qualsiasi altro attraverso meccanismi di handoff espliciti.

```python
def transfer_to_agent_b():
    return agent_b  # Handoff via ritorno funzione
103:
104: agent_a = Agent(
105:     name="Agent A",
106:     functions=[transfer_to_agent_b]
107: )
```

Quando usare: Task che richiedono esplorazione flessibile, task dove la pianificazione rigida è controproducente, task con requisiti emergenti che sfidano la decomposizione upfront.

Vantaggi: Nessun singolo punto di fallimento, scala efficacemente per esplorazione breadth-first, abilita comportamenti di problem-solving emergenti.

Svantaggi: La complessità di coordinamento aumenta con il numero di agenti, rischio di divergenza senza state keeper centrale, richiede robusti vincoli di convergenza.

Nota implementazione: Definisci protocolli di handoff espliciti con passaggio stato. Assicura che gli agenti possano comunicare i loro bisogni di contesto agli agenti riceventi.

**Pattern 3: Gerarchico**
Le strutture gerarchiche organizzano gli agenti in strati di astrazione: strati strategici, di pianificazione e di esecuzione. Agenti strato strategico definiscono obiettivi e vincoli; agenti strato pianificazione rompono obiettivi in piani azionabili; agenti strato esecuzione compiono task atomici.

```
Strato Strategia (Definizione Obiettivi) -> Strato Pianificazione (Decomposizione Task) -> Strato Esecuzione (Task Atomici)
```

Quando usare: Progetti su larga scala con chiara struttura gerarchica, workflow enterprise con strati di gestione, task che richiedono sia pianificazione di alto livello che esecuzione dettagliata.

Vantaggi: Rispecchia strutture organizzative, chiara separazione delle responsabilità, abilita strutture di contesto diverse a livelli diversi.

Svantaggi: Overhead coordinamento tra strati, potenziale disallineamento tra strategia ed esecuzione, propagazione errori complessa.

### Isolamento Contesto come Principio di Design

Lo scopo primario delle architetture multi-agente è l'isolamento del contesto. Ogni sub-agente opera in una finestra di contesto pulita focalizzata sul suo subtask senza portare contesto accumulato da altri subtask.

**Meccanismi Isolamento**
Delega contesto completa: Per task complessi dove il sub-agente ha bisogno di comprensione completa, il pianificatore condivide il suo intero contesto. Il sub-agente ha i suoi tool e istruzioni ma riceve contesto completo per le sue decisioni.

Passaggio istruzioni: Per subtask semplici e ben definiti, il pianificatore crea istruzioni via chiamata funzione. Il sub-agente riceve solo le istruzioni necessarie per il suo task specifico.

Memoria file system: Per task complessi che richiedono stato condiviso, gli agenti leggono e scrivono su storage persistente. Il file system serve come meccanismo di coordinamento, evitando rigonfiamento contesto da passaggio stato condiviso.

**Trade-off Isolamento**
La delega contesto completa fornisce massima capacità ma sconfigge lo scopo dei sub-agenti. Il passaggio istruzioni mantiene isolamento ma limita la flessibilità del sub-agente. La memoria file system abilita stato condiviso senza passaggio contesto ma introduce latenza e sfide di consistenza.

La scelta giusta dipende dalla complessità del task, bisogni di coordinamento e latenza accettabile.

### Consenso e Coordinamento

**Il Problema del Voto**
Il voto a maggioranza semplice tratta le allucinazioni da modelli deboli come uguali al ragionamento da modelli forti. Senza intervento, le discussioni multi-agente degenerano in consenso su false premesse dovuto al bias intrinseco verso l'accordo.

**Voto Pesato**
Pesa i voti agente per confidenza o expertise. Agenti con confidenza più alta o expertise di dominio portano più peso nelle decisioni finali.

**Protocolli Dibattito**
I protocolli di dibattito richiedono agli agenti di criticare gli output reciproci su round multipli. La critica avversaria produce spesso accuratezza più alta su ragionamenti complessi rispetto al consenso collaborativo.

**Intervento Basato su Trigger**
Monitora interazioni multi-agente per marcatori comportamentali specifici. Trigger di stallo attivano quando le discussioni non fanno progresso. Trigger di sicofania rilevano quando gli agenti mimano le risposte reciproche senza ragionamento unico.

### Considerazioni Framework

Diversi framework implementano questi pattern con filosofie diverse. LangGraph usa macchine a stati basate su grafo con nodi ed edge espliciti. AutoGen usa pattern conversazionali/event-driven con GroupChat. CrewAI usa flussi di processo basati su ruoli con strutture crew gerarchiche.

## Guida Pratica

### Modalità Fallimento e Mitigazioni

**Fallimento: Collo di Bottiglia Supervisore**
Il supervisore accumula contesto da tutti i lavoratori, diventando suscettibile a saturazione e degradazione.

Mitigazione: Implementa vincoli schema output così i lavoratori ritornano solo riassunti distillati. Usa checkpointing per persistere stato supervisore senza portare intera cronologia.

**Fallimento: Overhead Coordinamento**
La comunicazione agente consuma token e introduce latenza. Coordinamento complesso può negare benefici parallelizzazione.

Mitigazione: Minimizza comunicazione attraverso protocolli handoff chiari. Batcha risultati dove possibile. Usa pattern comunicazione asincroni.

**Fallimento: Divergenza**
Agenti che perseguono obiettivi diversi senza coordinamento centrale possono andare alla deriva dagli obiettivi intesi.

Mitigazione: Definisci confini obiettivo chiari per ogni agente. Implementa controlli convergenza che verificano progresso verso obiettivi condivisi. Usa limiti time-to-live su esecuzione agente.

**Fallimento: Propagazione Errore**
Errori nell'output di un agente si propagano ad agenti a valle che consumano quell'output.

Mitigazione: Valida output agente prima di passare ai consumatori. Implementa logica retry con circuit breakers. Usa operazioni idempotenti dove possibile.

## Esempi

**Esempio 1: Architettura Team Ricerca**

```text
Supervisore
├── Ricercatore (ricerca web, recupero documenti)
├── Analizzatore (analisi dati, statistiche)
├── Fact-checker (verifica, validazione)
└── Scrittore (generazione report, formattazione)
```

**Esempio 2: Protocollo Handoff**

```python
def handle_customer_request(request):
    if request.type == "billing":
        return transfer_to(billing_agent)
    elif request.type == "technical":
        return transfer_to(technical_agent)
    elif request.type == "sales":
        return transfer_to(sales_agent)
    else:
        return handle_general(request)
```

## Linee Guida

1. Progetta per isolamento contesto come beneficio primario dei sistemi multi-agente
2. Scegli pattern architettura basato su bisogni coordinamento, non metafora organizzativa
3. Implementa protocolli handoff espliciti con passaggio stato
4. Usa voto pesato o protocolli dibattito per consenso
5. Monitora per colli di bottiglia supervisore e implementa checkpointing
6. Valida output prima di passare tra agenti
7. Imposta limiti time-to-live per prevenire loop infiniti
8. Testa scenari fallimento esplicitamente

## Integrazione

Questa skill costruisce su context-fundamentals e context-degradation. Si connette a:

- **memory-systems** - Gestione stato condiviso attraverso agenti
- **tool-design** - Specializzazione tool per agente
- **context-optimization** - Strategie partizionamento contesto

## Riferimenti

Riferimento interno:

- [Frameworks Reference](./references/frameworks.md) - Pattern implementazione framework dettagliati

Skill correlate in questa collezione:

- context-fundamentals - Basi contesto
- memory-systems - Memoria cross-agente
- context-optimization - Strategie partizionamento

Risorse esterne:

- [Documentazione LangGraph](https://langchain-ai.github.io/langgraph/) - Pattern multi-agente e gestione stato
- [Framework AutoGen](https://microsoft.github.io/autogen/) - GroupChat e pattern conversazionali
- [Documentazione CrewAI](https://docs.crewai.com/) - Processi agente gerarchici
- [Ricerca su Coordinamento Multi-Agente](https://arxiv.org/abs/2308.00352) - Survey di sistemi multi-agente
