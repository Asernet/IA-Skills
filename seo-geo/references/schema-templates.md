# Template di Schema JSON-LD

Template di dati strutturati JSON-LD pronti all'uso per l'ottimizzazione SEO e GEO.

---

## 1. Schema FAQPage (+40% di Visibilità AI)

**Ideale per:** sezioni FAQ, pagine della knowledge base, pagine prodotto con Domande e Risposte.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Cos'è [Il tuo Prodotto/Servizio]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Risposta completa con statistiche. Secondo X, l'85% degli utenti riporta il beneficio Y.]"
      }
    },
    {
      "@type": "Question",
      "name": "Come funziona [Prodotto/Servizio]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Spiegazione passo dopo passo. Prima, fai... Poi... Infine...]"
      }
    },
    {
      "@type": "Question",
      "name": "Quali sono i vantaggi di [Prodotto/Servizio]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Elenca i vantaggi principali con dati. Gli utenti risparmiano in media X ore a settimana.]"
      }
    },
    {
      "@type": "Question",
      "name": "Quanto costa [Prodotto/Servizio]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Informazioni sui prezzi. I piani partono da €X/mese con un piano gratuito disponibile.]"
      }
    },
    {
      "@type": "Question",
      "name": "Come posso iniziare con [Prodotto/Servizio]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Istruzioni per l'installazione/registrazione. Esegui: curl -fsSL example.com/install.sh | bash]"
      }
    }
  ]
}
```

---

## 2. Schema WebPage

**Ideale per:** pagine di contenuto standard, landing page.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Titolo della Pagina]",
  "description": "[Descrizione della pagina, 150-160 caratteri]",
  "url": "https://example.com/pagina",
  "datePublished": "2024-01-15",
  "dateModified": "2024-12-20",
  "inLanguage": "it-IT",
  "isPartOf": {
    "@type": "WebSite",
    "name": "[Nome del Sito]",
    "url": "https://example.com"
  },
  "author": {
    "@type": "Person",
    "name": "[Nome dell'Autore]",
    "url": "https://example.com/chi-siamo"
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Nome dell'Organizzazione]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".summary", ".key-points"]
  }
}
```

---

## 3. Schema Article

**Ideale per:** post di blog, articoli di notizie, tutorial.

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[Titolo dell'Articolo - Max 110 caratteri]",
  "description": "[Riepilogo dell'articolo]",
  "image": [
    "https://example.com/immagine-1x1.jpg",
    "https://example.com/immagine-4x3.jpg",
    "https://example.com/immagine-16x9.jpg"
  ],
  "datePublished": "2024-01-15T08:00:00+00:00",
  "dateModified": "2024-12-20T10:30:00+00:00",
  "author": {
    "@type": "Person",
    "name": "[Nome dell'Autore]",
    "url": "https://example.com/autore/nome",
    "jobTitle": "[Titolo Professionale]",
    "worksFor": {
      "@type": "Organization",
      "name": "[Azienda]"
    }
  },
  "publisher": {
    "@type": "Organization",
    "name": "[Nome dell'Editore]",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png",
      "width": 600,
      "height": 60
    }
  },
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/url-articolo"
  },
  "keywords": ["parola-chiave1", "parola-chiave2", "parola-chiave3"],
  "articleSection": "[Categoria]",
  "wordCount": 2500
}
```

---

## 4. Schema SoftwareApplication

**Ideale per:** strumenti, app, prodotti software.

```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Nome dell'App]",
  "description": "[Descrizione dell'app]",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "url": "https://example.com",
  "downloadUrl": "https://example.com/download",
  "softwareVersion": "1.0.0",
  "releaseNotes": "https://example.com/changelog",
  "screenshot": "https://example.com/screenshot.png",
  "featureList": [
    "Descrizione Funzionalità 1",
    "Descrizione Funzionalità 2",
    "Descrizione Funzionalità 3"
  ],
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "150",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@type": "Organization",
    "name": "[Nome dell'Azienda]",
    "url": "https://example.com"
  }
}
```

---

## 5. Schema Organization

**Ideale per:** pagine "Chi siamo", pagine aziendali.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "[Nome dell'Organizzazione]",
  "alternateName": "[Nome Alternativo]",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "description": "[Descrizione dell'organizzazione]",
  "foundingDate": "2024",
  "founders": [
    {
      "@type": "Person",
      "name": "[Nome del Fondatore]"
    }
  ],
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "[Città]",
    "addressRegion": "[Provincia]",
    "addressCountry": "[Paese]"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer service",
    "email": "support@example.com"
  },
  "sameAs": [
    "https://twitter.com/example",
    "https://github.com/example",
    "https://linkedin.com/company/example"
  ]
}
```

---

## 6. Schema Product

