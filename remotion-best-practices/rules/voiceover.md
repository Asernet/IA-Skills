---
name: voiceover
description: Aggiungere voci fuori campo (voiceover) generate dall'AI alle composizioni Remotion usando ElevenLabs TTS
metadata:
  tags: voiceover, audio, elevenlabs, tts, speech, calculateMetadata, dynamic duration
---

# Aggiungere il voiceover AI a una composizione Remotion

Usa ElevenLabs TTS per generare l'audio parlato per ogni scena, quindi usa [`calculateMetadata`](./calculate-metadata) per dimensionare dinamicamente la composizione in base all'audio.

## Prerequisiti

È richiesta una **ElevenLabs API key**. Memorizzala in un file `.env` nella root del progetto:

```
ELEVENLABS_API_KEY=tua_chiave_qui
```

**DEVI** chiedere all'utente la sua ElevenLabs API key se non esiste un file `.env` o se `ELEVENLABS_API_KEY` non è impostata. **NON DEVI** ripiegare su altri strumenti TTS.

Quando esegui lo script di generazione, usa la flag `--env-file` per caricare il file `.env`:

```bash
node --env-file=.env --strip-types generate-voiceover.ts
```

## Generare l'audio con ElevenLabs

Crea uno script che legga la configurazione, chiami l'API di ElevenLabs per ogni scena e scriva i file MP3 nella cartella `public/` in modo che Remotion possa accedervi tramite `staticFile()`.

La chiamata API principale per una singola scena:

```ts title="generate-voiceover.ts"
const response = await fetch(
  `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`,
  {
    method: "POST",
    headers: {
      "xi-api-key": process.env.ELEVENLABS_API_KEY!,
      "Content-Type": "application/json",
      Accept: "audio/mpeg",
    },
    body: JSON.stringify({
      text: "Benvenuti allo spettacolo.",
      model_id: "eleven_multilingual_v2",
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.3,
      },
    }),
  },
);

const audioBuffer = Buffer.from(await response.arrayBuffer());
writeFileSync(`public/voiceover/${compositionId}/${scene.id}.mp3`, audioBuffer);
```

## Durata dinamica della composizione con calculateMetadata

Usa [`calculateMetadata`](./calculate-metadata.md) per misurare le [durate dell'audio](./get-audio-duration.md) e impostare la lunghezza della composizione di conseguenza.

```tsx
import { CalculateMetadataFunction, staticFile } from "remotion";
import { getAudioDuration } from "./get-audio-duration";

const FPS = 30;

const SCENE_AUDIO_FILES = [
  "voiceover/my-comp/scene-01-intro.mp3",
  "voiceover/my-comp/scene-02-main.mp3",
  "voiceover/my-comp/scene-03-outro.mp3",
];

export const calculateMetadata: CalculateMetadataFunction<Props> = async ({
  props,
}) => {
  const durations = await Promise.all(
    SCENE_AUDIO_FILES.map((file) => getAudioDuration(staticFile(file))),
  );

  const sceneDurations = durations.map((durationInSeconds) => {
    return durationInSeconds * FPS;
  });

  return {
    durationInFrames: Math.ceil(sceneDurations.reduce((sum, d) => sum + d, 0)),
  };
};
```

Le `sceneDurations` calcolate vengono passate al componente tramite una prop `voiceover`, così il componente sa quanto deve durare ogni scena.

Se la composizione usa [`<TransitionSeries>`](./transitions.md), sottrai la sovrapposizione dalla durata totale: [./transitions.md#calcolare-la-durata-totale-della-composizione](./transitions.md#calcolare-la-durata-totale-della-composizione)

## Renderizzare l'audio nel componente

Vedi [audio.md](./audio.md) per maggiori informazioni su come renderizzare l'audio nel componente.

## Ritardare l'inizio dell'audio

Vedi [audio.md#ritardo-delay](./audio.md#ritardo-delay) per maggiori informazioni su come ritardare l'inizio dell'audio.
