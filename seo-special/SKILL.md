---
name: seo-special
description: >
  L'Orchestratore Universale SEO-Special Power Module. Esegue audit profondi 
  basati su evidenze reali. Utilizza la SEO Station sul Desktop.
  Analisi SEO completa per qualsiasi sito web o tipologia di business. Esegue audit integrali del sito potenziati da automazione Python (Playwright, BeautifulSoup4), analisi approfondite della singola pagina, controlli SEO tecnici (scansionabilità, indicizzabilità, Core Web Vitals con INP), rilevamento/validazione/generazione di markup Schema, valutazione della qualità dei contenuti (framework E-E-A-T aggiornato a dicembre 2025), ottimizzazione delle immagini, analisi della sitemap e Generative Engine Optimization (GEO) per AI Overviews, citazioni su ChatGPT e Perplexity. Analizza l'accessibilità per i crawler AI (GPTBot, ClaudeBot, PerplexityBot), la conformità al file llms.txt e la citabilità passage-level. Rilevamento automatico del settore (SaaS, e-commerce, local, ecc.). Si attiva con: "SEO", "audit", "schema", "GEO", "SEO tecnico", "qualità dei contenuti".
triggers:
  ["seo audit", "seo technical", "seo content", "seo geo", "audit profondo"]
allowed-tools: [Read, Grep, Glob, Bash, WebFetch]
---

# SEO-Special — Universal SEO Analysis Module

Analisi SEO completa per tutti i settori (SaaS, servizi locali, e-commerce, editoria, agenzie). Coordina 12 task specifici e 6 sotto-agenti specializzati.

## Quick Reference

| Richiesta                          | What it does                                         |
| ---------------------------------- | ---------------------------------------------------- |
| `audit <url>`                      | Full website audit with parallel subagent delegation |
| `page <url>`                       | Deep single-page analysis                            |
| `sitemap <url or generate>`        | Analyze or generate XML sitemaps                     |
| `schema <url>`                     | Detect, validate, and generate Schema.org markup     |
| `images <url>`                     | Image optimization analysis                          |
| `technical <url>`                  | Technical SEO audit (8 categories)                   |
| `content <url>`                    | E-E-A-T and content quality analysis                 |
| `geo <url>`                        | AI Overviews / Generative Engine Optimization        |
| `plan <business-type>`             | Strategic SEO planning                               |
| `programmatic [url\|plan]`         | Programmatic SEO analysis and planning               |
| `competitor-pages [url\|generate]` | Competitor comparison page generation                |
| `hreflang [url]`                   | Hreflang/i18n SEO audit and generation               |

# Logica di Orchestrazione Automata

Quando l'utente invoca il comando `audit`, l'agente DEVE seguire questo workflow Milestone-Based:

1.  **Fase Data (Python Entry):** Eseguire `init_module.py` e `fetch_page.py` per raccogliere dati grezzi reali (HTML, headers). Se necessario, usare `capture_screenshot.py` per l'analisi visuale.
2.  **Rilevamento Settore:** Consultare `references/industry-signals.md` per identificare la tipologia di business.
3.  **Delega Parallela:** Avviare i sotto-agenti (`subagents/`) basandosi sui file estratti nella cartella `data/`.
4.  **Sintesi Multimodale:** Leggere i risultati dei task e generare un report unificato con un Punteggio di Salute SEO (SEO Health Score) ricalibrato.
5.  **Piano d'Azione:** Creare una roadmap prioritaria (Critico → Alto → Medio → Basso).

Per i singoli comandi, carica direttamente la relativa competenza (`tasks/task-*.md`).

# Conoscenza e Standard (Reference)

L'agente non deve inventare soglie o segnali, ma consultare i file in `references/`:

- 🔍 **Settori**: `references/industry-signals.md` (euristiche di rilevamento).
- 🛡️ **Qualità**: `references/quality-gates.md` (limiti per "thin content" e doorway pages).
- ⚡ **Prestazioni**: `references/cwv-thresholds.md` (soglie Core Web Vitals 2026).
- 📜 **Schema**: `references/schema-types.md` (stato tipi Schema.org).
- 🏆 **E-E-A-T**: `references/eeat-framework.md` (framework di valutazione qualità).

### Regole Tassative:

