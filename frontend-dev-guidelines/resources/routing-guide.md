# Guida Routing

Implementazione TanStack Router con routing folder-based e pattern lazy loading.

---

## Panoramica TanStack Router

**TanStack Router** con routing file-based:

- Struttura cartelle definisce le route
- Lazy loading per code splitting
- Routing type-safe
- Loader breadcrumb

---

## Routing Folder-Based

### Struttura Directory

```
routes/
  __root.tsx                    # Layout root
  index.tsx                     # Route home (/)
  posts/
    index.tsx                   # /posts
    create/
      index.tsx                 # /posts/create
    $postId.tsx                 # /posts/:postId (dinamico)
  comments/
    index.tsx                   # /comments
```

**Pattern**:

- `index.tsx` = Route a quel path
- `$param.tsx` = Parametro dinamico
- Cartelle annidate = Route annidate

---

## Pattern Route Base

### Esempio da posts/index.tsx

```typescript
/**
 * Componente route posts
 * Visualizza la lista principale dei blog post
 */

import { createFileRoute } from '@tanstack/react-router';
import { lazy } from 'react';

// Lazy load il componente pagina
const PostsList = lazy(() =>
    import('@/features/posts/components/PostsList').then(
        (module) => ({ default: module.PostsList }),
    ),
);

export const Route = createFileRoute('/posts/')({
    component: PostsPage,
    // Definisci dati breadcrumb
    loader: () => ({
        crumb: 'Posts',
    }),
});

function PostsPage() {
    return (
        <PostsList
            title='Tutti i Post'
            showFilters={true}
        />
    );
}

export default PostsPage;
```

**Punti Chiave:**

- Lazy load componenti pesanti
- `createFileRoute` con path route
- `loader` per dati breadcrumb
- Componente pagina renderizza contenuto
- Esporta sia Route che componente

---

## Lazy Loading Route

### Pattern Named Export

```typescript
import { lazy } from "react";

// Per named export, usa .then() per mappare a default
const MyPage = lazy(() =>
  import("@/features/my-feature/components/MyPage").then((module) => ({
    default: module.MyPage,
  })),
);
```

### Pattern Default Export

```typescript
import { lazy } from "react";

// Per default export, sintassi più semplice
const MyPage = lazy(() => import("@/features/my-feature/components/MyPage"));
```

### Perché Lazy Load le Route?

- Code splitting - bundle iniziale più piccolo
- Caricamento pagina iniziale più veloce
- Carica codice route solo quando navigato
- Performance migliore

---

## createFileRoute

### Configurazione Base

```typescript
export const Route = createFileRoute('/my-route/')({
    component: MyRoutePage,
});

function MyRoutePage() {
    return <div>Contenuto La Mia Route</div>;
}
```

### Con Loader Breadcrumb

```typescript
export const Route = createFileRoute("/my-route/")({
  component: MyRoutePage,
  loader: () => ({
    crumb: "Titolo La Mia Route",
  }),
});
```

Il breadcrumb appare automaticamente nella navigazione/app bar.

### Con Data Loader

```typescript
export const Route = createFileRoute("/my-route/")({
  component: MyRoutePage,
  loader: async () => {
    // Può prefetch dati qui
    const data = await api.getData();
    return { crumb: "La Mia Route", data };
  },
});
```

### Con Search Params

```typescript
export const Route = createFileRoute("/search/")({
  component: SearchPage,
  validateSearch: (search: Record<string, unknown>) => {
    return {
      query: (search.query as string) || "",
      page: Number(search.page) || 1,
    };
  },
});

function SearchPage() {
  const { query, page } = Route.useSearch();
  // Usa query e page
}
```

---

## Route Dinamiche

### Route con Parametri

```typescript
// routes/users/$userId.tsx

export const Route = createFileRoute('/users/$userId')({
    component: UserPage,
});

function UserPage() {
    const { userId } = Route.useParams();

    return <UserProfile userId={userId} />;
}
```

### Parametri Multipli

```typescript
// routes/posts/$postId/comments/$commentId.tsx

export const Route = createFileRoute('/posts/$postId/comments/$commentId')({
    component: CommentPage,
});

function CommentPage() {
    const { postId, commentId } = Route.useParams();

    return <CommentEditor postId={postId} commentId={commentId} />;
}
```

---

## Navigazione

### Navigazione Programmatica

```typescript
import { useNavigate } from '@tanstack/react-router';

export const MyComponent: React.FC = () => {
    const navigate = useNavigate();

    const handleClick = () => {
        navigate({ to: '/posts' });
    };

    return <Button onClick={handleClick}>Vedi Post</Button>;
};
```

### Con Parametri

```typescript
const handleNavigate = () => {
  navigate({
    to: "/users/$userId",
    params: { userId: "123" },
  });
};
```

### Con Search Params

```typescript
const handleSearch = () => {
  navigate({
    to: "/search",
    search: { query: "test", page: 1 },
  });
};
```

---

## Pattern Layout Route

### Layout Root (\_\_root.tsx)

```typescript
import { createRootRoute, Outlet } from '@tanstack/react-router';
import { Box } from '@mui/material';
import { CustomAppBar } from '~components/CustomAppBar';

export const Route = createRootRoute({
    component: RootLayout,
});

function RootLayout() {
    return (
        <Box>
            <CustomAppBar />
            <Box sx={{ p: 2 }}>
                <Outlet />  {/* Le route figlie renderizzano qui */}
            </Box>
        </Box>
    );
}
```

### Layout Annidati

```typescript
// routes/dashboard/index.tsx
export const Route = createFileRoute('/dashboard/')({
    component: DashboardLayout,
});

function DashboardLayout() {
    return (
        <Box>
            <DashboardSidebar />
            <Box sx={{ flex: 1 }}>
                <Outlet />  {/* Route annidate */}
            </Box>
        </Box>
    );
}
```

---

## Esempio Route Completo

```typescript
/**
 * Route profilo utente
 * Path: /users/:userId
 */

import { createFileRoute } from '@tanstack/react-router';
import { lazy } from 'react';
import { SuspenseLoader } from '~components/SuspenseLoader';

// Lazy load componente pesante
const UserProfile = lazy(() =>
    import('@/features/users/components/UserProfile').then(
        (module) => ({ default: module.UserProfile })
    )
);

export const Route = createFileRoute('/users/$userId')({
    component: UserPage,
    loader: () => ({
        crumb: 'Profilo Utente',
    }),
});

function UserPage() {
    const { userId } = Route.useParams();

    return (
        <SuspenseLoader>
            <UserProfile userId={userId} />
        </SuspenseLoader>
    );
}

export default UserPage;
```

---

## Riepilogo

**Checklist Routing:**

- ✅ Folder-based: `routes/my-route/index.tsx`
- ✅ Lazy load componenti: `React.lazy(() => import())`
- ✅ Usa `createFileRoute` con path route
- ✅ Aggiungi breadcrumb nella funzione `loader`
- ✅ Wrappa in `SuspenseLoader` per stati loading
- ✅ Usa `Route.useParams()` per parametri dinamici
- ✅ Usa `useNavigate()` per navigazione programmatica

**Vedi Anche:**

- [component-patterns.md](component-patterns.md) - Pattern lazy loading
- [loading-and-error-states.md](loading-and-error-states.md) - Utilizzo SuspenseLoader
- [complete-examples.md](complete-examples.md) - Esempi route completi
