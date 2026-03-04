import sys
import json
import re
from bs4 import BeautifulSoup

def analyze_geo(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html, 'html.parser')
    
    # Rimuovi script e style
    for script in soup(["script", "style", "noscript"]):
        script.extract()
        
    paragraphs = [p.get_text().strip() for p in soup.find_all('p') if len(p.get_text().strip()) > 50]
    
    paragraph_stats = []
    optimal_count = 0
    for p in paragraphs:
        word_count = len(p.split())
        is_optimal = 134 <= word_count <= 167
        if is_optimal:
            optimal_count += 1
        paragraph_stats.append({
            "text_preview": p[:50] + "...",
            "word_count": word_count,
            "is_optimal_geo": is_optimal
        })

    # Verifica definizioni (Cos'è / refers to)
    content_text = soup.get_text().lower()
    has_definitions = bool(re.search(r"(è|si riferisce a|significa|consiste in)\b", content_text))
    
    # Menzioni Brand e Entità (Euristiche)
    brand_mentions = len(re.findall(r"asernet", content_text))
    
    # Punteggi euristici
    geo_readiness = 0
    if optimal_count > 0: geo_readiness += 30
    if has_definitions: geo_readiness += 20
    if brand_mentions > 5: geo_readiness += 20
    # Altri punti per la struttura (H1-H3 già analizzati in task-content, qui consideriamo la presenza)
    if soup.find_all(['h1', 'h2', 'h3']): geo_readiness += 30

    return {
        "geo_readiness_score": geo_readiness,
        "paragraph_analysis": {
            "total_extracted": len(paragraphs),
            "optimal_geo_count": optimal_count,
            "details": paragraph_stats[:10]
        },
        "signals": {
            "has_definitions": has_definitions,
            "brand_mentions": brand_mentions,
            "ssr_confirmed": True # Già verificato in technical
        }
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_geo(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\geo_data.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print("GEO Analysis Done.")
