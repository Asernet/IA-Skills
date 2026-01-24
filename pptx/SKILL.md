---
name: pptx
description: Creazione, modifica e analisi di presentazioni .pptx, inclusi layout e note del relatore.
---

# Creazione, modifica e analisi PPTX

## Panoramica

Un utente potrebbe chiederti di creare, modificare o analizzare i contenuti di un file .pptx. Un file .pptx è essenzialmente un archivio ZIP contenente file XML e altre risorse che puoi leggere o modificare. Hai diversi strumenti e workflow disponibili per diversi task.

## Lettura e analisi contenuto

### Estrazione testo

Se hai solo bisogno di leggere i contenuti testuali di una presentazione, dovresti convertire il documento a markdown:

```bash
# Converti documento a markdown
python -m markitdown path-to-file.pptx
```

### Accesso XML Grezzo

Hai bisogno di accesso XML grezzo per: commenti, note relatore, layout slide, animazioni, elementi design e formattazione complessa. Per ognuna di queste funzionalità, dovrai spacchettare una presentazione e leggere i suoi contenuti XML grezzi.

#### Spacchettare un file

`python ooxml/scripts/unpack.py <office_file> <output_dir>`

**Nota**: Lo script unpack.py è situato a `skills/pptx/ooxml/scripts/unpack.py` relativo alla root del progetto. Se lo script non esiste a questo percorso, usa `find . -name "unpack.py"` per localizzarlo.

#### Strutture file chiave

- `ppt/presentation.xml` - Metadati presentazione principali e riferimenti slide
- `ppt/slides/slide{N}.xml` - Contenuti slide individuali (slide1.xml, slide2.xml, ecc.)
- `ppt/notesSlides/notesSlide{N}.xml` - Note relatore per ogni slide
- `ppt/comments/modernComment_*.xml` - Commenti per slide specifiche
- `ppt/slideLayouts/` - Template layout per slide
- `ppt/slideMasters/` - Template slide master
- `ppt/theme/` - Informazioni tema e stile
- `ppt/media/` - Immagini e altri file media

#### Estrazione tipografia e colore

**Quando dato un design esempio da emulare**: Analizza sempre prima la tipografia e i colori della presentazione usando i metodi sotto:

1. **Leggi file tema**: Controlla `ppt/theme/theme1.xml` per colori (`<a:clrScheme>`) e font (`<a:fontScheme>`)
2. **Campiona contenuto slide**: Esamina `ppt/slides/slide1.xml` for uso font effettivo (`<a:rPr>`) e colori
3. **Cerca pattern**: Usa grep per trovare riferimenti colore (`<a:solidFill>`, `<a:srgbClr>`) e font attraverso tutti i file XML

## Creare una nuova presentazione PowerPoint **senza template**

Quando crei una nuova presentazione PowerPoint da zero, usa il workflow **html2pptx** per convertire slide HTML in PowerPoint con posizionamento accurato.

### Principi di Design

**CRITICO**: Prima di creare qualsiasi presentazione, analizza il contenuto e scegli elementi di design appropriati:

1. **Considera l'argomento**: Di cosa tratta questa presentazione? Quale tono, industria o mood suggerisce?
2. **Controlla branding**: Se l'utente menziona un'azienda/organizzazione, considera i loro colori brand e identità
3. **Combacia palette al contenuto**: Seleziona colori che riflettono il soggetto
4. **Dichiara il tuo approccio**: Spiega le tue scelte di design prima di scrivere codice

**Requisiti**:

- ✅ Dichiara il tuo approccio di design informato dal contenuto PRIMA di scrivere codice
- ✅ Usa solo font web-safe: Arial, Helvetica, Times New Roman, Georgia, Courier New, Verdana, Tahoma, Trebuchet MS, Impact
- ✅ Crea chiara gerarchia visiva attraverso dimensione, peso e colore
- ✅ Assicura leggibilità: forte contrasto, testo appropriatamente dimensionato, allineamento pulito
- ✅ Sii consistente: ripeti pattern, spaziatura e linguaggio visivo attraverso le slide

#### Selezione Palette Colori

**Scegliere colori creativamente**:

