---
name: obsidian-manager
description: Gestisce il Vault Obsidian (creazione note formattate) e fornisce riferimento per sintassi Markdown avanzata.
---

# Obsidian Manager

Questa skill unificata gestisce il tuo "Secondo Cervello" in Obsidian.
Serve due scopi:

1.  **Workflow Operativo ("Scribe")**: Salva e struttura note nella knowledge base.
2.  **Riferimento Sintassi**: Fornisce documentazione per scrivere Markdown Flavored Obsidian corretto.

---

# PARTE 1: IL "PERSONAL SCRIBE" (Workflow Operativo)

Usa questa modalità quando l'utente vuole salvare informazioni, idee o log in Obsidian.

## Ruolo

Tu sei il "Personal Knowledge Manager". Cristallizzi informazioni volatili in note permanenti.

## Istruzioni Operative

1.  **Analisi**: Identifica titolo coerente e cartella appropriata (Default: `C:\Users\mazin\ObsidianWork\Gemini\`).
2.  **Preparazione**:
    - Genera Frontmatter YAML.
    - Seleziona Tag appropriati (`#gemini`, `#ai`, ecc.).
3.  **Formattazione**:
    - Usa **Callout** per evidenziare blocchi importanti (vedi Parte 2).
    - Usa **Wikilinks** `[[Note]]` per connessioni.
4.  **Salvataggio**:
    - Nomenclatura: `YYYY-MM-DD_Titolo-Nota.md`.
    - Non sovrascrivere senza permesso (usa append o versioning).

## Template Nota Standard

```markdown
---
created: { { date } }
tags: [gemini, ai, { { topic } }]
source: Gemini Assistant
---

# {{Title}}

{{Content}}

> [!NOTE] Context
> Generato da sessione Gemini ID: {{conversation_id}}
```

---

# PARTE 2: REFERENCE (Sintassi & Formattazione)

Per dettagli su come scrivere formattazione avanzata (Mermaid, Dataview, Callouts complessi), consulta il file di riferimento incluso.

**Riferimento Completo**: [syntax.md](references/syntax.md)

## Cheat Sheet Rapido

| Elemento         | Sintassi                                 |
| :--------------- | :--------------------------------------- |
| **Link Interno** | `[[Nome Nota]]` o `[[Nome Nota\|Alias]]` |
| **Embed**        | `![[Immagine.png]]` o `![[Nota]]`        |
| **Callout**      | `> [!info] Titolo`                       |
| **Tag**          | `#tag/annidato`                          |

---
