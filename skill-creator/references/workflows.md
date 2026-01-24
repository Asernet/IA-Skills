# Pattern di Workflow

## Workflow Sequenziali

Per task complessi, suddividi le operazioni in passaggi chiari e sequenziali. Spesso è utile fornire al modello una panoramica del processo all'inizio del file SKILL.md:

```markdown
La compilazione di un modulo PDF richiede questi passaggi:

1. Analizza il modulo (esegui analyze_form.py)
2. Crea mappatura campi (modifica fields.json)
3. Valida mappatura (esegui validate_fields.py)
4. Compila il modulo (esegui fill_form.py)
5. Verifica output (esegui verify_output.py)
```

## Workflow Condizionali

Per task con logica ramificata, guida il modello attraverso i punti decisionali:

```markdown
1. Determina il tipo di modifica:
   **Creazione nuovo contenuto?** → Segui "Workflow creazione" qui sotto
   **Modifica contenuto esistente?** → Segui "Workflow modifica" qui sotto

2. Workflow creazione: [passaggi]
3. Workflow modifica: [passaggi]
```
