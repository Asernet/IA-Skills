# Pattern Componenti

Architettura componenti React moderna per l'applicazione con enfasi su type safety, lazy loading e Suspense boundary.

---

## Pattern React.FC (PREFERITO)

### Perché React.FC

Tutti i componenti usano il pattern `React.FC<Props>` per:

- Type safety esplicita per le props
- Firme componenti consistenti
- Documentazione interfaccia props chiara
- Migliore autocomplete IDE

### Pattern Base

```typescript
import React from 'react';

interface MyComponentProps {
    /** ID utente da visualizzare */
    userId: number;
    /** Callback opzionale quando avviene un'azione */
    onAction?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ userId, onAction }) => {
    return (
        <div>
            Utente: {userId}
        </div>
    );
};

export default MyComponent;
```

**Punti Chiave:**

- Interfaccia props definita separatamente con commenti JSDoc
- `React.FC<Props>` fornisce type safety
- Destruttura props nei parametri
- Export default in fondo

---

## Pattern Lazy Loading

### Quando Fare Lazy Load

Lazy load componenti che sono:

- Pesanti (DataGrid, chart, editor rich text)
- Componenti a livello route
- Contenuti modal/dialog (non mostrati inizialmente)
- Contenuti below-the-fold

### Come Fare Lazy Load

```typescript
import React from "react";

// Lazy load componente pesante
const PostDataGrid = React.lazy(() => import("./grids/PostDataGrid"));

// Per export con nome
const MyComponent = React.lazy(() =>
  import("./MyComponent").then((module) => ({
    default: module.MyComponent,
  })),
);
```

**Esempio da PostTable.tsx:**

```typescript
/**
 * Componente container principale tabella post
 */
import React, { useState, useCallback } from 'react';
import { Box, Paper } from '@mui/material';

// Lazy load PostDataGrid per ottimizzare bundle size
const PostDataGrid = React.lazy(() => import('./grids/PostDataGrid'));

import { SuspenseLoader } from '~components/SuspenseLoader';

export const PostTable: React.FC<PostTableProps> = ({ formId }) => {
    return (
        <Box>
            <SuspenseLoader>
                <PostDataGrid formId={formId} />
            </SuspenseLoader>
        </Box>
    );
};

export default PostTable;
```

---

## Suspense Boundary

### Componente SuspenseLoader

**Import:**

```typescript
import { SuspenseLoader } from "~components/SuspenseLoader";
// Oppure
import { SuspenseLoader } from "@/components/SuspenseLoader";
```

**Utilizzo:**

```typescript
<SuspenseLoader>
    <LazyLoadedComponent />
</SuspenseLoader>
```

**Cosa fa:**

- Mostra indicatore loading mentre il componente lazy si carica
- Animazione fade-in fluida
- Esperienza loading consistente
- Previene layout shift

### Dove Posizionare i Suspense Boundary

**Livello Route:**

```typescript
// routes/my-route/index.tsx
const MyPage = lazy(() => import('@/features/my-feature/components/MyPage'));

function Route() {
    return (
        <SuspenseLoader>
            <MyPage />
        </SuspenseLoader>
    );
}
```

**Livello Componente:**

```typescript
function ParentComponent() {
    return (
        <Box>
            <Header />
            <SuspenseLoader>
                <HeavyDataGrid />
            </SuspenseLoader>
        </Box>
    );
}
```

**Boundary Multipli:**

```typescript
function Page() {
    return (
        <Box>
            <SuspenseLoader>
                <HeaderSection />
            </SuspenseLoader>

            <SuspenseLoader>
                <MainContent />
            </SuspenseLoader>

            <SuspenseLoader>
                <Sidebar />
            </SuspenseLoader>
        </Box>
    );
}
```

Ogni sezione si carica indipendentemente, UX migliore.

---

## Template Struttura Componente

### Ordine Raccomandato

