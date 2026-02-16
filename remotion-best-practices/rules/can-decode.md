---
name: can-decode
description: Verificare se un video può essere decodificato dal browser usando Mediabunny
metadata:
  tags: decode, validation, video, audio, compatibility, browser
---

# Verificare se un video può essere decodificato

Usa Mediabunny per verificare se un video può essere decodificato dal browser prima di tentare di riprodurlo.

## La funzione `canDecode()`

Questa funzione può essere copiata e incollata in qualsiasi progetto.

```tsx
import { Input, ALL_FORMATS, UrlSource } from "mediabunny";

export const canDecode = async (src: string) => {
  const input = new Input({
    formats: ALL_FORMATS,
    source: new UrlSource(src, {
      getRetryDelay: () => null,
    }),
  });

  try {
    await input.getFormat();
  } catch {
    return false;
  }

  const videoTrack = await input.getPrimaryVideoTrack();
  if (videoTrack && !(await videoTrack.canDecode())) {
    return false;
  }

  const audioTrack = await input.getPrimaryAudioTrack();
  if (audioTrack && !(await audioTrack.canDecode())) {
    return false;
  }

  return true;
};
```

## Utilizzo

```tsx
const src = "https://remotion.media/video.mp4";
const isDecodable = await canDecode(src);

if (isDecodable) {
  console.log("Il video può essere decodificato");
} else {
  console.log("Il video non può essere decodificato da questo browser");
}
```

## Utilizzo con Blob

Per il caricamento di file o drag-and-drop, usa `BlobSource`:

```tsx
import { Input, ALL_FORMATS, BlobSource } from "mediabunny";

export const canDecodeBlob = async (blob: Blob) => {
  const input = new Input({
    formats: ALL_FORMATS,
    source: new BlobSource(blob),
  });

  // Stessa logica di validazione vista sopra
};
```
