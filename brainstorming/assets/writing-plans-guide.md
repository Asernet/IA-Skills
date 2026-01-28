# Scrivere Piani

## Panoramica

Scrivi piani di implementazione completi assumendo che l'ingegnere non abbia alcun contesto del nostro codebase e un gusto discutibile. Documenta tutto ciò che devono sapere: quali file toccare per ogni task, codice, testing, docs che potrebbero dover controllare, come testarlo. Dai loro l'intero piano come task piccoli. DRY. YAGNI. TDD. Commit frequenti.

Assumi che siano sviluppatori abili, ma sappiano quasi nulla del nostro toolset o dominio problema. Assumi che non conoscano molto bene il buon design dei test.

**Annuncia all'avvio:** "Sto usando la guida interna di brainstorming per creare il piano di implementazione."

**Contesto:** Questo dovrebbe essere eseguito in un worktree dedicato (creato dalla skill brainstorming).

**Salva piani in:** `docs/plans/YYYY-MM-DD-<feature-name>.md`

## Granularità Task Piccoli

**Ogni passo è un'azione (2-5 minuti):**

- "Scrivi il test fallimentare" - passo
- "Eseguilo per assicurare che fallisca" - passo
- "Implementa il codice minimo per far passare il test" - passo
- "Esegui i test e assicura che passino" - passo
- "Committa" - passo

## Header Documento Piano

**Ogni piano DEVE iniziare con questo header:**

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [Una frase descrivendo cosa costruisce]

**Architecture:** [2-3 frasi sull'approccio]

**Tech Stack:** [Tecnologie/librerie chiave]

---
```

## Struttura Task

````markdown
### Task N: [Component Name]

**Files:**

- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```
````

**Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

**Step 3: Write minimal implementation**

```python
def function(input):
    return expected
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```

```

## Ricorda
- Percorsi file esatti sempre
- Codice completo nel piano (non "aggiungi validazione")
- Comandi esatti con output atteso
- Referenzia skill rilevanti con sintassi @
- DRY, YAGNI, TDD, commit frequenti

## Handoff Esecuzione

Dopo aver salvato il piano, offri scelta esecuzione:

**"Piano completo e salvato a `docs/plans/<filename>.md`. Due opzioni esecuzione:**

**1. Guidato da Subagente (questa sessione)** - Dispatcio subagente fresco per task, review tra task, iterazione veloce

**2. Sessione Parallela (separata)** - Apri nuova sessione con executing-plans, esecuzione batch con checkpoint

**Quale approccio?"**

**Se scelto Guidato da Subagente:**
- **REQUIRED SUB-SKILL:** Usa superpowers:subagent-driven-development
- Resta in questa sessione
- Subagente fresco per task + code review

**Se scelto Sessione Parallela:**
- Guidali ad aprire nuova sessione nel worktree
- Indica di caricare e seguire la guida in `assets/executing-plans-guide.md`

```
