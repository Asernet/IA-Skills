---
name: task-geo
description: Ottimizzazione dei contenuti per AI Overviews (ex SGE), ricerca web di ChatGPT, Perplexity e altre esperienze di ricerca basate sull'AI. Analisi della Generative Engine Optimization (GEO), inclusi segnali di menzione del brand, accessibilità per i crawler AI, conformità a llms.txt, punteggio di citabilità a livello di paragrafo e ottimizzazione specifica per piattaforma. Usare quando l'utente menziona "AI Overviews", "SGE", "GEO", "ricerca AI", "ottimizzazione LLM", "Perplexity", "citazioni AI", "ricerca ChatGPT" o "visibilità AI".
---

# Ottimizzazione Ricerca AI / GEO (Febbraio 2026)

## Criteri di Analisi GEO (Aggiornati)

## Statistiche Chiave

| Metrica                           | Valore                                         | Fonte           |
| --------------------------------- | ---------------------------------------------- | --------------- |
| Copertura AI Overviews            | 1,5 miliardi di utenti/mese in oltre 200 paesi | Google          |
| Copertura query AI Overviews      | 50%+ di tutte le query                         | Dati di settore |
| Crescita sessioni riferite da AI  | 527% (Gen-Mag 2025)                            | SparkToro       |
| Utenti attivi settimanali ChatGPT | 900 milioni                                    | OpenAI          |
| Query mensili Perplexity          | 500+ milioni                                   | Perplexity      |

## Insight Critico: Menzioni del Brand > Backlink

**Le menzioni del brand correlano 3 volte più fortemente con la visibilità AI rispetto ai backlink.**
(Studio Ahrefs Dicembre 2025 su 75.000 brand)

| Segnale                  | Correlazione con Citazioni AI |
| ------------------------ | ----------------------------- |
| Menzioni su YouTube      | ~0.737 (più forte)            |
| Menzioni su Reddit       | Alta                          |
| Presenza su Wikipedia    | Alta                          |
| Presenza su LinkedIn     | Moderata                      |
| Domain Rating (backlink) | ~0.266 (debole)               |

**Solo l'11% dei domini** viene citato sia da ChatGPT che da Google AI Overviews per la stessa query: l'ottimizzazione specifica per piattaforma è essenziale.

---

### 1. Punteggio Citabilità (25%)

**Lunghezza ottimale del paragrafo: 134-167 parole** per la citazione AI.
**Segnali forti:**

- Frasi chiare e citabili con fatti/statistiche specifici
- Blocchi di risposta autocontenuti (possono essere estratti senza contesto)
- Risposta diretta nelle prime 40-60 parole della sezione
- Affermazioni attribuite con fonti specifiche
- Definizioni che seguono i pattern "X è..." o "X si riferisce a..."
- Punti dati unici non presenti altrove

### 2. Leggibilità Strutturale (20%)

**Il 92% delle citazioni di AI Overview proviene da pagine nei primi 10 risultati**, ma il 47% proviene da pagine posizionate sotto la posizione 5 — dimostrando logiche di selezione differenti.

**Segnali forti:**

- Gerarchia dei titoli pulita H1→H2→H3
- Titoli basati su domande (corrispondono ai pattern delle query)
- Paragrafi brevi (2-4 frasi)
- Tabelle per dati comparativi
- Elenchi ordinati/non ordinati per contenuti passo-passo o multi-item
- Sezioni FAQ con formato Q&A chiaro

### 3. Contenuto Multi-Modale (15%)

I contenuti con elementi multi-modali vedono **tassi di selezione superiori del 156%**.

**Cosa controllare:**

- Testo + immagini pertinenti
- Contenuto video (integrato o linkato)
- Infografiche e grafici
- Elementi interattivi (calcolatori, strumenti)
- Dati strutturati a supporto dei media

### 4. Autorità e Segnali del Brand (20%)

**Segnali forti:**

- Firma dell'autore con credenziali
- Data di pubblicazione e data dell'ultimo aggiornamento
- Citazioni a fonti primarie (studi, documenti ufficiali, dati)
- Credenziali e affiliazioni dell'organizzazione
- Citazioni di esperti con attribuzione
- Presenza dell'entità su Wikipedia, Wikidata
- Menzioni su Reddit, YouTube, LinkedIn

### 5. Accessibilità Tecnica (20%)

**I crawler AI NON eseguono JavaScript** — il rendering lato server (SSR) è fondamentale.

**Cosa controllare:**

- Rendering lato server (SSR) vs contenuto solo client
- Accesso ai crawler AI nel file robots.txt
- Presenza e configurazione del file llms.txt
- Termini di licenza RSL 1.0

---

## Rilevamento Crawler AI

Controlla nel `robots.txt` questi crawler AI:

| Crawler       | Proprietario | Scopo                                   |
| ------------- | ------------ | --------------------------------------- |
| GPTBot        | OpenAI       | Ricerca web ChatGPT                     |
| OAI-SearchBot | OpenAI       | Funzionalità di ricerca OpenAI          |
| ChatGPT-User  | OpenAI       | Navigazione ChatGPT                     |
| ClaudeBot     | Anthropic    | Funzionalità web Claude                 |
| PerplexityBot | Perplexity   | Ricerca AI Perplexity                   |
| CCBot         | Common Crawl | Dati di addestramento (spesso bloccato) |
| anthropic-ai  | Anthropic    | Addestramento Claude                    |
| Bytespider    | ByteDance    | AI TikTok/Douyin                        |
| cohere-ai     | Cohere       | Modelli Cohere                          |

**Raccomandazione:** Consentire GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot per la visibilità nella ricerca AI. Bloccare CCBot e i crawler di addestramento se desiderato.

---

## Standard llms.txt

Lo standard emergente **llms.txt** fornisce ai crawler AI una guida strutturata ai contenuti.

**Percorso:** `/llms.txt` (root del dominio)

**Formato:**

```
# Titolo del sito
> Breve descrizione

## Sezioni principali
- [Titolo pagina](url): Descrizione
- [Un'altra pagina](url): Descrizione

## Opzionale: Fatti chiave
- Fatto 1
- Fatto 2
```

---

## RSL 1.0 (Really Simple Licensing)

Nuovo standard (Dicembre 2025) per termini di licenza AI leggibili dalle macchine.

**Sostenuto da:** Reddit, Yahoo, Medium, Quora, Cloudflare, Akamai, Creative Commons.

---

## Ottimizzazione Specifica per Piattaforma

| Piattaforma             | Fonti Principali di Citazione     | Focus Ottimizzazione                           |
| ----------------------- | --------------------------------- | ---------------------------------------------- |
| **Google AI Overviews** | Pagine nei primi 10 (92%)         | SEO tradizionale + ottimizzazione dei passaggi |
| **ChatGPT**             | Wikipedia (47,9%), Reddit (11,3%) | Presenza dell'entità, fonti autorevoli         |
| **Perplexity**          | Reddit (46,7%), Wikipedia         | Validazione della community, discussioni       |
| **Bing Copilot**        | Indice Bing, siti autorevoli      | SEO Bing, IndexNow                             |

---

## Formato Report GEO (Output)

Generare `GEO-ANALYSIS.md` con:

1. **Punteggio GEO Readiness: XX/100**
2. **Breakdown per piattaforma** (punteggi Google AIO, ChatGPT, Perplexity)
3. **Stato Accesso Crawler AI** (quali crawler sono consentiti/bloccati)
4. **Stato llms.txt** (presente, mancante, raccomandazioni)
5. **Analisi Menzioni Brand** (presenza su Wikipedia, Reddit, YouTube, LinkedIn)
6. **Citabilità a livello di paragrafo** (identificati blocchi ottimali di 134-167 parole)
7. **Verifica Server-Side Rendering** (analisi della dipendenza da JavaScript)
8. **Top 5 Modifiche ad Alto Impatto**
9. **Raccomandazioni Schema Markup** (per la scopribilità AI)
10. **Suggerimenti per la Riformulazione dei Contenuti** (passaggi specifici da riscrivere)

---

## Guadagni Rapidi (Quick Wins)

1. Aggiungere la definizione "Cos'è [argomento]?" nelle prime 60 parole
2. Creare blocchi di risposta autocontenuti di 134-167 parole
3. Aggiungere titoli H2/H3 basati su domande
4. Includere statistiche specifiche con fonti
5. Aggiungere date di pubblicazione/aggiornamento
6. Implementare lo schema Person per gli autori
7. Consentire i principali crawler AI nel file robots.txt

## Sforzo Medio

1. Creare il file `/llms.txt`
2. Aggiungere bio dell'autore con credenziali + link Wikipedia/LinkedIn
3. Garantire il rendering lato server per i contenuti chiave
4. Costruire la presenza dell'entità su Reddit, YouTube
5. Aggiungere tabelle di confronto con dati
6. Implementare sezioni FAQ (strutturate, non con schema per siti commerciali)

## Alto Impatto

1. Creare ricerche originali/sondaggi (citabilità unica)
2. Costruire la presenza su Wikipedia per il brand/persone chiave
3. Stabilire un canale YouTube con menzioni dei contenuti
4. Implementare un linking completo dell'entità (sameAs su tutte le piattaforme)
5. Sviluppare strumenti o calcolatori unici

---

## Visibilità nella Ricerca AI & GEO (2025-2026)

**Google AI Mode** lanciato pubblicamente a maggio 2025 come scheda separata nella Ricerca Google, disponibile in oltre 180 paesi. A differenza delle AI Overviews, l'AI Mode offre un'esperienza di ricerca completamente conversazionale con zero link blu organici.

## Freschezza dei Contenuti

- Data di pubblicazione visibile
- Data di ultimo aggiornamento se il contenuto è stato revisionato
- Segnalare i contenuti più vecchi di 12 mesi senza aggiornamenti per argomenti che cambiano rapidamente
