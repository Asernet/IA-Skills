# Risoluzione dei Problemi

## Problemi Comuni

### La Skill non viene caricata

**Sintomo:** Il trigger `/seo` o i comandi testuali non vengono riconosciuti dall'agente.

**Soluzioni:**

1. Verifica l'installazione:
```bash
ls ~/.gemini/skills/seo-special/SKILL.md
```

2. Verifica che `SKILL.md` abbia un frontmatter corretto:
```bash
head -5 ~/.gemini/skills/seo-special/SKILL.md
```
Dovrebbe iniziare con `---` seguito dalla configurazione YAML.

3. Riavvia la console o l'assistente Gemini:
```bash
# Dipende dall'implementazione (es. chiudi e riapri il terminale/chat)
```

4. Riesegui l'installer o clona nuovamente:
```bash
# vedi INSTALLATION.md per i dettagli
```

---

### Errori di Dipendenza Python

**Sintomo:** `ModuleNotFoundError: No module named 'requests'`

**Soluzione:**

A partire dalle ultime versioni, le dipendenze risiedono nella cartella della skill. Prova:

```bash
# Utilizzando l'ambiente virtuale se creato (consigliato)
~/.gemini/skills/seo-special/.venv/bin/pip install -r ~/.gemini/skills/seo-special/requirements.txt
```

Se il `venv` non esiste, installalo nel contesto utente (`--user`):
```bash
pip install --user -r ~/.gemini/skills/seo-special/requirements.txt
```

O installale singolarmente:
```bash
pip install --user beautifulsoup4 requests lxml playwright Pillow urllib3 validators
```

### File requirements.txt Non Trovato

**Sintomo:** `No such file: requirements.txt` dopo l'installazione

**Soluzione:** Verifica che il file esista nella directory della skill:

```bash
ls ~/.gemini/skills/seo-special/requirements.txt
```

Se mancante, riscaricalo:
```bash
curl -fsSL https://raw.githubusercontent.com/CinaWeb/Skills/main/seo-special/requirements.txt \
  -o ~/.gemini/skills/seo-special/requirements.txt
```

### Problemi di Rilevamento Python su Windows

**Sintomo:** `python non è riconosciuto come comando interno o esterno` o `pip punta a uno Python sbagliato`

**Soluzione:** 

1. Installa Python da [python.org](https://python.org) e assicurati di spuntare la casella "Add Python to PATH"
2. In alternativa, usa il launcher per Windows: `py -3 -m pip install -r requirements.txt`
3. Usa il prefisso esplicito `python -m pip` invece di `pip` da solo

---

### Errori con gli Screenshot di Playwright

**Sintomo:** `playwright._impl._errors.Error: Executable doesn't exist`

**Soluzione:**
```bash
playwright install chromium
```

Se fallisce ancora:
```bash
pip install playwright
python -m playwright install chromium
```

---

### Errori di Permesso Negato (Unix/Linux)

**Sintomo:** `Permission denied` quando si cerca di eseguire gli script

**Soluzione:**
```bash
chmod +x ~/.gemini/skills/seo-special/scripts/*.py
chmod +x ~/.gemini/skills/seo-special/hooks/*.py
chmod +x ~/.gemini/skills/seo-special/hooks/*.sh
```

---

### Gli Hook non si avviano

**Sintomo:** Lo script di validazione per lo Schema non entra in azione in automatico

**Verifiche:**

1. Verifica che gli hook siano registrati nelle impostazioni (se l'ambiente lo supporta)
2. Effettua un test manuale dell'hook bypassando l'automazione:
```bash
python3 ~/.gemini/skills/seo-special/hooks/validate-schema.py test.html
```

---

### Sottoagente non trovato

**Sintomo:** `Agent 'seo-technical' not found` o l'AI risponde di non poter gestire i subagent

**Soluzione:**

1. Verifica che i file Markdown degli agenti esistano:
```bash
ls ~/.gemini/skills/seo-special/subagents/seo-*.md
```

2. Controlla il frontmatter per rintracciare eventuali difetti di parsing:
```bash
head -5 ~/.gemini/skills/seo-special/subagents/seo-technical.md
```

---

### Errori di Timeout

**Sintomo:** `Request timed out after 30 seconds` o "Tempo scaduto"

**Soluzioni:**

1. Il sito web target potrebbe essere temporaneamente sovraccaricato o lento — riprova
2. Aumenta il valore di timeout nelle chiamate dello script
3. Verifica la tua connessione di rete
4. Alcuni siti bloccano esplicitamente le richieste automatizzate (protezioni antibot/Cloudflare)

---

### Falsi Positivi sulla Validazione dello Schema

**Sintomo:** L'hook o il JSON generati segnalano errori inesatti

**Verifiche:**

1. Accertati in primo luogo che i classici placeholder AI (es. `[NOME AZIENDA]`) siano stati sostituiti
2. Verifica che `@context` sia valorizzato sempre a `https://schema.org`
3. Cerca tipi schema deprecati (es. `HowTo`, `SpecialAnnouncement`)
4. Valida esplicitamente con il  [Test dei Risultati Multimediali di Google](https://search.google.com/test/rich-results)

---

### Avvio lento dell'Audit

**Sintomo:** La richiesta di full audit impiega troppo tempo per rispondere

**Soluzioni:**

1. Considera che il "Full Audit" scansiona fino a 500 pagine — su portali corposi **è normale** richieda tempo
2. I sub-agenti operano in background: monitora lo stato dell'ambiente e il traffico generato
3. Per test iper-rapidi, esegui `/seo page` su URL singole di landing page
4. Controlla i Time To First Byte (TTFB) del sito; tempi di reazione scarsi dilatano infinitamente l'audit

---

## Ricevere Assistenza

1. **Consulta la Documentazione:** Leggi attentamente [COMMANDS.md](COMMANDS.md) e [ARCHITECTURE.md](ARCHITECTURE.md)
2. **Issue su GitHub:** Segnala i bug in forma ufficiale all'interno della [Repository del progetto](https://github.com/CinaWeb/Skills).

## Modalità Debug

Per osservare da vicino lo stack di output e rintracciare difetti occulti, esegui gli script ausiliari a mano:

```bash
# Esempio Test fetch
python3 ~/.gemini/skills/seo-special/scripts/fetch_page.py https://example.com

# Esempio Test parser HTML
python3 ~/.gemini/skills/seo-special/scripts/parse_html.py page.html --json

# Esempio Test generazione Screenshot
python3 ~/.gemini/skills/seo-special/scripts/capture_screenshot.py https://example.com
```
