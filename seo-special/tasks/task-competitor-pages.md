---
name: task-competitor-pages
description: Genera pagine di confronto con i competitor e alternative ottimizzate per la SEO. Include layout 'X vs Y', pagine 'alternative a X', matrici delle funzionalità, schema markup e ottimizzazione della conversione (CRO). Da utilizzare quando l'utente richiede 'pagine di confronto', 'pagine vs', 'pagine alternative', 'confronto competitor' o 'X vs Y'.
---

# Pagine di Confronto Competitor & Alternative

Crea pagine ad alto tasso di conversione che intercettano query competitive come "X vs Y" o "Alternative a X", utilizzando contenuti strutturati e accurati.

## Tipi di Pagine

1. **Pagine di Confronto "X vs Y":**
   - Analisi testa a testa tra due prodotti/servizi.
   - Confronto bilanciato caratteristica per caratteristica.
   - Verdetto chiaro o raccomandazione giustificata.
   - Keyword target: `[Prodotto A] vs [Prodotto B]`.

2. **Pagine "Alternative a X":**
   - Elenco di alternative a un prodotto specifico.
   - Ogni alternativa con riassunto, pro/contro e caso d'uso ideale.
   - Keyword target: `Alternative a [Prodotto]`, `Migliori alternative a [Prodotto]`.

3. **Roundup "Migliori Strumenti [Categoria]":**
   - Elenco curato dei migliori tool in una categoria.
   - Criteri di ranking chiaramente dichiarati.
   - Keyword target: `Migliori strumenti [Categoria] [Anno]`.

4. **Pagine di Confronto (Comparison Table Pages):**
   - Matrice delle funzionalità con più prodotti disposti in colonne.
   - Ordinabile/filtrabile in caso di elementi interattivi.
   - Parole chiave target: confronto [categoria], tabella comparativa [categoria].

## Matrice delle Funzionalità (Analisi Top 5)

Per ogni analisi, identificare almeno **5 competitor chiave** e includere l'**URL del sito ufficiale** per trasparenza e reciprocità di entità (entity linking).

```
| Caratteristica   | Tuo Prodotto | URL Competitor | Competitor A  | Competitor B |
|------------------|:------------:|:--------------:|:-------------:|:------------:|
| Funzionalità 1   | ✅           | [link](url)    | ✅           | ❌          |
| Funzionalità 2   | ✅           | [link](url)    | ⚠️ Parziale  | ✅          |
| Funzionalità 3   | ❌           | [link](url)    | ✅           | ❌          |
| Prezzo (da)      | € X/mese     | [link](url)    | € Y/mese      | € Z/mese     |
```

## Requisiti di Accuratezza (Data Accuracy)
- Tutte le affermazioni devono essere verificabili da fonti pubbliche.
- I prezzi devono essere aggiornati (includere nota "al [data]").
- Revisione trimestrale obbligatoria per riflettere i cambiamenti dei competitor.
- Link alla fonte per ogni dato relativo ai competitor, ove possibile.

## Raccomandazioni Schema Markup

### Schema Product con AggregateRating
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "[Nome Prodotto]",
  "description": "[Descrizione Prodotto]",
  "brand": {
    "@type": "Brand",
    "name": "[Nome Brand]"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "[Valutazione]",
    "reviewCount": "[Conteggio]",
    "bestRating": "5",
    "worstRating": "1"
  }
}
```

### SoftwareApplication (per confronti tra software)
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "[Nome Software]",
  "applicationCategory": "[Categoria]",
  "operatingSystem": "[OS]",
  "offers": {
    "@type": "Offer",
    "price": "[Prezzo]",
    "priceCurrency": "USD"
  }
}
```

### ItemList (per pagine roundup)
```json
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Migliori Strumenti [Categoria] [Anno]",
  "itemListOrder": "https://schema.org/ItemListOrderDescending",
  "numberOfItems": "[Conteggio]",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "[Nome Prodotto]",
      "url": "[URL Prodotto]"
    }
  ]
}
```

## Targeting delle Parole Chiave

### Pattern di Intento di Confronto
| Pattern                     | Esempio                                    | Segnale Volume Ricerca |
|-----------------------------|--------------------------------------------|----------------------|
| `[A] vs [B]`                | "[Prodotto A] vs [Prodotto B]"             | Alto                 |
| `[A] alternative`           | "Alternative a Figma"                      | Alto                 |
| `[A] alternatives [year]`   | "Alternative a Notion 2026"                | Alto                 |
| `best [category] tools`     | "migliori strumenti project management"    | Alto                 |
| `[A] vs [B] for [use case]` | "AWS vs Azure per startup"                 | Medio                |
| `[A] review [year]`         | "Recensione Monday.com 2026"               | Medio                |
| `[A] vs [B] pricing`        | "Prezzi HubSpot vs Salesforce"             | Medio                |
| `is [A] better than [B]`    | "Notion è meglio di Confluence?"           | Medio                |

### Formule per Title Tag
- X vs Y: `[A] vs [B]: [Differenziatore Chiave] ([Anno])`
- Alternative: `Le [N] Migliori Alternative a [A] nel [Anno] (Gratis & a Pagamento)`
- Roundup: `I [N] Migliori Strumenti [Categoria] nel [Anno] — Confrontati e Classificati`

