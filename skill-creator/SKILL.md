---
name: skill-creator
description: Guida alla creazione di nuove skill efficaci o aggiornamento di quelle esistenti per estendere le capacità.
---

# Skill Creator

Questa skill fornisce guida per creare skill efficaci.

## Riguardo le Skill

Le skill sono pacchetti modulari e auto-contenuti che estendono le capacità di Claude fornendo conoscenze specializzate, workflow e tool. Pensale come "guide di onboarding" per domini o task specifici—trasformano Claude da un agente general-purpose in un agente specializzato equipaggiato con conoscenza procedurale che nessun modello può possedere pienamente.

### Cosa Forniscono le Skill

1. Workflow specializzati - Procedure multi-step per domini specifici
2. Integrazioni tool - Istruzioni per lavorare con formati file o API specifici
3. Expertise di dominio - Conoscenza specifica aziendale, schemi, logica di business
4. Risorse pacchettizzate - Script, riferimenti e asset per task complessi e ripetitivi

## Principi Core

### La Concisione è Chiave

La finestra di contesto è un bene pubblico. Le skill condividono la finestra di contesto con tutto il resto di cui Claude ha bisogno: prompt di sistema, cronologia conversazione, metadati altre skill, e la richiesta utente effettiva.

**Assunzione di default: Claude è già molto intelligente.** Aggiungi solo contesto che Claude non ha già. Sfida ogni pezzo di informazione: "Claude ha davvero bisogno di questa spiegazione?" e "Questo paragrafo giustifica il suo costo in token?"

Preferisci esempi concisi a spiegazioni verpose.

### Imposta Gradi di Libertà Appropriati

Combacia il livello di specificità alla fragilità e variabilità del task:

**Alta libertà (istruzioni testuali)**: Usa quando approcci multipli sono validi, le decisioni dipendono dal contesto, o le euristiche guidano l'approccio.

**Libertà media (pseudocodice o script con parametri)**: Usa quando un pattern preferito esiste, qualche variazione è accettabile, o la configurazione influenza il comportamento.

**Bassa libertà (script specifici, pochi parametri)**: Usa quando le operazioni sono fragili e inclini all'errore, la consistenza è critica, o una sequenza specifica deve essere seguita.

Pensa a Claude come se stesse esplorando un percorso: un ponte stretto con scogliere necessita guardrail specifici (bassa libertà), mentre un campo aperto permette molte rotte (alta libertà).

### Anatomia di una Skill

Ogni skill consiste in un file SKILL.md richiesto e risorse pacchettizzate opzionali:

```
skill-name/
├── SKILL.md (richiesto)
│   ├── YAML frontmatter metadata (richiesto)
│   │   ├── name: (richiesto)
│   │   └── description: (richiesto)
│   └── Istruzioni Markdown (richiesto)
└── Risorse Pacchettizzate (opzionale)
    ├── scripts/          - Codice eseguibile (Python/Bash/etc.)
    ├── references/       - Documentazione intesa per essere caricata nel contesto come necessario
    └── assets/           - File usati nell'output (template, icone, font, ecc.)
```

#### SKILL.md (richiesto)

Ogni SKILL.md consiste in:

- **Frontmatter** (YAML): Contiene campi `name` e `description`. Questi sono gli unici campi che Claude legge per determinare quando la skill viene usata, quindi è molto importante essere chiari e comprensivi nel descrivere cosa è la skill, e quando dovrebbe essere usata.
- **Corpo** (Markdown): Istruzioni e guida per usare la skill. Caricato solo DOPO che la skill si attiva (se accade).

#### Risorse Pacchettizzate (opzionale)

##### Script (`scripts/`)

Codice eseguibile (Python/Bash/etc.) per task che richiedono affidabilità deterministica o sono riscritti ripetutamente.

- **Quando includere**: Quando lo stesso codice viene riscritto ripetutamente o affidabilità deterministica è necessaria
- **Esempio**: `scripts/rotate_pdf.py` per task rotazione PDF
- **Benefici**: Efficiente in token, deterministico, può essere eseguito senza caricare nel contesto
- **Nota**: Gli script potrebbero comunque dover essere letti da Claude per patching o aggiustamenti specifici per ambiente

