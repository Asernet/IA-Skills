# Lavorare con le Basi di Obsidian

L'utente mantiene delle "Basi" in `Templates/Bases/*.base` che definiscono lo schema e le proprietà per diversi tipi di note (es. Ricette, Ritagli, Persone).

## Workflow

1.  **Identifica la Categoria:** Determina il tipo di contenuto che l'utente vuole acquisire (es. una Ricetta, un Articolo di Cronaca, un video di YouTube).
2.  **Trova la Base:** Cerca in `Templates/Bases/` un file `.base` corrispondente.
    - Esempio: Per una ricetta, cerca `Templates/Bases/Recipes.base`.
    - Esempio: Per un articolo generico, cerca `Templates/Bases/Clippings.base`.
3.  **Leggi la Base:** Leggi il contenuto del file `.base` per capire le proprietà richieste.

## Interpretazione dei file .base

I file Base usano una struttura simile a YAML. Cerca la sezione `properties`.

```yaml
properties:
  file.name:
    displayName: name
  note.author:
    displayName: author
  note.type:
    displayName: type
  note.ingredients:
    displayName: ingredients
```

- `note.X` corrisponde a un nome di proprietà `X` nel frontmatter.
- `displayName` aiuta a capire l'intento, ma la chiave della proprietà (es. `author`, `type`, `ingredients`) è ciò che conta per il template.

## Mappatura alle proprietà del Clipper

Quando crei il JSON per il Web Clipper, mappa le proprietà della Base all'array `properties` nel JSON.

| Proprietà Base     | Nome Proprietà JSON Clipper | Strategia Valore                        |
| :----------------- | :-------------------------- | :-------------------------------------- |
| `note.author`      | `author`                    | `{{author}}` o `{{schema:author.name}}` |
| `note.source`      | `source`                    | `{{url}}`                               |
| `note.published`   | `published`                 | `{{published}}`                         |
| `note.ingredients` | `ingredients`               | `{{schema:Recipe:recipeIngredient}}`    |
| `note.type`        | `type`                      | Costante (es. `Recipe`) o vuoto         |

**Passaggio Fondamentale:** Chiedi all'utente quali proprietà devono essere compilate automaticamente, quali devono essere fisse (es. `type: Recipe`) e quali devono essere lasciate vuote per l'inserimento manuale.
