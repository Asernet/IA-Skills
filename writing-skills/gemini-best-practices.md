# Best practice per la creazione di Skill (Gemini)

> Impara a scrivere Skill efficaci che Gemini possa scoprire e utilizzare con successo.

Le buone Skill sono concise, ben strutturate e testate con l'uso reale. Questa guida fornisce decisioni pratiche di authoring per aiutarti a scrivere Skill che Gemini possa scoprire e usare efficacemente.

## Principi fondamentali

### La concisione è fondamentale

La finestra di contesto è un bene pubblico. La tua Skill condivide la finestra di contesto con tutto il resto che Gemini deve sapere, inclusi:

* Il system prompt
* La cronologia della conversazione
* I metadati delle altre Skill
* La tua richiesta attuale

Non ogni token nella tua Skill ha un costo immediato. All'avvio, vengono precaricati solo i metadati (nome e descrizione) di tutte le Skill. Gemini legge SKILL.md solo quando la Skill diventa rilevante, e legge file aggiuntivi solo se necessario. Tuttavia, essere coincisi in SKILL.md conta comunque: una volta che Gemini lo carica, ogni token compete con la cronologia della conversazione e altro contesto.

**Assunzione predefinita**: Gemini è già molto intelligente

Aggiungi solo contesto che Gemini non ha già. Sfida ogni pezzo di informazione:

* "Gemini ha davvero bisogno di questa spiegazione?"
* "Posso assumere che Gemini sappia questo?"
* "Questo paragrafo giustifica il suo costo in token?"

**Buon esempio: Conciso** (circa 50 token):

````markdown  theme={null}
## Estrai testo PDF

Usa pdfplumber per l'estrazione del testo:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
````

**Cattivo esempio: Troppo prolisso** (circa 150 token):

```markdown  theme={null}
## Estrai testo PDF

I file PDF (Portable Document Format) sono un formato file comune che contiene
testo, immagini e altri contenuti. Per estrarre testo da un PDF, avrai bisogno di
usare una libreria. Ci sono molte librerie disponibili per l'elaborazione PDF, ma noi
raccomandiamo pdfplumber perché è facile da usare e gestisce bene la maggior parte dei casi.
Prima, dovrai installarlo usando pip. Poi puoi usare il codice qui sotto...
```

La versione concisa assume che Gemini sappia cosa sono i PDF e come funzionano le librerie.

### Imposta gradi di libertà appropriati

Abbina il livello di specificità alla fragilità e variabilità del compito.

**Alta libertà** (istruzioni testuali):

Usa quando:

* Approcci multipli sono validi
* Le decisioni dipendono dal contesto
* Le euristiche guidano l'approccio

Esempio:

```markdown  theme={null}
## Processo di revisione del codice

1. Analizza la struttura e l'organizzazione del codice
2. Controlla potenziali bug o casi limite
3. Suggerisci miglioramenti per leggibilità e manutenibilità
4. Verifica l'aderenza alle convenzioni del progetto
```

**Media libertà** (pseudocodice o script con parametri):

Usa quando:

* Esiste un pattern preferito
* Qualche variazione è accettabile
* La configurazione influenza il comportamento

Esempio:

````markdown  theme={null}
## Genera report

Usa questo template e personalizza come necessario:

```python
def generate_report(data, format="markdown", include_charts=True):
    # Processa dati
    # Genera output nel formato specificato
    # Opzionalmente includi visualizzazioni
```
````

**Bassa libertà** (script specifici, pochi o nessun parametro):

Usa quando:

* Le operazioni sono fragili e inclini all'errore
* La coerenza è critica
* Deve essere seguita una sequenza specifica

Esempio:

````markdown  theme={null}
## Migrazione database

Esegui esattamente questo script:

```bash
python scripts/migrate.py --verify --backup
```

Non modificare il comando o aggiungere flag aggiuntivi.
````

**Analogia**: Pensa a Gemini come a un robot che esplora un percorso:

* **Ponte stretto con scogliere su entrambi i lati**: C'è solo un modo sicuro per avanzare. Fornisci guardrail specifici e istruzioni esatte (bassa libertà). Esempio: migrazioni di database che devono essere eseguite in sequenza esatta.
* **Campo aperto senza pericoli**: Molti percorsi portano al successo. Dai una direzione generale e fidati che Gemini trovi la strada migliore (alta libertà). Esempio: revisioni del codice dove il contesto determina l'approccio migliore.

