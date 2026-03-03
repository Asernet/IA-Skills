<!-- Aggiornato: 2026-02-07 -->

# Template Strategia SEO per Business Generici

## Panoramica

Questo template si applica alle aziende che non rientrano perfettamente nelle categorie SaaS, servizi locali, e-commerce, editoria o agenzie. Personalizza in base al tuo specifico modello di business.

## Architettura del Sito Raccomandata

```
/
├── Home
├── /prodotti (o /servizi)
│   ├── /prodotto-1
│   ├── /prodotto-2
│   └── ...
├── /soluzioni (se applicabile)
│   ├── /soluzione-1
│   └── ...
├── /chi-siamo
│   ├── /team
│   ├── /storia
│   └── /valori
├── /risorse
│   ├── /blog
│   ├── /guide
│   ├── /faq
│   └── /glossario
├── /contatti
├── /supporto
└── /legale
    ├── /privacy
    └── /termini
```

## Principi SEO Universali

### Ogni Pagina Dovrebbe Avere

- Tag title unico (30-60 caratteri)
- Meta description unica (120-160 caratteri)
- Un singolo H1 che corrisponda all'intento della pagina
- Gerarchia dei titoli logica (H1→H2→H3)
- Link interni a contenuti correlati
- Chiamata all'azione (CTA) chiara

### Schema per Tutti i Siti

| Tipo di Pagina    | Tipi di Schema                     |
| ----------------- | ---------------------------------- |
| Homepage          | Organization, WebSite              |
| Chi Siamo         | Organization, AboutPage            |
| Contatti          | ContactPage                        |
| Blog              | Article, BlogPosting               |
| FAQ               | (FAQPage solo per siti gov/sanità) |
| Prodotto/Servizio | Product o Service                  |

## Standard di Qualità dei Contenuti

### Conteggio Minimo di Parole

| Tipo di Pagina    | Parole Min |
| ----------------- | ---------- |
| Homepage          | 500        |
| Prodotto/Servizio | 800        |
| Post del Blog     | 1.500      |
| Pagina Chi Siamo  | 400        |
| Landing Page      | 600        |

### Elementi Essenziali E-E-A-T

1. **Esperienza (Experience)**: Condividere esempi reali e casi studio
2. **Competenza (Expertise)**: Mostrare credenziali e qualifiche
3. **Autorevolezza (Authoritativeness)**: Guadagnare menzioni e citazioni
4. **Affidabilità (Trustworthiness)**: Informazioni di contatto complete, policy visibili

## Fondamenta Tecniche

### Indispensabili

- [ ] HTTPS abilitato
- [ ] Design mobile-responsive
- [ ] robots.txt configurato
- [ ] Sitemap XML inviata
- [ ] Google Search Console verificata
- [ ] Core Web Vitals superati (LCP < 2,5s, INP < 200ms, CLS < 0,1)

### Raccomandati

- [ ] Dati strutturati sulle pagine chiave
- [ ] Strategia di linking interno
- [ ] Pagina di errore 404 ottimizzata
- [ ] Catene di reindirizzamento eliminate
- [ ] Ottimizzazione delle immagini (WebP, lazy loading)

## Priorità dei Contenuti

### Fase 1: Fondamenta (settimane 1-4)

1. Ottimizzazione della homepage
2. Pagine core di prodotti/servizi
3. Pagine chi siamo e contatti
4. Implementazione dello schema di base

### Fase 2: Espansione (settimane 5-12)

1. Lancio del blog (2-4 post al mese)
2. Pagina FAQ
3. Pagine di prodotti/servizi aggiuntive
4. Audit del linking interno

### Fase 3: Crescita (settimane 13-24)

1. Pubblicazione costante di contenuti
2. Outreach per la link building
3. Ottimizzazione GEO
4. Ottimizzazione delle performance

### Fase 4: Autorità (mesi 7-12)

1. Contenuti di leadership di pensiero (thought leadership)
2. Ricerche originali
3. PR e menzioni media
4. Schema avanzato

## Metriche Chiave da Monitorare

- Traffico organico (complessivo e per sezione)
- Posizionamento delle parole chiave (branded e non branded)
- Tasso di conversione da traffico organico
- Pagine indicizzate
- Punteggi Core Web Vitals
- Backlink acquisiti

## Punti di Personalizzazione

Adattare questo template in base a:

1. **Modello di Business**: B2B vs B2C vs D2C
2. **Ambito Geografico**: Locale, nazionale o internazionale
3. **Tipo di Contenuto**: Incentrato sul prodotto vs ricco di contenuti
4. **Livello di Concorrenza**: Mercato di nicchia vs competitivo
5. **Risorse**: Budget e capacità del team

## Checklist per l'Ottimizzazione dei Motori Generativi (GEO)

- [ ] Includere fatti e statistiche chiari e citabili che i sistemi di AI possano estrarre e citare
- [ ] Usare dati strutturati (Schema.org) per aiutare i sistemi di AI a comprendere il contenuto
- [ ] Costruire l'autorità tematica attraverso cluster di contenuti completi
- [ ] Fornire dati originali, ricerche o prospettive uniche che l'AI non può trovare altrove
- [ ] Mantenere informazioni coerenti sull'entità (brand, persone, prodotti) in tutto il web
- [ ] Strutturare il contenuto con titoli chiari, definizioni e formati passo-passo
- [ ] Considerare l'aggiunta di un file `llms.txt` alla radice del sito (convenzione emergente per i crawler AI — Google lo tratta come un normale file di testo)
- [ ] Monitorare le citazioni AI in Google AI Overviews, ChatGPT, Perplexity e Bing Copilot
