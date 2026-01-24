---
name: subagent-driven-development
description: Usa per eseguire piani di implementazione con task indipendenti nella sessione corrente tramite sub-agenti.
---

# Sviluppo Guidato da Subagenti

Esegui piano dispatciando subagente fresco per task, con review a due stadi dopo ognuno: review compliance spec prima, poi review qualità codice.

**Principio core:** Subagente fresco per task + review a due stadi (spec poi qualità) = alta qualità, iterazione veloce

## Quando Usare

**vs. Executing Plans (sessione parallela):**

- Stessa sessione (nessuno switch contesto)
- Subagente fresco per task (nessun inquinamento contesto)
- Review a due stadi dopo ogni task: compliance spec prima, poi qualità codice
- Iterazione più veloce (nessun human-in-loop tra task)

## Il Processo

1. Leggi piano, estrai tutti i task con testo completo, nota contesto, crea TodoWrite
2. Per ogni task:
   a. Dispatcia subagente implementatore (`./implementer-prompt.md`)
   b. Se subagente chiede domande -> Rispondi, fornisci contesto
   c. Subagente implementa, testa, committa, auto-revisiona
   d. Dispatcia subagente revisore spec (`./spec-reviewer-prompt.md`)
   e. Se revisore spec trova problemi -> Subagente implementatore fixa -> Ripeti review
   f. Dispatcia subagente revisore qualità codice (`./code-quality-reviewer-prompt.md`)
   g. Se revisore qualità trova problemi -> Subagente implementatore fixa -> Ripeti review
   h. Segna task completo in TodoWrite
3. Dispatcia subagente revisore codice finale per intera implementazione
4. Usa superpowers:finishing-a-development-branch

## Template Prompt

- `./implementer-prompt.md` - Dispatcia subagente implementatore
- `./spec-reviewer-prompt.md` - Dispatcia subagente revisore compliance spec
- `./code-quality-reviewer-prompt.md` - Dispatcia subagente revisore qualità codice

## Esempio Workflow

```
Tu: Sto usando Sviluppo Guidato da Subagenti per eseguire questo piano.

[Leggi file piano una volta: docs/plans/feature-plan.md]
[Estrai tutti i 5 task con testo completo e contesto]
[Crea TodoWrite con tutti i task]

Task 1: Script installazione hook

[Ottieni testo Task 1 e contesto (già stratto)]
[Dispatcia subagente implementazione con testo task completo + contesto]

Implementatore: "Prima che inizi - l'hook dovrebbe essere installato a livello utente o sistema?"

Tu: "Livello utente (~/.config/superpowers/hooks/)"

Implementatore: "Capito. Implementando ora..."
[Dopo] Implementatore:
  - Implementato comando install-hook
  - Aggiunti test, 5/5 passanti
  - Auto-review: Trovato che ho mancato flag --force, aggiunto
  - Committato

[Dispatcia revisore compliance spec]
Revisore Spec: ✅ Spec compliant - tutti i requisiti soddisfatti, nulla extra

[Ottieni git SHA, dispatcia revisore qualità codice]
Revisore Codice: Punti di forza: Buona copertura test, pulito. Problemi: Nessuno. Approvato.

[Segna Task 1 completo]

Task 2: Modi recovery

[Ottieni testo Task 2 e contesto]
[Dispatcia subagente implementazione]

Implementatore: [Nessuna domanda, procede]
Implementatore:
  - Aggiunti modi verify/repair
  - 8/8 test passanti
  - Auto-review: Tutto bene
  - Committato

[Dispatcia revisore compliance spec]
Revisore Spec: ❌ Problemi:
  - Mancante: Reporting progresso (spec dice "riporta ogni 100 item")
  - Extra: Aggiunto flag --json (non richiesto)

[Implementatore fixa problemi]
Implementatore: Rimosso flag --json, aggiunto reporting progresso

[Revisore Spec revisiona ancora]
Revisore Spec: ✅ Spec compliant ora

[Dispatcia revisore qualità codice]
Revisore Codice: Punti di forza: Solido. Problemi (Importante): Numero magico (100)

[Implementatore fixa]
Implementatore: Estratta costante PROGRESS_INTERVAL

[Revisore Codice revisiona ancora]
Revisore Codice: ✅ Approvato

[Segna Task 2 completo]

...

[Dopo tutti i task]
[Dispatcia code-reviewer finale]
Revisore Finale: Tutti i requisiti soddisfatti, pronto per merge

Fatto!
```

## Vantaggi

**vs. Esecuzione Manuale:**

- Subagenti seguono TDD naturalmente
- Contesto fresco per task (nessuna confusione)
- Parallel-safe (subagenti non interferiscono)
- Subagente può fare domande (prima E durante lavoro)

**vs. Esecuzione Piani:**

- Stessa sessione (nessun handoff)
- Progresso continuo (nessuna attesa)
- Checkpoint review automatici

**Guadagni Efficienza:**

- Nessun overhead lettura file (controller fornisce testo completo)
- Controller cura esattamente quale contesto è necessario
- Subagente ottiene informazioni complete upfront
- Domande emerse prima che il lavoro inizi (non dopo)

**Quality Gates:**

- Auto-review cattura problemi prima dell'handoff
- Review a due-stadi: compliance spec, poi qualità codice
- Loop review assicurano che i fix funzionino davvero
- Compliance spec previene over/under-building
- Qualità codice assicura che implementazione sia ben-costruita

**Costo:**

- Più invocazioni subagente (implementatore + 2 revisori per task)
- Controller fa più lavoro prep (estraendo tutti i task upfront)
- Loop review aggiungono iterazioni
- Ma cattura problemi presto (più economico che debuggare dopo)

## Red Flag

**Mai:**

- Saltare review (compliance spec O qualità codice)
- Procedere con problemi non fixati
- Dispatciare subagenti implementazione multipli in parallelo (conflitti)
- Far leggere file piano al subagente (fornisci testo completo invece)
- Saltare contesto scene-setting (subagente deve capire dove si adatta il task)
- Ignorare domande subagente (rispondi prima di lasciarli procedere)
- Accettare "abbastanza vicino" su compliance spec (revisore spec trovato problemi = non fatto)
- Saltare loop review (revisore trovato problemi = implementatore fixa = review ancora)
- Lasciare che auto-review implementatore rimpiazzi review effettiva (entrambi sono necessari)
- **Iniziare review qualità codice prima che compliance spec sia ✅** (ordine sbagliato)
- Muovere al prossimo task mentre qualsiasi review ha problemi aperti

**Se subagente fa domande:**

- Rispondi chiaramente e completamente
- Fornisci contesto addizionale se necessario
- Non affrettarli nell'implementazione

**Se revisore trova problemi:**

- Implementatore (stesso subagente) li fixa
- Revisore revisiona ancora
- Ripeti finché approvato
- Non saltare la re-review

**Se subagente fallisce task:**

- Dispatcia subagente fix con istruzioni specifiche
- Non provare a fixare manualmente (inquinamento contesto)

## Integrazione

**Skill workflow richieste:**

- **superpowers:writing-plans** - Crea il piano che questa skill esegue
- **superpowers:requesting-code-review** - Template code review per subagenti revisori
- **superpowers:finishing-a-development-branch** - Completa sviluppo dopo tutti i task

**Subagenti dovrebbero usare:**

- **superpowers:test-driven-development** - Subagenti seguono TDD per ogni task

**Workflow alternativo:**

- **superpowers:executing-plans** - Usa per sessione parallela invece di esecuzione stessa-sessione
