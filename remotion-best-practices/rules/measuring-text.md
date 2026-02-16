---
name: measuring-text
description: Misurare le dimensioni del testo, adattare il testo ai contenitori e controllare l'overflow
metadata:
  tags: measure, text, layout, dimensions, fitText, fillTextBox
---

# Misurare il testo in Remotion

## Prerequisiti

Installa `@remotion/layout-utils` se non è già installato:

```bash
npx remotion add @remotion/layout-utils
```

## Misurare le dimensioni del testo

Usa `measureText()` per calcolare la larghezza e l'altezza del testo:

```tsx
import { measureText } from "@remotion/layout-utils";

const { width, height } = measureText({
  text: "Ciao Mondo",
  fontFamily: "Arial",
  fontSize: 32,
  fontWeight: "bold",
});
```

I risultati vengono memorizzati nella cache: le chiamate duplicate restituiscono il risultato memorizzato.

## Adattare il testo a una larghezza

Usa `fitText()` per trovare la dimensione ottimale del carattere per un contenitore:

```tsx
import { fitText } from "@remotion/layout-utils";

const { fontSize } = fitText({
  text: "Ciao Mondo",
  withinWidth: 600,
  fontFamily: "Inter",
  fontWeight: "bold",
});

return (
  <div
    style={{
      fontSize: Math.min(fontSize, 80), // Limita a 80px
      fontFamily: "Inter",
      fontWeight: "bold",
    }}
  >
    Ciao Mondo
  </div>
);
```

## Controllare l'overflow del testo

Usa `fillTextBox()` per verificare se il testo supera un box:

```tsx
import { fillTextBox } from "@remotion/layout-utils";

const box = fillTextBox({ maxBoxWidth: 400, maxLines: 3 });

const words = ["Ciao", "Mondo", "Questo", "è", "un", "test"];
for (const word of words) {
  const { exceedsBox } = box.add({
    text: word + " ",
    fontFamily: "Arial",
    fontSize: 24,
  });
  if (exceedsBox) {
    // Il testo traboccherebbe, gestisci di conseguenza
    break;
  }
}
```

## Best practice

**Carica prima i font:** Chiama le funzioni di misurazione solo dopo che i font sono stati caricati.

```tsx
import { loadFont } from "@remotion/google-fonts/Inter";

const { fontFamily, waitUntilDone } = loadFont("normal", {
  weights: ["400"],
  subsets: ["latin"],
});

waitUntilDone().then(() => {
  // Ora è sicuro misurare
  const { width } = measureText({
    text: "Ciao",
    fontFamily,
    fontSize: 32,
  });
});
```

**Usa validateFontIsLoaded:** Rileva tempestivamente i problemi di caricamento dei font:

```tsx
measureText({
  text: "Ciao",
  fontFamily: "MyCustomFont",
  fontSize: 32,
  validateFontIsLoaded: true, // Lancia un errore se il font non è caricato
});
```

**Fai corrispondere le proprietà del font:** Usa le stesse proprietà per la misurazione e per il rendering:

```tsx
const fontStyle = {
  fontFamily: "Inter",
  fontSize: 32,
  fontWeight: "bold" as const,
  letterSpacing: "0.5px",
};

const { width } = measureText({
  text: "Ciao",
  ...fontStyle,
});

return <div style={fontStyle}>Ciao</div>;
```

**Evita padding e bordi:** Usa `outline` invece di `border` per prevenire differenze di layout:

```tsx
<div style={{ outline: "2px solid red" }}>Testo</div>
```
