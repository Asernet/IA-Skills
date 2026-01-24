---
name: json-canvas
description: Crea e modifica file JSON Canvas (.canvas) con nodi e connessioni. Utile per mind map o diagrammi in Obsidian.
---

# Skill JSON Canvas

Questa skill abilita agenti skills-compatibili a creare ed editare file JSON Canvas validi (`.canvas`) usati in Obsidian e altre applicazioni.

## Panoramica

JSON Canvas è un formato file aperto per dati infinite canvas. I file Canvas usano l'estensione `.canvas` e contengono JSON valido che segue la [Spec JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/).

## Struttura File

Un file canvas contiene due array di primo livello:

```json
{
  "nodes": [],
  "edges": []
}
```

- `nodes` (opzionale): Array di oggetti nodo
- `edges` (opzionale): Array di oggetti edge che connettono nodi

## Nodi

I nodi sono oggetti piazzati sulla canvas. Ci sono quattro tipi di nodo:

- `text` - Contenuto testo con Markdown
- `file` - Riferimento a file/allegati
- `link` - URL esterno
- `group` - Contenitore visivo per altri nodi

### Ordinamento Z-Index

I nodi sono ordinati per z-index nell'array:

- Primo nodo = layer inferiore (visualizzato sotto gli altri)
- Ultimo nodo = layer superiore (visualizzato sopra gli altri)

### Attributi Nodo Generici

Tutti i nodi condividono questi attributi:

| Attributo | Richiesto | Tipo        | Descrizione                                  |
| --------- | --------- | ----------- | -------------------------------------------- |
| `id`      | Sì        | string      | Identificatore unico per il nodo             |
| `type`    | Sì        | string      | Tipo nodo: `text`, `file`, `link`, o `group` |
| `x`       | Sì        | integer     | Posizione X in pixel                         |
| `y`       | Sì        | integer     | Posizione Y in pixel                         |
| `width`   | Sì        | integer     | Larghezza in pixel                           |
| `height`  | Sì        | integer     | Altezza in pixel                             |
| `color`   | No        | canvasColor | Colore nodo (vedi sezione Colore)            |

### Nodi Testo

I nodi testo contengono contenuto Markdown.

```json
{
  "id": "6f0ad84f44ce9c17",
  "type": "text",
  "x": 0,
  "y": 0,
  "width": 400,
  "height": 200,
  "text": "# Hello World\n\nThis is **Markdown** content."
}
```

| Attributo | Richiesto | Tipo   | Descrizione                          |
| --------- | --------- | ------ | ------------------------------------ |
| `text`    | Sì        | string | Testo semplice con sintassi Markdown |

### Nodi File

I nodi file referenziano file o allegati (immagini, video, PDF, note, ecc.).

```json
{
  "id": "a1b2c3d4e5f67890",
  "type": "file",
  "x": 500,
  "y": 0,
  "width": 400,
  "height": 300,
  "file": "Attachments/diagram.png"
}
```

```json
{
  "id": "b2c3d4e5f6789012",
  "type": "file",
  "x": 500,
  "y": 400,
  "width": 400,
  "height": 300,
  "file": "Notes/Project Overview.md",
  "subpath": "#Implementation"
}
```

| Attributo | Richiesto | Tipo   | Descrizione                                   |
| --------- | --------- | ------ | --------------------------------------------- |
| `file`    | Sì        | string | Percorso al file all'interno del sistema      |
| `subpath` | No        | string | Link a intestazione o blocco (inizia con `#`) |

### Nodi Link

I nodi link visualizzano URL esterni.

```json
{
  "id": "c3d4e5f678901234",
  "type": "link",
  "x": 1000,
  "y": 0,
  "width": 400,
  "height": 200,
  "url": "https://obsidian.md"
}
```

| Attributo | Richiesto | Tipo   | Descrizione |
| --------- | --------- | ------ | ----------- |
| `url`     | Sì        | string | URL esterno |

### Nodi Gruppo

I nodi gruppo sono contenitori visivi per organizzare altri nodi.

```json
{
  "id": "d4e5f6789012345a",
  "type": "group",
  "x": -50,
  "y": -50,
  "width": 1000,
  "height": 600,
  "label": "Project Overview",
  "color": "4"
}
```

```json
{
  "id": "e5f67890123456ab",
  "type": "group",
  "x": 0,
  "y": 700,
  "width": 800,
  "height": 500,
  "label": "Resources",
  "background": "Attachments/background.png",
  "backgroundStyle": "cover"
}
```

| Attributo         | Richiesto | Tipo   | Descrizione                   |
| ----------------- | --------- | ------ | ----------------------------- |
| `label`           | No        | string | Etichetta testo per il gruppo |
| `background`      | No        | string | Percorso immagine sfondo      |
| `backgroundStyle` | No        | string | Stile rendering sfondo        |

#### Stili Sfondo

