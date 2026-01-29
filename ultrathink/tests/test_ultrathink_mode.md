# Test Scenario: ULTRATHINK Protocol

## Objective
Verify the deep system analysis trigger.

## Input Prompt
```text
"ULTRATHINK: Sto progettando un sistema per gestire i voti di un talent show nazionale in tempo reale. Milioni di utenti concorrenti."
```

## Expected Behavior (Pass Criteria)
1.  **Depth**: Massive shift in detailedness compared to default mode.
2.  **Structure**: Explicitly addresses the 4 lenses:
    - **Integrità Dati** (e.g., handling rapid writes, eventual consistency).
    - **Sicurezza** (e.g., bot prevention, rate limiting).
    - **Performance** (e.g., caching layers, message queues).
    - **UX/DX** (e.g., optimistic UI updates).
3.  **No Hacks**: Recommendations are enterprise-grade (e.g., Kafka, Redis, ScyllaDB).

## Baseline (Fail Criteria)
- Just writing a simple SQL schema without context.
- Ignoring the scale ("Millions of users").
- Missing one of the 4 required analysis lenses.
