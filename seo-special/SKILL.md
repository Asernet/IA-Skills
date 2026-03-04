---
name: seo-special
description: >
  L'Orchestratore Universale SEO-Special Power Module. Esegue audit profondi 
  basati su evidenze reali. Utilizza la SEO Station sul Desktop.
  Analisi SEO completa per qualsiasi sito web o tipologia di business. Esegue audit integrali del sito potenziati da automazione Python (Playwright, BeautifulSoup4), analisi approfondite della singola pagina, controlli SEO tecnici (scansionabilità, indicizzabilità, Core Web Vitals con INP), rilevamento/validazione/generazione di markup Schema, valutazione della qualità dei contenuti (framework E-E-A-T aggiornato a dicembre 2025), ottimizzazione delle immagini, analisi della sitemap e Generative Engine Optimization (GEO) per AI Overviews, citazioni su ChatGPT e Perplexity. Analizza l'accessibilità per i crawler AI (GPTBot, ClaudeBot, PerplexityBot), la conformità al file llms.txt e la citabilità passage-level. Rilevamento automatico del settore (SaaS, e-commerce, local, ecc.).
version: 1.2.0
category: seo
tags:
  [
    seo,
    audit,
    technical,
    content,
    geo,
    schema,
    e-e-a-t,
    performance,
    sitemap,
    programmatic,
  ]
triggers:
  ["seo audit", "seo technical", "seo content", "seo geo", "audit profondo"]
allowed-tools: [Read, Grep, Glob, Bash, WebFetch]
---

# SEO-Special: Modulo di Analisi SEO Universale

## Overview

Questa skill è l'Orchestratore Universale progettato per eseguire analisi SEO complete e professionali su qualsiasi sito web o tipologia di business. Coordina 12 competenze specializzate e 6 sotto-agenti per produrre report basati su evidenze tecniche reali, utilizzando la "SEO Station" sul Desktop dell'utente.

La skill integra automazione Python (Playwright, BeautifulSoup4) per il recupero dei dati, analisi della qualità dei contenuti secondo il framework E-E-A-T (aggiornato a dicembre 2025) e strategie di Generative Engine Optimization (GEO) per massimizzare la visibilità su AI Overviews, ChatGPT e Perplexity. Analizza l'accessibilità per i crawler AI (GPTBot, ClaudeBot, PerplexityBot), la conformità al file `llms.txt` e la citabilità passage-level. Il sistema esegue un rilevamento automatico del settore (SaaS, e-commerce, locale, ecc.) per adattare l'analisi al contesto specifico.

---

## Riferimento Rapido (Quick Reference)

| Comando                            | Descrizione Funzionalità (Azione)                    |
| ---------------------------------- | ---------------------------------------------------- |
| `audit <url>`                      | Audit completo del sito con delega ai sotto-agenti   |
| `page <url>`                       | Analisi approfondita di una singola pagina           |
| `sitemap <url\|generate>`          | Analisi o generazione di Sitemap XML                 |
| `schema <url>`                     | Rilevamento, validazione e generazione markup Schema |
| `images <url>`                     | Analisi ottimizzazione immagini                      |
| `technical <url>`                  | Audit SEO Tecnico (8 categorie)                      |
| `content <url>`                    | Analisi qualità e parametri E-E-A-T                  |
| `geo <url>`                        | Ottimizzazione per Motori Generativi (GEO/AI)        |
| `plan <settore>`                   | Pianificazione strategica SEO                        |
| `programmatic [url\|plan]`         | Analisi e pianificazione SEO programmatica           |
| `competitor-pages [url\|generate]` | Generazione pagine di confronto con i competitor     |
| `hreflang [url]`                   | Audit e generazione tag SEO internazionale (i18n)    |

---

## Logica di Orchestrazione Automata (Workflow)

L'agente deve seguire questo protocollo Milestone-Based per ogni invocazione di `audit`:

1.  **Fase Dati (Python Entry)**: Eseguire gli script Python (`init_module.py`, `fetch_page.py`) per raccogliere dati grezzi reali (HTML, headers). Se necessario, utilizzare `capture_screenshot.py` per l'analisi visuale.
2.  **Rilevamento Settore**: Identificare la tipologia di business consultando `references/industry-signals.md`.
3.  **Delega Parallela**: Avviare i sotto-agenti (in `subagents/`) basandosi sui file estratti nella cartella `data/`.
4.  **Sintesi Multimodale**: Leggere i risultati dei task e assegnare un Punteggio di Salute SEO (SEO Health Score) ricalibrato.
5.  **Fare un Audit Base**: Usare `task-audit` per fare un audit base del sito e salvarne il contenuto in un file md.
6.  **Piano d'Azione**: Creare una roadmap prioritaria (Critico → Alto → Medio → Basso).

