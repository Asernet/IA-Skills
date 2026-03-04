import sys
import xml.etree.ElementTree as ET
import requests
from urllib.parse import urlparse
import json

def analyze_sitemap(url):
    print(f"Fetch {url}...")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()
        content = r.text
    except Exception as e:
        return {"error": str(e), "url": url}
    
    root = ET.fromstring(content)
    # Strip namespaces for easier search
    for elem in root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]
            
    if root.tag == "sitemapindex":
        sitemaps = [elem.text for elem in root.iter("loc")]
        print(f"Trovato Index con {len(sitemaps)} sitemaps.")
        all_results = []
        for s in sitemaps:
            res = analyze_sitemap(s) # recursive call doesn't return list here. Let's do a fast implementation
            if "urls" in res:
                all_results.append(res)
        
        # aggregate
        total_urls = 0
        deprecations = 0
        bad_urls = 0
        location_pages = 0
        urls_list = []
        for r in all_results:
            total_urls += r.get("total_urls", 0)
            deprecations += r.get("deprecations", 0)
            bad_urls += r.get("bad_urls", 0)
            location_pages += r.get("location_pages", 0)
            urls_list.extend(r.get("urls", []))
            
        return {
            "type": "index",
            "url": url,
            "total_sitemaps": len(sitemaps),
            "total_urls": total_urls,
            "deprecations": deprecations,
            "bad_urls": bad_urls,
            "location_pages": location_pages,
            "passed_limit_gate": total_urls <= 50000,
            "passed_quality_gate": location_pages < 30
        }
    elif root.tag == "urlset":
        urls = [elem.text for elem in root.iter("loc") if elem.text]
        deprecations = 0
        location_pages = 0
        
        for elem in root.iter():
            if elem.tag in ["priority", "changefreq"]:
                deprecations += 1
                
        # fast check 10 urls only to prevent rate limits for the test
        sample = urls[:5]
        bad_urls = 0
        for u in sample:
            try:
                res = requests.head(u, headers=headers, timeout=5, allow_redirects=False)
                if res.status_code != 200:
                    bad_urls += 1
            except:
                bad_urls += 1
                
            if "milano" in u.lower() or "roma" in u.lower() or "torino" in u.lower() or "citta" in u.lower() or "agenzia-seo-" in u.lower():
                location_pages += 1
                
        print(f"Sitemap {url}: {len(urls)} URLs. {deprecations} tag deprecati.")
                
        return {
            "type": "sitemap",
            "url": url,
            "total_urls": len(urls),
            "deprecations": deprecations,
            "bad_urls_in_sample": bad_urls,
            "location_pages": location_pages,
            "urls": urls
        }
    else:
        return {"error": "Invalid XML format."}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        out = analyze_sitemap(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\sitemap_analysis.json", "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        print("Done.")
