---
name: task-geo
description: Ottimizzazione per AI Overviews, ChatGPT, Perplexity e altre esperienze di ricerca AI (GEO).
---

# Ottimizzazione Ricerca AI / GEO (Febbraio 2026)

## Criteri di Analisi GEO (Aggiornati)

### 1. Punteggio Citabilità (25%)
- **Lunghezza ottimale paragrafo:** 134-167 parole.
- **Segnali forti:** Fatti/statistiche specifici, blocchi di risposta autocontenuti, risposta diretta nelle prime 40-60 parole.

### 2. Leggibilità Strutturale (20%)
- Gerarchia H1→H2→H3 pulita.
- Titoli basati su domande (query pattern).
- Paragrafi brevi (2-4 frasi).
- Tabelle per dati comparativi e liste puntate.

### 3. Contenuto Multi-Modale (15%)
- Presenza di testo + immagini rilevanti.
- Video integrati o linkati.
- Infografiche e grafici.
- Elementi interattivi (calcolatori, tool).

### 4. Autorità e Segnali Brand (20%)
- Firma dell'autore con credenziali.
- Data di pubblicazione e ultimo aggiornamento.
- Citazioni a fonti primarie (studi, documenti ufficiali).
- Presenza entità su Wikipedia, Wikidata, Reddit, YouTube.

### 5. Accessibilità Tecnica (20%)
- **Il rendering JavaScript NON è eseguito dai crawler AI.**
- Verifica Server-Side Rendering (SSR).
- Presenza del file `llms.txt` e configurazione corretta.
- Termini di licenza RSL 1.0.

---

## Rilevamento Crawler AI

Verifica nel `robots.txt` l'accesso per:
- `GPTBot` (OpenAI training)
- `OAI-SearchBot` (OpenAI search)
- `ChatGPT-User` (OpenAI browsing)
- `ClaudeBot` (Anthropic)
- `PerplexityBot` (Perplexity search)

---

## Standard llms.txt

Il file `/llms.txt` (nella root) fornisce istruzioni strutturate ai crawler AI.

**Formato atteso:**
```
# Titolo del sito
> Breve descrizione

## Sezioni principali
- [Titolo pagina](url): Descrizione
```

---

## Formato Report GEO

1. **GEO Readiness Score: XX/100**
2. **Breakdown per piattaforma** (Google AIO, ChatGPT, Perplexity).
3. **Stato Accesso Crawler AI**.
4. **Stato llms.txt** (presente/mancante).
5. **Analisi Menzioni Brand** (Wikipedia, Reddit, YouTube, LinkedIn).
6. **Citabilità a Livello di Paragrafo** (blocchi ottimali identificati).
7. **Verifica SSR** (dipendenza JavaScript).
8. **Top 5 Modifiche ad Alto Impatto**.
9. **Suggerimenti Formattazione Contenuti**.

