---
name: task-content
description:
  Analisi della qualità dei contenuti e dell'E-E-A-T con valutazione della predisposizione alle citazioni AI.
  Usare quando l'utente menziona "qualità dei contenuti", "E-E-A-T", "analisi dei contenuti",
  "controllo leggibilità", "contenuto scarso" o "audit dei contenuti".
---

# Analisi Qualità Contenuti (E-E-A-T & Esperienza, Competenza, Autorevolezza, Affidabilità)

Consultare `references/eeat-framework.md` per i criteri completi.

### Esperienza (Experience - segnali diretti)

- Ricerca originale, casi studio, risultati prima/dopo
- Aneddoti personali, documentazione del processo
- Dati unici, approfondimenti proprietari
- Foto/video derivanti da esperienza diretta

### Competenza (Expertise)

- Credenziali dell'autore, certificazioni, bio
- Background professionale pertinente all'argomento
- Profondità tecnica adeguata al pubblico
- Affermazioni accurate e ben documentate

### Autorevolezza (Authoritativeness)

- Citazioni esterne, backlink da fonti autorevoli
- Menzioni del brand, riconoscimento del settore
- Pubblicazioni in testate riconosciute
- Citato da altri esperti

### Affidabilità (Trustworthiness)

- Informazioni di contatto, indirizzo fisico
- Informativa sulla privacy, termini di servizio
- Testimonianze dei clienti, recensioni
- Timestamp delle date, correzioni trasparenti
- Sito sicuro (HTTPS)

## Metriche del Contenuto

### Analisi del Conteggio Parole

Confrontare con i minimi per tipologia di pagina:
| Tipo di Pagina | Minimo |
|----------------|--------|
| Homepage       | 500    |
| Pagina Servizio| 800    |
| Post del Blog  | 1.500  |
| Pagina Prodotto| 300+   |
| Pagina Locale  | 500-600|

> **Importante:** Questi sono **livelli minimi di copertura tematica**, non obiettivi. Google ha confermato che il conteggio delle parole NON è un fattore di ranking diretto. L'obiettivo è una copertura tematica completa: una pagina di 500 parole che risponde esaustivamente alla query supererà una pagina di 2.000 parole che non lo fa. Usare questi valori come linee guida per una profondità di copertura adeguata, non come requisiti rigidi.

### Leggibilità

- Flesch Reading Ease: target 60-70 per il pubblico generale

> **Nota:** Il Flesch Reading Ease è un utile indicatore per l'accessibilità dei contenuti ma NON è un fattore di ranking diretto di Google. John Mueller ha confermato che Google non utilizza punteggi di leggibilità di base per il ranking. Yoast ha deprioritizzato i punteggi Flesch nella v19.3. Usare l'analisi della leggibilità come indicatore di qualità del contenuto, non come una metrica SEO da ottimizzare direttamente.

- Livello scolastico: corrispondente al pubblico target
- Lunghezza frase: media 15-20 parole
- Lunghezza paragrafo: 2-4 frasi

### Ottimizzazione delle Parole Chiave

- Parola chiave primaria nel titolo, H1, prime 100 parole
- Densità naturale (1-3%)
- Presenza di varianti semantiche
- Nessun keyword stuffing

### Struttura del Contenuto

- Gerarchia logica dei titoli (H1 → H2 → H3)
- Sezioni scansionabili con titoli descrittivi
- Elenchi puntati/numerati dove appropriato
- Indice dei contenuti per i contenuti lunghi

### Multimedia

- Immagini pertinenti con testo alt corretto
- Video dove appropriato
- Infografiche per dati complessi
- Grafici/diagrammi per le statistiche

### Linking Interno

- 3-5 link interni pertinenti ogni 1000 parole
- Testo ancora (anchor text) descrittivo
- Link a contenuti correlati
- Nessuna pagina orfana

### Linking Esterno

- Citare fonti autorevoli
- Aprire in una nuova scheda per l'esperienza utente
- Numero ragionevole (non eccessivo)

## Valutazione Contenuti AI (aggiunta QRG Settembre 2025)

I valutatori di Google ora valutano formalmente se il contenuto appare generato dall'AI.

### Contenuto AI Accettabile

- Dimostra autentico E-E-A-T
- Fornisce un valore unico
- Presenta supervisione e revisione umana
- Contiene approfondimenti originali

### Segnali di Contenuto AI di Bassa Qualità

- Frasario generico, mancanza di specificità
- Nessun approfondimento originale
- Struttura ripetitiva tra le pagine
- Nessuna attribuzione dell'autore
- Inesattezze fattuali

