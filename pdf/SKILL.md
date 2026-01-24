---
name: pdf
description: Toolkit completo per manipolazione PDF: estrazione testo/tabelle, creazione, unione/divisione e gestione moduli.
---

# Guida Processamento PDF

## Panoramica

Questa guida copre operazioni essenziali di processamento PDF usando librerie Python e tool da riga di comando. Per funzionalità avanzate, librerie JavaScript ed esempi dettagliati, vedi reference.md. Se devi compilare un modulo PDF, leggi forms.md e segui le sue istruzioni.

## Avvio Rapido

```python
from pypdf import PdfReader, PdfWriter

# Leggi un PDF
reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

# Estrai testo
text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Librerie Python

### pypdf - Operazioni Base

#### Unire PDF

```python
from pypdf import PdfWriter, PdfReader

writer = PdfWriter()
for pdf_file in ["doc1.pdf", "doc2.pdf", "doc3.pdf"]:
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        writer.add_page(page)

with open("merged.pdf", "wb") as output:
    writer.write(output)
```

#### Dividere PDF

```python
reader = PdfReader("input.pdf")
for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)
    with open(f"page_{i+1}.pdf", "wb") as output:
        writer.write(output)
```

#### Estrarre Metadati

```python
reader = PdfReader("document.pdf")
meta = reader.metadata
print(f"Title: {meta.title}")
print(f"Author: {meta.author}")
print(f"Subject: {meta.subject}")
print(f"Creator: {meta.creator}")
```

#### Ruotare Pagine

```python
reader = PdfReader("input.pdf")
writer = PdfWriter()

page = reader.pages[0]
page.rotate(90)  # Ruota 90 gradi orario
writer.add_page(page)

with open("rotated.pdf", "wb") as output:
    writer.write(output)
```

### pdfplumber - Estrazione Testo e Tabelle

#### Estrai Testo con Layout

```python
import pdfplumber

with pdfplumber.open("document.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

#### Estrai Tabelle

```python
with pdfplumber.open("document.pdf") as pdf:
    for i, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for j, table in enumerate(tables):
            print(f"Table {j+1} on page {i+1}:")
            for row in table:
                print(row)
```

#### Estrazione Tabelle Avanzata

```python
import pandas as pd

with pdfplumber.open("document.pdf") as pdf:
    all_tables = []
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            if table:  # Controlla se la tabella non è vuota
                df = pd.DataFrame(table[1:], columns=table[0])
                all_tables.append(df)

# Combina tutte le tabelle
if all_tables:
    combined_df = pd.concat(all_tables, ignore_index=True)
    combined_df.to_excel("extracted_tables.xlsx", index=False)
```

### reportlab - Creare PDF

#### Creazione PDF Base

```python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

c = canvas.Canvas("hello.pdf", pagesize=letter)
width, height = letter

# Aggiungi testo
c.drawString(100, height - 100, "Hello World!")
c.drawString(100, height - 120, "This is a PDF created with reportlab")

# Aggiungi una linea
c.line(100, height - 140, 400, height - 140)

# Salva
c.save()
```

#### Creare PDF con Pagine Multiple

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate("report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Aggiungi contenuto
title = Paragraph("Report Title", styles['Title'])
story.append(title)
story.append(Spacer(1, 12))

body = Paragraph("This is the body of the report. " * 20, styles['Normal'])
story.append(body)
story.append(PageBreak())

# Pagina 2
story.append(Paragraph("Page 2", styles['Heading1']))
story.append(Paragraph("Content for page 2", styles['Normal']))

# Build PDF
doc.build(story)
```

## Tool Riga di Comando

### pdftotext (poppler-utils)

```bash
# Estrai testo
pdftotext input.pdf output.txt

# Estrai testo preservando layout
pdftotext -layout input.pdf output.txt

# Estrai pagine specifiche
pdftotext -f 1 -l 5 input.pdf output.txt  # Pagine 1-5
```

### qpdf

```bash
# Unisci PDF
qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf

# Dividi pagine
qpdf input.pdf --pages . 1-5 -- pages1-5.pdf
qpdf input.pdf --pages . 6-10 -- pages6-10.pdf

# Ruota pagine
qpdf input.pdf output.pdf --rotate=+90:1  # Ruota pagina 1 di 90 gradi

# Rimuovi password
qpdf --password=mypassword --decrypt encrypted.pdf decrypted.pdf
```

### pdftk (se disponibile)

```bash
# Unisci
pdftk file1.pdf file2.pdf cat output merged.pdf

# Dividi
pdftk input.pdf burst

# Ruota
pdftk input.pdf rotate 1east output rotated.pdf
```

## Task Comuni

### Estrai Testo da PDF Scansionati

```python
# Richiede: pip install pytesseract pdf2image
import pytesseract
from pdf2image import convert_from_path

# Converti PDF in immagini
images = convert_from_path('scanned.pdf')

# OCR ogni pagina
text = ""
for i, image in enumerate(images):
    text += f"Page {i+1}:\n"
    text += pytesseract.image_to_string(image)
    text += "\n\n"

print(text)
```

### Aggiungi Filigrana (Watermark)

```python
from pypdf import PdfReader, PdfWriter

# Crea watermark (o carica esistente)
watermark = PdfReader("watermark.pdf").pages[0]

# Applica a tutte le pagine
reader = PdfReader("document.pdf")
writer = PdfWriter()

for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)

with open("watermarked.pdf", "wb") as output:
    writer.write(output)
```

### Estrai Immagini

```bash
# Usando pdfimages (poppler-utils)
pdfimages -j input.pdf output_prefix

# Questo estrae tutte le immagini come output_prefix-000.jpg, output_prefix-001.jpg, ecc.
```

### Protezione Password

```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("input.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

# Aggiungi password
writer.encrypt("userpassword", "ownerpassword")

with open("encrypted.pdf", "wb") as output:
    writer.write(output)
```

## Riferimento Rapido

| Task                 | Miglior Tool                    | Comando/Codice             |
| -------------------- | ------------------------------- | -------------------------- |
| Unire PDF            | pypdf                           | `writer.add_page(page)`    |
| Dividere PDF         | pypdf                           | Una pagina per file        |
| Estrarre testo       | pdfplumber                      | `page.extract_text()`      |
| Estrarre tabelle     | pdfplumber                      | `page.extract_tables()`    |
| Creare PDF           | reportlab                       | Canvas o Platypus          |
| Unione riga comando  | qpdf                            | `qpdf --empty --pages ...` |
| OCR PDF scansionati  | pytesseract                     | Converti a immagine prima  |
| Compilare moduli PDF | pdf-lib o pypdf (vedi forms.md) | Vedi forms.md              |

## Prossimi Passi

- Per uso avanzato pypdfium2, vedi reference.md
- Per librerie JavaScript (pdf-lib), vedi reference.md
- Se devi compilare un modulo PDF, segui le istruzioni in forms.md
- Per guide troubleshooting, vedi reference.md
