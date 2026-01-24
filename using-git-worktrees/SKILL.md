---
name: using-git-worktrees
description: Usa per iniziare lavori su feature che richiedono isolamento, creando worktree git separati.
---

# Usare Git Worktree

## Panoramica

I worktree Git creano spazi di lavoro isolati che condividono lo stesso repository, permettendo lavoro su branch multipli simultaneamente senza switchare.

**Principio core:** Selezione directory sistematica + verifica sicurezza = isolamento affidabile.

**Annuncia all'avvio:** "Sto usando la skill using-git-worktrees per impostare uno spazio di lavoro isolato."

## Processo Selezione Directory

Segui questo ordine di priorità:

### 1. Controlla Directory Esistenti

```bash
# Check in priority order
ls -d .worktrees 2>/dev/null     # Preferred (hidden)
ls -d worktrees 2>/dev/null      # Alternative
```

**Se trovata:** Usa quella directory. Se entrambe esistono, `.worktrees` vince.

### 2. Controlla CLAUDE.md

```bash
grep -i "worktree.*director" CLAUDE.md 2>/dev/null
```

**Se preferenza specificata:** Usala senza chiedere.

### 3. Chiedi Utente

Se nessuna directory esiste e nessuna preferenza CLAUDE.md:

```
Nessuna directory worktree trovata. Dove dovrei creare i worktree?

1. .worktrees/ (locale progetto, nascosta)
2. ~/.config/superpowers/worktrees/<project-name>/ (locazione globale)

Quale preferisci?
```

## Verifica Sicurezza

### Per Directory Locali Progetto (.worktrees o worktrees)

**DEVI verificare che la directory sia ignorata prima di creare worktree:**

```bash
# Check if directory is ignored (respects local, global, and system gitignore)
git check-ignore -q .worktrees 2>/dev/null || git check-ignore -q worktrees 2>/dev/null
```

**Se NON ignorata:**

Per la regola di Jesse "Fixa cose rotte immediatamente":

1. Aggiungi riga appropriata a .gitignore
2. Committa il cambiamento
3. Procedi con creazione worktree

**Perché critico:** Previene commit accidentale contenuti worktree nel repository.

### Per Directory Globale (~/.config/superpowers/worktrees)

Nessuna verifica .gitignore necessaria - fuori dal progetto interamente.

## Passi Creazione

### 1. Rileva Nome Progetto

```bash
project=$(basename "$(git rev-parse --show-toplevel)")
```

### 2. Crea Worktree

```bash
# Determine full path
case $LOCATION in
  .worktrees|worktrees)
    path="$LOCATION/$BRANCH_NAME"
    ;;
  ~/.config/superpowers/worktrees/*)
    path="~/.config/superpowers/worktrees/$project/$BRANCH_NAME"
    ;;
esac

# Create worktree with new branch
git worktree add "$path" -b "$BRANCH_NAME"
cd "$path"
```

### 3. Esegui Setup Progetto

Auto-rileva ed esegui setup appropriato:

```bash
# Node.js
if [ -f package.json ]; then npm install; fi

# Rust
if [ -f Cargo.toml ]; then cargo build; fi

# Python
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then poetry install; fi

# Go
if [ -f go.mod ]; then go mod download; fi
```

### 4. Verifica Baseline Pulita

Esegui test per assicurare che il worktree inizi pulito:

```bash
# Examples - use project-appropriate command
npm test
cargo test
pytest
go test ./...
```

**Se i test falliscono:** Riporta fallimenti, chiedi se procedere o investigare.

**Se i test passano:** Riporta pronto.

### 5. Riporta Locazione

```
Worktree pronto a <full-path>
Test passanti (<N> test, 0 fallimenti)
Pronto per implementare <feature-name>
```

## Riferimento Rapido

| Situazione                       | Azione                              |
| -------------------------------- | ----------------------------------- |
| `.worktrees/` esiste             | Usala (verifica ignorata)           |
| `worktrees/` esiste              | Usala (verifica ignorata)           |
| Entrambe esistono                | Usa `.worktrees/`                   |
| Nessuna esiste                   | Controlla CLAUDE.md → Chiedi utente |
| Directory non ignorata           | Aggiungi a .gitignore + commit      |
| Test falliscono durante baseline | Riporta fallimenti + chiedi         |
| No package.json/Cargo.toml       | Salta installazione dipendenze      |

## Errori Comuni

### Saltare verifica ignore

- **Problema:** Contenuti worktree vengono tracciati, inquinano git status
- **Fix:** Usa sempre `git check-ignore` prima di creare worktree locale progetto

### Assumere locazione directory

- **Problema:** Crea inconsistenza, viola convenzioni progetto
- **Fix:** Segui priorità: esistente > CLAUDE.md > chiedi

### Procedere con test fallimentari

- **Problema:** Non puoi distinguere nuovi bug da problemi pre-esistenti
- **Fix:** Riporta fallimenti, ottieni permesso esplicito per procedere

### Hardcodare comandi setup

- **Problema:** Si rompe su progetti che usano tool diversi
- **Fix:** Auto-rileva file progetto (package.json, ecc.)

## Red Flag

**Mai:**

- Creare worktree senza verificare che sia ignorato (locale progetto)
- Saltare verifica baseline test
- Procedere con test fallimentari senza chiedere
- Assumere locazione directory quando ambigua
- Saltare controllo CLAUDE.md

**Sempre:**

- Segui priorità directory: esistente > CLAUDE.md > chiedi
- Verifica directory ignorata per locale progetto
- Auto-rileva ed esegui setup progetto
- Verifica baseline test pulita

## Integrazione

**Chiamato da:**

- **brainstorming** (Fase 4) - RICHIESTO quando design approvato e implementazione segue
- Qualsiasi skill che necessita spazio di lavoro isolato

**Accoppia con:**

- **finishing-a-development-branch** - RICHIESTO per pulizia dopo lavoro completo
- **executing-plans** o **subagent-driven-development** - Il lavoro accade in questo worktree
