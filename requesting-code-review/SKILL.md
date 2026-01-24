---
name: requesting-code-review
description: Usa prima di completare task o merge, per verificare che il lavoro soddisfi i requisiti.
---

# Richiedere Code Review

Dispatcia subagente superpowers:code-reviewer per catturare problemi prima che si compongano a cascata.

**Principio core:** Revisiona presto, revisiona spesso.

## Quando Richiedere Review

**Obbligatorio:**

- Dopo ogni task nello sviluppo guidato da subagenti
- Dopo aver completato feature maggiore
- Prima del merge su main

**Opzionale ma prezioso:**

- Quando bloccato (prospettiva fresca)
- Prima refactoring (controllo baseline)
- Dopo fix bug complesso

## Come Richiedere

**1. Ottieni git SHA:**

```bash
BASE_SHA=$(git rev-parse HEAD~1)  # o origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatcia subagente code-reviewer:**

Usa tool Task con tipo superpowers:code-reviewer, riempi template a `code-reviewer.md`

**Placeholder:**

- `{WHAT_WAS_IMPLEMENTED}` - Cosa hai appena costruito
- `{PLAN_OR_REQUIREMENTS}` - Cosa dovrebbe fare
- `{BASE_SHA}` - Commit inizio
- `{HEAD_SHA}` - Commit fine
- `{DESCRIPTION}` - Breve riassunto

**3. Agisci su feedback:**

- Fixa problemi Critici immediatamente
- Fixa problemi Importanti prima di procedere
- Nota problemi Minori per dopo
- Respingi se revisore è in torto (con ragionamento)

## Esempio

```
[Appena completato Task 2: Aggiungi funzione verifica]

Tu: Lasciami richiedere code review prima di procedere.

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[Dispatcia subagente superpowers:code-reviewer]
  WHAT_WAS_IMPLEMENTED: Funzioni verifica e riparazione per indice conversazione
  PLAN_OR_REQUIREMENTS: Task 2 da docs/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: Aggiunto verifyIndex() e repairIndex() con 4 tipi problema

[Subagente ritorna]:
  Punti di forza: Architettura pulita, test reali
  Problemi:
    Importante: Indicatori progresso mancanti
    Minore: Numero magico (100) per intervallo reporting
  Valutazione: Pronto a procedere

Tu: [Fixa indicatori progresso]
[Continua a Task 3]
```

## Integrazione con Workflow

**Sviluppo Guidato da Subagenti:**

- Review dopo OGNI task
- Cattura problemi prima che compongano
- Fixa prima di muovere al prossimo task

**Esecuzione Piani:**

- Review dopo ogni batch (3 task)
- Ottieni feedback, applica, continua

**Sviluppo Ad-Hoc:**

- Review prima merge
- Review quando bloccato

## Red Flag

**Mai:**

- Saltare review perché "è semplice"
- Ignorare problemi Critici
- Procedere con problemi Importanti non fixati
- Discutere con feedback tecnico valido

**Se revisore in torto:**

- Respingi con ragionamento tecnico
- Mostra codice/test che provano che funziona
- Richiedi chiarimento

Vedi template a: requesting-code-review/code-reviewer.md
