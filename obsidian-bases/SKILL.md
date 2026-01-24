---
name: obsidian-bases
description: Crea e modifica Obsidian Bases (.base) per viste database, filtri e formule nelle note.
---

# Skill Obsidian Bases

Questa skill abilita agenti skills-compatibili a creare ed editare Obsidian Bases valide (file `.base`) incluse viste, filtri, formule e tutte le configurazioni correlate.

## Panoramica

Le Obsidian Bases sono file basati su YAML che definiscono viste dinamiche di note in un vault Obsidian. Un file Base può contenere viste multiple, filtri globali, formule, configurazioni proprietà e sommari personalizzati.

## Formato File

I file Base usano l'estensione `.base` e contengono YAML valido. Possono anche essere incorporati in blocchi codice Markdown.

## Schema Completo

```yaml
# Filtri globali applicati a TUTTE le viste nella base
filters:
  # Può essere una singola stringa filtro
  # O un oggetto filtro ricorsivo con and/or/not
  and: []
  or: []
  not: []

# Definisci proprietà formula che possono essere usate attraverso tutte le viste
formulas:
  formula_name: "expression"

# Configura nomi visualizzati e impostazioni per proprietà
properties:
  property_name:
    displayName: "Display Name"
  formula.formula_name:
    displayName: "Formula Display Name"
  file.ext:
    displayName: "Extension"

# Definisci formule sommario personalizzate
summaries:
  custom_summary_name: "values.mean().round(3)"

# Definisci una o più viste
views:
  - type: table | cards | list | map
    name: "View Name"
    limit: 10 # Opzionale: limita risultati
    groupBy: # Opzionale: raggruppa risultati
      property: property_name
      direction: ASC | DESC
    filters: # Filtri specifici vista
      and: []
    order: # Proprietà da visualizzare in ordine
      - file.name
      - property_name
      - formula.formula_name
    summaries: # Mappa proprietà a formule sommario
      property_name: Average
```

## Sintassi Filtri

I filtri restringono i risultati. Possono essere applicati globalmente o per-vista.

### Struttura Filtro

```yaml
# Filtro singolo
filters: 'status == "done"'

# AND - tutte le condizioni devono essere vere
filters:
  and:
    - 'status == "done"'
    - 'priority > 3'

# OR - qualsiasi condizione può essere vera
filters:
  or:
    - 'file.hasTag("book")'
    - 'file.hasTag("article")'

# NOT - escludi elementi corrispondenti
filters:
  not:
    - 'file.hasTag("archived")'

# Filtri annidati
filters:
  or:
    - file.hasTag("tag")
    - and:
        - file.hasTag("book")
        - file.hasLink("Textbook")
    - not:
        - file.hasTag("book")
        - file.inFolder("Required Reading")
```

### Operatori Filtro

| Operatore      | Descrizione            |
| -------------- | ---------------------- |
| `==`           | uguale (equals)        |
| `!=`           | non uguale (not equal) |
| `>`            | maggiore di            |
| `<`            | minore di              |
| `>=`           | maggiore o uguale      |
| `<=`           | minore o uguale        |
| `&&`           | e logico (and)         |
| `\|\|`         | o logico (or)          |
| <code>!</code> | non logico (not)       |

## Proprietà

### Tre Tipi di Proprietà

1. **Proprietà nota** - Da frontmatter: `note.author` o solo `author`
2. **Proprietà file** - Metadati file: `file.name`, `file.mtime`, ecc.
3. **Proprietà formula** - Valori calcolati: `formula.my_formula`

### Riferimento Proprietà File

