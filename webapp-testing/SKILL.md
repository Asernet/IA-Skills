---
name: webapp-testing
description: Toolkit per testare applicazioni web locali con Playwright: verifica UI, screenshot e debug.
---

# Testing Applicazioni Web

Per testare applicazioni web locali, scrivi script Python Playwright nativi.

**Script Helper Disponibili**:

- `scripts/with_server.py` - Gestisce il ciclo di vita del server (supporta server multipli)

**Esegui sempre gli script con `--help` prima** per vedere l'uso. NON leggere il sorgente finché non provi ad eseguire lo script prima e trovi che una soluzione personalizzata è assolutamente necessaria. Questi script possono essere molto grandi e quindi inquinare la tua finestra di contesto. Esistono per essere chiamati direttamente come script black-box piuttosto che ingeriti nella tua finestra di contesto.

## Albero Decisionale: Scegliere il Tuo Approccio

```
Task Utente → È HTML statico?
    ├─ Sì → Leggi file HTML direttamente per identificare selettori
    │         ├─ Successo → Scrivi script Playwright usando selettori
    │         └─ Fallisce/Incompleto → Tratta come dinamico (sotto)
    │
    └─ No (webapp dinamica) → Il server è già in esecuzione?
        ├─ No → Esegui: python scripts/with_server.py --help
        │        Poi usa l'helper + scrivi script Playwright semplificato
        │
        └─ Sì → Ricognizione-poi-azione:
            1. Naviga e aspetta per networkidle
            2. Prendi screenshot o ispeziona DOM
            3. Identifica selettori stato renderizzato
            4. Esegui azioni con selettori scoperti
```

## Esempio: Usare with_server.py

Per avviare un server, esegui `--help` prima, poi usa l'helper:

**Server singolo:**

```bash
python scripts/with_server.py --server "npm run dev" --port 5173 -- python your_automation.py
```

**Server multipli (es., backend + frontend):**

```bash
python scripts/with_server.py \
  --server "cd backend && python server.py" --port 3000 \
  --server "cd frontend && npm run dev" --port 5173 \
  -- python your_automation.py
```

Per creare uno script di automazione, includi solo logica Playwright (i server sono gestiti automaticamente):

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True) # Always launch chromium in headless mode
    page = browser.new_page()
    page.goto('http://localhost:5173') # Server already running and ready
    page.wait_for_load_state('networkidle') # CRITICAL: Wait for JS to execute
    # ... your automation logic
    browser.close()
```

## Pattern Ricognizione-Poi-Azione

1. **Ispeziona DOM renderizzato**:

   ```python
   page.screenshot(path='/tmp/inspect.png', full_page=True)
   content = page.content()
   page.locator('button').all()
   ```

2. **Identifica selettori** dai risultati ispezione

3. **Esegui azioni** usando selettori scoperti

## Trappola Comune

❌ **Non** ispezionare il DOM prima di aspettare `networkidle` su app dinamiche
✅ **Fai** aspettare `page.wait_for_load_state('networkidle')` prima dell'ispezione

## Best Practice

- **Usa script pacchettizzati come black box** - Per compiere un task, considera se uno degli script disponibili in `scripts/` può aiutare. Questi script gestiscono workflow comuni e complessi affidabilmente senza ingombrare la finestra contesto. Usa `--help` per vedere l'uso, poi invoca direttamente.
- Usa `sync_playwright()` per script sincroni
- Chiudi sempre il browser quando fatto
- Usa selettori descrittivi: `text=`, `role=`, selettori CSS, o ID
- Aggiungi attese appropriate: `page.wait_for_selector()` o `page.wait_for_timeout()`

## File Riferimento

- **examples/** - Esempi che mostrano pattern comuni:
  - `element_discovery.py` - Scoprire bottoni, link e input su una pagina
  - `static_html_automation.py` - Usare URL file:// per HTML locale
  - `console_logging.py` - Catturare log console durante automazione
