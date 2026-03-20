---
name: audio
description: Utilizzo di audio e suoni in Remotion - importazione, ritaglio, volume, velocità, pitch
metadata:
  tags: audio, media, trim, volume, speed, loop, pitch, mute, sound, sfx
---

# Uso dell'audio in Remotion

## Prerequisiti

Innanzitutto, deve essere installato il pacchetto `@remotion/media`.
Se non lo è, usa il seguente comando:

```bash
npx remotion add @remotion/media
```

## Importazione dell'audio

Usa `<Audio>` da `@remotion/media` per aggiungere l'audio alla tua composizione.

```tsx
import { Audio } from "@remotion/media";
import { staticFile } from "remotion";

export const MyComposition = () => {
  return <Audio src={staticFile("audio.mp3")} />;
};
```

Sono supportati anche gli URL remoti:

```tsx
<Audio src="https://remotion.media/audio.mp3" />
```

Per impostazione predefinita, l'audio viene riprodotto dall'inizio, a volume pieno e per l'intera durata.
È possibile sovrapporre più tracce audio aggiungendo più componenti `<Audio>`.

## Ritaglio (Trimming)

Usa `trimBefore` e `trimAfter` per rimuovere parti dell'audio. I valori sono in frame.

```tsx
const { fps } = useVideoConfig();

return (
  <Audio
    src={staticFile("audio.mp3")}
    trimBefore={2 * fps} // Salta i primi 2 secondi
    trimAfter={10 * fps} // Termina al decimo secondo
  />
);
```

L'audio inizierà comunque a suonare all'inizio della composizione - verrà riprodotta solo la parte specificata.

## Ritardo (Delaying)

Avvolgi l'audio in un `<Sequence>` per ritardare l'inizio della riproduzione:

```tsx
import { Sequence, staticFile } from "remotion";
import { Audio } from "@remotion/media";

const { fps } = useVideoConfig();

return (
  <Sequence from={1 * fps}>
    <Audio src={staticFile("audio.mp3")} />
  </Sequence>
);
```

L'audio inizierà a suonare dopo 1 secondo.

## Volume

Imposta un volume statico (da 0 a 1):

```tsx
<Audio src={staticFile("audio.mp3")} volume={0.5} />
```

Oppure usa una callback per un volume dinamico basato sul frame corrente:

```tsx
import { interpolate } from "remotion";

const { fps } = useVideoConfig();

return (
  <Audio
    src={staticFile("audio.mp3")}
    volume={(f) =>
      interpolate(f, [0, 1 * fps], [0, 1], { extrapolateRight: "clamp" })
    }
  />
);
```

Il valore di `f` parte da 0 quando l'audio inizia a suonare, non dal frame della composizione.

## Disattivazione audio (Muting)

Usa `muted` per silenziare l'audio. Può essere impostato dinamicamente:

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();

return (
  <Audio
    src={staticFile("audio.mp3")}
    muted={frame >= 2 * fps && frame <= 4 * fps} // Silenziato tra 2s e 4s
  />
);
```

## Velocità

Usa `playbackRate` per cambiare la velocità di riproduzione:

```tsx
<Audio src={staticFile("audio.mp3")} playbackRate={2} /> {/* Velocità 2x */}
<Audio src={staticFile("audio.mp3")} playbackRate={0.5} /> {/* Metà velocità */}
```

La riproduzione al contrario non è supportata.

## Loop

Usa `loop` per riprodurre l'audio in loop all'infinito:

```tsx
<Audio src={staticFile("audio.mp3")} loop />
```

Usa `loopVolumeCurveBehavior` per controllare come si comporta il conteggio dei frame durante il loop:

- `"repeat"`: Il conteggio dei frame torna a 0 ad ogni loop (predefinito)
- `"extend"`: Il conteggio dei frame continua a incrementare

```tsx
<Audio
  src={staticFile("audio.mp3")}
  loop
  loopVolumeCurveBehavior="extend"
  volume={(f) => interpolate(f, [0, 300], [1, 0])} // Sfuma (fade out) su più loop
/>
```

## Pitch

Usa `toneFrequency` per regolare l'intonazione (pitch) senza influenzare la velocità. I valori vanno da 0.01 a 2:

```tsx
<Audio
  src={staticFile("audio.mp3")}
  toneFrequency={1.5} // Intonazione più alta
/>
<Audio
  src={staticFile("audio.mp3")}
  toneFrequency={0.8} // Intonazione più bassa
/>
```

Il cambio di intonazione funziona solo durante il rendering lato server, non nell'anteprima di Remotion Studio o nel `<Player />`.
