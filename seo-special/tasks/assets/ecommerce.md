<!-- Aggiornato: 2026-02-07 -->

# Template Strategia SEO per E-commerce

## Caratteristiche del Settore

- Alta intenzione di transazione
- Comportamento di confronto dei prodotti
- Sensibilità al prezzo
- Processo decisionale basato sull'aspetto visivo
- Modelli di domanda stagionale
- Annunci competitivi nei marketplace

## Architettura del Sito Raccomandata

```
/
├── Home
├── /collezioni (o /categorie)
│   ├── /categoria-1
│   │   ├── /sottocategoria-1
│   │   └── ...
│   ├── /categoria-2
│   └── ...
├── /prodotti
│   ├── /prodotto-1
│   ├── /prodotto-2
│   └── ...
├── /brand
│   ├── /brand-1
│   └── ...
├── /saldi (o /offerte)
├── /nuovi-arrivi
├── /i-piu-venduti
├── /guida-regali
├── /blog
│   ├── /guide-acquisto
│   ├── /come-fare
│   └── /trend
├── /chi-siamo
├── /contatti
├── /spedizioni
├── /resi
└── /faq
```

## Raccomandazioni Schema

| Tipo di Pagina   | Tipi di Schema                                          |
| ---------------- | ------------------------------------------------------- |
| Pagina Prodotto  | Product, Offer, AggregateRating, Review, BreadcrumbList |
| Pagina Categoria | CollectionPage, ItemList, BreadcrumbList                |
| Pagina Brand     | Brand, Organization                                     |
| Blog             | Article, BlogPosting                                    |

### Ulteriori Schemi E-commerce (2025)

- **ProductGroup**: Da usare per prodotti con varianti (taglia, colore). Avvolge le singole voci Product con le proprietà `variesBy` e `hasVariant`. Vedere `schema/templates.json`.
- **Certification**: Per le certificazioni dei prodotti (Energy Star, sicurezza, biologico). Ha sostituito EnergyConsumptionDetails (Aprile 2025). Usare `hasCertification` su Product.
- **OfferShippingDetails**: Include tariffe di spedizione, tempi di gestione e tempi di transito. Fondamentale per l'idoneità a Merchant Center.

> **Schede gratuite di Google Merchant Center:** I prodotti possono apparire gratuitamente in Google Shopping. Assicurarsi che i dati strutturati Product siano nell'HTML iniziale renderizzato dal server (non iniettati via JavaScript) con le proprietà obbligatorie: `name`, `image`, `price`, `priceCurrency`, `availability`.

> **Nota sul Rendering JS:** I dati strutturati Product dovrebbero trovarsi nell'HTML iniziale renderizzato dal server — non iniettati dinamicamente via JavaScript (secondo la guida Google JS SEO di dicembre 2025).

### Esempio Schema Product

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "image": ["https://example.com/product.jpg"],
  "description": "Product description",
  "sku": "SKU123",
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/product"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "42"
  }
}
```

## Requisiti dei Contenuti

### Pagine Prodotto (min 400 parole)

- Descrizioni prodotto uniche (non copiate dal produttore)
- Caratteristiche in evidenza
- Casi d'uso / a chi è rivolto
- Tabella delle specifiche
- Guida alle taglie/vestibilità (per l'abbigliamento)
- Istruzioni per la cura
- Recensioni dei clienti

### Pagine di Categoria (min 400 parole)

- Introduzione alla categoria
- Estratto della guida all'acquisto
- Prodotti in evidenza
- Link alle sottocategorie
- Opzioni di filtro/ordinamento

## Considerazioni Tecniche

### Paginazione

- Usare rel="next"/rel="prev" o caricamento infinito (load-more)
- Assicurarsi che tutti i prodotti siano scansionabili
- Canonical verso la pagina di categoria principale

### Navigazione a Sfaccettature (Faceted Navigation)

- Noindex per le combinazioni di filtri che creano contenuti duplicati
- Usare i tag canonical in modo appropriato
- Assicurarsi che i filtri popolari siano indicizzabili

### Varianti di Prodotto

- URL singolo per il prodotto genitore con varianti
- Oppure URL separati con canonical verso il genitore
- Dati strutturati per tutte le varianti

## Priorità dei Contenuti

### Priorità Alta

1. Pagine di categoria (livello superiore)
2. Pagine dei prodotti più venduti
3. Homepage
4. Guide all'acquisto per le categorie principali

### Priorità Media

1. Pagine di sottocategoria
2. Pagine dei brand
3. Contenuti di confronto
4. Landing page stagionali

### Argomenti del Blog

- Guide all'acquisto ("Come scegliere...")
- Confronti tra prodotti
- Report sui trend
- Casi d'uso e ispirazione
- Guide alla cura e manutenzione

## Metriche Chiave da Monitorare

- Entrate da ricerca organica
- Ranking delle pagine prodotto
- Ranking delle pagine di categoria
- Percentuale di clic (CTR) per i risultati multimediali
- Valore medio dell'ordine (AOV) da ricerca organica

## Ottimizzazione per i Motori Generativi (GEO) per l'E-commerce

Le piattaforme di ricerca AI rispondono sempre più direttamente alle query sui prodotti. Ottimizzare per la citazione AI:

- [ ] Includere specifiche chiare del prodotto, dimensioni, materiali in formato strutturato
- [ ] Usare lo schema ProductGroup per i prodotti con varianti
- [ ] Fornire fotografie originali del prodotto con testo alt descrittivo
- [ ] Includere contenuti reali di recensioni dei clienti (schema AggregateRating)
- [ ] Mantenere dati coerenti sull'entità prodotto su tutte le piattaforme (sito, Amazon, Merchant Center)
- [ ] Strutturare i contenuti di confronto con tabelle di caratteristiche chiare che l'AI possa analizzare
- [ ] Aggiungere contenuti FAQ dettagliati per le domande comuni sui prodotti
