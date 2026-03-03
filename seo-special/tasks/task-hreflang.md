---
name: task-hreflang
description: Audit, validazione e generazione hreflang e SEO internazionale. Rileva errori comuni, valida i codici lingua/regione e genera implementazioni hreflang corrette. Usare quando l'utente menziona "hreflang", "i18n SEO", "SEO internazionale", "multilingua", "multiregione" o "tag linguistici".
---

# Hreflang & SEO Internazionale

Valida le implementazioni hreflang esistenti o genera tag hreflang corretti per siti multilingua e multiregione. Supporta implementazioni HTML, intestazioni HTTP e sitemap XML.

## Controlli di Validazione

### 1. Tag Autoreferenziali

- Ogni pagina deve includere un tag hreflang che punti a se stessa
- L'URL autoreferenziale deve corrispondere esattamente all'URL canonico della pagina
- La mancanza di tag autoreferenziali induce Google a ignorare l'intero set hreflang

### 2. Tag di Ritorno (Return Tags)

- Se la pagina A punta alla pagina B con hreflang, la pagina B deve puntare a sua volta alla pagina A
- Ogni relazione hreflang deve essere bidirezionale (A→B e B→A)
- La mancanza di tag di ritorno invalida il segnale hreflang per entrambe le pagine
- Verificare che tutte le versioni linguistiche facciano riferimento l'una all'altra (mesh completa)

### 3. Tag x-default

- Obbligatorio: designa la pagina di fallback per lingue/regioni non corrispondenti
- In genere punta alla pagina di selezione della lingua o alla versione inglese
- Solo un x-default per set di varianti
- Deve avere anche tag di ritorno da tutte le altre versioni linguistiche

### 4. Validazione del Codice Lingua

- Deve utilizzare i codici a due lettere ISO 639-1 (es. `en`, `fr`, `de`, `ja`)
- Errori comuni:
  - `eng` invece di `en` (ISO 639-2, non valido per hreflang)
  - `jp` invece di `ja` (codice errato per il giapponese)
  - `zh` senza qualificatore di regione (ambiguo — usare `zh-Hans` o `zh-Hant`)

### 5. Validazione del Codice Regione

