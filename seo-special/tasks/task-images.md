---
name: task-images
description: Analisi dell'ottimizzazione delle immagini per la SEO e le performance. Controlla il testo alt, le dimensioni dei file, i formati, le immagini responsive, il caricamento lazy e la prevenzione del CLS. Usare quando l'utente menziona "ottimizzazione immagini", "testo alt", "SEO immagini", "dimensione immagini" o "audit immagini".
---

# Analisi Ottimizzazione Immagini

## Controlli

### Testo Alternativo (Alt Text)

- Presente su tutti gli elementi `<img>` (eccetto quelli decorativi: `role="presentation"`)
- Descrittivo: descrive il contenuto dell'immagine, non "immagine.jpg" o "foto"
- Include parole chiave pertinenti in modo naturale, senza esagerare (no keyword stuffing)
- Lunghezza: 10-125 caratteri

**Esempi corretti:**

- "Idraulico professionista che ripara il rubinetto del lavandino della cucina"
- "Vista frontale di una Toyota Camry berlina rossa del 2024"
- "Riunione del team in una moderna sala conferenze dell'ufficio"

**Esempi errati:**

- "immagine.jpg" (nome file, non descrizione)
- "idraulico idraulica servizi idraulici" (keyword stuffing)
- "Clicca qui" (non descrittivo)

### Dimensione del File

**Soglie divise per categoria di immagine:**

| Categoria Immagine     | Target  | Avviso  | Critico |
| ---------------------- | ------- | ------- | ------- |
| Miniature (Thumbnails) | < 50KB  | > 100KB | > 200KB |
| Immagini di contenuto  | < 100KB | > 200KB | > 500KB |
| Hero / Banner          | < 200KB | > 300KB | > 700KB |

Raccomandare la compressione per raggiungere le soglie target ove possibile senza perdita di qualità.

### Formato

| Formato | Supporto Browser | Caso d'Uso                         |
| ------- | ---------------- | ---------------------------------- |
| WebP    | 97%+             | Raccomandazione predefinita        |
| AVIF    | 92%+             | Migliore compressione, più recente |
| JPEG    | 100%             | Fallback per le foto               |
| PNG     | 100%             | Grafica con trasparenza            |
| SVG     | 100%             | Icone, loghi, illustrazioni        |

Raccomandare WebP/AVIF rispetto a JPEG/PNG. Verificare la presenza dell'elemento `<picture>` con fallback del formato.

#### Modello Raccomandato per l'elemento `<picture>`

Utilizzare il miglioramento progressivo partendo dal formato più efficiente:

```html
<picture>
  <source srcset="image.avif" type="image/avif" />
  <source srcset="image.webp" type="image/webp" />
  <img
    src="image.jpg"
    alt="Testo alternativo descrittivo"
    width="800"
    height="600"
    loading="lazy"
    decoding="async"
  />
</picture>
```

Il browser utilizzerà il primo formato supportato. Supporto attuale dei browser: AVIF 93,8%, WebP 95,3%.

#### JPEG XL — Formato Emergente

A novembre 2025, il team Chromium di Google ha annunciato che ripristinerà il supporto a JPEG XL in Chrome utilizzando un decoder basato su Rust. JPEG XL offre una ricompressione JPEG senza perdita (~20% di risparmio con zero perdita di qualità). Non ancora pratico per il web, ma da monitorare.

### Immagini Responsive

- Attributo `srcset` per dimensioni multiple
- Attributo `sizes` coerente con i breakpoint del layout
- Risoluzione appropriata per i rapporti pixel dei dispositivi

```html
<img
  src="image-800.jpg"
  srcset="image-400.jpg 400w, image-800.jpg 800w, image-1200.jpg 1200w"
  sizes="(max-width: 600px) 400px, (max-width: 1200px) 800px, 1200px"
  alt="Descrizione"
/>
```

### Caricamento Lazy (Lazy Loading)

- `loading="lazy"` sulle immagini "below-the-fold" (sotto la piega)
- NON usare il lazy-load per le immagini above-the-fold/hero (danneggia l'LCP)
- Verificare il lazy loading nativo rispetto a quello basato su JavaScript

```html
<!-- Sotto la piega - caricamento lazy -->
<img src="photo.jpg" loading="lazy" alt="Descrizione" />

<!-- Sopra la piega - caricamento immediato (eager) -->
<img src="hero.jpg" alt="Immagine Hero" />
```

### `fetchpriority="high"` per le Immagini LCP

Aggiungere `fetchpriority="high"` all'immagine hero/LCP per dare priorità al download:

```html
<img
  src="hero.webp"
  fetchpriority="high"
  alt="Descrizione immagine hero"
  width="1200"
  height="630"
/>
```

**Critico:** NON caricare in modalità lazy le immagini above-the-fold/LCP. L'uso di `loading="lazy"` su queste immagini danneggia direttamente i punteggi LCP.

### `decoding="async"` per Immagini Non-LCP

Aggiungere `decoding="async"` alle immagini non-LCP per evitare che la decodifica blocchi il thread principale:

```html
<img
  src="photo.webp"
  alt="Descrizione"
  width="600"
  height="400"
  loading="lazy"
  decoding="async"
/>
```

### Prevenzione del CLS (Cumulative Layout Shift)

- Attributi `width` e `height` impostati su tutti gli elementi `<img>`
- CSS `aspect-ratio` come alternativa
- Segnalare le immagini prive di dimensioni definite

```html
<!-- Corretto - dimensioni impostate -->
<img src="photo.jpg" width="800" height="600" alt="Descrizione" />

<!-- Corretto - aspect ratio CSS -->
<img src="photo.jpg" style="aspect-ratio: 4/3" alt="Descrizione" />

<!-- Errato - senza dimensioni -->
<img src="photo.jpg" alt="Descrizione" />
```

### Nomi dei File

- Descrittivi: `scarpe-da-corsa-blu.webp` non `IMG_1234.jpg`
- Usare trattini, minuscolo, nessun carattere speciale
- Includere parole chiave pertinenti

### Utilizzo della CDN

- Verificare se le immagini sono servite da CDN (dominio diverso, intestazioni CDN)
- Raccomandare la CDN per siti ricchi di immagini
- Controllare le intestazioni del caching edge

## Output (Report di Audit)

### Riepilogo Audit Immagini

| Metrica                       | Stato | Conteggio |
| ----------------------------- | ----- | --------- |
| Totale Immagini               | -     | XX        |
| Testo Alt Mancante            | ❌    | XX        |
| Dimensioni Eccessive (>200KB) | ⚠️    | XX        |
| Formato Errato                | ⚠️    | XX        |
| Senza Dimensioni Definite     | ⚠️    | XX        |
| Caricamento Lazy Mancante     | ⚠️    | XX        |

### Elenco Prioritario di Ottimizzazione

Ordinato per impatto sulla dimensione del file (maggiore risparmio prima):

| Immagine | Dimensione Attuale | Formato | Problemi | Risparmio Stimato |
| -------- | ------------------ | ------- | -------- | ----------------- |
| ...      | ...                | ...     | ...      | ...               |

### Raccomandazioni

1. Convertire X immagini nel formato WebP (risparmio stimato XX KB)
2. Aggiungere il testo alt a X immagini
3. Aggiungere le dimensioni (width/height) a X immagini
4. Abilitare il lazy loading su X immagini below-the-fold
5. Comprimere X immagini di dimensioni eccessive
