---
name: measuring-dom-nodes
description: Misurare le dimensioni degli elementi DOM in Remotion
metadata:
  tags: measure, layout, dimensions, getBoundingClientRect, scale
---

# Misurare i nodi DOM in Remotion

Remotion applica una trasformazione `scale()` al contenitore del video, il che influisce sui valori ottenuti da `getBoundingClientRect()`. Usa `useCurrentScale()` per ottenere misurazioni corrette.

## Misurare le dimensioni di un elemento

```tsx
import { useCurrentScale } from "remotion";
import { useRef, useEffect, useState } from "react";

export const MyComponent = () => {
  const ref = useRef<HTMLDivElement>(null);
  const scale = useCurrentScale();
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });

  useEffect(() => {
    if (!ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    setDimensions({
      width: rect.width / scale,
      height: rect.height / scale,
    });
  }, [scale]);

  return <div ref={ref}>Contenuto da misurare</div>;
};
```
