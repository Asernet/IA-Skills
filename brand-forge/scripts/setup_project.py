#!/usr/bin/env python3
import os
import sys

def main():
    """Crea la struttura delle cartelle necessaria per il progetto di branding nella cartella Documenti."""
    # Percorso dinamico alla cartella Documenti dell'utente
    home = os.path.expanduser("~")
    base_output = os.path.join(home, "Documents", "brand_assets")
    
    if not os.path.exists(base_output):
        os.makedirs(base_output)
        print(f"✅ Cartella di output creata in: {base_output}")
    else:
        print(f"ℹ️ Cartella di output già esistente: {base_output}")

if __name__ == "__main__":
    main()
