# Esecuzione Piani

## Panoramica

Carica piano, revisiona criticamente, esegui task in batch, riporta per revisione tra batch.

**Principio base:** Esecuzione in batch con checkpoint per revisione architetto.

**Annuncia all'inizio:** "Sto usando la guida interna di brainstorming (ex executing-plans) per implementare questo piano."

## Il Processo

### Passo 1: Carica e Revisiona Piano

1. Leggi file piano
2. Revisiona criticamente - identifica qualsiasi domanda o preoccupazione sul piano
3. Se preoccupazioni: Sollevale con il tuo partner umano prima di iniziare
4. Se nessuna preoccupazione: Crea TodoWrite e procedi

### Passo 2: Esegui Batch

**Default: Primi 3 task**

Per ogni task:

1. Segna come in_progress
2. Segui ogni passaggio esattamente (il piano ha passaggi a misura di morso)
3. Esegui verifiche come specificato
4. Segna come completato

### Passo 3: Riporta

Quando batch completo:

- Mostra cosa è stato implementato
- Mostra output verifica
- Dì: "Pronto per feedback."

### Passo 4: Continua

Basato su feedback:

- Applica cambiamenti se necessario
- Esegui prossimo batch
- Ripeti finché completo

### Passo 5: Completa Sviluppo

Dopo che tutti i task sono completi e verificati:

- Annuncia: "Sto usando la skill finishing-a-development-branch per completare questo lavoro."
- **SOTTO-SKILL RICHIESTA:** Usa superpowers:finishing-a-development-branch
- Segui quella skill per verificare test, presentare opzioni, eseguire scelta

## Quando Fermarsi e Chiedere Aiuto

**FERMATI ed esegui immediatamente quando:**

- Colpisci un blocco a metà batch (dipendenza mancante, test fallisce, istruzione non chiara)
- Il piano ha gap critici che prevengono l'inizio
- Non capisci un'istruzione
- La verifica fallisce ripetutamente

**Chiedi chiarimento piuttosto che indovinare.**

## Quando Rivisitare Passaggi Precedenti

**Torna alla Revisione (Passo 1) quando:**

- Il partner aggiorna il piano basato sul tuo feedback
- L'approccio fondamentale necessita ripensamento

**Non forzare attraverso i blocchi** - fermati e chiedi.

## Ricorda

- Revisiona piano criticamente prima
- Segui passaggi piano esattamente
- Non saltare verifiche
- Referenzia skill quando il piano dice di farlo
- Tra batch: riporta solo e aspetta
- Fermati quando bloccato, non indovinare
