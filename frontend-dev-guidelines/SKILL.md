---
name: frontend-dev-guidelines
description: Linee guida sviluppo frontend per applicazioni React/TypeScript. Pattern moderni inclusi Suspense, lazy loading, useSuspenseQuery, organizzazione file con directory features, styling MUI v7, TanStack Router e ottimizzazione performance.
---

# Linee Guida Sviluppo Frontend

## Scopo

Guida completa per sviluppo React moderno, con enfasi su data fetching basato su Suspense, lazy loading, organizzazione file appropriata e ottimizzazione performance.

## Quando Usare Questa Skill

- Creazione nuovi componenti o pagine
- Costruzione nuove feature
- Fetching dati con TanStack Query
- Setup routing con TanStack Router
- Styling componenti con MUI v7
- Ottimizzazione performance
- Organizzazione codice frontend
- Best practice TypeScript

---

## Quick Start

### Checklist Nuovo Componente

Stai creando un componente? Segui questa checklist:

- [ ] Usa pattern `React.FC<Props>` con TypeScript
- [ ] Lazy load se componente pesante: `React.lazy(() => import())`
- [ ] Wrappa in `<SuspenseLoader>` per stati loading
- [ ] Usa `useSuspenseQuery` per data fetching
- [ ] Alias import: `@/`, `~types`, `~components`, `~features`
- [ ] Stili: Inline se <100 righe, file separato se >100 righe
- [ ] Usa `useCallback` per event handler passati ai children
- [ ] Default export in fondo
- [ ] Nessun early return con loading spinner
- [ ] Usa `useMuiSnackbar` per notifiche utente

### Checklist Nuova Feature

Stai creando una feature? Imposta questa struttura:

- [ ] Crea directory `features/{feature-name}/`
- [ ] Crea subdirectory: `api/`, `components/`, `hooks/`, `helpers/`, `types/`
- [ ] Crea file API service: `api/{feature}Api.ts`
- [ ] Setup tipi TypeScript in `types/`
- [ ] Crea route in `routes/{feature-name}/index.tsx`
- [ ] Lazy load componenti feature
- [ ] Usa Suspense boundary
- [ ] Esporta API pubblica da feature `index.ts`

---

## Riferimento Rapido Alias Import

| Alias         | Risolve A        | Esempio                                                       |
| ------------- | ---------------- | ------------------------------------------------------------- |
| `@/`          | `src/`           | `import { apiClient } from '@/lib/apiClient'`                 |
| `~types`      | `src/types`      | `import type { User } from '~types/user'`                     |
| `~components` | `src/components` | `import { SuspenseLoader } from '~components/SuspenseLoader'` |
| `~features`   | `src/features`   | `import { authApi } from '~features/auth'`                    |

---

## Cheatsheet Import Comuni

```typescript
// React & Lazy Loading
import React, { useState, useCallback, useMemo } from "react";
const Heavy = React.lazy(() => import("./Heavy"));

// Componenti MUI
import { Box, Paper, Typography, Button, Grid } from "@mui/material";
import type { SxProps, Theme } from "@mui/material";

// TanStack Query (Suspense)
import { useSuspenseQuery, useQueryClient } from "@tanstack/react-query";

// TanStack Router
import { createFileRoute } from "@tanstack/react-router";

// Componenti Progetto
import { SuspenseLoader } from "~components/SuspenseLoader";

// Hook
import { useAuth } from "@/hooks/useAuth";
import { useMuiSnackbar } from "@/hooks/useMuiSnackbar";

// Tipi
import type { Post } from "~types/post";
```

---

## Guide per Argomento

### 🎨 Pattern Componenti

**I componenti React moderni usano:**

- `React.FC<Props>` per type safety
- `React.lazy()` per code splitting
- `SuspenseLoader` per stati loading
- Pattern named const + default export

**Concetti Chiave:**

- Lazy load componenti pesanti (DataGrid, chart, editor)
- Wrappa sempre i componenti lazy in Suspense
- Usa componente SuspenseLoader (con animazione fade)
- Struttura componente: Props → Hook → Handler → Render → Export

---

### 📊 Data Fetching

**PATTERN PRIMARIO: useSuspenseQuery**

- Usa con Suspense boundary
- Strategia cache-first (controlla cache grid prima di API)
- Sostituisce controlli `isLoading`
- Type-safe con generics

**Layer API Service:**

