---
name: maps
description: Creare animazioni di mappe con Mapbox
metadata:
  tags: map, map animation, mapbox
---

Le mappe possono essere aggiunte a un video Remotion con Mapbox.  
La [documentazione di Mapbox](https://docs.mapbox.com/mapbox-gl-js/api/) contiene il riferimento API.

## Prerequisiti

Mapbox e `@turf/turf` devono essere installati.

Cerca nel progetto i file di lock ed esegui il comando corretto a seconda del package manager:

Se viene trovato `package-lock.json`, usa il seguente comando:

```bash
npm i mapbox-gl @turf/turf @types/mapbox-gl
```

Se viene trovato `bun.lock`, usa il seguente comando:

```bash
bun i mapbox-gl @turf/turf @types/mapbox-gl
```

Se viene trovato `yarn.lock`, usa il seguente comando:

```bash
yarn add mapbox-gl @turf/turf @types/mapbox-gl
```

Se viene trovato `pnpm-lock.yaml`, usa il seguente comando:

```bash
pnpm i mapbox-gl @turf/turf @types/mapbox-gl
```

L'utente deve creare un account Mapbox gratuito e generare un token di accesso visitando https://console.mapbox.com/account/access-tokens/.

Il token Mapbox deve essere aggiunto al file `.env`:

```txt title=".env"
REMOTION_MAPBOX_TOKEN=pk.tuo-token-mapbox-per-l-accesso
```

## Aggiungere una mappa

Ecco un esempio base di una mappa in Remotion.

```tsx
import { useEffect, useMemo, useRef, useState } from "react";
import { AbsoluteFill, useDelayRender, useVideoConfig } from "remotion";
import mapboxgl, { Map } from "mapbox-gl";

export const lineCoordinates = [
  [6.56158447265625, 46.059891147620725],
  [6.5691375732421875, 46.05679376154153],
  [6.5842437744140625, 46.05059898938315],
  [6.594886779785156, 46.04702502069337],
  [6.601066589355469, 46.0460718554722],
  [6.6089630126953125, 46.0365370783104],
  [6.6185760498046875, 46.018420689207964],
];

mapboxgl.accessToken = process.env.REMOTION_MAPBOX_TOKEN as string;

export const MyComposition = () => {
  const ref = useRef<HTMLDivElement>(null);
  const { delayRender, continueRender } = useDelayRender();

  const { width, height } = useVideoConfig();
  const [handle] = useState(() => delayRender("Caricamento mappa..."));
  const [map, setMap] = useState<Map | null>(null);

  useEffect(() => {
    const _map = new Map({
      container: ref.current!,
      zoom: 11.53,
      center: [6.5615, 46.0598],
      pitch: 65,
      bearing: 0,
      style: "mapbox://styles/mapbox/standard",
      interactive: false,
      fadeDuration: 0,
    });

    _map.on("style.load", () => {
      // Nasconde tutte le caratteristiche dello stile Mapbox Standard
      const hideFeatures = [
        "showRoadsAndTransit",
        "showRoads",
        "showTransit",
        "showPedestrianRoads",
        "showRoadLabels",
        "showTransitLabels",
        "showPlaceLabels",
        "showPointOfInterestLabels",
        "showPointsOfInterest",
        "showAdminBoundaries",
        "showLandmarkIcons",
        "showLandmarkIconLabels",
        "show3dObjects",
        "show3dBuildings",
        "show3dTrees",
        "show3dLandmarks",
        "show3dFacades",
      ];
      for (const feature of hideFeatures) {
        _map.setConfigProperty("basemap", feature, false);
      }

      _map.setConfigProperty("basemap", "colorTrunks", "rgba(0, 0, 0, 0)");

      _map.addSource("trace", {
        type: "geojson",
        data: {
          type: "Feature",
          properties: {},
          geometry: {
            type: "LineString",
            coordinates: lineCoordinates,
          },
        },
      });
      _map.addLayer({
        type: "line",
        source: "trace",
        id: "line",
        paint: {
          "line-color": "black",
          "line-width": 5,
        },
        layout: {
          "line-cap": "round",
          "line-join": "round",
        },
      });
    });

    _map.on("load", () => {
      continueRender(handle);
      setMap(_map);
    });
  }, [handle, lineCoordinates]);

  const style: React.CSSProperties = useMemo(
    () => ({ width, height, position: "absolute" }),
    [width, height],
  );

  return <AbsoluteFill ref={ref} style={style} />;
};
```

I seguenti aspetti sono importanti in Remotion:

- Le animazioni devono essere guidate da `useCurrentFrame()` e le animazioni fornite nativamente da Mapbox devono essere disabilitate. Per esempio, la prop `fadeDuration` deve essere impostata a `0`, `interactive` a `false`, ecc.
- Il caricamento della mappa deve essere ritardato usando `useDelayRender()` e la mappa deve essere impostata a `null` finché non è carica.
- L'elemento che contiene il ref DEVE avere larghezza e altezza esplicite e `position: "absolute"`.
- Non aggiungere una funzione di pulizia (cleanup) `_map.remove();`.

## Disegnare linee

A meno che io non lo richieda, non aggiungere un effetto bagliore (glow) alle linee.
A meno che io non lo richieda, non aggiungere punti supplementari alle linee.

## Stile della mappa

Per impostazione predefinita, usa lo stile `mapbox://styles/mapbox/standard`.  
Nascondi le etichette (labels) dallo stile della mappa di base.

A meno che io non richieda diversamente, rimuovi tutte le caratteristiche dallo stile Mapbox Standard.

```tsx
// Nasconde tutte le caratteristiche dello stile Mapbox Standard
const hideFeatures = [
  "showRoadsAndTransit",
  "showRoads",
  "showTransit",
  "showPedestrianRoads",
  "showRoadLabels",
  "showTransitLabels",
  "showPlaceLabels",
  "showPointOfInterestLabels",
  "showPointsOfInterest",
  "showAdminBoundaries",
  "showLandmarkIcons",
  "showLandmarkIconLabels",
  "show3dObjects",
  "show3dBuildings",
  "show3dTrees",
  "show3dLandmarks",
  "show3dFacades",
];
for (const feature of hideFeatures) {
  _map.setConfigProperty("basemap", feature, false);
}

_map.setConfigProperty("basemap", "colorMotorways", "transparent");
_map.setConfigProperty("basemap", "colorRoads", "transparent");
_map.setConfigProperty("basemap", "colorTrunks", "transparent");
```

## Animare la telecamera

Puoi animare la telecamera lungo la linea aggiungendo un hook `useEffect` che aggiorna la posizione della telecamera in base al frame corrente.

A meno che io non lo richieda, non saltare tra diverse angolazioni della telecamera.

```tsx
import * as turf from "@turf/turf";
import { interpolate } from "remotion";
import { Easing } from "remotion";
import { useCurrentFrame, useVideoConfig, useDelayRender } from "remotion";

const animationDuration = 20;
const cameraAltitude = 4000;
```

```tsx
const frame = useCurrentFrame();
const { fps } = useVideoConfig();
const { delayRender, continueRender } = useDelayRender();

useEffect(() => {
  if (!map) {
    return;
  }
  const handle = delayRender("Spostamento punto...");

  const routeDistance = turf.length(turf.lineString(lineCoordinates));

  const progress = interpolate(
    frame / fps,
    [0.00001, animationDuration],
    [0, 1],
    {
      easing: Easing.inOut(Easing.sin),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    },
  );

  const camera = map.getFreeCameraOptions();

  const alongRoute = turf.along(
    turf.lineString(lineCoordinates),
    routeDistance * progress,
  ).geometry.coordinates;

  camera.lookAtPoint({
    lng: alongRoute[0],
    lat: alongRoute[1],
  });

  map.setFreeCameraOptions(camera);
  map.once("idle", () => continueRender(handle));
}, [lineCoordinates, fps, frame, handle, map]);
```

Note:

IMPORTANTE: Mantieni la telecamera per impostazione predefinita con il nord rivolto verso l'alto.
IMPORTANTE: Per animazioni in più fasi, imposta tutte le proprietà in tutte le fasi (zoom, posizione, progresso della linea) per evitare salti. Sovrascrivi i valori iniziali.

- Il progresso è limitato (clamped) a un valore minimo per evitare che la linea sia vuota, il che può causare errori di turf.
- Vedi [Timing](./timing.md) per altre opzioni di temporizzazione.
- Considera le dimensioni della composizione e rendi le linee abbastanza spesse e la dimensione del carattere delle etichette abbastanza grande da essere leggibile quando la composizione viene ridimensionata.

## Animare le linee

### Linee rette (interpolazione lineare)

Per animare una linea che appare dritta sulla mappa, usa l'interpolazione lineare tra le coordinate. NON usare le funzioni `lineSliceAlong` o `along` di turf, poiché utilizzano calcoli geodetici (cerchio massimo) che appaiono curvi su una proiezione di Mercatore.

```tsx
const frame = useCurrentFrame();
const { durationInFrames } = useVideoConfig();

useEffect(() => {
  if (!map) return;

  const animationHandle = delayRender("Animazione linea...");

  const progress = interpolate(frame, [0, durationInFrames - 1], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.inOut(Easing.cubic),
  });

  // Interpolazione lineare per una linea dritta sulla mappa
  const start = lineCoordinates[0];
  const end = lineCoordinates[1];
  const currentLng = start[0] + (end[0] - start[0]) * progress;
  const currentLat = start[1] + (end[1] - start[1]) * progress;

  const lineData: GeoJSON.Feature<GeoJSON.LineString> = {
    type: "Feature",
    properties: {},
    geometry: {
      type: "LineString",
      coordinates: [start, [currentLng, currentLat]],
    },
  };

  const source = map.getSource("trace") as mapboxgl.GeoJSONSource;
  if (source) {
    source.setData(lineData);
  }

  map.once("idle", () => continueRender(animationHandle));
}, [frame, map, durationInFrames]);
```

### Linee curve (geodetiche/cerchio massimo)

Per animare una linea che segue il percorso geodetico (cerchio massimo) tra due punti, usa `lineSliceAlong` di turf. Questo è utile per mostrare rotte aeree o la distanza più breve effettiva sulla Terra.

```tsx
import * as turf from "@turf/turf";

const routeLine = turf.lineString(lineCoordinates);
const routeDistance = turf.length(routeLine);

const currentDistance = Math.max(0.001, routeDistance * progress);
const slicedLine = turf.lineSliceAlong(routeLine, 0, currentDistance);

const source = map.getSource("route") as mapboxgl.GeoJSONSource;
if (source) {
  source.setData(slicedLine);
}
```

## Marker

Aggiungi etichette e marker dove appropriato.

```tsx
_map.addSource("markers", {
  type: "geojson",
  data: {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        properties: { name: "Punto 1" },
        geometry: { type: "Point", coordinates: [-118.2437, 34.0522] },
      },
    ],
  },
});

_map.addLayer({
  id: "city-markers",
  type: "circle",
  source: "markers",
  paint: {
    "circle-radius": 40,
    "circle-color": "#FF4444",
    "circle-stroke-width": 4,
    "circle-stroke-color": "#FFFFFF",
  },
});

_map.addLayer({
  id: "labels",
  type: "symbol",
  source: "markers",
  layout: {
    "text-field": ["get", "name"],
    "text-font": ["DIN Pro Bold", "Arial Unicode MS Bold"],
    "text-size": 50,
    "text-offset": [0, 0.5],
    "text-anchor": "top",
  },
  paint: {
    "text-color": "#FFFFFF",
    "text-halo-color": "#000000",
    "text-halo-width": 2,
  },
});
```

Assicurati che siano abbastanza grandi. Controlla le dimensioni della composizione e scala le etichette di conseguenza.
Per una dimensione della composizione di 1920x1080, la dimensione del carattere dell'etichetta dovrebbe essere almeno 40px.

IMPORTANTE: Mantieni il `text-offset` abbastanza piccolo da farlo stare vicino al marker. Considera il raggio del cerchio del marker. Per un raggio del cerchio di 40, questo è un buon offset:

```tsx
"text-offset": [0, 0.5],
```

## Edifici 3D

Per abilitare gli edifici 3D, usa il seguente codice:

```tsx
_map.setConfigProperty("basemap", "show3dObjects", true);
_map.setConfigProperty("basemap", "show3dLandmarks", true);
_map.setConfigProperty("basemap", "show3dBuildings", true);
```

## Rendering

Quando renderizzi un'animazione di mappa, assicurati di renderizzare con i seguenti flag:

```
npx remotion render --gl=angle --concurrency=1
```
