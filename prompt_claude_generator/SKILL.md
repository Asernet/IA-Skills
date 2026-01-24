---
name: prompt-claude-generator
description: Genera prompt ottimizzati per i modelli Claude (Anthropic), sfruttando tag XML, Chain of Thought e separazione dei contesti.
---

# Prompt Claude Generator

## Descrizione

Skill specializzata nella generazione di prompt altamente ottimizzati per i modelli della famiglia **Claude** (Anthropic). Questa skill sfrutta le specificità dell'architettura di Claude, ponendo forte enfasi sull'uso di **tag XML** per la strutturazione, **Chain of Thought (CoT)**, e una chiara separazione dei contesti.

# RICE PROMPT GENERATOR

## COSA FAI

Trasformi richieste vaghe in prompt strutturati secondo il framework RICE (Role, Instructions, Context, Examples) per massimizzare efficacia LLM.

**Output:** SOLO il prompt generato, zero meta-conversazione.

---

## FRAMEWORK RICE - APPLICAZIONE

Ogni prompt DEVE contenere questi 4 elementi:

### **R - ROLE** (Ruolo)

Chi deve essere l'LLM per questo task?

- **Task tecnico:** "Senior [Technology] Developer/Engineer"
- **Task creativo:** "[Tipo] Copywriter/Designer con esperienza in [settore]"
- **Task analitico:** "[Dominio] Analyst/Consultant con focus su [area]"

**Regola:** Specificità batte generalità. "Python Developer" < "Senior Python Developer specializzato in data pipelines"

### **I - INSTRUCTIONS** (Istruzioni)

Step atomici, imperativi, ordinati logicamente.

**❌ Sbagliato:**

- "Migliora il codice" (vago)
- "Considera best practices" (ambiguo)

**✅ Corretto:**

1. Analizza il codice per [problema specifico]
2. Applica [tecnica precisa] a [elemento identificato]
3. Verifica che [criterio misurabile] sia soddisfatto

**Formato:** Lista numerata, 1 azione per punto, verbi imperativi.

### **C - CONTEXT** (Contesto)

Vincoli, background, formato output, criteri qualità.

**Elementi obbligatori:**

- **Formato output:** JSON/Markdown/Codice/Prosa
- **Vincoli tecnici:** Lunghezza, dipendenze, compatibilità
- **Criterio qualità:** Cosa rende l'output "buono"
- **Cosa evitare:** Anti-pattern, errori comuni

**Elementi opzionali:**

- Background del problema
- Stakeholder target
- Deadline/urgenza

### **E - EXAMPLES** (Esempi)

Input → Output concreto quando migliora comprensione.

**Quando OBBLIGATORIO:**

- Task con output non-ovvio
- Formato specifico richiesto
- Stile/tono particolare

**Quando OPZIONALE:**

- Task standard (es. "traduci testo")
- Istruzioni già cristalline

**Formato:**

```
Input: [esempio concreto]
Output: [risultato atteso completo, non placeholder]
```

---

## STRATEGIA ADATTIVA RICE

### Task Semplice

**Minimo RICE:**

```
ROLE: [expertise base]
INSTRUCTIONS:
1. [azione principale]
CONTEXT: Output formato [X]
```

(Esempi opzionali)

### Task Complesso

**RICE completo:**

```
ROLE: [expertise dettagliata + dominio]
INSTRUCTIONS:
1-5. [step dettagliati]
CONTEXT:
- Formato: [specifico]
- Vincoli: [lista]
- Qualità: [criteri verificabili]
EXAMPLES: [1-2 esempi concreti]
```

### Task Creativo

**RICE enfatizzato su Context:**

```
ROLE: [persona creativa specifica]
INSTRUCTIONS: [step creativi]
CONTEXT:
- Tono: [dettagliato]
- Riferimenti: [esempi stile]
- Evitare: [cliché specifici]
EXAMPLES: [esempi stilistici]
```

---

## CHECKLIST RICE COMPLETA

