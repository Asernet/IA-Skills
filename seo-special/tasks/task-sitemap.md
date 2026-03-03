---
name: task-sitemap
description: Analizza le sitemap XML esistenti o generane di nuove con template di settore. Valida il formato, gli URL e la struttura. Usare quando l'utente dice "sitemap", "genera sitemap", "problemi sitemap" o "sitemap XML".
---

# Analisi e Generazione Sitemap

## Modalità 1: Analisi Sitemap Esistente

### Controlli di Validazione

- **Formato XML valido**: Verifica sintassi e namespace XML.
- **Conteggio URL < 50.000 per file**: Limite del protocollo per singolo file.
- **Tutti gli URL restituiscono HTTP 200**: Nessun link rotto ammesso.
- **Date `<lastmod>` accurate**: Le date non devono essere tutte identiche.
- **Nessun tag deprecato**: `<priority>` e `<changefreq>` sono ignorati da Google.
- **Riferimento in robots.txt**: La sitemap deve essere segnalata nel file robots.txt.
- **Confronto pagine scansionate vs sitemap**: Segnalare le pagine mancanti.

### Segnali di Qualità

- **File indice della sitemap** se gli URL superano i 50.000.
- **Suddivisione per tipo di contenuto** (pagine, post, immagini, video).
- **Solo URL canonici** inclusi nella sitemap.
- **Nessun URL con noindex** incluso.
- **Nessun URL reindirizzato** (redirect).
- **Solo URL HTTPS** (niente HTTP).

### Problemi Comuni

| Problema                        | Gravità | Soluzione                                   |
| ------------------------------- | ------- | ------------------------------------------- |
| >50k URL in un singolo file     | Critica | Suddividere con un indice della sitemap     |
| URL non-200                     | Alta    | Rimuovere o correggere gli URL interrotti   |
| URL con noindex inclusi         | Alta    | Rimuovere dalla sitemap                     |
| URL reindirizzati inclusi       | Media   | Aggiornare agli URL finali                  |
| Tutte le date lastmod identiche | Bassa   | Usare le date di modifica reali             |
| Uso di priority/changefreq      | Info    | Possono essere rimossi (ignorati da Google) |

## Modalità 2: Generazione Nuova Sitemap

### Processo

1. Chiedere il tipo di attività (o rilevarlo automaticamente dal sito esistente).
2. Caricare il template di settore dalla directory `assets/`.
3. Pianificazione interattiva della struttura con l'utente.
4. Applicazione dei "quality gates":
   - ⚠️ **AVVISO** a 30+ pagine località (richiesto >60% di contenuto unico).
   - 🛑 **STOP** a 50+ pagine località (richiesta giustificazione esplicita).
5. Generare l'output XML valido.
6. Suddivisione a 50k URL con indice della sitemap se necessario.
7. Generare la documentazione `STRUCTURE.md`.

### Pagine Programmatiche Sicure (OK su larga scala)

✅ **Pagine di integrazione** (con documenti di configurazione reali).
✅ **Pagine di template/strumenti** (con contenuti scaricabili).
✅ **Pagine di glossario** (definizioni di oltre 200 parole).
✅ **Pagine prodotto** (specifiche uniche, recensioni).
✅ **Pagine profilo utente** (contenuti generati dagli utenti).

### Rischio Penalità (evitare su larga scala)

❌ Pagine località con solo il nome della città sostituito.
❌ "Miglior [strumento] per [settore]" senza valore specifico.
❌ "Alternativa a [competitor]" senza dati reali di confronto.
❌ Pagine generate dall'AI senza revisione umana e valore unico.

## Formato Sitemap

### Sitemap Standard

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/pagina</loc>
    <lastmod>2026-02-07</lastmod>
  </url>
</urlset>
```

### Indice della Sitemap (per >50k URL)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap>
    <loc>https://example.com/sitemap-pages.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://example.com/sitemap-posts.xml</loc>
    <lastmod>2026-02-07</lastmod>
  </sitemap>
</sitemapindex>
```

## Output

### Per l'Analisi

- `VALIDATION-REPORT.md`: Risultati dell'analisi.
- Elenco dei problemi con gravità.
- Raccomandazioni.

### Per la Generazione

- `sitemap.xml` (o file suddivisi con indice).
- `STRUCTURE.md`: Documentazione dell'architettura del sito.
- Riepilogo del conteggio URL e dell'organizzazione.
