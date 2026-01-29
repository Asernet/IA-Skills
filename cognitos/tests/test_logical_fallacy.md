# Test Scenario: Logical Fallacy (Circular Reasoning / Begging the Question)

## Objective
Test Cognitos' ability to dismantle circular reasoning (Circulus in Probando).

## Input Prompt
```text
"La telepatia deve esistere per forza. Come faccio a saperlo? Perché posso sentire i pensieri degli altri. E il fatto che io senta i pensieri degli altri è la prova definitiva che la telepatia è un fenomeno reale."
```

## Expected Behavior (Pass Criteria)
1.  **Diagnosis**: Identifies Circular Reasoning (Presupposing the conclusion in the premise).
2.  **Socratic Dialogue** (Optional but good): Asks "How do you distinguish hearing thoughts from imagining them?"
3.  **Deconstruction**: Points out that the proof relies entirely on the claim itself being true.

## Baseline (Fail Criteria)
- Engaging in a debate about telepatia instead of the logic structure.
- Failing to identify that A proves B and B proves A.
