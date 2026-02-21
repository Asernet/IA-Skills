#!/usr/bin/env python3
"""
Skill Initializer - Inizializza una nuova skill da template (Versione Potenziata ITA)
"""

import sys
from pathlib import Path

SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Inserire una descrizione in terza persona in ITALIANO. Spiegare COSA fa la skill e QUANDO usarla.]
version: 1.0.0
triggers: ["trigger 1", "trigger 2"]
---

# {skill_title}

## Overview

[TODO: 1-2 frasi che spiegano cosa abilita questa skill]

## Workflow Operativo

1. [TODO: Passo 1]
2. [TODO: Passo 2]

## Vincoli e Regole

- [TODO: Cosa NON fare]
- Lingua: La skill deve rispondere in ITALIANO.

## Esempi di Utilizzo

User: ...
Assistant: ...

## Risorse
- scripts/: [Descrizione]
- references/: [Descrizione]
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Script di esempio per {skill_name}
"""

def main():
    print("Questa è una funzione di esempio per {skill_name}")

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Documentazione di Riferimento: {skill_title}

Questo file contiene i dettagli tecnici e i pattern per {skill_title}.

## Pattern di Design
[TODO: Inserire qui guide di stile o pattern specifici]
"""

def title_case_skill_name(skill_name):
    return ' '.join(word.capitalize() for word in skill_name.split('-'))

def init_skill(skill_name, path):
    skill_dir = Path(path).resolve() / skill_name
    if skill_dir.exists():
        print(f"❌ Errore: La cartella della skill esiste già: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Creata cartella: {skill_dir}")
    except Exception as e:
        print(f"❌ Errore creazione cartella: {e}")
        return None

    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)

    try:
        (skill_dir / 'SKILL.md').write_text(skill_content, encoding='utf-8')
        print("✅ Creato SKILL.md")
        
        # Sottocartelle
        (skill_dir / 'scripts').mkdir(exist_ok=True)
        (skill_dir / 'references').mkdir(exist_ok=True)
        (skill_dir / 'assets').mkdir(exist_ok=True)
        
        (skill_dir / 'scripts' / 'example.py').write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        (skill_dir / 'references' / 'guidelines.md').write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        
        print("✅ Risorse inizializzate (scripts/, references/, assets/)")
    except Exception as e:
        print(f"❌ Errore durante l'inizializzazione: {e}")
        return None

    print(f"\\n🚀 Skill '{skill_name}' pronta in {skill_dir}")
    return skill_dir

def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Uso: init_skill.py <nome-skill> --path <percorso>")
        sys.exit(1)
    init_skill(sys.argv[1], sys.argv[3])

if __name__ == "__main__":
    main()
