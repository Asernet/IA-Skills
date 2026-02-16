---
name: import-srt-captions
description: Importazione di file di sottotitoli .srt in Remotion usando @remotion/captions
metadata:
  tags: captions, subtitles, srt, import, parse
---

# Importazione di sottotitoli .srt in Remotion

Se hai un file di sottotitoli `.srt` esistente, puoi importarlo in Remotion usando `parseSrt()` da `@remotion/captions`.

Se non hai un file .srt, leggi [Trascrivere l'audio](transcribe-captions.md) per scoprire invece come generare i sottotitoli.

## Prerequisiti

Innanzitutto, deve essere installato il pacchetto `@remotion/captions`.
Se non lo è, usa il seguente comando:

```bash
npx remotion add @remotion/captions # Se il progetto usa npm
bunx remotion add @remotion/captions # Se il progetto usa bun
yarn remotion add @remotion/captions # Se il progetto usa yarn
pnpm exec remotion add @remotion/captions # Se il progetto usa pnpm
```

## Lettura di un file .srt

Usa `staticFile()` per fare riferimento a un file `.srt` nella tua cartella `public`, quindi caricalo e analizzalo:

```tsx
import { useState, useEffect, useCallback } from "react";
import { AbsoluteFill, staticFile, useDelayRender } from "remotion";
import { parseSrt } from "@remotion/captions";
import type { Caption } from "@remotion/captions";

export const MyComponent: React.FC = () => {
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const { delayRender, continueRender, cancelRender } = useDelayRender();
  const [handle] = useState(() => delayRender());

  const fetchCaptions = useCallback(async () => {
    try {
      const response = await fetch(staticFile("subtitles.srt"));
      const text = await response.text();
      const { captions: parsed } = parseSrt({ input: text });
      setCaptions(parsed);
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [continueRender, cancelRender, handle]);

  useEffect(() => {
    fetchCaptions();
  }, [fetchCaptions]);

  if (!captions) {
    return null;
  }

  return <AbsoluteFill>{/* Usa i sottotitoli qui */}</AbsoluteFill>;
};
```

Sono supportati anche gli URL remoti: puoi usare `fetch()` su un file remoto tramite URL invece di usare `staticFile()`.

## Utilizzo dei sottotitoli importati

Una volta analizzati, i sottotitoli sono nel formato `Caption` e possono essere usati con tutte le utility di `@remotion/captions`.
