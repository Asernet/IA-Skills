import sys
import json
from bs4 import BeautifulSoup

def analyze_technical(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Meta Tags
    title = soup.title.string if soup.title else "N/A"
    meta_desc = soup.find('meta', attrs={"name": "description"})
    desc = meta_desc['content'] if meta_desc else "N/A"
    meta_robots = soup.find('meta', attrs={"name": "robots"})
    robots_val = meta_robots['content'] if meta_robots else "index, follow" # Default

    # 2. Canonical
    canonical_tag = soup.find('link', rel='canonical')
    canonical = canonical_tag['href'] if canonical_tag else "N/A"

    # 3. Viewport (Mobile)
    viewport_tag = soup.find('meta', attrs={"name": "viewport"})
    viewport = viewport_tag['content'] if viewport_tag else "N/A"

    # 4. Hreflang
    hreflangs = [{"lang": l.get("hreflang"), "href": l.get("href")} for l in soup.find_all("link", rel="alternate") if l.get("hreflang")]

    # 5. Charset
    charset_tag = soup.find('meta', charset=True)
    charset = charset_tag['charset'] if charset_tag else "N/A"

    return {
        "title": title,
        "description": desc,
        "robots": robots_val,
        "canonical": canonical,
        "viewport": viewport,
        "hreflangs": hreflangs,
        "charset": charset,
        "ssr_detected": len(soup.find_all(recursive=False)) > 0 # Simple check
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_technical(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\technical_analysis.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print("Analisi tecnica completata.")
