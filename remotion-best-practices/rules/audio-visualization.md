---
name: audio-visualization
description: Pattern di visualizzazione audio - barre dello spettro, forme d'onda, effetti reattivi ai bassi
metadata:
  tags: audio, visualization, spectrum, waveform, bass, music, audiogram, frequency
---

# Visualizzazione Audio in Remotion

## Prerequisiti

```bash
npx remotion add @remotion/media-utils
```

## Caricamento dei dati audio

Usa `useWindowedAudioData()` (https://www.remotion.dev/docs/use-windowed-audio-data) per caricare i dati audio:

```tsx
import { useWindowedAudioData } from "@remotion/media-utils";
import { staticFile, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
  src: staticFile("podcast.wav"),
  frame,
  fps,
  windowInSeconds: 30,
});
```

## Visualizzazione a barre dello spettro (Spectrum Bar)

Usa `visualizeAudio()` (https://www.remotion.dev/docs/visualize-audio) per ottenere i dati di frequenza per i grafici a barre:

```tsx
import { useWindowedAudioData, visualizeAudio } from "@remotion/media-utils";
import { staticFile, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
  src: staticFile("music.mp3"),
  frame,
  fps,
  windowInSeconds: 30,
});

if (!audioData) {
  return null;
}

const frequencies = visualizeAudio({
  fps,
  frame,
  audioData,
  numberOfSamples: 256,
  optimizeFor: "speed",
  dataOffsetInSeconds,
});

return (
  <div style={{ display: "flex", alignItems: "flex-end", height: 200 }}>
    {frequencies.map((v, i) => (
      <div
        key={i}
        style={{
          flex: 1,
          height: `${v * 100}%`,
          backgroundColor: "#0b84f3",
          margin: "0 1px",
        }}
      />
    ))}
  </div>
);
```

- `numberOfSamples` deve essere una potenza di 2 (32, 64, 128, 256, 512, 1024)
- I valori vanno da 0 a 1; a sinistra dell'array = bassi, a destra = alti
- Usa `optimizeFor: "speed"` per Lambda o conteggi di campioni elevati

**Importante:** Quando passi `audioData` ai componenti figli, passa anche il `frame` dal genitore. Non chiamare `useCurrentFrame()` in ogni figlio - questo causa una visualizzazione discontinua quando i figli sono all'interno di `<Sequence>` con offset.

## Visualizzazione della forma d'onda (Waveform)

Usa `visualizeAudioWaveform()` (https://www.remotion.dev/docs/media-utils/visualize-audio-waveform) con `createSmoothSvgPath()` (https://www.remotion.dev/docs/media-utils/create-smooth-svg-path) per visualizzazioni in stile oscilloscopio:

```tsx
import {
  createSmoothSvgPath,
  useWindowedAudioData,
  visualizeAudioWaveform,
} from "@remotion/media-utils";
import { staticFile, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { width, fps } = useVideoConfig();
const HEIGHT = 200;

const { audioData, dataOffsetInSeconds } = useWindowedAudioData({
  src: staticFile("voice.wav"),
  frame,
  fps,
  windowInSeconds: 30,
});

if (!audioData) {
  return null;
}

const waveform = visualizeAudioWaveform({
  fps,
  frame,
  audioData,
  numberOfSamples: 256,
  windowInSeconds: 0.5,
  dataOffsetInSeconds,
});

const path = createSmoothSvgPath({
  points: waveform.map((y, i) => ({
    x: (i / (waveform.length - 1)) * width,
    y: HEIGHT / 2 + (y * HEIGHT) / 2,
  })),
});

return (
  <svg width={width} height={HEIGHT}>
    <path d={path} fill="none" stroke="#0b84f3" strokeWidth={2} />
  </svg>
);
```

## Effetti reattivi ai bassi (Bass-Reactive)

Estrai le basse frequenze per animazioni reattive al ritmo (beat):

```tsx
const frequencies = visualizeAudio({
  fps,
  frame,
  audioData,
  numberOfSamples: 128,
  optimizeFor: "speed",
  dataOffsetInSeconds,
});

const lowFrequencies = frequencies.slice(0, 32);
const bassIntensity =
  lowFrequencies.reduce((sum, v) => sum + v, 0) / lowFrequencies.length;

const scale = 1 + bassIntensity * 0.5;
const opacity = Math.min(0.6, bassIntensity * 0.8);
```

## Forma d'onda basata sul volume

Usa `getWaveformPortion()` (https://www.remotion.dev/docs/get-waveform-portion) quando hai bisogno di dati di volume semplificati invece dello spettro di frequenza:

```tsx
import { getWaveformPortion } from "@remotion/media-utils";
import { useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const currentTimeInSeconds = frame / fps;

const waveform = getWaveformPortion({
  audioData,
  startTimeInSeconds: currentTimeInSeconds,
  durationInSeconds: 5,
  numberOfSamples: 50,
});

// Restituisce un array di oggetti { index, amplitude } (amplitude: 0-1)
waveform.map((bar) => (
  <div key={bar.index} style={{ height: bar.amplitude * 100 }} />
));
```

## Post-elaborazione

Le basse frequenze dominano naturalmente. Applica la scala logaritmica per il bilanciamento visivo:

```tsx
const minDb = -100;
const maxDb = -30;

const scaled = frequencies.map((value) => {
  const db = 20 * Math.log10(value);
  return (db - minDb) / (maxDb - minDb);
});
```
