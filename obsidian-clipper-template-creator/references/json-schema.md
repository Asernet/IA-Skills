# Schema JSON di Obsidian Web Clipper

Obsidian Web Clipper importa i template tramite file JSON.

## Struttura Root

```json
{
  "schemaVersion": "0.1.0",
  "name": "Template Name",
  "behavior": "create",
  "noteContentFormat": "Markdown content here...",
  "properties": [],
  "triggers": [],
  "noteNameFormat": "{{title}}",
  "path": "Inbox/"
}
```

### Campi

- **`schemaVersion`**: Sempre "0.1.0".
- **`name`**: Il nome visualizzato del template nel Clipper.
- **`behavior`**: Come viene creata la nota.
  - `create`: Crea una nuova nota.
  - `append-specific`: Aggiunge a una nota specifica (richiede che `path` sia un percorso file completo).
  - `append-daily`: Aggiunge alla nota del giorno (daily note).
- **`noteContentFormat`**: Il corpo della nota.
  - Usa `\n` per le nuove righe.
  - Può usare tutte le variabili (es. `{{content}}`, `{{selection}}`).
- **`noteNameFormat`**: Il pattern del nome del file (es. `{{date}} - {{title}}`).
- **`path`**: La posizione dove salvare la nota.
  - Per il comportamento `create`: La _cartella_ in cui salvare la nota (es. `Clippings/` o `Recipes/`).
  - Per il comportamento `append-specific`: Il _percorso completo del file_ della nota a cui aggiungere contenuto (es. `Databases/Recipes.md`).
- **`triggers`**: Array di stringhe per selezionare automaticamente questo template.
  - **Pattern URL**: `["https://www.youtube.com/watch"]` (Stringa semplice o Regex).
  - **Tipi di Schema**: `["schema:Recipe"]` (Si attiva se la pagina contiene questo tipo di Schema.org).

## Proprietà

L'array `properties` definisce il frontmatter YAML della nota.

```json
"properties": [
    {
        "name": "category",
        "value": "Recipes",
        "type": "text"
    },
    {
        "name": "published",
        "value": "{{published}}",
        "type": "datetime"
    }
]
```

### Tipi di Proprietà

- **`text`**: Stringa di testo semplice.
- **`multitext`**: Elenco di stringhe di testo (per tag/alias).
- **`number`**: Valore numerico.
- **`checkbox`**: Booleano vero/falso.
- **`date`**: Stringa della data (YYYY-MM-DD).
- **`datetime`**: Stringa di data e ora.

### Struttura dell'Oggetto Proprietà

- **`name`**: La chiave nel frontmatter YAML.
- **`value`**: Il valore da popolare. Può contenere variabili.
- **`type`**: Uno dei tipi elencati sopra.