##### Riferimenti (`references/`)

Documentazione e materiale di riferimento intesi per essere caricati come necessario nel contesto per informare il processo e pensiero di Claude.

- **Quando includere**: Per documentazione che Claude dovrebbe referenziare mentre lavora
- **Esempi**: `references/finance.md` per schemi finanziari, `references/mnda.md` per template NDA aziendale, `references/policies.md` per policy aziendali, `references/api_docs.md` per specifiche API
- **Casi d'uso**: Schemi database, documentazione API, conoscenza dominio, policy aziendali, guide workflow dettagliate
- **Benefici**: Mantiene SKILL.md snello, caricato solo quando Claude determina che è necessario
- **Best practice**: Se i file sono grandi (>10k parole), includi pattern di ricerca grep in SKILL.md
- **Evita duplicazione**: Le informazioni dovrebbero vivere o in SKILL.md o nei file riferimento, non entrambi. Preferisci file riferimento per informazioni dettagliate a meno che non sia veramente core per la skill—questo mantiene SKILL.md snello rendendo le informazioni scopribili senza ingolfare la finestra contesto. Tieni solo istruzioni procedurali essenziali e guida workflow in SKILL.md; sposta materiale riferimento dettagliato, schemi ed esempi nei file riferimento.

##### Asset (`assets/`)

File non intesi per essere caricati nel contesto, ma piuttosto usati all'interno dell'output che Claude produce.

- **Quando includere**: Quando la skill necessita file che saranno usati nell'output finale
- **Esempi**: `assets/logo.png` per asset brand, `assets/slides.pptx` per template PowerPoint, `assets/frontend-template/` per boilerplate HTML/React, `assets/font.ttf` per tipografia
- **Casi d'uso**: Template, immagini, icone, codice boilerplate, font, documenti campione che vengono copiati o modificati
- **Benefici**: Separa risorse output dalla documentazione, abilita Claude a usare file senza caricarli nel contesto

#### Cosa Non Includere in una Skill

Una skill dovrebbe contenere solo file essenziali che supportano direttamente la sua funzionalità. NON creare documentazione estranea o file ausiliari, inclusi:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- ecc.

La skill dovrebbe contenere solo le informazioni necessarie per un agente AI per fare il lavoro a portata di mano. Non dovrebbe contenere contesto ausiliario sul processo che ha portato a crearla, procedure di setup e testing, documentazione rivolta all'utente, ecc. Creare file di documentazione addizionali aggiunge solo disordine e confusione.

### Principio di Design Divulgazione Progressiva

Le skill usano un sistema di caricamento a tre livelli per gestire il contesto efficientemente:

1. **Metadati (name + description)** - Sempre nel contesto (~100 parole)
2. **Corpo SKILL.md** - Quando la skill si attiva (<5k parole)
3. **Risorse pacchettizzate** - Come necessario da Claude (Illimitato perché gli script possono essere eseguiti senza leggere nella finestra contesto)

#### Pattern Divulgazione Progressiva

Mantieni il corpo di SKILL.md all'essenziale e sotto 500 righe per minimizzare rigonfiamento contesto. Dividi il contenuto in file separati quando ci si avvicina a questo limite. Quando separi contenuto in altri file, è molto importante referenziarli da SKILL.md e descrivere chiaramente quando leggerli, per assicurare che il lettore della skill sappia che esistono e quando usarli.

**Principio chiave:** Quando una skill supporta variazioni, framework o opzioni multiple, mantieni solo il workflow core e la guida alla selezione in SKILL.md. Sposta dettagli specifici per variante (pattern, esempi, configurazione) in file di riferimento separati.

**Pattern 1: Guida alto livello con riferimenti**

```markdown
# PDF Processing

## Avvio rapido

Estrai testo con pdfplumber:
[esempio codice]

## Funzionalità avanzate

- **Compilazione moduli**: Vedi [FORMS.md](FORMS.md) per guida completa
- **Riferimento API**: Vedi [REFERENCE.md](REFERENCE.md) per tutti i metodi
- **Esempi**: Vedi [EXAMPLES.md](EXAMPLES.md) per pattern comuni
```

