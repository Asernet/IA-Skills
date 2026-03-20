# Guida all'Installazione

## Prerequisiti

- **Python 3.8+** con pip
- **Git** per clonare il repository
- **Ambiente Gemini AI** (es. l'agente locale di Gemini) configurato e funzionante

Opzionale:
- **Playwright** per le funzionalità di cattura screenshot visiva

## Installazione Rapida

*(Attualmente in fase di sviluppo. Si consiglia l'installazione manuale)*

### Unix/macOS/Linux

```bash
# curl -fsSL https://raw.githubusercontent.com/CinaWeb/Skills/main/seo-special/install.sh | bash
```

### Windows (PowerShell)

```powershell
# irm https://raw.githubusercontent.com/CinaWeb/Skills/main/seo-special/install.ps1 | iex
```

## Installazione Manuale

Questi passaggi servono a configurare la skill `seo-special` all'interno dell'ecosistema Gemini.

1. **Clonazione della directory delle skill**
   Consigliabile navigare nella directory destinata alle skill (es. `~/.gemini/skills/`).

```bash
# Entra nella cartella delle skill di Gemini
cd ~/.gemini/skills

# Clona la repository (se non l'hai già fatto)
git clone https://github.com/CinaWeb/Skills.git

# O in alternativa, scarica e sposta solo la cartella seo-special all'interno di ~/.gemini/skills/
```

2. **Installazione delle dipendenze Python**

A differenza di Claude Code, in Gemini l'ambiente Python è gestito a livello globale o di ambiente utente corrente. Installa i requisiti definiti nella cartella `seo-special`.

```bash
# Naviga all'interno della skill
cd ~/.gemini/skills/seo-special

# Opzione A: Usare un ambiente virtuale (raccomandato)
python -m venv .venv

# Su Windows
.\.venv\Scripts\activate
# Su Unix/macOS
source .venv/bin/activate

# Installa i moduli
pip install -r requirements.txt

# Opzione B: Installazione a livello utente (Globale)
pip install --user -r requirements.txt
```

3. **Installazione dei browser per Playwright** (opzionale, per analisi visiva)

```bash
pip install playwright
playwright install chromium
```

Playwright è del tutto opzionale — senza la sua installazione, le analisi visive e procedurali ripiegheranno in automatico su `WebFetch` (BeautifulSoup/requests).

## Percorsi di Installazione

Per funzionare, Gemini si aspetta di trovare i componenti della skill nei seguenti percorsi:

| Componente | Percorso |
|-----------|------|
| Skill Multi-Agente | `~/.gemini/skills/seo-special/` |
| Punto d'ingresso | `~/.gemini/skills/seo-special/SKILL.md` |
| Task/Competenze | `~/.gemini/skills/seo-special/tasks/task-*.md` |
| Sottoagenti | `~/.gemini/skills/seo-special/subagents/seo-*.md` |

## Verifica dell'Installazione

1. Avvia il tuo assistente Gemini.
2. Controlla che le skill siano caricate (solitamente digitando `@seo-special` o pronunciando le frasi di attivazione del trigger, es. `seo audit`, `audit profondo`).

Dovresti vederlo avviare il caricamento della documentazione o visualizzare il prompt in attesa della fornitura di un URL da scansionare.

## Disinstallazione

Per disinstallare o rimuovere la skill, basterà eliminare la directory associata.

```bash
# Windows (PowerShell)
Remove-Item -Recurse -Force ~/.gemini/skills/seo-special

# Unix/macOS
rm -rf ~/.gemini/skills/seo-special
```

## Risoluzione dei Problemi

### Errore "Skill non trovata"

Assicurati che la skill sia installata nella posizione di riconoscimento di Gemini.

```bash
# Verifica la presenza del root della skill
ls ~/.gemini/skills/seo-special/SKILL.md
```

Se il file non esiste, dovrai riposizionare i file clonati o estrarli nel percorso corretto.

### Errori di dipendenza Python

Se l'installazione dei `requirements.txt` fallisce, installa le dipendenze manualmente:

```bash
pip install beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

### Errori relativi agli screenshot con Playwright

Se il fallback visuale via browser headless si interrompe, installa Chromium forzatamente:

```bash
playwright install chromium
```

### Problemi di Permessi (Unix/Linux)

Assicurati che gli script Python e Bash possiedano i permessi di esecuzione:

```bash
chmod +x ~/.gemini/skills/seo-special/scripts/*.py
chmod +x ~/.gemini/skills/seo-special/hooks/*.py
chmod +x ~/.gemini/skills/seo-special/hooks/*.sh
```
