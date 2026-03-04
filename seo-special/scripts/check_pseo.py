import requests
from bs4 import BeautifulSoup
import json

urls = [
    "https://www.asernet.it/neuros_case_study_tag/casalinghi/",
    "https://www.asernet.it/neuros_case_study_tag/sanitaria/",
    "https://www.asernet.it/categoria/ecommerce-marketing-tips/"
]

results = []

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Count words in the main content area (excluding nav/footer if possible)
        # Using a broad approach for simplicity in this script
        text = soup.get_text()
        word_count = len(text.split())
        
        # Check for specific headings or unique text blocks
        h1 = soup.find('h1').get_text(strip=True) if soup.find('h1') else "N/A"
        
        # Check number of links (items in the directory)
        articles = soup.find_all('article')
        items_count = len(articles)
        
        results.append({
            "url": url,
            "h1": h1,
            "word_count": word_count,
            "items_count": items_count,
            "status_code": r.status_code
        })
    except Exception as e:
        results.append({"url": url, "error": str(e)})

print(json.dumps(results, indent=2))