Claude carica FORMS.md, REFERENCE.md, o EXAMPLES.md solo quando necessario.

**Pattern 2: Organizzazione specifica per dominio**

Per Skill con domini multipli, organizza il contenuto per dominio per evitare caricamento contesto irrilevante:

```
bigquery-skill/
├── SKILL.md (panoramica e navigazione)
└── reference/
    ├── finance.md (entrate, metriche fatturazione)
    ├── sales.md (opportunità, pipeline)
    ├── product.md (uso API, feature)
    └── marketing.md (campagne, attribuzione)
```

Quando un utente chiede metriche vendita, Claude legge solo sales.md.

Similmente, per skill che supportano framework o varianti multipli, organizza per variante:

```
cloud-deploy/
├── SKILL.md (workflow + selezione provider)
└── references/
    ├── aws.md (pattern deployment AWS)
    ├── gcp.md (pattern deployment GCP)
    └── azure.md (pattern deployment Azure)
```

Quando l'utente sceglie AWS, Claude legge solo aws.md.

**Pattern 3: Dettagli condizionali**

Mostra contenuto base, linka a contenuto avanzato:

```markdown
# DOCX Processing

## Creare documenti

Usa docx-js per nuovi documenti. Vedi [DOCX-JS.md](DOCX-JS.md).

## Editare documenti

Per edit semplici, modifica XML direttamente.

**Per revisioni (tracked changes)**: Vedi [REDLINING.md](REDLINING.md)
**Per dettagli OOXML**: Vedi [OOXML.md](OOXML.md)
```

Claude legge REDLINING.md o OOXML.md solo quando l'utente necessita quelle funzionalità.

**Linee guida importanti:**

- **Evita riferimenti profondamente annidati** - Mantieni riferimenti profondi un livello da SKILL.md. Tutti i file riferimento dovrebbero linkare direttamente da SKILL.md.
- **Struttura file riferimento più lunghi** - Per file più lunghi di 100 righe, includi un indice in cima così Claude può vedere l'intero scopo quando visualizza anteprima.

## Processo Creazione Skill

La creazione skill coinvolge questi passi:

1. Comprendi la skill con esempi concreti
2. Pianifica contenuti skill riutilizzabili (script, riferimenti, asset)
3. Inizializza la skill (esegui init_skill.py)
4. Edita la skill (implementa risorse e scrivi SKILL.md)
5. Impacchetta la skill (esegui package_skill.py)
6. Itera basato su uso reale

Segui questi passi in ordine, saltando solo se c'è una chiara ragione per cui non sono applicabili.

### Passo 1: Comprendere la Skill con Esempi Concreti

Salta questo passo solo quando i pattern d'uso della skill sono già chiaramente compresi. Rimane prezioso anche quando si lavora con una skill esistente.

Per creare una skill efficace, comprendi chiaramente esempi concreti di come la skill sarà usata. Questa comprensione può venire sia da esempi utente diretti o esempi generati validati con feedback utente.

Concludi questo passo quando c'è un senso chiaro della funzionalità che la skill dovrebbe supportare.

### Passo 2: Pianificare i Contenuti Skill Riutilizzabili

Per trasformare esempi concreti in una skill efficace, analizza ogni esempio:

1. Considerando come eseguire sull'esempio da zero
2. Identificando quali script, riferimenti e asset sarebbero utili quando si eseguono questi workflow ripetutamente

Per stabilire i contenuti della skill, analizza ogni esempio concreto per creare una lista delle risorse riutilizzabili da includere: script, riferimenti e asset.

### Passo 3: Inizializzare la Skill

A questo punto, è tempo di creare effettivamente la skill.

Salta questo passo solo se la skill che stai sviluppando esiste già, e iterazione o impacchettamento è necessario. In questo caso, continua al prossimo passo.

Quando crei una nuova skill da zero, esegui sempre lo script `init_skill.py`. Lo script genera convenientemente una nuova directory skill template che include automaticamente tutto ciò che una skill richiede.

