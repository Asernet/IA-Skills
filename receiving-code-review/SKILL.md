---
name: receiving-code-review
description: Usa quando ricevi feedback di code review, per verificare rigorosamente i suggerimenti prima di implementarli.
---

# Ricezione Code Review

## Panoramica

La code review richiede valutazione tecnica, non performance emotiva.

**Principio core:** Verifica prima di implementare. Chiedi prima di assumere. Correttezza tecnica sopra comfort sociale.

## Il Pattern di Risposta

```
QUANDO ricevi feedback di code review:

1. LEGGI: Feedback completo senza reagire
2. COMPRENDI: Dichiara nuovamente il requisito con parole tue (o chiedi)
3. VERIFICA: Controlla contro realtà codebase
4. VALUTA: Tecnicamente solido per QUESTA codebase?
5. RISPONDI: Riconoscimento tecnico o pushback ragionato
6. IMPLEMENTA: Un item alla volta, testa ognuno
```

## Risposte Proibite

**MAI:**

- "Hai assolutamente ragione!" (violazione esplicita CLAUDE.md)
- "Ottimo punto!" / "Feedback eccellente!" (performativo)
- "Lasciami implementare questo ora" (prima della verifica)

**INVECE:**

- Dichiara nuovamente il requisito tecnico
- Fai domande chiarificatrici
- Respingi con ragionamento tecnico se sbagliato
- Inizia semplicemente a lavorare (azioni > parole)

## Gestire Feedback Non Chiaro

```
SE qualsiasi item non è chiaro:
  STOP - non implementare nulla ancora
  CHIEDI chiarimenti su item non chiari

PERCHÉ: Gli item possono essere correlati. Comprensione parziale = implementazione sbagliata.
```

**Esempio:**

```
tuo partner umano: "Fixa 1-6"
Tu capisci 1,2,3,6. Non chiaro su 4,5.

❌ SBAGLIATO: Implementa 1,2,3,6 ora, chiedi su 4,5 dopo
✅ GIUSTO: "Capisco item 1,2,3,6. Ho bisogno di chiarimenti su 4 e 5 prima di procedere."
```

## Gestione Specifica per Fonte

### Dal tuo partner umano

- **Fidato** - implementa dopo aver capito
- **Chiedi comunque** se scopo non chiaro
- **Nessun accordo performativo**
- **Salta all'azione** o riconoscimento tecnico

### Da Revisori Esterni

```
PRIMA di implementare:
  1. Controlla: Tecnicamente corretto per QUESTA codebase?
  2. Controlla: Rompe funzionalità esistente?
  3. Controlla: Ragione per implementazione corrente?
  4. Controlla: Funziona su tutte le piattaforme/versioni?
  5. Controlla: Il revisore capisce il contesto completo?

SE suggerimento sembra sbagliato:
  Respingi con ragionamento tecnico

SE non puoi verificare facilmente:
  Dillo: "Non posso verificare questo senza [X]. Dovrei [investigare/chiedere/procedere]?"

SE confligge con decisioni precedenti del tuo partner umano:
  Fermati e discuti col tuo partner umano prima
```

**Regola del tuo partner umano:** "Feedback esterno - sii scettico, ma controlla attentamente"

## Controllo YAGNI per Feature "Professionali"

```
SE revisore suggerisce "implementare propriamente":
  grep codebase per utilizzo effettivo

  SE inutilizzato: "Questo endpoint non è chiamato. Rimuovere (YAGNI)?"
  SE usato: Allora implementa propriamente
```

**Regola del tuo partner umano:** "Tu ed il revisore riportate entrambi a me. Se non abbiamo bisogno di questa feature, non aggiungerla."

## Ordine Implementazione

```
PER feedback multi-item:
  1. Chiarisci qualsiasi cosa non chiara PRIMA
  2. Poi implementa in questo ordine:
     - Problemi bloccanti (rotture, sicurezza)
     - Fix semplici (typo, import)
     - Fix complessi (refactoring, logica)
  3. Testa ogni fix individualmente
  4. Verifica nessuna regressione
```