```typescript
/**
 * Descrizione componente
 * Cosa fa, quando usarlo
 */
import React, { useState, useCallback, useMemo, useEffect } from 'react';
import { Box, Paper, Button } from '@mui/material';
import type { SxProps, Theme } from '@mui/material';
import { useSuspenseQuery } from '@tanstack/react-query';

// Import feature
import { myFeatureApi } from '../api/myFeatureApi';
import type { MyData } from '~types/myData';

// Import componenti
import { SuspenseLoader } from '~components/SuspenseLoader';

// Hook
import { useAuth } from '@/hooks/useAuth';
import { useMuiSnackbar } from '@/hooks/useMuiSnackbar';

// 1. INTERFACCIA PROPS (con JSDoc)
interface MyComponentProps {
    /** ID dell'entità da visualizzare */
    entityId: number;
    /** Callback opzionale quando l'azione completa */
    onComplete?: () => void;
    /** Modalità visualizzazione */
    mode?: 'view' | 'edit';
}

// 2. STILI (se inline e <100 righe)
const componentStyles: Record<string, SxProps<Theme>> = {
    container: {
        p: 2,
        display: 'flex',
        flexDirection: 'column',
    },
    header: {
        mb: 2,
        display: 'flex',
        justifyContent: 'space-between',
    },
};

// 3. DEFINIZIONE COMPONENTE
export const MyComponent: React.FC<MyComponentProps> = ({
    entityId,
    onComplete,
    mode = 'view',
}) => {
    // 4. HOOK (in questo ordine)
    // - Hook context prima
    const { user } = useAuth();
    const { showSuccess, showError } = useMuiSnackbar();

    // - Data fetching
    const { data } = useSuspenseQuery({
        queryKey: ['myEntity', entityId],
        queryFn: () => myFeatureApi.getEntity(entityId),
    });

    // - Stato locale
    const [selectedItem, setSelectedItem] = useState<string | null>(null);
    const [isEditing, setIsEditing] = useState(mode === 'edit');

    // - Valori memoizzati
    const filteredData = useMemo(() => {
        return data.filter(item => item.active);
    }, [data]);

    // - Effect
    useEffect(() => {
        // Setup
        return () => {
            // Cleanup
        };
    }, []);

    // 5. EVENT HANDLER (con useCallback)
    const handleItemSelect = useCallback((itemId: string) => {
        setSelectedItem(itemId);
    }, []);

    const handleSave = useCallback(async () => {
        try {
            await myFeatureApi.updateEntity(entityId, { /* data */ });
            showSuccess('Entità aggiornata con successo');
            onComplete?.();
        } catch (error) {
            showError('Aggiornamento entità fallito');
        }
    }, [entityId, onComplete, showSuccess, showError]);

    // 6. RENDER
    return (
        <Box sx={componentStyles.container}>
            <Box sx={componentStyles.header}>
                <h2>Il Mio Componente</h2>
                <Button onClick={handleSave}>Salva</Button>
            </Box>

            <Paper sx={{ p: 2 }}>
                {filteredData.map(item => (
                    <div key={item.id}>{item.name}</div>
                ))}
            </Paper>
        </Box>
    );
};

// 7. EXPORT (default export in fondo)
export default MyComponent;
```

---

## Separazione Componenti

### Quando Dividere i Componenti

**Dividi in componenti multipli quando:**

- Componente supera 300 righe
- Responsabilità distinte multiple
- Sezioni riutilizzabili
- JSX annidato complesso

**Esempio:**

```typescript
// ❌ EVITA - Monolitico
function MassiveComponent() {
    // 500+ righe
    // Logica ricerca
    // Logica filtro
    // Logica grid
    // Logica pannello azioni
}

// ✅ PREFERITO - Modulare
function ParentContainer() {
    return (
        <Box>
            <SearchAndFilter onFilter={handleFilter} />
            <DataGrid data={filteredData} />
            <ActionPanel onAction={handleAction} />
        </Box>
    );
}
```

