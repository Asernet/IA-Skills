---
name: bdi-mental-states
description: Usa questa skill per modellare stati mentali di agenti, architetture BDI (Belief-Desire-Intention), o integrazione AI neuro-simbolica.
---

# Modellazione Stati Mentali BDI

Trasforma il contesto RDF esterno in stati mentali dell'agente (credenze, desideri, intenzioni - Belief, Desire, Intention) utilizzando pattern ontologici BDI formali. Questa skill abilita gli agenti a ragionare sul contesto attraverso l'architettura cognitiva, supportando ragionamento deliberativo, spiegabilità e interoperabilità semantica all'interno di sistemi multi-agente.

## Quando Attivare

Attiva questa skill quando:

- Processi contesto RDF esterno in credenze dell'agente sugli stati del mondo
- Modelli agenzia razionale con cicli di percezione, deliberazione e azione
- Abiliti la spiegabilità attraverso catene di ragionamento tracciabili
- Implementi framework BDI (SEMAS, JADE, JADEX)
- Aumenti gli LLM con strutture cognitive formali (Logic Augmented Generation)
- Coordini stati mentali attraverso piattaforme multi-agente
- Tracci l'evoluzione temporale di credenze, desideri e intenzioni
- Colleghi stati motivazionali a piani d'azione

## Concetti Chiave

### Architettura della Realtà Mentale

**Stati Mentali (Endurants)**: Attributi cognitivi persistenti

- `Belief` (Credenza): Ciò che l'agente crede essere vero sul mondo
- `Desire` (Desiderio): Ciò che l'agente desidera realizzare
- `Intention` (Intenzione): Ciò che l'agente si impegna a raggiungere

**Processi Mentali (Perdurants)**: Eventi che modificano gli stati mentali

- `BeliefProcess`: Formazione/aggiornamento credenze dalla percezione
- `DesireProcess`: Generazione desideri dalle credenze
- `IntentionProcess`: Impegno verso desideri come intenzioni azionabili

### Pattern Catena Cognitiva

```turtle
:Belief_store_open a bdi:Belief ;
    rdfs:comment "Store is open" ;
    bdi:motivates :Desire_buy_groceries .

:Desire_buy_groceries a bdi:Desire ;
    rdfs:comment "I desire to buy groceries" ;
    bdi:isMotivatedBy :Belief_store_open .

:Intention_go_shopping a bdi:Intention ;
    rdfs:comment "I will buy groceries" ;
    bdi:fulfils :Desire_buy_groceries ;
    bdi:isSupportedBy :Belief_store_open ;
    bdi:specifies :Plan_shopping .
```

### Grounding Stato del Mondo

Gli stati mentali fanno riferimento a configurazioni strutturate dell'ambiente:

```turtle
:Agent_A a bdi:Agent ;
    bdi:perceives :WorldState_WS1 ;
    bdi:hasMentalState :Belief_B1 .

:WorldState_WS1 a bdi:WorldState ;
    rdfs:comment "Meeting scheduled at 10am in Room 5" ;
    bdi:atTime :TimeInstant_10am .

:Belief_B1 a bdi:Belief ;
    bdi:refersTo :WorldState_WS1 .
```

### Pianificazione Orientata agli Obiettivi

Le intenzioni specificano piani che indirizzano obiettivi attraverso sequenze di task:

```turtle
:Intention_I1 bdi:specifies :Plan_P1 .

:Plan_P1 a bdi:Plan ;
    bdi:addresses :Goal_G1 ;
    bdi:beginsWith :Task_T1 ;
    bdi:endsWith :Task_T3 .

:Task_T1 bdi:precedes :Task_T2 .
:Task_T2 bdi:precedes :Task_T3 .
```

## Paradigma T2B2T

Triples-to-Beliefs-to-Triples implementa un flusso bidirezionale tra knowledge graph RDF e stati mentali interni:

**Fase 1: Triples-to-Beliefs**

