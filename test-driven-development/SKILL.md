---
name: test-driven-development
description: Usa durante l'implementazione di feature o fix, scrivendo i test prima del codice.
---

# Test-Driven Development (TDD)

## Panoramica

Scrivi il test prima. Guardalo fallire. Scrivi codice minimo per passare.

**Principio core:** Se non hai guardato il test fallire, non sai se testa la cosa giusta.

**Violare la lettera delle regole è violare lo spirito delle regole.**

## Quando Usare

**Sempre:**

- Nuove feature
- Fix bug
- Refactoring
- Cambiamenti comportamento

**Eccezioni (chiedi al tuo partner umano):**

- Prototipi usa e getta
- Codice generato
- File configurazione

Pensi "salto TDD solo questa volta"? Stop. Questa è razionalizzazione.

## La Legge Ferrea

```
NESSUN CODICE PRODUZIONE SENZA UN TEST FALLIMENTARE PRIMA
```

Scrivi codice prima del test? Cancellalo. Ricomincia.

**Nessuna eccezione:**

- Non tenerlo come "riferimento"
- Non "adattarlo" mentre scrivi test
- Non guardarlo
- Cancellare significa cancellare

Implementa fresco dai test. Punto.

## Red-Green-Refactor

### RED - Scrivi Test Fallimentare

Scrivi un test minimo che mostra cosa dovrebbe accadere.

**Requisiti:**

- Un comportamento
- Nome chiaro
- Codice reale (niente mock a meno che inevitabile)

### Verifica RED - Guardalo Fallire

**OBBLIGATORIO. Non saltare mai.**

```bash
npm test path/to/test.test.ts
```

Conferma:

- Test fallisce (non errori)
- Messaggio fallimento è atteso
- Fallisce perché feature mancante (non typo)

**Test passa?** Stai testando comportamento esistente. Fixa test.

**Test errori?** Fixa errore, riesegui finché fallisce correttamente.

### GREEN - Codice Minimo

Scrivi il codice più semplice per passare il test.

Non aggiungere feature, rifattorizzare altro codice o "migliorare" oltre il test.

### Verifica GREEN - Guardalo Passare

**OBBLIGATORIO.**

```bash
npm test path/to/test.test.ts
```

Conferma:

- Test passa
- Altri test passano ancora
- Output intatto (nessun errore, warning)

**Test fallisce?** Fixa codice, non test.

**Altri test falliscono?** Fixa ora.

### REFACTOR - Pulisci

Dopo verde solo:

- Rimuovi duplicazione
- Migliora nomi
- Estrai helper

Mantieni test verdi. Non aggiungere comportamento.

### Ripeti

Prossimo test fallimentare per prossima feature.

## Test Buoni

| Qualità            | Buono                             | Cattivo                                             |
| ------------------ | --------------------------------- | --------------------------------------------------- |
| **Minimale**       | Una cosa. "e" nel nome? Dividilo. | `test('validates email and domain and whitespace')` |
| **Chiaro**         | Nome descrive comportamento       | `test('test1')`                                     |
| **Mostra intento** | Dimostra API desiderata           | Oscura cosa il codice dovrebbe fare                 |

## Razionalizzazioni Comuni

| Scusa                                       | Realtà                                                                   |
| ------------------------------------------- | ------------------------------------------------------------------------ |
| "Troppo semplice da testare"                | Codice semplice si rompe. Test richiede 30 secondi.                      |
| "Testerò dopo"                              | Test passano immediatamente non provano nulla.                           |
| "Test dopo ottengono stessi obiettivi"      | Test-dopo = "cosa fa questo?" Test-prima = "cosa dovrebbe fare questo?"  |
| "Già testato manualmente"                   | Ad-hoc ≠ sistematico. Nessun record, non puoi rieseguire.                |
| "Cancellare X ore è spreco"                 | Fallacia costi affondati. Tenere codice non verificato è debito tecnico. |
| "Tengo come riferimento, scrivo test prima" | Lo adatterai. Quello è testare dopo. Cancellare significa cancellare.    |
| "Bisogno di esplorare prima"                | Bene. Butta via esplorazione, inizia con TDD.                            |
| "Test difficile = design non chiaro"        | Ascolta il test. Difficile da testare = difficile da usare.              |
| "TDD mi rallenterà"                         | TDD più veloce del debugging. Pragmatico = test-first.                   |
| "Test manuale più veloce"                   | Manuale non prova casi limite. Ritesterai ogni cambio.                   |
| "Codice esistente non ha test"              | Lo stai migliorando. Aggiungi test per codice esistente.                 |

## Red Flag - STOP e Ricomincia

- Codice prima del test
- Test dopo implementazione
- Test passa immediatamente
- Non puoi spiegare perché test ha fallito
- Test aggiunti "dopo"
- Razionalizzare "solo questa volta"
- "L'ho già testato manualmente"
- "Test dopo ottengono lo stesso scopo"
- "Riguarda lo spirito non il rituale"
- "Tengo come riferimento" o "adatto codice esistente"
- "Già speso X ore, cancellare è spreco"
- "TDD è dogmatico, sto essendo pragmatico"
- "Questo è diverso perché..."

**Tutti questi significano: Cancella codice. Ricomincia con TDD.**

## Checklist Verifica

Prima di segnare lavoro completo:

- [ ] Ogni nuova funzione/metodo ha un test
- [ ] Guardato ogni test fallire prima di implementare
- [ ] Ogni test fallito per ragione attesa (feature mancante, non typo)
- [ ] Scritto codice minimo per passare ogni test
- [ ] Tutti i test passano
- [ ] Output intatto (no errori, warning)
- [ ] Test usano codice reale (mock solo se inevitabile)
- [ ] Casi limite ed errori coperti

Non puoi spuntare tutte le caselle? Hai saltato TDD. Ricomincia.

## Integrazione Debugging

Trovato bug? Scrivi test fallimentare che lo riproduce. Segui ciclo TDD. Test prova fix e previene regressione.

Mai fixare bug senza un test.

## Regola Finale

```
Codice produzione → test esiste e fallito prima
Altrimenti → non TDD
```

Nessuna eccezione senza permesso del tuo partner umano.
