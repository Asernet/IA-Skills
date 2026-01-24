---
name: using-superpowers
description: Usa all'inizio di ogni conversazione per stabilire come trovare e invocare le skill.
---

<EXTREMELY-IMPORTANT>
If you think there is even a 1% chance a skill might apply to what you are doing, you ABSOLUTELY MUST invoke the skill.

IF A SKILL APPLIES TO YOUR TASK, YOU DO NOT HAVE A CHOICE. YOU MUST USE IT.

This is not negotiable. This is not optional. You cannot rationalize your way out of this.
</EXTREMELY-IMPORTANT>

## Come Accedere alle Skill

**In Claude Code:** Usa il tool `Skill`. Quando invochi una skill, il suo contenuto è caricato e presentato a te—seguilo direttamente. Mai usare il tool Read su file skill.

**In altri ambienti:** Controlla la documentazione della tua piattaforma per come le skill sono caricate.

# Usare Skill

## La Regola

**Invoca skill rilevanti o richieste PRIMA di qualsiasi risposta o azione.** Anche un 1% di possibilità che una skill possa applicarsi significa che dovresti invocare la skill per controllare. Se una skill invocata si rivela sbagliata per la situazione, non devi usarla.

## Red Flag

Questi pensieri significano STOP—stai razionalizzando:

| Pensiero                                  | Realtà                                                         |
| ----------------------------------------- | -------------------------------------------------------------- |
| "Questa è solo una domanda semplice"      | Domande sono task. Controlla per skill.                        |
| "Ho bisogno di più contesto prima"        | Controllo skill viene PRIMA domande chiarificatrici.           |
| "Lasciami esplorare la codebase prima"    | Skill ti dicono COME esplorare. Controlla prima.               |
| "Posso controllare git/file velocemente"  | I file mancano di contesto conversazione. Controlla per skill. |
| "Lasciami raccogliere informazioni prima" | Skill to dicono COME raccogliere informazioni.                 |
| "Questo non necessita una skill formale"  | Se una skill esiste, usala.                                    |
| "Ricordo questa skill"                    | Skill evolvono. Leggi versione corrente.                       |
| "Questo non conta come un task"           | Azione = task. Controlla per skill.                            |
| "La skill è eccessiva"                    | Cose semplici diventano complesse. Usala.                      |
| "Farò solo questa cosa prima"             | Controlla PRIMA di fare qualsiasi cosa.                        |
| "Questo sembra produttivo"                | Azione indisciplinata spreca tempo. Skill prevengono questo.   |
| "So cosa significa"                       | Conoscere il concetto ≠ usare la skill. Invocala.              |

## Priorità Skill

Quando skill multiple potrebbero applicarsi, usa questo ordine:

1. **Skill di processo prima** (brainstorming, debugging) - queste determinano COME approcciare il task
2. **Skill di implementazione dopo** (frontend-design, mcp-builder) - queste guidano esecuzione

"Costruiamo X" → brainstorming prima, poi skill implementazione.
"Fixa questo bug" → debugging prima, poi skill dominio-specifiche.

## Tipi Skill

**Rigide** (TDD, debugging): Segui esattamente. Non adattare via la disciplina.

**Flessibili** (pattern): Adatta principi al contesto.

La skill stessa ti dice quale.

## Istruzioni Utente

Istruzioni dicono COSA, non COME. "Aggiungi X" o "Fixa Y" non significa saltare workflow.
