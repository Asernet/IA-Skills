import os
import sys
import subprocess
import venv
from pathlib import Path

# Configurazione percorsi
SCRIPT_DIR = Path(__file__).parent.absolute()
SKILL_ROOT = SCRIPT_DIR.parent
VENV_DIR = SKILL_ROOT / ".venv"

# Determinazione percorsi eseguibili in base al SO
if sys.platform == "win32":
    PYTHON_EXEC = VENV_DIR / "Scripts" / "python.exe"
    PIP_EXEC = VENV_DIR / "Scripts" / "pip.exe"
else:
    PYTHON_EXEC = VENV_DIR / "bin" / "python"
    PIP_EXEC = VENV_DIR / "bin" / "pip"

def ensure_environment():
    """Verifica e crea l'ambiente virtuale se necessario."""
    if not VENV_DIR.exists():
        print(f"[INFO] Creazione virtual environment in {VENV_DIR}...")
        try:
            venv.create(VENV_DIR, with_pip=True)
        except Exception as e:
            print(f"[ERROR] Impossibile creare venv: {e}")
            sys.exit(1)

    # Verifica se theHarvester è installato
    # Usiamo un flag file o proviamo a importare nel venv per check veloce?
    # Meglio check con pip freeze o chiamata diretta
    try:
        subprocess.check_call(
            [str(PYTHON_EXEC), "-c", "import theHarvester"], 
            stdout=subprocess.DEVNULL, 
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print("[INFO] Installazione theHarvester in corso (richiede tempo)...")
        try:
            # Aggiorna pip per sicurezza
            subprocess.check_call(
                [str(PYTHON_EXEC), "-m", "pip", "install", "--upgrade", "pip"],
                stdout=subprocess.DEVNULL
            )
            # Installa theHarvester direttamente da GitHub per avere l'ultima versione funzionante
            subprocess.check_call(
                [str(PIP_EXEC), "install", "git+https://github.com/laramies/theHarvester.git"],
                stdout=sys.stdout,
                stderr=sys.stderr
            )
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Installazione fallita: {e}")
            sys.exit(1)

def run_harvester(args):
    """Esegue theHarvester con gli argomenti passati."""
    if not args:
        print("Uso: python harvest.py -d <domain> -b <source> [options]")
        # Eseguiamo --help come fallback
        cmd = [str(PYTHON_EXEC), "theHarvester.py", "--help"] 
        # Nota: theHarvester installato via pip espone un entry point 'theHarvester' solitamente.
        # Controlliamo se esiste lo script o il modulo.
        # Se installato via pip, si lancia con `theHarvester` (binario) o `python -m theHarvester`.
        cmd = [str(PYTHON_EXEC), "-m", "theHarvester", "--help"]
    else:
        cmd = [str(PYTHON_EXEC), "-m", "theHarvester"] + args

    print(f"[EXEC] {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=False)
    except KeyboardInterrupt:
        print("\n[INFO] Interrotto dall'utente.")

if __name__ == "__main__":
    print("--- Data Enricher OSINT Module ---")
    ensure_environment()
    
    # Passiamo tutti gli argomenti ricevuti allo script wrapper
    script_args = sys.argv[1:]
    run_harvester(script_args)
