---
name: docx
description: Creazione, modifica e analisi di documenti .docx con supporto per revisioni, commenti e formattazione.
---

# Creazione, modifica e analisi DOCX

## Panoramica

Un utente potrebbe chiederti di creare, modificare o analizzare i contenuti di un file .docx. Un file .docx è essenzialmente un archivio ZIP contenente file XML e altre risorse che puoi leggere o modificare. Hai diversi strumenti e workflow disponibili per diversi task.

## Albero Decisionale Workflow

### Lettura/Analisi Contenuto

Usa sezioni "Estrazione testo" o "Accesso XML Grezzo" sotto

### Creazione Nuovo Documento

Usa workflow "Creazione nuovo documento Word"

### Modifica Documento Esistente

- **Tuo documento + modifiche semplici**
  Usa workflow "Editing OOXML Base"

- **Documento di qualcun altro**
  Usa **"Workflow Redlining"** (default raccomandato)

- **Doc legali, accademici, business o governativi**
  Usa **"Workflow Redlining"** (richiesto)

## Lettura e analisi contenuto

### Estrazione testo

Se hai solo bisogno di leggere i contenuti di testo di un documento, dovresti convertire il documento in markdown usando pandoc. Pandoc fornisce supporto eccellente per preservare la struttura del documento e può mostrare le modifiche tracciate:

```bash
# Convert document to markdown with tracked changes
pandoc --track-changes=all path-to-file.docx -o output.md
# Options: --track-changes=accept/reject/all
```

### Accesso XML Grezzo

Hai bisogno di accesso XML grezzo per: commenti, formattazione complessa, struttura documento, media incorporati e metadati. Per ognuna di queste funzionalità, dovrai spacchettare un documento e leggere i suoi contenuti XML grezzi.

#### Spacchettare un file

`python ooxml/scripts/unpack.py <office_file> <output_directory>`

#### Strutture file chiave

- `word/document.xml` - Contenuti documento principale
- `word/comments.xml` - Commenti referenziati in document.xml
- `word/media/` - Immagini e file media incorporati
- Modifiche tracciate usano tag `<w:ins>` (inserimenti) e `<w:del>` (cancellazioni)

## Creazione nuovo documento Word

Quando crei un nuovo documento Word da zero, usa **docx-js**, che ti permette di creare documenti Word usando JavaScript/TypeScript.

### Workflow

1. **OBBLIGATORIO - LEGGI INTERO FILE**: Leggi [`docx-js.md`](docx-js.md) (~500 righe) completamente dall'inizio alla fine. **MAI impostare limiti di range quando leggi questo file.** Leggi il contenuto file completo per sintassi dettagliata, regole di formattazione critiche e best practices prima di procedere con la creazione documento.
2. Crea un file JavaScript/TypeScript usando componenti Document, Paragraph, TextRun (Puoi assumere che tutte le dipendenze siano installate, ma se no, riferisciti alla sezione dipendenze sotto)
3. Esporta come .docx usando Packer.toBuffer()

## Modifica documento Word esistente

Quando modifichi un documento Word esistente, usa la **Libreria Document** (una libreria Python per manipolazione OOXML). La libreria gestisce automaticamente il setup infrastruttura e fornisce metodi per la manipolazione documento. Per scenari complessi, puoi accedere al DOM sottostante direttamente attraverso la libreria.

### Workflow

1. **OBBLIGATORIO - LEGGI INTERO FILE**: Leggi [`ooxml.md`](ooxml.md) (~600 righe) completamente dall'inizio alla fine. **MAI impostare limiti di range quando leggi questo file.** Leggi il contenuto file completo per API Libreria Document e pattern XML per editare direttamente file documento.
2. Spacchetta il documento: `python ooxml/scripts/unpack.py <office_file> <output_directory>`
3. Crea ed esegui uno script Python usando la Libreria Document (vedi sezione "Document Library" in ooxml.md)
4. Impacchetta il documento finale: `python ooxml/scripts/pack.py <input_directory> <office_file>`

La Libreria Document fornisce sia metodi di alto livello per operazioni comuni e accesso DOM diretto per scenari complessi.

## Workflow Redlining per revisione documenti

Questo workflow ti permette di pianificare modifiche tracciate comprensive usando markdown prima di implementarle in OOXML. **CRITICO**: Per modifiche tracciate complete, devi implementare TUTTE le modifiche sistematicamente.

**Strategia Batching**: Raggruppa cambiamenti correlati in batch di 3-10 cambiamenti. Questo rende il debugging gestibile mantenendo l'efficienza. Testa ogni batch prima di muovere al prossimo.

**Principio: Edit Minimi, Precisi**
Quando implementi modifiche tracciate, marca solo il testo che cambia effettivamente. Ripetere testo immutato rende gli edit più difficili da revisionare e appare non professionale. Spezza le sostituzioni in: [testo immutato] + [cancellazione] + [inserimento] + [testo immutato]. Preserva l'RSID del run originale per testo immutato estraendo l'elemento `<w:r>` dall'originale e riusandolo.

Esempio - Cambiare "30 days" a "60 days" in una frase:

```python
# BAD - Replaces entire sentence
'<w:del><w:r><w:delText>The term is 30 days.</w:delText></w:r></w:del><w:ins><w:r><w:t>The term is 60 days.</w:t></w:r></w:ins>'

# GOOD - Only marks what changed, preserves original <w:r> for unchanged text
'<w:r w:rsidR="00AB12CD"><w:t>The term is </w:t></w:r><w:del><w:r><w:delText>30</w:delText></w:r></w:del><w:ins><w:r><w:t>60</w:t></w:r></w:ins><w:r w:rsidR="00AB12CD"><w:t> days.</w:t></w:r>'
```

