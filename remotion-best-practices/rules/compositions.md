---
name: compositions
description: Definizione di composizioni, still, cartelle, props predefinite e metadati dinamici
metadata:
  tags: composition, still, folder, props, metadata
---

Una `<Composition>` definisce il componente, la larghezza, l'altezza, i fps e la durata di un video renderizzabile.

Normalmente viene posizionata nel file `src/Root.tsx`.

```tsx
import { Composition } from "remotion";
import { MyComposition } from "./MyComposition";

export const RemotionRoot = () => {
  return (
    <Composition
      id="MyComposition"
      component={MyComposition}
      durationInFrames={100}
      fps={30}
      width={1080}
      height={1080}
    />
  );
};
```

## Props predefinite (Default Props)

Passa `defaultProps` per fornire valori iniziali al tuo componente.  
I valori devono essere serializzabili in JSON (`Date`, `Map`, `Set` e `staticFile()` sono supportati).

```tsx
import { Composition } from "remotion";
import { MyComposition, MyCompositionProps } from "./MyComposition";

export const RemotionRoot = () => {
  return (
    <Composition
      id="MyComposition"
      component={MyComposition}
      durationInFrames={100}
      fps={30}
      width={1080}
      height={1080}
      defaultProps={
        {
          title: "Hello World",
          color: "#ff0000",
        } satisfies MyCompositionProps
      }
    />
  );
};
```

Usa le dichiarazioni `type` per le props invece di `interface` per garantire la sicurezza dei tipi di `defaultProps`.

## Cartelle (Folders)

Usa `<Folder>` per organizzare le composizioni nella barra laterale.  
I nomi delle cartelle possono contenere solo lettere, numeri e trattini.

```tsx
import { Composition, Folder } from "remotion";

export const RemotionRoot = () => {
  return (
    <>
      <Folder name="Marketing">
        <Composition id="Promo" /* ... */ />
        <Composition id="Ad" /* ... */ />
      </Folder>
      <Folder name="Social">
        <Folder name="Instagram">
          <Composition id="Story" /* ... */ />
          <Composition id="Reel" /* ... */ />
        </Folder>
      </Folder>
    </>
  );
};
```

## Still (Immagini fisse)

Usa `<Still>` per immagini a frame singolo. Non richiede `durationInFrames` o `fps`.

```tsx
import { Still } from "remotion";
import { Thumbnail } from "./Thumbnail";

export const RemotionRoot = () => {
  return (
    <Still id="Thumbnail" component={Thumbnail} width={1280} height={720} />
  );
};
```

## Calcolo dei metadati (Calculate Metadata)

Usa `calculateMetadata` per rendere dinamiche dimensioni, durata o props in base ai dati.

```tsx
import { Composition, CalculateMetadataFunction } from "remotion";
import { MyComposition, MyCompositionProps } from "./MyComposition";

const calculateMetadata: CalculateMetadataFunction<
  MyCompositionProps
> = async ({ props, abortSignal }) => {
  const data = await fetch(`https://api.example.com/video/${props.videoId}`, {
    signal: abortSignal,
  }).then((res) => res.json());

  return {
    durationInFrames: Math.ceil(data.duration * 30),
    props: {
      ...props,
      videoUrl: data.url,
    },
  };
};

export const RemotionRoot = () => {
  return (
    <Composition
      id="MyComposition"
      component={MyComposition}
      durationInFrames={100} // Segnaposto, verrà sovrascritto
      fps={30}
      width={1080}
      height={1080}
      defaultProps={{ videoId: "abc123" }}
      calculateMetadata={calculateMetadata}
    />
  );
};
```

La funzione può restituire `props`, `durationInFrames`, `width`, `height`, `fps` e valori predefiniti relativi al codec. Viene eseguita una sola volta prima dell'inizio del rendering.

## Nidificare composizioni l'una nell'altra

Per aggiungere una composizione all'interno di un'altra, puoi usare il componente `<Sequence>` con le prop `width` e `height` per specificare le dimensioni della composizione nidificata.

```tsx
<AbsoluteFill>
  <Sequence width={COMPOSITION_WIDTH} height={COMPOSITION_HEIGHT}>
    <CompositionComponent />
  </Sequence>
</AbsoluteFill>
```
