import os
import sys
from urllib.parse import urlparse

def get_workspace():
    # Definiamo la SEO Station sul Desktop
    base = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'SEO_WORKSPACE')
    if not os.path.exists(base):
        os.makedirs(base)
    return base

def save_file(domain, subfolder, filename, content):
    base = get_workspace()
    target_dir = os.path.join(base, subfolder, domain)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    file_path = os.path.join(target_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return file_path

if __name__ == "__main__":
    # Usage: python generate_report.py <url> <subfolder> <filename> <content_file_path>
    # Per evitare troncamenti CLI, leggiamo il contenuto da un file temporaneo
    if len(sys.argv) > 4:
        url = sys.argv[1]
        subfolder = sys.argv[2]
        filename = sys.argv[3]
        content_path = sys.argv[4]
        
        domain = urlparse(url).netloc.replace('www.', '').replace('.', '_')
        with open(content_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        path = save_file(domain, subfolder, filename, content)
        print(f"SALVATO: {path}")
