# Workflow di Aggiornamento Selettivo

Questo documento descrive la procedura per aggiornare il repository locale con le modifiche dal remote `asernet`, mantenendo il controllo su quali nuove cartelle sincronizzare.

## Procedura

1.  **Analisi delle Differenze**
    Esegui lo script di controllo per vedere cosa sta arrivando dal repository remoto:
    ```bash
    python scripts/check_incoming.py
    ```
    *Opzionale: puoi specificare un branch diverso, es. `python scripts/check_incoming.py origin/main`*

2.  **Decisione**
    Lo script elencherà le cartelle contrassegnate come `[NUOVO]`.
    *   Se vuoi accettarle (sincronizzarle): Non fare nulla.
    *   Se vuoi rifiutarle (non scaricarle): Copia il nome della cartella e aggiungilo al tuo file `.gitignore` (alla radice del repo).

3.  **Aggiornamento (Merge)**
    Una volta configurato il `.gitignore` con le esclusioni desiderate, procedi con il merge:
    ```bash
    git merge asernet/main
    ```

## Note Importanti
- Se aggiungi una cartella al `.gitignore` PRIMA del merge, git eviterà di tracciarla.
- Se una cartella esiste già in locale, lo script la ignorerà (è considerata già accettata).
- Lo script esegue automaticamente un `git fetch` prima dell'analisi.