| Proprietà         | Tipo   | Descrizione                    |
| ----------------- | ------ | ------------------------------ |
| `file.name`       | String | Nome file                      |
| `file.basename`   | String | Nome file senza estensione     |
| `file.path`       | String | Percorso completo al file      |
| `file.folder`     | String | Percorso cartella genitore     |
| `file.ext`        | String | Estensione file                |
| `file.size`       | Number | Dimensione file in byte        |
| `file.ctime`      | Date   | Tempo creazione                |
| `file.mtime`      | Date   | Tempo modifica                 |
| `file.tags`       | List   | Tutti i tag nel file           |
| `file.links`      | List   | Link interni nel file          |
| `file.backlinks`  | List   | File che linkano a questo file |
| `file.embeds`     | List   | Embed nella nota               |
| `file.properties` | Object | Tutte le proprietà frontmatter |

### La Keyword `this`

- In area contenuto principale: riferisce al file base stesso
- Quando incorporato: riferisce al file che incorpora
- In sidebar: riferisce al file attivo nel contenuto principale

## Sintassi Formule

Le formule calcolano valori dalle proprietà. Definite nella sezione `formulas`.

```yaml
formulas:
  # Aritmetica semplice
  total: "price * quantity"

  # Logica condizionale
  status_icon: 'if(done, "✅", "⏳")'

  # Formattazione stringa
  formatted_price: 'if(price, price.toFixed(2) + " dollars")'

  # Formattazione data
  created: 'file.ctime.format("YYYY-MM-DD")'

  # Espressioni complesse
  days_old: "((now() - file.ctime) / 86400000).round(0)"
```

## Riferimento Funzioni

### Funzioni Globali

| Funzione       | Firma                                     | Descrizione                                           |
| -------------- | ----------------------------------------- | ----------------------------------------------------- |
| `date()`       | `date(string): date`                      | Parsea stringa a data. Formato: `YYYY-MM-DD HH:mm:ss` |
| `duration()`   | `duration(string): duration`              | Parsea stringa durata                                 |
| `now()`        | `now(): date`                             | Data e ora corrente                                   |
| `today()`      | `today(): date`                           | Data corrente (tempo = 00:00:00)                      |
| `if()`         | `if(condition, trueResult, falseResult?)` | Condizionale                                          |
| `min()`        | `min(n1, n2, ...): number`                | Numero più piccolo                                    |
| `max()`        | `max(n1, n2, ...): number`                | Numero più grande                                     |
| `number()`     | `number(any): number`                     | Converti a numero                                     |
| `link()`       | `link(path, display?): Link`              | Crea un link                                          |
| `list()`       | `list(element): List`                     | Avvolgi in lista se non lo è già                      |
| `file()`       | `file(path): file`                        | Ottieni oggetto file                                  |
| `image()`      | `image(path): image`                      | Crea immagine per rendering                           |
| `icon()`       | `icon(name): icon`                        | Icona Lucide per nome                                 |
| `html()`       | `html(string): html`                      | Renderizza come HTML                                  |
| `escapeHTML()` | `escapeHTML(string): string`              | Escapa caratteri HTML                                 |

### Funzioni Tipo Any

| Funzione     | Firma                       | Descrizione        |
| ------------ | --------------------------- | ------------------ |
| `isTruthy()` | `any.isTruthy(): boolean`   | Coerce a booleano  |
| `isType()`   | `any.isType(type): boolean` | Controlla tipo     |
| `toString()` | `any.toString(): string`    | Converti a stringa |

### Funzioni & Campi Data

**Campi:** `date.year`, `date.month`, `date.day`, `date.hour`, `date.minute`, `date.second`, `date.millisecond`

| Funzione     | Firma                         | Descrizione                    |
| ------------ | ----------------------------- | ------------------------------ |
| `date()`     | `date.date(): date`           | Rimuovi porzione tempo         |
| `format()`   | `date.format(string): string` | Formatta con pattern Moment.js |
| `time()`     | `date.time(): string`         | Ottieni tempo come stringa     |
| `relative()` | `date.relative(): string`     | Tempo relativo leggibile       |
| `isEmpty()`  | `date.isEmpty(): boolean`     | Sempre falso per date          |

### Aritmetica Data

