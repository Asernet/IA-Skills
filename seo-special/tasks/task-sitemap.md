---
name: task-sitemap
description: Analisi e generazione di sitemap XML con quality gate per pagine località e limiti di protocollo.
---

# Analisi e Generazione Sitemap (Standard 2026)

## Modalità 1: Analisi Sitemap Esistente

### Controlli di Validazione
- **Formato XML:** Verifica sintassi e namespace.
- **Limite URL:** Massimo 50.000 URL per file (limite di protocollo).
- **Stato HTTP:** Tutti gli URL devono restituire stato 200.
- **Tag Deprecati:** `<priority>` e `<changefreq>` sono ignorati da Google; segnala se presenti (possono essere rimossi).
- **Accuratezza lastmod:** Verifica che le date non siano tutte identiche (segnale di scarsa qualità).
- **Inclusione in robots.txt:** Verifica riferimento esplicito.

### Segnali di Qualità
- Suddivisione per tipo di contenuto (pagine, post, immagini, video).
- Solo URL canonici e in HTTPS.
- Nessun URL con noindex o redirect incluso.

## Modalità 2: Generazione Nuova Sitemap

### Quality Gates (Fondamentali)
- ⚠️ **AVVISO** a 30+ pagine località: richiesto 60%+ di contenuto unico per pagina.
- 🛑 **STOP** a 50+ pagine località: richiesta giustificazione esplicita per evitare penalità "doorway".

### Pagine Sicure vs Rischio Penalità
- **Sicure ✅:** Glossari (200+ parole), Integrazioni, Prodotti con specifiche uniche.
- **Rischio ❌:** Pagine località con solo cambio nome città, comparazioni senza dati reali, contenuti AI senza revisione.

## Formato Output
- `VALIDATION-REPORT.md`: Risultati analisi con gravità (Critica, Alta, Media, Bassa).
- `sitemap.xml`: File generato (con indice se >50k URL).
- `STRUCTURE.md`: Documentazione dell'architettura del sito.
