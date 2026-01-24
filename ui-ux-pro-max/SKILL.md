---
name: ui-ux-pro-max
description: Intelligenza di design UI/UX avanzata. Genera palette, font pairing e codice per interfacce moderne e accessibili.
---

# UI/UX Pro Max - Intelligence Design

Database ricercabile di stili UI, palette colori, accoppiamenti font, tipi grafico, raccomandazioni prodotto, linee guida UX e best practice specifiche per stack.

## Prerequisiti

Controlla se Python è installato:

```bash
python3 --version || python --version
```

Se Python non è installato, installalo basato sull'OS dell'utente.

## Come Usare Questa Skill

Quando l'utente richiede lavoro UI/UX (design, build, create, implement, review, fix, improve), segui questo workflow:

### Passo 1: Analizza Requisiti Utente

Estrai informazioni chiave dalla richiesta utente:

- **Tipo prodotto**: SaaS, e-commerce, portfolio, dashboard, landing page, ecc.
- **Keyword stile**: minimal, playful, professional, elegant, dark mode, ecc.
- **Industria**: healthcare, fintech, gaming, education, ecc.
- **Stack**: React, Vue, Next.js, o default a `html-tailwind`

### Passo 2: Cerca Domini Rilevanti

Usa `search.py` più volte per raccogliere informazioni comprensive. Cerca finché hai abbastanza contesto.

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --domain <domain> [-n <max_results>]
```

**Ordine ricerca raccomandato:**

1. **Product** - Ottieni raccomandazioni stile per tipo prodotto
2. **Style** - Ottieni guida stile dettagliata (colori, effetti, framework)
3. **Typography** - Ottieni accoppiamenti font con import Google Fonts
4. **Color** - Ottieni palette colori (Primary, Secondary, CTA, Background, Text, Border)
5. **Landing** - Ottieni struttura pagina (se landing page)
6. **Chart** - Ottieni raccomandazioni grafico (se dashboard/analytics)
7. **UX** - Ottieni best practice e anti-pattern
8. **Stack** - Ottieni linee guida specifiche stack (default: html-tailwind)

### Passo 3: Linee Guida Stack (Default: html-tailwind)

Se l'utente non specifica uno stack, **default a `html-tailwind`**.

```bash
python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<keyword>" --stack html-tailwind
```

Stack disponibili: `html-tailwind`, `react`, `nextjs`, `vue`, `svelte`, `swiftui`, `react-native`, `flutter`

---

## Riferimento Ricerca

### Domini Disponibili

| Dominio      | Usa Per                                | Esempi Keyword                                           |
| ------------ | -------------------------------------- | -------------------------------------------------------- |
| `product`    | Raccomandazioni tipo prodotto          | SaaS, e-commerce, portfolio, healthcare, beauty, service |
| `style`      | Stili UI, colori, effetti              | glassmorphism, minimalism, dark mode, brutalism          |
| `typography` | Accoppiamenti font, Google Fonts       | elegant, playful, professional, modern                   |
| `color`      | Palette colori per tipo prodotto       | saas, ecommerce, healthcare, beauty, fintech, service    |
| `landing`    | Struttura pagina, strategie CTA        | hero, hero-centric, testimonial, pricing, social-proof   |
| `chart`      | Tipi grafico, raccomandazioni librerie | trend, comparison, timeline, funnel, pie                 |
| `ux`         | Best practice, anti-pattern            | animation, accessibility, z-index, loading               |
| `prompt`     | Prompt AI, keyword CSS                 | (nome stile)                                             |

### Stack Disponibili

| Stack           | Focus                                        |
| --------------- | -------------------------------------------- |
| `html-tailwind` | Utility Tailwind, responsive, a11y (DEFAULT) |
| `react`         | State, hooks, performance, pattern           |
| `nextjs`        | SSR, routing, immagini, API route            |
| `vue`           | Composition API, Pinia, Vue Router           |
| `svelte`        | Runes, stores, SvelteKit                     |
| `swiftui`       | View, State, Navigation, Animation           |
| `react-native`  | Componenti, Navigation, Liste                |
| `flutter`       | Widget, State, Layout, Theming               |

---

## Suggerimenti per Risultati Migliori

1. **Sii specifico con keyword** - "healthcare SaaS dashboard" > "app"
2. **Cerca più volte** - Keyword diverse rivelano insight diversi
3. **Combina domini** - Style + Typography + Color = Sistema design completo
4. **Controlla sempre UX** - Cerca "animation", "z-index", "accessibility" per problemi comuni
5. **Usa flag stack** - Ottieni best practice specifiche implementazione
6. **Itera** - Se la prima ricerca non combacia, prova keyword diverse

---

## Regole Comuni per UI Professionale

Questi sono problemi frequentemente trascurati che rendono la UI non professionale:

### Icone & Elementi Visivi

| Regola                                | Fai                                             | Non Fare                                        |
| ------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| **No icon emoji**                     | Usa icone SVG (Heroicons, Lucide, Simple Icons) | Usa emoji come 🎨 🚀 ⚙️ come icone UI           |
| **Stati hover stabili**               | Usa transizioni colore/opacità su hover         | Usa trasformazioni scala che spostano il layout |
| **Loghi brand corretti**              | Ricerca SVG ufficiali da Simple Icons           | Indovina o usa percorsi logo non corretti       |
| **Dimensionamento icone consistente** | Usa viewBox fisso (24x24) con w-6 h-6           | Mischia dimensioni icone diverse a caso         |

### Interazione & Cursore

| Regola                 | Fai                                                             | Non Fare                                       |
| ---------------------- | --------------------------------------------------------------- | ---------------------------------------------- |
| **Puntatore cursore**  | Aggiungi `cursor-pointer` a tutte le card cliccabili/hoverabili | Lascia cursore default su elementi interattivi |
| **Feedback hover**     | Fornisci feedback visivo (colore, ombra, bordo)                 | Nessuna indicazione elemento è interattivo     |
| **Transizioni fluide** | Usa `transition-colors duration-200`                            | Cambi stato istantanei o troppo lenti (>500ms) |

### Contrasto Light/Dark Mode

| Regola                    | Fai                                  | Non Fare                                  |
| ------------------------- | ------------------------------------ | ----------------------------------------- |
| **Card glass light mode** | Usa `bg-white/80` o opacità maggiore | Usa `bg-white/10` (troppo trasparente)    |
| **Contrasto testo light** | Usa `#0F172A` (slate-900) per testo  | Usa `#94A3B8` (slate-400) per testo corpo |
| **Testo muto light**      | Usa `#475569` (slate-600) minimo     | Usa gray-400 o più chiaro                 |
| **Visibilità bordo**      | Usa `border-gray-200` in light mode  | Usa `border-white/10` (invisibile)        |

