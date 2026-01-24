---
name: evaluation
description: Usa questa skill per valutare le performance dell'agente, creare framework di test o metriche di qualità.
---

# Metodi di Valutazione per Sistemi Agente

La valutazione di sistemi agente richiede approcci diversi rispetto al software tradizionale o anche applicazioni standard di modelli linguistici. Gli agenti prendono decisioni dinamiche, sono non-deterministici tra le esecuzioni, e spesso mancano di risposte corrette singole. Una valutazione efficace deve tenere conto di queste caratteristiche fornendo feedback azionabile. Un robusto framework di valutazione abilita il miglioramento continuo, cattura le regressioni, e valida che le scelte di context engineering raggiungano gli effetti intesi.

## Quando Attivare

Attiva questa skill quando:

- Testi le performance dell'agente sistematicamente
- Validi scelte di context engineering
- Misuri miglioramenti nel tempo
- Catturi regressioni prima del deployment
- Costruisci quality gates per pipeline di agenti
- Confronti diverse configurazioni di agenti
- Valuti sistemi di produzione continuamente

## Concetti Chiave

La valutazione degli agenti richiede approcci focalizzati sui risultati che tengano conto del non-determinismo e dei percorsi validi multipli. Rubriche multi-dimensionali catturano vari aspetti di qualità: accuratezza fattuale, completezza, accuratezza citazioni, qualità fonti, ed efficienza tool. LLM-as-judge fornisce valutazione scalabile mentre la valutazione umana cattura i casi limite.

L'insight chiave è che gli agenti possono trovare percorsi alternativi agli obiettivi—la valutazione dovrebbe giudicare se raggiungono i risultati giusti seguendo processi ragionevoli.