Prima di generare, verifica presenza di:

**ROLE:**
✓ Expertise specifica (non generica)?  
✓ Livello seniority appropriato?

**INSTRUCTIONS:**
✓ Step numerati e ordinati?  
✓ Verbi imperativi (Analizza/Applica/Verifica)?  
✓ Zero ambiguità (DEVE vs PUÒ chiarito)?

**CONTEXT:**
✓ Formato output esplicito?  
✓ Vincoli tecnici dichiarati?  
✓ Criteri qualità misurabili?

**EXAMPLES:**
✓ Necessari per questo task?  
✓ Input + Output completi (no placeholder)?  
✓ Mostrano formato E contenuto?

---

## ESEMPIO RICE COMPLETO

**Input utente:**  
"Voglio refactoring di questo codice Python"

**Prompt RICE generato:**

`````markdown
## ROLE

Senior Python Developer specializzato in clean code, performance optimization e maintainability. Esperto in PEP8, type system Python 3.10+, e design patterns.

## INSTRUCTIONS

1. Analizza il codice identificando: bug logici, violazioni PEP8, anti-pattern, code smells, problemi performance
2. Riscrivi il codice applicando:
   - Type hinting completo (parametri, return, variabili complesse)
   - Docstring formato Google
   - Naming esplicito (no abbreviazioni)
   - Error handling appropriato
   - Ottimizzazioni performance dove applicabili
3. Genera diff side-by-side (Prima → Dopo)
4. Spiega ogni modifica in italiano indicando categoria (bug/style/performance)

## CONTEXT

**Formato output:**

```
## Codice Refactorato
[codice completo]

## Modifiche Applicate
- [Categoria] Modifica 1: spiegazione
- [Categoria] Modifica 2: spiegazione
```

**Vincoli:**

- Logica funzionale INVARIATA (stesso comportamento I/O)
- NO dipendenze esterne se evitabili con stdlib
- Compatibilità: Python 3.10+
- Max complessità ciclomatica: 10/funzione
- Se codice già ottimale, dichiaralo esplicitamente

**Criteri qualità:**

- Codice eseguibile senza errori
- Ogni modifica giustificata
- Leggibilità > brevità

**Evitare:**

- Over-engineering (no pattern complessi per logica semplice)
- Modifiche puramente estetiche senza valore
- Ottimizzazioni premature

## EXAMPLES

**Input:**

```python
def calc(a,b,op):
    if op=='+': return a+b
    elif op=='-': return a-b
```

**Output:**

````markdown
## Codice Refactorato

```python
from typing import Literal

def calculate_operation(
    first_operand: float,
    second_operand: float,
    operation: Literal['+', '-']
) -> float:
    """Esegue operazione aritmetica tra due numeri.

    Args:
        first_operand: Primo numero dell'operazione
        second_operand: Secondo numero dell'operazione
        operation: Tipo di operazione ('+' addizione, '-' sottrazione)

    Returns:
        Risultato dell'operazione aritmetica

    Raises:
        ValueError: Se operation non è tra i valori supportati
    """
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y
    }

    if operation not in operations:
        raise ValueError(
            f"Operazione '{operation}' non supportata. "
            f"Usa: {', '.join(operations.keys())}"
        )

    return operations[operation](first_operand, second_operand)
```
````
`````

## Modifiche Applicate

- [BUG] Aggiunto error handling per operazioni invalide (prima falliva silenziosamente)
- [STYLE] Rinominato `calc` → `calculate_operation` (PEP8: nomi espliciti)
- [STYLE] Parametri `a,b` → `first_operand, second_operand` (leggibilità)
- [TYPE] Aggiunto type hinting completo: `float` per operandi, `Literal` per operatore
- [DOC] Aggiunta docstring Google-style con Args/Returns/Raises
- [DESIGN] Usato dict+lambda per sostituire if/elif (scalabile, DRY)
- [PERFORMANCE] Nessuna modifica necessaria (operazioni O(1))

```

```

```

```
