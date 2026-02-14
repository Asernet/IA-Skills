---
name: lottie
description: Incorporare animazioni Lottie in Remotion.
metadata:
  category: Animazione
---

# Uso delle animazioni Lottie in Remotion

## Prerequisiti

Innanzitutto, deve essere installato il pacchetto `@remotion/lottie`.  
Se non lo è, usa il seguente comando:

```bash
npx remotion add @remotion/lottie # Se il progetto usa npm
bunx remotion add @remotion/lottie # Se il progetto usa bun
yarn remotion add @remotion/lottie # Se il progetto usa yarn
pnpm exec remotion add @remotion/lottie # Se il progetto usa pnpm
```

## Visualizzare un file Lottie

Per importare un'animazione Lottie:

- Recupera l'asset Lottie
- Avvolgi il processo di caricamento in `delayRender()` e `continueRender()`
- Salva i dati dell'animazione in uno stato
- Renderizza l'animazione Lottie usando il componente `Lottie` dal pacchetto `@remotion/lottie`

```tsx
import { Lottie, LottieAnimationData } from "@remotion/lottie";
import { useEffect, useState } from "react";
import { cancelRender, continueRender, delayRender } from "remotion";

export const MyAnimation = () => {
  const [handle] = useState(() => delayRender("Caricamento animazione Lottie"));

  const [animationData, setAnimationData] =
    useState<LottieAnimationData | null>(null);

  useEffect(() => {
    fetch("https://assets4.lottiefiles.com/packages/lf20_zyquagfl.json")
      .then((data) => data.json())
      .then((json) => {
        setAnimationData(json);
        continueRender(handle);
      })
      .catch((err) => {
        cancelRender(err);
      });
  }, [handle]);

  if (!animationData) {
    return null;
  }

  return <Lottie animationData={animationData} />;
};
```

## Stile e animazione

Lottie supporta la prop `style` per consentire stili e animazioni:

```tsx
return (
  <Lottie animationData={animationData} style={{ width: 400, height: 400 }} />
);
```
