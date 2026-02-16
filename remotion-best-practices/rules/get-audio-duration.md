---
name: get-audio-duration
description: Ottenere la durata di un file audio in secondi con Mediabunny
metadata:
  tags: duration, audio, length, time, seconds, mp3, wav
---

# Ottenere la durata dell'audio con Mediabunny

Mediabunny può estrarre la durata di un file audio. Funziona negli ambienti browser, Node.js e Bun.

## Ottenere la durata dell'audio

```tsx title="get-audio-duration.ts"
import { Input, ALL_FORMATS, UrlSource } from "mediabunny";

export const getAudioDuration = async (src: string) => {
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
const duration = await getAudioDuration("https://remotion.media/audio.mp3");
console.log(duration); // es. 180.5 (secondi)
```

## Utilizzo con staticFile in Remotion

Assicurati di avvolgere il percorso del file in `staticFile()`:

```tsx
import { staticFile } from "remotion";

const duration = await getAudioDuration(staticFile("audio.mp3"));
```

## In Node.js e Bun

Usa `FileSource` al posto di `UrlSource`:

```tsx
import { Input, ALL_FORMATS, FileSource } from "mediabunny";

const input = new Input({
  formats: ALL_FORMATS,
  source: new FileSource(file), // Oggetto File da input o drag-drop
});
```
