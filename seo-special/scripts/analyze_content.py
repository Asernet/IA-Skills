import sys
import json
from bs4 import BeautifulSoup
import re

def analyze_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html, 'html.parser')
    
    # Rimuovi script e style
    for script in soup(["script", "style", "noscript"]):
        script.extract()
        
    text = soup.get_text(separator=' ')
    words = [w for w in text.split() if w.strip()]
    word_count = len(words)
    
    # E-E-A-T Checks Heuristics
    experience_signals = len(soup.find_all(string=re.compile(r'case study|casi studio|portfolio|risultati|abbiamo aiutato', re.I)))
    expertise_signals = len(soup.find_all(string=re.compile(r'certificati|partner|team|specialisti|anni di esperienza', re.I)))
    authoritativeness_signals = len(soup.find_all(string=re.compile(r'dicono di noi|recensioni|premio|riconoscimento', re.I)))
    trustworthiness_signals = len(soup.find_all(string=re.compile(r'privacy|termini|contattaci|sede legale|p\.iva', re.I)))
    
    # AI Citation predisposition
    has_stats = len(re.findall(r'\b\d+%|\b\d+ mln|\b\d+ mila', text)) > 0
    has_clear_hierarchy = len(soup.find_all(['h1', 'h2', 'h3'])) > 5
    has_lists = len(soup.find_all(['ul', 'ol'])) > 0
    
    ai_score = 0
    if has_stats: ai_score += 30
    if has_clear_hierarchy: ai_score += 40
    if has_lists: ai_score += 30
    
    # E-E-A-T Score
    eeat_score = min(100, (experience_signals*5) + (expertise_signals*5) + (authoritativeness_signals*5) + (trustworthiness_signals*10))
    if eeat_score == 0: eeat_score = 45 # baseline for agency
    
    # Content Quality
    quality_score = 100
    if word_count < 500: quality_score -= 30
    elif word_count < 800: quality_score -= 10
    
    out = {
        "word_count": word_count,
        "quality_score": min(100, max(0, quality_score)),
        "eeat": {
            "score": eeat_score,
            "experience": "Alta" if experience_signals > 2 else "Media",
            "expertise": "Alta" if expertise_signals > 2 else "Media",
            "authoritativeness": "Media" if authoritativeness_signals > 0 else "Bassa",
            "trustworthiness": "Alta" if trustworthiness_signals > 2 else "Media"
        },
        "ai_citation_score": ai_score,
        "recommendations": []
    }
    
    if word_count < 800:
        out["recommendations"].append("Aumentare il word count della homepage per coprire meglio le entità semantiche.")
    if authoritativeness_signals == 0:
        out["recommendations"].append("Aggiungere sezioni 'Dicono di noi' o recensioni per aumentare il fattore Authoritativeness.")
    if not has_stats:
        out["recommendations"].append("Inserire dati statistici o percentuali di crescita per favorire l'estrazione da parte di chatbot AI (GEO).")
        
    return out

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_content(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\content_analysis.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"Analisi completata. {res.get('word_count', 0)} parole.")
