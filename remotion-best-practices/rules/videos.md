---
name: videos
description: Incorporare video in Remotion - ritaglio, volume, velocità, loop, intonazione
metadata:
  tags: video, media, trim, volume, speed, loop, pitch
---

# Usare i video in Remotion

## Prerequisiti

Innanzitutto, è necessario installare il pacchetto `@remotion/media`.  
In caso contrario, usa il seguente comando:

```bash
npx remotion add @remotion/media # Se il progetto usa npm
bunx remotion add @remotion/media # Se il progetto usa bun
yarn remotion add @remotion/media # Se il progetto usa yarn
pnpm exec remotion add @remotion/media # Se il progetto usa pnpm
```

Usa `<Video>` da `@remotion/media` per incorporare video nella tua composizione.

```tsx
import { Video } from "@remotion/media";
import { staticFile } from "remotion";

export const MyComposition = () => {
  return <Video src={staticFile("video.mp4")} />;
};
```

Sono supportati anche gli URL remoti:

```tsx
<Video src="https://remotion.media/video.mp4" />
```

## Ritaglio (Trimming)

Usa `trimBefore` e `trimAfter` per rimuovere porzioni del video. I valori sono espressi in frame (per impostazione predefinita, ma puoi calcolarli in secondi usando gli FPS).

```tsx
const { fps } = useVideoConfig();

return (
  <Video
    src={staticFile("video.mp4")}
    trimBefore={2 * fps} // Salta i primi 2 secondi
    trimAfter={10 * fps} // Finisce al decimo secondo
  />
);
```

## Ritardo

Avvolgi il video in una `<Sequence>` per ritardare il momento in cui appare:

```tsx
import { Sequence, staticFile } from "remotion";
import { Video } from "@remotion/media";

const { fps } = useVideoConfig();

return (
  <Sequence from={1 * fps}>
    <Video src={staticFile("video.mp4")} />
  </Sequence>
);
```

Il video apparirà dopo 1 secondo.

## Dimensionamento e Posizionamento

Usa la prop `style` per controllare le dimensioni e la posizione:

```tsx
<Video
  src={staticFile("video.mp4")}
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

## Volume

Imposta un volume statico (da 0 a 1):

```tsx
<Video src={staticFile("video.mp4")} volume={0.5} />
```

Oppure usa un callback per un volume dinamico basato sul frame corrente:

```tsx
import { interpolate } from "remotion";

const { fps } = useVideoConfig();

return (
  <Video
    src={staticFile("video.mp4")}
    volume={(f) =>
      interpolate(f, [0, 1 * fps], [0, 1], { extrapolateRight: "clamp" })
    }
  />
);
```

Usa `muted` per silenziare completamente il video:

```tsx
<Video src={staticFile("video.mp4")} muted />
```

## Velocità (Speed)

Usa `playbackRate` per cambiare la velocità di riproduzione:

```tsx
<Video src={staticFile("video.mp4")} playbackRate={2} /> {/* Velocità 2x */}
<Video src={staticFile("video.mp4")} playbackRate={0.5} /> {/* Metà velocità */}
```

La riproduzione al contrario non è supportata.

## Loop

Usa `loop` per riprodurre il video in loop all'infinito:

```tsx
<Video src={staticFile("video.mp4")} loop />
```

Usa `loopVolumeCurveBehavior` per controllare come si comporta il conteggio dei frame durante il loop:

- `"repeat"`: Il conteggio dei frame torna a 0 ad ogni loop (per il callback `volume`)
- `"extend"`: Il conteggio dei frame continua ad aumentare

```tsx
<Video
  src={staticFile("video.mp4")}
  loop
  loopVolumeCurveBehavior="extend"
  volume={(f) => interpolate(f, [0, 300], [1, 0])} // Dissolvenza su più loop
/>
```

## Intonazione (Pitch)

Usa `toneFrequency` per regolare l'intonazione senza influire sulla velocità. I valori vanno da 0.01 a 2:

```tsx
<Video
  src={staticFile("video.mp4")}
  toneFrequency={1.5} // Intonazione più alta
/>
<Video
  src={staticFile("video.mp4")}
  toneFrequency={0.8} // Intonazione più bassa
/>
```

La modifica dell'intonazione funziona solo durante il rendering lato server, non nell'anteprima di Remotion Studio o nel `<Player />`.
