---
name: get-video-dimensions
description: Ottenere larghezza e altezza di un file video con Mediabunny
metadata:
  tags: dimensions, width, height, resolution, size, video
---

# Ottenere le dimensioni del video con Mediabunny

Mediabunny può estrarre la larghezza e l'altezza di un file video. Funziona negli ambienti browser, Node.js e Bun.

## Ottenere le dimensioni del video

```tsx
import { Input, ALL_FORMATS, UrlSource } from "mediabunny";

export const getVideoDimensions = async (src: string) => {
  const input = new Input({
    formats: ALL_FORMATS,
    source: new UrlSource(src, {
      getRetryDelay: () => null,
    }),
  });

  const videoTrack = await input.getPrimaryVideoTrack();
  if (!videoTrack) {
    throw new Error("Nessuna traccia video trovata");
  }

  return {
    width: videoTrack.displayWidth,
    height: videoTrack.displayHeight,
  };
};
```

## Utilizzo

```tsx
const dimensions = await getVideoDimensions("https://remotion.media/video.mp4");
console.log(dimensions.width); // es. 1920
console.log(dimensions.height); // es. 1080
```

## Utilizzo con file locali

Per i file locali, usa `FileSource` al posto di `UrlSource`:

```tsx
import { Input, ALL_FORMATS, FileSource } from "mediabunny";

const input = new Input({
  formats: ALL_FORMATS,
  source: new FileSource(file), // Oggetto File da input o drag-drop
});

const videoTrack = await input.getPrimaryVideoTrack();
const width = videoTrack.displayWidth;
const height = videoTrack.displayHeight;
```

## Utilizzo con staticFile in Remotion

```tsx
import { staticFile } from "remotion";

const dimensions = await getVideoDimensions(staticFile("video.mp4"));
```