```turtle
# External RDF context triggers belief formation
:WorldState_notification a bdi:WorldState ;
    rdfs:comment "Push notification: Payment request $250" ;
    bdi:triggers :BeliefProcess_BP1 .

:BeliefProcess_BP1 a bdi:BeliefProcess ;
    bdi:generates :Belief_payment_request .
```

**Fase 2: Beliefs-to-Triples**

```turtle
# Mental deliberation produces new RDF output
:Intention_pay a bdi:Intention ;
    bdi:specifies :Plan_payment .

:PlanExecution_PE1 a bdi:PlanExecution ;
    bdi:satisfies :Plan_payment ;
    bdi:bringsAbout :WorldState_payment_complete .
```

## Selezione Notazione per Livello

| Livello C4   | Notazione | Rappresentazione Stato Mentale                       |
| ------------ | --------- | ---------------------------------------------------- |
| L1 Context   | ArchiMate | Confini agente, fonti percezione esterne             |
| L2 Container | ArchiMate | Motore ragionamento BDI, belief store, plan executor |
| L3 Component | UML       | Gestori stati mentali, gestori processi              |
| L4 Code      | UML/RDF   | Classi Belief/Desire/Intention, istanze ontologia    |

## Giustificazione e Spiegabilità

Le entità mentali si collegano a evidenze di supporto per un ragionamento tracciabile:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:isJustifiedBy :Justification_J1 .

:Justification_J1 a bdi:Justification ;
    rdfs:comment "Official announcement received via email" .

:Intention_I1 a bdi:Intention ;
    bdi:isJustifiedBy :Justification_J2 .

:Justification_J2 a bdi:Justification ;
    rdfs:comment "Location precondition satisfied" .
```

## Dimensioni Temporali

Gli stati mentali persistono per periodi di tempo limitati:

```turtle
:Belief_B1 a bdi:Belief ;
    bdi:hasValidity :TimeInterval_TI1 .

:TimeInterval_TI1 a bdi:TimeInterval ;
    bdi:hasStartTime :TimeInstant_9am ;
    bdi:hasEndTime :TimeInstant_11am .
```

Interroga stati mentali attivi in momenti specifici:

```sparql
SELECT ?mentalState WHERE {
    ?mentalState bdi:hasValidity ?interval .
    ?interval bdi:hasStartTime ?start ;
               bdi:hasEndTime ?end .
    FILTER(?start <= "2025-01-04T10:00:00"^^xsd:dateTime &&
           ?end >= "2025-01-04T10:00:00"^^xsd:dateTime)
}
```

## Entità Mentali Composizionali

Entità mentali complesse si decompongono in parti costituenti per aggiornamenti selettivi:

```turtle
:Belief_meeting a bdi:Belief ;
    rdfs:comment "Meeting at 10am in Room 5" ;
    bdi:hasPart :Belief_meeting_time , :Belief_meeting_location .

# Update only location component
:BeliefProcess_update a bdi:BeliefProcess ;
    bdi:modifies :Belief_meeting_location .
```

## Pattern di Integrazione

### Logic Augmented Generation (LAG)

Aumenta output LLM con vincoli ontologici:

```python
def augment_llm_with_bdi_ontology(prompt, ontology_graph):
    ontology_context = serialize_ontology(ontology_graph, format='turtle')
    augmented_prompt = f"{ontology_context}\n\n{prompt}"

    response = llm.generate(augmented_prompt)
    triples = extract_rdf_triples(response)

    is_consistent = validate_triples(triples, ontology_graph)
    return triples if is_consistent else retry_with_feedback()
```

### Traduzione Regole SEMAS

Mappa ontologia BDI a regole di produzione eseguibili:

```prolog
% Belief triggers desire formation
[HEAD: belief(agent_a, store_open)] /
[CONDITIONALS: time(weekday_afternoon)] »
[TAIL: generate_desire(agent_a, buy_groceries)].

