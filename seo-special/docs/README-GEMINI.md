# Guida Utente: SEO-Special Power Module per Gemini CLI

Il modulo **SEO-Special** è un toolkit avanzato per l'analisi SEO di nuova generazione, ottimizzato per gli standard del **2026** e integrato nativamente in Gemini CLI.

## Come Invocare il Modulo

Puoi attivare le analisi SEO utilizzando i seguenti trigger naturali:

### 1. Audit Completo
Scansiona il sito, rileva il business e coordina i sub-agenti per un report a 360°.
- `seo audit [URL]`
- `analizza il mio sito [URL]`

### 2. SEO Tecnico & Performance
Analisi di scansione, indicizzabilità e Core Web Vitals (focus su INP).
- `seo technical [URL]`
- `cwv 2026 [URL]`
- `sitemap check [URL]`

### 3. Ottimizzazione AI (GEO)
Prepara il tuo sito per ChatGPT, Perplexity e Google AI Overviews.
- `seo geo [URL]`
- `ai search optimization [URL]`

### 4. Qualità Contenuti & E-E-A-T
Valuta l'autorità, l'esperienza e la predisposizione alle citazioni AI.
- `eeat check [URL]`
- `analisi contenuti [URL]`

## Struttura dei Report
Tutti i report sono generati in **Italiano** e includono:
- **Punteggio Salute (0-100)**: Un voto sintetico per ogni categoria.
- **Priorità d'Azione**: Problemi suddivisi in Critici, Alti, Medi e Bassi.
- **Snippet JSON-LD**: Codice pronto da copiare per i dati strutturati.
- **Action Plan**: Una roadmap strategica per il miglioramento dei ranking.

## Manutenzione e Verifica
Per verificare che l'ambiente sia configurato correttamente (Python, Playwright, Dipendenze), esegui lo script di hardening:
`python scripts/init_module.py`

---
*Modulo configurato e validato il 3 Marzo 2026.*