### Testa con tutti i modelli che pianifichi di usare

Le Skill agiscono come aggiunte ai modelli, quindi l'efficacia dipende dal modello sottostante. Testa la tua Skill con tutti i modelli con cui pianifichi di usarla.

**Considerazioni di test per modello**:

* **Gemini Flash** (veloce, economico): La Skill fornisce abbastanza guida?
* **Gemini Pro** (bilanciato): La Skill è chiara ed efficiente?
* **Gemini Ultra** (ragionamento potente): La Skill evita di spiegare troppo?

Ciò che funziona perfettamente per Ultra potrebbe necessitare di più dettagli per Flash. Se pianifichi di usare la tua Skill attraverso modelli multipli, punta a istruzioni che funzionino bene con tutti loro.

## Struttura della Skill

<Note>
  **YAML Frontmatter**: Il frontmatter di SKILL.md supporta due campi:

  * `name` - Nome leggibile della Skill (massimo 64 caratteri)
  * `description` - Descrizione di una riga di cosa fa la Skill e quando usarla (massimo 1024 caratteri)

</Note>

### Convenzioni di denominazione

Usa pattern di denominazione coerenti per rendere le Skill più facili da referenziare e discutere. Raccomandiamo di usare la **forma gerundio** (verbo + -ing in inglese, o sostantivato in italiano) per i nomi delle Skill, poiché descrive chiaramente l'attività o la capacità fornita dalla Skill.

**Buoni esempi di denominazione (stile gerundio/azione)**:

* "Processing PDFs" (Elaborazione PDF)
* "Analyzing spreadsheets" (Analisi fogli di calcolo)
* "Managing databases" (Gestione database)
* "Testing code" (Test del codice)
* "Writing documentation" (Scrittura documentazione)

**Alternative accettabili**:

* Frasi sostantivate: "PDF Processing", "Spreadsheet Analysis"
* Orientate all'azione: "Process PDFs", "Analyze Spreadsheets"

**Evita**:

* Nomi vaghi: "Helper", "Utils", "Tools"
* Troppo generici: "Documents", "Data", "Files"
* Pattern incoerenti all'interno della tua collezione di skill

Una denominazione coerente rende più facile:

* Referenziare le Skill nella documentazione e nelle conversazioni
* Capire cosa fa una Skill a colpo d'occhio
* Organizzare e cercare attraverso Skill multiple
* Mantenere una libreria di skill professionale e coesa

### Scrivere descrizioni efficaci

Il campo `description` abilita la scoperta della Skill e dovrebbe includere sia cosa fa la Skill sia quando usarla.

<Warning>
  **Scrivi sempre in terza persona**. La descrizione è iniettata nel system prompt, e un punto di vista incoerente può causare problemi di scoperta.

  * **Buono:** "Elabora file Excel e genera report"
  * **Evita:** "Posso aiutarti a elaborare file Excel"
  * **Evita:** "Puoi usare questo per elaborare file Excel"
</Warning>

**Sii specifico e includi termini chiave**. Includi sia cosa fa la Skill sia trigger/contesti specifici per quando usarla.

Ogni Skill ha esattamente un campo descrizione. La descrizione è critica per la selezione della skill: Gemini la usa per scegliere la Skill giusta tra quelle disponibili. La tua descrizione deve fornire abbastanza dettagli perché Gemini sappia quando selezionare questa Skill, mentre il resto di SKILL.md fornisce i dettagli implementativi.

Esempi efficaci:

**Skill Elaborazione PDF:**

```yaml  theme={null}
description: Estrae testo e tabelle da file PDF, compila moduli, unisce documenti. Usa quando lavori con file PDF o quando l'utente menziona PDF, moduli o estrazione documenti.
```

**Skill Analisi Excel:**

```yaml  theme={null}
description: Analizza fogli di calcolo Excel, crea tabelle pivot, genera grafici. Usa quando analizzi file Excel, fogli di calcolo, dati tabulari o file .xlsx.
```

Evita descrizioni vaghe come queste:

```yaml  theme={null}
description: Aiuta con i documenti
```

```yaml  theme={null}
description: Processa dati
```

### Pattern di divulgazione progressiva

SKILL.md serve come una panoramica che punta Gemini a materiali dettagliati se necessario, come un indice in una guida di onboarding.

