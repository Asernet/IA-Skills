import sys
import json
from bs4 import BeautifulSoup
import os

def analyze_images(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
    except Exception as e:
        return {"error": str(e)}

    soup = BeautifulSoup(html, 'html.parser')
    images = soup.find_all('img')
    
    img_data = []
    missing_alt = 0
    missing_dimensions = 0
    no_lazy = 0
    non_modern_format = 0
    
    modern_formats = ['.webp', '.avif', '.svg']
    
    for i, img in enumerate(images):
        src = img.get('src', '')
        alt = img.get('alt', '')
        width = img.get('width')
        height = img.get('height')
        loading = img.get('loading')
        srcset = img.get('srcset')
        fetchpriority = img.get('fetchpriority')
        
        # Check Alt
        has_alt = bool(alt and alt.strip())
        if not has_alt:
            missing_alt += 1
            
        # Check Dimensions
        has_dim = bool(width and height)
        if not has_dim:
            missing_dimensions += 1
            
        # Check Lazy
        is_lazy = loading == 'lazy'
        if not is_lazy and i > 5: # Assuming first 5 might be above-the-fold
            no_lazy += 1
            
        # Check Format
        ext = os.path.splitext(src.split('?')[0])[1].lower()
        is_modern = any(ext == f for f in modern_formats)
        if not is_modern:
            non_modern_format += 1
            
        img_data.append({
            "index": i,
            "src": src,
            "alt": alt,
            "has_alt": has_alt,
            "width": width,
            "height": height,
            "has_dimensions": has_dim,
            "loading": loading,
            "is_lazy": is_lazy,
            "format": ext,
            "is_modern": is_modern,
            "srcset": bool(srcset),
            "fetchpriority": fetchpriority
        })

    return {
        "summary": {
            "total_images": len(images),
            "missing_alt": missing_alt,
            "missing_dimensions": missing_dimensions,
            "no_lazy_below_fold": no_lazy,
            "non_modern_formats": non_modern_format
        },
        "details": img_data
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_images(sys.argv[1])
        output_path = r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\images_analysis.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print(f"Image Analysis Done. Results saved to {output_path}")
