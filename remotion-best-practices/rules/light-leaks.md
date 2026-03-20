---
name: light-leaks
description: Effetti di overlay light leak per Remotion usando @remotion/light-leaks.
metadata:
  tags: light-leaks, overlays, effects, transitions
---

## Light Leaks

Funziona solo da Remotion 4.0.415 in su. Usa `npx remotion versions` per controllare la tua versione di Remotion e `npx remotion upgrade` per aggiornarla.

`<LightLeak>` da `@remotion/light-leaks` renderizza un effetto light leak basato su WebGL. Si rivela durante la prima metà della sua durata e si ritrae durante la seconda metà.

Viene tipicamente utilizzato all'interno di un `<TransitionSeries.Overlay>` per essere riprodotto sopra il punto di stacco tra due scene. Vedi la regola **transitions** per l'uso di `<TransitionSeries>` e degli overlay.

## Prerequisiti

```bash
npx remotion add @remotion/light-leaks
```

## Utilizzo di base con TransitionSeries

```tsx
import { TransitionSeries } from "@remotion/transitions";
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
</TransitionSeries>;
```

## Props

- `durationInFrames?` — predefinito sulla durata della sequenza/composizione genitore. L'effetto si rivela durante la prima metà e si ritrae durante la seconda metà.
- `seed?` — determina la forma del pattern del light leak. Seed diversi producono pattern diversi. Predefinito: `0`.
- `hueShift?` — ruota la tonalità in gradi (`0`–`360`). Predefinito: `0` (da giallo a arancione). `120` = verde, `240` = blu.

## Personalizzare l'aspetto

```tsx
import { LightLeak } from "@remotion/light-leaks";

// Light leak con tonalità blu e un pattern diverso
<LightLeak seed={5} hueShift={240} />;

// Light leak con tonalità verde
<LightLeak seed={2} hueShift={120} />;
```

## Utilizzo standalone

`<LightLeak>` può essere usato anche al di fuori di `<TransitionSeries>`, ad esempio come overlay decorativo in qualsiasi composizione:

```tsx
import { AbsoluteFill } from "remotion";
import { LightLeak } from "@remotion/light-leaks";

const MyComp: React.FC = () => (
  <AbsoluteFill>
    <MyContent />
    <LightLeak durationInFrames={60} seed={3} />
  </AbsoluteFill>
);
```
