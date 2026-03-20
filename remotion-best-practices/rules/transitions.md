---
name: transitions
description: Transizioni di scena e overlay per Remotion usando TransitionSeries.
metadata:
  tags: transitions, overlays, fade, slide, wipe, scenes
---

## TransitionSeries

`<TransitionSeries>` organizza le scene e supporta due modi per migliorare il punto di stacco tra di esse:

- **Transitions** (`<TransitionSeries.Transition>`) — dissolvenza incrociata, scorrimento, scorrimento a tendina, ecc. tra due scene. Accorcia la timeline perché entrambe le scene vengono riprodotte simultaneamente durante la transizione.
- **Overlays** (`<TransitionSeries.Overlay>`) — renderizza un effetto (es. un light leak) sopra il punto di stacco senza accorciare la timeline.

I componenti figli sono posizionati in modo assoluto.

## Prerequisiti

```bash
npx remotion add @remotion/transitions
```

## Esempio di transizione

```tsx
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneA />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    presentation={fade()}
    timing={linearTiming({ durationInFrames: 15 })}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneB />
  </TransitionSeries.Sequence>
</TransitionSeries>;
```

## Esempio di overlay

Qualsiasi componente React può essere usato come overlay. Per un effetto pronto all'uso, vedi la regola **light-leaks**.

```tsx
import { TransitionSeries } from "@remotion/transitions";
import { LightLeak } from "@remotion/light-leaks";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneA />
  </TransitionSeries.Sequence>
  <TransitionSeries.Overlay durationInFrames={20}>
    <LightLeak />
  </TransitionSeries.Overlay>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneB />
  </TransitionSeries.Sequence>
</TransitionSeries>;
```

## Mischiare transizioni e overlay

Transizioni e overlay possono coesistere nella stessa `<TransitionSeries>`, ma un overlay non può essere adiacente a una transizione o a un altro overlay.

```tsx
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { LightLeak } from "@remotion/light-leaks";

<TransitionSeries>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneA />
  </TransitionSeries.Sequence>
  <TransitionSeries.Overlay durationInFrames={30}>
    <LightLeak />
  </TransitionSeries.Overlay>
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneB />
  </TransitionSeries.Sequence>
  <TransitionSeries.Transition
    presentation={fade()}
    timing={linearTiming({ durationInFrames: 15 })}
  />
  <TransitionSeries.Sequence durationInFrames={60}>
    <SceneC />
  </TransitionSeries.Sequence>
</TransitionSeries>;
```

## Prop della transizione

`<TransitionSeries.Transition>` richiede:

- `presentation` — l'effetto visivo (es. `fade()`, `slide()`, `wipe()`).
- `timing` — controlla la velocità e l'easing (es. `linearTiming()`, `springTiming()`).

## Prop dell'overlay

`<TransitionSeries.Overlay>` accetta:

- `durationInFrames` — per quanto tempo l'overlay è visibile (intero positivo).
- `offset?` — sposta l'overlay rispetto al centro del punto di stacco. Positivo = dopo, negativo = prima. Predefinito: `0`.

## Tipi di transizione disponibili

Importa le transizioni dai loro rispettivi moduli:

```tsx
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import { flip } from "@remotion/transitions/flip";
import { clockWipe } from "@remotion/transitions/clock-wipe";
```

## Transizione Slide con direzione

```tsx
import { slide } from "@remotion/transitions/slide";

<TransitionSeries.Transition
  presentation={slide({ direction: "from-left" })}
  timing={linearTiming({ durationInFrames: 20 })}
/>;
```

Direzioni: `"from-left"`, `"from-right"`, `"from-top"`, `"from-bottom"`

## Opzioni di temporizzazione (Timing)

```tsx
import { linearTiming, springTiming } from "@remotion/transitions";

// Temporizzazione lineare - velocità costante
linearTiming({ durationInFrames: 20 });

// Temporizzazione a molla - movimento organico
springTiming({ config: { damping: 200 }, durationInFrames: 25 });
```

## Calcolo della durata

Le transizioni sovrappongono scene adiacenti, quindi la lunghezza totale della composizione è **più breve** della somma di tutte le durate delle sequenze. Gli overlay **non** influenzano la durata totale.

Ad esempio, con due sequenze da 60 frame e una transizione da 15 frame:

- Senza transizioni: `60 + 60 = 120` frame
- Con transizione: `60 + 60 - 15 = 105` frame

Aggiungere un overlay tra altre due sequenze non cambia il totale.

### Ottenere la durata di una transizione

Usa il metodo `getDurationInFrames()` sull'oggetto timing:

```tsx
import { linearTiming, springTiming } from "@remotion/transitions";

const linearDuration = linearTiming({
  durationInFrames: 20,
}).getDurationInFrames({ fps: 30 });
// Restituisce 20

const springDuration = springTiming({
  config: { damping: 200 },
}).getDurationInFrames({ fps: 30 });
// Restituisce la durata calcolata in base alla fisica della molla
```

Per `springTiming` senza un `durationInFrames` esplicito, la durata dipende dagli `fps` perché calcola quando l'animazione della molla si stabilizza.

### Calcolare la durata totale della composizione

```tsx
import { linearTiming } from "@remotion/transitions";

const scene1Duration = 60;
const scene2Duration = 60;
const scene3Duration = 60;

const timing1 = linearTiming({ durationInFrames: 15 });
const timing2 = linearTiming({ durationInFrames: 20 });

const transition1Duration = timing1.getDurationInFrames({ fps: 30 });
const transition2Duration = timing2.getDurationInFrames({ fps: 30 });

const totalDuration =
  scene1Duration +
  scene2Duration +
  scene3Duration -
  transition1Duration -
  transition2Duration;
// 60 + 60 + 60 - 15 - 20 = 145 frame
```
