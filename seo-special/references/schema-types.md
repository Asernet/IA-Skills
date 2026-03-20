# Tipi Schema.org — Stato e Raccomandazioni (Febbraio 2026)

**Versione Schema.org:** 29.4 (8 dicembre 2025)

## Formato Preferito

Usare sempre **JSON-LD** (`<script type="application/ld+json">`).
La documentazione di Google raccomanda esplicitamente JSON-LD rispetto a Microdata e RDFa.

**Nota sulla AI Search:** I contenuti con uno schema corretto hanno una probabilità ~2,5 volte superiore di apparire nelle risposte generate dall'AI (confermato da Google e Microsoft, marzo 2025).

---

## Attivi — Raccomandati liberamente

| Tipo                   | Caso d'Uso                   | Proprietà Chiave                                                    |
| ---------------------- | ---------------------------- | ------------------------------------------------------------------- |
| Organization           | Informazioni aziendali       | name, url, logo, contactPoint, sameAs                               |
| LocalBusiness          | Attività fisiche             | name, address, telephone, openingHours, geo, priceRange             |
| SoftwareApplication    | App desktop/mobile           | name, operatingSystem, applicationCategory, offers, aggregateRating |
| WebApplication         | SaaS basati su browser       | name, applicationCategory, offers, browserRequirements, featureList |
| Product                | Prodotti fisici/digitali     | name, image, description, sku, brand, offers, review                |
| Offer                  | Prezzi                       | price, priceCurrency, availability, url, validFrom                  |
| Service                | Attività di servizi          | name, provider, areaServed, description, offers                     |
| Article                | Post del blog, news          | headline, author, datePublished, dateModified, image, publisher     |
| BlogPosting            | Contenuti del blog           | Uguale ad Article + contesto specifico del blog                     |
| NewsArticle            | Contenuti di news            | Uguale ad Article + contesto specifico delle news                   |
| Review                 | Recensioni singole           | reviewRating, author, itemReviewed, reviewBody                      |
| AggregateRating        | Riepiloghi delle valutazioni | ratingValue, reviewCount, bestRating, worstRating                   |
| BreadcrumbList         | Navigazione                  | itemListElement con position, name, item                            |
| WebSite                | Livello sito                 | name, url, potentialAction (SearchAction per la ricerca sitelinks)  |
| WebPage                | Livello pagina               | name, description, datePublished, dateModified                      |
| Person                 | Autore/team                  | name, jobTitle, url, sameAs, image, worksFor                        |
| ContactPage            | Pagine di contatto           | name, url                                                           |
| VideoObject            | Contenuti video              | name, description, thumbnailUrl, uploadDate, duration, contentUrl   |
| ImageObject            | Contenuti immagine           | contentUrl, caption, creator, copyrightHolder                       |
| Event                  | Eventi                       | name, startDate, endDate, location, organizer, offers               |
| JobPosting             | Annunci di lavoro            | title, description, datePosted, hiringOrganization, jobLocation     |
| Course                 | Contenuti educativi          | name, description, provider, hasCourseInstance                      |
| DiscussionForumPosting | Thread del forum             | headline, author, datePublished, text, url                          |
| ProductGroup           | Prodotti con varianti        | name, productGroupID, variesBy, hasVariant                          |
| ProfilePage            | Profili autore/creatore      | mainEntity (Person), name, url, description, sameAs                 |

---

## Limitati — Solo per tipi di sito specifici

| Tipo    | Restrizione                                   | Dal         |
| ------- | --------------------------------------------- | ----------- |
| FAQPage | SOLO siti di autorità governative e sanitarie | Agosto 2023 |

> Google ha limitato drasticamente i risultati avanzati (rich results) per le FAQ. Solo le fonti autorevoli (governo, organizzazioni sanitarie) ricevono ora i rich results per le FAQ. NON raccomandare lo schema FAQPage per i siti commerciali.

---

## Deprecati — Mai raccomandare

