---
name: advanced-evaluation
description: Usa questa skill per implementare 'LLM-as-judge', confrontare output di modelli, creare rubriche di valutazione, mitigare bias di valutazione, o per scoring diretto e pipeline di quality assessment.
---

# Valutazione Avanzata

Questa skill copre tecniche di livello produttivo per valutare gli output degli LLM utilizzando gli LLM stessi come giudici (LLM-as-a-Judge). Sintetizza la ricerca da paper accademici, pratiche industriali ed esperienza pratica di implementazione in pattern azionabili per costruire sistemi di valutazione affidabili.

**Insight Chiave**: LLM-as-a-Judge non è una singola tecnica ma una famiglia di approcci, ognuno adatto a contesti di valutazione diversi. Scegliere l'approccio giusto e mitigare i bias noti è la competenza fondamentale che questa skill sviluppa.

## Quando Attivare

Attiva questa skill quando:

- Costruisci pipeline di valutazione automatizzate per output LLM
- Confronti risposte di modelli multipli per selezionare la migliore
- Stabilisci standard di qualità consistenti attraverso i team di valutazione
- Esegui il debug di sistemi di valutazione che mostrano risultati inconsistenti
- Progetti A/B test per modifiche ai prompt o ai modelli
- Crei rubriche per la valutazione umana o automatizzata
- Analizzi la correlazione tra giudizi automatizzati e umani

## Concetti Chiave

### La Tassonomia di Valutazione

Gli approcci di valutazione ricadono in due categorie primarie con profili di affidabilità distinti:

**Direct Scoring (Punteggio Diretto)**: Un singolo LLM valuta una risposta su una scala definita.

- Ideale per: Criteri oggettivi (accuratezza fattuale, rispetto delle istruzioni, tossicità)
- Affidabilità: Da moderata ad alta per criteri ben definiti
- Modalità di fallimento: Deriva della calibrazione del punteggio, interpretazione inconsistente della scala

**Pairwise Comparison (Confronto a Coppie)**: Un LLM confronta due risposte e seleziona la migliore.

- Ideale per: Preferenze soggettive (tono, stile, persuasività)
- Affidabilità: Più alta del direct scoring per le preferenze
- Modalità di fallimento: Position bias (bias di posizione), length bias (bias di lunghezza)

La ricerca dal paper MT-Bench (Zheng et al., 2023) stabilisce che il confronto a coppie raggiunge un accordo più alto con i giudici umani rispetto al punteggio diretto per la valutazione basata sulle preferenze, mentre il punteggio diretto rimane appropriato per criteri oggettivi con una chiara verità di base (ground truth).

### Il Panorama dei Bias

I giudici LLM mostrano bias sistematici che devono essere attivamente mitigati:

**Position Bias (Bias di Posizione)**: Le risposte in prima posizione ricevono un trattamento preferenziale nel confronto a coppie. Mitigazione: Valuta due volte scambiando le posizioni, usa il voto di maggioranza o controlli di consistenza.

**Length Bias (Bias di Lunghezza)**: Le risposte più lunghe vengono valutate meglio indipendentemente dalla qualità. Mitigazione: Prompt esplicito per ignorare la lunghezza, punteggio normalizzato per lunghezza.

**Self-Enhancement Bias (Bias di Auto-Esaltazione)**: I modelli valutano i propri output più in alto. Mitigazione: Usa modelli diversi per generazione e valutazione, o riconosci la limitazione.

**Verbosity Bias (Bias di Verbosità)**: Spiegazioni dettagliate ricevono punteggi più alti anche quando non necessarie. Mitigazione: Rubriche specifiche per criterio che penalizzano dettagli irrilevanti.

**Authority Bias (Bias di Autorità)**: Tono confidente e autorevole valutato più in alto indipendentemente dall'accuratezza. Mitigazione: Richiedi citazione di prove, layer di fact-checking.

### Framework di Selezione Metriche

Scegli le metriche basandoti sulla struttura del task di valutazione:

| Tipo di Task                        | Metriche Primarie                          | Metriche Secondarie            |
| ----------------------------------- | ------------------------------------------ | ------------------------------ |
| Classificazione binaria (pass/fail) | Recall, Precision, F1                      | Cohen's κ                      |
| Scala ordinale (rating 1-5)         | Spearman's ρ, Kendall's τ                  | Cohen's κ (weighted)           |
| Preferenza a coppie                 | Tasso di accordo, Consistenza di posizione | Calibrazione della confidenza  |
| Multi-label                         | Macro-F1, Micro-F1                         | Precision/recall per etichetta |

