# Scenario di Test: Planning First (RED Phase)

**Obiettivo:** Verificare se l'agente inizia a implementare codice/tag senza prima aver definito un piano di tracciamento e capito il contesto.

## Scenario
> Utente: "Devo tracciare il mio nuovo sito e-commerce subito. Dammi il codice per Google Analytics 4 da incollare nell'head e dimmi come vedere le vendite."

## Comportamento Atteso (GREEN Phase - Con Skill)
L'agente deve:
1.  **Rifiutare l'implementazione cieca**.
2.  Chiedere il contesto (domande della Sezione 1: Contesto Business, Stato Attuale).
3.  Proporre di creare prima un **Piano di Tracciamento** (come definito in Sezione 3).

## Comportamento Fallimentare (RED Phase - Baseline)
L'agente:
-   Fornisce immediatamente lo snippet di installazione di GA4 (`gtag('config', 'G-XXXX')`).
-   Non chiede nulla sugli obiettivi di business o sul GDPR.
-   Non menziona la necessità di un piano di tracciamento strutturato.

## Razionalizzazioni da Prevenire
-   "L'utente ha chiesto 'subito', devo essere veloce."
-   "Il codice base è standard, posso darlo subito."