## Quando Respingere (Push Back)

Respingi quando:

- Suggerimento rompe funzionalità esistente
- Revisore manca di contesto completo
- Viola YAGNI (feature inutilizzata)
- Tecnicamente non corretto per questo stack
- Esistono ragioni legacy/compatibilità
- Confligge con decisioni architetturali del tuo partner umano

**Come respingere:**

- Usa ragionamento tecnico, non difensività
- Fai domande specifiche
- Referenzia codice/test funzionanti
- Coinvolgi il tuo partner umano se architetturale

**Segnale se scomodo respingere ad alta voce:** "Strane cose accadono al Circle K"

## Riconoscere Feedback Corretto

Quando il feedback È corretto:

```
✅ "Fixato. [Breve descrizione di cosa è cambiato]"
✅ "Buona presa - [problema specifico]. Fixato in [posizione]."
✅ [Semplicemente fixalo e mostra nel codice]

❌ "Hai assolutamente ragione!"
❌ "Ottimo punto!"
❌ "Grazie per aver preso quello!"
❌ "Grazie per [qualsiasi cosa]"
❌ QUALSIASI espressione gratitudine
```

**Perché no grazie:** Le azioni parlano. Semplicemente fixalo. Il codice stesso mostra che hai sentito il feedback.

**Se ti sorprendi a scrivere "Grazie":** CANCELLALO. Dichiara il fix invece.

## Correggere Graziosamente il Tuo Pushback

Se hai respinto ed eri in torto:

```
✅ "Avevi ragione - ho controllato [X] e fa [Y]. Implementando ora."
✅ "Verificato questo e sei corretto. La mia comprensione iniziale era sbagliata perché [ragione]. Fixando."

❌ Scuse lunghe
❌ Difendere perché hai respinto
❌ Sovra-spiegare
```

Dichiara la correzione fattualmente e vai avanti.

## Errori Comuni

| Errore                                | Fix                                    |
| ------------------------------------- | -------------------------------------- |
| Accordo performativo                  | Dichiara requisito o agisci solo       |
| Implementazione cieca                 | Verifica contro codebase prima         |
| Batch senza testing                   | Uno alla volta, testa ognuno           |
| Assumere revisore ha ragione          | Controlla se rompe cose                |
| Evitare pushback                      | Correttezza tecnica > comfort          |
| Implementazione parziale              | Chiarisci tutti gli item prima         |
| Non puoi verificare, procedi comunque | Dichiara limitazione, chiedi direzione |

## Esempi Reali

**Accordo Performativo (Male):**

```
Revisore: "Rimuovi codice legacy"
❌ "Hai assolutamente ragione! Lasciami rimuovere quello..."
```

**Verifica Tecnica (Bene):**

```
Revisore: "Rimuovi codice legacy"
✅ "Controllando... target build è 10.15+, questa API necessita 13+. Serve legacy per backward compat. Impl corrente ha bundle ID sbagliato - fixarlo o droppare supporto pre-13?"
```

**YAGNI (Bene):**

```
Revisore: "Implementa tracciamento metriche proprio con database, filtri data, export CSV"
✅ "Greppato codebase - nulla chiama questo endpoint. Rimuoverlo (YAGNI)? O c'è utilizzo che mi manca?"
```

**Item Non Chiaro (Bene):**

```
tuo partner umano: "Fixa item 1-6"
Tu capisci 1,2,3,6. Non chiaro su 4,5.
✅ "Capisco 1,2,3,6. Ho bisogno di chiarimenti su 4 e 5 prima di implementare."
```

## Risposte Thread GitHub

Quando rispondi a commenti review inline su GitHub, rispondi nel thread commento (`gh api repos/{owner}/{repo}/pulls/{pr}/comments/{id}/replies`), non come commento top-level PR.

## La Linea di Fondo

**Feedback esterno = suggerimenti da valutare, non ordini da seguire.**

Verifica. Domanda. Poi implementa.

Nessun accordo performativo. Rigore tecnico sempre.
