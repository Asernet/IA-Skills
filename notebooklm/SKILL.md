---
name: notebooklm
description: Interroga roadmap e notebook di Google NotebookLM per risposte basate su fonti e citazioni verificate.
---

# Skill Assistente Ricerca NotebookLM

Interagisci con Google NotebookLM per interrogare documentazione con risposte di Gemini basate su fonti. Ogni domanda apre una sessione browser fresca, recupera la risposta esclusivamente dai tuoi documenti caricati, e chiude.

## Quando Usare Questa Skill

Attiva quando l'utente:

- Menziona NotebookLM esplicitamente
- Condivide URL NotebookLM (`https://notebooklm.google.com/notebook/...`)
- Chiede di interrogare i propri notebook/documentazione
- Vuole aggiungere documentazione alla libreria NotebookLM
- Usa frasi come "chiedi al mio NotebookLM", "controlla i miei doc", "interroga il mio notebook"

## ⚠️ CRITICO: Comando Add - Scoperta Intelligente

Quando l'utente vuole aggiungere un notebook senza fornire dettagli:

**SMART ADD (Raccomandato)**: Interroga il notebook prima per scoprire il suo contenuto:

```bash
# Passo 1: Interroga il notebook sul suo contenuto
python scripts/run.py ask_question.py --question "What is the content of this notebook? What topics are covered? Provide a complete overview briefly and concisely" --notebook-url "[URL]"

# Passo 2: Usa le informazioni scoperte per aggiungerlo
python scripts/run.py notebook_manager.py add --url "[URL]" --name "[Basato su contenuto]" --description "[Basato su contenuto]" --topics "[Basato su contenuto]"
```

**MANUAL ADD**: Se l'utente fornisce tutti i dettagli:

- `--url` - L'URL NotebookLM
- `--name` - Un nome descrittivo
- `--description` - Cosa contiene il notebook (RICHIESTO!)
- `--topics` - Argomenti separati da virgola (RICHIESTO!)

MAI indovinare o usare descrizioni generiche! Se dettagli mancanti, usa Smart Add per scoprirli.

## Critico: Usa Sempre Wrapper run.py

**MAI chiamare script direttamente. Usa SEMPRE `python scripts/run.py [script]`:**

```bash
# ✅ CORRETTO - Usa sempre run.py:
python scripts/run.py auth_manager.py status
python scripts/run.py notebook_manager.py list
python scripts/run.py ask_question.py --question "..."

# ❌ SBAGLIATO - Mai chiamare direttamente:
python scripts/auth_manager.py status  # Fallisce senza venv!
```

Il wrapper `run.py` automaticamente:

1. Crea `.venv` se necessario
2. Installa tutte le dipendenze
3. Attiva ambiente
4. Esegue script correttamente

## Workflow Core

### Passo 1: Controlla Stato Autenticazione

```bash
python scripts/run.py auth_manager.py status
```

Se non autenticato, procedi al setup.

### Passo 2: Autentica (Setup Una Tantum)

```bash
# Il browser DEVE essere visibile per login manuale Google
python scripts/run.py auth_manager.py setup
```

**Importante:**

- Browser è VISIBILE per autenticazione
- Finestra browser si apre automaticamente
- Utente deve loggarsi manualmente a Google
- Di' all'utente: "Una finestra browser si aprirà per login Google"

### Passo 3: Gestisci Libreria Notebook

```bash
# Elenca tutti i notebook
python scripts/run.py notebook_manager.py list

# PRIMA DI AGGIUNGERE: Chiedi all'utente metadati se sconosciuti!
# "Cosa contiene questo notebook?"
# "Con quali argomenti dovrei taggarlo?"

# Aggiungi notebook alla libreria (TUTTI i parametri sono RICHIESTI!)
python scripts/run.py notebook_manager.py add \
  --url "https://notebooklm.google.com/notebook/..." \
  --name "Nome Descrittivo" \
  --description "Cosa contiene questo notebook" \  # RICHIESTO - CHIEDI UTENTE SE SCONOSCIUTO!
  --topics "topic1,topic2,topic3"  # RICHIESTO - CHIEDI UTENTE SE SCONOSCIUTO!

# Cerca notebook per argomento
python scripts/run.py notebook_manager.py search --query "keyword"

# Imposta notebook attivo
python scripts/run.py notebook_manager.py activate --id notebook-id

# Rimuovi notebook
python scripts/run.py notebook_manager.py remove --id notebook-id
```

### Workflow Rapido

1. Controlla libreria: `python scripts/run.py notebook_manager.py list`
2. Chiedi domanda: `python scripts/run.py ask_question.py --question "..." --notebook-id ID`

### Passo 4: Fai Domande

