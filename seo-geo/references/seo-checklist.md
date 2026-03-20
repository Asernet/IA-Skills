# Checklist per l'Audit SEO/GEO

Checklist completa per l'audit e l'ottimizzazione dei siti web sia per la SEO tradizionale che per la GEO (visibilità nella ricerca AI).

## Livelli di Priorità

| Livello | Significato  | Azione                                                                         |
| ------- | ------------ | ------------------------------------------------------------------------------ |
| **P0**  | Critico      | Da correggere immediatamente - blocca l'indicizzazione o causa grossi problemi |
| **P1**  | Importante   | Da correggere presto - impatto significativo sul ranking                       |
| **P2**  | Raccomandato | Utile da avere - migliora la visibilità e l'esperienza utente                  |

---

## SEO Tecnica

### P0 - Critico

- [ ] **P0** Il file `robots.txt` permette la scansione delle pagine importanti
- [ ] **P0** Il sito è accessibile (nessun errore 5xx)
- [ ] **P0** HTTPS abilitato (certificato SSL valido)
- [ ] **P0** Design responsive per dispositivi mobili
- [ ] **P0** Nessuna pagina critica bloccata dal tag `noindex`
- [ ] **P0** Il sito è indicizzato su Google (verifica: `site:dominio.it`)

### P1 - Importante

- [ ] **P1** Il file `robots.txt` permette l'accesso ai bot AI (GPTBot, PerplexityBot, ClaudeBot)
- [ ] **P1** La sitemap XML esiste ed è stata inviata
- [ ] **P1** Il sito è indicizzato su Bing (per la visibilità di Copilot)
- [ ] **P1** Tag Canonical implementati correttamente
- [ ] **P1** Nessun problema di contenuti duplicati
- [ ] **P1** Tempo di caricamento della pagina < 3 secondi
- [ ] **P1** LCP (Largest Contentful Paint) < 2.5s

### P2 - Raccomandato

- [ ] **P2** FID (First Input Delay) < 100ms
- [ ] **P2** CLS (Cumulative Layout Shift) < 0.1
- [ ] **P2** Immagini ottimizzate (formato WebP, lazy loading)
- [ ] **P2** CSS/JS minimizzati
- [ ] **P2** Compressione GZIP/Brotli abilitata
- [ ] **P2** CDN configurata
- [ ] **P2** Test di ottimizzazione mobile superato
- [ ] **P2** Nessun avviso di contenuto misto (mixed content)
- [ ] **P2** Header di sicurezza configurati

---

## SEO On-Page

### P0 - Critico

- [ ] **P0** Esiste un tag `<title>` unico (50-60 caratteri)
- [ ] **P0** Il titolo contiene la parola chiave primaria
- [ ] **P0** Esiste una `<meta descrizione>` unica (150-160 caratteri)
- [ ] **P0** Un singolo tag H1 per pagina
- [ ] **P0** L'H1 contiene la parola chiave primaria

### P1 - Importante

- [ ] **P1** La descrizione è accattivante e include la parola chiave
- [ ] **P1** `<meta name="robots">` impostato correttamente
- [ ] **P1** Gerarchia dei titoli logica (H1 > H2 > H3)
- [ ] **P1** Tutte le immagini hanno l'attributo `alt`
- [ ] **P1** Link interni a contenuti correlati
- [ ] **P1** Nessun link rotto (errori 404)
- [ ] **P1** L'anchor text è descrittivo

### P2 - Raccomandato

- [ ] **P2** `og:title` impostato
- [ ] **P2** `og:description` impostato
- [ ] **P2** `og:image` impostato (raccomandato 1200x630px)
- [ ] **P2** `og:url` impostato (URL canonico)
- [ ] **P2** `og:type` impostato (website/article)
- [ ] **P2** `twitter:card` impostato (summary_large_image)
- [ ] **P2** `twitter:title` impostato
- [ ] **P2** `twitter:description` impostato
- [ ] **P2** `twitter:image` impostato
- [ ] **P2** I paragrafi sono brevi (2-3 frasi)
- [ ] **P2** Elenchi puntati usati per le liste
- [ ] **P2** Tabelle usate per i confronti
- [ ] **P2** Il testo Alt include parole chiave dove naturale
- [ ] **P2** I nomi dei file immagine sono descrittivi
- [ ] **P2** I link esterni hanno `rel="noopener noreferrer"`

---

## Markup Schema (Dati Strutturati)

### P1 - Importante

- [ ] **P1** Schema Organization sulla homepage
- [ ] **P1** Schema WebPage su tutte le pagine
- [ ] **P1** Schema Article sui post del blog
- [ ] **P1** Lo schema supera il Test dei Risultati Multimediali di Google
- [ ] **P1** Nessun errore nella sezione "Miglioramenti" della Search Console

### P2 - Raccomandato - Potenziamento GEO

- [ ] **P2** Schema FAQPage sulle sezioni FAQ (+40% visibilità AI)
- [ ] **P2** Schema BreadcrumbList per la navigazione
- [ ] **P2** SpeakableSpecification per la ricerca vocale
- [ ] **P2** datePublished e dateModified inclusi
- [ ] **P2** Informazioni sull'autore con credenziali
- [ ] **P2** Informazioni sull'editore con logo
- [ ] **P2** Lo schema supera il Validatore di Schema.org

