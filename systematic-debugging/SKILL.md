---
name: systematic-debugging
description: Usa quando incontri bug o fallimenti di test, per un approccio sistematico alla risoluzione prima di proporre fix.
---

# Debugging Sistematico

## Panoramica

Fix casuali sprecano tempo e creano nuovi bug. Patch veloci mascherano problemi sottostanti.

**Principio core:** Trova SEMPRE la causa radice prima di tentare fix. Fix sintomo sono fallimento.

**Violare la lettera di questo processo è violare lo spirito del debugging.**

## La Legge Ferrea

```
NESSUN FIX SENZA PRIMA INVESTIGAZIONE CAUSA RADICE
```

Se non hai completato la Fase 1, non puoi proporre fix.

## Quando Usare

Usa per QUALSIASI problema tecnico:

- Fallimenti test
- Bug in produzione
- Comportamento inaspettato
- Problemi performance
- Fallimenti build
- Problemi integrazione

**Usa questo SOPRATTUTTO quando:**

- Sotto pressione tempo (emergenze rendono l'indovinare allettante)
- "Solo un fix veloce" sembra ovvio
- Hai già provato fix multipli
- Fix precedente non ha funzionato
- Non capisci pienamente il problema

**Non saltare quando:**

- Problema sembra semplice (bug semplici hanno cause radice pure)
- Sei di fretta (affrettare garantisce rilavorazione)
- Manager lo vuole fixato ORA (sistematico è più veloce che agitarsi)

## Le Quattro Fasi

DEVI completare ogni fase prima di procedere alla prossima.

### Fase 1: Investigazione Causa Radice

**PRIMA di tentare QUALSIASI fix:**

1. **Leggi Messaggi Errore Attentamente**
   - Non saltare errori o warning
   - Spesso contengono la soluzione esatta
   - Leggi stack trace completamente
   - Nota numeri riga, percorsi file, codici errore

2. **Riproduci Consistentemente**
   - Puoi innescarlo affidabilmente?
   - Quali sono i passi esatti?
   - Accade ogni volta?
   - Se non riproducibile → raccogli più dati, non indovinare

3. **Controlla Cambiamenti Recenti**
   - Cosa è cambiato che potrebbe causare questo?
   - Git diff, commit recenti
   - Nuove dipendenze, cambi config
   - Differenze ambientali

4. **Raccogli Prove in Sistemi Multi-Componente**

   **QUANDO sistema ha componenti multipli (CI → build → signing, API → service → database):**

   **PRIMA di proporre fix, aggiungi strumentazione diagnostica:**

   ```
   Per OGNI confine componente:
     - Logga quali dati entrano nel componente
     - Logga quali dati escono dal componente
     - Verifica propagazione ambiente/config
     - Controlla stato a ogni layer

   Esegui una volta per raccogliere prove mostrando DOVE si rompe
   POI analizza prove per identificare componente fallimentare
   POI investiga quel componente specifico
   ```

   **Esempio (sistema multi-layer):**

   ```bash
   # Layer 1: Workflow
   echo "=== Secrets available in workflow: ==="
   echo "IDENTITY: ${IDENTITY:+SET}${IDENTITY:-UNSET}"

   # Layer 2: Build script
   echo "=== Env vars in build script: ==="
   env | grep IDENTITY || echo "IDENTITY not in environment"

   # Layer 3: Signing script
   echo "=== Keychain state: ==="
   security list-keychains
   security find-identity -v

   # Layer 4: Actual signing
   codesign --sign "$IDENTITY" --verbose=4 "$APP"
   ```

   **Questo rivela:** Quale layer fallisce (secrets → workflow ✓, workflow → build ✗)

5. **Traccia Flusso Dati**

   **QUANDO errore è profondo nello stack chiamate:**

   Vedi `root-cause-tracing.md` in questa directory per la tecnica completa di tracciamento a ritroso.

   **Versione veloce:**
   - Dove origina il valore cattivo?
   - Cosa ha chiamato questo con valore cattivo?
   - Continua a tracciare su finché trovi la sorgente
   - Fixa alla sorgente, non al sintomo

### Fase 2: Analisi Pattern

**Trova il pattern prima di fixare:**

1. **Trova Esempi Funzionanti**
   - Localizza codice funzionante simile nella stessa codebase
   - Cosa funziona che è simile a cosa è rotto?

2. **Confronta Contro Riferimenti**
   - Se implementi pattern, leggi implementazione riferimento COMPLETAMENTE
   - Non scorrere - leggi ogni riga
   - Comprendi il pattern pienamente prima di applicare

3. **Identifica Differenze**
   - Cosa è diverso tra funzionante e rotto?
   - Lista ogni differenza, per quanto piccola
   - Non assumere "quello non può importare"

4. **Comprendi Dipendenze**
   - Di quali altri componenti ha bisogno questo?
   - Quali settaggi, config, ambiente?
   - Quali assunzioni fa?

### Fase 3: Ipotesi e Testing

**Metodo scientifico:**

1. **Forma Ipotesi Singola**
   - Dichiara chiaramente: "Penso X è la causa radice perché Y"
   - Scrivilo
   - Sii specifico, non vago

2. **Testa Minimalmente**
   - Fai il PIÙ PICCOLO cambiamento possibile per testare ipotesi
   - Una variabile alla volta
   - Non fixare cose multiple in una volta

3. **Verifica Prima di Continuare**
   - Ha funzionato? Sì → Fase 4
   - Non ha funzionato? Forma NUOVA ipotesi
   - NON aggiungere altri fix sopra

4. **Quando Non Sai**
   - Dì "Non capisco X"
   - Non fingere di sapere
   - Chiedi aiuto
   - Ricerca di più

### Fase 4: Implementazione

**Fixa la causa radice, non il sintomo:**

1. **Crea Caso Test Fallimentare**
   - Riproduzione più semplice possibile
   - Test automatizzato se possibile
   - Script test one-off se nessun framework
   - DEVI avere prima di fixare
   - Usa la skill `superpowers:test-driven-development` per scrivere test fallimentari appropriati

2. **Implementa Singolo Fix**
   - Indirizza la causa radice identificata
   - UN cambiamento alla volta
   - Nessun miglioramento "già che sono qui"
   - Nessun refactoring pacchettizzato

3. **Verifica Fix**
   - Test passa ora?
   - Nessun altro test rotto?
   - Problema effettivamente risolto?

4. **Se Fix Non Funziona**
   - STOP
   - Conta: Quanti fix hai provato?
   - Se < 3: Ritorna a Fase 1, ri-analizza con nuova informazione
   - **Se ≥ 3: STOP e metti in discussione l'architettura (step 5 sotto)**
   - NON tentare Fix #4 senza discussione architetturale

5. **Se 3+ Fix Falliti: Metti in Discussione Architettura**

   **Pattern indicante problema architetturale:**
   - Ogni fix rivela nuovo stato condiviso/accoppiamento/problema in posto diverso
   - Fix richiedono "refactoring massiccio" per implementare
   - Ogni fix crea nuovi sintomi altrove

   **STOP e metti in discussione fondamentali:**
   - Questo pattern è fondamentalmente solido?
   - Stiamo "rimanendo con esso per pura inerzia"?
   - Dovremmo rifattorizzare architettura vs. continuare a fixare sintomi?

   **Discuti col tuo partner umano prima di tentare altri fix**

   Questa NON è un'ipotesi fallita - questa è un'architettura sbagliata.

## Red Flag - STOP e Segui Processo

Se ti sorprendi a pensare:

- "Fix veloce per ora, investogo dopo"
- "Prova solo a cambiare X e vedi se funziona"
- "Aggiungi cambi multipli, esegui test"
- "Salta il test, verificherò manualmente"
- "È probabilmente X, lasciami fixare quello"
- "Non capisco pienamente ma questo potrebbe funzionare"
- "Il pattern dice X ma lo adatterò differentemente"
- "Ecco i problemi principali: [lista fix senza investigazione]"
- Proporre soluzioni prima di tracciare flusso dati
- **"Ancora un tentativo fix" (quando già provato 2+)**
- **Ogni fix rivela nuovo problema in posto diverso**

**TUTTI questi significano: STOP. Ritorna a Fase 1.**

**Se 3+ fix falliti:** Metti in discussione l'architettura (vedi Fase 4.5)

## Segnali dal tuo partner umano Che Lo Stai Facendo Sbagliato

**Fai attenzione a queste ridirezioni:**

- "Quello non sta accadendo?" - Hai assunto senza verificare
- "Ci mostrerà...?" - Avresti dovuto aggiungere raccolta prove
- "Smetti di indovinare" - Stai proponendo fix senza capire
- "Ultrathink this" - Metti in discussione fondamentali, non solo sintomi
- "Siamo bloccati?" (frustrato) - Il tuo approccio non sta funzionando

**Quando vedi questi:** STOP. Ritorna a Fase 1.

## Razionalizzazioni Comuni

| Scusa                                           | Realtà                                                                                    |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------- |
| "Problema è semplice, non serve processo"       | Problemi semplici hanno cause radice pure. Processo è veloce per bug semplici.            |
| "Emergenza, no tempo per processo"              | Debugging sistematico è PIÙ VELOCE che agitarsi a tentativi.                              |
| "Prova solo questo prima, poi investiga"        | Primo fix imposta il pattern. Fallo giusto dall'inizio.                                   |
| "Scriverò test dopo conferma fix funziona"      | Fix non testati non rimangono. Test prima lo prova.                                       |
| "Fix multipli in una volta salva tempo"         | Non puoi isolare cosa ha funzionato. Causa nuovi bug.                                     |
| "Riferimento troppo lungo, adatterò il pattern" | Comprensione parziale garantisce bug. Leggilo completamente.                              |
| "Vedo il problema, lasciami fixarlo"            | Vedere sintomi ≠ capire causa radice.                                                     |
| "Ancora un tentativo fix" (dopo 2+ fallimenti)  | 3+ fallimenti = problema architetturale. Metti in discussione pattern, non fixare ancora. |

## Riferimento Rapido

| Fase                   | Attività Chiave                                          | Criteri Successo           |
| ---------------------- | -------------------------------------------------------- | -------------------------- |
| **1. Causa Radice**    | Leggi errori, riproduci, controlla cambi, raccogli prove | Capire COSA e PERCHÉ       |
| **2. Pattern**         | Trova esempi funzionanti, confronta                      | Identifica differenze      |
| **3. Ipotesi**         | Forma teoria, testa minimalmente                         | Confermata o nuova ipotesi |
| **4. Implementazione** | Crea test, fixa, verifica                                | Bug risolto, test passano  |

## Quando il Processo Rivela "Nessuna Causa Radice"

Se l'investigazione sistematica rivela che il problema è veramente ambientale, dipendente da timing, o esterno:

1. Hai completato il processo
2. Documenta cosa hai investigato
3. Implementa gestione appropriata (retry, timeout, messaggio errore)
4. Aggiungi monitoraggio/logging per investigazione futura

**Ma:** 95% dei casi "nessuna causa radice" sono investigazione incompleta.

## Tecniche di Supporto

Queste tecniche sono parte del debugging sistematico e disponibili in questa directory:

- **`root-cause-tracing.md`** - Traccia bug all'indietro attraverso stack chiamate per trovare innesco originale
- **`defense-in-depth.md`** - Aggiungi validazione a layer multipli dopo aver trovato causa radice
- **`condition-based-waiting.md`** - Rimpiazza timeout arbitrari con polling condizione

**Skill correlate:**

- **superpowers:test-driven-development** - Per creare caso test fallimentare (Fase 4, Passo 1)
- **superpowers:verification-before-completion** - Verifica fix ha funzionato prima di reclamare successo

## Impatto Mondo Reale

Da sessioni di debugging:

- Approccio sistematico: 15-30 minuti per fixare
- Approccio fix casuali: 2-3 ore di agitazione
- Tasso fix prima-volta: 95% vs 40%
- Nuovi bug introdotti: Vicino zero vs comune
