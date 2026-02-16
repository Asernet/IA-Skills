---
name: transcribe-captions
description: Trascrivere l'audio per generare sottotitoli in Remotion
metadata:
  tags: captions, transcribe, whisper, audio, speech-to-text
---

# Trascrivere l'audio

Per trascrivere l'audio e generare sottotitoli in Remotion, puoi usare la funzione [`transcribe()`](https://www.remotion.dev/docs/install-whisper-cpp/transcribe) dal pacchetto [`@remotion/install-whisper-cpp`](https://www.remotion.dev/docs/install-whisper-cpp).

## Prerequisiti

Innanzitutto, è necessario installare il pacchetto `@remotion/install-whisper-cpp`.
Se non è installato, usa il seguente comando:

```bash
npx remotion add @remotion/install-whisper-cpp
```

## Trascrizione

Crea uno script Node.js per scaricare Whisper.cpp e un modello, e trascrivere l'audio.

```ts
import path from "path";
import {
  downloadWhisperModel,
  installWhisperCpp,
  transcribe,
  toCaptions,
} from "@remotion/install-whisper-cpp";
import fs from "fs";

const to = path.join(process.cwd(), "whisper.cpp");

await installWhisperCpp({
  to,
  version: "1.5.5",
});

await downloadWhisperModel({
  model: "medium.en",
  folder: to,
});

// Converti prima l'audio in un file wav a 16KHz se necessario:
// import {execSync} from 'child_process';
// execSync('ffmpeg -i /path/to/audio.mp4 -ar 16000 /path/to/audio.wav -y');

const whisperCppOutput = await transcribe({
  model: "medium.en",
  whisperPath: to,
  whisperCppVersion: "1.5.5",
  inputPath: "/path/to/audio123.wav",
  tokenLevelTimestamps: true,
});

// Opzionale: Applica il nostro post-processing consigliato
const { captions } = toCaptions({
  whisperCppOutput,
});

// Scrivilo nella cartella public/ così può essere recuperato da Remotion
fs.writeFileSync("captions123.json", JSON.stringify(captions, null, 2));
```

Trascrivi ogni clip individualmente e crea più file JSON.

Vedi [Visualizzare i sottotitoli](display-captions.md) per come visualizzare i sottotitoli in Remotion.
