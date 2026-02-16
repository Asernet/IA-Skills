---
name: display-captions
description: Visualizzazione dei sottotitoli in Remotion con pagine in stile TikTok e evidenziazione delle parole
metadata:
  tags: captions, subtitles, display, tiktok, highlight
---

# Visualizzazione dei sottotitoli in Remotion

Questa guida spiega come visualizzare i sottotitoli in Remotion, supponendo che tu li abbia già nel formato [`Caption`](https://www.remotion.dev/docs/captions/caption).

## Prerequisiti

Leggi [Trascrivere l'audio](transcribe-captions.md) per scoprire come generare i sottotitoli.

Innanzitutto, deve essere installato il pacchetto [`@remotion/captions`](https://www.remotion.dev/docs/captions).
Se non lo è, usa il seguente comando:

```bash
npx remotion add @remotion/captions
```

## Recupero dei sottotitoli

Per prima cosa, recupera il file JSON dei sottotitoli. Usa [`useDelayRender()`](https://www.remotion.dev/docs/use-delay-render) per sospendere il rendering fino al caricamento dei sottotitoli:

```tsx
import { useState, useEffect, useCallback } from "react";
import { AbsoluteFill, staticFile, useDelayRender } from "remotion";
import type { Caption } from "@remotion/captions";

export const MyComponent: React.FC = () => {
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const { delayRender, continueRender, cancelRender } = useDelayRender();
  const [handle] = useState(() => delayRender());

  const fetchCaptions = useCallback(async () => {
    try {
      // Supponendo che captions.json sia nella cartella public/.
      const response = await fetch(staticFile("captions123.json"));
      const data = await response.json();
      setCaptions(data);
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

  return <AbsoluteFill>{/* Renderizza i sottotitoli qui */}</AbsoluteFill>;
};
```

## Creazione delle pagine

Usa `createTikTokStyleCaptions()` per raggruppare i sottotitoli in pagine. L'opzione `combineTokensWithinMilliseconds` controlla quante parole appaiono contemporaneamente:

```tsx
import { useMemo } from "react";
import { createTikTokStyleCaptions } from "@remotion/captions";
import type { Caption } from "@remotion/captions";

// Ogni quanto i sottotitoli devono cambiare (in millisecondi)
// Valori più alti = più parole per pagina
// Valori più bassi = meno parole (stile parola per parola)
const SWITCH_CAPTIONS_EVERY_MS = 1200;

const { pages } = useMemo(() => {
  return createTikTokStyleCaptions({
    captions,
    combineTokensWithinMilliseconds: SWITCH_CAPTIONS_EVERY_MS,
  });
}, [captions]);
```

## Rendering con le Sequence

Itera sulle pagine e renderizza ognuna in una `<Sequence>`. Calcola il frame di inizio e la durata basandoti sui tempi della pagina:

```tsx
import { Sequence, useVideoConfig, AbsoluteFill } from "remotion";
import type { TikTokPage } from "@remotion/captions";

const CaptionedContent: React.FC = () => {
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        const nextPage = pages[index + 1] ?? null;
        const startFrame = (page.startMs / 1000) * fps;
        const endFrame = Math.min(
          nextPage ? (nextPage.startMs / 1000) * fps : Infinity,
          startFrame + (SWITCH_CAPTIONS_EVERY_MS / 1000) * fps,
        );
        const durationInFrames = endFrame - startFrame;

        if (durationInFrames <= 0) {
          return null;
        }

        return (
          <Sequence
            key={index}
            from={startFrame}
            durationInFrames={durationInFrames}
          >
            <CaptionPage page={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
```

## Preservare gli spazi bianchi

I sottotitoli sono sensibili agli spazi bianchi. Dovresti includere gli spazi nel campo `text` prima di ogni parola. Usa `whiteSpace: "pre"` per preservare gli spazi bianchi nei sottotitoli.

## Componente separato per i sottotitoli

Metti la logica dei sottotitoli in un componente separato.  
Crea un nuovo file dedicato.

## Evidenziazione delle parole (Word Highlighting)

Una pagina di sottotitoli contiene dei `tokens` che puoi usare per evidenziare la parola attualmente pronunciata:

```tsx
import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import type { TikTokPage } from "@remotion/captions";

const HIGHLIGHT_COLOR = "#39E508";

const CaptionPage: React.FC<{ page: TikTokPage }> = ({ page }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Tempo attuale relativo all'inizio della sequenza
  const currentTimeMs = (frame / fps) * 1000;
  // Converti in tempo assoluto aggiungendo l'inizio della pagina
  const absoluteTimeMs = page.startMs + currentTimeMs;

  return (
    <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
      <div style={{ fontSize: 80, fontWeight: "bold", whiteSpace: "pre" }}>
        {page.tokens.map((token) => {
          const isActive =
            token.fromMs <= absoluteTimeMs && token.toMs > absoluteTimeMs;

          return (
            <span
              key={token.fromMs}
              style={{ color: isActive ? HIGHLIGHT_COLOR : "white" }}
            >
              {token.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
```

## Visualizzare i sottotitoli insieme al contenuto video

Per impostazione predefinita, posiziona i sottotitoli insieme al contenuto video, in modo che siano sincronizzati.  
Per ogni video, crea un nuovo file JSON dei sottotitoli.

```tsx
<AbsoluteFill>
  <Video src={staticFile("video.mp4")} />
  <CaptionPage page={page} />
</AbsoluteFill>
```
