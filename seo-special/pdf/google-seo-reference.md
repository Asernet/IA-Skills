<!-- Aggiornato: 2026-02-07 -->

# Riferimento Rapido SEO di Google (Febbraio 2026)

Guida di riferimento concisa per i sotto-agenti. Riassume i concetti chiave della Ricerca Google, i requisiti e le migliori pratiche. Non è una riproduzione dell'intera documentazione di Google — vedere i Link alla Documentazione Ufficiale in fondo per i dettagli completi.

---

## Come Funziona la Ricerca Google

La Ricerca Google opera in tre fasi: **Scansione (Crawling)** (Googlebot scopre le pagine seguendo i link e leggendo le sitemap), **Indicizzazione (Indexing)** (Google elabora e memorizza il contenuto della pagina, i metadati e i segnali nel suo indice di ricerca), e **Pubblicazione (Serving)** (quando un utente effettua una ricerca, gli algoritmi di Google classificano le pagine indicizzate per pertinenza, qualità e usabilità per restituire i risultati più utili). Le pagine devono essere scansionabili e indicizzabili per apparire nei risultati di ricerca.

---

## Fondamenti della Ricerca Google (Google Search Essentials)

Precedentemente noti come "Webmaster Guidelines". Requisiti chiave:

### Requisiti Tecnici

- Le pagine devono essere accessibili a Googlebot (non bloccate da robots.txt o noindex)
- Le pagine devono restituire uno stato HTTP 200 per i contenuti indicizzabili
- Il contenuto deve essere in un formato che Google può elaborare (HTML preferito, contenuto renderizzato via JS supportato ma più lento)
- Le pagine devono essere servite tramite HTTPS

### Norme sullo Spam

- Nessun cloaking (mostrare contenuti diversi a Googlebot rispetto agli utenti)
- Nessuna doorway page (pagine create esclusivamente per posizionarsi per query specifiche)
- Nessun testo o link nascosto
- Nessun keyword stuffing
- Nessun link spam (acquisto di link, eccessivi scambi di link)
- Nessun contenuto copiato o generato automaticamente senza valore aggiunto
- Nessun redirect ingannevole
- Nessuna pagina di affiliazione con contenuti scarsi (thin affiliate pages)

### Migliori Pratiche Chiave

- Crea contenuti per gli utenti, non per i motori di ricerca
- Rendi il tuo sito facile da navigare con una gerarchia chiara
- Usa titoli e meta description descrittivi e univoci per ogni pagina
- Usa i tag di intestazione (H1-H6) per strutturare il contenuto in modo logico
- Ottimizza le immagini con testo alt e dimensioni di file appropriate
- Assicurati che il design sia responsive e mobile-friendly
- Migliora la velocità di caricamento della pagina (Core Web Vitals)
- Invia una sitemap XML a Google Search Console
- Usa i dati strutturati (JSON-LD) per aiutare Google a comprendere i contenuti

---

## Segnali di Qualità dei Contenuti

Google valuta la qualità dei contenuti attraverso il framework E-E-A-T:

- **Experience (Esperienza)**: Il creatore del contenuto ha un'esperienza di prima mano con l'argomento? (Foto originali, storie personali, uso dimostrato)
- **Expertise (Competenza)**: Il creatore ha conoscenze o credenziali pertinenti? (Background professionale, profondità tecnica, fonti accurate)
- **Authoritativeness (Autorevolezza)**: Il creatore o il sito sono riconosciuti come fonte di riferimento? (Citazioni di settore, menzioni del brand, riconoscimento di esperti)
- **Trustworthiness (Affidabilità)**: Il contenuto e il sito sono affidabili e trasparenti? (Info di contatto, sito sicuro, standard editoriali, affermazioni accurate)

> **Nota YMYL**: Gli argomenti "Your Money or Your Life" (salute, finanza, sicurezza, legale) sono soggetti ai più alti standard E-E-A-T. Contenuti YMYL imprecisi possono causare danni nel mondo reale, quindi Google applica soglie di qualità più rigorose.

> **Aggiornamento Dicembre 2025**: La valutazione E-E-A-T ora si estende a TUTTE le query competitive, non solo ai temi YMYL. Ogni pagina che compete per il ranking viene valutata su questi segnali.

---

## Core Web Vitals

Misurati al 75° percentile dei dati degli utenti reali (dati di campo).

| Metrica                             | Buono   | Necessita Miglioramento | Scarso  |
| ----------------------------------- | ------- | ----------------------- | ------- |
| **LCP** (Largest Contentful Paint)  | ≤ 2.5s  | 2.5s – 4.0s             | > 4.0s  |
| **INP** (Interaction to Next Paint) | ≤ 200ms | 200ms – 500ms           | > 500ms |
| **CLS** (Cumulative Layout Shift)   | ≤ 0.1   | 0.1 – 0.25              | > 0.25  |

**Fatti chiave:**

