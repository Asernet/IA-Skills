import sys
import json
import re
from bs4 import BeautifulSoup

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouyàèéìòù"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def flesch_reading_ease_it(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    words = re.findall(r'\b\w+\b', text)
    if not words or not sentences:
         return 0
    syllables = sum(count_syllables(w) for w in words)
    words_count = len(words)
    sentences_count = len(sentences)
    
    # Formula adattata per l'italiano (Franchina o simili) o approssimazione standard
    fre = 206.835 - (1.015 * (words_count / sentences_count)) - (84.6 * (syllables / words_count))
    return fre

def analyze_task_content(filepath):
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
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    
    fre_score = flesch_reading_ease_it(text)
    
    # Gerarchia
    h1 = len(soup.find_all('h1'))
    h2 = len(soup.find_all('h2'))
    h3 = len(soup.find_all('h3'))
    
    # Multimedia
    images = soup.find_all('img')
    images_with_alt = [img for img in images if img.get('alt')]
    
    # Links
    links = soup.find_all('a')
    internal_links = [l for l in links if l.get('href') and ('asernet.it' in l.get('href') or l.get('href').startswith('/'))]
    external_links = [l for l in links if l.get('href') and l.get('href').startswith('http') and 'asernet.it' not in l.get('href')]
    
    # Liste e Tabelle
    lists = len(soup.find_all(['ul', 'ol']))
    tables = len(soup.find_all('table'))

    out = {
        "metrics": {
            "word_count": word_count,
            "flesch_reading_ease": round(fre_score, 2),
            "h1_count": h1,
            "h2_count": h2,
            "h3_count": h3,
            "total_images": len(images),
            "images_with_alt": len(images_with_alt),
            "internal_links": len(internal_links),
            "external_links": len(external_links),
            "lists_count": lists,
            "tables_count": tables
        }
    }
    return out

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_task_content(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\task_content_analysis.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print("Done.")
