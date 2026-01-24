---
name: xlsx
description: Creazione, modifica e analisi avanzata di fogli di calcolo Excel (.xlsx) con formule e formattazione.
---

# Requisiti per Output

## Tutti i file Excel

### Zero Errori Formula

- Ogni modello Excel DEVE essere consegnato con ZERO errori formula (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preservare Template Esistenti (quando si aggiornano template)

- Studia e combacia ESATTAMENTE formato, stile e convenzioni esistenti quando modifichi file
- Mai imporre formattazione standardizzata su file con pattern stabiliti
- Convenzioni template esistenti sovrascrivono SEMPRE queste linee guida

## Modelli finanziari

### Standard Color Coding

A meno che non dichiarato altrimenti dall'utente o template esistente

#### Convenzioni Colore Standard-Industria

- **Testo Blu (RGB: 0,0,255)**: Input hardcoded, e numeri che gli utenti cambieranno per scenari
- **Testo Nero (RGB: 0,0,0)**: TUTTE le formule e calcoli
- **Testo Verde (RGB: 0,128,0)**: Link che tirano da altri worksheet all'interno dello stesso workbook
- **Testo Rosso (RGB: 255,0,0)**: Link esterni ad altri file
- **Sfondo Giallo (RGB: 255,255,0)**: Assunzioni chiave che necessitano attenzione o celle che necessitano di essere aggiornate

### Standard Formattazione Numeri

#### Regole Formato Richieste

- **Anni**: Formatta come stringhe testo (es., "2024" non "2.024")
- **Valuta**: Usa formato $#.##0; SEMPRE specificare unità negli header ("Revenue ($mm)")
- **Zeri**: Usa formattazione numero per rendere tutti gli zeri "-", incluse percentuali (es., "$#.##0;($#.##0);-")
- **Percentuali**: Default a formato 0,0% (uno decimale)
- **Multipli**: Formatta come 0,0x per multipli valutazione (EV/EBITDA, P/E)
- **Numeri negativi**: Usa parentesi (123) non meno -123

### Regole Costruzione Formula

#### Piazzamento Assunzioni

- Piazza TUTTE le assunzioni (tassi crescita, margini, multipli, ecc.) in celle assunzione separate
- Usa riferimenti cella invece di valori hardcoded nelle formule
- Esempio: Usa =B5*(1+$B$6) invece di =B5*1,05

#### Prevenzione Errore Formula

- Verifica che tutti i riferimenti cella siano corretti
- Controlla errori off-by-one nei range
- Assicura formule consistenti attraverso tutti i periodi proiezione
- Testa con casi limite (valori zero, numeri negativi)
- Verifica nessun riferimento circolare non intenzionale

#### Requisiti Documentazione per Hardcode

- Commenta o in celle a fianco (se fine tabella). Formato: "Source: [System/Document], [Date], [Specific Reference], [URL if applicable]"

# Creazione, modifica e analisi XLSX

## Panoramica

Un utente potrebbe chiederti di creare, editare o analizzare i contenuti di un file .xlsx. Hai tool e workflow diversi disponibili per task diversi.

## Requisiti Importanti

**LibreOffice Richiesto per Ricalcolo Formule**: Puoi assumere che LibreOffice sia installato per ricalcolare valori formula usando lo script `recalc.py`. Lo script configura automaticamente LibreOffice alla prima esecuzione

## Lettura e analisi dati

### Analisi dati con pandas

Per analisi dati, visualizzazione e operazioni base, usa **pandas** che fornisce potenti capacità manipolazione dati:

```python
import pandas as pd

# Read Excel
df = pd.read_excel('file.xlsx')  # Default: first sheet
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets as dict

# Analyze
df.head()      # Preview data
df.info()      # Column info
df.describe()  # Statistics

# Write Excel
df.to_excel('output.xlsx', index=False)
```

## Workflow File Excel

## CRITICO: Usa Formule, Non Valori Hardcoded

**Usa sempre formule Excel invece di calcolare valori in Python e hardcodarli.** Questo assicura che il foglio di calcolo rimanga dinamico e aggiornabile.

### ❌ SBAGLIATO - Hardcodare Valori Calcolati

```python
# Bad: Calculating in Python and hardcoding result
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcodes 5000
```

### ✅ CORRETTO - Usare Formule Excel

```python
# Good: Let Excel calculate the sum
sheet['B10'] = '=SUM(B2:B9)'
```

Questo si applica a TUTTI i calcoli - totali, percentuali, rapporti, differenze, ecc.

## Workflow Comune

1. **Scegli tool**: pandas per dati, openpyxl per formule/formattazione
2. **Crea/Carica**: Crea nuovo workbook o carica file esistente
3. **Modifica**: Aggiungi/edita dati, formule e formattazione
4. **Salva**: Scrivi su file
5. **Ricalcola formule (OBBLIGATORIO SE SI USANO FORMULE)**: Usa lo script recalc.py
   ```bash
   python recalc.py output.xlsx
   ```
6. **Verifica e fixa qualsiasi errore**:
   - Lo script ritorna JSON con dettagli errore
   - Se `status` è `errors_found`, controlla `error_summary` per tipi errore specifici e locazioni
   - Fixa errori identificati e ricalcola di nuovo

### Creare nuovi file Excel

```python
# Using openpyxl for formulas and formatting
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active

# Add data
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'
sheet.append(['Row', 'of', 'data'])

# Add formula
sheet['B2'] = '=SUM(A1:A10)'

# Formatting
sheet['A1'].font = Font(bold=True, color='FF0000')

wb.save('output.xlsx')
```

### Editare file Excel esistenti

```python
# Using openpyxl to preserve formulas and formatting
from openpyxl import load_workbook

# Load existing file
wb = load_workbook('existing.xlsx')
sheet = wb.active

# Modify cells
sheet['A1'] = 'New Value'
sheet.insert_rows(2)  # Insert row at position 2

wb.save('modified.xlsx')
```

## Ricalcolare formule

File Excel creati o modificati da openpyxl contengono formule come stringhe ma non valori calcolati. Usa lo script `recalc.py` fornito per ricalcolare formule:

```bash
python recalc.py <excel_file> [timeout_seconds]
```

## Checklist Verifica Formula

Controlli veloci per assicurare che le formule funzionino correttamente:

### Verifica Essenziale

- [ ] **Testa 2-3 riferimenti campione**: Verifica tirino valori corretti prima di costruire modello completo
- [ ] **Mappatura colonne**: Conferma colonne Excel combacino (es., colonna 64 = BL, non BK)
- [ ] **Offset righe**: Ricorda righe Excel sono 1-indexed (DataFrame row 5 = Excel row 6)

### Trappole Comuni

- [ ] **Gestione NaN**: Controlla valori null con `pd.notna()`
- [ ] **Divisione per zero**: Controlla denominatori prima di usare `/` in formule (#DIV/0!)
- [ ] **Riferimenti sbagliati**: Verifica tutti i riferimenti cella puntino a celle intese (#REF!)

## Best Practice

### Selezione Libreria

- **pandas**: Migliore per analisi dati, operazioni bulk ed export dati semplice
- **openpyxl**: Migliore per formattazione complessa, formule e feature Excel-specifiche

### Lavorare con openpyxl

- Indici cella sono 1-based
- Usa `data_only=True` per leggere valori calcolati
- **Warning**: Se aperto con `data_only=True` e salvato, le formule sono rimpiazzate con valori e perse permanentemente

### Lavorare con pandas

- Specifica tipi dati per evitare problemi inferenza
- Gestisci date propriamente

## Linee Guida Stile Codice

**IMPORTANTE**: Quando generi codice Python per operazioni Excel:

- Scrivi codice Python minimo, conciso senza commenti non necessari
- Evita nomi variabili verposi e operazioni ridondanti
- Evita statement print non necessari

**Per file Excel stessi**:

- Aggiungi commenti a celle con formule complesse o assunzioni importanti
- Documenta sorgenti dati per valori hardcoded
