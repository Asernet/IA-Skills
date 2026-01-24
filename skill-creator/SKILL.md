---
name: skill-creator
description: Guida completa alla progettazione di skill ed agente generatore per creare nuove skill nell'ambiente Gemini CLI.
---

# Skill Creator & Generator

Questa skill unificata serve due scopi:

1.  **Guida di Riferimento**: Fornisce principi, pattern e best practice per progettare skill efficaci.
2.  **Agente Generatore**: Agisce come "Skill Generator" operativo per creare fisicamente i file delle skill.

---

# PARTE 1: IL "MANUALE" (Guida alla Progettazione)

Le skill sono pacchetti modulari e auto-contenuti che estendono le capacità di Claude fornendo conoscenze specializzate, workflow e tool.

## Principi Core

### La Concisione è Chiave

La finestra di contesto è un bene pubblico. Aggiungi solo contesto che Claude o Gemini-CLI non hanno già. Preferisci esempi concisi a spiegazioni verpose.

### Gradi di Libertà

- **Alta libertà**: Istruzioni testuali (quando approcci multipli sono validi).
- **Libertà media**: Pseudocodice (quando esiste un pattern preferito).
- **Bassa libertà**: Script specifici (quando la consistenza è critica).

### Anatomia di una Skill

Ogni skill deve trovarsi in `C:\Users\mazin\.gemini\skills\<skill-name>\` e contenere almeno `SKILL.md`.

#### Struttura Directory

```
skill-name/
├── SKILL.md (richiesto)
│   ├── YAML frontmatter (name, description)
│   └── Istruzioni Markdown
└── Risorse (opzionale)
    ├── scripts/    - Codice eseguibile
    ├── references/ - Documentazione pesante
    └── assets/     - File usati nell'output
```

#### Pubblicazione e Validazione

Usa sempre `scripts/init_skill.py` per creare e `scripts/package_skill.py` per validare e impacchettare.

---

# PARTE 2: L' "OPERAIO" (Agente Generatore)

Quando ti viene chiesto di "Creare una nuova skill" o agire come "Skill Generator", attiva questa modalità.

## Ruolo Attivo

Tu sei l'agente **Skill Generator**. Il tuo compito è meta-programmare file di configurazione (`.md`) per l'ambiente Gemini CLI.

## Processo di Creazione

Segui rigorosamente questa sequenza:

1.  **Analisi**: Identifica compito e ruolo. Se vago, chiedi chiarimenti.
2.  **Definizione**: Elabora Frontmatter (name: kebab-case, description: ITALIANO terza persona) e Contenuto.
3.  **Conferma**: Mostra bozza strutturata.
4.  **Lingua della Skill**: La skill deve essere scritta in **ITALIANO** (eccetto termini tecnici standard).
5.  **Esecuzione**:
    - Crea cartella: `C:\Users\mazin\.gemini\skills\[nome-skill]\`
    - Scrivi file: `C:\Users\mazin\.gemini\skills\[nome-skill]\SKILL.md`

## Template Obbligatorio SKILL.md

```markdown
---
name: [nome-skill-kebab-case]
description:
  [Descrizione in terza persona in ITALIANO. Es: "Genera unit test per..."]
---

# [Nome Skill]

## Ruolo

[Chi è l'agente quando usa questa skill?]

## Istruzioni Operative

1. [Azione 1]
2. [Azione 2]

## Vincoli

- [Cosa NON fare]

## Esempi

User: ...
Assistant: ...
```

## Regole per la Generazione

- **Lingua**: Tutto il contenuto generato deve essere in **ITALIANO** (eccetto termini tecnici standard).
- **Path**: Non deviare mai da `C:\Users\mazin\.gemini\skills\`.
- **Focus**: Una skill = Una responsabilità.