**Driver di Performance: La Scoperta del 95%**
Ricerche sulla valutazione BrowseComp (che testa l'abilità di agenti di browsing di localizzare informazioni difficili da trovare) hanno trovato che tre fattori spiegano il 95% della varianza di performance:

| Fattore              | Varianza Spiegata | Implicazione                               |
| -------------------- | ----------------- | ------------------------------------------ |
| Uso token            | 80%               | Più token = performance migliore           |
| Numero chiamate tool | ~10%              | Più esplorazione aiuta                     |
| Scelta modello       | ~5%               | Modelli migliori moltiplicano l'efficienza |

Questa scoperta ha implicazioni significative per il design della valutazione:

- **I budget di token contano**: Valuta agenti con budget di token realistici, non risorse illimitate
- **Aggiornamenti modello battono aumenti token**: Aggiornare a Claude Sonnet 4.5 o GPT-5.2 fornisce guadagni maggiori che raddoppiare budget di token su versioni precedenti
- **Validazione multi-agente**: La scoperta valida architetture che distribuiscono lavoro attraverso agenti con finestre di contesto separate

## Argomenti Dettagliati

### Sfide di Valutazione

**Non-Determinismo e Percorsi Validi Multipli**
Gli agenti possono prendere percorsi validi completamente diversi per raggiungere gli obiettivi. Un agente potrebbe cercare tre fonti mentre un altro ne cerca dieci. Potrebbero usare tool diversi per trovare la stessa risposta. Valutazioni tradizionali che controllano passaggi specifici falliscono in questo contesto.

La soluzione è la valutazione focalizzata sui risultati che giudica se gli agenti raggiungono i risultati giusti mentre seguono processi ragionevoli.

**Fallimenti Dipendenti dal Contesto**
I fallimenti dell'agente spesso dipendono dal contesto in modi sottili. Un agente potrebbe avere successo su query semplici ma fallire su quelle complesse. Potrebbe funzionare bene con un set di tool ma fallire con un altro. I fallimenti possono emergere solo dopo interazione estesa quando il contesto si accumula.

La valutazione deve coprire un range di livelli di complessità e testare interazioni estese, non solo query isolate.

**Dimensioni di Qualità Composit**
La qualità dell'agente non è una singola dimensione. Include accuratezza fattuale, completezza, coerenza, efficienza tool e qualità di processo. Un agente potrebbe segnare alto sull'accuratezza ma basso in efficienza, o viceversa.

Le rubriche di valutazione devono catturare dimensioni multiple con pesatura appropriata per il caso d'uso.

### Design Rubrica Valutazione

**Rubrica Multi-Dimensionale**
Rubriche efficaci coprono dimensioni chiave con livelli descrittivi:

Accuratezza fattuale: Le affermazioni corrispondono alla verità di base (da eccellente a fallito)

Completezza: L'output copre gli aspetti richiesti (da eccellente a fallito)

Accuratezza citazioni: Le citazioni corrispondono alle fonti dichiarate (da eccellente a fallito)

Qualità fonti: Usa fonti primarie appropriate (da eccellente a fallito)

Efficienza tool: Usa i tool giusti un numero ragionevole di volte (da eccellente a fallito)

**Scoring Rubrica**
Converti valutazioni dimensione in punteggi numerici (0.0 a 1.0) con pesatura appropriata. Calcola punteggi complessivi pesati. Determina soglia di passaggio basata sui requisiti del caso d'uso.

### Metodologie di Valutazione

**LLM-as-Judge**
La valutazione basata su LLM scala a grandi set di test e fornisce giudizi consistenti. La chiave è progettare prompt di valutazione efficaci che catturano le dimensioni di interesse.

Fornisci descrizione chiara del task, output agente, verità di base (se disponibile), scala di valutazione con descrizioni livelli, e richiedi giudizio strutturato.

**Valutazione Umana**
La valutazione umana cattura ciò che l'automazione manca. Gli umani notano risposte allucinate su query inusuali, fallimenti di sistema e bias sottili che la valutazione automatizzata manca.

Una valutazione umana efficace copre casi limite, campiona sistematicamente, traccia pattern e fornisce comprensione contestuale.

**End-State Evaluation**
Per agenti che mutano stato persistente, la valutazione end-state si focalizza sul se lo stato finale corrisponde alle aspettative piuttosto che su come l'agente ci è arrivato.

### Design Test Set

**Selezione Campione**
Inizia con piccoli campioni durante lo sviluppo. Presto nello sviluppo dell'agente, i cambiamenti hanno impatti drammatici perché c'è abbondante frutta bassa. Piccoli set di test rivelano grandi effetti.

Campiona da pattern di utilizzo reale. Aggiungi casi limite noti. Assicura copertura attraverso livelli di complessità.

**Stratificazione Complessità**
I set di test dovrebbero spaziare livelli di complessità: semplice (singola chiamata tool), medio (multiple chiamate tool), complesso (molte chiamate tool, ambiguità significativa), e molto complesso (interazione estesa, ragionamento profondo).

### Valutazione Context Engineering

**Testare Strategie Contesto**
Le scelte di context engineering dovrebbero essere validate attraverso valutazione sistematica. Esegui agenti con diverse strategie di contesto sullo stesso set di test. Confronta punteggi qualità, uso token e metriche efficienza.

**Degradation Testing**
Testa come la degradazione del contesto influenza le performance eseguendo agenti a diverse dimensioni di contesto. Identifica dirupi di performance dove il contesto diventa problematico. Stabilisci limiti operativi sicuri.

### Valutazione Continua

**Pipeline Valutazione**
Costruisci pipeline di valutazione che girano automaticamente sui cambiamenti agente. Traccia risultati nel tempo. Confronta versioni per identificare miglioramenti o regressioni.

**Monitoraggio Produzione**
Traccia metriche di valutazione in produzione campionando interazioni e valutando casualmente. Imposta alert per cali di qualità. Mantieni dashboard per analisi trend.

## Guida Pratica

### Costruire Framework di Valutazione

1. Definisci dimensioni di qualità rilevanti per il tuo caso d'uso
2. Crea rubriche con descrizioni livelli chiare e azionabili
3. Costruisci set di test da pattern di utilizzo reale e casi limite
4. Implementa pipeline di valutazione automatizzate
5. Stabilisci metriche base prima di fare cambiamenti
6. Esegui valutazioni su tutti i cambiamenti significativi
7. Traccia metriche nel tempo per analisi trend
8. Supplementa valutazione automatizzata con revisione umana

### Evitare Trappole Valutazione

Overfitting a percorsi specifici: Valuta risultati, non passaggi specifici.
Ignorare casi limite: Includi scenari di test diversi.
Ossessione singola metrica: Usa rubriche multi-dimensionali.
Trascurare effetti contesto: Testa con dimensioni contesto realistiche.
Saltare valutazione umana: La valutazione automatizzata manca problemi sottili.

## Esempi

**Esempio 1: Valutazione Semplice**

```python
def evaluate_agent_response(response, expected):
    rubric = load_rubric()
    scores = {}
    for dimension, config in rubric.items():
        scores[dimension] = assess_dimension(response, expected, dimension)
    overall = weighted_average(scores, config["weights"])
    return {"passed": overall >= 0.7, "scores": scores}
```

**Esempio 2: Struttura Test Set**

I set di test dovrebbero spaziare livelli di complessità multipli per assicurare valutazione comprensiva:

```python
test_set = [
    {
        "name": "simple_lookup",
        "input": "What is the capital of France?",
        "expected": {"type": "fact", "answer": "Paris"},
        "complexity": "simple",
        "description": "Single tool call, factual lookup"
    },
    {
        "name": "medium_query",
        "input": "Compare the revenue of Apple and Microsoft last quarter",
        "complexity": "medium",
        "description": "Multiple tool calls, comparison logic"
    },
    {
        "name": "multi_step_reasoning",
        "input": "Analyze sales data from Q1-Q4 and create a summary report with trends",
        "complexity": "complex",
        "description": "Many tool calls, aggregation, analysis"
    },
    {
        "name": "research_synthesis",
        "input": "Research emerging AI technologies, evaluate their potential impact, and recommend adoption strategy",
        "complexity": "very_complex",
        "description": "Extended interaction, deep reasoning, synthesis"
    }
]
```

## Linee Guida

1. Usa rubriche multi-dimensionali, non singole metriche
2. Valuta risultati, non specifici percorsi di esecuzione
3. Copri livelli di complessità da semplice a complesso
4. Testa con dimensioni contesto e storici realistici
5. Esegui valutazioni continuamente, non solo prima del rilascio
6. Supplementa valutazione LLM con revisione umana
7. Traccia metriche nel tempo per rilevamento trend
8. Imposta chiare soglie pass/fail basate sul caso d'uso

## Integrazione

Questa skill si connette a tutte le altre skill come preoccupazione trasversale:

- **context-fundamentals** - Valutare uso contesto
- **context-degradation** - Rilevare degradazione
- **context-optimization** - Misurare efficacia ottimizzazione
- **multi-agent-patterns** - Valutare coordinamento
- **tool-design** - Valutare efficacia tool
- **memory-systems** - Valutare qualità memoria

## Riferimenti

Riferimento interno:

- [Metrics Reference](./references/metrics.md) - Metriche di valutazione dettagliate e implementazione

Riferimenti:

Skill interne:

- Tutte le altre skill si connettono alla valutazione per misurazione qualità

Risorse esterne:

- LLM evaluation benchmarks
- Agent evaluation research papers
- Production monitoring practices
