---
name: charts
description: Pattern di visualizzazione dati e grafici per Remotion. Usa quando crei grafici a barre, a torta, a linee, grafici azionari o qualsiasi animazione basata su dati.
metadata:
  tags: charts, data, visualization, bar-chart, pie-chart, line-chart, stock-chart, svg-paths, graphs
---

# Grafici in Remotion

Crea grafici usando il codice React - HTML, SVG e D3.js sono tutti supportati.

Disabilita tutte le animazioni da librerie di terze parti - causano sfarfallio.  
Guida tutte le animazioni tramite `useCurrentFrame()`.

## Grafico a barre (Bar Chart)

```tsx
const STAGGER_DELAY = 5;
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const bars = data.map((item, i) => {
  const height = spring({
    frame,
    fps,
    delay: i * STAGGER_DELAY,
    config: { damping: 200 },
  });
  return <div style={{ height: height * item.value }} />;
});
```

## Grafico a torta (Pie Chart)

Anima i segmenti usando `stroke-dashoffset`, iniziando dalle ore 12:

```tsx
const progress = interpolate(frame, [0, 100], [0, 1]);
const circumference = 2 * Math.PI * radius;
const segmentLength = (value / total) * circumference;
const offset = interpolate(progress, [0, 1], [segmentLength, 0]);

<circle
  r={radius}
  cx={center}
  cy={center}
  fill="none"
  stroke={color}
  strokeWidth={strokeWidth}
  strokeDasharray={`${segmentLength} ${circumference}`}
  strokeDashoffset={offset}
  transform={`rotate(-90 ${center} ${center})`}
/>;
```

## Grafico a linee / Animazione di percorsi (Path)

Usa `@remotion/paths` per animare i percorsi SVG (grafici a linee, grafici azionari, firme).

Installa: `npx remotion add @remotion/paths`  
Documentazione: https://remotion.dev/docs/paths.md

### Convertire punti dati in un percorso SVG

```tsx
type Point = { x: number; y: number };

const generateLinePath = (points: Point[]): string => {
  if (points.length < 2) return "";
  return points.map((p, i) => `${i === 0 ? "M" : "L"} ${p.x} ${p.y}`).join(" ");
};
```

### Disegnare il percorso con animazione

```tsx
import { evolvePath } from "@remotion/paths";

const path = "M 100 200 L 200 150 L 300 180 L 400 100";
const progress = interpolate(frame, [0, 2 * fps], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
  easing: Easing.out(Easing.quad),
});

const { strokeDasharray, strokeDashoffset } = evolvePath(progress, path);

<path
  d={path}
  fill="none"
  stroke="#FF3232"
  strokeWidth={4}
  strokeDasharray={strokeDasharray}
  strokeDashoffset={strokeDashoffset}
/>;
```

### Seguire il percorso con un marker/freccia

```tsx
import {
  getLength,
  getPointAtLength,
  getTangentAtLength,
} from "@remotion/paths";

const pathLength = getLength(path);
const point = getPointAtLength(path, progress * pathLength);
const tangent = getTangentAtLength(path, progress * pathLength);
const angle = Math.atan2(tangent.y, tangent.x);

<g
  style={{
    transform: `translate(${point.x}px, ${point.y}px) rotate(${angle}rad)`,
    transformOrigin: "0 0",
  }}
>
  <polygon points="0,0 -20,-10 -20,10" fill="#FF3232" />
</g>;
```
