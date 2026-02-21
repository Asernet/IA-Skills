# Filtri di Obsidian Web Clipper

**Documentazione Ufficiale:** [help.obsidian.md/web-clipper/filters](https://help.obsidian.md/web-clipper/filters)

Usa i filtri per formattare le variabili: `{{variable|filter}}`.

## Formattazione del Testo

- `markdown`: Converte HTML in Markdown.
- `strip_tags`: Rimuove i tag HTML.
- `trim`: Rimuove gli spazi bianchi.
- `upper`: Converte in maiuscolo.
- `lower`: Converte in minuscolo.
- `title`: Iniziali Maiuscole (Title Case).
- `capitalize`: Capitalizza la prima lettera.
- `camel`: CamelCase.
- `kebab`: kebab-case.
- `snake`: snake_case.
- `pascal`: PascalCase.
- `replace:"vecchio","nuovo"`: Sostituisce il testo.
- `safe_name`: Rende il nome sicuro per i nomi dei file.
- `blockquote`: Formatta come citazione (blockquote).
- `link`: Crea un link markdown.
- `wikilink`: Crea un [[wikilink]].
- `list`: Formatta un array come elenco.
- `table`: Formatta un array come tabella.
- `callout`: Formatta come blocco callout.

## Date

- `date:"formato"`: Formatta la data (es. `YYYY-MM-DD`).
- `date_modify:"+1 day"`: Modifica la data.
- `duration`: Formatta la durata.

## Numeri

- `calc`: Esegue calcoli.
- `length`: Ottiene la lunghezza di una stringa/array.
- `round`: Arrotonda i numeri.

## Elaborazione HTML

- `remove_html`: Rimuove i tag HTML.
- `remove_attr`: Rimuove gli attributi.
- `strip_attr`: Rimuove attributi specifici.

## Array e Oggetti

- `map`: Trasforma gli elementi di un array (es. `map:item =>> item.text`).
- `join:"separatore"`: Unisce gli elementi di un array.
- `split:"separatore"`: Divide una stringa in un array.
- `first`: Primo elemento.
- `last`: Ultimo elemento.
- `slice:inizio,fine`: Taglia l'array (slice).
- `unique`: Elementi unici.
- `template:"formato"`: Formatta gli elementi usando una stringa template.
