---
name: ffmpeg
description: Utilizzo di FFmpeg e FFprobe in Remotion
metadata:
  tags: ffmpeg, ffprobe, video, trimming
---

## FFmpeg in Remotion

`ffmpeg` e `ffprobe` non hanno bisogno di essere installati. Sono disponibili tramite `bunx remotion ffmpeg` e `bunx remotion ffprobe`:

```bash
bunx remotion ffmpeg -i input.mp4 output.mp3
bunx remotion ffprobe input.mp4
```

### Ritagliare i video (Trimming)

Hai 2 opzioni per ritagliare i video:

1. Usa la riga di comando di FFmpeg. DEVI ricodificare il video per evitare frame bloccati all'inizio del video.

```bash
# Ricodifica dal frame esatto
bunx remotion ffmpeg -ss 00:00:05 -i public/input.mp4 -to 00:00:10 -c:v libx264 -c:a aac public/output.mp4
```

2. Usa le prop `trimBefore` e `trimAfter` del componente `<Video>`. Il vantaggio è che questa operazione non è distruttiva e puoi cambiare il ritaglio in qualsiasi momento.

```tsx
import { Video } from "@remotion/media";

<Video
  src={staticFile("video.mp4")}
  trimBefore={5 * fps}
  trimAfter={10 * fps}
/>;
```
