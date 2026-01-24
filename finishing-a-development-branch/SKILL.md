---
name: finishing-a-development-branch
description: Usa quando l'implementazione è completa e i test passano, per decidere come integrare il lavoro (merge, PR, cleanup).
---

# Completare un Branch di Sviluppo

## Panoramica

Guida il completamento del lavoro di sviluppo presentando opzioni chiare e gestendo il workflow scelto.

**Principio base:** Verifica test → Presenta opzioni → Esegui scelta → Pulisci.

**Annuncia all'inizio:** "Sto usando la skill finishing-a-development-branch per completare questo lavoro."

## Il Processo

### Passo 1: Verifica Test

**Prima di presentare opzioni, verifica che i test passino:**

```bash
# Esegui suite di test del progetto
npm test / cargo test / pytest / go test ./...
```

**Se i test falliscono:**

```
Test falliti (<N> fallimenti). Devi fixare prima di completare:

[Mostra fallimenti]

Impossibile procedere con merge/PR finché i test passano.
```

Stop. Non procedere al Passo 2.

**Se i test passano:** Continua al Passo 2.

### Passo 2: Determina Base Branch

```bash
# Prova base branch comuni
git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null
```

O chiedi: "Questo branch si è staccato da main - è corretto?"

### Passo 3: Presenta Opzioni

Presenta esattamente queste 4 opzioni:

```
Implementazione completa. Cosa vorresti fare?

1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
4. Discard this work

Quale opzione?
```

**Non aggiungere spiegazioni** - mantieni opzioni concise.

### Passo 4: Esegui Scelta

#### Opzione 1: Merge Locale

```bash
# Switch to base branch
git checkout <base-branch>

# Pull latest
git pull

# Merge feature branch
git merge <feature-branch>

# Verify tests on merged result
<test command>

# If tests pass
git branch -d <feature-branch>
```

Poi: Pulisci worktree (Passo 5)

#### Opzione 2: Push e Crea PR

```bash
# Push branch
git push -u origin <feature-branch>

# Create PR
gh pr create --title "<title>" --body "$(cat <<'EOF'
## Summary
<2-3 bullets of what changed>

## Test Plan
- [ ] <verification steps>
EOF
)"
```

Poi: Pulisci worktree (Passo 5)

#### Opzione 3: Mantieni Così Com'è

Riporta: "Mantenendo branch <name>. Worktree preservato a <path>."

**Non pulire worktree.**

#### Opzione 4: Scarta

**Conferma prima:**

```
Questo cancellerà permanentemente:
- Branch <name>
- Tutti i commit: <commit-list>
- Worktree a <path>

Digita 'discard' per confermare.
```

Aspetta conferma esatta.

Se confermato:

```bash
git checkout <base-branch>
git branch -D <feature-branch>
```

Poi: Pulisci worktree (Passo 5)

### Passo 5: Pulisci Worktree

**Per Opzioni 1, 2, 4:**

Controlla se in worktree:

```bash
git worktree list | grep $(git branch --show-current)
```

Se sì:

```bash
git worktree remove <worktree-path>
```

**Per Opzione 3:** Mantieni worktree.

## Riferimento Rapido

| Opzione          | Merge | Push | Keep Worktree | Cleanup Branch |
| ---------------- | ----- | ---- | ------------- | -------------- |
| 1. Merge locally | ✓     | -    | -             | ✓              |
| 2. Create PR     | -     | ✓    | ✓             | -              |
| 3. Keep as-is    | -     | -    | ✓             | -              |
| 4. Discard       | -     | -    | -             | ✓ (force)      |

## Errori Comuni

**Saltare verifica test**

- **Problema:** Merge codice rotto, crea PR fallimentare
- **Fix:** Verifica sempre test prima di offrire opzioni

**Domande a risposta aperta**

- **Problema:** "Cosa dovrei fare dopo?" → ambiguo
- **Fix:** Presenta esattamente 4 opzioni strutturate

**Cleanup automatico worktree**

- **Problema:** Rimuove worktree quando potresti averne bisogno (Opzione 2, 3)
- **Fix:** Pulisci solo per Opzioni 1 e 4

**Nessuna conferma per discard**

- **Problema:** Cancella lavoro accidentalmente
- **Fix:** Richiedi conferma digitata "discard"

## Red Flags

**Mai:**

- Procedere con test falliti
- Merge senza verificare test sul risultato
- Cancellare lavoro senza conferma
- Force-push senza richiesta esplicita

**Sempre:**

- Verificare test prima di offrire opzioni
- Presentare esattamente 4 opzioni
- Ottenere conferma digitata per Opzione 4
- Pulire worktree solo per Opzioni 1 & 4

## Integrazione

**Chiamato da:**

- **subagent-driven-development** (Step 7) - Dopo che tutti i task sono completi
- **executing-plans** (Step 5) - Dopo che tutti i batch sono completi

**Accoppia con:**

- **using-git-worktrees** - Pulisce worktree creato da quella skill
