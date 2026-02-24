---
name: skill-creator
description: "Centrale di Ingegneria per Skill AI. Gestisce il ciclo di vita completo (Design, Creazione, Refactoring) con standard qualitativi Anthropic e pattern avanzati."
version: 2.1.0
category: meta
tags:
  [
    automation,
    scaffolding,
    skill-creation,
    prompt-engineering,
    qualitative-standards,
  ]
---

# Skill Creator Pro: Manuale di Ingegneria Qualitativa

Questa skill non è solo un generatore di file, ma un custode degli standard di qualità per gli agenti AI. Segui questa guida per creare skill che siano robuste, concise e potenti.

---

# 🧠 ARCHITETTURA DELLA CONOSCENZA (3 Livelli)

Ogni skill deve seguire il pattern della **Progressive Disclosure** (Rivelazione Progressiva):

1.  **Livello 1: Metadata (Frontmatter YAML)**: Informazioni rapide per l'indicizzatore.
2.  **Livello 2: SKILL.md (Il Cuore)**: Istruzioni operative principali (1.500 - 2.000 parole). Deve essere autonomo ma non sovraccarico.
3.  **Livello 3: Bundled Resources (Le Appendici)**:
    - `references/`: Documentazione pesante, guide di stile, specifiche tecniche (>5.000 parole).
    - `examples/`: Campioni di codice funzionanti, coppie input/output per lo stile.
    - `scripts/`: Utilità eseguibili per automatizzare task specifici.

---

# 📏 STANDARD QUALITATIVI (Must-Have)

- **Persona**: Scrivi sempre in **terza persona** (es: "Questa skill deve...", NOT "Usa questa skill per...").
- **Mood**: Usa il modo **imperativo/infinito** per le istruzioni operative.
- **Concisione**: La finestra di contesto è preziosa. Non spiegare concetti che l'IA già conosce (es: nozioni base di Python).
- **Integrità Tecnica**: Path, comandi e snippet di codice devono essere esatti e testati.

---

# 🎨 PATTERN DI DESIGN DELLE SKILL

### 1. Workflow Patterns

- **Sequenziale**: Per task lineari. Mostra sempre un'anteprima (overview) dei passaggi all'inizio.
- **Condizionale**: Per task con logica a bivi. Usa blocchi "Se... allora..." chiaramente demarcati.

### 2. Output Patterns

- **Template Rigido**: Se l'output deve essere processato da altri tool/API (Markdown strutturato, JSON).
- **Esempi per lo Stile**: Fornisci coppie `Input -> Output` per insegnare all'IA il tono e il livello di dettaglio desiderato.

---

# 🛠️ WORKFLOW OPERATIVO POTENZIATO

### Fase 0: Scansione Ambiente & Discovery

- Verifica `COPILOT_INSTALLED` e `CLAUDE_INSTALLED`.
- Identifica il ruolo dell'agente: È uno strumento di analisi, generazione codice o documentazione?

### Fase 1: Ingegneria del Prompt (TDD) [30%]

- **NON saltare questo passaggio**: Usa la metodologia `writing-skills`.
- Definisci i criteri di successo (Cosa rende questa skill "buona"?).

### Fase 2: Creazione Struttura Deep [60%]

- Crea la cartella in `C:\Users\M.Macelloni\.gemini\skills\[nome]`.
- Genera il file `SKILL.md` (vedi Template).
- **Proattività**: Se la skill è complessa, crea automaticamente i file in `references/` e `examples/`.

### Fase 3: Deployment & Symlink [100%]

- Offri sempre l'installazione globale (`ln -sf`) per rendere la skill universale.

---

# 🔄 MODALITÀ REFACTORY & MIGLIORAMENTO

Durante la manutenzione di skill esistenti (specialmente se provenienti dalla community in inglese):

1.  **Traduzione Analitica**: Traduci riga per riga. Non riassumere mai.
2.  **Iniezione di Sostanza**: Se il file originale è povero, arricchiscilo con i "Pattern di Design" descritti sopra.
3.  **Verifica Coerenza**: Assicurati che i path assoluti puntino alle directory corrette dell'utente.

---

# 📝 TEMPLATE PROFESSIONALE SKILL.md

```markdown
---
name: [nome-kebab-case]
description: [Terza persona, Italiano]
triggers: ["...", "..."]
---

# [Titolo]

## Overview

[Spiegazione breve del perché e quando usare questa skill]

## Workflow

1. [Passo 1]
2. [Passo 2]

## Design Patterns

[Elenco dei pattern usati, es: Template Pattern per report]

## Risorse Bundled

- [references/...]
- [examples/...]
```
