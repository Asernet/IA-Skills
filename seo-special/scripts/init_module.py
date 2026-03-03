import sys
import subprocess
import pkg_resources

def check_env():
    print("--- Verifica Ambiente SEO-Special ---")
    
    # 1. Verifica Python
    print(f"Python: {sys.version.split()[0]} [OK]")
    
    # 2. Verifica Dipendenze
    import os
    req_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'requirements.txt')
    try:
        with open(req_file, 'r') as f:
            requirements = pkg_resources.parse_requirements(f)
            for requirement in requirements:
                try:
                    pkg_resources.require(str(requirement))
                    print(f"Dipendenza {requirement}: [OK]")
                except pkg_resources.DistributionNotFound:
                    print(f"Dipendenza {requirement}: [MANCANTE]")
                except pkg_resources.VersionConflict as e:
                    print(f"Dipendenza {requirement}: [CONFLITTO VERSIONI - {e}]")
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
