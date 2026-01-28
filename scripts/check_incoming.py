import argparse
import subprocess
import sys
import os

def run_git_command(command, cwd=None):
    """Esegue un comando git e restituisce l'output."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Errore nell'esecuzione del comando: {' '.join(command)}")
        print(e.stderr)
        sys.exit(1)

def get_incoming_changes(remote_branch):
    """Ottiene la lista dei file aggiunti nel remote rispetto al locale."""
    # git diff --name-status HEAD..remote_branch
    # Filtriamo per 'A' (Added). Anche le modifiche 'M' a file esistenti ci interessano? 
    # La richiesta specifica è "nuove cartelle che arrivano". 
    # Quindi ci concentriamo su ciò che non esiste in locale.
    
    output = run_git_command(["git", "diff", "--name-status", f"HEAD..{remote_branch}"])
    
    new_items = set()
    
    for line in output.splitlines():
        if not line:
            continue
        parts = line.split(maxsplit=1)
        status = parts[0]
        path = parts[1]
        
        # Ci interessano i file aggiunti (A) o anche rinominati (R) che appaiono come nuovi percorsi
        # Ma per semplificare, guardiamo tutto ciò che è nel diff e controlliamo se esiste in locale.
        
        top_level = path.split('/')[0]
        top_level = path.split('\\')[0] # Gestione separatori windows se git li restituisce così (di solito git usa /)
        
        if '/' in path:
             top_level = path.split('/')[0]
        
        new_items.add(top_level)
        
    return sorted(list(new_items))

def is_ignored(path):
    """Controlla se un percorso è ignorato da git."""
    try:
        # git check-ignore esce con 0 se ignorato, 1 se non ignorato
        subprocess.run(
            ["git", "check-ignore", "-q", "--", path],
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    parser = argparse.ArgumentParser(description="Controlla nuovi file/cartelle in arrivo da un remote.")
    parser.add_argument("remote_branch", nargs="?", default="asernet/main", help="Branch remoto da controllare (default: asernet/main)")
    args = parser.parse_args()

    print(f"--- Controllo arrivi da {args.remote_branch} ---")
    
    # 1. Fetch
    print("Eseguendo git fetch...")
    run_git_command(["git", "fetch", args.remote_branch.split('/')[0]])
    
    # 2. Get differences
    incoming_candidates = get_incoming_changes(args.remote_branch)
    
    if not incoming_candidates:
        print("Nessuna differenza rilevata tra HEAD e il remote (a livello di struttura).")
        return

    print(f"\nTrovati {len(incoming_candidates)} elementi top-level coinvolti nelle modifiche.")
    print("Analisi dello stato locale...\n")

    new_not_ignored = []
    
    for item in incoming_candidates:
        if os.path.exists(item):
            # Esiste già in locale, quindi è un aggiornamento di qualcosa che abbiamo accettato
            continue
            
        # Non esiste in locale. È ignorato?
        if is_ignored(item):
            print(f"[IGNORATO] {item}")
        else:
            new_not_ignored.append(item)
            print(f"[NUOVO]    {item}")

    print("\n" + "="*40)
    if new_not_ignored:
        print(f"ATTENZIONE: Ci sono {len(new_not_ignored)} nuovi elementi NON ignorati.")
        print("Se procedi con il merge, questi verranno scaricati.")
        print("Per escluderli, aggiungili al .gitignore prima del merge.")
        print("Lista da aggiungere al .gitignore se indesiderati:")
        for item in new_not_ignored:
            print(f"{item}/")
    else:
        print("Tutti i nuovi elementi rilevati sono già ignorati o esistono già in locale.")
        print("È sicuro procedere con il merge secondo le tue regole di esclusione.")

if __name__ == "__main__":
    main()