| Valore   | Descrizione                                           |
| -------- | ----------------------------------------------------- |
| `cover`  | Riempie intera larghezza e altezza del nodo           |
| `ratio`  | Mantiene aspect ratio immagine sfondo                 |
| `repeat` | Ripete immagine come pattern in entrambe le direzioni |

## Edges (Connessioni)

Gli edge sono linee che connettono i nodi.

```json
{
  "id": "f67890123456789a",
  "fromNode": "6f0ad84f44ce9c17",
  "toNode": "a1b2c3d4e5f67890"
}
```

```json
{
  "id": "0123456789abcdef",
  "fromNode": "6f0ad84f44ce9c17",
  "fromSide": "right",
  "fromEnd": "none",
  "toNode": "b2c3d4e5f6789012",
  "toSide": "left",
  "toEnd": "arrow",
  "color": "1",
  "label": "leads to"
}
```

| Attributo  | Richiesto | Tipo        | Default | Descrizione                         |
| ---------- | --------- | ----------- | ------- | ----------------------------------- |
| `id`       | Sì        | string      | -       | Identificatore unico per l'edge     |
| `fromNode` | Sì        | string      | -       | ID Nodo dove inizia la connessione  |
| `fromSide` | No        | string      | -       | Lato dove inizia l'edge             |
| `fromEnd`  | No        | string      | `none`  | Forma all'inizio dell'edge          |
| `toNode`   | Sì        | string      | -       | ID Nodo dove finisce la connessione |
| `toSide`   | No        | string      | -       | Lato dove finisce l'edge            |
| `toEnd`    | No        | string      | `arrow` | Forma alla fine dell'edge           |
| `color`    | No        | canvasColor | -       | Colore linea                        |
| `label`    | No        | string      | -       | Etichetta testo per l'edge          |

### Valori Lato

| Valore   | Descrizione             |
| -------- | ----------------------- |
| `top`    | Lato superiore del nodo |
| `right`  | Lato destro del nodo    |
| `bottom` | Lato inferiore del nodo |
| `left`   | Lato sinistro del nodo  |

### Forme Estremità

| Valore  | Descrizione             |
| ------- | ----------------------- |
| `none`  | Nessuna forma estremità |
| `arrow` | Estremità freccia       |

## Colori

Il tipo `canvasColor` può essere specificato in due modi:

### Colori Hex

```json
{
  "color": "#FF0000"
}
```

### Colori Preset

```json
{
  "color": "1"
}
```

| Preset | Colore    |
| ------ | --------- |
| `"1"`  | Rosso     |
| `"2"`  | Arancione |
| `"3"`  | Giallo    |
| `"4"`  | Verde     |
| `"5"`  | Ciano     |
| `"6"`  | Viola     |

Nota: Valori colore specifici per i preset sono intenzionalmente non definiti, permettendo alle applicazioni di usare i propri colori brand.

## Generazione ID

ID nodo ed edge devono essere stringhe uniche. Obsidian genera ID esadecimali a 16 caratteri:

```json
"id": "6f0ad84f44ce9c17"
```

## Linee Guida Layout

### Posizionamento

- Coordinate possono essere negative (la canvas si estende infinitamente)
- `x` aumenta verso destra
- `y` aumenta verso il basso
- Posizione si riferisce all'angolo in alto a sinistra del nodo

### Dimensioni Raccomandate

| Tipo Nodo      | Larghezza Suggerita | Altezza Suggerita |
| -------------- | ------------------- | ----------------- |
| Testo piccolo  | 200-300             | 80-150            |
| Testo medio    | 300-450             | 150-300           |
| Testo grande   | 400-600             | 300-500           |
| Anteprima file | 300-500             | 200-400           |
| Anteprima link | 250-400             | 100-200           |
| Gruppo         | Varies              | Varies            |

### Spaziatura

- Lascia 20-50px padding dentro i gruppi
- Spazia i nodi 50-100px per leggibilità
- Allinea nodi alla griglia (multipli di 10 o 20) per layout più puliti

## Regole Validazione

1. Tutti i valori `id` devono essere unici attraverso nodi ed edge
2. `fromNode` e `toNode` devono referenziare ID nodo esistenti
3. Campi richiesti devono essere presenti per ogni tipo nodo
4. `type` deve essere uno di: `text`, `file`, `link`, `group`
5. `backgroundStyle` deve essere uno di: `cover`, `ratio`, `repeat`
6. `fromSide`, `toSide` deve essere uno di: `top`, `right`, `bottom`, `left`
7. `fromEnd`, `toEnd` deve essere uno di: `none`, `arrow`
8. Preset colore devono essere `"1"` attraverso `"6"` o colore hex valido

## Riferimenti

- [JSON Canvas Spec 1.0](https://jsoncanvas.org/spec/1.0/)
- [JSON Canvas GitHub](https://github.com/obsidianmd/jsoncanvas)