```yaml
# Unità durata: y/year/years, M/month/months, d/day/days,
#                 w/week/weeks, h/hour/hours, m/minute/minutes, s/second/seconds

# Aggiungi/sottrai durate
"date + \"1M\""           # Aggiungi 1 mese
"date - \"2h\""           # Sottrai 2 ore
"now() + \"1 day\""       # Domani
"today() + \"7d\""        # Una settimana da oggi

# Sottrai date per differenza millisecondi
"now() - file.ctime"

# Aritmetica durata complessa
"now() + (duration('1d') * 2)"
```

### Funzioni Stringa

**Campo:** `string.length`

| Funzione        | Firma                                          | Descrizione                     |
| --------------- | ---------------------------------------------- | ------------------------------- |
| `contains()`    | `string.contains(value): boolean`              | Controlla sottostringa          |
| `containsAll()` | `string.containsAll(...values): boolean`       | Tutte le sottostringhe presenti |
| `containsAny()` | `string.containsAny(...values): boolean`       | Qualsiasi sottostringa presente |
| `startsWith()`  | `string.startsWith(query): boolean`            | Inizia con query                |
| `endsWith()`    | `string.endsWith(query): boolean`              | Finisce con query               |
| `isEmpty()`     | `string.isEmpty(): boolean`                    | Vuoto o non presente            |
| `lower()`       | `string.lower(): string`                       | A minuscolo                     |
| `title()`       | `string.title(): string`                       | A Title Case                    |
| `trim()`        | `string.trim(): string`                        | Rimuovi whitespace              |
| `replace()`     | `string.replace(pattern, replacement): string` | Sostituisci pattern             |
| `repeat()`      | `string.repeat(count): string`                 | Ripeti stringa                  |
| `reverse()`     | `string.reverse(): string`                     | Inverti stringa                 |
| `slice()`       | `string.slice(start, end?): string`            | Sottostringa                    |
| `split()`       | `string.split(separator, n?): list`            | Dividi in lista                 |

### Funzioni Numero

| Funzione    | Firma                               | Descrizione           |
| ----------- | ----------------------------------- | --------------------- |
| `abs()`     | `number.abs(): number`              | Valore assoluto       |
| `ceil()`    | `number.ceil(): number`             | Arrotonda su          |
| `floor()`   | `number.floor(): number`            | Arrotonda giù         |
| `round()`   | `number.round(digits?): number`     | Arrotonda a cifre     |
| `toFixed()` | `number.toFixed(precision): string` | Notazione punto fisso |
| `isEmpty()` | `number.isEmpty(): boolean`         | Non presente          |

### Funzioni Lista

**Campo:** `list.length`

| Funzione        | Firma                                   | Descrizione                                           |
| --------------- | --------------------------------------- | ----------------------------------------------------- |
| `contains()`    | `list.contains(value): boolean`         | Elemento esiste                                       |
| `containsAll()` | `list.containsAll(...values): boolean`  | Tutti gli elementi esistono                           |
| `containsAny()` | `list.containsAny(...values): boolean`  | Qualsiasi elemento esiste                             |
| `filter()`      | `list.filter(expression): list`         | Filtra per condizione (usa `value`, `index`)          |
| `map()`         | `list.map(expression): list`            | Trasforma elementi (usa `value`, `index`)             |
| `reduce()`      | `list.reduce(expression, initial): any` | Riduci a valore singolo (usa `value`, `index`, `acc`) |
| `flat()`        | `list.flat(): list`                     | Appiattisci liste annidate                            |
| `join()`        | `list.join(separator): string`          | Unisci a stringa                                      |
| `reverse()`     | `list.reverse(): list`                  | Inverti ordine                                        |
| `slice()`       | `list.slice(start, end?): list`         | Sottolista                                            |
| `sort()`        | `list.sort(): list`                     | Ordina ascendente                                     |
| `unique()`      | `list.unique(): list`                   | Rimuovi duplicati                                     |
| `isEmpty()`     | `list.isEmpty(): boolean`               | Nessun elemento                                       |