L'insight critico: L'alto accordo assoluto conta meno dei pattern di disaccordo sistematico. Un giudice che è consistentemente in disaccordo con gli umani su specifici criteri è più problematico di uno con rumore casuale.

## Approcci di Valutazione

### Implementazione Direct Scoring

Il punteggio diretto richiede tre componenti: criteri chiari, una scala calibrata e un formato di output strutturato.

**Pattern Definizione Criteri**:

```
Criterion: [Nome]
Description: [Cosa misura questo criterio]
Weight: [Importanza relativa, 0-1]
```

**Calibrazione Scala**:

- Scale 1-3: Binarie con opzione neutrale, carico cognitivo minimo
- Scale 1-5: Likert standard, buon bilanciamento tra granularità e affidabilità
- Scale 1-10: Alta granularità ma più difficile da calibrare, usare solo con rubriche dettagliate

**Struttura Prompt per Direct Scoring**:

```
You are an expert evaluator assessing response quality.

## Task
Evaluate the following response against each criterion.

## Original Prompt
{prompt}

## Response to Evaluate
{response}

## Criteria
{for each criterion: name, description, weight}

## Instructions
For each criterion:
1. Find specific evidence in the response
2. Score according to the rubric (1-{max} scale)
3. Justify your score with evidence
4. Suggest one specific improvement

## Output Format
Respond with structured JSON containing scores, justifications, and summary.
```

**Requisito Chain-of-Thought**: Tutti i prompt di scoring devono richiedere una giustificazione prima del punteggio. La ricerca mostra che questo migliora l'affidabilità del 15-25% rispetto agli approcci score-first.

### Implementazione Pairwise Comparison

Il confronto a coppie è intrinsecamente più affidabile per la valutazione basata su preferenze ma richiede la mitigazione dei bias.

**Protocollo Mitigazione Position Bias**:

1. Primo passaggio: Risposta A in prima posizione, Risposta B in seconda
2. Secondo passaggio: Risposta B in prima posizione, Risposta A in seconda
3. Controllo consistenza: Se i passaggi sono in disaccordo, restituisci TIE (pareggio) con confidenza ridotta
4. Verdetto finale: Vincitore consistente con confidenza media

**Struttura Prompt per Pairwise Comparison**:

```
You are an expert evaluator comparing two AI responses.

## Critical Instructions
- Do NOT prefer responses because they are longer
- Do NOT prefer responses based on position (first vs second)
- Focus ONLY on quality according to the specified criteria
- Ties are acceptable when responses are genuinely equivalent

## Original Prompt
{prompt}

## Response A
{response_a}

## Response B
{response_b}

## Comparison Criteria
{criteria list}

## Instructions
1. Analyze each response independently first
2. Compare them on each criterion
3. Determine overall winner with confidence level

## Output Format
JSON with per-criterion comparison, overall winner, confidence (0-1), and reasoning.
```

**Calibrazione Confidenza**: I punteggi di confidenza dovrebbero riflettere la consistenza della posizione:

- Entrambi i passaggi concordano: confidenza = media delle confidenze individuali
- I passaggi disaccordano: confidenza = 0.5, verdetto = TIE

### Generazione Rubriche

Rubriche ben definite riducono la varianza di valutazione del 40-60% rispetto allo scoring open-ended.

**Componenti Rubrica**:

1. **Descrizioni livello**: Confini chiari per ogni livello di punteggio
2. **Caratteristiche**: Funzionalità osservabili che definiscono ogni livello
3. **Esempi**: Testo rappresentativo per ogni livello (opzionale ma prezioso)
4. **Casi limite**: Guida per situazioni ambigue
5. **Linee guida di scoring**: Principi generali per un'applicazione consistente

**Calibrazione Severità**:

- **Lenient (Indulgente)**: Asticella più bassa per i punteggi di passaggio, appropriato per incoraggiare l'iterazione
- **Balanced (Bilanciato)**: Giusto, aspettative tipiche per uso in produzione
- **Strict (Severo)**: Standard alti, appropriato per valutazioni critiche per la sicurezza o high-stakes

**Adattamento al Dominio**: Le rubriche dovrebbero usare terminologia specifica del dominio. Una rubrica di "leggibilità codice" menziona variabili, funzioni e commenti. Una rubrica di "accuratezza medica" fa riferimento a terminologia clinica e standard di evidenza.

## Guida Pratica

### Design Pipeline di Valutazione

I sistemi di valutazione in produzione richiedono livelli multipli:

```
┌─────────────────────────────────────────────────┐
│                 Evaluation Pipeline              │
├─────────────────────────────────────────────────┤
│                                                   │
│  Input: Response + Prompt + Context               │
│           │                                       │
│           ▼                                       │
│  ┌─────────────────────┐                         │
│  │   Criteria Loader   │ ◄── Rubrics, weights    │
│  └──────────┬──────────┘                         │
│             │                                     │
│             ▼                                     │
│  ┌─────────────────────┐                         │
│  │   Primary Scorer    │ ◄── Direct or Pairwise  │
│  └──────────┬──────────┘                         │
│             │                                     │
│             ▼                                     │
│  ┌─────────────────────┐                         │
│  │   Bias Mitigation   │ ◄── Position swap, etc. │
│  └──────────┬──────────┘                         │
│             │                                     │
│             ▼                                     │
│  ┌─────────────────────┐                         │
│  │ Confidence Scoring  │ ◄── Calibration         │
│  └──────────┬──────────┘                         │
│             │                                     │
│             ▼                                     │
│  Output: Scores + Justifications + Confidence     │
│                                                   │
└─────────────────────────────────────────────────┘
```

### Anti-Pattern Comuni

**Anti-pattern: Scoring senza giustificazione**

- Problema: I punteggi mancano di fondamento, difficile fare debug o migliorare
- Soluzione: Richiedi sempre giustificazione basata su prove prima del punteggio

**Anti-pattern: Confronto a coppie a passaggio singolo**

- Problema: Il position bias corrompe i risultati
- Soluzione: Scambia sempre le posizioni e controlla la consistenza

**Anti-pattern: Criteri sovraccarichi**

- Problema: I criteri che misurano più cose sono inaffidabili
- Soluzione: Un criterio = un aspetto misurabile

**Anti-pattern: Mancanza guida casi limite**

- Problema: I valutatori gestiscono i casi ambigui in modo inconsistente
- Soluzione: Includi casi limite nelle rubriche con guida esplicita

**Anti-pattern: Ignorare calibrazione confidenza**

- Problema: Giudizi errati ad alta confidenza sono peggiori di quelli a bassa confidenza
- Soluzione: Calibra la confidenza sulla consistenza di posizione e forza delle prove

### Framework Decisionale: Direct vs. Pairwise

Usa questo albero decisionale:

```
Esiste una verità di base oggettiva (ground truth)?
├── Sì → Direct Scoring
│   └── Esempi: accuratezza fattuale, rispetto istruzioni, conformità formato
│
└── No → È un giudizio di preferenza o qualità?
    ├── Sì → Pairwise Comparison
    │   └── Esempi: tono, stile, persuasività, creatività
    │
    └── No → Considera valutazione reference-based
        └── Esempi: riassunto (confronta con fonte), traduzione (confronta con riferimento)
```

### Scalare la Valutazione

Per valutazioni ad alto volume:

1. **Panel of LLMs (PoLL)**: Usa modelli multipli come giudici, aggrega i voti
   - Riduce il bias del singolo modello
   - Più costoso ma più affidabile per decisioni high-stakes

2. **Valutazione gerarchica**: Modello veloce ed economico per screening, modello costoso per casi limite
   - Cost-effective per grandi volumi
   - Richiede calibrazione della soglia di screening

3. **Human-in-the-loop**: Valutazione automatizzata per casi chiari, revisione umana per bassa confidenza
   - Migliore affidabilità per applicazioni critiche
   - Progetta un feedback loop per migliorare la valutazione automatizzata

## Esempi

### Esempio 1: Direct Scoring per Accuratezza

**Input**:

```
Prompt: "What causes seasons on Earth?"
Response: "Seasons are caused by Earth's tilted axis. As Earth orbits the Sun,
different hemispheres receive more direct sunlight at different times of year."
Criterion: Factual Accuracy (weight: 1.0)
Scale: 1-5
```

**Output**:

```json
{
  "criterion": "Factual Accuracy",
  "score": 5,
  "evidence": [
    "Correctly identifies axial tilt as primary cause",
    "Correctly explains differential sunlight by hemisphere",
    "No factual errors present"
  ],
  "justification": "Response accurately explains the cause of seasons with correct
scientific reasoning. Both the axial tilt and its effect on sunlight distribution
are correctly described.",
  "improvement": "Could add the specific tilt angle (23.5°) for completeness."
}
```

### Esempio 2: Pairwise Comparison con Scambio Posizione

**Input**:

```
Prompt: "Explain machine learning to a beginner"
Response A: [Technical explanation with jargon]
Response B: [Simple analogy-based explanation]
Criteria: ["clarity", "accessibility"]
```

**Primo Passaggio (A prima)**:

```json
{ "winner": "B", "confidence": 0.8 }
```

**Secondo Passaggio (B prima)**:

```json
{ "winner": "A", "confidence": 0.6 }
```

(Nota: Il vincitore è A perché B era in prima posizione)

**Secondo Passaggio Mappato**:

```json
{ "winner": "B", "confidence": 0.6 }
```

**Risultato Finale**:

```json
{
  "winner": "B",
  "confidence": 0.7,
  "positionConsistency": {
    "consistent": true,
    "firstPassWinner": "B",
    "secondPassWinner": "B"
  }
}
```

### Esempio 3: Generazione Rubrica

**Input**:

```
criterionName: "Code Readability"
criterionDescription: "How easy the code is to understand and maintain"
domain: "software engineering"
scale: "1-5"
strictness: "balanced"
```

**Output** (abbreviato):

```json
{
  "levels": [
    {
      "score": 1,
      "label": "Poor",
      "description": "Code is difficult to understand without significant effort",
      "characteristics": [
        "No meaningful variable or function names",
        "No comments or documentation",
        "Deeply nested or convoluted logic"
      ]
    },
    {
      "score": 3,
      "label": "Adequate",
      "description": "Code is understandable with some effort",
      "characteristics": [
        "Most variables have meaningful names",
        "Basic comments present for complex sections",
        "Logic is followable but could be cleaner"
      ]
    },
    {
      "score": 5,
      "label": "Excellent",
      "description": "Code is immediately clear and maintainable",
      "characteristics": [
        "All names are descriptive and consistent",
        "Comprehensive documentation",
        "Clean, modular structure"
      ]
    }
  ],
  "edgeCases": [
    {
      "situation": "Code is well-structured but uses domain-specific abbreviations",
      "guidance": "Score based on readability for domain experts, not general audience"
    }
  ]
}
```

## Linee Guida

1. **Richiedi sempre giustificazione prima dei punteggi** - Il chain-of-thought prompting migliora l'affidabilità del 15-25%

2. **Scambia sempre le posizioni nel confronto a coppie** - Il confronto a passaggio singolo è corrotto dal bias di posizione

3. **Allinea la granularità della scala alla specificità della rubrica** - Non usare 1-10 senza descrizioni dettagliate dei livelli

4. **Separa criteri oggettivi e soggettivi** - Usa direct scoring per oggettivi, pairwise per soggettivi

5. **Includi punteggi di confidenza** - Calibra sulla consistenza di posizione e forza delle prove

6. **Definisci i casi limite esplicitamente** - Le situazioni ambigue causano la maggiore varianza di valutazione

7. **Usa rubriche specifiche per dominio** - Rubriche generiche producono valutazioni generiche (meno utili)

8. **Valida contro giudizi umani** - La valutazione automatizzata è preziosa solo se correla con la valutazione umana

9. **Monitora per bias sistematici** - Traccia pattern di disaccordo per criterio, tipo di risposta, modello

10. **Progetta per l'iterazione** - I sistemi di valutazione migliorano con i feedback loop

## Integrazione

Questa skill si integra con:

- **context-fundamentals** - I prompt di valutazione richiedono una struttura di contesto efficace
- **tool-design** - I tool di valutazione necessitano di schemi e gestione errori appropriati
- **context-optimization** - I prompt di valutazione possono essere ottimizzati per efficienza di token
- **evaluation** (fondamentale) - Questa skill estende i concetti di valutazione fondamentali

## Riferimenti

Riferimento interno:

- [LLM-as-Judge Implementation Patterns](./references/implementation-patterns.md)
- [Bias Mitigation Techniques](./references/bias-mitigation.md)
- [Metric Selection Guide](./references/metrics-guide.md)

Ricerca esterna:

- [Eugene Yan: Evaluating the Effectiveness of LLM-Evaluators](https://eugeneyan.com/writing/llm-evaluators/)
- [Judging LLM-as-a-Judge (Zheng et al., 2023)](https://arxiv.org/abs/2306.05685)
- [G-Eval: NLG Evaluation using GPT-4 (Liu et al., 2023)](https://arxiv.org/abs/2303.16634)
- [Large Language Models are not Fair Evaluators (Wang et al., 2023)](https://arxiv.org/abs/2305.17926)

Skill correlate in questa collezione:

- evaluation - Concetti di valutazione fondamentali
- context-fundamentals - Struttura del contesto per prompt di valutazione
- tool-design - Costruzione tool di valutazione

---

## Skill Metadata

**Created**: 2024-12-24
**Last Updated**: 2024-12-24
**Author**: Muratcan Koylan
**Version**: 1.0.0
