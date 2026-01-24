# Pattern Comuni

Pattern usati frequentemente per form, autenticazione, DataGrid, dialog e altri elementi UI comuni.

---

## Autenticazione con useAuth

### Ottenere l'Utente Corrente

```typescript
import { useAuth } from '@/hooks/useAuth';

export const MyComponent: React.FC = () => {
    const { user } = useAuth();

    // Proprietà disponibili:
    // - user.id: string
    // - user.email: string
    // - user.username: string
    // - user.roles: string[]

    return (
        <div>
            <p>Loggato come: {user.email}</p>
            <p>Username: {user.username}</p>
            <p>Ruoli: {user.roles.join(', ')}</p>
        </div>
    );
};
```

**MAI fare chiamate API dirette per auth** - usa sempre l'hook `useAuth`.

---

## Form con React Hook Form

### Form Base

```typescript
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { TextField, Button } from '@mui/material';
import { useMuiSnackbar } from '@/hooks/useMuiSnackbar';

// Schema Zod per validazione
const formSchema = z.object({
    username: z.string().min(3, 'Username deve avere almeno 3 caratteri'),
    email: z.string().email('Indirizzo email non valido'),
    age: z.number().min(18, 'Devi avere almeno 18 anni'),
});

type FormData = z.infer<typeof formSchema>;

export const MyForm: React.FC = () => {
    const { showSuccess, showError } = useMuiSnackbar();

    const { register, handleSubmit, formState: { errors } } = useForm<FormData>({
        resolver: zodResolver(formSchema),
        defaultValues: {
            username: '',
            email: '',
            age: 18,
        },
    });

    const onSubmit = async (data: FormData) => {
        try {
            await api.submitForm(data);
            showSuccess('Form inviato con successo');
        } catch (error) {
            showError('Invio form fallito');
        }
    };

    return (
        <form onSubmit={handleSubmit(onSubmit)}>
            <TextField
                {...register('username')}
                label='Username'
                error={!!errors.username}
                helperText={errors.username?.message}
            />

            <TextField
                {...register('email')}
                label='Email'
                error={!!errors.email}
                helperText={errors.email?.message}
                type='email'
            />

            <TextField
                {...register('age', { valueAsNumber: true })}
                label='Età'
                error={!!errors.age}
                helperText={errors.age?.message}
                type='number'
            />

            <Button type='submit' variant='contained'>
                Invia
            </Button>
        </form>
    );
};
```

---

## Pattern Componente Dialog

### Struttura Dialog Standard

Da BEST_PRACTICES.md - Tutti i dialog devono avere:

- Icona nel titolo
- Pulsante chiusura (X)
- Pulsanti azione in basso

```typescript
import { Dialog, DialogTitle, DialogContent, DialogActions, Button, IconButton } from '@mui/material';
import { Close, Info } from '@mui/icons-material';

interface MyDialogProps {
    open: boolean;
    onClose: () => void;
    onConfirm: () => void;
}

export const MyDialog: React.FC<MyDialogProps> = ({ open, onClose, onConfirm }) => {
    return (
        <Dialog open={open} onClose={onClose} maxWidth='sm' fullWidth>
            <DialogTitle>
                <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <Info color='primary' />
                        Titolo Dialog
                    </Box>
                    <IconButton onClick={onClose} size='small'>
                        <Close />
                    </IconButton>
                </Box>
            </DialogTitle>

            <DialogContent>
                {/* Contenuto qui */}
            </DialogContent>

            <DialogActions>
                <Button onClick={onClose}>Annulla</Button>
                <Button onClick={onConfirm} variant='contained'>
                    Conferma
                </Button>
            </DialogActions>
        </Dialog>
    );
};
```

---

## Pattern Wrapper DataGrid

### Contratto Componente Wrapper

Da BEST_PRACTICES.md - I wrapper DataGrid devono accettare:

**Props Obbligatorie:**

- `rows`: Array dati
- `columns`: Definizioni colonne
- Stati loading/errore

**Props Opzionali:**

