---
name: planning-with-files
description: Implementa pianificazione basata su file (stile Manus) per task complessi. Crea task_plan.md, findings.md e progress.md.
---

# Pianificazione con File

Lavora come Manus: Usa file markdown persistenti come la tua "memoria di lavoro su disco".

## Importante: Dove Vanno i File

Quando usi questa skill:

- **Template** sono memorizzati nella directory skill a `${CLAUDE_PLUGIN_ROOT}/templates/`
- **I tuoi file di pianificazione** (`task_plan.md`, `findings.md`, `progress.md`) dovrebbero essere creati nella **tua directory progetto** — la cartella dove stai lavorando

| Posizione                                  | Cosa Va Lì                                   |
| ------------------------------------------ | -------------------------------------------- |
| Directory Skill (`${CLAUDE_PLUGIN_ROOT}/`) | Template, script, doc riferimento            |
| Tua directory progetto                     | `task_plan.md`, `findings.md`, `progress.md` |

Questo assicura che i tuoi file di pianificazione vivano accanto al tuo codice, non sepolti nella cartella di installazione della skill.

## Avvio Rapido

Prima di QUALSIASI task complesso:

1. **Crea `task_plan.md`** nel tuo progetto — Usa [templates/task_plan.md](templates/task_plan.md) come riferimento
2. **Crea `findings.md`** nel tuo progetto — Usa [templates/findings.md](templates/findings.md) come riferimento
3. **Crea `progress.md`** nel tuo progetto — Usa [templates/progress.md](templates/progress.md) come riferimento
4. **Rileggi piano prima delle decisioni** — Rinfresca obiettivi nella finestra di attenzione
5. **Aggiorna dopo ogni fase** — Segna completo, logga errori

> **Nota:** Tutti e tre i file di pianificazione dovrebbero essere creati nella tua directory di lavoro corrente (la root del tuo progetto), non nella cartella di installazione della skill.

## Il Pattern Core

```
Finestra Contesto = RAM (volatile, limitata)
Filesystem = Disco (persistente, illimitato)

→ Qualsiasi cosa importante viene scritta su disco.
```

## Scopo dei File

| File           | Scopo                        | Quando Aggiornare       |
| -------------- | ---------------------------- | ----------------------- |
| `task_plan.md` | Fasi, progresso, decisioni   | Dopo ogni fase          |
| `findings.md`  | Ricerca, scoperte            | Dopo QUALSIASI scoperta |
| `progress.md`  | Log sessione, risultati test | Attraverso la sessione  |

## Regole Critiche

### 1. Crea Piano Prima

Non iniziare mai un task complesso senza `task_plan.md`. Non negoziabile.

### 2. La Regola 2-Azioni

> "Dopo ogni 2 operazioni di visualizzazione/browser/ricerca, salva IMMEDIATAMENTE le scoperte chiave su file di testo."

Questo previene che informazioni visuali/multimodali vengano perse.

### 3. Leggi Prima di Decidere

Prima di decisioni maggiori, leggi il file piano. Questo mantiene gli obiettivi nella tua finestra di attenzione.

### 4. Aggiorna Dopo Agire

Dopo aver completato qualsiasi fase:

- Segna stato fase: `in_progress` → `complete`
- Logga qualsiasi errore incontrato
- Nota file creati/modificati

### 5. Logga TUTTI gli Errori

Ogni errore va nel file piano. Questo costruisce conoscenza e previene ripetizione.

```markdown
## Errori Incontrati

| Errore            | Tentativo | Risoluzione           |
| ----------------- | --------- | --------------------- |
| FileNotFoundError | 1         | Creato config default |
| API timeout       | 2         | Aggiunto logica retry |
```

### 6. Mai Ripetere Fallimenti

```
if azione_fallita:
    prossima_azione != stessa_azione
```

Traccia cosa hai provato. Muta l'approccio.

## Il Protocollo Errore 3-Strike

```
TENTATIVO 1: Diagnostica & Fix
  → Leggi errore attentamente
  → Identifica causa radice
  → Applica fix mirato

TENTATIVO 2: Approccio Alternativo
  → Stesso errore? Prova metodo diverso
  → Tool diverso? Libreria diversa?
  → MAI ripetere esattamente la stessa azione fallimentare

TENTATIVO 3: Ripensamento Più Ampio
  → Metti in discussione assunzioni
  → Cerca soluzioni
  → Considera aggiornamento piano

DOPO 3 FALLIMENTI: Scala a Utente
  → Spiega cosa hai provato
  → Condividi l'errore specifico
  → Chiedi guida
```

## Matrice Decisionale Leggi vs Scrivi

| Situazione             | Azione                            | Ragione                              |
| ---------------------- | --------------------------------- | ------------------------------------ |
| Appena scritto un file | NON leggere                       | Contenuto ancora nel contesto        |
| Visto immagine/PDF     | Scrivi findings ORA               | Multimodale → testo prima di perdere |
| Browser ritornato dati | Scrivi su file                    | Screenshot non persistono            |
| Iniziando nuova fase   | Leggi piano/findings              | Ri-orienta se contesto stantio       |
| Errore accaduto        | Leggi file rilevante              | Serve stato corrente per fixare      |
| Riprendendo dopo gap   | Leggi tutti i file pianificazione | Recupera stato                       |

## Il Test Riavvio 5-Domande

Se riesci a rispondere a queste, la tua gestione contesto è solida:

| Domanda             | Fonte Risposta                |
| ------------------- | ----------------------------- |
| Dove sono?          | Fase corrente in task_plan.md |
| Dove sto andando?   | Fasi rimanenti                |
| Qual è l'obiettivo? | Statement obiettivo nel piano |
| Cosa ho imparato?   | findings.md                   |
| Cosa ho fatto?      | progress.md                   |

## Quando Usare Questo Pattern

**Usa per:**

- Task multi-step (3+ step)
- Task di ricerca
- Costruire/creare progetti
- Task che spaziano molte chiamate tool
- Qualsiasi cosa che richieda organizzazione

**Salta per:**

- Domande semplici
- Edit su file singolo
- Lookup veloci

## Template

Copia questi template per iniziare:

- [templates/task_plan.md](templates/task_plan.md) — Tracciamento fasi
- [templates/findings.md](templates/findings.md) — Storage ricerca
- [templates/progress.md](templates/progress.md) — Logging sessione

## Script

Script helper per automazione:

- `scripts/init-session.sh` — Inizializza tutti i file pianificazione
- `scripts/check-complete.sh` — Verifica tutte le fasi complete

## Argomenti Avanzati

- **Principi Manus:** Vedi [reference.md](reference.md)
- **Esempi Reali:** Vedi [examples.md](examples.md)

## Anti-Pattern

| Non Fare                                  | Fai Invece                         |
| ----------------------------------------- | ---------------------------------- |
| Usa TodoWrite per persistenza             | Crea file task_plan.md             |
| Dichiara obiettivi una volta e dimentica  | Rileggi piano prima di decisioni   |
| Nascondi errori e riprova silenziosamente | Logga errori su file piano         |
| Riempi tutto nel contesto                 | Memorizza contenuto grande su file |
| Inizia ad eseguire immediatamente         | Crea file piano PRIMA              |
| Ripeti azioni fallite                     | Traccia tentativi, muta approccio  |
| Crea file in directory skill              | Crea file nel tuo progetto         |