### Layout & Spaziatura

| Regola                    | Fai                                        | Non Fare                                           |
| ------------------------- | ------------------------------------------ | -------------------------------------------------- |
| **Navbar fluttuante**     | Aggiungi spaziatura `top-4 left-4 right-4` | Attacca navbar a `top-0 left-0 right-0`            |
| **Padding contenuto**     | Tieni conto dell'altezza fissa navbar      | Lascia contenuto nascondersi dietro elementi fissi |
| **Max-width consistente** | Usa stesso `max-w-6xl` o `max-w-7xl`       | Mischia larghezze container diverse                |

---

## Checklist Pre-Consegna

Prima di consegnare codice UI, verifica questi item:

### Qualità Visiva

- [ ] Nessuna emoji usata come icona (usa SVG invece)
- [ ] Tutte le icone da set icone consistente (Heroicons/Lucide)
- [ ] Loghi brand sono corretti (verificati da Simple Icons)
- [ ] Stati hover non causano spostamento layout
- [ ] Usa colori tema direttamente (bg-primary) non wrapper var()

### Interazione

- [ ] Tutti gli elementi cliccabili hanno `cursor-pointer`
- [ ] Stati hover forniscono feedback visivo chiaro
- [ ] Transizioni sono fluide (150-300ms)
- [ ] Stati focus visibili per navigazione tastiera

### Light/Dark Mode

- [ ] Testo light mode ha contrasto sufficiente (4.5:1 minimo)
- [ ] Elementi Glass/trasparenti visibili in light mode
- [ ] Bordi visibili in entrambe le modalità
- [ ] Testa entrambe le modalità prima della consegna

### Layout

- [ ] Elementi fluttuanti hanno spaziatura appropriata dai bordi
- [ ] Nessun contenuto nascosto dietro navbar fisse
- [ ] Responsive a 320px, 768px, 1024px, 1440px
- [ ] Nessun scroll orizzontale su mobile

### Accessibilità

- [ ] Tutte le immagini hanno alt text
- [ ] Input form hanno label
- [ ] Il colore non è l'unico indicatore
- [ ] `prefers-reduced-motion` rispettato
