---
name: task-hreflang
description: Validazione tag linguistici (hreflang) per siti multilingua e multiregione.
---

# Analisi hreflang (SEO Internazionale)

## Workflow di Validazione

1. **Rilevamento Tag:** Identificazione dei tag `link rel="alternate" hreflang="X"`.
2. **Controllo Codici ISO:** Verifica correttezza codici lingua (ISO 639-1) e regione (ISO 3166-1 Alpha-2).
3. **Verifica Reciprocità:** Ogni pagina deve puntare a se stessa e le altre devono ricambiare il puntamento.
4. **Tag x-default:** Verifica presenza del tag per utenti senza corrispondenza linguistica specifica.
5. **Codici di Stato:** Gli URL nelle sitemap e nei tag devono restituire stato 200.

## Formato Report

- **Stato Conformità:** ✅/⚠️/❌
- **Errori Rilevati:** (Mancata reciprocità, codici errati, URL non 200).
- **Raccomandazioni:** Correzioni specifiche per il codice.
