---
name: assets
description: Importazione di immagini, video, audio e font in Remotion
metadata:
  tags: assets, staticFile, images, fonts, public
---

# Importazione di asset in Remotion

## La cartella public

Posiziona gli asset nella cartella `public/` alla radice del tuo progetto.

## Utilizzo di staticFile()

DEVI usare `staticFile()` per fare riferimento ai file nella cartella `public/`:

```tsx
import { Img, staticFile } from "remotion";

export const MyComposition = () => {
  return <Img src={staticFile("logo.png")} />;
};
```

La funzione restituisce un URL codificato che funziona correttamente quando si distribuisce in sottodirectory.

## Utilizzo con i componenti

**Immagini:**

```tsx
import { Img, staticFile } from "remotion";

<Img src={staticFile("photo.png")} />;
```

**Video:**

```tsx
import { Video } from "@remotion/media";
import { staticFile } from "remotion";

<Video src={staticFile("clip.mp4")} />;
```

**Audio:**

```tsx
import { Audio } from "@remotion/media";
import { staticFile } from "remotion";

<Audio src={staticFile("music.mp3")} />;
```

**Font:**

```tsx
import { staticFile } from "remotion";

const fontFamily = new FontFace("MyFont", `url(${staticFile("font.woff2")})`);
await fontFamily.load();
document.fonts.add(fontFamily);
```

## URL remoti

Gli URL remoti possono essere utilizzati direttamente senza `staticFile()`:

```tsx
<Img src="https://example.com/image.png" />
<Video src="https://remotion.media/video.mp4" />
```

## Note importanti

- I componenti di Remotion (`<Img>`, `<Video>`, `<Audio>`) assicurano che gli asset siano completamente caricati prima del rendering
- I caratteri speciali nei nomi dei file (`#`, `?`, `&`) vengono codificati automaticamente
