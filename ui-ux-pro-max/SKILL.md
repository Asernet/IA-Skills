---
name: ui-ux-pro-max
description: "Intelligenza di design UI/UX. 50 stili, 21 palette, 50 abbinamenti di font, 20 grafici, 9 stack (React, Next.js, Vue, Svelte, SwiftUI, React Native, Flutter, Tailwind, shadcn/ui). Azioni: pianifica, costruisci, crea, progetta, implementa, rivedi, correggi, migliora, ottimizza, potenzia, rifattorizza, controlla il codice UI/UX. Progetti: sito web, landing page, dashboard, pannello di amministrazione, e-commerce, SaaS, portfolio, blog, app mobile, .html, .tsx, .vue, .svelte. Elementi: pulsante, modale, navbar, barra laterale, scheda, tabella, modulo, grafico. Stili: glassmorphism, claymorphism, minimalismo, brutalismo, neumorphism, bento grid, dark mode, responsive, skeuomorphism, flat design. Argomenti: palette colori, accessibilità, animazione, layout, tipografia, abbinamento font, spaziatura, hover, ombra, sfumatura. Integrazioni: shadcn/ui MCP per ricerca componenti ed esempi."
---

# UI/UX Pro Max - Design Intelligence

Guida completa al design per applicazioni web e mobile. Contiene 50+ stili, 97 palette di colori, 57 abbinamenti di font, 99 linee guida UX e 25 tipi di grafici su 9 stack tecnologici. Database ricercabile con raccomandazioni basate sulla priorità.

## Ruolo

Agisci come un esperto di UI/UX Design System. Fai riferimento a queste linee guida quando:

- Progetti nuovi componenti UI o pagine
- Scegli palette di colori e tipografia
- Rivedi il codice per problemi di UX
- Costruisci landing page o dashboard
- Implementi requisiti di accessibilità

## Categorie di Regole per Priorità

| Priorità | Categoria           | Impatto | Dominio               |
| -------- | ------------------- | ------- | --------------------- |
| 1        | Accessibilità       | CRITICO | `ux`                  |
| 2        | Tocco & Interazione | CRITICO | `ux`                  |
| 3        | Performance         | ALTO    | `ux`                  |
| 4        | Layout & Responsive | ALTO    | `ux`                  |
| 5        | Tipografia & Colore | MEDIO   | `typography`, `color` |
| 6        | Animazione          | MEDIO   | `ux`                  |
| 7        | Selezione Stile     | MEDIO   | `style`, `product`    |
| 8        | Grafici & Dati      | BASSO   | `chart`               |

## Istruzioni Operative

### Riferimento Rapido

#### 1. Accessibilità (CRITICO)

- `color-contrast` - Rapporto minimo 4.5:1 per testo normale
- `focus-states` - Anelli di focus visibili sugli elementi interattivi
- `alt-text` - Testo alternativo descrittivo per immagini significative
- `aria-labels` - aria-label per pulsanti solo icona
- `keyboard-nav` - L'ordine di tabulazione corrisponde all'ordine visivo
- `form-labels` - Usa label con attributo for

#### 2. Tocco & Interazione (CRITICO)

- `touch-target-size` - Target tattili minimi di 44x44px
- `hover-vs-tap` - Usa click/tap per interazioni primarie
- `loading-buttons` - Disabilita il pulsante durante operazioni asincrone
- `error-feedback` - Messaggi di errore chiari vicino al problema
- `cursor-pointer` - Aggiungi cursor-pointer agli elementi cliccabili

#### 3. Performance (ALTO)

- `image-optimization` - Usa WebP, srcset, lazy loading
- `reduced-motion` - Controlla prefers-reduced-motion
- `content-jumping` - Riserva spazio per contenuto asincrono

#### 4. Layout & Responsive (ALTO)

- `viewport-meta` - width=device-width initial-scale=1
- `readable-font-size` - Minimo 16px testo body su mobile
- `horizontal-scroll` - Assicura che il contenuto rientri nella larghezza della viewport
- `z-index-management` - Definisci scala z-index (10, 20, 30, 50)

#### 5. Tipografia & Colore (MEDIO)

- `line-height` - Usa 1.5-1.75 per testo body
- `line-length` - Limita a 65-75 caratteri per riga
- `font-pairing` - Abbina personalità font intestazione/body

#### 6. Animazione (MEDIO)

- `duration-timing` - Usa 150-300ms per micro-interazioni
- `transform-performance` - Usa transform/opacity, non width/height
- `loading-states` - Skeleton screens o spinner

#### 7. Selezione Stile (MEDIO)

- `style-match` - Abbina lo stile al tipo di prodotto
- `consistency` - Usa lo stesso stile su tutte le pagine
- `no-emoji-icons` - Usa icone SVG, non emoji

#### 8. Grafici & Dati (BASSO)

- `chart-type` - Abbina tipo di grafico al tipo di dati
- `color-guidance` - Usa palette di colori accessibili
- `data-table` - Fornisci alternativa tabellare per accessibilità

### Workflow di Utilizzo

Quando l'utente richiede lavoro UI/UX (design, build, create, implement, review, fix, improve), segui questo flusso:

#### Passo 1: Analizza Requisiti Utente

Estrai informazioni chiave dalla richiesta utente:

- **Tipo prodotto**: SaaS, e-commerce, portfolio, dashboard, landing page, ecc.
- **Parole chiave stile**: minimal, playful, professional, elegant, dark mode, ecc.
- **Settore**: healthcare, fintech, gaming, education, ecc.
- **Stack**: React, Vue, Next.js, o default `html-tailwind`

#### Passo 2: Genera Design System (RICHIESTO)

**Inizia sempre con `--design-system`** per raccomandazioni complete con ragionamento:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<product_type> <industry> <keywords>" --design-system [-p "Nome Progetto"]
```

Questo comando:

1. Cerca in 5 domini in parallelo (product, style, color, landing, typography)
2. Applica regole di ragionamento da `ui-reasoning.csv` per selezionare le corrispondenze migliori
3. Restituisce design system completo: pattern, stile, colori, tipografia, effetti
4. Include anti-pattern da evitare

**Esempio:**

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "beauty spa wellness service" --design-system -p "Serenity Spa"
```

#### Passo 2b: Persistenza Design System (Master + Overrides Pattern)

Per salvare il design system per **recupero gerarchico tra sessioni**, aggiungi `--persist`:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Nome Progetto"
```

Questo crea:

- `design-system/MASTER.md` — Fonte di Verità Globale con tutte le regole di design
- `design-system/pages/` — Cartella per override specifici per pagina

**Con override specifico per pagina:**

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<query>" --design-system --persist -p "Nome Progetto" --page "dashboard"
```

#### Passo 3: Supplemento con Ricerche Dettagliate (se necessario)

Dopo aver ottenuto il design system, usa ricerche di dominio per dettagli aggiuntivi:

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

| Bisogno                 | Dominio      | Esempio                                 |
| ----------------------- | ------------ | --------------------------------------- |
| Più opzioni stile       | `style`      | `--domain style "glassmorphism dark"`   |
| Raccomandazioni grafici | `chart`      | `--domain chart "real-time dashboard"`  |
| Best practice UX        | `ux`         | `--domain ux "animation accessibility"` |
| Font alternativi        | `typography` | `--domain typography "elegant luxury"`  |
| Struttura landing       | `landing`    | `--domain landing "hero social-proof"`  |

#### Passo 4: Linee Guida Stack (Default: html-tailwind)

Ottieni best practice specifiche per l'implementazione. Se l'utente non specifica uno stack, **usa default `html-tailwind`**.

```bash
python3 skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

Stack disponibili: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`, `shadcn`, `jetpack-compose`

## Vincoli

Questi sono problemi spesso trascurati che rendono la UI non professionale:

### Icone & Elementi Visivi

- **NON usare emoji come icone**: Usa icone SVG (Heroicons, Lucide, Simple Icons).
- **NON usare loghi errati**: Ricerca SVG ufficiali da Simple Icons.
- **Stati hover stabili**: Usa transizioni colore/opacità, NON trasformazioni di scala che spostano il layout.
- **Dimensioni icone consistenti**: Usa viewBox fissi (24x24) con w-6 h-6.

### Interazione & Cursore

- **Cursore pointer**: Aggiungi `cursor-pointer` a tutte le schede cliccabili/hoverable.
- **Feedback hover**: Fornisci feedback visivo (colore, ombra, bordo).
- **Transizioni fluide**: Usa `transition-colors duration-200`. NIENTE cambi di stato istantanei o troppo lenti.

### Contrasto Light/Dark Mode

- **Glass card light mode**: Usa `bg-white/80` o opacità maggiore. NON `bg-white/10` (troppo trasparente).
- **Testo contrasto light**: Usa `#0F172A` (slate-900) per testo. NON `#94A3B8` (slate-400) per testo body.
- **Testo muted light**: Usa `#475569` (slate-600) minimo.
- **Visibilità bordi**: Usa `border-gray-200` in light mode.

### Layout & Spaziatura

- **Navbar fluttuante**: Aggiungi spaziatura `top-4 left-4 right-4`. NON attaccare navbar a `top-0 left-0 right-0`.
- **Padding contenuto**: Considera altezza navbar fissa.
- **Max-width consistente**: Usa stesso `max-w-6xl` o `max-w-7xl`.

## Checklist Pre-Consegna

Prima di consegnare codice UI, verifica questi elementi:

- [ ] Niente emoji usate come icone (usa SVG invece)
- [ ] Tutte le icone da set consistente (Heroicons/Lucide)
- [ ] Loghi brand corretti (verificati da Simple Icons)
- [ ] Stati hover non causano shift del layout
- [ ] Usa colori del tema direttamente (bg-primary) non wrapper var()
- [ ] Tutti gli elementi cliccabili hanno `cursor-pointer`
- [ ] Stati hover forniscono feedback visivo chiaro
- [ ] Transizioni sono fluide (150-300ms)
- [ ] Stati focus visibili per navigazione tastiera
- [ ] Testo light mode ha contrasto sufficiente (4.5:1 minimo)
- [ ] Elementi glass/trasparenti visibili in light mode
- [ ] Bordi visibili in entrambe le modalità
- [ ] Test entrambe le modalità prima della consegna
- [ ] Elementi fluttuanti hanno spaziatura appropriata dai bordi
- [ ] Niente contenuto nascosto dietro navbar fisse
- [ ] Responsive a 375px, 768px, 1024px, 1440px
- [ ] Niente scroll orizzontale su mobile
- [ ] Tutte le immagini hanno alt text
- [ ] Input form hanno label
- [ ] Il colore non è l'unico indicatore
- [ ] `prefers-reduced-motion` rispettato
