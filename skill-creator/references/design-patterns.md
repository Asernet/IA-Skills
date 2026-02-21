# Design Patterns per Skill AI

Questi pattern devono essere applicati per garantire che le skill siano coerenti e di alta qualità.

## 1. Pattern di Output (Template)

Usa sempre un formato strutturato per i report o le risposte complesse.

### Template Rigido

```markdown
# [Titolo Analisi]

## Sintesi Esecutiva

[Descrizione breve]

## Risultati Chiave

- [Dato 1]
- [Dato 2]
```

## 2. Pattern di Workflow

### Sequenziale

1. Analisi -> 2. Elaborazione -> 3. Verifica.
   Sempre mostrare lo stato di avanzamento all'utente.

### Condizionale

"Se l'input è X, segui il workflow A; se è Y, segui il workflow B."

## 3. Gerarchia Informativa (Progressive Disclosure)

- **SKILL.md**: Solo istruzioni critiche.
- **references/**: Documentazione estesa e guide tecniche.
- **examples/**: Esempi pratici di conversazione.
