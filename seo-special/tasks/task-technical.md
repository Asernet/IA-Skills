---
name: task-technical
description: Audit SEO tecnico in 8 categorie: scansione, indicizzabilità, sicurezza, struttura URL, mobile, Core Web Vitals, dati strutturati e rendering JavaScript. Usare quando l'utente menziona "SEO tecnica", "problemi di scansione", "robots.txt", "Core Web Vitals", "velocità del sito" o "header di sicurezza".
---

# Audit SEO Tecnico

## Categorie di Analisi

### 1. Scansione (Crawlability)

- **robots.txt**: esistente, valido, non blocca risorse importanti.
- **Sitemap XML**: esistente, riferita nel robots.txt, formato valido.
- **Tag Noindex**: intenzionali vs accidentali.
- **Profondità di scansione**: pagine importanti entro 3 clic dalla homepage.
- **Rendering JavaScript**: verificare se il contenuto critico richiede l'esecuzione di JS.
- **Budget di scansione**: per siti grandi (>10k pagine), l'efficienza è fondamentale.

#### Gestione dei Crawler AI

A partire dal 2025-2026, le società di AI scansionano attivamente il web per addestrare modelli e alimentare la ricerca AI. Gestire questi crawler tramite il robots.txt è una considerazione fondamentale della SEO tecnica.

**Crawler AI noti:**

| Crawler         | Società      | Token robots.txt  | Scopo                                 |
| --------------- | ------------ | ----------------- | ------------------------------------- |
| GPTBot          | OpenAI       | `GPTBot`          | Addestramento modelli                 |
| ChatGPT-User    | OpenAI       | `ChatGPT-User`    | Navigazione in tempo reale            |
| ClaudeBot       | Anthropic    | `ClaudeBot`       | Addestramento modelli                 |
| PerplexityBot   | Perplexity   | `PerplexityBot`   | Indice di ricerca + addestramento     |
| Bytespider      | ByteDance    | `Bytespider`      | Addestramento modelli                 |
| Google-Extended | Google       | `Google-Extended` | Addestramento Gemini (NON la ricerca) |
| CCBot           | Common Crawl | `CCBot`           | Dataset aperto                        |

**Distinzioni chiave:**

- Bloccare `Google-Extended` impedisce l'uso dei dati per l'addestramento di Gemini ma NON influisce sull'indicizzazione della Ricerca Google o sulle AI Overviews (che usano `Googlebot`).
- Bloccare `GPTBot` impedisce l'addestramento di OpenAI ma NON impedisce a ChatGPT di citare i tuoi contenuti tramite la navigazione (`ChatGPT-User`).
- Circa il 3-5% dei siti web ora utilizza regole robots.txt specifiche per l'AI.

**Esempio — blocco selettivo dei crawler AI:**

```
# Consenti l'indicizzazione per la ricerca, blocca i crawler di addestramento AI
User-agent: GPTBot
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: Bytespider
Disallow: /

# Consenti tutti gli altri crawler (incluso Googlebot per la ricerca)
User-agent: *
Allow: /
```

**Raccomandazione:** valutare la strategia di visibilità AI prima di bloccare. Essere citati dai sistemi di AI aumenta la consapevolezza del brand e il traffico di riferimento. Fare riferimento alla skill `seo-geo` per l'ottimizzazione completa della visibilità AI.

### 2. Indicizzabilità (Indexability)

- **Tag Canonical**: autoreferenziali, nessun conflitto con noindex.
- **Contenuti duplicati**: quasi duplicati, URL con parametri, www vs non-www.
- **Contenuti scarsi (Thin content)**: pagine al di sotto dei conteggi minimi di parole per tipo.
- **Paginazione**: pattern rel=next/prev o caricamento infinito (load-more).
- **Hreflang**: corretto per siti multilingua/multiregione.
- **Index bloat**: pagine non necessarie che consumano il budget di scansione.

### 3. Sicurezza

- **HTTPS**: applicato, certificato SSL valido, nessun contenuto misto.
- **Header di sicurezza**:
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Frame-Options
  - X-Content-Type-Options
  - Referrer-Policy
- **Preload HSTS**: verifica dell'inclusione nella lista di preload per siti ad alta sicurezza.

### 4. Struttura degli URL

- **URL puliti**: descrittivi, con trattini, senza parametri di query per il contenuto.
- **Gerarchia**: struttura delle cartelle logica che riflette l'architettura del sito.
- **Reindirizzamenti**: nessuna catena (max 1 salto), 301 per spostamenti permanenti.
- **Lunghezza URL**: segnalare se superiore a 100 caratteri.
- **Slash finali**: utilizzo coerente.

