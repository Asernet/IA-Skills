<!-- Aggiornato: 2026-02-07 -->

# Template Strategia SEO per Agenzie/Consulenze

## Caratteristiche del Settore

- Basato sui servizi, transazioni di alto valore
- Competenza e fiducia sono fondamentali
- Cicli di considerazione lunghi
- Decisioni guidate da portfolio/casi studio
- Vendite basate sulle relazioni
- Vantaggi della specializzazione di nicchia

## Architettura del Sito Raccomandata

```
/
17: ├── Home
18: ├── /servizi
19: │   ├── /servizio-1
20: │   │   ├── /sotto-servizio-1
21: │   │   └── ...
22: │   └── /servizio-2
23: ├── /settori
24: │   ├── /settore-1
25: │   ├── /settore-2
26: │   └── ...
27: ├── /lavori (o /casi-studio)
28: │   ├── /caso-studio-1
29: │   ├── /caso-studio-2
30: │   └── ...
31: ├── /chi-siamo
32: │   ├── /team
33: │   │   ├── /membro-team-1
34: │   │   └── ...
35: │   ├── /cultura
36: │   └── /carriera
37: ├── /insight (o /blog)
38: │   ├── /articoli
39: │   ├── /guide
40: │   ├── /webinar
41: │   └── /podcast
42: ├── /contatti
43: ├── /processo
44: └── /faq
```

## Raccomandazioni Schema

| Tipo di Pagina  | Tipi di Schema                    |
| --------------- | --------------------------------- |
| Homepage        | Organization, ProfessionalService |
| Pagina Servizio | Service, ProfessionalService      |
| Caso Studio     | Article, Organization (cliente)   |
| Membro del Team | Person, ProfilePage               |
| Blog            | Article, BlogPosting              |

### Esempio Schema ProfessionalService

```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Agency Name",
  "description": "What the agency does",
  "url": "https://example.com",
  "logo": "https://example.com/logo.png",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Agency St",
    "addressLocality": "City",
    "addressRegion": "State",
    "postalCode": "12345"
  },
  "telephone": "+1-555-555-5555",
  "areaServed": "National",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Services",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Service 1"
        }
      }
    ]
  }
}
```

## Requisiti E-E-A-T

### Le Pagine del Team Devono Includere

- Foto professionali (headshot)
- Bio dettagliate con credenziali
- Esperienza nel settore
- Partecipazioni a conferenze
- Pubblicazioni
- Profili social

### I Casi Studio Devono Includere

- Nome del cliente (con permesso) o settore
- Descrizione della sfida/problema
- Approccio/metodologia
- Risultati con metriche specifiche
- Timeline
- Citazione della testimonianza

## Priorità dei Contenuti

### Priorità Alta

1. Pagine dei servizi (dettagliate, specifiche)
2. Pagine di settore (competenza verticale)
3. 3-5 casi studio dettagliati
4. Pagine del team/leadership

### Priorità Media

1. Pagina metodologia/processo
2. Blog con leadership di pensiero (thought leadership)
3. Contenuti di confronto (rispetto alle alternative)
4. Pagina FAQ

### Argomenti di Thought Leadership

- Analisi dei trend di settore
- Guide pratiche (non competitive)
- Ricerche originali/sondaggi
- Recap di eventi e insight
- Interviste a esperti
- Recensioni di strumenti/tecnologie

## Strategia dei Contenuti

### Pagine dei Servizi (min 800 parole)

- Proposta di valore chiara
- Panoramica della metodologia
- Elenco dei deliverable
- Casi studio pertinenti
- Membri del team che forniscono il servizio
- CTA per programmare una consulenza

### Pagine di Settore (min 800 parole)

- Sfide specifiche del settore
- In che modo le risolvete in modo diverso
- Casi studio pertinenti
- Credenziali/esperienza nel settore
- Logo dei clienti (con permesso)

### Casi Studio (min 1.000 parole)

- Sintesi esecutiva
- Background del cliente
- Dettagli della sfida
- Approccio alla soluzione
- Processo di implementazione
- Risultati misurabili
- Testimonianza del cliente
- Servizi correlati/CTA

## Metriche Chiave da Monitorare

- Traffico organico verso le pagine dei servizi
- Visualizzazioni delle pagine dei casi studio
- Invii del modulo di contatto da traffico organico
- Tempo sulla pagina per i contenuti chiave
- Conversione Blog → pagina servizio

## Ottimizzazione per i Motori Generativi (GEO) per le Agenzie

- [ ] Pubblicare casi studio originali con metriche e risultati specifici e citabili
- [ ] Usare lo schema Person con link sameAs per tutti i membri del team (costruisce l'autorità dell'entità)
- [ ] Usare lo schema ProfilePage per le pagine dei membri del team
- [ ] Includere dichiarazioni di competenza chiare e citabili nelle descrizioni delle pagine dei servizi
- [ ] Produrre ricerche di settore e sondaggi originali che i sistemi di AI possano citare
- [ ] Strutturare i contenuti di thought leadership con titoli chiari e insight estraibili
- [ ] Mantenere informazioni coerenti sull'entità agenzia tra directory, profili social e siti di settore
- [ ] Monitorare le citazioni AI in ChatGPT, Perplexity e Google AI Overviews per il brand e i termini dei servizi chiave
