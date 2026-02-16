# Riferimento Tool e API SEO/GEO

Elenco curato di strumenti e API per l'ottimizzazione SEO e GEO.

---

## Strumenti Gratuiti

### Generatori di Markup Schema

| Strumento             | URL                                            | Funzionalità                           |
| --------------------- | ---------------------------------------------- | -------------------------------------- |
| **TechnicalSEO.com**  | technicalseo.com/tools/schema-markup-generator | Molteplici tipi di schema, validazione |
| **Rank Ranger**       | rankranger.com/schema-markup-generator         | Schemi FAQ, Article, Product           |
| **Merkle**            | technicalseo.com/tools/schema-markup-generator | Generatore di schemi completo          |
| **JSON-LD Generator** | jsonld.com                                     | Semplice costruttore di schemi         |

### Strumenti di Validazione

| Strumento                              | URL                                    | Scopo                     |
| -------------------------------------- | -------------------------------------- | ------------------------- |
| **Test Risultati Multimediali Google** | search.google.com/test/rich-results    | Testare il markup schema  |
| **Validatore Schema.org**              | validator.schema.org                   | Validare qualsiasi schema |
| **Test Ottimizzazione Mobile Google**  | search.google.com/test/mobile-friendly | Usabilità mobile          |
| **PageSpeed Insights**                 | pagespeed.web.dev                      | Core Web Vitals           |

### Strumenti di Audit SEO

| Strumento                   | URL                              | Funzionalità                   |
| --------------------------- | -------------------------------- | ------------------------------ |
| **SEOmator**                | seomator.com/free-seo-audit-tool | Audit gratuito completo        |
| **Screaming Frog (Gratis)** | screamingfrog.co.uk              | Scansiona fino a 500 URL       |
| **Google Search Console**   | search.google.com/search-console | Dati ufficiali di Google       |
| **Bing Webmaster Tools**    | bing.com/webmasters              | Dati di indicizzazione di Bing |

---

## Strumenti SEO a Pagamento

### Piattaforme Complete

| Strumento      | Prezzo     | Ideale per                              |
| -------------- | ---------- | --------------------------------------- |
| **Ahrefs**     | $99/mese+  | Analisi backlink, ricerca parole chiave |
| **Semrush**    | $139/mese+ | Toolkit all-in-one SEO + GEO            |
| **Moz Pro**    | $99/mese+  | Autorità del dominio, link building     |
| **SE Ranking** | $65/mese+  | All-in-one conveniente                  |

### Ottimizzazione dei Contenuti

| Strumento      | Prezzo     | Ideale per                          |
| -------------- | ---------- | ----------------------------------- |
| **Surfer SEO** | $89/mese+  | Ottimizzazione contenuti per l'IA   |
| **Clearscope** | $170/mese+ | Ottimizzazione contenuti enterprise |
| **Frase**      | $15/mese+  | Brief di contenuti IA               |
| **MarketMuse** | $149/mese+ | Strategia dei contenuti             |

---

## Strumenti GEO / Visibilità AI

### Monitoraggio della Ricerca AI

| Strumento                 | Prezzo         | Piattaforme                         |
| ------------------------- | -------------- | ----------------------------------- |
| **Profound**              | $499/mese+     | ChatGPT, Perplexity, Claude, Gemini |
| **Otterly.ai**            | Prova gratuita | ChatGPT, Perplexity, Google AIO     |
| **SE Ranking AI Toolkit** | Incluso        | AI Overview, ChatGPT                |
| **Semrush AI Visibility** | Incluso        | Google AIO, ChatGPT                 |
| **Peec AI**               | Fascia media   | Sentiment + visibilità              |
| **Scrunch AI**            | Variabile      | Tracciamento brand, citazioni       |

### Funzionalità di Visibilità AI da Cercare

- Tracciamento delle citazioni su piattaforme AI
- Approfondimenti a livello di prompt
- Attribuzione della fonte
- Analisi del sentiment
- Benchmarking competitivo
- Raccomandazioni operative

---

## API per l'Automazione

### API di Google

| API                    | Scopo                                 | Documentazione                                           |
| ---------------------- | ------------------------------------- | -------------------------------------------------------- |
| **Search Console API** | Stato indicizzazione, dati di ricerca | developers.google.com/webmaster-tools                    |
| **PageSpeed API**      | Dati Core Web Vitals                  | developers.google.com/speed/docs/insights/v5/get-started |
| **Indexing API**       | Richiesta di indicizzazione           | developers.google.com/search/apis/indexing-api           |
| **Custom Search API**  | Ricerca programmatica                 | developers.google.com/custom-search                      |

### API per Dati SEO

| API                      | Scopo                   | Prezzo                     |
| ------------------------ | ----------------------- | -------------------------- |
| **DataForSEO**           | Dati SEO completi       | Pagamento per utilizzo     |
| **Moz API**              | DA, PA, dati dei link   | Incluso con Moz            |
| **Ahrefs API**           | Backlink, parole chiave | Incluso con Ahrefs         |
| **SE Ranking API**       | Ranking, audit          | Incluso con SE Ranking     |
| **SEO Review Tools API** | Vari controlli SEO      | Piano gratuito disponibile |

### API per Schema/Metadati

| API                          | Scopo                            | Prezzo                 |
| ---------------------------- | -------------------------------- | ---------------------- |
| **Apify Metadata Extractor** | Estrazione meta, sitemap, robots | $12/mese+              |
| **Firecrawl**                | Scansione siti web per SEO       | Pagamento per utilizzo |

