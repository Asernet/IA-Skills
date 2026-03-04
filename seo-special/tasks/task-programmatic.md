---
name: task-programmatic
description: Pianificazione e analisi SEO programmatica per pagine generate su larga scala da fonti di dati. Copre motori di template, pattern URL, automazione del linking interno, salvaguardie contro i contenuti "thin" e prevenzione dell'index bloat. Usare quando l'utente menziona "SEO programmatica", "pagine su larga scala", "pagine dinamiche", "pagine template", "pagine generate" o "SEO guidata dai dati".
---

# Analisi e Pianificazione SEO Programmatica

Costruire e analizzare pagine SEO generate su larga scala da fonti di dati strutturati. Implementa "quality gates" per prevenire penalità per contenuti scarsi (thin content) e l'index bloat.

## Valutazione della Fonte Dati

Valutare i dati che alimentano le pagine programmatiche:

- **File CSV/JSON**: Conteggio righe, univocità delle colonne, valori mancanti.
- **Endpoint API**: Struttura della risposta, freschezza dei dati, limiti di frequenza (rate limits).
- **Query al database**: Conteggio dei record, completezza dei campi, frequenza di aggiornamento.
- Controlli di qualità dei dati:
  - Ogni record deve avere abbastanza attributi unici per generare contenuti distinti.
  - Segnalare record duplicati o quasi duplicati (>80% di sovrapposizione dei campi).
  - Verificare la freschezza dei dati — dati obsoleti producono pagine obsolete.

## Pianificazione del Motore di Template

Progettare template che producano pagine uniche e di valore:

- **Punti di iniezione delle variabili**: Titolo, H1, sezioni del corpo, meta description, schema.
- **Blocchi di contenuto**: Statici (condivisi tra le pagine) vs Dinamici (unici per pagina).
- **Logica condizionale**: Mostrare/nascondere sezioni in base alla disponibilità dei dati.
- **Contenuti supplementari**: Articoli correlati, consigli contestuali, contenuti generati dagli utenti.
- Checklist di revisione del template:
  - Ogni pagina deve apparire come una risorsa autonoma e di valore.
  - Evitare pattern tipo "mad-libs" (semplice sostituzione di nomi di città/prodotti in testi identici).
  - Le sezioni dinamiche devono aggiungere informazioni reali, non solo varianti di parole chiave.

## Strategia dei Pattern URL

### Pattern Comuni

- `/strumenti/[nome-strumento]` — Pagine di directory strumenti/prodotti.
- `/[città]/[servizio]` — Pagine località + servizio.
- `/integrazioni/[piattaforma]` — Landing page di integrazione.
- `/glossario/[termine]` — Pagine di definizione/riferimento.
- `/template/[nome-template]` — Pagine di download template.

### Regole URL

- Slug in minuscolo, con trattini, derivati dai dati.
- Gerarchia logica che rifletta l'architettura del sito.
- Nessuno slug duplicato — imporre l'univocità al momento della generazione.
- Mantenere gli URL sotto i 100 caratteri.
- Nessun parametro di query per gli URL dei contenuti primari.
- Uso coerente dello slash finale (coerente con il pattern del sito esistente).

## Automazione del Linking Interno

- **Modello Hub/Spoke**: Pagine hub di categoria che puntano alle singole pagine programmatiche.
- **Elementi correlati**: Linking automatico a 3-5 pagine correlate basato sugli attributi dei dati.
- **Breadcrumb**: Generare lo schema BreadcrumbList dalla gerarchia degli URL.
- **Cross-linking**: Link tra pagine programmatiche che condividono attributi (stessa categoria, stessa città, stessa funzione).
- **Anchor text**: Usare anchor text descrittivi e variegati — evitare la ripetizione di parole chiave a corrispondenza esatta.
- Densità dei link: 3-5 link interni ogni 1000 parole (coerente con le linee guida `task-content.md`).

## Salvaguardie contro i Contenuti Scarsi (Thin Content)

### Quality Gates

| Metrica                              | Soglia | Azione                                                                     |
| ------------------------------------ | ------ | -------------------------------------------------------------------------- |
| Pagine senza revisione dei contenuti | 100+   | ⚠️ AVVISO — richiede audit dei contenuti prima della pubblicazione         |
| Pagine senza giustificazione         | 500+   | 🛑 STOP — richiede approvazione esplicita dell'utente e audit thin content |
| Contenuto unico per pagina           | <40%   | ❌ Segnala come thin content — rischio penalità elevato                    |
| Conteggio parole per pagina          | <300   | ⚠️ Segnala per revisione — potrebbe mancare di valore sufficiente          |

### Abuso di Contenuti su Larga Scala — Contesto di Applicazione (2025-2026)

La policy di Google sull'abuso dei contenuti su larga scala (introdotta a marzo 2024) ha visto un'escalation nei controlli nel 2025:

- **Giugno 2025**: Ondata di azioni manuali contro siti con contenuti generati dall'AI su larga scala.
- **Agosto 2025**: L'aggiornamento spam SpamBrain ha migliorato il rilevamento di schemi di link e "content farm" generati dall'AI.
- **Risultato**: Google ha segnalato una riduzione del 45% dei contenuti di bassa qualità e non originali nei risultati di ricerca dopo l'applicazione di marzo 2024.

