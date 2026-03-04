import sys
import json
from bs4 import BeautifulSoup

def analyze_schema(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Rileva JSON-LD
    json_ld_blocks = []
    scripts = soup.find_all('script', type='application/ld+json')
    for s in scripts:
        try:
            content = json.loads(s.string)
            json_ld_blocks.append(content)
        except:
            json_ld_blocks.append({"error": "Invalid JSON-LD syntax"})

    # 2. Rileva Microdata (basic check)
    has_microdata = len(soup.find_all(attrs={"itemscope": True})) > 0

    # 3. Validazione di base
    validation_results = []
    deprecated_types = ["HowTo", "SpecialAnnouncement", "CourseInfo", "EstimatedSalary", "LearningVideo"]
    
    for idx, block in enumerate(json_ld_blocks):
        if "error" in block:
            validation_results.append({f"Block {idx+1}": "Error: Invalid Syntax"})
            continue
            
        res = {"block": idx+1, "type": block.get("@type"), "issues": []}
        
        # Check context
        context = block.get("@context", "")
        if context != "https://schema.org":
            res["issues"].append(f"Context is '{context}', should be 'https://schema.org'")
            
        # Check deprecated
        if block.get("@type") in deprecated_types:
            res["issues"].append(f"Type '{block.get('@type')}' is deprecated")
            
        # Check for Graph
        if "@graph" in block:
            res["type"] = "Graph"
            for item in block["@graph"]:
                if item.get("@type") in deprecated_types:
                    res["issues"].append(f"Graph item '{item.get('@type')}' is deprecated")

        validation_results.append(res)

    return {
        "json_ld_count": len(json_ld_blocks),
        "has_microdata": has_microdata,
        "validation": validation_results,
        "raw_blocks": json_ld_blocks
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_schema(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\schema_analysis.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"Analisi schema completata. Rilevati {res['json_ld_count']} blocchi JSON-LD.")