> **Helpful Content System (Marzo 2024):** Il sistema Helpful Content è stato integrato nell'algoritmo di ranking principale di Google durante l'aggiornamento core di marzo 2024. Non opera più come classificatore autonomo. I segnali di utilità sono ora ponderati all'interno di ogni aggiornamento core: si applicano i medesimi principi (contenuti incentrati sull'utente, dimostrazione di E-E-A-T, soddisfazione dell'intento dell'utente), ma l'applicazione è continua anziché tramite aggiornamenti HCU separati.

## Predisposizione alle Citazioni AI (segnali GEO)

Ottimizzare per i motori di ricerca AI (ChatGPT, Perplexity, Google AI Overviews):

- Dichiarazioni chiare e citabili con statistiche/fatti
- Dati strutturati (specialmente per i punti dati)
- Forte gerarchia dei titoli (flusso H1→H2→H3)
- Formattazione con risposta immediata per le domande chiave
- Tabelle ed elenchi per i dati comparativi
- Chiara attribuzione e citazione delle fonti

### Visibilità nella Ricerca AI & GEO (2025-2026)

**Google AI Mode** è stato lanciato pubblicamente a maggio 2025 come scheda separata nella Ricerca Google, disponibile in oltre 180 paesi. A differenza delle AI Overviews (che appaiao sopra i risultati organici), l'AI Mode offre un'esperienza di ricerca completamente conversazionale con **zero link blu organici**, rendendo la citazione AI l'unico meccanismo di visibilità.

**Strategie chiave di ottimizzazione per la citazione AI:**

- **Risposte strutturate:** Formati chiari di domanda-risposta, modelli di definizione e istruzioni passo-passo che i sistemi AI possono estrarre e citare
- **Dati di prima parte:** Ricerche originali, statistiche, casi studio e dataset unici sono altamente citati dai sistemi AI
- **Schema markup:** Gli schema di Articoli, FAQ (per piattaforme AI non Google) e contenuti strutturati aiutano i sistemi AI ad analizzare e attribuire i contenuti
- **Autorità tematica:** I sistemi AI citano preferenzialmente fonti che dimostrano una profonda competenza: costruire cluster di contenuti, non pagine isolate
- **Chiarezza dell'entità:** Assicurarsi che il brand, gli autori e i concetti chiave siano chiaramente definiti con dati strutturati (schema Organization, Person)
- **Monitoraggio multi-piattaforma:** Monitorare la visibilità su Google AI Overviews, AI Mode, ChatGPT, Perplexity e Bing Copilot, non solo i ranking tradizionali. Trattare la citazione AI come un KPI autonomo insieme ai ranking organici e al traffico.

**Generative Engine Optimization (GEO):**
La GEO è la disciplina emergente dell'ottimizzazione dei contenuti specificamente per le risposte generate dall'AI. I segnali GEO chiave includono: citabilità (fatti estratti chiari e concisi), attribuzione (citazioni delle fonti all'interno del contenuto), struttura (gerarchia dei titoli ben organizzata) e freschezza (dati aggiornati regolarmente). Consultare la skill `seo-geo` per i workflow GEO dettagliati.

## Freschezza dei Contenuti

- Data di pubblicazione visibile
- Data di ultimo aggiornamento se il contenuto è stato revisionato
- Segnalare i contenuti più vecchi di 12 mesi senza aggiornamenti per argomenti che cambiano rapidamente

## Ottimizzazione Google Discover (2026)

- **Clickbait Detection:** Verifica titoli sensazionalistici o fuorvianti.
- **Content Depth:** Profondità e originalità del contenuto.
- **Local Relevance:** Segnali di rilevanza locale.

## Output

### Punteggio Qualità Contenuto: XX/100

| Fattore       | Peso | Punteggio | Segnali Chiave |
| ------------- | ---- | --------- | -------------- |
| Esperienza    | 20%  | XX/100    | ...            |
| Competenza    | 25%  | XX/100    | ...            |
| Autorevolezza | 25%  | XX/100    | ...            |
| Affidabilità  | 30%  | XX/100    | ...            |

### Predisposizione Citazioni AI: XX/100

### Problemi Rilevati

- Elenco criticità riscontrate.

### Raccomandazioni Prioritarie

- Suggerimenti specifici per migliorare l'E-E-A-T.
- Proposte di riformulazione per favorire le citazioni nei motori AI.
- Correzione di contenuti scarsi o duplicati.
