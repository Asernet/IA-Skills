# Riferimento dei Comandi

## Panoramica

Tutti i comandi di Gemini SEO iniziano con `/seo` seguito da un sottocomando.

## Elenco dei Comandi

### `/seo audit <url>`

Audit SEO completo del sito web con analisi in parallelo.

**Esempio:**
```
/seo audit https://example.com
```

**Cosa fa:**
1. Esamina fino a 500 pagine
2. Rileva il tipo di attività aziendale
3. Delega il lavoro a 6 sottoagenti specialisti in parallelo
4. Genera il Punteggio di Salute SEO (0-100)
5. Crea un piano d'azione con priorità

**Output:**
- `FULL-AUDIT-REPORT.md`
- `ACTION-PLAN.md`
- `screenshots/` (se Playwright è disponibile)

---

### `/seo page <url>`

Analisi profonda di una singola pagina.

**Esempio:**
```
/seo page https://example.com/about
```

**Cosa analizza:**
- SEO On-page (title, meta, heading, URL)
- Qualità del contenuto (conteggio parole, leggibilità, E-E-A-T)
- Elementi tecnici (canonical, robots, Open Graph)
- Markup Schema
- Immagini (testo alternativo, dimensioni, formati)
- Potenziali problemi nei Core Web Vitals

---

### `/seo technical <url>`

Audit SEO tecnico su 8 categorie.

**Esempio:**
```
/seo technical https://example.com
```

**Categorie:**
1. Scansionabilità
2. Indicizzabilità
3. Sicurezza
4. Struttura degli URL
5. Ottimizzazione mobile
6. Core Web Vitals (LCP, INP, CLS)
7. Dati strutturati
8. Rendering JavaScript

---

### `/seo content <url>`

Analisi dell'E-E-A-T e della qualità dei contenuti.

**Esempio:**
```
/seo content https://example.com/blog/post
```

**Cosa valuta:**
- Segnali di esperienza (conoscenza di prima mano)
- Competenza (credenziali dell'autore)
- Autorevolezza (riconoscimento esterno)
- Affidabilità (trasparenza, sicurezza)
- Predisposizione alle citazioni IA
- Freschezza dei contenuti

---

### `/seo schema <url>`

Rilevamento, validazione e generazione di markup Schema.

**Esempio:**
```
/seo schema https://example.com
```

**Cosa fa:**
- Rileva gli schema esistenti (JSON-LD, Microdata, RDFa)
- Convalida in base ai requisiti di Google
- Identifica opportunità mancanti
- Genera JSON-LD pronto all'uso

---

### `/seo geo <url>`

Panoramiche IA / Generative Engine Optimization (GEO).

**Esempio:**
```
/seo geo https://example.com/blog/guide
```

**Cosa analizza:**
- Punteggio di citabilità (fatti citabili, statistiche)
- Leggibilità strutturale (titoli, elenchi, tabelle)
- Chiarezza dell'entità (definizioni, contesto)
- Segnali di autorità (credenziali, fonti)
- Supporto ai dati strutturati

---

### `/seo images <url>`

Analisi dell'ottimizzazione delle immagini.

**Esempio:**
```
/seo images https://example.com
```

**Cosa controlla:**
- Presenza e qualità del testo alternativo (alt text)
- Dimensioni dei file (segnala >200KB)
- Formati (raccomandazioni WebP/AVIF)
- Immagini reattive (srcset, sizes)
- Lazy loading
- Prevenzione del CLS (dimensioni dichiarate)

---

### `/seo sitemap <url>`

Analizza la sitemap XML esistente.

**Esempio:**
```
/seo sitemap https://example.com/sitemap.xml
```

**Cosa verifica:**
- Formato XML
- Numero di URL (<50k per file)
- Codici di stato degli URL
- Accuratezza del tag lastmod
- Tag deprecati (priority, changefreq)
- Copertura rispetto alle pagine indicizzate

---

### `/seo sitemap generate`

Genera una nuova sitemap con modelli di settore.

**Esempio:**
```
/seo sitemap generate
```

**Processo:**
1. Seleziona o rileva automaticamente il tipo di azienda
2. Pianificazione interattiva della struttura
3. Applica soglie di qualità (limiti di 30/50 pagine di località)
4. Genera XML valido
5. Crea documentazione

---

### `/seo plan <type>`

Pianificazione strategica SEO.

**Tipi:** `saas`, `local`, `ecommerce`, `publisher`, `agency`

**Esempio:**
```
/seo plan saas
```

**Cosa crea:**
- Strategia SEO completa
- Analisi competitiva
- Calendario editoriale
- Roadmap di implementazione (4 fasi)
- Progettazione dell'architettura del sito

---

### `/seo competitor-pages [url|generate]`

Generazione di pagine di confronto con la concorrenza.

**Esempi:**
```
/seo competitor-pages https://example.com/vs/competitor
/seo competitor-pages generate
```

**Capacità:**
- Generazione layout di pagine comparabili "X vs Y"
- Creazione di strutture per pagine "Alternative a X"
- Creazione di matrici di confronto delle funzionalità con punteggio
- Generazione markup Schema "Product" + "AggregateRating"
- Posizionamento ottimizzato della CTA (Call to Action) per conversioni
- Applica linee guida di equità (dati accurati, citazioni da fonti)

---

### `/seo hreflang [url]`

Audit Hreflang e generazione per la SEO internazionale.

**Esempio:**
```
/seo hreflang https://example.com
```

**Capacità:**
- Convalida tag hreflang autoreferenziali
- Verifica la reciprocità del tag di ritorno (A→B richiede B→A)
- Verifica la presenza del tag x-default
- Convalida i codici di lingua ISO 639-1 e regionali ISO 3166-1
- Controlla l'allineamento degli URL canonici con hreflang
- Rileva problemi di conformità di protocollo (HTTP vs HTTPS)
- Genera correttamente tag dei link hreflang e sitemap XML

---

### `/seo programmatic [url|plan]`

Analisi e pianificazione SEO programmatica per pagine scalate su larga scala.

**Esempi:**
```
/seo programmatic https://example.com/tools/
/seo programmatic plan
```

**Capacità:**
- Valuta la qualità delle origini dati (CSV, JSON, API, database)
- Piani con motori di template per un contenuto per pagina unico 
- Modella strategie tramite URL es. (`/tools/[tool-name]`, `/[city]/[service]`)
- Automatizza i collegamenti interni (hub/spoke, oggetti correlati, breadcrumbs)
- Applica filtri contro i "thin content" (soglie di qualità e del conteggio di parole)
- Previene l'eccesso indicizzato (noindex per basso valore, paginazione estesa e nav-faccettata)

---

## Riferimento Rapido

| Comando | Caso d'uso |
|---------|----------|
| `/seo audit <url>` | Audit completo del sito web |
| `/seo competitor-pages [url\|generate]` | Pagine di confronto con i competitor |
| `/seo content <url>` | Analisi della qualità / E-E-A-T |
| `/seo geo <url>` | Ottimizzazione per l'IA |
| `/seo hreflang [url]` | Audit hreflang / i18n |
| `/seo images <url>` | Ottimizzazione immagini |
| `/seo page <url>` | Analisi della singola pagina |
| `/seo plan <type>` | Pianificazione della strategia |
| `/seo programmatic [url\|plan]` | Analisi programmatica della SEO |
| `/seo schema <url>` | Audit schema/Markup Validation |
| `/seo sitemap <url>` | Analisi e validazioni Sitemap |
| `/seo sitemap generate` | Creazione di una Sitemap |
| `/seo technical <url>` | Check Tecnico SEO globale |