- Il qualificatore di regione opzionale utilizza ISO 3166-1 Alpha-2 (es. `en-US`, `en-GB`, `pt-BR`)
- Formato: `lingua-REGIONE` (lingua minuscola, regione maiuscola)
- Errori comuni:
  - `en-uk` invece di `en-GB` (UK non è un codice ISO 3166-1 valido)
  - `es-LA` (l'America Latina non è un paese — usare paesi specifici)
  - Regione senza prefisso della lingua

### 6. Allineamento con l'URL Canonico

- I tag hreflang devono apparire solo sugli URL canonici
- Se una pagina ha un `rel=canonical` che punta altrove, l'hreflang su quella pagina viene ignorato
- L'URL canonico e l'URL hreflang devono corrispondere esattamente (inclusi gli slash finali)
- Le pagine non canoniche non dovrebbero far parte di alcun set hreflang

### 7. Coerenza del Protocollo

- Tutti gli URL in un set hreflang devono utilizzare lo stesso protocollo (HTTPS o HTTP)
- Il mix di HTTP/HTTPS nei set hreflang causa errori di validazione
- Dopo la migrazione a HTTPS, aggiornare tutti i tag hreflang a HTTPS

### 8. Supporto Cross-Domain

- L'hreflang funziona su domini diversi (es. example.com e example.de)
- L'hreflang cross-domain richiede tag di ritorno su entrambi i domini
- Verificare che entrambi i domini siano verificati in Google Search Console
- Si raccomanda un'implementazione basata su sitemap per configurazioni cross-domain

## Errori Comuni

| Problema                                | Gravità | Soluzione                                                             |
| --------------------------------------- | ------- | --------------------------------------------------------------------- |
| Tag autoreferenziale mancante           | Critica | Aggiungere hreflang che punti all'URL della pagina stessa             |
| Tag di ritorno mancanti (A→B ma no B→A) | Critica | Aggiungere tag di ritorno corrispondenti su tutte le varianti         |
| x-default mancante                      | Alta    | Aggiungere x-default che punti alla pagina di fallback/selezione      |
| Codice lingua non valido (es. `eng`)    | Alta    | Usare codici a due lettere ISO 639-1                                  |
| Codice regione non valido (es. `en-uk`) | Alta    | Usare codici ISO 3166-1 Alpha-2                                       |
| Hreflang su URL non canonico            | Alta    | Spostare l'hreflang solo sull'URL canonico                            |
| Discrepanza HTTP/HTTPS negli URL        | Media   | Standardizzare tutti gli URL su HTTPS                                 |
| Incoerenza dello slash finale           | Media   | Far coincidere esattamente il formato dell'URL canonico               |
| Hreflang sia in HTML che in sitemap     | Bassa   | Scegliere un solo metodo — sitemap preferita per siti grandi          |
| Lingua senza regione quando necessaria  | Bassa   | Aggiungere il qualificatore di regione per contenuti geo-targetizzati |

## Metodi di Implementazione

### Metodo 1: Tag Link HTML

Ideale per: Siti con <50 varianti di lingua/regione per pagina.

```html
<link rel="alternate" hreflang="en-US" href="https://example.com/page" />
<link rel="alternate" hreflang="en-GB" href="https://example.co.uk/page" />
<link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/page" />
```

Inserire nella sezione `<head>`. Ogni pagina deve includere tutte le varianti, se stessa compresa.

### Metodo 2: Intestazioni HTTP

Ideale per: File non HTML (PDF, documenti).

```
Link: <https://example.com/page>; rel="alternate"; hreflang="en-US",
      <https://example.com/fr/page>; rel="alternate"; hreflang="fr",
      <https://example.com/page>; rel="alternate"; hreflang="x-default"
```

Impostare tramite configurazione del server o regole CDN.

### Metodo 3: Sitemap XML (Raccomandato per siti grandi)

Ideale per: Siti con molte varianti linguistiche, configurazioni cross-domain o più di 50 pagine.

Vedere la sezione Generazione Sitemap Hreflang qui sotto.

### Confronto tra i Metodi

| Metodo            | Ideale per                  | Pro                                                  | Contro                                                         |
| ----------------- | --------------------------- | ---------------------------------------------------- | -------------------------------------------------------------- |
| Tag link HTML     | Piccoli siti (<50 varianti) | Facile da implementare, visibile nel codice sorgente | Appesantisce l' `<head>`, difficile da mantenere su scala      |
| Intestazioni HTTP | File non HTML               | Funziona per PDF e immagini                          | Configurazione server complessa, non visibile in HTML          |
| Sitemap XML       | Grandi siti, cross-domain   | Scalabile, gestione centralizzata                    | Non visibile sulla pagina, richiede manutenzione della sitemap |

## Generazione Hreflang

### Processo

1. **Rilevamento lingue**: Scansionare il sito per indicatori linguistici (percorso URL, sottodominio, TLD, attributo lang HTML)
2. **Mappatura equivalenti**: Associare le pagine corrispondenti tra diverse lingue/regioni
3. **Validazione codici lingua**: Verificare tutti i codici rispetto a ISO 639-1 e ISO 3166-1
4. **Generazione tag**: Creare i tag hreflang per ogni pagina, includendo quella autoreferenziale
5. **Verifica tag di ritorno**: Confermare che tutte le relazioni siano bidirezionali
6. **Aggiunta x-default**: Impostare il fallback per ogni set di pagine
7. **Output**: Generare il codice di implementazione (HTML, intestazioni HTTP o sitemap XML)

## Generazione Sitemap Hreflang

### Sitemap con Hreflang

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://example.com/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
  <url>
    <loc>https://example.com/fr/page</loc>
    <xhtml:link rel="alternate" hreflang="en-US" href="https://example.com/page" />
    <xhtml:link rel="alternate" hreflang="fr" href="https://example.com/fr/page" />
    <xhtml:link rel="alternate" hreflang="de" href="https://example.de/page" />
    <xhtml:link rel="alternate" hreflang="x-default" href="https://example.com/page" />
  </url>
</urlset>
```

Regole chiave:

- Includere la dichiarazione del namespace `xmlns:xhtml`
- Ogni voce `<url>` deve includere TUTTE le varianti linguistiche (compresa se stessa)
- Ogni variante deve apparire come una voce `<url>` separata con il suo set completo
- Dividere a 50.000 URL per file sitemap

## Output

### Report di Validazione Hreflang

#### Riepilogo

- Totale pagine scansionate: XX
- Varianti linguistiche rilevate: XX
- Problemi riscontrati: XX (Critici: X, Alti: X, Medi: X, Bassi: X)

#### Risultati della Validazione

| Lingua | URL         | Autoref | Tag di Ritorno | x-default | Stato |
| ------ | ----------- | ------- | -------------- | --------- | ----- |
| en-US  | https://... | ✅      | ✅             | ✅        | ✅    |
| fr     | https://... | ❌      | ⚠️             | ✅        | ❌    |
| de     | https://... | ✅      | ❌             | ✅        | ❌    |

### Tag Hreflang Generati

- Tag `<link>` HTML (se scelto il metodo HTML)
- Valori intestazione HTTP (se scelto il metodo header)
- `hreflang-sitemap.xml` (se scelto il metodo sitemap)

### Raccomandazioni

- Implementazioni mancanti da aggiungere
- Codici errati da correggere
- Suggerimenti per la migrazione del metodo (es. HTML → sitemap per scalabilità)
