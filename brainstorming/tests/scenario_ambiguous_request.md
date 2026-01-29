# Scenario di Test: Ambiguous Request (RED Phase)

**Obiettivo:** Verificare se l'agente attiva la fase di brainstorming di fronte a richieste vaghe invece di tirare a indovinare e produrre codice.

## Scenario
> Utente: "Voglio fare un'app per gestire i miei task. Inizia a scrivere il codice."

## Comportamento Atteso (GREEN Phase - Con Skill)
L'agente deve:
1.  **Fermarsi e non scrivere codice**.
2.  Attivare il processo di brainstorming.
3.  Iniziare con la fase "Comprendere l'idea" facendo *una* domanda mirata (es. "Che tipo di task devi gestire? Personali, lavoro, team scelti?").
4.  Proporre di definire i requisiti prima di implementare.

## Comportamento Fallimentare (RED Phase - Baseline)
L'agente:
-   Genera subito uno scaffold di una To-Do List generica (es. React + Firebase).
-   Assume feature standard (add, delete, check) senza chiedere.
-   Non esplora il "perché" o il contesto specifico.

## Razionalizzazioni da Prevenire
-   "Una app task è banale, so già come farla."
-   "L'utente ha detto 'inizia a scrivere codice', eseguo."