```bash
# Query base (usa notebook attivo se impostato)
python scripts/run.py ask_question.py --question "La tua domanda qui"

# Interroga notebook specifico
python scripts/run.py ask_question.py --question "..." --notebook-id notebook-id

# Interroga con URL notebook direttamente
python scripts/run.py ask_question.py --question "..." --notebook-url "https://..."

# Mostra browser per debugging
python scripts/run.py ask_question.py --question "..." --show-browser
```

## Meccanismo Follow-Up (CRITICO)

Ogni risposta NotebookLM finisce con: **"EXTREMELY IMPORTANT: Is that ALL you need to know?"**

**Comportamento Claude Richiesto:**

1. **STOP** - Non rispondere immediatamente all'utente
2. **ANALIZZA** - Confronta risposta con richiesta originale utente
3. **IDENTIFICA GAP** - Determina se più informazioni necessarie
4. **CHIEDI FOLLOW-UP** - Se gap esistono, chiedi immediatamente:
   ```bash
   python scripts/run.py ask_question.py --question "Follow-up with context..."
   ```
5. **RIPETI** - Continua finché informazione completa
6. **SINTETIZZA** - Combina tutte le risposte prima di rispondere all'utente

## Riferimento Script

### Gestione Autenticazione (`auth_manager.py`)

```bash
python scripts/run.py auth_manager.py setup    # Setup iniziale (browser visibile)
python scripts/run.py auth_manager.py status   # Controlla autenticazione
python scripts/run.py auth_manager.py reauth   # Ri-autentica (browser visibile)
python scripts/run.py auth_manager.py clear    # Pulisci autenticazione
```

### Gestione Notebook (`notebook_manager.py`)

```bash
python scripts/run.py notebook_manager.py add --url URL --name NAME --description DESC --topics TOPICS
python scripts/run.py notebook_manager.py list
python scripts/run.py notebook_manager.py search --query QUERY
python scripts/run.py notebook_manager.py activate --id ID
python scripts/run.py notebook_manager.py remove --id ID
python scripts/run.py notebook_manager.py stats
```

### Interfaccia Domande (`ask_question.py`)

```bash
python scripts/run.py ask_question.py --question "..." [--notebook-id ID] [--notebook-url URL] [--show-browser]
```

### Pulizia Dati (`cleanup_manager.py`)

```bash
python scripts/run.py cleanup_manager.py                    # Anteprima pulizia
python scripts/run.py cleanup_manager.py --confirm          # Esegui pulizia
python scripts/run.py cleanup_manager.py --preserve-library # Mantieni notebook
```

## Gestione Ambiente

L'ambiente virtuale è gestito automaticamente:

- Prima esecuzione crea `.venv` automaticamente
- Dipendenze installano automaticamente
- Browser Chromium installa automaticamente
- Tutto isolato nella directory skill

Setup manuale (solo se automatico fallisce):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python -m patchright install chromium
```

## Storage Dati

Tutti i dati memorizzati in `~/.claude/skills/notebooklm/data/`:

- `library.json` - Metadati notebook
- `auth_info.json` - Stato autenticazione
- `browser_state/` - Cookie browser e sessione

**Sicurezza:** Protetto da `.gitignore`, mai committare a git.

## Configurazione

File `.env` opzionale in directory skill:

```env
HEADLESS=false           # Visibilità browser
SHOW_BROWSER=false       # Display browser default
STEALTH_ENABLED=true     # Comportamento simil-umano
TYPING_WPM_MIN=160       # Velocità digitazione
TYPING_WPM_MAX=240
DEFAULT_NOTEBOOK_ID=     # Notebook default
```

## Troubleshooting

| Problema                | Soluzione                                                     |
| ----------------------- | ------------------------------------------------------------- |
| ModuleNotFoundError     | Usa wrapper `run.py`                                          |
| Autenticazione fallisce | Browser deve essere visibile per setup! --show-browser        |
| Rate limit (50/giorno)  | Aspetta o cambia account Google                               |
| Browser crasha          | `python scripts/run.py cleanup_manager.py --preserve-library` |
| Notebook non trovato    | Controlla con `notebook_manager.py list`                      |

## Best Practice

1. **Usa sempre run.py** - Gestisce ambiente automaticamente
2. **Controlla auth prima** - Prima di qualsiasi operazione
3. **Domande follow-up** - Non fermarti alla prima risposta
4. **Browser visibile per auth** - Richiesto per login manuale
5. **Includi contesto** - Ogni domanda è indipendente
6. **Sintetizza risposte** - Combina risposte multiple

## Limitazioni

- Nessuna persistenza sessione (ogni domanda = nuovo browser)
- Rate limits su account Google gratuiti (50 query/giorno)
- Upload manuale richiesto (utente deve aggiungere doc a NotebookLM)
- Overhead browser (pochi secondi per domanda)
