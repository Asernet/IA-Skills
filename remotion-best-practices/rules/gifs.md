---
name: gif
description: Visualizzazione di GIF, APNG, AVIF e WebP in Remotion
metadata:
  tags: gif, animation, images, animated, apng, avif, webp
---

# Uso delle immagini animate in Remotion

## Utilizzo di base

Usa `<AnimatedImage>` per visualizzare un'immagine GIF, APNG, AVIF o WebP sincronizzata con la timeline di Remotion:

```tsx
import { AnimatedImage, staticFile } from "remotion";

export const MyComposition = () => {
  return (
    <AnimatedImage src={staticFile("animation.gif")} width={500} height={500} />
  );
};
```

Sono supportati anche gli URL remoti (deve essere abilitato il CORS):

```tsx
<AnimatedImage
  src="https://example.com/animation.gif"
  width={500}
  height={500}
/>
```

## Dimensionamento e adattamento (fit)

Controlla come l'immagine riempie il suo contenitore con la prop `fit`:

```tsx
// Allunga per riempire (predefinito)
<AnimatedImage src={staticFile("animation.gif")} width={500} height={300} fit="fill" />

// Mantiene il rapporto d'aspetto, entra nel contenitore
<AnimatedImage src={staticFile("animation.gif")} width={500} height={300} fit="contain" />

// Riempie il contenitore, ritaglia se necessario
<AnimatedImage src={staticFile("animation.gif")} width={500} height={300} fit="cover" />
```

## Velocità di riproduzione

Usa `playbackRate` per controllare la velocità dell'animazione:

```tsx
<AnimatedImage src={staticFile("animation.gif")} width={500} height={500} playbackRate={2} /> {/* Velocità 2x */}
<AnimatedImage src={staticFile("animation.gif")} width={500} height={500} playbackRate={0.5} /> {/* Metà velocità */}
```

## Comportamento del loop

Controlla cosa succede quando l'animazione finisce:

```tsx
// Loop indefinito (predefinito)
<AnimatedImage src={staticFile("animation.gif")} width={500} height={500} loopBehavior="loop" />

// Riproduci una volta, mostra il frame finale
<AnimatedImage src={staticFile("animation.gif")} width={500} height={500} loopBehavior="pause-after-finish" />

// Riproduci una volta, poi svuota il canvas
<AnimatedImage src={staticFile("animation.gif")} width={500} height={500} loopBehavior="clear-after-finish" />
```

## Stile

Usa la prop `style` per CSS aggiuntivo (usa le prop `width` e `height` per il dimensionamento):

```tsx
<AnimatedImage
  src={staticFile("animation.gif")}
  width={500}
  height={500}
  style={{
    borderRadius: 20,
    position: "absolute",
    top: 100,
    left: 50,
  }}
/>
```

## Ottenere la durata della GIF

Usa `getGifDurationInSeconds()` da `@remotion/gif` per ottenere la durata di una GIF.

```bash
npx remotion add @remotion/gif
```

```tsx
import { getGifDurationInSeconds } from "@remotion/gif";
import { staticFile } from "remotion";

const duration = await getGifDurationInSeconds(staticFile("animation.gif"));
console.log(duration); // es. 2.5
```

Questo è utile per impostare la durata della composizione in modo che corrisponda alla GIF:

```tsx
import { getGifDurationInSeconds } from "@remotion/gif";
import { staticFile, CalculateMetadataFunction } from "remotion";

const calculateMetadata: CalculateMetadataFunction = async () => {
  const duration = await getGifDurationInSeconds(staticFile("animation.gif"));
  return {
    durationInFrames: Math.ceil(duration * 30),
  };
};
```

## Alternativa

Se `<AnimatedImage>` non funziona (supportato solo in Chrome e Firefox), puoi usare `<Gif>` da `@remotion/gif` al suo posto.

```bash
npx remotion add @remotion/gif # Se il progetto usa npm
bunx remotion add @remotion/gif # Se il progetto usa bun
yarn remotion add @remotion/gif # Se il progetto usa yarn
pnpm exec remotion add @remotion/gif # Se il progetto usa pnpm
```

```tsx
import { Gif } from "@remotion/gif";
import { staticFile } from "remotion";

export const MyComposition = () => {
  return <Gif src={staticFile("animation.gif")} width={500} height={500} />;
};
```

Il componente `<Gif>` ha le stesse prop di `<AnimatedImage>` ma supporta solo file GIF.