---

## Ottimizzazione GEO (Ricerca AI)

### P1 - Importante - Metodi GEO di Princeton

- [ ] **P1** Il contenuto include citazioni autorevoli (+40%)
- [ ] **P1** Statistiche e punti dati inclusi (+37%)
- [ ] **P1** Citazioni di esperti con attribuzione (+30%)
- [ ] **P1** NO keyword stuffing (causa una penalizzazione del -10%)

### P2 - Raccomandato - Potenziamento GEO

- [ ] **P2** Tono autorevole e sicuro (+25%)
- [ ] **P2** Il contenuto è accessibile/facile da capire (+20%)
- [ ] **P2** Terminologia tecnica appropriata (+18%)
- [ ] **P2** Vocabolario diversificato in tutto il testo (+15%)
- [ ] **P2** Alta fluenza e leggibilità (+15-30%)

### Struttura del Contenuto per l'AI

- [ ] Formato "Answer-first" (risposta diretta in alto)
- [ ] Paragrafi chiari ed estraibili
- [ ] Formato FAQ per le domande comuni
- [ ] Tabelle per dati comparativi
- [ ] Elenchi per processi passo-passo

### Accesso dei Bot AI

- [ ] GPTBot consentito nel robots.txt
- [ ] PerplexityBot consentito nel robots.txt
- [ ] ClaudeBot consentito nel robots.txt
- [ ] Anthropic-ai consentito nel robots.txt
- [ ] Bingbot consentito nel robots.txt

---

## SEO Off-Page

### Backlink

- [ ] Backlink di qualità da siti pertinenti
- [ ] Domini referenti diversificati
- [ ] Nessun backlink tossico o di spam
- [ ] Menzioni del brand (anche senza link)

### Segnali E-E-A-T

- [ ] Bio degli autori con credenziali
- [ ] Pagina "Chi siamo" con informazioni sull'azienda
- [ ] Informazioni di contatto visibili
- [ ] Informativa sulla privacy e termini di servizio
- [ ] Badge di fiducia/certificazioni se applicabili
- [ ] Recensioni/testimonianze dei clienti

### Presenza Sociale

- [ ] Profili social media attivi
- [ ] Link ai profili social sul sito web
- [ ] Pulsanti di condivisione social sui contenuti
- [ ] Branding coerente su tutte le piattaforme

---

## Strategia dei Contenuti

### Audit dei Contenuti

- [ ] Tutte le pagine hanno contenuti unici e di valore
- [ ] Nessun contenuto povero (thin content < 300 parole per le pagine principali)
- [ ] Il contenuto corrisponde all'intento di ricerca
- [ ] Il contenuto è aggiornato (entro 30 giorni per notizie/tecnologia)
- [ ] Il contenuto fornisce un valore unico rispetto ai concorrenti

### Strategia delle Parole Chiave

- [ ] Parola chiave primaria identificata per ogni pagina
- [ ] Parole chiave secondarie mappate
- [ ] Parole chiave a coda lunga (long-tail) targetizzate
- [ ] Nessuna cannibalizzazione delle parole chiave
- [ ] Le parole chiave corrispondono all'intento dell'utente

---

## Monitoraggio e Analitica

### Configurazione

- [ ] Google Analytics installato
- [ ] Google Search Console collegata
- [ ] Bing Webmaster Tools collegato
- [ ] Sitemap inviata a entrambi

### Controlli Regolari

- [ ] Settimanale: Controlla gli errori in Search Console
- [ ] Settimanale: Revisiona i Core Web Vitals
- [ ] Mensile: Analizza i trend del traffico organico
- [ ] Mensile: Revisiona le pagine con le migliori performance
- [ ] Trimestrale: Audit SEO completo

---

## Comandi per Audit Rapido

```bash
# Controlla i meta tag
curl -sL "https://example.com" | grep -E "<title>|<meta"

# Controlla il robots.txt
curl -s "https://example.com/robots.txt"

# Controlla la sitemap
curl -s "https://example.com/sitemap.xml" | head -30

# Controlla la velocità della pagina (usando l'API PageSpeed Insights)
# Richiede la chiave API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://example.com&strategy=mobile"

# Controlla se è indicizzato su Google
# Controllo manuale: https://www.google.com/search?q=site:example.com

# Valida lo schema
# Apri: https://search.google.com/test/rich-results?url=https://example.com
```

---

## Matrice delle Priorità

| Priorità    | Task                             | Impatto                     |
| ----------- | -------------------------------- | --------------------------- |
| **Critica** | Correggi gli errori di scansione | Blocca l'indicizzazione     |
| **Critica** | Abilita HTTPS                    | Fiducia + posizionamento    |
| **Alta**    | Core Web Vitals                  | UX + posizionamento         |
| **Alta**    | Ottimizzazione mobile            | 60%+ del traffico           |
| **Alta**    | Schema FAQPage                   | +40% visibilità AI          |
| **Media**   | Meta descrizioni                 | Miglioramento del CTR       |
| **Media**   | Link interni                     | Distribuzione dell'autorità |
| **Bassa**   | Meta tag social                  | Aspetto delle condivisioni  |
