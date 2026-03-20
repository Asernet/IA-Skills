---
name: parameters
description: Rendere un video parametrizzabile aggiungendo uno schema Zod
metadata:
  tags: parameters, zod, schema
---

Per rendere un video parametrizzabile, è possibile aggiungere uno schema Zod a una composizione.

Innanzitutto, deve essere installato `zod` - deve essere esattamente la versione `3.22.3`.

Cerca nel progetto i file di lock ed esegui il comando corretto a seconda del package manager:

Se viene trovato `package-lock.json`, usa il seguente comando:

```bash
npm i zod@3.22.3
```

Se viene trovato `bun.lockb`, usa il seguente comando:

```bash
bun i zod@3.22.3
```

Se viene trovato `yarn.lock`, usa il seguente comando:

```bash
yarn add zod@3.22.3
```

Se viene trovato `pnpm-lock.yaml`, usa il seguente comando:

```bash
pnpm i zod@3.22.3
```

Quindi, è possibile definire uno schema Zod insieme al componente:

```tsx title="src/MyComposition.tsx"
import { z } from "zod";

export const MyCompositionSchema = z.object({
  title: z.string(),
});

const MyComponent: React.FC<z.infer<typeof MyCompositionSchema>> = () => {
  return (
    <div>
      <h1>{props.title}</h1>
    </div>
  );
};
```

Nel file principale (root), lo schema può essere passato alla composizione:

```tsx title="src/Root.tsx"
import { Composition } from "remotion";
import { MycComponent, MyCompositionSchema } from "./MyComposition";

export const RemotionRoot = () => {
  return (
    <Composition
      id="MyComposition"
      component={MyComponent}
      durationInFrames={100}
      fps={30}
      width={1080}
      height={1080}
      defaultProps={{ title: "Hello World" }}
      schema={MyCompositionSchema}
    />
  );
};
```

Ora l'utente può modificare il parametro visivamente nella barra laterale.

Tutti gli schemi supportati da Zod sono supportati da Remotion.

Remotion richiede che il tipo di primo livello sia un `z.object()`, perché la collezione di props di un componente React è sempre un oggetto.

## Selettore di colore (Color picker)

Per aggiungere un selettore di colore, usa `zColor()` da `@remotion/zod-types`.

Se non è installato, usa il seguente comando:

```bash
npx remotion add @remotion/zod-types # Se il progetto usa npm
bunx remotion add @remotion/zod-types # Se il progetto usa bun
yarn remotion add @remotion/zod-types # Se il progetto usa yarn
pnpm exec remotion add @remotion/zod-types # Se il progetto usa pnpm
```

Quindi importa `zColor` da `@remotion/zod-types`:

```tsx
import { zColor } from "@remotion/zod-types";
```

Quindi usalo nello schema:

```tsx
export const MyCompositionSchema = z.object({
  color: zColor(),
});
```
