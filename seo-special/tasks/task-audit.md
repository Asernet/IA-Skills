---
name: task-audit
description: Audit SEO completo del sito web con delega ai sub-agenti. Scansiona fino a 500 pagine, rileva il tipo di business e genera un punteggio di salute.
---

# Audit SEO Completo del Sito Web

## Processo Operativo

1. **Recupero Homepage:** Utilizza `scripts/fetch_page.py` per ottenere l'HTML della home.
2. **Rilevamento Business:** Analizza i segnali della homepage (es. e-commerce, blog, locale, SaaS).
3. **Scansione (Crawl):** Segui i link interni fino a 500 pagine, rispettando il file `robots.txt`.
4. **Delega ai Sub-agenti:** Coordina l'analisi specialistica:
   - `seo-technical`: robots.txt, sitemap, canonical, Core Web Vitals, sicurezza.
   - `seo-content`: E-E-A-T, leggibilità, contenuti scarsi, citabilità AI.
   - `seo-schema`: Rilevamento, validazione e opportunità mancanti.
   - `seo-sitemap`: Analisi struttura e quality gate località.
   - `seo-performance`: Misurazioni LCP, INP, CLS.
   - `seo-visual`: Screenshot, test mobile, above-the-fold.
5. **Punteggio (Scoring):** Aggrega i risultati in un SEO Health Score (0-100).
6. **Report Finale:** Genera un piano d'azione prioritizzato.

## Configurazione Scansione

- **Pagine Max:** 500
- **Rispetto robots.txt:** Sì
- **Segui Redirect:** Sì (max 3 salti)
- **Timeout per pagina:** 30 secondi
- **Richieste simultanee:** 5
- **Ritardo tra richieste:** 1 secondo

# File di Output (Output Files)

- FULL-AUDIT-REPORT.md — Risultati completi dell'analisi (Comprehensive findings).
- ACTION-PLAN.md — Raccomandazioni ordinate per priorità (Critico → Alto → Medio → Basso).
- screenshots/ — Catture schermata desktop e mobile (se il modulo Playwright è disponibile).

## Pesi dello Scoring

| Categoria                    | Peso |
|------------------------------|------|
| SEO Tecnico                  | 25% |
| Qualità Contenuti            | 25% |
| SEO On-Page                  | 20% |
| Schema / Dati Strutturati    | 10% |
| Performance (CWV)            | 10% |
| Immagini                     | 5% |
| Predisposizione Ricerca AI   | 5% |

## Struttura del Report

### Executive Summary
- Punteggio Salute SEO Globale (0-100)
- Tipo di business rilevato
- Top 5 problemi critici
- Top 5 "Quick Wins" (vittorie rapide)

### SEO Tecnico (Technical SEO)
- Problemi di scansionabilità (Crawlability)
- Errori di indicizzabilità
- Criticità relative alla sicurezza
- Stato dei Core Web Vitals

### Qualità dei Contenuti (Content Quality)
- Valutazione E-E-A-T
- Pagine con contenuti scarsi (Thin content)
- Problemi di contenuti duplicati
- Punteggi di leggibilità (Readability)

### SEO On-Page
- Criticità dei Title tag
- Errori nelle Meta description
- Struttura delle intestazioni (Heading)
- Lacune nel collegamento interno (Internal linking)

### Schema e Dati Strutturati
- Implementazione attuale
- Errori di validazione
- Opportunità mancanti

### Prestazioni (Performance)
- Punteggi LCP, INP e CLS
- Esigenze di ottimizzazione delle risorse
- Impatto degli script di terze parti

### Immagini
- Testi alternativi (Alt text) mancanti
- Immagini sovradimensionate
- Raccomandazioni sui formati (es. WebP/AVIF)

### Predisposizione alla AI Search (AI Search Readiness)
- Punteggio di citabilità (Citability score)
- Miglioramenti strutturali
- Segnali di autorevolezza

### Dettaglio Categorie
- Analisi approfondita per ogni ambito tecnico e contenutistico.

## Definizioni Priorità

- **Critico:** Blocca l'indicizzazione o causa penalità (risolvere immediatamente).
- **Alto:** Impatta significativamente il ranking (risolvere entro 1 settimana).
- **Medio:** Opportunità di ottimizzazione (risolvere entro 1 mese).
- **Basso:** Miglioramenti opzionali (backlog).