- Componenti toolbar
- Azioni custom
- Stato iniziale

```typescript
import { DataGridPro } from '@mui/x-data-grid-pro';
import type { GridColDef } from '@mui/x-data-grid-pro';

interface DataGridWrapperProps {
    rows: any[];
    columns: GridColDef[];
    loading?: boolean;
    toolbar?: React.ReactNode;
    onRowClick?: (row: any) => void;
}

export const DataGridWrapper: React.FC<DataGridWrapperProps> = ({
    rows,
    columns,
    loading = false,
    toolbar,
    onRowClick,
}) => {
    return (
        <DataGridPro
            rows={rows}
            columns={columns}
            loading={loading}
            slots={{ toolbar: toolbar ? () => toolbar : undefined }}
            onRowClick={(params) => onRowClick?.(params.row)}
            // Configurazione standard
            pagination
            pageSizeOptions={[25, 50, 100]}
            initialState={{
                pagination: { paginationModel: { pageSize: 25 } },
            }}
        />
    );
};
```

---

## Pattern Mutation

### Aggiornamento con Invalidazione Cache

```typescript
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useMuiSnackbar } from "@/hooks/useMuiSnackbar";

export const useUpdateEntity = () => {
  const queryClient = useQueryClient();
  const { showSuccess, showError } = useMuiSnackbar();

  return useMutation({
    mutationFn: ({ id, data }: { id: number; data: any }) =>
      api.updateEntity(id, data),

    onSuccess: (result, variables) => {
      // Invalida query interessate
      queryClient.invalidateQueries({ queryKey: ["entity", variables.id] });
      queryClient.invalidateQueries({ queryKey: ["entities"] });

      showSuccess("Entità aggiornata");
    },

    onError: () => {
      showError("Aggiornamento entità fallito");
    },
  });
};

// Utilizzo
const updateEntity = useUpdateEntity();

const handleSave = () => {
  updateEntity.mutate({ id: 123, data: { name: "Nuovo Nome" } });
};
```

---

## Pattern Gestione Stato

### TanStack Query per Stato Server (PRIMARIO)

Usa TanStack Query per **tutti i dati server**:

- Fetching: useSuspenseQuery
- Mutation: useMutation
- Caching: Automatico
- Sincronizzazione: Built-in

```typescript
// ✅ CORRETTO - TanStack Query per dati server
const { data: users } = useSuspenseQuery({
  queryKey: ["users"],
  queryFn: () => userApi.getUsers(),
});
```

### useState per Stato UI

Usa `useState` per **solo stato UI locale**:

- Input form (non controllati)
- Modal aperto/chiuso
- Tab selezionata
- Flag UI temporanei

```typescript
// ✅ CORRETTO - useState per stato UI
const [modalOpen, setModalOpen] = useState(false);
const [selectedTab, setSelectedTab] = useState(0);
```

### Zustand per Stato Client Globale (Minimale)

Usa Zustand solo per **stato client globale**:

- Preferenza tema
- Stato sidebar collassata
- Preferenze utente (non da server)

```typescript
import { create } from "zustand";

interface AppState {
  sidebarOpen: boolean;
  toggleSidebar: () => void;
}

export const useAppState = create<AppState>((set) => ({
  sidebarOpen: true,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
}));
```

**Evita prop drilling** - usa context o Zustand invece.

---

## Riepilogo

**Pattern Comuni:**

- ✅ Hook useAuth per utente corrente (id, email, roles, username)
- ✅ React Hook Form + Zod per form
- ✅ Dialog con icona + pulsante chiusura
- ✅ Contratti wrapper DataGrid
- ✅ Mutation con invalidazione cache
- ✅ TanStack Query per stato server
- ✅ useState per stato UI
- ✅ Zustand per stato client globale (minimale)

**Vedi Anche:**

- [data-fetching.md](data-fetching.md) - Pattern TanStack Query
- [component-patterns.md](component-patterns.md) - Struttura componenti
- [loading-and-error-states.md](loading-and-error-states.md) - Gestione errori