Per i singoli comandi, caricare direttamente la relativa competenza presente in `tasks/task-*.md`.

---

## Standard Tecnologici e Design Patterns

### 1. Protocollo SEO Station (Inviolabile)
- **Directory di Lavoro**: Ogni operazione avviene rigorosamente in `Desktop/Progetti/[sito]/`.
- **Fase Dati**: Tutti i file grezzi (HTML, robots, json) devono essere salvati in `Desktop/Progetti/[sito]/data/`.
- **Fase Analisi**: L'agente deve leggere esplicitamente i file in `data/` prima di formulare ogni conclusione. I report senza dati tecnici estratti sono nulli.
- **Fase Report**: I risultati finali (.md e .pdf) sono salvati in `Desktop/Progetti/[sito]/report/`.
- **Fase Pulizia**: Eliminare i file temporanei e non utili all'utente dopo ogni operazione.

### 2. Regole Tassative di Analisi
- Mai raccomandare lo schema `HowTo` (deprecato).
- Schema `FAQ` ammesso solo per siti governativi, sanitari e di pubblica utilità, anche per e-commerce.
- Tutti i riferimenti ai Core Web Vitals devono usare l'**INP**, mai il FID.
- Verificare sempre l'ambiente Python tramite `requirements.txt` prima di eseguire script.
- **Interattività**: Chiedere conferma prima di ogni Milestone di analisi profonda.

---

## Metodologia di Punteggio (Scoring)

Il **Punteggio di Salute SEO (0-100)** è un aggregato ponderato di tutte le categorie:

| Categoria                       | Peso |
| ------------------------------- | ---- |
| SEO Tecnico                     | 25%  |
| Qualità dei Contenuti           | 20%  |
| Predisposizione AI Search (GEO) | 15%  |
| SEO On-Page                     | 15%  |
| Schema / Dati Strutturati       | 10%  |
| Prestazioni (CWV)               | 10%  |
| Ottimizzazione Immagini         | 5%   |

### Livelli di Priorità
- **Critico (Critical)**: Blocca l'indicizzazione o causa penalizzazioni (correzione immediata).
- **Alto (High)**: Impatta significativamente il posizionamento (correggere entro 1 settimana).
- **Medio (Medium)**: Opportunità di ottimizzazione (correggere entro 1 mese).
- **Basso (Low)**: Miglioramento consigliato (da inserire nel backlog).

---

## Struttura della Skill (Competenze e Sotto-agenti)

### Competenze Specifiche (Tasks)
- `task-audit`: Audit completo con delega parallela.
- `task-page`: Analisi approfondita della singola pagina.
- `task-technical`: SEO Tecnico suddiviso in 8 categorie.
- `task-content`: Analisi E-E-A-T e qualità contenuti.
- `task-schema`: Rilevamento e generazione markup Schema.org.
- `task-images`: Ottimizzazione immagini.
- `task-sitemap`: Analisi e generazione Sitemap XML.
- `task-geo`: Ottimizzazione per AI Overviews e GEO.
- `task-plan`: Pianificazione strategica basata su modelli.
- `task-programmatic`: Analisi/pianificazione SEO programmatica.
- `task-competitor-pages`: Confronto qualitativo con i competitor.
- `task-hreflang`: Audit e generazione tag per SEO internazionale.

### Sotto-agenti Specializzati (Subagents)
- `seo-technical`: Scansionabilità, indicizzabilità, sicurezza e CWV.
- `seo-content`: Valutazione E-E-A-T, leggibilità e thin content.
- `seo-schema`: Rilevamento, validazione e generazione dati strutturati.
- `seo-sitemap`: Analisi struttura, copertura e quality gates.
- `seo-performance`: Misurazione tecnica dei Core Web Vitals.
- `seo-visual`: Screenshot, usabilità mobile e analisi above-the-fold.

---

## Risorse Bundled (Appendici)

Consultare i file in `references/` per soglie e framework:
- `references/industry-signals.md`: Euristiche rilevamento settore.
- `references/quality-gates.md`: Limiti per thin content e spam.
- `references/cwv-thresholds.md`: Soglie Core Web Vitals 2026.
- `references/schema-types.md`: Mappatura tipi Schema.org supportati.
- `references/eeat-framework.md`: Guida alla valutazione della qualità.
