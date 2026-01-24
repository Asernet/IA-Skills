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
   python "C:\Users\mazin\.gemini\skills\skills-library-manager\scripts\manage_library.py"
   ```

2. Lo script esegue automaticamente:
   - **Validazione** di tutte le skill (struttura SKILL.md)
   - Se OK: **Indicizzazione** e **Aggiornamento Vademecum** in Obsidian
   - Se KO: Creazione file **⚠️ Skills Alert.md** in Obsidian con errori

3. Comunica all'utente il risultato finale.

## Vincoli

- Non modificare manualmente i file generati (`skills_index.json`, `Vademecum Skills.md`)
- Se ci sono errori di validazione, correggili prima di rieseguire
