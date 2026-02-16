---
name: timing
description: Curve di interpolazione in Remotion - animazioni lineari, easing e spring
metadata:
  tags: spring, bounce, easing, interpolation
---

Un'interpolazione lineare semplice si ottiene usando la funzione `interpolate`.

```ts title="Andamento da 0 a 1 su 100 frame"
import { interpolate } from "remotion";

const opacity = interpolate(frame, [0, 100], [0, 1]);
```

Per impostazione predefinita, i valori non sono vincolati (clamped), quindi il valore può uscire dall'intervallo [0, 1].  
Ecco come possono essere vincolati:

```ts title="Andamento da 0 a 1 su 100 frame con estrapolazione"
const opacity = interpolate(frame, [0, 100], [0, 1], {
  extrapolateRight: "clamp",
  extrapolateLeft: "clamp",
});
```

## Animazioni a molla (Spring animations)

Le animazioni a molla hanno un movimento più naturale.  
Vanno da 0 a 1 nel tempo.

```ts title="Animazione a molla da 0 a 1 su 100 frame"
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const scale = spring({
  frame,
  fps,
});
```

### Proprietà fisiche

La configurazione predefinita è: `mass: 1, damping: 10, stiffness: 100`.  
Questo fa sì che l'animazione abbia un po' di rimbalzo (bounce) prima di stabilizzarsi.

La configurazione può essere sovrascritta in questo modo:

```ts
const scale = spring({
  frame,
  fps,
  config: { damping: 200 },
});
```

La configurazione consigliata per un movimento naturale senza rimbalzo è: `{ damping: 200 }`.

Ecco alcune configurazioni comuni:

```tsx
const smooth = { damping: 200 }; // Fluido, senza rimbalzo (rivelazioni sottili)
const snappy = { damping: 20, stiffness: 200 }; // Scattante, rimbalzo minimo (elementi UI)
const bouncy = { damping: 8 }; // Entrata con rimbalzo (animazioni giocose)
const heavy = { damping: 15, stiffness: 80, mass: 2 }; // Pesante, lento, piccolo rimbalzo
```

### Ritardo (Delay)

L'animazione inizia immediatamente per impostazione predefinita.  
Usa il parametro `delay` per ritardare l'animazione di un certo numero di frame.

```tsx
const entrance = spring({
  frame: frame - ENTRANCE_DELAY,
  fps,
  delay: 20,
});
```

### Durata

Una `spring()` ha una durata naturale basata sulle proprietà fisiche.  
Per estendere l'animazione a una durata specifica, usa il parametro `durationInFrames`.

```tsx
const spring = spring({
  frame,
  fps,
  durationInFrames: 40,
});
```

### Combinare spring() con interpolate()

Mappa l'output della molla (0-1) su intervalli personalizzati:

```tsx
const springProgress = spring({
  frame,
  fps,
});

// Mappa sulla rotazione
const rotation = interpolate(springProgress, [0, 1], [0, 360]);

<div style={{ rotate: rotation + "deg" }} />;
```

### Sommare le molle

Le molle restituiscono solo numeri, quindi è possibile eseguire operazioni matematiche:

```tsx
const frame = useCurrentFrame();
const { fps, durationInFrames } = useVideoConfig();

const inAnimation = spring({
  frame,
  fps,
});
const outAnimation = spring({
  frame,
  fps,
  durationInFrames: 1 * fps,
  delay: durationInFrames - 1 * fps,
});

const scale = inAnimation - outAnimation;
```

## Easing

L'easing può essere aggiunto alla funzione `interpolate`:

```ts
import { interpolate, Easing } from "remotion";

const value1 = interpolate(frame, [0, 100], [0, 1], {
  easing: Easing.inOut(Easing.quad),
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

L'easing predefinito è `Easing.linear`.  
Esistono varie altre convessità:

- `Easing.in` per iniziare lentamente e accelerare
- `Easing.out` per iniziare velocemente e rallentare
- `Easing.inOut`

e curve (ordinate dalla più lineare alla più curva):

- `Easing.quad`
- `Easing.sin`
- `Easing.exp`
- `Easing.circle`

Convessità e curve devono essere combinate per una funzione di easing:

```ts
const value1 = interpolate(frame, [0, 100], [0, 1], {
  easing: Easing.inOut(Easing.quad),
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```

Sono supportate anche le curve di Beziér cubiche:

```ts
const value1 = interpolate(frame, [0, 100], [0, 1], {
  easing: Easing.bezier(0.8, 0.22, 0.96, 0.65),
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});
```