Uso:

```bash
scripts/init_skill.py <skill-name> --path <output-directory>
```

Lo script:

- Crea la directory skill al percorso specificato
- Genera un template SKILL.md con frontmatter corretto e placeholder TODO
- Crea directory esempio risorse: `scripts/`, `references/`, e `assets/`
- Aggiunge file esempio in ogni directory che possono essere personalizzati o cancellati

Dopo inizializzazione, personalizza o rimuovi SKILL.md generato e file esempio come necessario.

### Passo 4: Editare la Skill

Quando editi la skill (nuovamente generata o esistente), ricorda che la skill sta venendo creata per un'altra istanza di Claude da usare. Includi informazioni che sarebbero benefiche e non ovvie a Claude. Considera quale conoscenza procedurale, dettagli dominio-specifici, o asset riutilizzabili aiuterebbero un'altra istanza Claude a eseguire questi task più efficacemente.

#### Impara Pattern Design Provati

Consulta queste guide utili basate sui bisogni della tua skill:

- **Processi multi-step**: Vedi references/workflows.md per workflow sequenziali e logica condizionale
- **Formati output specifici o standard qualità**: Vedi references/output-patterns.md per template e pattern esempio

Questi file contengono best practice stabilite per design skill efficace.

#### Inizia con Contenuti Skill Riutilizzabili

Per iniziare implementazione, inizia con le risorse riutilizzabili identificate sopra: file `scripts/`, `references/`, e `assets/`. Nota che questo passo potrebbe richiedere input utente.

Script aggiunti devono essere testati eseguendoli effettivamente per assicurare che non ci siano bug e che l'output corrisponda a quanto atteso.

Qualsiasi file esempio e directory non necessario per la skill dovrebbe essere cancellato.

#### Aggiorna SKILL.md

**Linee guida Scrittura:** Usa sempre forma imperativa/infinito.

##### Frontmatter

Scrivi il frontmatter YAML con `name` e `description`:

- `name`: Il nome della skill
- `description`: Questo è il meccanismo di attivazione primario per la tua skill, e aiuta Claude a capire quando usare la skill.
  - Includi sia cosa fa la Skill e trigger/contesti specifici per quando usarla.
  - Includi tutte le informazioni "quando usare" qui - Non nel corpo. Il corpo è caricato solo dopo l'attivazione, quindi sezioni "Quando Usare Questa Skill" nel corpo non sono utili a Claude.

Non includere altri campi nel frontmatter YAML.

##### Corpo

Scrivi istruzioni per usare la skill e le sue risorse pacchettizzate.

### Passo 5: Impacchettare una Skill

Una volta che lo sviluppo della skill è completo, deve essere impacchettata in un file .skill distribuibile che viene condiviso con l'utente. Il processo di impacchettamento valida automaticamente la skill prima per assicurare che soddisfi tutti i requisiti:

```bash
scripts/package_skill.py <path/to/skill-folder>
```

Specifica opzionale directory output:

```bash
scripts/package_skill.py <path/to/skill-folder> ./dist
```

Lo script di impacchettamento:

1. **Validerà** la skill automaticamente, controllando:
   - Formato frontmatter YAML e campi richiesti
   - Convenzioni naming skill e struttura directory
   - Completezza e qualità descrizione
   - Organizzazione file e riferimenti risorse

2. **Impacchetterà** la skill se la validazione passa, creando un file .skill nominato dopo la skill (es., `my-skill.skill`) che include tutti i file e mantiene la struttura directory corretta per distribuzione.

Se la validazione fallisce, lo script riporterà gli errori e uscirà senza creare un pacchetto. Fixa ogni errore validazione ed esegui il comando di impacchettamento di nuovo.

### Passo 6: Iterare

Dopo aver testato la skill, gli utenti potrebbero richiedere miglioramenti.

**Workflow Iterazione:**

1. Usa la skill su task reali
2. Nota difficoltà o inefficiente
3. Identifica come SKILL.md o risorse pacchettizzate dovrebbero essere aggiornate
4. Implementa cambiamenti e testa di nuovo