**Quality gates avanzati per pagine programmatiche:**

- **Differenziazione dei contenuti**: ≥30-40% del contenuto deve essere realmente unico tra due pagine programmatiche (non solo la sostituzione della città o della parola chiave).
- **Revisione umana**: Revisione a campione di almeno il 5-10% delle pagine generate prima della pubblicazione.
- **Rollout progressivo**: Pubblicare in lotti di 50-100 pagine. Monitorare indicizzazione e ranking per 2-4 settimane prima di espandersi. Mai pubblicare oltre 500 pagine contemporaneamente senza una revisione della qualità.
- **Test del valore autonomo**: Ogni pagina deve superare la domanda: "Varrebbe la pena pubblicare questa pagina anche se non esistessero altre pagine simili?".
- **Abuso della reputazione del sito**: Pubblicare contenuti programmatici sotto un dominio ad alta autorità (non proprio) può innescare penalità. Google ha iniziato a controllare questo aspetto aggressivamente a novembre 2024.

> **Raccomandazione**: La soglia di AVVISO al `<40% di contenuto unico` rimane appropriata. Considerare uno STOP al `<30%` per prevenire il rischio di abuso di contenuti su larga scala.

### Pagine Programmatiche Sicure (OK su larga scala)

✅ Pagine di integrazione (con documentazione reale di configurazione, dettagli API, screenshot).
✅ Pagine di template/strumenti (con contenuti scaricabili, istruzioni d'uso).
✅ Pagine di glossario (definizioni di oltre 200 parole con esempi, termini correlati).
✅ Pagine prodotto (specifiche uniche, recensioni, dati di confronto).
✅ Pagine basate sui dati (statistiche uniche, grafici, analisi per ogni record).

### Rischio Penalità (evitare su larga scala)

❌ Pagine località con solo il nome della città sostituito in testi identici.
❌ "Miglior [strumento] per [settore]" senza valore specifico per il settore.
❌ "Alternativa a [competitor]" senza dati reali di confronto.
❌ Pagine generate dall'AI senza revisione umana e valore aggiunto unico.
❌ Pagine dove oltre il 60% del contenuto è testo fisso del template.

### Calcolo dell'Univocità

% Contenuto Unico = (parole uniche per questa pagina) / (parole totali nella pagina) × 100

Misurare rispetto a tutte le altre pagine del set programmatico. Header, footer e navigazione condivisi sono esclusi dal calcolo. Il testo fisso del template È incluso.

## Strategia Canonical

- Ogni pagina programmatica deve avere un tag canonical autoreferenziale.
- Le varianti di parametri (ordinamento, filtri, paginazione) devono puntare all'URL di base.
- Serie paginate: canonical alla pagina 1 o uso di rel=next/prev.
- Se le pagine programmatiche si sovrappongono a pagine manuali, la pagina manuale è la canonica.
- Nessun canonical verso un dominio diverso a meno di configurazioni cross-domain intenzionali.

## Integrazione della Sitemap

- Generare automaticamente voci sitemap per tutte le pagine programmatiche.
- Dividere a 50.000 URL per file sitemap (limite del protocollo).
- Usare un indice delle sitemap se sono necessari più file.
- `<lastmod>` deve riflettere il timestamp di aggiornamento reale dei dati (non l'ora di generazione).
- Escludere dalla sitemap le pagine programmatiche con noindex.
- Registrare la sitemap nel file robots.txt.
- Aggiornare la sitemap dinamicamente man mano che nuovi record vengono aggiunti alla fonte dati.

## Prevenzione dell'Index Bloat

- **Noindex per pagine di basso valore**: Pagine che non soddisfano i quality gates.
- **Paginazione**: Noindex per i risultati paginati oltre la pagina 1 (o usare rel=next/prev).
- **Navigazione sfaccettata (Faceted navigation)**: Noindex per le viste filtrate, canonical alla categoria di base.
- **Budget di scansione (Crawl budget)**: Per siti con oltre 10.000 pagine programmatiche, monitorare le statistiche di scansione in Search Console.
- **Consolidamento pagine scarse**: Unire record con dati insufficienti in pagine aggregate.
- **Audit regolari**: Revisione mensile del numero di pagine indicizzate rispetto a quello previsto.

## Output

### Punteggio SEO Programmatica: XX/100

### Riepilogo della Valutazione

| Categoria            | Stato    | Punteggio   |
| -------------------- | -------- | ----------- |
| Qualità dei Dati     | ✅/⚠️/❌ | XX/100    |
| Univocità Template   | ✅/⚠️/❌ | XX/100    |
| Struttura URL        | ✅/⚠️/❌ | XX/100    |
| Linking Interno      | ✅/⚠️/❌ | XX/100    |
| Rischio Thin Content | ✅/⚠️/❌ | XX/100    |
| Gestione Indice      | ✅/⚠️/❌ | XX/100    |

### Problemi Critici (correggere immediatamente)

### Priorità Alta (correggere entro 1 settimana)

### Priorità Media (correggere entro 1 mese)

### Priorità Bassa (backlog)

### Raccomandazioni

- Miglioramenti della fonte dati.
- Modifiche al template.
- Adeguamenti dei pattern URL.
- Azioni per la conformità ai "quality gates".