- Crea `features/{feature}/api/{feature}Api.ts`
- Usa istanza axios `apiClient`
- Metodi centralizzati per feature
- Formato route: `/form/route` (NON `/api/form/route`)

---

### 📁 Organizzazione File

**features/ vs components/:**

- `features/`: Domain-specifico (post, commenti, auth)
- `components/`: Veramente riutilizzabile (SuspenseLoader, CustomAppBar)

**Subdirectory Feature:**

```
features/
  my-feature/
    api/          # Layer API service
    components/   # Componenti feature
    hooks/        # Hook custom
    helpers/      # Funzioni utility
    types/        # Tipi TypeScript
```

---

### 🎨 Styling

**Inline vs Separato:**

- <100 righe: Inline `const styles: Record<string, SxProps<Theme>>`
- > 100 righe: File `.styles.ts` separato

**Metodo Primario:**

- Usa prop `sx` per componenti MUI
- Type-safe con `SxProps<Theme>`
- Accesso tema: `(theme) => theme.palette.primary.main`

**Grid MUI v7:**

```typescript
<Grid size={{ xs: 12, md: 6 }}>  // ✅ sintassi v7
<Grid xs={12} md={6}>             // ❌ sintassi vecchia
```

---

### 🛣️ Routing

**TanStack Router - Folder-Based:**

- Directory: `routes/my-route/index.tsx`
- Lazy load componenti
- Usa `createFileRoute`
- Dati breadcrumb nel loader

**Esempio:**

```typescript
import { createFileRoute } from "@tanstack/react-router";
import { lazy } from "react";

const MyPage = lazy(() => import("@/features/my-feature/components/MyPage"));

export const Route = createFileRoute("/my-route/")({
  component: MyPage,
  loader: () => ({ crumb: "La Mia Route" }),
});
```

---

### ⏳ Stati Loading ed Errore

**REGOLA CRITICA: Nessun Early Return**

```typescript
// ❌ MAI - Causa layout shift
if (isLoading) {
    return <LoadingSpinner />;
}

// ✅ SEMPRE - Layout consistente
<SuspenseLoader>
    <Content />
</SuspenseLoader>
```

**Perché:** Previene Cumulative Layout Shift (CLS), UX migliore

**Gestione Errori:**

- Usa `useMuiSnackbar` per feedback utente
- MAI `react-toastify`
- Callback `onError` di TanStack Query

---

### ⚡ Performance

**Pattern Ottimizzazione:**

- `useMemo`: Computazioni costose (filter, sort, map)
- `useCallback`: Event handler passati ai children
- `React.memo`: Componenti costosi
- Ricerca debounced (300-500ms)
- Prevenzione memory leak (cleanup in useEffect)

---

### 📘 TypeScript

**Standard:**

- Strict mode, nessun tipo `any`
- Return type espliciti sulle funzioni
- Type import: `import type { User } from '~types/user'`
- Interfacce prop componenti con JSDoc

---

## Principi Core

1. **Lazy Load Tutto il Pesante**: Route, DataGrid, chart, editor
2. **Suspense per Loading**: Usa SuspenseLoader, non early return
3. **useSuspenseQuery**: Pattern primario data fetching per nuovo codice
4. **Feature Organizzate**: Subdirectory api/, components/, hooks/, helpers/
5. **Stili Basati su Dimensione**: <100 inline, >100 separato
6. **Alias Import**: Usa @/, ~types, ~components, ~features
7. **Nessun Early Return**: Previene layout shift
8. **useMuiSnackbar**: Per tutte le notifiche utente

---

## Template Componente Moderno (Copia Rapida)

```typescript
import React, { useState, useCallback } from 'react';
import { Box, Paper } from '@mui/material';
import { useSuspenseQuery } from '@tanstack/react-query';
import { featureApi } from '../api/featureApi';
import type { FeatureData } from '~types/feature';

interface MyComponentProps {
    id: number;
    onAction?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ id, onAction }) => {
    const [state, setState] = useState<string>('');

    const { data } = useSuspenseQuery({
        queryKey: ['feature', id],
        queryFn: () => featureApi.getFeature(id),
    });

    const handleAction = useCallback(() => {
        setState('updated');
        onAction?.();
    }, [onAction]);

    return (
        <Box sx={{ p: 2 }}>
            <Paper sx={{ p: 3 }}>
                {/* Contenuto */}
            </Paper>
        </Box>
    );
};

export default MyComponent;
```

---

## Skill Correlate

- **docker-expert**: Containerizzazione applicazioni frontend
