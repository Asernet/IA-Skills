---
name: task-page
description: Analisi SEO approfondita di una singola pagina che copre elementi on-page, qualità dei contenuti, meta tag tecnici, schema, immagini e performance. Usare quando l'utente dice "analizza questa pagina", "controlla la SEO della pagina" o fornisce un singolo URL per la revisione.
---

# Analisi Singola Pagina

## Cosa Analizzare

### SEO On-Page

- Tag Title: 50-60 caratteri, include la parola chiave primaria, unico.
- Meta Description: 150-160 caratteri, persuasiva, include la parola chiave.
- H1: esattamente uno per pagina, pertinente all'intento della pagina, include la parola chiave.
- H2-H6: gerarchia logica (nessun livello saltato), descrittivi.
- URL: breve, descrittivo, con trattini, senza parametri inutili.
- Link interni: sufficienti, anchor text pertinente, nessuna pagina orfana.
- Link esterni: verso fonti autorevoli, in numero ragionevole.

### Qualità dei Contenuti

- Conteggio parole rispetto ai minimi per tipo di pagina (vedi `task-content.md`).
- Leggibilità: punteggio Flesch Reading Ease, livello scolastico.
- Densità delle parole chiave: naturale (1-3%), presenza di varianti semantiche.
- Segnali E-E-A-T: bio dell'autore, credenziali, indicatori di esperienza diretta.
- Freschezza del contenuto: data di pubblicazione, data dell'ultimo aggiornamento.

### Elementi Tecnici

- Tag Canonical: presente, autoreferenziale o puntato all'URL corretto.
- Meta Robots: index/follow, a meno che non sia intenzionalmente bloccato.
- Open Graph: og:title, og:description, og:image, og:url.
- Twitter Card: twitter:card, twitter:title, twitter:description.
- Hreflang: se multilingua, verificare la corretta implementazione.

### Schema Markup

- Rilevare tutti i tipi (preferito JSON-LD).
- Validare le proprietà obbligatorie.
- Identificare opportunità mancanti.
- MAI raccomandare HowTo (deprecato) o FAQ (limitato a siti governativi/sanitari).

### Immagini

- Testo Alt: presente, descrittivo, include parole chiave dove naturale.
- Dimensione file: segnalare >200KB (avviso), >500KB (critico).
- Formato: raccomandare WebP/AVIF rispetto a JPEG/PNG.
- Dimensioni: larghezza/altezza impostate per prevenire il CLS.
- Lazy loading: `loading="lazy"` sulle immagini sotto la piega (below-fold).

### Core Web Vitals (solo riferimento — non misurabili solo dal codice HTML)

- Segnalare potenziali problemi di LCP (immagini hero enormi, risorse che bloccano il rendering).
- Segnalare potenziali problemi di INP (JS pesante, mancanza di async/defer).
- Segnalare potenziali problemi di CLS (dimensioni immagini mancanti, contenuti iniettati).

## Output

### Page Score Card

```
Punteggio Complessivo: XX/100

SEO On-Page:      XX/100  ████████░░
Qualità Contenuti: XX/100  ██████████
Tecnico:          XX/100  ███████░░░
Schema:           XX/100  █████░░░░░
Immagini:         XX/100  ████████░░
```

### Problemi Rilevati

Organizzati per priorità: Critico → Alto → Medio → Basso

### Raccomandazioni

Miglioramenti specifici e applicabili con l'impatto atteso.

### Suggerimenti Schema

Codice JSON-LD pronto all'uso per le opportunità rilevate.
