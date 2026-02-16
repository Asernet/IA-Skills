---
name: animations
description: Skill fondamentali di animazione per Remotion
metadata:
  tags: animations, transitions, frames, useCurrentFrame
---

Tutte le animazioni DEVONO essere guidate dall'hook `useCurrentFrame()`.  
Scrivi le animazioni in secondi e moltiplicale per il valore `fps` da `useVideoConfig()`.

```tsx
import { useCurrentFrame } from "remotion";

export const FadeIn = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const opacity = interpolate(frame, [0, 2 * fps], [0, 1], {
    extrapolateRight: "clamp",
  });

  return <div style={{ opacity }}>Hello World!</div>;
};
```

Le transizioni o animazioni CSS sono VIETATE - non verranno renderizzate correttamente.  
Le classi di animazione di Tailwind sono VIETATE - non verranno renderizzate correttamente.
