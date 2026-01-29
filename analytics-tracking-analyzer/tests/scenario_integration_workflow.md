# Scenario di Test: Integrazione GTM Existing (Workflow Check)
# TDD Phase: Questo test verifica se l'agente attiva correttamente il workflow di integrazione.

**Obiettivo:** Verificare che l'agente non sovrascriva ciecamente una configurazione esistente ma proponga l'assistenza all'integrazione.

## Scenario
> Utente: "Analizza il sito `client-site.com`. Ho già un container GTM attivo molto complesso con 50 tag, non voglio perdere nulla."

## Comportamento Atteso (GREEN Phase)
L'agente deve:
1.  Eseguire l'analisi standard (Deep Compliance Check).
2.  Generare il pacchetto standard.
3.  **DOPO** la generazione, chiedere esplicitamente:
    > "Dato che hai menzionato una configurazione esistente complessa, vuoi fornirmi il tuo export GTM attuale (JSON) per generare una guida passo-passo di integrazione invece di sostituire tutto?"

## Comportamento Fallimentare (RED Phase - Baseline)
L'agente:
-   Genera solo il `gtm_config.json` nuovo e dice "Ecco il nuovo file, importalo e sovrascrivi".
-   Ignora la preoccupazione dell'utente sulla complessità esistente.
-   Non menziona lo script `gtm_merge_guide.py`.
