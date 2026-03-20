---
name: sequencing
description: Pattern di sequenziamento per Remotion - ritardi, ritagli, limite di durata degli elementi
metadata:
  tags: sequence, series, timing, delay, trim
---

Usa `<Sequence>` per ritardare il momento in cui un elemento appare nella timeline.

```tsx
import { Sequence } from "remotion";

const {fps} = useVideoConfig();

<Sequence from={1 * fps} durationInFrames={2 * fps} premountFor={1 * fps}>
  <Title />
</Sequence>
<Sequence from={2 * fps} durationInFrames={2 * fps} premountFor={1 * fps}>
  <Subtitle />
</Sequence>
```

Per impostazione predefinita, questo avvolgerà il componente in un elemento absolute fill.  
Se gli elementi non devono essere avvolti, usa la prop `layout`:

```tsx
<Sequence layout="none">
  <Title />
</Sequence>
```

## Premounting (pre-caricamento)

Questo carica il componente nella timeline prima che venga effettivamente riprodotto.  
Effettua sempre il premount di ogni `<Sequence>`!

```tsx
<Sequence premountFor={1 * fps}>
  <Title />
</Sequence>
```

## Series (Serie)

Usa `<Series>` quando gli elementi devono essere riprodotti uno dopo l'altro senza sovrapposizioni.

```tsx
import { Series } from "remotion";

<Series>
  <Series.Sequence durationInFrames={45}>
    <Intro />
  </Series.Sequence>
  <Series.Sequence durationInFrames={60}>
    <MainContent />
  </Series.Sequence>
  <Series.Sequence durationInFrames={30}>
    <Outro />
  </Series.Sequence>
</Series>;
```

Come per `<Sequence>`, gli elementi verranno avvolti in un elemento absolute fill per impostazione predefinita quando si usa `<Series.Sequence>`, a meno che la prop `layout` non sia impostata su `none`.

### Serie con sovrapposizioni

Usa un offset negativo per sequenze sovrapposte:

```tsx
<Series>
  <Series.Sequence durationInFrames={60}>
    <SceneA />
  </Series.Sequence>
  <Series.Sequence offset={-15} durationInFrames={60}>
    {/* Inizia 15 frame prima della fine di SceneA */}
    <SceneB />
  </Series.Sequence>
</Series>
```

## Riferimenti ai frame all'interno delle sequenze

All'interno di una Sequence, `useCurrentFrame()` restituisce il frame locale (partendo da 0):

```tsx
<Sequence from={60} durationInFrames={30}>
  <MyComponent />
  {/* All'interno di MyComponent, useCurrentFrame() restituisce 0-29, non 60-89 */}
</Sequence>
```

## Sequenze nidificate

Le sequenze possono essere nidificate per temporizzazioni complesse:

```tsx
<Sequence from={0} durationInFrames={120}>
  <Background />
  <Sequence from={15} durationInFrames={90} layout="none">
    <Title />
  </Sequence>
  <Sequence from={45} durationInFrames={60} layout="none">
    <Subtitle />
  </Sequence>
</Sequence>
```

## Nidificare composizioni all'interno di un'altra

Per aggiungere una composizione all'interno di un'altra composizione, puoi usare il componente `<Sequence>` con le prop `width` e `height` per specificare le dimensioni della composizione.

```tsx
<AbsoluteFill>
  <Sequence width={COMPOSITION_WIDTH} height={COMPOSITION_HEIGHT}>
    <CompositionComponent />
  </Sequence>
</AbsoluteFill>
```
