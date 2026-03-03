---
name: task-schema
description: Rileva, valida e genera dati strutturati Schema.org. Formato JSON-LD preferito. Usare quando l'utente menziona "schema", "dati strutturati", "risultati multimediali", "JSON-LD" o "markup".
---

# Analisi e Generazione Schema Markup

## Rilevamento

1. Scansionare il codice sorgente della pagina per JSON-LD `<script type="application/ld+json">`.
2. Controllare la presenza di Microdata (`itemscope`, `itemprop`).
3. Controllare la presenza di RDFa (`typeof`, `property`).
4. Raccomandare sempre JSON-LD come formato primario (preferenza dichiarata da Google).

## Validazione

- Verificare le proprietà obbligatorie per ogni tipo di schema.
- Convalidare rispetto ai tipi di risultati multimediali supportati da Google.
- Verificare errori comuni:
  - `@context` mancante.
  - `@type` non valido.
  - Tipi di dati errati.
  - Testo segnaposto (placeholder).
  - URL relativi (devono essere assoluti).
  - Formati di data non validi.
- Segnalare i tipi deprecati (vedi sotto).

## Stato dei Tipi di Schema (aggiornato a Febbraio 2026)

Consultare `references/schema-types.md` per l'elenco completo. Regole chiave:

### ATTIVI — raccomandati liberamente:

Organization, LocalBusiness, SoftwareApplication, WebApplication, Product (con markup Certification da aprile 2025), ProductGroup, Offer, Service, Article, BlogPosting, NewsArticle, Review, AggregateRating, BreadcrumbList, WebSite, WebPage, Person, ProfilePage, ContactPage, VideoObject, ImageObject, Event, JobPosting, Course, DiscussionForumPosting.

### VIDEO E SPECIALIZZATI — raccomandati liberamente:

BroadcastEvent, Clip, SeekToAction, SoftwareSourceCode.

Vedere `schema/templates.json` per i template JSON-LD pronti all'uso per questi tipi.

> **Rendering JSON-LD e JavaScript:** Secondo la guida JS SEO di Google di dicembre 2025, i dati strutturati iniettati tramite JavaScript potrebbero subire ritardi nell'elaborazione. Per markup sensibili al tempo (specialmente Product, Offer), includere il JSON-LD nell'HTML iniziale renderizzato dal server.

### LIMITATI — solo per siti specifici:

- **FAQ**: SOLO per siti governativi e autorità sanitarie (limitato da agosto 2023).

### DEPRECATI — non raccomandare mai:

- **HowTo**: Risultati multimediali rimossi a settembre 2023.
- **SpecialAnnouncement**: Deprecato dal 31 luglio 2025.
- **CourseInfo, EstimatedSalary, LearningVideo**: Ritirati a giugno 2025.
- **ClaimReview**: Rimosso dai risultati multimediali a giugno 2025.
- **VehicleListing**: Rimosso dai risultati multimediali a giugno 2025.
- **Practice Problem**: Rimosso dai risultati multimediali a fine 2025.
- **Dataset**: Rimosso dai risultati multimediali a fine 2025.
- **Book Actions**: Deprecazione revocata — ancora funzionale a febbraio 2026 (nota storica).

## Generazione

Quando si genera uno schema per una pagina:

1. Identificare il tipo di pagina dall'analisi del contenuto.
2. Selezionare i tipi di schema appropriati.
3. Generare JSON-LD valido con tutte le proprietà obbligatorie e raccomandate.
4. Includere solo dati veritieri e verificabili — usare segnaposto chiaramente contrassegnati per l'utente.
5. Convalidare l'output prima della presentazione.

## Template Schema Comuni

### Organization (Organizzazione)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Nome Azienda]",
  "url": "[URL Sito Web]",
  "logo": "[URL Logo]",
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "[Telefono]",
    "contactType": "customer service"
  },
  "sameAs": ["[URL Facebook]", "[URL LinkedIn]", "[URL Twitter]"]
}
```

### LocalBusiness (Attività Locale)

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Nome Attività]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Via/Piazza]",
    "addressLocality": "[Città]",
    "addressRegion": "[Provincia]",
    "postalCode": "[CAP]",
    "addressCountry": "IT"
  },
  "telephone": "[Telefono]",
  "openingHours": "Mo-Fr 09:00-17:00",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "[Lat]",
    "longitude": "[Long]"
  }
}
```

### Article/BlogPosting (Articolo/Post del Blog)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Titolo]",
  "author": {
    "@type": "Person",
    "name": "[Nome Autore]"
  },
  "datePublished": "[AAAA-MM-GG]",
  "dateModified": "[AAAA-MM-GG]",
  "image": "[URL Immagine]",
  "publisher": {
    "@type": "Organization",
    "name": "[Editore]",
    "logo": {
      "@type": "ImageObject",
      "url": "[URL Logo]"
    }
  }
}
```

## Output

- `SCHEMA-REPORT.md` — risultati del rilevamento e della validazione.
- `generated-schema.json` — snippet JSON-LD pronti all'uso.

### Risultati della Validazione

| Schema | Tipo | Stato    | Problemi |
| ------ | ---- | -------- | -------- |
| ...    | ...  | ✅/⚠️/❌ | ...      |

### Raccomandazioni

- Opportunità di schema mancanti.
- Correzioni di validazione necessarie.
- Codice generato per l'implementazione.
