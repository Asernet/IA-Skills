---
name: trimming
description: Pattern di ritaglio per Remotion - tagliare l'inizio o la fine delle animazioni
metadata:
  tags: sequence, trim, clip, cut, offset
---

Usa `<Sequence>` con un valore `from` negativo per ritagliare l'inizio di un'animazione.

## Ritagliare l'inizio

Un valore `from` negativo sposta il tempo all'indietro, facendo iniziare l'animazione a metà percorso:

```tsx
import { Sequence, useVideoConfig } from "remotion";

const fps = useVideoConfig();

<Sequence from={-0.5 * fps}>
  <MyAnimation />
</Sequence>;
```

L'animazione appare 15 frame dopo l'inizio del suo progresso: i primi 15 frame vengono ritagliati.
All'interno di `<MyAnimation>`, `useCurrentFrame()` inizia da 15 invece che da 0.

## Ritagliare la fine

Usa `durationInFrames` per smontare (unmount) il contenuto dopo una durata specifica:

```tsx
<Sequence durationInFrames={1.5 * fps}>
  <MyAnimation />
</Sequence>
```

L'animazione viene riprodotta per 45 frame, dopodiché il componente viene rimosso.

## Ritagliare e Ritardare

Nidifica le sequenze sia per ritagliare l'inizio che per ritardare la comparsa:

```tsx
<Sequence from={30}>
  <Sequence from={-15}>
    <MyAnimation />
  </Sequence>
</Sequence>
```

La sequenza interna ritaglia 15 frame dall'inizio, e la sequenza esterna ritarda il risultato di 30 frame.
