---
name: skills-library-manager
description: Gestisce la libreria delle skill eseguendo validazione, indicizzazione e aggiornamento del Vademecum in Obsidian.
---

# Skills Library Manager

Skill per orchestrare la manutenzione della libreria delle skill.

## Ruolo

Quando l'utente chiede di "aggiornare la libreria skill", "validare le skill", o "sincronizzare il vademecum", esegui lo script di gestione.

## Istruzioni Operative

1. Esegui lo script:

   ```bash
   python "/skills/skills-library-manager/scripts/manage_library.py"
   ```

2. Lo script esegue automaticamente:
   - **Validazione** di tutte le skill (struttura SKILL.md)
   - Se KO: Creazione file **⚠️ Skills Alert.md** in Obsidian con errori

3. Se tutti i passaggi precedenti di controllo sono ok, quindi non ci sono stati errori fail il push delle skill su github.

4. Comunica all'utente il risultato finale.

## Vincoli

- Non modificare manualmente i file generati (`skills_index.json`, `Vademecum Skills.md`)
- Se ci sono errori di validazione, correggili prima di rieseguire
