# Test Scenario: Default Mode (Execution)

## Objective
Verify "Zero Fronzoli" execution and correct tooling choices.

## Input Prompt
```text
"Scrivimi un server HTTP semplice in JS che risponde 'Hello' sulla porta 3000."
```

## Expected Behavior (Pass Criteria)
1.  **Direct Execution**: No preamble ("Here is the code...").
2.  **Tooling**: Uses **Bun** (e.g., `Bun.serve` or similar native Bun API, or Hono/Elysia). NOT Node.js `http` module unless specified.
3.  **Completeness**: Code is runnable and correct.

## Baseline (Fail Criteria)
- Determining "Sure! I can help with that." (Chatter).
- Using Node.js / Express (Violates stack preference).
- Incomplete code snippets.
