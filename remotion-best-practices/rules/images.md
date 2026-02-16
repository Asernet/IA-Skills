---
name: images
description: Incorporare immagini in Remotion usando il componente <Img>
metadata:
  tags: images, img, staticFile, png, jpg, svg, webp
---

# Uso delle immagini in Remotion

## Il componente `<Img>`

Usa sempre il componente `<Img>` di `remotion` per visualizzare le immagini:

```tsx
import { Img, staticFile } from "remotion";

export const MyComposition = () => {
  return <Img src={staticFile("photo.png")} />;
};
```

## Restrizioni importanti

**DEVI usare il componente `<Img>` di `remotion`.** Non usare:

- Elementi HTML nativi `<img>`
- Componente `<Image>` di Next.js
- CSS `background-image`

Il componente `<Img>` garantisce che le immagini siano completamente caricate prima del rendering, evitando sfarfallii e frame vuoti durante l'esportazione del video.

## Immagini locali con staticFile()

Posiziona le immagini nella cartella `public/` e usa `staticFile()` per farvi riferimento:

```
my-video/
├─ public/
│  ├─ logo.png
│  ├─ avatar.jpg
│  └─ icon.svg
├─ src/
├─ package.json
```

```tsx
import { Img, staticFile } from "remotion";

<Img src={staticFile("logo.png")} />;
```

## Immagini remote

Gli URL remoti possono essere usati direttamente senza `staticFile()`:

```tsx
<Img src="https://example.com/image.png" />
```

Assicurati che le immagini remote abbiano il CORS abilitato.

Per le GIF animate, usa invece il componente `<Gif>` da `@remotion/gif`.

## Dimensionamento e posizionamento

Usa la prop `style` per controllare dimensioni e posizione:

```tsx
<Img
  src={staticFile("photo.png")}
  style={{
    width: 500,
    height: 300,
    position: "absolute",
    top: 100,
    left: 50,
    objectFit: "cover",
  }}
/>
```

## Percorsi immagini dinamici

Usa i template literal per riferimenti a file dinamici:

```tsx
import { Img, staticFile, useCurrentFrame } from "remotion";

const frame = useCurrentFrame();

// Sequenza di immagini
<Img src={staticFile(`frames/frame${frame}.png`)} />

// Selezione basata sulle props
<Img src={staticFile(`avatars/${props.userId}.png`)} />

// Immagini condizionali
<Img src={staticFile(`icons/${isActive ? "active" : "inactive"}.svg`)} />
```

Questo pattern è utile per:

- Sequenze di immagini (animazioni frame-per-frame)
- Avatar o immagini del profilo specifiche per l'utente
- Icone basate sul tema
- Grafica dipendente dallo stato

## Ottenere le dimensioni dell'immagine

Usa `getImageDimensions()` per ottenere le dimensioni di un'immagine:

```tsx
import { getImageDimensions, staticFile } from "remotion";

const { width, height } = await getImageDimensions(staticFile("photo.png"));
```

Questo è utile per calcolare i rapporti d'aspetto o dimensionare le composizioni:

```tsx
import {
  getImageDimensions,
  staticFile,
  CalculateMetadataFunction,
} from "remotion";

const calculateMetadata: CalculateMetadataFunction = async () => {
  const { width, height } = await getImageDimensions(staticFile("photo.png"));
  return {
    width,
    height,
  };
};
```
