import os
import argparse

def init_project(path):
    print(f"Inizializzazione progetto in: {path}")
    
    # 1. Creazione directory
    directories = ['directives', 'execution', '.tmp']
    for directory in directories:
        dir_path = os.path.join(path, directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Creato: {dir_path}")
        else:
            print(f"Gia' esistente: {dir_path}")

    # 2. Creazione .env (se non esiste)
    env_path = os.path.join(path, '.env')
    if not os.path.exists(env_path):
        with open(env_path, 'w') as f:
            pass
        print(f"Creato: .env")

    # 3. Creazione .gitignore
    gitignore_path = os.path.join(path, '.gitignore')
    gitignore_content = ".env\n.tmp/\n__pycache__/\n*.py[cod]\n*$py.class\n"
    with open(gitignore_path, 'w') as f:
        f.write(gitignore_content)
    print(f"Aggiornato/Creato: .gitignore")

    # 4. Creazione template direttiva
    template_path = os.path.join(path, 'directives', 'template.md')
    template_content = """# Titolo della Direttiva (SOP)

## Obiettivo
[Descrizione breve]

## Input
- [ ] Parametro 1

## Tool/Esecuzione
1. Richiama lo script `execution/nome_script.py`

## Output
- [ ] Risultato atteso

## Casi Limite & Errori
- Errore API...
"""
    if not os.path.exists(template_path):
        with open(template_path, 'w') as f:
            f.write(template_content)
        print(f"Creato: directives/template.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Inizializza struttura DOE')
    parser.add_argument('--path', required=True, help='Percorso del progetto')
    args = parser.parse_args()
    
    path = os.path.abspath(args.path)
    if os.path.isdir(path):
        init_project(path)
    else:
        print(f"Errore: {path} non e' una directory valida.")