### Workflow modifiche tracciate

1. **Ottieni rappresentazione markdown**: Converti documento a markdown con modifiche tracciate preservate:

   ```bash
   pandoc --track-changes=all path-to-file.docx -o current.md
   ```

2. **Identifica e raggruppa cambiamenti**: Revisiona il documento e identifica TUTTI i cambiamenti necessari, organizzandoli in batch logici:

   **Metodi localizzazione** (per trovare cambiamenti in XML):
   - Numeri sezione/intestazione (es. "Section 3.2", "Article IV")
   - Identificatori paragrafo se numerati
   - Pattern grep con testo circostante unico
   - Struttura documento (es. "first paragraph", "signature block")
   - **NON usare numeri riga markdown** - non mappano a struttura XML

   **Organizzazione Batch** (raggruppa 3-10 cambiamenti correlati per batch):
   - Per sezione: "Batch 1: Section 2 amendments", "Batch 2: Section 5 updates"
   - Per tipo: "Batch 1: Date corrections", "Batch 2: Party name changes"
   - Per complessità: Inizia con semplici sostituzioni testo, poi affronta cambiamenti strutturali complessi
   - Sequenziale: "Batch 1: Pages 1-3", "Batch 2: Pages 4-6"

3. **Leggi documentazione e spacchetta**:
   - **OBBLIGATORIO - LEGGI INTERO FILE**: Leggi [`ooxml.md`](ooxml.md) (~600 righe) completamente dall'inizio alla fine. **MAI impostare limiti di range quando leggi questo file.** Psta attenzione speciale alle sezioni "Document Library" e "Tracked Change Patterns".
   - **Spacchetta il documento**: `python ooxml/scripts/unpack.py <file.docx> <dir>`
   - **Nota l'RSID suggerito**: Lo script di spacchettamento suggerirà un RSID da usare per le tue modifiche tracciate. Copia questo RSID per uso nel passo 4b.

4. **Implementa cambiamenti in batch**: Raggruppa cambiamenti logicamente (per sezione, per tipo, o per prossimità) e implementali insieme in un singolo script. Questo approccio:
   - Rende il debugging più facile (batch più piccolo = più facile isolare errori)
   - Permette progresso incrementale
   - Mantiene efficienza (dimensione batch di 3-10 cambiamenti funziona bene)

   **Raggruppamenti batch suggeriti:**
   - Per sezione documento (es. "Section 3 changes", "Definitions", "Termination clause")
   - Per tipo cambiamento (es. "Date changes", "Party name updates", "Legal term replacements")
   - Per prossimità (es. "Changes on pages 1-3", "Changes in first half of document")

   Per ogni batch di cambiamenti correlati:

   **a. Mappa testo a XML**: Grep per testo in `word/document.xml` per verificare come il testo è diviso attraverso elementi `<w:r>`.

   **b. Crea ed esegui script**: Usa `get_node` per trovare nodi, implementare cambiamenti, poi `doc.save()`. Vedi sezione **"Document Library"** in ooxml.md per pattern.

   **Nota**: Fai sempre grep `word/document.xml` immediatamente prima di scrivere uno script per ottenere numeri riga correnti e verificare contenuto testo. I numeri riga cambiano dopo ogni esecuzione script.

5. **Impacchetta il documento**: Dopo che tutti i batch sono completi, converti la directory spacchettata indietro a .docx:

   ```bash
   python ooxml/scripts/pack.py unpacked reviewed-document.docx
   ```

6. **Verifica finale**: Fai un controllo comprensivo del documento completo:
   - Converti documento finale a markdown:
     ```bash
     pandoc --track-changes=all reviewed-document.docx -o verification.md
     ```
   - Verifica TUTTI i cambiamenti siano stati applicati correttamente:
     ```bash
     grep "original phrase" verification.md  # Should NOT find it
     grep "replacement phrase" verification.md  # Should find it
     ```
   - Controlla che nessun cambiamento non intenzionale sia stato introdotto

## Convertire Documenti in Immagini

Per analizzare visivamente documenti Word, convertili in immagini usando un processo a due step:

1. **Converti DOCX a PDF**:

   ```bash
   soffice --headless --convert-to pdf document.docx
   ```

2. **Converti pagine PDF a immagini JPEG**:
   ```bash
   pdftoppm -jpeg -r 150 document.pdf page
   ```
   Questo crea file come `page-1.jpg`, `page-2.jpg`, ecc.

Opzioni:

- `-r 150`: Imposta risoluzione a 150 DPI (aggiusta per bilancio qualità/dimensione)
- `-jpeg`: Output formato JPEG (usa `-png` per PNG se preferito)
- `-f N`: Prima pagina da convertire (es., `-f 2` inizia da pagina 2)
- `-l N`: Ultima pagina da convertire (es., `-l 5` ferma a pagina 5)
- `page`: Prefisso per file output

Esempio per range specifico:

```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 document.pdf page  # Converte solo pagine 2-5
```

## Linee Guida Stile Codice

**IMPORTANTE**: Quando generi codice per operazioni DOCX:

- Scrivi codice conciso
- Evita nomi variabili prolissi e operazioni ridondanti
- Evita statement print non necessari

## Dipendenze

Dipendenze richieste (installa se non disponibili):

- **pandoc**: `sudo apt-get install pandoc` (per estrazione testo)
- **docx**: `npm install -g docx` (per creazione nuovi documenti)
- **LibreOffice**: `sudo apt-get install libreoffice` (per conversione PDF)
- **Poppler**: `sudo apt-get install poppler-utils` (per pdftoppm per convertire PDF a immagini)
- **defusedxml**: `pip install defusedxml` (per parsing XML sicuro)
