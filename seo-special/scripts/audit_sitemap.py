import requests
import xml.etree.ElementTree as ET
import sys
import json

def validate_sitemap(url):
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        content = response.text
    except Exception as e:
        return {"error": str(e)}

    # Check for deprecated tags in raw text
    has_priority = "<priority>" in content
    has_changefreq = "<changefreq>" in content

    try:
        root = ET.fromstring(content)
    except Exception as e:
        return {"error": f"Invalid XML: {str(e)}"}

    urls = []
    # Namespaces are common in sitemaps
    ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    for url_tag in root.findall('s:url', ns):
        loc = url_tag.find('s:loc', ns)
        if loc is not None:
            urls.append(loc.text)

    # Simple location pattern detection
    location_keywords = ["agenzia-foggia", "ecommerce-milano", "marketing-roma", "sede-", "ufficio-"]
    location_pages = [u for u in urls if any(k in u.lower() for k in location_keywords)]

    return {
        "url": url,
        "total_urls": len(urls),
        "has_priority": has_priority,
        "has_changefreq": has_changefreq,
        "location_pages_count": len(location_pages),
        "location_pages_sample": location_pages[:5],
        "status_check_sample": urls[:3]
    }

if __name__ == "__main__":
    target = "https://www.asernet.it/page-sitemap.xml"
    res = validate_sitemap(target)
    with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\sitemap_audit.json", "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)
    print("Sitemap Audit Done.")
