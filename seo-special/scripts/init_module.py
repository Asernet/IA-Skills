import sys
import subprocess
import importlib.metadata

def check_env():
    print("--- Verifica Ambiente SEO-Special ---")
    
    # 1. Verifica Python
    print(f"Python: {sys.version.split()[0]} [OK]")
    
    # 2. Verifica Dipendenze
    import os
    req_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'requirements.txt')
    try:
        with open(req_file, 'r') as f:
            for line in f:
                req = line.strip().split('>=')[0].split('==')[0].split('<')[0].split('>')[0]
                if req and not req.startswith('#'):
                    try:
                        importlib.metadata.version(req)
                        print(f"Dipendenza {req}: [OK]")
                    except importlib.metadata.PackageNotFoundError:
                        print(f"Dipendenza {req}: [MANCANTE]")
    except Exception as e:
        print(f"Errore lettura requirements: {e}")

    # 3. Verifica Playwright
    try:
        import playwright
        print("Playwright: [INSTALLATO]")
        # Verifica Chromium
        # (Semplificata: controlliamo se il comando 'playwright' è nel PATH)
        result = subprocess.run(["playwright", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Playwright CLI: {result.stdout.strip()} [OK]")
        else:
            print("Playwright CLI: [NON TROVATO NEL PATH]")
    except ImportError:
        print("Playwright: [NON INSTALLATO]")

if __name__ == "__main__":
    check_env()