- Mai raccomandare lo schema `HowTo` (deprecato).
- Schema `FAQ` ammesso solo per siti governativi e sanitari.
- Tutti i riferimenti ai Core Web Vitals devono usare l'**INP**, mai il FID.
- Verificare sempre l'ambiente Python tramite `requirements.txt` prima di eseguire script.

# Metodologia di Punteggio (Scoring Methodology)

## Punteggio di Salute SEO (0-100)

Aggregato ponderato di tutte le categorie:

| Categoria                       | Peso |
| ------------------------------- | ---- |
| SEO Tecnico                     | 25%  |
| Qualità dei Contenuti           | 20%  |
| Predisposizione AI Search (GEO) | 15%  |
| SEO On-Page                     | 15%  |
| Schema / Dati Strutturati       | 10%  |
| Prestazioni (CWV)               | 10%  |
| Ottimizzazione Immagini         | 5%   |

## Livelli di Priorità

- **Critico (Critical):** Blocca l'indicizzazione o causa penalizzazioni (richiede correzione immediata).
- **Alto (High):** Impatta significativamente il posizionamento/ranking (correggere entro 1 settimana).
- **Medio (Medium):** Opportunità di ottimizzazione (correggere entro 1 mese).
- **Basso (Low):** Miglioramento consigliato (da inserire nel backlog).

# Competenze Specifiche (Tasks)

Questo modulo orchestra 12 competenze specializzate:

- task-audit — Audit completo del sito web con delega parallela ai sotto-agenti.
- task-page — Analisi approfondita della singola pagina (deep page analysis).
- task-technical — SEO Tecnico suddiviso in 8 categorie.
- task-content — Analisi dell'E-E-A-T e della qualità dei contenuti.
- task-schema — Rilevamento e generazione di markup Schema.org.
- task-images — Ottimizzazione delle immagini.
- task-sitemap — Analisi e generazione di Sitemap XML.
- task-geo — Ottimizzazione per AI Overviews e GEO (Generative Engine Optimization).
- task-plan — Pianificazione strategica basata su modelli (templates).
- task-programmatic — Analisi e pianificazione di strategie SEO programmatiche.
- task-competitor-pages — Generazione di pagine di confronto con i competitor.
- task-hreflang — Audit e generazione di tag hreflang per SEO internazionale (i18n).

# Sotto-agenti (Subagents)

Per l'analisi in parallelo durante gli audit:

- seo-technical — Scansionabilità (crawlability), indicizzabilità, sicurezza e Core Web Vitals (CWV).
- seo-content — Valutazione E-E-A-T, leggibilità e analisi dei contenuti scarsi (thin content).
- seo-schema — Rilevamento, validazione e generazione di dati strutturati.
- seo-sitemap — Analisi della struttura, copertura e verifica dei criteri di qualità (quality gates).
- seo-performance — Misurazione tecnica dei Core Web Vitals.
- seo-visual — Screenshot, test di usabilità mobile e analisi dell'area above-the-fold.

## 🛑 PROTOCOLLO SEO STATION (Inviolabile)

1.  **Working Directory:** Ogni operazione avviene in `Desktop/SEO_WORKSPACE/`.
2.  **Fase Data:** Tutti i file grezzi (HTML, robots, json) devono essere salvati in `SEO_WORKSPACE/data/[sito]/`.
3.  **Fase Analisi:** L'agente DEVE leggere esplicitamente i file in `data/` prima di formulare ogni conclusione. I report senza dati tecnici estratti sono nulli.
4.  **Fase Report:** I risultati finali (.md e .pdf) sono salvati in `SEO_WORKSPACE/report/[sito]/`.
5.  **Interattività:** Chiedere conferma prima di ogni Milestone di analisi profonda.

## Workflow Milestone-Based

- **Step 0:** Inizializzazione Workspace e Fetch Dati.
- **Step 1:** Audit Tecnico (Lettura robots.txt e sitemaps reali).
- **Step 2:** Analisi Contenuti (Word count e E-E-A-T reale).
- **Step 3:** Strategia GEO (Verifica llms.txt riga per riga).
- **Step 4:** Schema Markup (Validazione blocchi JSON-LD estratti).
- **Step 5:** Consolidamento PDF.

[Comandi e Reference invariati...]
