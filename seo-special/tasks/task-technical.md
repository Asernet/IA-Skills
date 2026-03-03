---
name: task-technical
description: Audit SEO tecnico in 8 categorie: scansione, indicizzabilità, sicurezza, struttura URL, mobile, Core Web Vitals, dati strutturati e rendering JavaScript.
---

# Audit SEO Tecnico (Aggiornamento 2026)

## Categorie di Analisi

### 1. Scansione (Crawlability)
- `robots.txt`: esistente, valido, non blocca risorse critiche.
- `Sitemap XML`: riferita in robots.txt, formato valido.
- **Gestione Crawler AI:** Verifica accesso per GPTBot, ClaudeBot, PerplexityBot.
- **llms.txt:** Presenza del file per la guida dei crawler AI.

### 2. Indicizzabilità (Indexability)
- **Tag Canonical:** autoriferiti, senza conflitti con noindex.
- **Contenuti Duplicati:** parametri URL, www vs non-www.
- **Thin Content:** pagine sotto i minimi di parole per tipo.
- **Hreflang:** corretti per siti multilingua/multiregione.

### 3. Sicurezza
- **HTTPS:** forzato, certificato valido, nessun contenuto misto.
- **Header di Sicurezza:** CSP, HSTS, X-Frame-Options, X-Content-Type-Options.

### 4. Struttura URL
- **URL Puliti:** descrittivi, con trattini, senza parametri inutili.
- **Gerarchia:** struttura cartelle logica.
- **Redirect:** nessuna catena (max 1 salto), 301 per spostamenti permanenti.

### 5. Ottimizzazione Mobile
- **Responsive Design:** meta tag viewport, CSS responsive.
- **Target Tattili:** min 48x48px con spaziatura 8px.
- **Font:** base min 16px.
- **Mobile-First Indexing:** Google scansiona ESCLUSIVAMENTE con Googlebot mobile (completato Luglio 2024).

### 6. Core Web Vitals (CWV 2026)
- **LCP** (Largest Contentful Paint): target <2.5s.
- **INP** (Interaction to Next Paint): target <200ms.
  - **IMPORTANTE:** INP ha sostituito FID definitivamente a Marzo 2024.
- **CLS** (Cumulative Layout Shift): target <0.1.
- Valutazione basata sul **75° percentile** dei dati reali.

### 7. Dati Strutturati (Schema)
- Rilevamento: JSON-LD (preferito), Microdata, RDFa.
- Validazione rispetto ai tipi supportati da Google.

### 8. Rendering JavaScript (JS SEO)
- Verifica se il contenuto critico richiede l'esecuzione di JS (CSR vs SSR).
- **Update Dicembre 2025:**
  - Google NON esegue JS su pagine che restituiscono codici di stato non-200.
  - I dati strutturati iniettati via JS possono subire ritardi nell'elaborazione.
  - I tag canonical in HTML crudo vincono su quelli iniettati via JS se in conflitto.

---

## Formato Output

### Punteggio Tecnico: XX/100

| Categoria | Stato | Punteggio |
|-----------|-------|-----------|
| Scansione | ✅/⚠️/❌ | XX/100 |
| Indicizzabilità | ✅/⚠️/❌ | XX/100 |
| Sicurezza | ✅/⚠️/❌ | XX/100 |
| Struttura URL | ✅/⚠️/❌ | XX/100 |
| Mobile | ✅/⚠️/❌ | XX/100 |
| Core Web Vitals | ✅/⚠️/❌ | XX/100 |
| Dati Strutturati | ✅/⚠️/❌ | XX/100 |
| Rendering JS | ✅/⚠️/❌ | XX/100 |

### Problemi Critici (Risolvere immediatamente)
### Alta Priorità (Entro 1 settimana)
### Media Priorità (Entro 1 mese)
### Bassa Priorità (Backlog)
