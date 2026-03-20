---
name: subtitles
description: regole per sottotitoli e didascalie
metadata:
  tags: subtitles, captions, remotion, json
---

Tutti i sottotitoli devono essere elaborati in JSON. I sottotitoli devono utilizzare il tipo `Caption`, che è il seguente:

```ts
import type { Caption } from "@remotion/captions";
```

Questa è la definizione:

```ts
type Caption = {
  text: string;
  startMs: number;
  endMs: number;
  timestampMs: number | null;
  confidence: number | null;
};
```

## Generare i sottotitoli

Per trascrivere file video e audio al fine di generare sottotitoli, scarica il file [./transcribe-captions.md](./transcribe-captions.md) per ulteriori istruzioni.

## Visualizzare i sottotitoli

Per visualizzare i sottotitoli nel tuo video, scarica il file [./display-captions.md](./display-captions.md) per ulteriori istruzioni.

## Importare i sottotitoli

Per importare i sottotitoli da un file .srt, scarica il file [./import-srt-captions.md](./import-srt-captions.md) per ulteriori istruzioni.
