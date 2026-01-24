#!/usr/bin/env python3
"""
Skills Library Manager - Orchestra validazione, indicizzazione e aggiornamento Obsidian

Esegue in sequenza:
1. validate_skills.py - Verifica struttura SKILL.md
2. generate_index.py - Genera skills_index.json
3. update_vademecum.py - Aggiorna Vademecum Skills in Obsidian

Se la validazione fallisce, crea un file di alert in Obsidian.

Usage:
  python manage_library.py
"""

import os
import sys
import re
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
SKILLS_DIR = os.path.join(BASE_DIR, "skills")
OBSIDIAN_ALERT_PATH = r"C:\Users\mazin\ObsidianWork\Gemini\⚠️ Skills Alert.md"

def validate_skills():
    """Valida tutte le skill e restituisce (success, errors)"""
    print("🔍 Validazione skill in corso...")
    errors = []
    skill_count = 0

    for root, dirs, files in os.walk(SKILLS_DIR):
        dirs[:] = [d for d in dirs if d != '.disabled']
        if "SKILL.md" in files:
            skill_count += 1
            skill_path = os.path.join(root, "SKILL.md")
            rel_path = os.path.relpath(skill_path, SKILLS_DIR)
            
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            has_frontmatter = content.strip().startswith("---")
            has_header = re.search(r'^#\s+', content, re.MULTILINE)
            
            if not (has_frontmatter or has_header):
                errors.append(f"❌ {rel_path}: Manca frontmatter o heading principale")
            
            if has_frontmatter:
                fm_match = re.search(r'^---\s*(.*?)\s*---', content, re.DOTALL)
                if fm_match:
                    fm_content = fm_match.group(1)
                    if "name:" not in fm_content:
                        errors.append(f"⚠️ {rel_path}: Frontmatter manca 'name:'")
                    if "description:" not in fm_content:
                        errors.append(f"⚠️ {rel_path}: Frontmatter manca 'description:'")
                else:
                    errors.append(f"❌ {rel_path}: Frontmatter malformato")

    print(f"✅ Controllate {skill_count} skill.")
    return (len(errors) == 0, errors, skill_count)

def generate_index():
    """Esegue generate_index.py"""
    print("\n📇 Generazione indice skill...")
    import subprocess
    script_path = os.path.join(SCRIPTS_DIR, "generate_index.py")
    subprocess.run([sys.executable, script_path], check=True)

def update_vademecum():
    """Esegue update_vademecum.py"""
    print("\n📝 Aggiornamento Vademecum Obsidian...")
    import subprocess
    script_path = os.path.join(SCRIPTS_DIR, "update_vademecum.py")
    subprocess.run([sys.executable, script_path], check=True)

def create_alert_file(errors):
    """Crea file di alert in Obsidian con gli errori"""
    print(f"\n📢 Creazione file alert in Obsidian...")
    
    content_lines = [
        "# ⚠️ Skills Validation Alert",
        "",
        f"**Data**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Errori Rilevati",
        "",
    ]
    
    for error in errors:
        content_lines.append(f"- {error}")
    
    content_lines.extend([
        "",
        "---",
        "_Correggi gli errori e riesegui `manage_library.py`_",
    ])
    
    content = "\n".join(content_lines)
    
    with open(OBSIDIAN_ALERT_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ File alert creato: {OBSIDIAN_ALERT_PATH}")

def remove_alert_file():
    """Rimuove il file di alert se esiste (validazione OK)"""
    if os.path.exists(OBSIDIAN_ALERT_PATH):
        os.remove(OBSIDIAN_ALERT_PATH)
        print("🗑️ File alert precedente rimosso.")

def main():
    print("=" * 50)
    print("🔧 SKILLS LIBRARY MANAGER")
    print("=" * 50)
    print()
    
    # Step 1: Validazione
    success, errors, skill_count = validate_skills()
    
    if success:
        print("\n✨ Validazione completata senza errori!")
        remove_alert_file()
        
        # Step 2: Indicizzazione
        generate_index()
        
        # Step 3: Aggiornamento Obsidian
        update_vademecum()
        
        print("\n" + "=" * 50)
        print(f"🎉 COMPLETATO! {skill_count} skill gestite.")
        print("=" * 50)
    else:
        print(f"\n❌ Validazione fallita con {len(errors)} errori:")
        for error in errors:
            print(f"   {error}")
        
        # Crea file alert
        create_alert_file(errors)
        
        print("\n" + "=" * 50)
        print("⚠️ Correggi gli errori e riesegui.")
        print("=" * 50)
        sys.exit(1)

if __name__ == "__main__":
    main()
