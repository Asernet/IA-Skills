# Best practice per la creazione di Skill

> Impara a scrivere Skill efficaci che Claude possa scoprire e utilizzare con successo.

Le buone Skill sono concise, ben strutturate e testate con l'uso reale. Questa guida fornisce decisioni pratiche di authoring per aiutarti a scrivere Skill che Claude possa scoprire e usare efficacemente.

Per un background concettuale su come funzionano le Skill, vedi la [Panoramica delle Skill](/en/docs/agents-and-tools/agent-skills/overview).

## Principi fondamentali

### La concisione è fondamentale

La [finestra di contesto](https://platform.claude.com/docs/en/build-with-claude/context-windows) è un bene pubblico. La tua Skill condivide la finestra di contesto con tutto il resto che Claude deve sapere, inclusi:

* Il system prompt
* La cronologia della conversazione
* I metadati delle altre Skill
* La tua richiesta attuale

Non ogni token nella tua Skill ha un costo immediato. All'avvio, vengono precaricati solo i metadati (nome e descrizione) di tutte le Skill. Claude legge SKILL.md solo quando la Skill diventa rilevante, e legge file aggiuntivi solo se necessario. Tuttavia, essere coincisi in SKILL.md conta comunque: una volta che Claude lo carica, ogni token compete con la cronologia della conversazione e altro contesto.

**Assunzione predefinita**: Claude è già molto intelligente

Aggiungi solo contesto che Claude non ha già. Sfida ogni pezzo di informazione:

* "Claude ha davvero bisogno di questa spiegazione?"
* "Posso assumere che Claude sappia questo?"
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

La versione concisa assume che Claude sappia cosa sono i PDF e come funzionano le librerie.

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

**Analogia**: Pensa a Claude come a un robot che esplora un percorso:

* **Ponte stretto con scogliere su entrambi i lati**: C'è solo un modo sicuro per avanzare. Fornisci guardrail specifici e istruzioni esatte (bassa libertà). Esempio: migrazioni di database che devono essere eseguite in sequenza esatta.
* **Campo aperto senza pericoli**: Molti percorsi portano al successo. Dai una direzione generale e fidati che Claude trovi la strada migliore (alta libertà). Esempio: revisioni del codice dove il contesto determina l'approccio migliore.

### Testa con tutti i modelli che pianifichi di usare

Le Skill agiscono come aggiunte ai modelli, quindi l'efficacia dipende dal modello sottostante. Testa la tua Skill con tutti i modelli con cui pianifichi di usarla.

**Considerazioni di test per modello**:

* **Claude Haiku** (veloce, economico): La Skill fornisce abbastanza guida?
* **Claude Sonnet** (bilanciato): La Skill è chiara ed efficiente?
* **Claude Opus** (ragionamento potente): La Skill evita di spiegare troppo?

Ciò che funziona perfettamente per Opus potrebbe necessitare di più dettagli per Haiku. Se pianifichi di usare la tua Skill attraverso modelli multipli, punta a istruzioni che funzionino bene con tutti loro.

## Struttura della Skill

<Note>
  **YAML Frontmatter**: Il frontmatter di SKILL.md supporta due campi:

  * `name` - Nome leggibile della Skill (massimo 64 caratteri)
  * `description` - Descrizione di una riga di cosa fa la Skill e quando usarla (massimo 1024 caratteri)

  Per dettagli completi sulla struttura della Skill, vedi la [Panoramica delle Skill](/en/docs/agents-and-tools/agent-skills/overview#skill-structure).
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

Ogni Skill ha esattamente un campo descrizione. La descrizione è critica per la selezione della skill: Claude la usa per scegliere la Skill giusta tra potenzialmente 100+ Skill disponibili. La tua descrizione deve fornire abbastanza dettagli perché Claude sappia quando selezionare questa Skill, mentre il resto di SKILL.md fornisce i dettagli implementativi.

Esempi efficaci:

**Skill Elaborazione PDF:**

```yaml  theme={null}
description: Estrae testo e tabelle da file PDF, compila moduli, unisce documenti. Usa quando lavori con file PDF o quando l'utente menziona PDF, moduli o estrazione documenti.
```

**Skill Analisi Excel:**

```yaml  theme={null}
description: Analizza fogli di calcolo Excel, crea tabelle pivot, genera grafici. Usa quando analizzi file Excel, fogli di calcolo, dati tabulari o file .xlsx.
```

**Skill Git Commit Helper:**

```yaml  theme={null}
description: Genera messaggi di commit descrittivi analizzando i git diff. Usa quando l'utente chiede aiuto per scrivere messaggi di commit o revisionare modifiche in stage.
```

Evita descrizioni vaghe come queste:

```yaml  theme={null}
description: Aiuta con i documenti
```

```yaml  theme={null}
description: Processa dati
```

```yaml  theme={null}
description: Fa cose con file
```

### Pattern di divulgazione progressiva

SKILL.md serve come una panoramica che punta Claude a materiali dettagliati se necessario, come un indice in una guida di onboarding. Per una spiegazione di come funziona la divulgazione progressiva, vedi [Come funzionano le Skill](/en/docs/agents-and-tools/agent-skills/overview#how-skills-work) nella panoramica.

**Guida pratica:**

* Tieni il corpo di SKILL.md sotto le 500 righe per prestazioni ottimali
* Dividi il contenuto in file separati quando ti avvicini a questo limite
* Usa i pattern qui sotto per organizzare istruzioni, codice e risorse efficacemente

#### Panoramica visiva: Da semplice a complesso

Una Skill basilare inizia con solo un file SKILL.md contenente metadati e istruzioni:

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=87782ff239b297d9a9e8e1b72ed72db9" alt="Simple SKILL.md file showing YAML frontmatter and markdown body" data-og-width="2048" width="2048" data-og-height="1153" height="1153" data-path="images/agent-skills-simple-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=c61cc33b6f5855809907f7fda94cd80e 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=90d2c0c1c76b36e8d485f49e0810dbfd 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=ad17d231ac7b0bea7e5b4d58fb4aeabb 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f5d0a7a3c668435bb0aee9a3a8f8c329 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=0e927c1af9de5799cfe557d12249f6e6 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=46bbb1a51dd4c8202a470ac8c80a893d 2500w" />

Man mano che la tua Skill cresce, puoi raggruppare contenuto aggiuntivo che Claude carica solo quando necessario:

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=a5e0aa41e3d53985a7e3e43668a33ea3" alt="Bundling additional reference files like reference.md and forms.md." data-og-width="2048" width="2048" data-og-height="1327" height="1327" data-path="images/agent-skills-bundling-content.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f8a0e73783e99b4a643d79eac86b70a2 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=dc510a2a9d3f14359416b706f067904a 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=82cd6286c966303f7dd914c28170e385 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=56f3be36c77e4fe4b523df209a6824c6 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=d22b5161b2075656417d56f41a74f3dd 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=3dd4bdd6850ffcc96c6c45fcb0acd6eb 2500w" />

La struttura della directory Skill completa potrebbe apparire così:

```
pdf/
├── SKILL.md              # Istruzioni principali (caricate quando attivata)
├── FORMS.md              # Guida compilazione moduli (caricata se necessario)
├── reference.md          # Riferimento API (caricato se necessario)
├── examples.md           # Esempi d'uso (caricato se necessario)
└── scripts/
    ├── analyze_form.py   # Script utility (eseguito, non caricato)
    ├── fill_form.py      # Script compilazione moduli
    └── validate.py       # Script validazione
```

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

Claude carica FORMS.md, REFERENCE.md, o EXAMPLES.md solo quando necessario.

#### Pattern 2: Organizzazione specifica per dominio

Per Skill con domini multipli, organizza il contenuto per dominio per evitare di caricare contesto irrilevante. Quando un utente chiede metriche di vendita, Claude deve leggere solo schemi relativi alle vendite, non dati finanziari o di marketing. Questo mantiene basso l'uso di token e focalizzato il contesto.

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

## Ricerca rapida

Trova metriche specifiche usando grep:

```bash
grep -i "revenue" reference/finance.md
grep -i "pipeline" reference/sales.md
grep -i "api usage" reference/product.md
```
````

#### Pattern 3: Dettagli condizionali

Mostra contenuto base, link a contenuto avanzato:

```markdown  theme={null}
# DOCX Processing

## Creazione documenti

Usa docx-js per nuovi documenti. Vedi [DOCX-JS.md](DOCX-JS.md).

## Modifica documenti

Per modifiche semplici, modifica l'XML direttamente.

**Per revisioni (tracked changes)**: Vedi [REDLINING.md](REDLINING.md)
**Per dettagli OOXML**: Vedi [OOXML.md](OOXML.md)
```

Claude legge REDLINING.md o OOXML.md solo quando l'utente necessita di quelle funzionalità.

### Evita riferimenti profondamente annidati

Claude potrebbe leggere parzialmente i file quando sono referenziati da altri file referenziati. Quando incontra riferimenti annidati, Claude potrebbe usare comandi come `head -100` per vedere l'anteprima del contenuto piuttosto che leggere interi file, risultando in informazioni incomplete.

**Mantieni i riferimenti profondi un livello da SKILL.md**. Tutti i file di riferimento dovrebbero linkare direttamente da SKILL.md per assicurare che Claude legga file completi quando necessario.

**Cattivo esempio: Troppo profondo**:

```markdown  theme={null}
# SKILL.md
Vedi [advanced.md](advanced.md)...

# advanced.md
Vedi [details.md](details.md)...

# details.md
Ecco l'informazione attuale...
```

**Buon esempio: Profondo un livello**:

```markdown  theme={null}
# SKILL.md

**Uso base**: [istruzioni in SKILL.md]
**Funzionalità avanzate**: Vedi [advanced.md](advanced.md)
**Riferimento API**: Vedi [reference.md](reference.md)
**Esempi**: Vedi [examples.md](examples.md)
```

### Struttura file riferimento lunghi con indice

Per file riferimento più lunghi di 100 righe, includi un indice all'inizio. Questo assicura che Claude possa vedere l'ambito completo delle informazioni disponibili anche quando visualizza anteprime con letture parziali.

**Esempio**:

```markdown  theme={null}
# Riferimento API

## Contenuti
- Autenticazione e setup
- Metodi core (create, read, update, delete)
- Funzionalità avanzate (operazioni batch, webhooks)
- Pattern gestione errori
- Esempi di codice

## Autenticazione e setup
...

## Metodi core
...
```

Claude può quindi leggere il file completo o saltare a sezioni specifiche se necessario.

Per dettagli su come questa architettura basata su filesystem abilita la divulgazione progressiva, vedi la sezione [Runtime environment](#runtime-environment) nell'area Advanced qui sotto.

## Workflow e cicli di feedback

### Usa workflow per task complessi

Rompi operazioni complesse in step chiari e sequenziali. Per workflow particolarmente complessi, fornisci una checklist che Claude può copiare nella sua risposta e spuntare mentre progredisce.

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
- [ ] Step 5: Verifica citazioni
```

**Step 1: Leggi tutti i documenti sorgente**

Revisiona ogni documento nella directory `sources/`. Nota gli argomenti principali e le prove a supporto.

**Step 2: Identifica temi chiave**

Cerca pattern tra le fonti. Quali temi appaiono ripetutamente? Dove concordano o discordano le fonti?

**Step 3: Fai cross-reference delle affermazioni**

Per ogni affermazione maggiore, verifica che appaia nel materiale sorgente. Nota quale fonte supporta ogni punto.

**Step 4: Crea sommario strutturato**

Organizza le scoperte per tema. Includi:
- Affermazione principale
- Prove a supporto dalle fonti
- Punti di vista conflittuali (se presenti)

**Step 5: Verifica citazioni**

Controlla che ogni affermazione referenzi il documento sorgente corretto. Se le citazioni sono incomplete, torna allo Step 3.
````

Questo esempio mostra come i workflow si applicano a compiti di analisi che non richiedono codice. Il pattern checklist funziona per qualsiasi processo complesso e multi-step.

**Esempio 2: Workflow compilazione modulo PDF** (per Skill con codice):

````markdown  theme={null}
## Workflow compilazione modulo PDF

Copia questa checklist e spunta gli item mentre li completi:

```
Task Progress:
- [ ] Step 1: Analizza il modulo (esegui analyze_form.py)
- [ ] Step 2: Crea mappatura campi (modifica fields.json)
- [ ] Step 3: Valida mappatura (esegui validate_fields.py)
- [ ] Step 4: Compila il modulo (esegui fill_form.py)
- [ ] Step 5: Verifica output (esegui verify_output.py)
```

**Step 1: Analizza il modulo**

Esegui: `python scripts/analyze_form.py input.pdf`

Questo estrae campi modulo e le loro posizioni, salvando in `fields.json`.

**Step 2: Crea mappatura campi**

Modifica `fields.json` per aggiungere valori per ogni campo.

**Step 3: Valida mappatura**

Esegui: `python scripts/validate_fields.py fields.json`

Correggi qualsiasi errore di validazione prima di continuare.

**Step 4: Compila il modulo**

Esegui: `python scripts/fill_form.py input.pdf fields.json output.pdf`

**Step 5: Verifica output**

Esegui: `python scripts/verify_output.py output.pdf`

Se la verifica fallisce, torna allo Step 2.
````

Step chiari prevengono che Claude salti validazioni critiche. La checklist aiuta sia Claude che te a tracciare il progresso attraverso workflow multi-step.

### Implementa cicli di feedback

**Pattern comune**: Esegui validatore → correggi errori → ripeti

Questo pattern migliora grandemente la qualità dell'output.

**Esempio 1: Conformità style guide** (per Skill senza codice):

```markdown  theme={null}
## Processo revisione contenuti

1. Bozza il tuo contenuto seguendo le linee guida in STYLE_GUIDE.md
2. Revisiona contro la checklist:
   - Controlla coerenza terminologia
   - Verifica che gli esempi seguano il formato standard
   - Conferma che tutte le sezioni richieste siano presenti
3. Se trovati problemi:
   - Nota ogni problema con riferimento sezione specifico
   - Revisiona il contenuto
   - Revisiona la checklist di nuovo
4. Procedi solo quando tutti i requisiti sono soddisfatti
5. Finalizza e salva il documento
```

Questo mostra il pattern loop di validazione usando documenti di riferimento invece di script. Il "validatore" è STYLE\_GUIDE.md, e Claude esegue il controllo leggendo e comparando.

**Esempio 2: Processo modifica documenti** (per Skill con codice):

```markdown  theme={null}
## Processo modifica documenti

1. Fai le tue modifiche a `word/document.xml`
2. **Valida immediatamente**: `python ooxml/scripts/validate.py unpacked_dir/`
3. Se la validazione fallisce:
   - Revisiona il messaggio di errore attentamente
   - Correggi i problemi nell'XML
   - Esegui validazione di nuovo
4. **Procedi solo quando la validazione passa**
5. Ricostruisci: `python ooxml/scripts/pack.py unpacked_dir/ output.docx`
6. Testa il documento di output
```

Il loop di validazione cattura gli errori presto.

## Linee guida contenuto

### Evita informazioni sensibili al tempo

Non includere informazioni che diventeranno obsolete:

**Cattivo esempio: Sensibile al tempo** (diventerà sbagliato):

```markdown  theme={null}
Se stai facendo questo prima di Agosto 2025, usa la vecchia API.
Dopo Agosto 2025, usa la nuova API.
```

**Buon esempio** (usa sezione "vecchi pattern"):

```markdown  theme={null}
## Metodo corrente

Usa l'endpoint API v2: `api.example.com/v2/messages`

## Vecchi pattern

<details>
<summary>Legacy v1 API (deprecata 2025-08)</summary>

La v1 API usava: `api.example.com/v1/messages`

Questo endpoint non è più supportato.
</details>
```

La sezione vecchi pattern fornisce contesto storico senza ingombrare il contenuto principale.

### Usa terminologia coerente

Scegli un termine e usalo attraverso la Skill:

**Buono - Coerente**:

* Sempre "API endpoint"
* Sempre "field"
* Sempre "extract"

**Cattivo - Incoerente**:

* Mescola "API endpoint", "URL", "API route", "path"
* Mescola "field", "box", "element", "control"
* Mescola "extract", "pull", "get", "retrieve"

La coerenza aiuta Claude a capire e seguire le istruzioni.

## Pattern comuni

### Pattern template

Fornisci template per il formato di output. Abbina il livello di rigidità alle tue necessità.

**Per requisiti rigidi** (come risposte API o formati dati):

````markdown  theme={null}
## Struttura report

Usa SEMPRE questa esatta struttura template:

```markdown
# [Titolo Analisi]

## Executive summary
[Panoramica di un paragrafo dei risultati chiave]

## Key findings
- Risultato 1 con dati a supporto
- Risultato 2 con dati a supporto
- Risultato 3 con dati a supporto

## Raccomandazioni
1. Raccomandazione azionabile specifica
2. Raccomandazione azionabile specifica
```
````

**Per guida flessibile** (quando l'adattamento è utile):

````markdown  theme={null}
## Struttura report

Ecco un formato default sensato, ma usa il tuo miglior giudizio basato sull'analisi:

```markdown
# [Titolo Analisi]

## Executive summary
[Panoramica]

## Key findings
[Adatta sezioni basandoti su cosa scopri]

## Raccomandazioni
[Ritaglia al contesto specifico]
```

Aggiusta sezioni come necessario per il tipo specifico di analisi.
````

### Pattern esempi

Per Skill dove la qualità dell'output dipende dal vedere esempi, fornisci coppie input/output proprio come nel prompting regolare:

````markdown  theme={null}
## Formato messaggio commit

Genera messaggi commit seguendo questi esempi:

**Esempio 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication

Add login endpoint and token validation middleware
```

**Esempio 2:**
Input: Fixed bug where dates displayed incorrectly in reports
Output:
```
fix(reports): correct date formatting in timezone conversion

Use UTC timestamps consistently across report generation
```

**Esempio 3:**
Input: Updated dependencies and refactored error handling
Output:
```
chore: update dependencies and refactor error handling

- Upgrade lodash to 4.17.21
- Standardize error response format across endpoints
```

Segui questo stile: tipo(ambito): breve descrizione, poi spiegazione dettagliata.
````

Gli esempi aiutano Claude a capire lo stile desiderato e il livello di dettaglio più chiaramente che le sole descrizioni.

### Pattern workflow condizionale

Guida Claude attraverso punti decisionali:

```markdown  theme={null}
## Workflow modifica documento

1. Determina il tipo di modifica:

   **Creando nuovo contenuto?** → Segui "Workflow creazione" qui sotto
   **Modificando contenuto esistente?** → Segui "Workflow modifica" qui sotto

2. Workflow creazione:
   - Usa libreria docx-js
   - Costruisci documento da zero
   - Esporta in formato .docx

3. Workflow modifica:
   -spacchetta documento esistente
   - Modifica XML direttamente
   - Valida dopo ogni cambiamento
   - Ricostruisci quando completo
```

<Tip>
  Se i workflow diventano grandi o complicati con molti step, considera di spingerli in file separati e dire a Claude di leggere il file appropriato basato sul task a portata di mano.
</Tip>

## Valutazione e iterazione

### Costruisci valutazioni prima

**Crea valutazioni PRIMA di scrivere documentazione estesa.** Questo assicura che la tua Skill risolva problemi reali invece di documentarne di immaginati.

**Sviluppo guidato dalla valutazione (Evaluation-driven development):**

1. **Identifica gap**: Esegui Claude su task rappresentativi senza una Skill. Documenta fallimenti specifici o contesto mancante
2. **Crea valutazioni**: Costruisci tre scenari che testano questi gap
3. **Stabilisci baseline**: Misura la performance di Claude senza la Skill
4. **Scrivi istruzioni minime**: Crea giusto abbastanza contenuto per indirizzare i gap e passare le valutazioni
5. **Itera**: Esegui valutazioni, compara contro baseline, e raffina

Questo approccio assicura che stai risolvendo problemi attuali piuttosto che anticipare requisiti che potrebbero non materializzarsi mai.

**Struttura valutazione**:

```json  theme={null}
{
  "skills": ["pdf-processing"],
  "query": "Estrai tutto il testo da questo file PDF e salvalo in output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Legge con successo il file PDF usando una libreria appropriata di elaborazione PDF o tool riga di comando",
    "Estrae contenuto testuale da tutte le pagine nel documento senza mancare nessuna pagina",
    "Salva il testo estratto in un file chiamato output.txt in un formato chiaro e leggibile"
  ]
}
```

<Note>
  Questo esempio dimostra una valutazione guidata dai dati con una semplice rubrica di test. Non forniamo attualmente un modo integrato per eseguire queste valutazioni. Gli utenti possono creare il loro proprio sistema di valutazione. Le valutazioni sono la tua fonte di verità per misurare l'efficacia della Skill.
</Note>

### Sviluppa Skill iterativamente con Claude

Il processo di sviluppo Skill più efficace coinvolge Claude stesso. Lavora con un'istanza di Claude ("Claude A") per creare una Skill che sarà usata da altre istanze ("Claude B"). Claude A ti aiuta a progettare e raffinare istruzioni, mentre Claude B le testa in task reali. Questo funziona perché i modelli Claude capiscono sia come scrivere istruzioni efficaci per agenti sia di quali informazioni gli agenti hanno bisogno.

**Creare una nuova Skill:**

1. **Completa un task senza una Skill**: Lavora attraverso un problema con Claude A usando prompting normale. Mentre lavori, fornirai naturalmente contesto, spiegherai preferenze e condividerai conoscenza procedurale. Nota quale informazione fornisci ripetutamente.

2. **Identifica il pattern riutilizzabile**: Dopo aver completato il task, identifica quale contesto hai fornito che sarebbe utile per task futuri simili.

   **Esempio**: Se hai lavorato attraverso un'analisi BigQuery, potresti aver fornito nomi tabelle, definizioni campi, regole filtraggio (come "escludi sempre account test"), e pattern query comuni.

3. **Chiedi a Claude A di creare una Skill**: "Crea una Skill che catturi questo pattern di analisi BigQuery che abbiamo appena usato. Includi gli schemi tabella, convenzioni di denominazione, e la regola sul filtrare account test."

   <Tip>
     I modelli Claude capiscono il formato e la struttura Skill nativamente. Non hai bisogno di system prompt speciali o una skill "writing skills" per ottenere che Claude aiuti a creare Skill. Chiedi semplicemente a Claude di creare una Skill ed esso genererà contenuto SKILL.md strutturato propriamente con frontmatter appropriato e contenuto corpo.
   </Tip>

4. **Revisiona per concisione**: Controlla che Claude A non abbia aggiunto spiegazioni non necessarie. Chiedi: "Rimuovi la spiegazione su cosa significa win rate - Claude lo sa già."

5. **Migliora architettura informazione**: Chiedi a Claude A di organizzare il contenuto più efficacemente. Per esempio: "Organizza questo così lo schema tabella è in un file riferimento separato. Potremmo aggiungere più tabelle dopo."

6. **Testa su task simili**: Usa la Skill con Claude B (una istanza fresca con la Skill caricata) su casi d'uso correlati. Osserva se Claude B trova l'informazione giusta, applica regole correttamente, e gestisce il task con successo.

7. **Itera basato su osservazione**: Se Claude B fatica o manca qualcosa, torna a Claude A con specifici: "Quando Claude ha usato questa Skill, ha dimenticato di filtrare per data per Q4. Dovremmo aggiungere una sezione sui pattern filtraggio data?"

**Iterare su Skill esistenti:**

Lo stesso pattern gerarchico continua quando migliori Skill. Alterni tra:

* **Lavorare con Claude A** (l'esperto che aiuta a raffinare la Skill)
* **Testare con Claude B** (l'agente che usa la Skill per eseguire lavoro reale)
* **Osservare il comportamento di Claude B** e portare insight indietro a Claude A

1. **Usa la Skill in workflow reali**: Dai a Claude B (con la Skill caricata) task attuali, non scenari test

2. **Osserva il comportamento di Claude B**: Nota dove fatica, dove ha successo, o dove fa scelte inaspettate

   **Esempio osservazione**: "Quando ho chiesto a Claude B per un report vendite regionali, ha scritto la query ma ha dimenticato di filtrare via account test, anche se la Skill menziona questa regola."

3. **Torna a Claude A per miglioramenti**: Condividi il corrente SKILL.md e descrivi cosa hai osservato. Chiedi: "Ho notato che Claude B ha dimenticato di filtrare account test quando ho chiesto per un report regionale. La Skill menziona il filtraggio, ma forse non è abbastanza prominente?"

4. **Revisiona i suggerimenti di Claude A**: Claude A potrebbe suggerire di riorganizzare per rendere le regole più prominenti, usando linguaggio più forte come "MUST filter" invece di "always filter", o ristrutturando la sezione workflow.

5. **Applica e testa cambiamenti**: Aggiorna la Skill con i raffinamenti di Claude A, poi testa di nuovo con Claude B su richieste simili

6. **Ripeti basato su utilizzo**: Continua questo ciclo osserva-raffina-testa mentre incontri nuovi scenari. Ogni iterazione migliora la Skill basandosi sul comportamento reale dell'agente, non assunzioni.

**Raccogliere feedback dal team:**

1. Condividi Skill con compagni di team e osserva il loro utilizzo
2. Chiedi: La Skill si attiva quando aspettato? Le istruzioni sono chiare? Cosa manca?
3. Incorpora feedback per indirizzare punti ciechi nei tuoi propri pattern di utilizzo

**Perché questo approccio funziona**: Claude A capisce bisogni agente, tu fornisci competenza dominio, Claude B rivela gap attraverso uso reale, e raffinamento iterativo migliora Skill basato su comportamento osservato piuttosto che assunzioni.

### Osserva come Claude naviga le Skill

Mentre iteri sulle Skill, fai attenzione a come Claude le usa effettivamente nella pratica. Guarda per:

* **Percorsi esplorazione inaspettati**: Claude legge file in un ordine che non hai anticipato? Questo potrebbe indicare che la tua struttura non è così intuitiva come pensavi
* **Connessioni mancate**: Claude fallisce nel seguire riferimenti a file importanti? I tuoi link potrebbero necessitare di essere più espliciti o prominenti
* **Eccessiva dipendenza su certe sezioni**: Se Claude legge ripetutamente lo stesso file, considera se quel contenuto dovrebbe essere nel SKILL.md principale invece
* **Contenuto ignorato**: Se Claude non accede mai a un file raggruppato, potrebbe essere non necessario o poveramente segnalato nelle istruzioni principali

Itera basandoti su queste osservazioni piuttosto che assunzioni. Il 'name' e 'description' nei metadati della tua Skill sono particolarmente critici. Claude li usa quando decide se triggerare la Skill in risposta al task corrente. Assicurati che descrivano chiaramente cosa fa la Skill e quando dovrebbe essere usata.

## Anti-pattern da evitare

### Evita percorsi stile Windows

Usa sempre slash in avanti nei percorsi file, anche su Windows:

* ✓ **Buono**: `scripts/helper.py`, `reference/guide.md`
* ✗ **Evita**: `scripts\helper.py`, `reference\guide.md`

I percorsi stile Unix funzionano attraverso tutte le piattaforme, mentre i percorsi stile Windows causano errori su sistemi Unix.

### Evita di offrire troppe opzioni

Non presentare approcci multipli a meno che necessario:

````markdown  theme={null}
**Cattivo esempio: Troppe scelte** (confondente):
"Puoi usare pypdf, o pdfplumber, o PyMuPDF, o pdf2image, o..."

**Buon esempio: Fornisci un default** (con via di fuga):
"Usa pdfplumber per estrazione testo:
```python
import pdfplumber
```

Per PDF scansionati che richiedono OCR, usa pdf2image con pytesseract invece."
````

## Avanzato: Skill con codice eseguibile

Le sezioni sotto si focalizzano su Skill che includono script eseguibili. Se la tua Skill usa solo istruzioni markdown, salta a [Checklist per Skill efficaci](#checklist-for-effective-skills).

### Risolvi, non scaricare (Solve, don't punt)

Quando scrivi script per Skill, gestisci condizioni errore piuttosto che scaricare su Claude.

**Buon esempio: Gestisci errori esplicitamente**:

```python  theme={null}
def process_file(path):
    """Processa un file, creandolo se non esiste."""
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        # Crea file con contenuto default invece di fallire
        print(f"File {path} non trovato, creo default")
        with open(path, 'w') as f:
            f.write('')
        return ''
    except PermissionError:
        # Fornisci alternativa invece di fallire
        print(f"Non posso accedere a {path}, uso default")
        return ''
```

**Cattivo esempio: Scarica su Claude**:

```python  theme={null}
def process_file(path):
    # Fallisci semplicemente e lascia che Claude capisca
    return open(path).read()
```

Anche i parametri di configurazione dovrebbero essere giustificati e documentati per evitare "voodoo constants" (Legge di Ousterhout). Se tu non conosci il valore giusto, come lo determinerà Claude?

**Buon esempio: Auto-documentante**:

```python  theme={null}
# Le richieste HTTP tipicamente completano entro 30 secondi
# Timeout più lungo tiene conto di connessioni lente
REQUEST_TIMEOUT = 30

# Tre tentativi bilanciano affidabilità vs velocità
# Molti fallimenti intermittenti si risolvono al secondo tentativo
MAX_RETRIES = 3
```

**Cattivo esempio: Numeri magici**:

```python  theme={null}
TIMEOUT = 47  # Perché 47?
RETRIES = 5   # Perché 5?
```

### Fornisci script di utilità

Anche se Claude potrebbe scrivere uno script, script pre-fatti offrono vantaggi:

**Benefici degli script di utilità**:

* Più affidabili del codice generato
* Salvano token (nessun bisogno di includere codice nel contesto)
* Salvano tempo (nessuna generazione codice richiesta)
* Assicurano coerenza attraverso gli usi

<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=4bbc45f2c2e0bee9f2f0d5da669bad00" alt="Bundling executable scripts alongside instruction files" data-og-width="2048" width="2048" data-og-height="1154" height="1154" data-path="images/agent-skills-executable-scripts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=9a04e6535a8467bfeea492e517de389f 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=e49333ad90141af17c0d7651cca7216b 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=954265a5df52223d6572b6214168c428 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=2ff7a2d8f2a83ee8af132b29f10150fd 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=48ab96245e04077f4d15e9170e081cfb 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-executable-scripts.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=0301a6c8b3ee879497cc5b5483177c90 2500w" />

Il diagramma sopra mostra come script eseguibili lavorano di fianco ai file istruzione. Il file istruzione (forms.md) referenzia lo script, e Claude può eseguirlo senza caricare i suoi contenuti nel contesto.

**Importante distinzione**: Rendi chiaro nelle tue istruzioni se Claude dovrebbe:

* **Eseguire lo script** (più comune): "Run `analyze_form.py` to extract fields"
* **Leggerlo come riferimento** (per logica complessa): "See `analyze_form.py` for the field extraction algorithm"

Per la maggior parte degli script di utilità, l'esecuzione è preferita perché è più affidabile ed efficiente. Vedi la sezione [Runtime environment](#runtime-environment) sotto per dettagli su come funziona l'esecuzione script.

**Esempio**:

````markdown  theme={null}
## Script di utilità

**analyze_form.py**: Estrae tutti i campi modulo da PDF

```bash
python scripts/analyze_form.py input.pdf > fields.json
```

Formato output:
```json
{
  "field_name": {"type": "text", "x": 100, "y": 200},
  "signature": {"type": "sig", "x": 150, "y": 500}
}
```

**validate_boxes.py**: Controlla per box sovrapposti

```bash
python scripts/validate_boxes.py fields.json
# Returns: "OK" or lists conflicts
```

**fill_form.py**: Applica valori campo al PDF

```bash
python scripts/fill_form.py input.pdf fields.json output.pdf
```
````

### Usa analisi visiva

Quando gli input possono essere renderizzati come immagini, fai analizzare a Claude questi:

````markdown  theme={null}
## Analisi layout modulo

1. Converti PDF in immagini:
   ```bash
   python scripts/pdf_to_images.py form.pdf
   ```

2. Analizza ogni immagine pagina per identificare campi modulo
3. Claude può vedere posizioni campi e tipi visivamente
````

<Note>
  In questo esempio, dovresti aver bisogno di scrivere lo script `pdf_to_images.py`.
</Note>

Le capacità di visione di Claude aiutano a capire layout e strutture.

### Crea output intermedi verificabili

Quando Claude esegue task complessi e aperti, può fare errori. Il pattern "plan-validate-execute" cattura errori presto facendo creare a Claude prima un piano in un formato strutturato, poi validando quel piano con uno script prima di eseguirlo.

**Esempio**: Immagina di chiedere a Claude di aggiornare 50 campi modulo in un PDF basandosi su un foglio di calcolo. Senza validazione, Claude potrebbe referenziare campi non esistenti, creare valori conflittuali, mancare campi richiesti, o applicare aggiornamenti incorrettamente.

**Soluzione**: Usa il pattern workflow mostrato sopra (compilazione modulo PDF), ma aggiungi un file intermedio `changes.json` che viene validato prima di applicare cambiamenti. Il workflow diventa: analizza → **crea file piano** → **valida piano** → esegui → verifica.

**Perché questo pattern funziona:**

* **Cattura errori presto**: La validazione trova problemi prima che i cambiamenti siano applicati
* **Verificabile da macchina**: Gli script forniscono verifica oggettiva
* **Pianificazione reversibile**: Claude può iterare sul piano senza toccare gli originali
* **Debugging chiaro**: I messaggi errore puntano a problemi specifici

**Quando usare**: Operazioni batch, cambiamenti distruttivi, regole di validazione complesse, operazioni ad alta posta.

**Tip implementazione**: Rendi gli script di validazione prolissi con messaggi errore specifici come "Field 'signature\_date' not found. Available fields: customer\_name, order\_total, signature\_date\_signed" per aiutare Claude a correggere problemi.

### Dipendenze pacchetti

Le Skill girano nell'ambiente di esecuzione codice con limitazioni specifiche della piattaforma:

* **claude.ai**: Può installare pacchetti da npm e PyPI e pullare da repository GitHub
* **Anthropic API**: Non ha accesso rete e nessuna installazione pacchetti runtime

Lista i pacchetti richiesti nel tuo SKILL.md e verifica che siano disponibili nella [documentazione tool esecuzione codice](/en/docs/agents-and-tools/tool-use/code-execution-tool).

### Ambiente runtime

Le Skill girano in un ambiente di esecuzione codice con accesso filesystem, comandi bash, e capacità esecuzione codice. Per la spiegazione concettuale di questa architettura, vedi [L'architettura delle Skills](/en/docs/agents-and-tools/agent-skills/overview#the-skills-architecture) nella panoramica.

**Come questo influenza il tuo authoring:**

**Come Claude accede alle Skill:**

1. **Metadati pre-caricati**: All'avvio, il nome e la descrizione dal frontmatter YAML di tutte le Skill sono caricati nel system prompt
2. **File letti on-demand**: Claude usa tool bash Read per accedere a SKILL.md e altri file dal filesystem quando necessario
3. **Script eseguiti efficientemente**: Script di utilità possono essere eseguiti via bash senza caricare i loro interi contenuti nel contesto. Solo l'output dello script consuma token
4. **Nessuna penalità contesto per grandi file**: File di riferimento, dati, o documentazione non consumano token di contesto finché non letti attualmente

* **I percorsi file contano**: Claude naviga la tua directory skill come un filesystem. Usa slash in avanti (`reference/guide.md`), non backslash
* **Nomina file descrittivamente**: Usa nomi che indicano contenuto: `form_validation_rules.md`, non `doc2.md`
* **Organizza per scoperta**: Struttura directory per dominio o feature
  * Buono: `reference/finance.md`, `reference/sales.md`
  * Cattivo: `docs/file1.md`, `docs/file2.md`
* **Raggruppa risorse comprensive**: Includi doc API complete, esempi estesi, grandi dataset; nessuna penalità contesto finché non acceduti
* **Preferisci script per operazioni deterministiche**: Scrivi `validate_form.py` piuttosto che chiedere a Claude di generare codice di validazione
* **Rendi chiaro l'intento di esecuzione**:
  * "Esegui `analyze_form.py` per estrarre campi" (esegui)
  * "Vedi `analyze_form.py` per algoritmo estrazione" (leggi come riferimento)
* **Testa pattern accesso file**: Verifica che Claude possa navigare la tua struttura directory testando con richieste reali

**Esempio:**

```
bigquery-skill/
├── SKILL.md (panoramica, punta a file riferimento)
└── reference/
    ├── finance.md (metriche entrate)
    ├── sales.md (dati pipeline)
    └── product.md (analitiche uso)
```

Quando l'utente chiede sulle entrate, Claude legge SKILL.md, vede il riferimento a `reference/finance.md`, e invoca bash per leggere solo quel file. I file sales.md e product.md rimangono sul filesystem, consumando zero token contesto finché necessari. Questo modello basato su filesystem è ciò che abilita la divulgazione progressiva. Claude può navigare e caricare selettivamente esattamente ciò che ogni task richiede.

Per dettagli completi sull'architettura tecnica, vedi [Come funzionano le Skill](/en/docs/agents-and-tools/agent-skills/overview#how-skills-work) nella panoramica Skill.

### Riferimenti tool MCP

Se la tua Skill usa tool MCP (Model Context Protocol), usa sempre nomi tool completamente qualificati per evitare errori "tool not found".

**Formato**: `ServerName:tool_name`

**Esempio**:

```markdown  theme={null}
Usa il tool BigQuery:bigquery_schema per recuperare schemi tabella.
Usa il tool GitHub:create_issue per creare issue.
```

Dove:

* `BigQuery` e `GitHub` sono nomi server MCP
* `bigquery_schema` e `create_issue` sono i nomi tool all'interno di quei server

Senza il prefisso server, Claude potrebbe fallire nel localizzare il tool, specialmente quando server MCP multipli sono disponibili.

### Evita di assumere che i tool siano installati

Non assumere che i pacchetti siano disponibili:

````markdown  theme={null}
**Cattivo esempio: Assume installazione**:
"Usa la libreria pdf per processare il file."

**Buon esempio: Esplicito sulle dipendenze**:
"Installa pacchetto richiesto: `pip install pypdf`

Poi usalo:
```python
from pypdf import PdfReader
reader = PdfReader("file.pdf")
```"
````

## Note tecniche

### Requisiti frontmatter YAML

Il frontmatter SKILL.md include solo campi `name` (64 caratteri max) e `description` (1024 caratteri max). Vedi la [Panoramica Skill](/en/docs/agents-and-tools/agent-skills/overview#skill-structure) per dettagli struttura completi.

### Budget Token

Tieni il corpo SKILL.md sotto le 500 righe per prestazioni ottimali. Se il tuo contenuto eccede questo, dividilo in file separati usando i pattern di divulgazione progressiva descritti prima. Per dettagli architetturali, vedi la [Panoramica Skill](/en/docs/agents-and-tools/agent-skills/overview#how-skills-work).

## Checklist per Skill efficaci

Prima di condividere una Skill, verifica:

### Qualità Core

* [ ] Descrizione è specifica e include termini chiave
* [ ] Descrizione include sia cosa fa la Skill sia quando usarla
* [ ] Corpo SKILL.md è sotto 500 righe
* [ ] Dettagli aggiuntivi sono in file separati (se necessario)
* [ ] Nessuna informazione sensibile al tempo (o in sezione "vecchi pattern")
* [ ] Terminologia coerente ovunque
* [ ] Esempi sono concreti, non astratti
* [ ] Riferimenti file sono profondi un livello
* [ ] Divulgazione progressiva usata appropriatamente
* [ ] Workflow hanno step chiari

### Codice e script

* [ ] Script risolvono problemi piuttosto che scaricare su Claude
* [ ] Gestione errori è esplicita e utile
* [ ] Nessuna "voodoo constants" (tutti i valori giustificati)
* [ ] Pacchetti richiesti listati nelle istruzioni e verificati come disponibili
* [ ] Script hanno documentazione chiara
* [ ] Nessun percorso stile Windows (tutti slash in avanti)
* [ ] Step validazione/verifica per operazioni critiche
* [ ] Feedback loops inclusi per task qualità-critica

### Testing

* [ ] Almeno tre valutazioni create
* [ ] Testato con Haiku, Sonnet, e Opus
* [ ] Testato con scenari di utilizzo reali
* [ ] Feedback team incorporato (se applicabile)

## Prossimi passi

<CardGroup cols={2}>
  <Card title="Inizia con Agent Skills" icon="rocket" href="/en/docs/agents-and-tools/agent-skills/quickstart">
    Crea la tua prima Skill
  </Card>

  <Card title="Usa Skills in Claude Code" icon="terminal" href="/en/docs/claude-code/skills">
    Crea e gestisci Skills in Claude Code
  </Card>

  <Card title="Usa Skills con l'API" icon="code" href="/en/api/skills-guide">
    Carica e usa Skills programmaticamente
  </Card>
</CardGroup>