**Ideale per:** pagine prodotto e-commerce.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Nome del Prodotto]",
  "description": "[Descrizione del prodotto]",
  "image": [
    "https://example.com/immagine-prodotto-1.jpg",
    "https://example.com/immagine-prodotto-2.jpg"
  ],
  "sku": "[SKU]",
  "brand": {
    "@type": "Brand",
    "name": "[Nome del Brand]"
  },
  "offers": {
    "@type": "Offer",
    "url": "https://example.com/prodotto",
    "priceCurrency": "EUR",
    "price": "99.99",
    "priceValidUntil": "2025-12-31",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "[Nome del Venditore]"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "89"
  },
  "review": [
    {
      "@type": "Review",
      "reviewRating": {
        "@type": "Rating",
        "ratingValue": "5",
        "bestRating": "5"
      },
      "author": {
        "@type": "Person",
        "name": "[Nome del Recensore]"
      },
      "reviewBody": "[Testo della recensione]"
    }
  ]
}
```

---

## 7. Schema HowTo

**Ideale per:** tutorial, guide, articoli "come fare".

```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Come [Fare Qualcosa]",
  "description": "[Breve descrizione di ciò che copre questa guida]",
  "image": "https://example.com/immagine-how-to.jpg",
  "totalTime": "PT15M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "EUR",
    "value": "0"
  },
  "supply": [
    {
      "@type": "HowToSupply",
      "name": "[Elemento necessario 1]"
    }
  ],
  "tool": [
    {
      "@type": "HowToTool",
      "name": "[Strumento necessario 1]"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Passaggio 1: [Nome Passaggio]",
      "text": "[Istruzioni dettagliate del passaggio]",
      "image": "https://example.com/passaggio-1.jpg",
      "url": "https://example.com/guida#passaggio1"
    },
    {
      "@type": "HowToStep",
      "name": "Passaggio 2: [Nome Passaggio]",
      "text": "[Istruzioni dettagliate del passaggio]",
      "image": "https://example.com/passaggio-2.jpg",
      "url": "https://example.com/guida#passaggio2"
    },
    {
      "@type": "HowToStep",
      "name": "Passaggio 3: [Nome Passaggio]",
      "text": "[Istruzioni dettagliate del passaggio]",
      "image": "https://example.com/passaggio-3.jpg",
      "url": "https://example.com/guida#passaggio3"
    }
  ]
}
```

---

## 8. Schema BreadcrumbList

**Ideale per:** tutte le pagine con gerarchia di navigazione.

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Categoria]",
      "item": "https://example.com/categoria"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Pagina Corrente]",
      "item": "https://example.com/categoria/pagina"
    }
  ]
}
```

---

## 9. Schema LocalBusiness

**Ideale per:** pagine di attività locali.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[Nome dell'Attività]",
  "description": "[Descrizione dell'attività]",
  "image": "https://example.com/immagine-attività.jpg",
  "url": "https://example.com",
  "telephone": "+1-555-555-5555",
  "email": "contatto@example.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Indirizzo Stradale]",
    "addressLocality": "[Città]",
    "addressRegion": "[Provincia]",
    "postalCode": "[CAP]",
    "addressCountry": "IT"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 37.7749,
    "longitude": -122.4194
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "09:00",
      "closes": "17:00"
    }
  ],
  "priceRange": "$$"
}
```

---

## 10. SpeakableSpecification (Potenziamento GEO)

**Ideale per:** ottimizzazione della ricerca vocale, estrazione AI.

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "[Titolo della Pagina]",
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": ["h1", ".summary", ".punti-chiave", ".risposta-faq"]
  }
}
```

---

## Esempio di Schema Combinato

Per una pagina prodotto software con FAQ:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "OPC Skills - Skill per Agenti AI per Solopreneur",
      "description": "Oltre 10 skill per agenti per Claude Code, Cursor, Codex. Hunting di domini, ricerca sui social media, creazione di loghi.",
      "url": "https://opc.dev",
      "dateModified": "2024-12-20",
      "speakable": {
        "@type": "SpeakableSpecification",
        "cssSelector": ["h1", ".hero-description", ".faq-answer"]
      }
    },
    {
      "@type": "SoftwareApplication",
      "name": "OPC Skills",
      "applicationCategory": "DeveloperApplication",
      "operatingSystem": "Cross-platform",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "EUR"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "Cos'è OPC Skills?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "OPC Skills è una collezione di oltre 10 skill per agenti AI per solopreneur, che supporta Claude Code, Cursor e Codex."
          }
        }
      ]
    },
    {
      "@type": "Organization",
      "name": "OPC Skills",
      "url": "https://opc.dev",
      "sameAs": ["https://github.com/ReScienceLab/opc-skills"]
    }
  ]
}
```

---

## Strumenti di Validazione

1. **Test dei Risultati Multimediali di Google**

   ```
   https://search.google.com/test/rich-results?url={il-tuo-url}
   ```

2. **Validatore di Schema.org**

   ```
   https://validator.schema.org/?url={il-tuo-url}
   ```

3. **Google Search Console**
   - Controlla la sezione "Miglioramenti" per problemi relativi allo schema
   - Monitora le prestazioni dei risultati multimediali