### 5. Ottimizzazione Mobile

- **Responsive design**: meta tag viewport, CSS responsive.
- **Target tattili**: minimo 48x48px con spaziatura di 8px.
- **Dimensione font**: base minima 16px.
- **Nessuno scorrimento orizzontale**.
- **Indicizzazione Mobile-first**: Google indicizza la versione mobile. **L'indicizzazione mobile-first è completa al 100% dal 5 luglio 2024.** Google ora scansiona e indicizza TUTTI i siti web esclusivamente con lo user-agent mobile Googlebot.

### 6. Core Web Vitals

- **LCP** (Largest Contentful Paint): target < 2,5s.
- **INP** (Interaction to Next Paint): target < 200ms.
  - L'INP ha sostituito il FID il 12 marzo 2024. Il FID è stato rimosso da tutti gli strumenti Chrome il 9 settembre 2024. NON fare riferimento al FID.
- **CLS** (Cumulative Layout Shift): target < 0,1.
- La valutazione utilizza il 75° percentile dei dati degli utenti reali.

### 7. Dati Strutturati

- **Rilevamento**: JSON-LD (preferito), Microdata, RDFa.
- **Validazione** rispetto ai tipi supportati da Google.
- Vedere la skill `seo-schema` per l'analisi completa.

### 8. Rendering JavaScript

- Verificare se il contenuto è visibile nell'HTML iniziale rispetto a quando richiede JS.
- Identificare il rendering lato client (CSR) rispetto al rendering lato server (SSR).
- Segnalare framework SPA (React, Vue, Angular) che potrebbero causare problemi di indicizzazione.
- Verificare la configurazione del rendering dinamico, se applicabile.

#### SEO JavaScript — Guida all'indicizzazione e ai Canonical (Dicembre 2025)

Google ha aggiornato la documentazione SEO JavaScript a Dicembre 2025 con chiarimenti critici:

1. **Conflitti Canonical**: se un tag canonical nell'HTML crudo differisce da uno iniettato tramite JavaScript, Google può utilizzare ENTRAMBI. Assicurarsi che i tag canonical siano identici tra l'HTML renderizzato dal server e l'output renderizzato da JS.
2. **noindex con JavaScript**: se l'HTML crudo contiene `<meta name="robots" content="noindex">` ma JavaScript lo rimuove, Google POTREBBE comunque onorare il noindex dell'HTML crudo. Inviare le direttive robots corrette nella risposta HTML iniziale.
3. **Codici di stato non-200**: Google NON esegue il rendering JavaScript su pagine che restituiscono codici di stato HTTP diversi da 200. Qualsiasi contenuto o meta tag iniettato via JS su pagine di errore sarà invisibile a Googlebot.
4. **Dati strutturati in JavaScript**: Product, Article e altri dati strutturati iniettati via JS potrebbero subire ritardi nell'elaborazione. Per i dati strutturati sensibili al tempo (specialmente il markup Product per l'e-commerce), includerli nell'HTML iniziale renderizzato dal server.

**Best practice**: servire gli elementi SEO critici (canonical, meta robots, dati strutturati, title, meta description) nell'HTML iniziale renderizzato dal server invece di affidarsi all'iniezione tramite JavaScript.

### 9. Protocollo IndexNow

- Verificare se il sito supporta IndexNow per Bing, Yandex, Naver.
- Supportato da motori di ricerca diversi da Google.
- Raccomandare l'implementazione per un'indicizzazione più rapida su motori non-Google.

## Output

### Punteggio Tecnico: XX/100

### Suddivisione per Categoria

| Categoria        | Stato    | Punteggio |
| ---------------- | -------- | --------- |
| Scansione        | ✅/⚠️/❌ | XX/100    |
| Indicizzabilità  | ✅/⚠️/❌ | XX/100    |
| Sicurezza        | ✅/⚠️/❌ | XX/100    |
| Struttura URL    | ✅/⚠️/❌ | XX/100    |
| Mobile           | ✅/⚠️/❌ | XX/100    |
| Core Web Vitals  | ✅/⚠️/❌ | XX/100    |
| Dati Strutturati | ✅/⚠️/❌ | XX/100    |
| Rendering JS     | ✅/⚠️/❌ | XX/100    |

### Problemi Critici (risolvere immediatamente)

### Priorità Alta (entro 1 settimana)

### Priorità Media (entro 1 mese)

### Priorità Bassa (backlog)
