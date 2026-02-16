---
name: calculate-metadata
description: Impostazione dinamica di durata, dimensioni e props della composizione
metadata:
  tags: calculateMetadata, duration, dimensions, props, dynamic
---

# Uso di calculateMetadata

Usa `calculateMetadata` su una `<Composition>` per impostare dinamicamente durata, dimensioni e trasformare le props prima del rendering.

```tsx
<Composition
  id="MyComp"
  component={MyComponent}
  durationInFrames={300}
  fps={30}
  width={1920}
  height={1080}
  defaultProps={{ videoSrc: "https://remotion.media/video.mp4" }}
  calculateMetadata={calculateMetadata}
/>
```

## Impostazione della durata basata su un video

Usa le skill [`getVideoDuration`](./get-video-duration.md) e [`getVideoDimensions`](./get-video-dimensions.md) per ottenere la durata e le dimensioni del video:

```tsx
import { CalculateMetadataFunction } from "remotion";
import { getVideoDuration } from "./get-video-duration";

const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  const durationInSeconds = await getVideoDuration(props.videoSrc);

  return {
    durationInFrames: Math.ceil(durationInSeconds * 30),
  };
};
```

## Far corrispondere le dimensioni di un video

Usa la skill [`getVideoDimensions`](./get-video-dimensions.md) per ottenere le dimensioni del video:

```tsx
import { CalculateMetadataFunction } from "remotion";
import { getVideoDuration } from "./get-video-duration";
import { getVideoDimensions } from "./get-video-dimensions";

const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  const dimensions = await getVideoDimensions(props.videoSrc);

  return {
    width: dimensions.width,
    height: dimensions.height,
  };
};
```

## Durata basata su più video

```tsx
const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  const metadataPromises = props.videos.map((video) =>
    getVideoDuration(video.src),
  );
  const allMetadata = await Promise.all(metadataPromises);

  const totalDuration = allMetadata.reduce(
    (sum, durationInSeconds) => sum + durationInSeconds,
    0,
  );

  return {
    durationInFrames: Math.ceil(totalDuration * 30),
  };
};
```

## Impostazione di un outName predefinito

Imposta il nome del file di output predefinito basato sulle props:

```tsx
const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  return {
    defaultOutName: `video-${props.id}.mp4`,
  };
};
```

## Trasformazione delle props

Recupera dati o trasforma le props prima del rendering:

```tsx
const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
  abortSignal,
}) => {
  const response = await fetch(props.dataUrl, { signal: abortSignal });
  const data = await response.json();

  return {
    props: {
      ...props,
      fetchedData: data,
    },
  };
};
```

L'`abortSignal` annulla le richieste obsolete quando le props cambiano nello Studio.

## Valore di ritorno

Tutti i campi sono opzionali. I valori restituiti sovrascrivono le props della `<Composition>`:

- `durationInFrames`: Numero di frame
- `width`: Larghezza della composizione in pixel
- `height`: Altezza della composizione in pixel
- `fps`: Frame per secondo
- `props`: Props trasformate passate al componente
- `defaultOutName`: Nome file di output predefinito
- `defaultCodec`: Codec predefinito per il rendering
