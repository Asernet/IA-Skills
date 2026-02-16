---
name: remotion-best-practices
description: Best practice per Remotion - Creazione di video in React
metadata:
  tags: remotion, video, react, animation, composition
triggers: ["remotion", "video creation", "react video", "animazione remotion"]
---

# Remotion Best Practices

## Quando usare

Usa questa skill ogni volta che lavori con il codice di Remotion per ottenere conoscenze specifiche del dominio.

## Sottotitoli (Captions)

Quando gestisci didascalie o sottotitoli, consulta il file [./rules/subtitles.md](./rules/subtitles.md) per ulteriori informazioni.

## Utilizzo di FFmpeg

Per alcune operazioni video, come il ritaglio (trimming) dei video o il rilevamento dei silenzi, dovrebbe essere usato FFmpeg. Consulta il file [./rules/ffmpeg.md](./rules/ffmpeg.md) per ulteriori informazioni.

## Visualizzazione Audio

Quando hai bisogno di visualizzare l'audio (barre dello spettro, forme d'onda, effetti reattivi ai bassi), consulta il file [./rules/audio-visualization.md](./rules/audio-visualization.md) per ulteriori informazioni.

## Come usare

Leggi i singoli file delle regole per spiegazioni dettagliate ed esempi di codice:

- [rules/3d.md](rules/3d.md) - Contenuti 3D in Remotion usando Three.js e React Three Fiber
- [rules/animations.md](rules/animations.md) - Skill fondamentali di animazione per Remotion
- [rules/assets.md](rules/assets.md) - Importazione di immagini, video, audio e font in Remotion
- [rules/audio.md](rules/audio.md) - Utilizzo di audio e suoni in Remotion - importazione, ritaglio, volume, velocità, pitch
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Impostazione dinamica di durata, dimensioni e props della composizione
- [rules/can-decode.md](rules/can-decode.md) - Verificare se un video può essere decodificato dal browser usando Mediabunny
- [rules/charts.md](rules/charts.md) - Pattern di visualizzazione dati e grafici per Remotion (barre, torta, linee, grafici azionari)
- [rules/compositions.md](rules/compositions.md) - Definizione di composizioni, still, cartelle, props predefinite e metadati dinamici
- [rules/extract-frames.md](rules/extract-frames.md) - Estrazione di frame da video a timestamp specifici usando Mediabunny
- [rules/fonts.md](rules/fonts.md) - Caricamento di Google Fonts e font locali in Remotion
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Ottenere la durata di un file audio in secondi con Mediabunny
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Ottenere larghezza e altezza di un file video con Mediabunny
- [rules/get-video-duration.md](rules/get-video-duration.md) - Ottenere la durata di un file video in secondi con Mediabunny
- [rules/gifs.md](rules/gifs.md) - Visualizzazione di GIF sincronizzate con la timeline di Remotion
- [rules/images.md](rules/images.md) - Inserimento di immagini in Remotion usando il componente Img
- [rules/light-leaks.md](rules/light-leaks.md) - Effetti di sovrapposizione light leak usando @remotion/light-leaks
- [rules/lottie.md](rules/lottie.md) - Inserimento di animazioni Lottie in Remotion
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Misurazione delle dimensioni degli elementi DOM in Remotion
- [rules/measuring-text.md](rules/measuring-text.md) - Misurazione delle dimensioni del testo, adattamento del testo ai contenitori e controllo dell'overflow
- [rules/sequencing.md](rules/sequencing.md) - Pattern di sequenziamento per Remotion - ritardo, ritaglio, limitazione della durata degli elementi
- [rules/tailwind.md](rules/tailwind.md) - Utilizzo di TailwindCSS in Remotion
- [rules/text-animations.md](rules/text-animations.md) - Pattern di tipografia e animazione del testo per Remotion
- [rules/timing.md](rules/timing.md) - Curve di interpolazione in Remotion - animazioni lineari, easing, spring
- [rules/transitions.md](rules/transitions.md) - Pattern di transizione di scena per Remotion
- [rules/transparent-videos.md](rules/transparent-videos.md) - Rendering di un video con trasparenza
- [rules/trimming.md](rules/trimming.md) - Pattern di ritaglio per Remotion - tagliare l'inizio o la fine delle animazioni
- [rules/videos.md](rules/videos.md) - Inserimento di video in Remotion - ritaglio, volume, velocità, looping, pitch
- [rules/parameters.md](rules/parameters.md) - Rendere un video parametrizzabile aggiungendo uno schema Zod
- [rules/maps.md](rules/maps.md) - Aggiungere una mappa usando Mapbox e animarla
- [rules/voiceover.md](rules/voiceover.md) - Aggiunta di voiceover generato dall'IA alle composizioni Remotion usando ElevenLabs TTS