---

## Estensioni Browser

### Analisi SEO

| Estensione                 | Browser        | Funzionalità            |
| -------------------------- | -------------- | ----------------------- |
| **SEOquake**               | Chrome/Firefox | Metriche SEO rapide     |
| **MozBar**                 | Chrome         | DA, PA, dati dei link   |
| **Ahrefs SEO Toolbar**     | Chrome         | Backlink, parole chiave |
| **Detailed SEO Extension** | Chrome         | Controlli SEO tecnici   |

### Test dello Schema

| Estensione                       | Browser | Funzionalità                      |
| -------------------------------- | ------- | --------------------------------- |
| **Structured Data Testing Tool** | Chrome  | Visualizza lo schema della pagina |
| **Schema Builder**               | Chrome  | Generatore di schema              |

---

## Strumenti da Riga di Comando

### Comandi curl per Controlli SEO

```bash
# Controlla i meta tag
curl -sL "https://example.com" | grep -E "<title>|<meta"

# Controlla il robots.txt
curl -s "https://example.com/robots.txt"

# Controlla la sitemap
curl -s "https://example.com/sitemap.xml"

# Controlla gli header HTTP
curl -I "https://example.com"

# Controlla la catena dei redirect
curl -sIL "https://example.com" | grep -E "HTTP|Location"

# Controlla la dimensione della pagina
curl -sL "https://example.com" | wc -c

# Controlla il tempo di caricamento
curl -o /dev/null -s -w "Totale: %{time_total}s\n" "https://example.com"
```

### Utilizzo delle API di Google via curl

```bash
# PageSpeed Insights (nessuna chiave API necessaria per base)
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com"

# Con chiave API (più richieste consentite)
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&key=LA_TUA_CHIAVE_API"
```

---

## Template Robots.txt per i Bot AI

```
# Motori di Ricerca
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# Bot AI
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Applebot-Extended
Allow: /

# Sitemap
Sitemap: https://example.com/sitemap.xml
```

---

## Script

Script Python pronti all'uso nella cartella `scripts/`.

### Configurazione (script DataForSEO)

```bash
export DATAFORSEO_LOGIN=il_tuo_login
export DATAFORSEO_PASSWORD=la_tua_password
```

### seo_audit.py

Audit SEO completo - meta tag, robots.txt, sitemap, tempo di caricamento, schema, accesso bot AI. Nessuna API richiesta.

```bash
python3 scripts/seo_audit.py "https://example.com"
```

### keyword_research.py

Ottieni idee per parole chiave, volume di ricerca, difficoltà.

```bash
python3 scripts/keyword_research.py "seo tools" --limit 20
python3 scripts/keyword_research.py "seo tools" --location 2826  # UK
```

### serp_analysis.py

Analizza i primi 20 risultati di Google per una parola chiave.

```bash
python3 scripts/serp_analysis.py "best seo tools" --depth 20
```

### backlinks.py

Ottieni il profilo dei backlink per un dominio.

```bash
python3 scripts/backlinks.py "example.com" --limit 20
```

### domain_overview.py

Ottieni metriche del dominio - traffico, parole chiave, ranking.

```bash
python3 scripts/domain_overview.py "example.com"
```

---

## Integrazione nel Workflow

### Utilizzo con OPC Skills

```bash
# Usa la skill twitter per trovare consigli SEO
python3 scripts/search_tweets.py "SEO tips 2026" --limit 20

# Usa la skill reddit per trovare discussioni
python3 scripts/search_posts.py "GEO optimization" --subreddit SEO --limit 10

# Usa WebSearch per la ricerca di parole chiave
# (Integrato nell'agente)
```

### Idee per l'Automazione

1. **Audit SEO settimanale** - Scansiona il sito con curl, controlla gli errori
2. **Monitoraggio dello schema** - Valida lo schema dopo i deploy con l'API Rich Results Test
3. **Tracciamento del ranking** - Monitora la visibilità AI con Otterly.ai o Profound
4. **Freschezza dei contenuti** - Segnala i contenuti obsoleti in base a dateModified
5. **Monitoraggio dei concorrenti** - Traccia i cambiamenti dei concorrenti con l'API DataForSEO

---

## Risorse

### Apprendimento

| Risorsa                   | URL                               | Tipo      |
| ------------------------- | --------------------------------- | --------- |
| **Guida SEO di Google**   | developers.google.com/search/docs | Ufficiale |
| **Moz Beginner's Guide**  | moz.com/beginners-guide-to-seo    | Tutorial  |
| **Backlinko**             | backlinko.com/hub/seo             | Avanzato  |
| **Search Engine Journal** | searchenginejournal.com           | Notizie   |

### Ricerca GEO

| Risorsa                                 | URL                                     | Tipo     |
| --------------------------------------- | --------------------------------------- | -------- |
| **Paper GEO di Princeton**              | arxiv.org/abs/2311.09735                | Ricerca  |
| **Guida GEO (SingleGrain)**             | singlegrain.com/geo                     | Guida    |
| **Ottimizzazione Ricerca AI (Semrush)** | semrush.com/blog/ai-search-optimization | Tutorial |

### Community

| Community       | Piattaforma | Focus             |
| --------------- | ----------- | ----------------- |
| **r/SEO**       | Reddit      | SEO Generale      |
| **r/bigseo**    | Reddit      | SEO Avanzata      |
| **r/TechSEO**   | Reddit      | SEO Tecnica       |
| **SEO Twitter** | Twitter     | Notizie, consigli |