### Pattern H1
- Corrispondenza con l'intento del title tag
- Includi la parola chiave principale in modo naturale
- Mantieni sotto i 70 caratteri

## Layout Ottimizzati per la Conversione

### Posizionamento CTA
- **Above fold**: Breve riassunto del confronto con CTA primaria
- **Dopo la tabella di confronto**: CTA "Prova [Tuo Prodotto] gratis"
- **Fondo pagina**: Raccomandazione finale con CTA
- Evita CTA aggressive nelle sezioni descrittive dei competitor (riduce la fiducia)

### Sezioni Social Proof (Riprova Sociale)
- Testimonianze dei clienti rilevanti per i criteri di confronto
- Valutazioni G2/Capterra/TrustPilot (con link alla fonte)
- Case study che mostrano la migrazione dal competitor
- Storie "Passati da [Competitor]"

### In Evidenza sui Prezzi
- Tabella chiara di confronto prezzi
- Evidenzia i vantaggi di valore (non solo il prezzo più basso)
- Includi costi nascosti (costi di setup, prezzi per utente, costi di eccedenza)
- Link alla pagina completa dei prezzi

### Segnali di Fiducia
- Timestamp "Ultimo aggiornamento [data]"
- Autore con competenza rilevante
- Dichiarazione della metodologia (come sono stati condotti i confronti)
- Dichiarazione di affiliazione al proprio prodotto

## Linee Guida di Correttezza (Fairness)

- **Accuratezza**: Tutte le informazioni sui competitor devono essere verificabili da fonti pubbliche
- **Nessuna diffamazione**: Non fare mai affermazioni false o fuorvianti sui competitor
- **Cita le fonti**: Inserisci link a siti web dei competitor, siti di recensioni o documentazione
- **Aggiornamenti tempestivi**: Rivedi e aggiorna quando i competitor rilasciano cambiamenti importanti
- **Dichiara l'affiliazione**: Dichiara chiaramente quale prodotto è tuo
- **Presentazione bilanciata**: Riconosci i punti di forza dei competitor in modo onesto
- **Accuratezza dei prezzi**: Includi disclaimer "al [data]" su tutti i dati di prezzo
- **Verifica delle funzionalità**: Testa le funzionalità dei competitor dove possibile, altrimenti cita la documentazione

## Linking Interno

- Linka le pagine del tuo prodotto/servizio dalle sezioni di confronto
- Link incrociati tra pagine di confronto correlate (es., "A vs B" linka a "A vs C")
- Linka a pagine specifiche delle funzionalità quando discuti singole funzionalità
- Breadcrumb: Home > Confronti > [Questa Pagina]
- Sezione confronti correlati a fondo pagina
- Linka a case study e testimonianze menzionate nel confronto

## Output

### Template Pagina di Confronto
- `COMPARISON-PAGE.md` — Struttura della pagina pronta da implementare con sezioni
- Tabella matrice delle funzionalità
- Outline dei contenuti con obiettivi di conteggio parole (minimo 1.500 parole)

### Schema Markup
- `comparison-schema.json` — Product/SoftwareApplication/ItemList JSON-LD

### Strategia Keyword
- Keyword primarie e secondarie
- Opportunità correlate a coda lunga (long-tail)
- Gap di contenuti rispetto alle pagine dei competitor esistenti

### Raccomandazioni
- Miglioramenti ai contenuti per pagine di confronto esistenti
- Nuove opportunità di pagine di confronto
- Aggiunte di schema markup
- Suggerimenti per l'ottimizzazione delle conversioni


## Analisi Strategica (Gap Analysis)
Oltre alla tabella tecnica, l'analisi deve evidenziare:
1. **Il Vantaggio Ingiusto:** Cosa rende la tua offerta unica (es. AI proprietaria, Business Design).
2. **GEO Dominance:** Confronto sull'accessibilità per le AI (presenza di `llms.txt`, crawler bots consentiti).
3. **E-E-A-T Comparison:** Analisi dell'autorevolezza del team e dei casi studio rispetto ai competitor.

## Raccomandazioni Schema Markup
- **Product:** Con `AggregateRating` per mostrare le stelline nei risultati.
- **SoftwareApplication:** Per confronti tra software (include categoria e OS).
- **ItemList:** Per le pagine roundup (elenco numerato di ListItem).

## Strategia di Conversione
- **Above-the-fold:** Breve riassunto del confronto con CTA primaria.
- **Dopo la tabella:** "Prova [Tuo Prodotto] gratis".
- **Social Proof:** Testimonianze di clienti che sono passati dal competitor al tuo prodotto.

## Linee Guida di Correttezza (Fairness)
- **Nessuna diffamazione:** Non fare mai affermazioni false o fuorvianti sui competitor.
- **Cita le fonti:** Inserisci link ai siti dei competitor o a documentazione ufficiale.
- **Trasparenza:** Dichiara chiaramente l'affiliazione con il tuo prodotto.

---

## Formato Output
- `PAGINA-CONFRONTO.md`: Struttura pronta all'uso con sezioni ottimizzate.
- `generated-schema.json`: Snippet JSON-LD per la pagina.
- `KEYWORD-STRATEGY.md`: Keyword primarie, secondarie e opportunità long-tail.
