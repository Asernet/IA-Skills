---
name: task-images
description: Ottimizzazione immagini con focus su performance (fetchpriority, WebP/AVIF, CLS).
---

# Ottimizzazione Immagini Avanzata

## Analisi Tecnica
- **fetchpriority="high":** Obbligatorio per immagini hero/LCP. NON usare lazy loading su queste.
- **loading="lazy":** Solo per immagini below-the-fold.
- **decoding="async":** Per immagini non-LCP per non bloccare il thread principale.
- **JPEG XL:** Supporto ripristinato in Chromium (Nov 2025); monitorare per adozione futura.

## Soglie di Peso (KB)
| Categoria | Target | Avviso | Critico |
|-----------|--------|--------|---------|
| Thumbnail | < 50KB | > 100KB | > 200KB |
| Contenuto | < 100KB| > 200KB | > 500KB |
| Hero/Banner| < 200KB| > 300KB | > 700KB |

## Formato Output
- Report con risparmio stimato in KB.
- Elenco immagini critiche e raccomandazioni alt text (10-125 caratteri).
