---
name: fonts
description: Caricamento di Google Fonts e font locali in Remotion
metadata:
  tags: fonts, google-fonts, typography, text
---

# Uso dei font in Remotion

## Google Fonts con @remotion/google-fonts

Il modo consigliato per usare i Google Fonts. È type-safe e blocca automaticamente il rendering finché il font non è pronto.

### Prerequisiti

Innanzitutto, deve essere installato il pacchetto `@remotion/google-fonts`.
Se non lo è, usa il seguente comando:

```bash
npx remotion add @remotion/google-fonts # Se il progetto usa npm
bunx remotion add @remotion/google-fonts # Se il progetto usa bun
yarn remotion add @remotion/google-fonts # Se il progetto usa yarn
pnpm exec remotion add @remotion/google-fonts # Se il progetto usa pnpm
```

```tsx
import { loadFont } from "@remotion/google-fonts/Lobster";

const { fontFamily } = loadFont();

export const MyComposition = () => {
  return <div style={{ fontFamily }}>Ciao Mondo</div>;
};
```

Preferibilmente, specifica solo i pesi (weights) e i sottoinsieme (subsets) necessari per ridurre le dimensioni del file:

```tsx
import { loadFont } from "@remotion/google-fonts/Roboto";

const { fontFamily } = loadFont("normal", {
  weights: ["400", "700"],
  subsets: ["latin"],
});
```

### Attendere il caricamento del font

Usa `waitUntilDone()` se hai bisogno di sapere quando il font è pronto:

```tsx
import { loadFont } from "@remotion/google-fonts/Lobster";

const { fontFamily, waitUntilDone } = loadFont();

await waitUntilDone();
```

## Font locali con @remotion/fonts

Per i file di font locali, usa il pacchetto `@remotion/fonts`.

### Prerequisiti

Innanzitutto, installa `@remotion/fonts`:

```bash
npx remotion add @remotion/fonts # Se il progetto usa npm
bunx remotion add @remotion/fonts # Se il progetto usa bun
yarn remotion add @remotion/fonts # Se il progetto usa yarn
pnpm exec remotion add @remotion/fonts # Se il progetto usa pnpm
```

### Caricare un font locale

Posiziona il file del font nella cartella `public/` e usa `loadFont()`:

```tsx
import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

await loadFont({
  family: "MyFont",
  url: staticFile("MyFont-Regular.woff2"),
});

export const MyComposition = () => {
  return <div style={{ fontFamily: "MyFont" }}>Ciao Mondo</div>;
};
```

### Caricare più pesi (weights)

Carica ogni peso separatamente con lo stesso nome di famiglia:

```tsx
import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

await Promise.all([
  loadFont({
    family: "Inter",
    url: staticFile("Inter-Regular.woff2"),
    weight: "400",
  }),
  loadFont({
    family: "Inter",
    url: staticFile("Inter-Bold.woff2"),
    weight: "700",
  }),
]);
```

### Opzioni disponibili

```tsx
loadFont({
  family: "MyFont", // Richiesto: nome da usare nel CSS
  url: staticFile("font.woff2"), // Richiesto: URL del file del font
  format: "woff2", // Opzionale: rilevato automaticamente dall'estensione
  weight: "400", // Opzionale: peso del font
  style: "normal", // Opzionale: normal o italic
  display: "block", // Opzionale: comportamento font-display
});
```

## Utilizzo nei componenti

Chiama `loadFont()` al livello superiore del tuo componente o in un file separato che viene importato all'inizio:

```tsx
import { loadFont } from "@remotion/google-fonts/Montserrat";

const { fontFamily } = loadFont("normal", {
  weights: ["400", "700"],
  subsets: ["latin"],
});

export const Title: React.FC<{ text: string }> = ({ text }) => {
  return (
    <h1
      style={{
        fontFamily,
        fontSize: 80,
        fontWeight: "bold",
      }}
    >
      {text}
    </h1>
  );
};
```
