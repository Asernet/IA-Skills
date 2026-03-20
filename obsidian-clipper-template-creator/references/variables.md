# Variabili di Obsidian Web Clipper

**Documentazione Ufficiale:** [help.obsidian.md/web-clipper/variables](https://help.obsidian.md/web-clipper/variables)

## Variabili Predefinite

Estratte automaticamente dalla pagina.

- `{{content}}`: Contenuto principale dell'articolo (markdown).
- `{{contentHtml}}`: Contenuto principale dell'articolo (HTML).
- `{{title}}`: Titolo della pagina.
- `{{url}}`: URL della pagina.
- `{{author}}`: Nome dell'autore.
- `{{date}}`: Data corrente.
- `{{published}}`: Data di pubblicazione (se rilevata).
- `{{site}}`: Nome del sito.
- `{{description}}`: Meta descrizione.
- `{{highlights}}`: Testo evidenziato (se presente).
- `{{selection}}`: Testo selezionato.
- `{{fullHtml}}`: HTML completo della pagina.
- `{{favicon}}`: URL della favicon.
- `{{image}}`: URL dell'immagine di condivisione social.
- `{{words}}`: Conteggio parole.
- `{{domain}}`: Nome del dominio.

## Variabili di Prompt (IA)

Usa `{{"Il tuo prompt qui"}}` per chiedere all'Interprete IA di estrarre o riassumere informazioni.
_Richiede che l'Interprete sia abilitato._

Esempi:

- `{{"Riassumi in 3 punti elenco"}}`
- `{{"Estrai l'elenco degli ingredienti"}}`
- `{{"Traduci in Italiano"}}`

## Variabili Selettore

Estrai i contenuti usando i selettori CSS.
Sintassi: `{{selector:selettore-css}}` o `{{selector:selettore-css?attributo}}`

Esempi:

- `{{selector:h1}}`: Testo del tag H1.
- `{{selector:img.hero?src}}`: Sorgente dell'immagine con classe 'hero'.
- `{{selector:.author}}`: Testo dell'elemento con classe 'author'.
- `{{selectorHtml:body|markdown}}`: HTML completo convertito in markdown.

## Meta Variabili

Estrai dati dai meta tag.
Sintassi: `{{meta:nome}}` o `{{meta:proprietà}}`

Esempi:

- `{{meta:description}}`
- `{{meta:og:title}}`

## Variabili Schema.org

Estrai dati strutturati.
Sintassi: `{{schema:Proprietà}}` o `{{schema:@Tipo:Proprietà}}`

Esempi:

- `{{schema:Recipe:recipeIngredient}}`
- `{{schema:author.name}}`
- `{{schema:Article:headline}}`