### Funzioni File

| Funzione        | Firma                              | Descrizione                 |
| --------------- | ---------------------------------- | --------------------------- |
| `asLink()`      | `file.asLink(display?): Link`      | Converti a link             |
| `hasLink()`     | `file.hasLink(otherFile): boolean` | Ha link al file             |
| `hasTag()`      | `file.hasTag(...tags): boolean`    | Ha uno qualsiasi dei tag    |
| `hasProperty()` | `file.hasProperty(name): boolean`  | Ha proprietà                |
| `inFolder()`    | `file.inFolder(folder): boolean`   | In cartella o sottocartella |

### Funzioni Link

| Funzione    | Firma                         | Descrizione          |
| ----------- | ----------------------------- | -------------------- |
| `asFile()`  | `link.asFile(): file`         | Ottieni oggetto file |
| `linksTo()` | `link.linksTo(file): boolean` | Linka al file        |

### Funzioni Oggetto

| Funzione    | Firma                       | Descrizione       |
| ----------- | --------------------------- | ----------------- |
| `isEmpty()` | `object.isEmpty(): boolean` | Nessuna proprietà |
| `keys()`    | `object.keys(): list`       | Lista chiavi      |
| `values()`  | `object.values(): list`     | Lista valori      |

### Funzioni Espressione Regolare

| Funzione    | Firma                             | Descrizione          |
| ----------- | --------------------------------- | -------------------- |
| `matches()` | `regexp.matches(string): boolean` | Testa corrispondenza |

## Tipi Vista

### Vista Tabella

```yaml
views:
  - type: table
    name: "My Table"
    order:
      - file.name
      - status
      - due_date
    summaries:
      price: Sum
      count: Average
```

### Vista Schede

```yaml
views:
  - type: cards
    name: "Gallery"
    order:
      - file.name
      - cover_image
      - description
```

### Vista Lista

```yaml
views:
  - type: list
    name: "Simple List"
    order:
      - file.name
      - status
```

### Vista Mappa

Richiede proprietà latitudine/longitudine e il plugin community Maps.

```yaml
views:
  - type: map
    name: "Locations"
    # Impostazioni specifiche mappa per proprietà lat/lng
```

## Formule Sommario Default

| Nome        | Tipo Input | Descrizione                |
| ----------- | ---------- | -------------------------- |
| `Average`   | Number     | Media matematica           |
| `Min`       | Number     | Numero più piccolo         |
| `Max`       | Number     | Numero più grande          |
| `Sum`       | Number     | Somma di tutti i numeri    |
| `Range`     | Number     | Max - Min                  |
| `Median`    | Number     | Mediana matematica         |
| `Stddev`    | Number     | Deviazione standard        |
| `Earliest`  | Date       | Data più vecchia           |
| `Latest`    | Date       | Data più recente           |
| `Range`     | Date       | Ultima - Prima (data)      |
| `Checked`   | Boolean    | Conteggio valori true      |
| `Unchecked` | Boolean    | Conteggio valori false     |
| `Empty`     | Any        | Conteggio valori vuoti     |
| `Filled`    | Any        | Conteggio valori non vuoti |
| `Unique`    | Any        | Conteggio valori unici     |

## Incorporare Bases

Incorpora in file Markdown:

```markdown
![[MyBase.base]]

<!-- Vista specifica -->

![[MyBase.base#View Name]]
```

## Regole Quoting YAML

- Usa apici singoli per formule contenenti apici doppi: `'if(done, "Yes", "No")'`
- Usa apici doppi per stringhe semplici: `"My View Name"`
- Escapa apici annidati propriamente in espressioni complesse

## Riferimenti

- [Sintassi Bases](https://help.obsidian.md/bases/syntax)
- [Funzioni](https://help.obsidian.md/bases/functions)
- [Viste](https://help.obsidian.md/bases/views)
- [Formule](https://help.obsidian.md/formulas)
