---
name: verification-before-completion
description: Usa prima di dichiarare un lavoro finito. Richiede esecuzione di comandi di verifica e conferma output.
---

# Verifica Prima del Completamento

## Panoramica

Reclamare lavoro completo senza verifica è disonestà, non efficienza.

**Principio core:** Prove prima dei claim, sempre.

**Violare la lettera di questa regola è violare lo spirito di questa regola.**

## La Legge Ferrea

```
NESSUN CLAIM DI COMPLETAMENTO SENZA PROVE DI VERIFICA FRESCHE
```

Se non hai eseguito il comando di verifica in questo messaggio, non puoi reclamare che passi.

## La Funzione Gate

```
PRIMA di reclamare qualsiasi stato o esprimere soddisfazione:

1. IDENTIFICA: Quale comando prova questo claim?
2. ESEGUI: Esegui il comando COMPLETO (fresco, completo)
3. LEGGI: Output completo, controlla exit code, conta fallimenti
4. VERIFICA: L'output conferma il claim?
   - Se NO: Dichiara stato attuale con prova
   - Se SÌ: Dichiara claim CON prova
5. SOLO ALLORA: Fai il claim

Saltare qualsiasi passo = mentire, non verificare
```

## Fallimenti Comuni

| Claim                   | Richiede                          | Non Sufficiente                           |
| ----------------------- | --------------------------------- | ----------------------------------------- |
| Test passano            | Output comando test: 0 fallimenti | Esecuzione precedente, "dovrebbe passare" |
| Linter pulito           | Output linter: 0 errori           | Controllo parziale, estrapolazione        |
| Build ha successo       | Comando build: exit 0             | Linter passante, log sembrano buoni       |
| Bug fixato              | Test sintomo originale: passa     | Codice cambiato, assunto fixato           |
| Test regressione lavora | Ciclo red-green verificato        | Test passa una volta                      |
| Agente completato       | Diff VCS mostra cambiamenti       | Agente riporta "successo"                 |
| Requisiti soddisfatti   | Checklist riga-per-riga           | Test passanti                             |

## Red Flag - STOP

- Usare "dovrebbe", "probabilmente", "sembra"
- Esprimere soddisfazione prima della verifica ("Grande!", "Perfetto!", "Fatto!", ecc.)
- Stare per committare/pushare/PR senza verifica
- Fidarsi report successo agente
- Affidarsi a verifica parziale
- Pensare "solo questa volta"
- Stanco e volere lavoro finito
- **QUALSIASI dicitura implicante successo senza aver eseguito verifica**

## Prevenzione Razionalizzazione

| Scusa                                      | Realtà                     |
| ------------------------------------------ | -------------------------- |
| "Dovrebbe funzionare ora"                  | ESEGUI la verifica         |
| "Sono confidente"                          | Confidenza ≠ prova         |
| "Solo questa volta"                        | Nessuna eccezione          |
| "Linter passato"                           | Linter ≠ compilatore       |
| "Agente detto successo"                    | Verifica indipendentemente |
| "Sono stanco"                              | Esaurimento ≠ scusa        |
| "Controllo parziale è abbastanza"          | Parziale prova nulla       |
| "Parole diverse quindi regola non applica" | Spirito sopra lettera      |

## Pattern Chiave

**Test:**

```
✅ [Esegui comando test] [Vedi: 34/34 pass] "Tutti i test passano"
❌ "Dovrebbe passare ora" / "Sembra corretto"
```

**Test regressione (TDD Red-Green):**

```
✅ Scrivi → Esegui (pass) → Revert fix → Esegui (DEVE FALLIRE) → Ripristina → Esegui (pass)
❌ "Ho scritto un test regressione" (senza verifica red-green)
```

**Build:**

```
✅ [Esegui build] [Vedi: exit 0] "Build passa"
❌ "Linter passato" (linter non controlla compilazione)
```

**Requisiti:**

```
✅ Rileggi piano → Crea checklist → Verifica ogni → Riporta gap o completamento
❌ "Test passano, fase completa"
```

**Delega Agente:**

```
✅ Agente riporta successo → Controlla diff VCS → Verifica cambiamenti → Riporta stato attuale
❌ Credi report agente
```

## Perché Questo Importa

Da 24 memorie di fallimento:

- il tuo partner umano ha detto "Non ti credo" - fiducia rotta
- Funzioni non definite shippate - crasherebbe
- Requisiti mancanti shippati - feature incomplete
- Tempo sprecato su falso completamento → ridirezione → rilavorazione
- Viola: "Onestà è un valore core. Se menti, sarai rimpiazzato."

## Quando Applicare

**SEMPRE prima:**

- QUALSIASI variazione di claim successo/completamento
- QUALSIASI espressione di soddisfazione
- QUALSIASI dichiarazione positiva su stato lavoro
- Committare, creazione PR, completamento task
- Muovere al prossimo task
- Delegare ad agenti

**Regola si applica a:**

- Frasi esatte
- Parafrasi e sinonimi
- Implicazioni di successo
- QUALSIASI comunicazione suggerente completamento/correttezza

## La Linea di Fondo

**Nessuna scorciatoia per verifica.**

Esegui il comando. Leggi l'output. POI reclama il risultato.

Questo è non-negoziabile.