- L'INP ha sostituito il FID (First Input Delay) il 12 marzo 2024. Il FID è stato rimosso completamente da tutti gli strumenti Chrome (CrUX API, PageSpeed Insights, Lighthouse) il 9 settembre 2024. NON fare riferimento al FID.
- I Core Web Vitals sono un segnale di ranking confermato (da giugno 2021)
- I dati di campo (CrUX) sono preferiti ai dati di laboratorio (Lighthouse) per la valutazione
- L'obiettivo è superare tutte e tre le metriche con giudizio "Buono"

**Strumenti di misurazione:**

- Google PageSpeed Insights (dati di campo + laboratorio)
- Chrome User Experience Report (CrUX) — dati di campo
- Lighthouse (solo dati di laboratorio)
- Rapporto Core Web Vitals di Google Search Console

---

## Migliori Pratiche per i Dati Strutturati

- **JSON-LD è il formato preferito da Google** (rispetto a Microdata e RDFa)
- Posiziona JSON-LD nei tag `<script type="application/ld+json">` nell' `<head>` o nel `<body>`
- Includi sempre le proprietà `@context` e `@type`
- **Le proprietà obbligatorie** devono essere presenti per l'idoneità ai risultati avanzati (rich results)
- **Le proprietà raccomandate** migliorano la qualità dei rich results ma non sono obbligatorie
- Contrassegna solo il contenuto visibile sulla pagina
- Usa il Test dei Risultati Avanzati di Google per convalidare prima della pubblicazione
- Non contrassegnare contenuti fuorvianti o nascosti agli utenti
- Mantieni lo schema aggiornato — aggiornalo quando cambiano i contenuti della pagina

### Tipi Deprecati/Limitati (a Febbraio 2026)

- **HowTo**: Risultati avanzati rimossi (Settembre 2023)
- **FAQ**: Limitato ai siti di autorità governative e sanitarie (Agosto 2023)
- **SpecialAnnouncement**: Deprecato (31 luglio 2025)
- **CourseInfo, EstimatedSalary, LearningVideo**: Ritirati (Giugno 2025)
- **ClaimReview**: Ritirato (Giugno 2025)
- **VehicleListing**: Ritirato (Giugno 2025)

---

## Penalità Comuni e Come Evitarle

### Azioni Manuali

Notifiche in Google Search Console per violazioni. Cause comuni:

- **Link non naturali** (acquisto/vendita di link): Rifiuta i link dannosi (disavow), richiedi riconsiderazione
- **Contenuti scarsi (Thin content)**: Aggiungi un valore unico sostanziale alle pagine interessate
- **Cloaking/redirect ingannevoli**: Rimuovi la pubblicazione ingannevole, richiedi riconsiderazione
- **Spam generato dagli utenti**: Modera commenti/forum, aggiungi nofollow ai link degli utenti
- **Problemi con i dati strutturati**: Correggi il markup fuorviante o spam

### Declassamenti Algoritmici

Nessuna notifica manuale — rilevati tramite cali nel ranking. Cause comuni:

- **Helpful Content System**: Integrato nel core ranking di Google a marzo 2024 — non è più un sistema autonomo. I segnali di utilità sono ora valutati all'interno di ogni core update. Contenuti di basso valore, generati dall'AI o inutili su scala innescano ancora declassamenti tramite i core update.
- **Core Updates**: Rivalutazione generale della qualità su tutti i segnali
- **Spam Updates**: Rilevamento automatico di pattern di spam
- **Link Spam Updates**: Svalutazione di pattern di link manipolativi

### Passaggi per il Recupero

1. Identifica il problema (Search Console, analisi della timeline del ranking)
2. Risolvi la causa alla base (rimuovi lo spam, migliora i contenuti, pulisci i link)
3. Per le azioni manuali: invia una richiesta di riconsiderazione tramite Search Console
4. Per gli algoritmici: migliora la qualità, attendi la rivalutazione del prossimo core update
5. Monitora il recupero nei rapporti sulle prestazioni di Search Console

---

## Link alla Documentazione Ufficiale

- [Fondamenti della Ricerca Google](https://developers.google.com/search/docs/essentials)
- [Come Funziona la Ricerca Google](https://developers.google.com/search/docs/fundamentals/how-search-works)
- [Panoramica sui Dati Strutturati](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Test dei Risultati Avanzati](https://search.google.com/test/rich-results)
- [Rapporto Core Web Vitals](https://support.google.com/webmasters/answer/9205520)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Guida di Search Console](https://support.google.com/webmasters)
- [Rapporto sulle Azioni Manuali](https://support.google.com/webmasters/answer/9044175)
- [Dashboard dello Stato della Ricerca Google](https://status.search.google.com/)
- [Blog di Google Search Central](https://developers.google.com/search/blog)
- [Norme sullo Spam](https://developers.google.com/search/docs/essentials/spam-policies)
- [E-E-A-T e Linee Guida per i Valutatori di Qualità](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)

> **L'indicizzazione mobile-first** è completa al 100% dal 5 luglio 2024. Google ora scansiona e indicizza TUTTI i siti web esclusivamente con lo user-agent mobile Googlebot.