% Desire triggers intention commitment
[HEAD: desire(agent_a, buy_groceries)] /
[CONDITIONALS: belief(agent_a, has_shopping_list)] »
[TAIL: commit_intention(agent_a, buy_groceries)].
```

## Linee Guida

1. Modella gli stati del mondo come configurazioni indipendenti dalle prospettive dell'agente, fornendo substrato referenziale per gli stati mentali.

2. Distingui endurants (stati mentali persistenti) da perdurants (processi mentali temporali), allineandosi con l'ontologia DOLCE.

3. Tratta gli obiettivi come descrizioni piuttosto che stati mentali, mantenendo la separazione tra livelli cognitivi e di pianificazione.

4. Usa relazioni `hasPart` per strutture meronimiche che abilitano aggiornamenti selettivi delle credenze.

5. Associa ogni entità mentale con costrutti temporali via `atTime` o `hasValidity`.

6. Usa coppie di proprietà bidirezionali (`motivates`/`isMotivatedBy`, `generates`/`isGeneratedBy`) per querying flessibile.

7. Collega entità mentali a istanze `Justification` per spiegabilità e fiducia.

8. Implementa T2B2T attraverso: (1) traduci RDF in credenze, (2) esegui ragionamento BDI, (3) proietta stati mentali indietro in RDF.

9. Definisci restrizioni esistenziali sui processi mentali (es. `BeliefProcess ⊑ ∃generates.Belief`).

10. Riutilizza ODP consolidati (EventCore, Situation, TimeIndexedSituation, BasicPlan, Provenance) per interoperabilità.

## Domande di Competenza

Valida l'implementazione contro queste query SPARQL:

```sparql
# CQ1: What beliefs motivated formation of a given desire?
SELECT ?belief WHERE {
    :Desire_D1 bdi:isMotivatedBy ?belief .
}

# CQ2: Which desire does a particular intention fulfill?
SELECT ?desire WHERE {
    :Intention_I1 bdi:fulfils ?desire .
}

# CQ3: Which mental process generated a belief?
SELECT ?process WHERE {
    ?process bdi:generates :Belief_B1 .
}

# CQ4: What is the ordered sequence of tasks in a plan?
SELECT ?task ?nextTask WHERE {
    :Plan_P1 bdi:hasComponent ?task .
    OPTIONAL { ?task bdi:precedes ?nextTask }
} ORDER BY ?task
```

## Anti-Pattern

1. **Confondere stati mentali con stati del mondo**: Gli stati mentali fanno riferimento a stati del mondo, non sono stati del mondo essi stessi.

2. **Limiti temporali mancanti**: Ogni stato mentale dovrebbe avere intervalli di validità per ragionamento diacronico.

3. **Strutture di credenza piatte**: Usa modellazione composizionale con `hasPart` per credenze complesse.

4. **Giustificazioni implicite**: Collega sempre le entità mentali a istanze di giustificazione esplicite.

5. **Mappatura diretta intenzione-azione**: Le intenzioni specificano piani che contengono task; le azioni eseguono task.

## Integrazione

- **Processamento RDF**: Applica dopo il parsing del contesto RDF esterno per costruire rappresentazioni cognitive
- **Ragionamento Semantico**: Combina con ragionamento ontologico per inferire relazioni implicite di stati mentali
- **Comunicazione Multi-Agente**: Integra con FIPA ACL per condivisione credenze cross-platform
- **Contesto Temporale**: Coordina con ragionamento temporale per evoluzione stati mentali
- **Explainable AI**: Alimenta sistemi di spiegazione tracciando percezione attraverso deliberazione fino all'azione
- **Neuro-Symbolic AI**: Applica in pipeline LAG per vincolare output LLM con strutture cognitive

## Riferimenti

Vedi cartella `references/` per documentazione dettagliata:

- `bdi-ontology-core.md` - Core ontology patterns and class definitions
- `rdf-examples.md` - Complete RDF/Turtle examples
- `sparql-competency.md` - Full competency question SPARQL queries
- `framework-integration.md` - SEMAS, JADE, LAG integration patterns

Fonti primarie:

- Zuppiroli et al. "The Belief-Desire-Intention Ontology" (2025)
- Rao & Georgeff "BDI agents: From theory to practice" (1995)
- Bratman "Intention, plans, and practical reason" (1987)