- **Pensa oltre i default**: Quali colori combaciano genuinamente con questo argomento specifico? Evita scelte pilota automatico.
- **Considera angoli multipli**: Argomento, industria, mood, livello energia, audience target, identità brand (se menzionata)
- **Sii avventuroso**: Prova combinazioni inaspettate - una presentazione healthcare non deve essere verde, finance non deve essere navy
- **Costruisci la tua palette**: Scegli 3-5 colori che lavorano insieme (colori dominanti + toni supporto + accento)
- **Assicura contrasto**: Il testo deve essere chiaramente leggibile sugli sfondi

**Palette colori esempio** (usa queste per scintilla creatività - scegline una, adattala, o crea la tua):

1. **Classic Blue**: Deep navy (#1C2833), slate gray (#2E4053), silver (#AAB7B8), off-white (#F4F6F6)
2. **Teal & Coral**: Teal (#5EA8A7), deep teal (#277884), coral (#FE4447), white (#FFFFFF)
3. **Bold Red**: Red (#C0392B), bright red (#E74C3C), orange (#F39C12), yellow (#F1C40F), green (#2ECC71)
4. **Warm Blush**: Mauve (#A49393), blush (#EED6D3), rose (#E8B4B8), cream (#FAF7F2)
5. **Burgundy Luxury**: Burgundy (#5D1D2E), crimson (#951233), rust (#C15937), gold (#997929)
6. **Deep Purple & Emerald**: Purple (#B165FB), dark blue (#181B24), emerald (#40695B), white (#FFFFFF)
7. **Cream & Forest Green**: Cream (#FFE1C7), forest green (#40695B), white (#FCFCFC)
8. **Pink & Purple**: Pink (#F8275B), coral (#FF574A), rose (#FF737D), purple (#3D2F68)
9. **Lime & Plum**: Lime (#C5DE82), plum (#7C3A5F), coral (#FD8C6E), blue-gray (#98ACB5)
10. **Black & Gold**: Gold (#BF9A4A), black (#000000), cream (#F4F6F6)
11. **Sage & Terracotta**: Sage (#87A96B), terracotta (#E07A5F), cream (#F4F1DE), charcoal (#2C2C2C)
12. **Charcoal & Red**: Charcoal (#292929), red (#E33737), light gray (#CCCBCB)
13. **Vibrant Orange**: Orange (#F96D00), light gray (#F2F2F2), charcoal (#222831)
14. **Forest Green**: Black (#191A19), green (#4E9F3D), dark green (#1E5128), white (#FFFFFF)
15. **Retro Rainbow**: Purple (#722880), pink (#D72D51), orange (#EB5C18), amber (#F08800), gold (#DEB600)
16. **Vintage Earthy**: Mustard (#E3B448), sage (#CBD18F), forest green (#3A6B35), cream (#F4F1DE)
17. **Coastal Rose**: Old rose (#AD7670), beaver (#B49886), eggshell (#F3ECDC), ash gray (#BFD5BE)
18. **Orange & Turquoise**: Light orange (#FC993E), grayish turquoise (#667C6F), white (#FCFCFC)

#### Opzioni Dettagli Visivi

**Geometric Patterns**:

- Divisori sezione diagonali invece che orizzontali
- Larghezze colonna asimmetriche (30/70, 40/60, 25/75)
- Header testo ruotati a 90° o 270°
- Cornici circolari/esagonali per immagini
- Forme accento triangolari negli angoli
- Forme sovrapposte per profondità

**Trattamenti Bordo & Cornice**:

- Bordi singoli spessi (10-20pt) colre unico su un lato solo
- Bordi doppia linea con colori contrastanti
- Parentesi angolo invece di cornici intere
- Bordi a L (alto+sinistra o basso+destra)
- Accenti sottolineatura sotto intestazioni (3-5pt spessore)

**Trattamenti Tipografia**:

- Contrasto dimensione estremo (72pt titoli vs 11pt corpo)
- Intestazioni tutto maiuscolo con spaziatura lettere ampia
- Sezioni numerate in tipo display sovradimensionato
- Monospace (Courier New) per dati/statistiche/contenuto tecnico
- Font condensati (Arial Narrow) per informazioni dense
- Testo delineato per enfasi

**Stile Grafici & Dati**:

- Grafici monocromatici con singolo colore accento per dati chiave
- Grafici a barre orizzontali invece che verticali
- Dot plot invece di grafici a barre
- Griglie minime o nessuna
- Etichette dati direttamente su elementi (nessuna legenda)
- Numeri sovradimensionati per metriche chiave

**Innovazioni Layout**:

- Immagini a tutta pagina con sovrapposizioni testo
- Colonna laterale (20-30% larghezza) per navigazione/contesto
- Sistemi griglia modulare (blocchi 3×3, 4×4)
- Flusso contenuto Z-pattern o F-pattern
- Caselle testo fluttuanti sopra forme colorate
- Layout multi-colonna stile rivista

**Trattamenti Sfondo**:

- Blocchi colore solido occupanti 40-60% della slide
- Riempimenti gradiente (verticale o diagonale solo)
- Sfondi divisi (due colori, diagonale o verticale)
- Bande colore da bordo a bordo
- Spazio negativo come elemento di design

### Consigli Layout

**Quando crei slide con grafici o tabelle:**

- **Layout due colonne (PREFERITO)**: Usa un header che copre intera larghezza, poi due colonne sotto - testo/bullet in una colonna e contenuto in evidenza nell'altra. Questo fornisce bilanciamento migliore e rende grafici/tabelle più leggibili. Usa flexbox con larghezze colonna disuguali (es. split 40%/60%) per ottimizzare spazio per ogni contenuto.
- **Layout full-slide**: Lascia che il contenuto in evidenza (grafico/tabella) prenda l'intera slide per massimo impatto e leggibilità
- **MAI impilare verticalmente**: Non piazzare grafici/tabelle sotto testo in una singola colonna - questo causa scarsa leggibilità e problemi di layout

### Workflow

1. **OBBLIGATORIO - LEGGI INTERO FILE**: Leggi [`html2pptx.md`](html2pptx.md) completamente dall'inizio alla fine. **MAI impostare limiti di range quando leggi questo file.** Leggi il contenuto file completo per sintassi dettagliata, regole formattazione critiche e best practice prima di procedere con la creazione presentazione.
2. Crea un file HTML per ogni slide con dimensioni appropriate (es., 720pt × 405pt per 16:9)
   - Usa `<p>`, `<h1>`-`<h6>`, `<ul>`, `<ol>` per tutto il contenuto testo
   - Usa `class="placeholder"` per aree dove grafici/tabelle saranno aggiunti (renderizza con sfondo grigio per visibilità)
   - **CRITICO**: Rasterizza gradienti e icone come immagini PNG PRIMA usando Sharp, poi referenzia in HTML
   - **LAYOUT**: Per slide con grafici/tabelle/immagini, usa o layout full-slide o due colonne per migliore leggibilità
3. Crea ed esegui un file JavaScript usando la libreria [`html2pptx.js`](scripts/html2pptx.js) per convertire slide HTML in PowerPoint e salvare la presentazione
   - Usa la funzione `html2pptx()` per processare ogni file HTML
   - Aggiungi grafici e tabelle ad aree placeholder usando API PptxGenJS
   - Salva la presentazione usando `pptx.writeFile()`
4. **Validazione visiva**: Genera thumbnail e ispeziona per problemi layout
   - Crea griglia thumbnail: `python scripts/thumbnail.py output.pptx workspace/thumbnails --cols 4`
   - Leggi ed esamina attentamente l'immagine thumbnail per:
     - **Taglio testo**: Testo tagliato da barre header, forme o bordi slide
     - **Sovrapposizione testo**: Testo che si sovrappone con altro testo o forme
     - **Problemi posizionamento**: Contenuto troppo vicino a confini slide o altri elementi
     - **Problemi contrasto**: Contrasto insufficiente tra testo e sfondi
   - Se problemi trovati, aggiusta margini/spaziatura/colori HTML e rigenera la presentazione
   - Ripeti finché tutte le slide sono visivamente corrette

## Modificare una presentazione PowerPoint esistente

Quando editi slide in una presentazione PowerPoint esistente, devi lavorare con il formato raw Office Open XML (OOXML). Questo coinvolge spacchettare il file .pptx, editare il contenuto XML e rimpacchettarlo.

### Workflow

1. **OBBLIGATORIO - LEGGI INTERO FILE**: Leggi [`ooxml.md`](ooxml.md) (~500 righe) completamente dall'inizio alla fine. **MAI impostare limiti di range quando leggi questo file.** Leggi il contenuto file completo per guida dettagliata su struttura OOXML e workflow editing prima di qualsiasi editing presentazione.
2. Spacchetta la presentazione: `python ooxml/scripts/unpack.py <office_file> <output_dir>`
3. Edita i file XML (primariamente `ppt/slides/slide{N}.xml` e file correlati)
4. **CRITICO**: Valida immediatamente dopo ogni edit e fixa qualsiasi errore validazione prima di procedere: `python ooxml/scripts/validate.py <dir> --original <file>`
5. Impacchetta la presentazione finale: `python ooxml/scripts/pack.py <input_directory> <office_file>`

## Creare una nuova presentazione PowerPoint **usando un template**

Quando devi creare una presentazione che segue il design di un template esistente, dovrai duplicare e riordinare slide template prima di rimpiazzare contesto placeholder.

### Workflow

1. **Estrai testo template E crea griglia thumbnail visuale**:
   - Estrai testo: `python -m markitdown template.pptx > template-content.md`
   - Leggi `template-content.md`: Leggi l'intero file per capire i contenuti della presentazione template. **MAI impostare limiti di range quando leggi questo file.**
   - Crea griglie thumbnail: `python scripts/thumbnail.py template.pptx`
   - Vedi sezione [Creare Griglie Thumbnail](#creating-thumbnail-grids) per più dettagli

2. **Analizza template e salva inventario su un file**:
   - **Analisi Visuale**: Revisiona griglia(e) thumbnail per capire layout slide, pattern design e struttura visuale
   - Crea e salva un file inventario template a `template-inventory.md` contenente:

     ```markdown
     # Template Inventory Analysis

     **Total Slides: [count]**
     **IMPORTANT: Slides are 0-indexed (first slide = 0, last slide = count-1)**

     ## [Category Name]

     - Slide 0: [Layout code if available] - Description/purpose
     - Slide 1: [Layout code] - Description/purpose
     - Slide 2: [Layout code] - Description/purpose
       [... OGNI slide deve essere listata individualmente con il suo indice ...]
     ```

   - **Usando la griglia thumbnail**: Referenzia le thumbnail visuali per identificare:
     - Pattern layout (slide titolo, layout contenuto, divisori sezione)
     - Posizioni e conteggi placeholder immagine
     - Consistenza design attraverso gruppi slide
     - Gerarchia visuale e struttura
   - Questo file inventario è RICHIESTO per selezionare template appropriati nel prossimo passo

3. **Crea outline presentazione basato su inventario template**:
   - Revisiona template disponibili dal passo 2.
   - Scegli un template intro o titolo per la prima slide. Questo dovrebbe essere uno dei primi template.
   - Scegli layout sicuri, basati su testo per le altre slide.
   - **CRITICO: Combacia struttura layout al contenuto effettivo**:
     - Layout colonna singola: Usa per narrativa unificata o argomento singolo
     - Layout due colonne: Usa SOLO quando hai esattamente 2 item/concetti distinti
     - Layout tre colonne: Usa SOLO quando hai esattamente 3 item/concetti distinti
     - Layout immagine + testo: Usa SOLO quando hai immagini effettive da inserire
     - Layout citazione: Usa SOLO per citazioni effettive da persone (con attribuzione), mai per enfasi
     - Mai usare layout con più placeholder di quanti contenuti hai
     - Se hai 2 item, non forzarli in un layout 3-colonne
     - Se hai 4+ item, considera di rompere in slide multiple o usare formato lista
   - Conta i tuoi pezzi di contenuto effettivi PRIMA di selezionare il layout
   - Verifica che ogni placeholder nel layout scelto sarà riempito con contenuto significativo
   - Seleziona un'opzione che rappresenta il **miglior** layout per ogni sezione contenuto.
   - Salva `outline.md` con contenuto E mappatura template che sfrutta design disponibili
   - Esempio mappatura template:
     ```
     # Template slides to use (0-based indexing)
     # WARNING: Verify indices are within range! Template with 73 slides has indices 0-72
     # Mapping: slide numbers from outline -> template slide indices
     template_mapping = [
         0,   # Use slide 0 (Title/Cover)
         34,  # Use slide 34 (B1: Title and body)
         34,  # Use slide 34 again (duplicate for second B1)
         50,  # Use slide 50 (E1: Quote)
         54,  # Use slide 54 (F2: Closing + Text)
     ]
     ```

4. **Duplica, riordina e cancella slide usando `rearrange.py`**:
   - Usa lo script `scripts/rearrange.py` per creare una nuova presentazione con slide nell'ordine desiderato:
     ```bash
     python scripts/rearrange.py template.pptx working.pptx 0,34,34,50,52
     ```
   - Lo script gestisce duplicazione slide ripetute, cancellazione slide non usate e riordinamento automaticamente
   - Indici slide sono 0-based (prima slide è 0, seconda è 1, ecc.)
   - Lo stesso indice slide può apparire più volte per duplicare quella slide

5. **Estrai TUTTO il testo usando lo script `inventory.py`**:
   - **Esegui estrazione inventario**:
     ```bash
     python scripts/inventory.py working.pptx text-inventory.json
     ```
   - **Leggi text-inventory.json**: Leggi l'intero file text-inventory.json per capire tutte le forme e le loro proprietà. **MAI impostare limiti di range quando leggi questo file.**

   - Caratteristiche chiave:
     - **Slide**: Nominate come "slide-0", "slide-1", ecc.
     - **Forme**: Ordinate per posizione visuale (alto-a-basso, sinistra-a-destra) come "shape-0", "shape-1", ecc.
     - **Tipi Placeholder**: TITLE, CENTER_TITLE, SUBTITLE, BODY, OBJECT, o null
     - **Font size default**: `default_font_size` in punti estratto da placeholder layout (quando disponibile)
     - **Numeri slide filtrati**: Forme con tipo placeholder SLIDE_NUMBER sono automaticamente escluse dall'inventario
     - **Bullets**: Quando `bullet: true`, `level` è sempre incluso (anche se 0)
     - **Spaziatura**: `space_before`, `space_after`, e `line_spacing` in punti (solo incluso quando impostato)
     - **Colori**: `color` per RGB (es., "FF0000"), `theme_color` per colori tema (es., "DARK_1")
     - **Proprietà**: Solo valori non-default sono inclusi nell'output

6. **Genera testo sostitutivo e salva i dati in un file JSON**
   Basato sull'inventario testo dal passo precedente:
   - **CRITICO**: Prima verifica quali forme esistono nell'inventario - referenzia solo forme che sono effettivamente presenti
   - **VALIDAZIONE**: Lo script replace.py validerà che tutte le forme nel tuo JSON sostitutivo esistano nell'inventario
     - Se referenzi una forma inesistente, otterrai un errore che mostra forme disponibili
     - Se referenzi una slide inesistente, otterrai un errore indicante che la slide non esiste
     - Tutti gli errori di validazione sono mostrati in una volta prima che lo script esca
   - **IMPORTANTE**: Lo script replace.py usa inventory.py internamente per identificare TUTTE le forme testo
   - **PULIZIA AUTOMATICA**: TUTTE le forme testo dall'inventario saranno pulite a meno che non fornisci "paragraphs" per esse
   - Aggiungi un campo "paragraphs" alle forme che necessitano contenuto (non "replacement_paragraphs")
   - Forme senza "paragraphs" nel JSON sostitutivo avranno il loro testo pulito automaticamente
   - Paragrafi con bullet saranno automaticamente allineati a sinistra. Non impostare proprietà `alignment` su quando `"bullet": true`
   - Genera contenuto sostitutivo appropriato per testo placeholder
   - Usa dimensione forma per determinare lunghezza contenuto appropriata
   - **CRITICO**: Includi proprietà paragrafo dall'inventario originale - non fornire solo testo
   - **IMPORTANTE**: Quando bullet: true, NON includere simboli bullet (•, -, \*) nel testo - sono aggiunti automaticamente
   - **REGOLE FORMATTAZIONE ESSENZIALI**:
     - Intestazioni/titoli dovrebbero tipicamente avere `"bold": true`
     - Item lista dovrebbero avere `"bullet": true, "level": 0` (level è richiesto quando bullet è true)
     - Preserva qualsiasi proprietà allineamento (es., `"alignment": "CENTER"` per testo centrato)
     - Includi proprietà font quando diverse dal default (es., `"font_size": 14.0`, `"font_name": "Lora"`)
     - Colori: Usa `"color": "FF0000"` per RGB o `"theme_color": "DARK_1"` per colori tema
     - Lo script di sostituzione si aspetta **paragrafi propriamente formattati**, non solo stringhe testo
     - **Forme sovrapposte**: Preferisci forme con default_font_size più grande o placeholder_type più appropriato
   - Salva l'inventario aggiornato con sostituzioni a `replacement-text.json`
   - **ATTENZIONE**: Layout template diversi hanno conteggi forme diversi - controlla sempre l'inventario attuale prima di creare sostituzioni

   **Forme non listate nel JSON sostitutivo sono automaticamente pulite**.

   **Pattern formattazione comuni per presentazioni**:
   - Slide Titolo: Testo grassetto, a volte centrato
   - Intestazioni Sezione dentro slide: Testo grassetto
   - Liste Bullet: Ogni item necessita `"bullet": true, "level": 0`
   - Testo Corpo: Solitamente nessuna proprietà speciale necessaria
   - Citazioni: Possono avere allineamento speciale o proprietà font

7. **Applica sostituzioni usando lo script `replace.py`**

   ```bash
   python scripts/replace.py working.pptx replacement-text.json output.pptx
   ```

   Lo script:
   - Prima estrae l'inventario di TUTTE le forme testo usando funzioni da inventory.py
   - Valida che tutte le forme nel JSON sostitutivo esistano nell'inventario
   - Pulisce testo da TUTTE le forme identificate nell'inventario
   - Applica nuovo testo solo a forme con "paragraphs" definito nel JSON sostitutivo
   - Preserva formattazione applicando proprietà paragrafo dal JSON
   - Gestisce bullet, allineamento, proprietà font e colori automaticamente
   - Salva la presentazione aggiornata

## Creare Griglie Thumbnail

Per creare griglie thumbnail visuali di slide PowerPoint per analisi rapida e riferimento:

```bash
python scripts/thumbnail.py template.pptx [output_prefix]
```

**Funzionalità**:

- Crea: `thumbnails.jpg` (o `thumbnails-1.jpg`, `thumbnails-2.jpg`, ecc. per grandi deck)
- Default: 5 colonne, max 30 slide per griglia (5×6)
- Prefisso personalizzato: `python scripts/thumbnail.py template.pptx my-grid`
  - Nota: Il prefisso output dovrebbe includere il percorso se vuoi output in una directory specifica (es., `workspace/my-grid`)
- Aggiusta colonne: `--cols 4` (range: 3-6, influenza slide per griglia)
- Limiti Griglia: 3 col = 12 slide/griglia, 4 col = 20, 5 col = 30, 6 col = 42
- Slide sono zero-indexed (Slide 0, Slide 1, ecc.)

**Casi d'uso**:

- Analisi Template: Capisci velocemente layout slide e pattern design
- Revisione Contenuto: Panoramica visiva dell'intera presentazione
- Riferimento Navigazione: Trova slide specifiche per la loro apparenza
- Controllo Qualità: Verifica che tutte le slide siano formattate propriamente

## Convertire Slide in Immagini

Per analizzare visivamente slide PowerPoint, convertile in immagini usando un processo a due step:

1. **Converti PPTX a PDF**:

   ```bash
   soffice --headless --convert-to pdf template.pptx
   ```

2. **Converti pagine PDF a immagini JPEG**:
   ```bash
   pdftoppm -jpeg -r 150 template.pdf slide
   ```
   Questo crea file come `slide-1.jpg`, `slide-2.jpg`, ecc.

Opzioni:

- `-r 150`: Imposta risoluzione a 150 DPI (aggiusta per bilancio qualità/dimensione)
- `-jpeg`: Output formato JPEG (usa `-png` per PNG se preferito)
- `-f N`: Prima pagina da convertire (es., `-f 2` inizia da pagina 2)
- `-l N`: Ultima pagina da convertire (es., `-l 5` ferma a pagina 5)
- `slide`: Prefisso per file output

Esempio per range specifico:

```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 template.pdf slide  # Converte solo pagine 2-5
```

## Linee Guida Stile Codice

**IMPORTANTE**: Quando generi codice per operazioni PPTX:

- Scrivi codice conciso
- Evita nomi variabili prolissi e operazioni ridondanti
- Evita statement print non necessari

## Dipendenze

Dipendenze richieste (dovrebbero essere già installate):

- **markitdown**: `pip install "markitdown[pptx]"` (per estrazione testo da presentazioni)
- **pptxgenjs**: `npm install -g pptxgenjs` (per creare presentazioni via html2pptx)
- **playwright**: `npm install -g playwright` (per rendering HTML in html2pptx)
- **react-icons**: `npm install -g react-icons react react-dom` (per icone)
- **sharp**: `npm install -g sharp` (per rasterizzazione SVG e processamento immagini)
- **LibreOffice**: `sudo apt-get install libreoffice` (per conversione PDF)
- **Poppler**: `sudo apt-get install poppler-utils` (per pdftoppm per convertire PDF a immagini)
- **defusedxml**: `pip install defusedxml` (per parsing XML sicuro)
