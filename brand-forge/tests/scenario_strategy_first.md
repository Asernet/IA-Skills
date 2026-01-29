# Scenario di Test: Strategy First (RED Phase)

**Obiettivo:** Verificare se l'agente esegue la fase strategica (Blueprint) prima di generare asset visivi, anche se l'utente chiede direttamente il logo.

## Scenario
> Utente: "Ho bisogno di un logo per la mia start-up di scarpe vegane. Fammi subito 4 proposte."

## Comportamento Atteso (GREEN Phase - Con Skill)
L'agente deve:
1.  **Non generare immagini immediatamente**.
2.  Attivare la **Fase 1: Brand Architecture**.
3.  Spiegare che per fare un logo efficace serve prima capire il brand (Soul, Archetipo, Target).
4.  Attivare la ricerca sui competitor (Market Scanning) o fare domande strategiche.

## Comportamento Fallimentare (RED Phase - Baseline)
L'agente:
-   Attiva subito `generate_image` con prompt generici ("vegan shoes logo").
-   Non crea nessun documento di Blueprint.
-   Non chiede nulla sul posizionamento o sui valori del brand.

## Razionalizzazioni da Prevenire
-   "L'utente ha chiesto solo il logo."
-   "Posso fare il logo e poi spiegare perché ho scelto quei colori."
