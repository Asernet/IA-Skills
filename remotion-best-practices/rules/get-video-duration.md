---
name: get-video-duration
description: Ottenere la durata di un file video in secondi con Mediabunny
metadata:
  tags: duration, video, length, time, seconds
---

# Ottenere la durata del video con Mediabunny

Mediabunny può estrarre la durata di un file video. Funziona negli ambienti browser, Node.js e Bun.

## Ottenere la durata del video

```tsx
import { Input, ALL_FORMATS, UrlSource } from "mediabunny";

export const getVideoDuration = async (src: string) => {
  const input = new Input({
    formats: ALL_FORMATS,
    source: new UrlSource(src, {
      getRetryDelay: () => null,
    }),
  });

  const durationInSeconds = await input.computeDuration();
  return durationInSeconds;
};
```

## Utilizzo

```tsx
const duration = await getVideoDuration("https://remotion.media/video.mp4");
console.log(duration); // es. 10.5 (secondi)
```

## File video dalla cartella public/

Assicurati di avvolgere il percorso del file in `staticFile()`:

```tsx
import { staticFile } from "remotion";

const duration = await getVideoDuration(staticFile("video.mp4"));
```

## In Node.js e Bun

Usa `FileSource` al posto di `UrlSource`:

```tsx
import { Input, ALL_FORMATS, FileSource } from "mediabunny";

const input = new Input({
  formats: ALL_FORMATS,
  source: new FileSource(file), // Oggetto File da input o drag-drop
});

const durationInSeconds = await input.computeDuration();
```