| Tipo                                | Stato                                    | Dal            | Note                                                      |
| ----------------------------------- | ---------------------------------------- | -------------- | --------------------------------------------------------- |
| HowTo                               | Risultati avanzati completamente rimossi | Settembre 2023 | Google ha smesso di mostrare i rich results per "how-to"  |
| SpecialAnnouncement                 | Deprecato                                | 31 luglio 2025 | Schema dell'era COVID, non più elaborato                  |
| CourseInfo                          | Ritirato dai rich results                | Giugno 2025    | Unito in Course                                           |
| EstimatedSalary                     | Ritirato dai rich results                | Giugno 2025    | Non più visualizzato                                      |
| LearningVideo                       | Ritirato dai rich results                | Giugno 2025    | Usare VideoObject al suo posto                            |
| ClaimReview                         | Ritirato dai rich results                | Giugno 2025    | Il markup fact-check non genera più rich results          |
| VehicleListing                      | Ritirato dai rich results                | Giugno 2025    | Dati strutturati per l'elenco veicoli interrotti          |
| Azioni del Libro (Book Actions)     | Deprecato poi ANNULLATO                  | Giugno 2025    | **Ancora funzionale a febbraio 2026** — solo nota storica |
| Problema Pratico (Practice Problem) | Ritirato dai rich results                | Fine 2025      | I problemi pratici educativi non sono più visualizzati    |
| Dataset                             | Ritirato dai rich results                | Fine 2025      | Funzionalità Dataset Search interrotta                    |

---

## Aggiunte Recenti (2024-2026)

| Tipo/Funzionalità                                     | Aggiunto        | Note                                                                                     |
| ----------------------------------------------------- | --------------- | ---------------------------------------------------------------------------------------- |
| Markup della Certificazione Prodotto                  | Aprile 2025     | Classi energetiche, certificazioni di sicurezza. Ha sostituito EnergyConsumptionDetails. |
| ProductGroup                                          | 2025            | Varianti di prodotto e-commerce con proprietà variesBy, hasVariant                       |
| ProfilePage                                           | 2025            | Pagine profilo autore/creatore con mainEntity Person per E-E-A-T                         |
| DiscussionForumPosting                                | 2024            | Per contenuti di forum/community                                                         |
| Speakable                                             | Aggiornato 2024 | Per l'ottimizzazione della ricerca vocale                                                |
| LoyaltyProgram                                        | Giugno 2025     | Prezzi per i membri, dati strutturati per carte fedeltà                                  |
| Policy di spedizione/reso a livello di organizzazione | Novembre 2025   | Configurazione tramite Search Console senza Merchant Center                              |
| ConferenceEvent                                       | Dicembre 2025   | Aggiunta di Schema.org v29.4                                                             |
| PerformingArtsEvent                                   | Dicembre 2025   | Aggiunta di Schema.org v29.4                                                             |

## Requisiti E-commerce (Aggiornati)

| Requisito                                     | Stato            | Dal                                                  |
| --------------------------------------------- | ---------------- | ---------------------------------------------------- |
| `returnPolicyCountry` in MerchantReturnPolicy | **Obbligatorio** | Marzo 2025                                           |
| Dati strutturati per varianti di prodotto     | Ampliato         | 2025 — include abbigliamento, cosmetici, elettronica |

> **Nota:** La Content API for Shopping chiuderà il 18 agosto 2026. Migrare alla Merchant API.

---

## Checklist di Validazione

Per ogni blocco di schema, verificare:

1. ✅ `@context` è `"https://schema.org"` (non http)
2. ✅ `@type` è un tipo valido e non deprecato
3. ✅ Tutte le proprietà obbligatorie sono presenti
4. ✅ I valori delle proprietà corrispondono ai tipi di dati previsti
5. ✅ Nessun testo segnaposto (es. "[Nome Azienda]")
6. ✅ Gli URL sono assoluti, non relativi
7. ✅ Le date sono nel formato ISO 8601
8. ✅ Le immagini hanno URL validi

## Strumenti di Test

- [Test dei Risultati Avanzati di Google](https://search.google.com/test/rich-results)
- [Validatore di Schema.org](https://validator.schema.org/)
