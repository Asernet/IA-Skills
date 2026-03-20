<!-- Aggiornato: 2026-02-07 -->

# Soglie Core Web Vitals (Febbraio 2026)

## Metriche Attuali

| Metrica                         | Buono  | Necessita Miglioramento | Scarso |
| ------------------------------- | ------ | ----------------------- | ------ |
| LCP (Largest Contentful Paint)  | ≤2.5s  | 2.5s–4.0s               | >4.0s  |
| INP (Interaction to Next Paint) | ≤200ms | 200ms–500ms             | >500ms |
| CLS (Cumulative Layout Shift)   | ≤0.1   | 0.1–0.25                | >0.25  |

## Fatti Chiave

- L'INP ha sostituito il FID (First Input Delay) il **12 marzo 2024**. Il FID è stato completamente rimosso da tutti gli strumenti Chrome (CrUX API, PageSpeed Insights, Lighthouse) il **9 settembre 2024**. L'INP è l'unica metrica di interattività.
- La valutazione utilizza il **75° percentile** dei dati degli utenti reali (dati di campo da CrUX).
- Google valuta a **livello di pagina** e a **livello di origine**.
- I Core Web Vitals sono un segnale di ranking **"tiebreaker"** (di spareggio) — contano soprattutto quando la qualità dei contenuti è simile tra i concorrenti.
- **Soglie invariate rispetto alle definizioni originali** — ignorare le affermazioni di "soglie ristrette" dai blog SEO.
- L'aggiornamento core di dicembre 2025 sembra aver dato un peso maggiore ai **CWV mobile**.
- A ottobre 2025: il **57,1%** dei siti desktop e il **49,7%** dei siti mobile superano tutti e tre i CWV.

## Sottoparti LCP (Aggiunta CrUX Febbraio 2025)

L'LCP può ora essere suddiviso in sottoparti diagnostiche:

| Sottoparte               | Cosa Misura                                       | Target                   |
| ------------------------ | ------------------------------------------------- | ------------------------ |
| **TTFB**                 | Time to First Byte (risposta del server)          | <800ms                   |
| **Resource Load Delay**  | Tempo dal TTFB all'inizio della richiesta risorsa | Minimizzare              |
| **Resource Load Time**   | Tempo per scaricare la risorsa LCP                | Dipende dalla dimensione |
| **Element Render Delay** | Tempo dal caricamento della risorsa al rendering  | Minimizzare              |

**LCP Totale = TTFB + Resource Load Delay + Resource Load Time + Element Render Delay**

Usa questa suddivisione per identificare quale fase sta causando problemi di LCP.

## Soft Navigations API (Sperimentale)

**Chrome 139+ Origin Trial (Luglio 2025)** — Primo passo verso la misurazione dei CWV nelle SPA (Single Page Applications).

- Risolve la storica lacuna nella misurazione delle SPA
- Attualmente sperimentale, **nessun impatto sul ranking ancora**
- Rileva le "navigazioni soft" (cambiamenti di URL senza caricamento completo della pagina)
- Potrebbe influenzare la futura misurazione dei CWV per le SPA

**Rilevamento:** Verificare la presenza di framework SPA (React, Vue, Angular, Svelte) e avvisare sulle attuali limitazioni della misurazione dei CWV.

## Fonti di Misurazione

### Dati di Campo (Utenti Reali)

- Chrome User Experience Report (CrUX)
- PageSpeed Insights (utilizza i dati CrUX)
- Rapporto Core Web Vitals di Search Console

### Dati di Laboratorio (Simulati)

- Lighthouse
- WebPageTest
- Chrome DevTools

> I dati di campo sono ciò che Google usa per il ranking. I dati di laboratorio sono utili per il debug.

## Colli di Bottiglia Comuni

### LCP (Largest Contentful Paint)

- Immagini hero non ottimizzate (comprimere, usare WebP/AVIF, aggiungere preload)
- CSS/JS che bloccano il rendering (defer, async, inlining del CSS critico)
- Risposta del server lenta (TTFB >200ms — usare edge CDN, caching)
- Blocco da script di terze parti (ritardare analytics, widget di chat)
- Ritardo nel caricamento dei web font (usare font-display: swap + preload)

### INP (Interaction to Next Paint)

- Task JavaScript lunghi sul thread principale (suddividere in task più piccoli <50ms)
- Gestori di eventi pesanti (usare debounce, requestAnimationFrame)
- Dimensione DOM eccessiva (>1.500 elementi è preoccupante)
- Script di terze parti che occupano il thread principale
- Operazioni sincrone XHR o localStorage
- Layout thrashing (molteplici reflow forzati)

### CLS (Cumulative Layout Shift)

- Immagini/iframe senza dimensioni width/height
- Contenuto iniettato dinamicamente sopra il contenuto esistente
- Web font che causano layout shift (usare font-display: swap + preload)
- Annunci/embed senza spazio riservato
- Caricamento tardivo di contenuti che spostano la pagina verso il basso

## Priorità di Ottimizzazione

1. **LCP** — Massimo impatto per le prestazioni percepite
2. **CLS** — Problema più comune che influisce sull'esperienza utente
3. **INP** — Fondamentale per le applicazioni interattive

## Strumenti

```bash
# PageSpeed Insights API
curl "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=URL&key=API_KEY"

# Lighthouse CLI
npx lighthouse URL --output json --output-path report.json
```

## Aggiornamenti Strumenti Performance (2025)

- **Lighthouse 13.0** (Ottobre 2025): Ristrutturazione completa dell'audit con categorie di performance riorganizzate e pesi dello scoring aggiornati. Lighthouse è uno strumento di laboratorio (condizioni simulate) — confrontare sempre con i dati di campo CrUX per le prestazioni reali.
- **CrUX Vis** ha sostituito la dashboard CrUX (Novembre 2025). La vecchia dashboard di Looker Studio è stata deprecata. Usare [CrUX Vis](https://cruxvis.withgoogle.com) o direttamente l'API CrUX.
- **Sottoparti LCP** aggiunte a CrUX (Febbraio 2025): Time to First Byte (TTFB), ritardo di caricamento risorsa (resource load delay), tempo di caricamento risorsa (resource load time) e ritardo di rendering dell'elemento (element render delay) sono ora disponibili come sottocomponenti di LCP nei dati CrUX.
- **Funzionalità Google Search Console 2025** (Dicembre 2025): Configurazione potenziata dall'AI per l'analisi automatizzata. Filtro per query branded vs non-branded. Dati orari disponibili nell'API. Annotazioni personalizzate sui grafici. Monitoraggio dei canali social.

> **L'indicizzazione mobile-first** è completa al 100% dal 5 luglio 2024. Google ora scansiona e indicizza TUTTI i siti web esclusivamente con lo user-agent mobile Googlebot. Assicurati che la tua versione mobile contenga tutti i contenuti critici, i dati strutturati e i meta tag.
