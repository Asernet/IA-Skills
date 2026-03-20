import sys
import re
from bs4 import BeautifulSoup

def detect_fake_freshness(html_content):
    """
    Analizza i segnali di freschezza del contenuto confrontando metadati e corpo del testo.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. Estrai date dai metadati (JSON-LD, Meta tags)
    dates = {
        'published': None,
        'modified': None
    }
    
    # Esempio: JSON-LD Article
    import json
    scripts = soup.find_all('script', type='application/ld+json')
    for script in scripts:
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                dates['published'] = data.get('datePublished') or dates['published']
                dates['modified'] = data.get('dateModified') or dates['modified']
            elif isinstance(data, list):
                for item in data:
                    dates['published'] = item.get('datePublished') or dates['published']
                    dates['modified'] = item.get('dateModified') or dates['modified']
        except:
            continue
            
    # 2. Analizza segnali di freschezza nel testo (es. "Ultimo aggiornamento: ...")
    text_signals = soup.find_all(string=re.compile(r'(?i)(ultimo aggiornamento|aggiornato il|last updated|updated on)'))
    
    # 3. Analisi di discrepanza (Placeholder per logica avanzata di confronto hash del corpo testo)
    # In una versione reale, servirebbe confrontare il corpo attuale con una versione passata (Wayback o cache)
    
    return {
        'meta_dates': dates,
        'text_signals_found': len(text_signals) > 0,
        'recommendation': "Verifica se il contenuto è stato realmente aggiornato o solo la data."
    }

if __name__ == "__main__":
    # Leggi HTML da stdin o file
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            print(json.dumps(detect_fake_freshness(f.read()), indent=2))