**Guida pratica:**

* Tieni il corpo di SKILL.md sotto le 500 righe per prestazioni ottimali
* Dividi il contenuto in file separati quando ti avvicini a questo limite
* Usa i pattern qui sotto per organizzare istruzioni, codice e risorse efficacemente

#### Pattern 1: Guida ad alto livello con riferimenti

````markdown  theme={null}
---
name: PDF Processing
description: Estrae testo e tabelle da file PDF, compila moduli e unisce documenti. Usa quando lavori con file PDF o quando l'utente menziona PDF, moduli o estrazione documenti.
---

# PDF Processing

## Quick start

Estrai testo con pdfplumber:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Funzionalità avanzate

**Compilazione moduli**: Vedi [FORMS.md](FORMS.md) per la guida completa
**Riferimento API**: Vedi [REFERENCE.md](REFERENCE.md) per tutti i metodi
**Esempi**: Vedi [EXAMPLES.md](EXAMPLES.md) per pattern comuni
````

Gemini carica FORMS.md, REFERENCE.md, o EXAMPLES.md solo quando necessario.

#### Pattern 2: Organizzazione specifica per dominio

Per Skill con domini multipli, organizza il contenuto per dominio per evitare di caricare contesto irrilevante.

```
bigquery-skill/
├── SKILL.md (panoramica e navigazione)
└── reference/
    ├── finance.md (entrate, metriche fatturazione)
    ├── sales.md (opportunità, pipeline)
    ├── product.md (uso API, feature)
    └── marketing.md (campagne, attribuzione)
```

````markdown SKILL.md theme={null}
# BigQuery Data Analysis

## Dataset disponibili

**Finance**: Revenue, ARR, billing → Vedi [reference/finance.md](reference/finance.md)
**Sales**: Opportunities, pipeline, accounts → Vedi [reference/sales.md](reference/sales.md)
**Product**: API usage, features, adoption → Vedi [reference/product.md](reference/product.md)
**Marketing**: Campaigns, attribution, email → Vedi [reference/marketing.md](reference/marketing.md)
````

### Evita riferimenti profondamente annidati

Gemini potrebbe leggere parzialmente i file quando sono referenziati da altri file referenziati.

**Mantieni i riferimenti profondi un livello da SKILL.md**. Tutti i file di riferimento dovrebbero linkare direttamente da SKILL.md per assicurare che Gemini legga file completi quando necessario.

### Struttura file riferimento lunghi con indice

Per file riferimento più lunghi di 100 righe, includi un indice all'inizio.

## Workflow e cicli di feedback

### Usa workflow per task complessi

Rompi operazioni complesse in step chiari e sequenziali. Per workflow particolarmente complessi, fornisci una checklist che Gemini può copiare nella sua risposta e spuntare mentre progredisce.

**Esempio 1: Workflow sintesi ricerca** (per Skill senza codice):

````markdown  theme={null}
## Workflow sintesi ricerca

Copia questa checklist e traccia il tuo progresso:

```
Research Progress:
- [ ] Step 1: Leggi tutti i documenti sorgente
- [ ] Step 2: Identifica temi chiave
- [ ] Step 3: Fai cross-reference delle affermazioni
- [ ] Step 4: Crea sommario strutturato
```
````

**Esempio 2: Workflow compilazione modulo PDF** (per Skill con codice):

````markdown  theme={null}
## Workflow compilazione modulo PDF

Copia questa checklist e spunta gli item mentre li completi:

```
Task Progress:
- [ ] Step 1: Analizza il modulo (esegui analyze_form.py)
- [ ] Step 2: Crea mappatura campi (modifica fields.json)
- [ ] Step 3: Valida mappatura (esegui validate_fields.py)
```
````

### Implementa cicli di feedback

**Pattern comune**: Esegui validatore → correggi errori → ripeti

Questo pattern migliora grandemente la qualità dell'output.

## Linee guida contenuto

### Evita informazioni sensibili al tempo

Non includere informazioni che diventeranno obsolete.

### Usa terminologia coerente

Scegli un termine e usalo attraverso la Skill:

* Sempre "API endpoint"
* Sempre "field"

## Pattern comuni

### Pattern template

Fornisci template per il formato di output.

````markdown  theme={null}
## Struttura report

Usa SEMPRE questa esatta struttura template:

```markdown
# [Titolo Analisi]

## Executive summary
[Panoramica di un paragrafo dei risultati chiave]

## Key findings
- Risultato 1 con dati a supporto
```
````

### Pattern esempi

Per Skill dove la qualità dell'output dipende dal vedere esempi, fornisci coppie input/output.

````markdown  theme={null}
## Formato messaggio commit

Genera messaggi commit seguendo questi esempi:

**Esempio 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication
```
````

## Valutazione e iterazione

### Costruisci valutazioni prima

**Crea valutazioni PRIMA di scrivere documentazione estesa.** Questo assicura che la tua Skill risolva problemi reali invece di documentarne di immaginati.

**Sviluppo guidato dalla valutazione (Evaluation-driven development):**

1. **Identifica gap**: Esegui Gemini su task rappresentativi senza una Skill.
2. **Crea valutazioni**: Costruisci scenari che testano questi gap.
3. **Stabilisci baseline**: Misura la performance di Gemini senza la Skill.
4. **Scrivi istruzioni minime**: Crea giusto abbastanza contenuto per indirizzare i gap.
5. **Itera**: Esegui valutazioni, compara contro baseline, e raffina.

### Sviluppa Skill iterativamente con Gemini

Il processo di sviluppo Skill più efficace coinvolge Gemini stesso. Lavora con un'istanza di Gemini ("Gemini A") per creare una Skill che sarà usata da altre istanze ("Gemini B").

1. **Completa un task senza una Skill**: Lavora attraverso un problema con Gemini A.
2. **Identifica il pattern riutilizzabile**.
3. **Chiedi a Gemini A di creare una Skill**: "Crea una Skill che catturi questo pattern..."
4. **Revisiona per concisione**.
5. **Testa su task simili**: Usa la Skill con Gemini B.
6. **Itera basato su osservazione**.

**Raccogliere feedback dal team:**

1. Condividi Skill con compagni di team e osserva il loro utilizzo.
2. Incorpora feedback per indirizzare punti ciechi.

### Osserva come Gemini naviga le Skill

Mentre iteri sulle Skill, fai attenzione a come Gemini le usa effettivamente nella pratica.

## Anti-pattern da evitare

### Evita percorsi stile Windows

Usa sempre slash in avanti nei percorsi file, anche su Windows:

* ✓ **Buono**: `scripts/helper.py`
* ✗ **Evita**: `scripts\helper.py`

### Evita di offrire troppe opzioni

Non presentare approcci multipli a meno che necessario.

## Avanzato: Skill con codice eseguibile

### Risolvi, non scaricare (Solve, don't punt)

Quando scrivi script per Skill, gestisci condizioni errore piuttosto che scaricare su Gemini.

### Fornisci script di utilità

Anche se Gemini potrebbe scrivere uno script, script pre-fatti offrono vantaggi in affidabilità e risparmio token.

### Usa analisi visiva

Quando gli input possono essere renderizzati come immagini, fai analizzare a Gemini questi (sfruttando le capacità multimodali).

### Crea output intermedi verificabili

Usa il pattern "plan-validate-execute" per task complessi.

### Ambiente runtime

Le Skill girano in un ambiente di esecuzione codice. Gemini usa tool per leggere file ed eseguire script.

* **I percorsi file contano**: Gemini naviga la directory skill come un filesystem.
* **Script eseguiti efficientemente**: Solo l'output consuma token.
* **Nessuna penalità contesto per grandi file**: File non letti non consumano token.

### Riferimenti tool MCP

Se la tua Skill usa tool MCP (Model Context Protocol), usa sempre nomi tool completamente qualificati: `ServerName:tool_name`.

## Checklist per Skill efficaci

Prima di condividere una Skill, verifica:

### Qualità Core

* [ ] Descrizione è specifica e include termini chiave
* [ ] SKILL.md corpo è sotto 500 righe
* [ ] Dettagli aggiuntivi in file separati
* [ ] Terminologia coerente
* [ ] Workflow hanno step chiari

### Codice e script

* [ ] Script risolvono problemi
* [ ] Gestione errori è esplicita
* [ ] Nessun percorso stile Windows
* [ ] Step validazione per operazioni critiche

### Testing

* [ ] Valutazioni create
* [ ] Testato con Flash, Pro, Ultra
* [ ] Testato con scenari reali