### Quando Tenere Insieme

**Tieni nello stesso file quando:**

- Componente < 200 righe
- Logica strettamente accoppiata
- Non riutilizzabile altrove
- Componente presentazione semplice

---

## Pattern Export

### Named Const + Default Export (PREFERITO)

```typescript
export const MyComponent: React.FC<Props> = ({ ... }) => {
    // Logica componente
};

export default MyComponent;
```

**Perché:**

- Named export per testing/refactoring
- Default export per comodità lazy loading
- Entrambe le opzioni disponibili ai consumatori

### Lazy Loading Named Export

```typescript
const MyComponent = React.lazy(() =>
  import("./MyComponent").then((module) => ({
    default: module.MyComponent,
  })),
);
```

---

## Comunicazione Componenti

### Props Giù, Eventi Su

```typescript
// Parent
function Parent() {
    const [selectedId, setSelectedId] = useState<string | null>(null);

    return (
        <Child
            data={data}                    // Props giù
            onSelect={setSelectedId}       // Eventi su
        />
    );
}

// Child
interface ChildProps {
    data: Data[];
    onSelect: (id: string) => void;
}

export const Child: React.FC<ChildProps> = ({ data, onSelect }) => {
    return (
        <div onClick={() => onSelect(data[0].id)}>
            {/* Contenuto */}
        </div>
    );
};
```

### Evita Prop Drilling

**Usa context per nesting profondo:**

```typescript
// ❌ EVITA - Prop drilling 5+ livelli
<A prop={x}>
  <B prop={x}>
    <C prop={x}>
      <D prop={x}>
        <E prop={x} />  // Finalmente lo usa qui
      </D>
    </C>
  </B>
</A>

// ✅ PREFERITO - Context o TanStack Query
const MyContext = createContext<MyData | null>(null);

function Provider({ children }) {
    const { data } = useSuspenseQuery({ ... });
    return <MyContext.Provider value={data}>{children}</MyContext.Provider>;
}

function DeepChild() {
    const data = useContext(MyContext);
    // Usa data direttamente
}
```

---

## Pattern Avanzati

### Compound Components

```typescript
// Card.tsx
export const Card: React.FC<CardProps> & {
    Header: typeof CardHeader;
    Body: typeof CardBody;
    Footer: typeof CardFooter;
} = ({ children }) => {
    return <Paper>{children}</Paper>;
};

Card.Header = CardHeader;
Card.Body = CardBody;
Card.Footer = CardFooter;

// Utilizzo
<Card>
    <Card.Header>Titolo</Card.Header>
    <Card.Body>Contenuto</Card.Body>
    <Card.Footer>Azioni</Card.Footer>
</Card>
```

### Render Props (Raro, ma utile)

```typescript
interface DataProviderProps {
    children: (data: Data) => React.ReactNode;
}

export const DataProvider: React.FC<DataProviderProps> = ({ children }) => {
    const { data } = useSuspenseQuery({ ... });
    return <>{children(data)}</>;
};

// Utilizzo
<DataProvider>
    {(data) => <Display data={data} />}
</DataProvider>
```

---

## Riepilogo

**Ricetta Componente Moderno:**

1. `React.FC<Props>` con TypeScript
2. Lazy load se pesante: `React.lazy(() => import())`
3. Wrappa in `<SuspenseLoader>` per loading
4. Usa `useSuspenseQuery` per dati
5. Alias import (@/, ~types, ~components)
6. Event handler con `useCallback`
7. Default export in fondo
8. Nessun early return per stati loading

**Vedi Anche:**

- [data-fetching.md](data-fetching.md) - Dettagli useSuspenseQuery
- [loading-and-error-states.md](loading-and-error-states.md) - Best practice Suspense
- [complete-examples.md](complete-examples.md) - Esempi completi funzionanti
