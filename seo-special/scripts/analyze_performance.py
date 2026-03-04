import sys
import json
import requests
import time

def analyze_performance(url):
    print(f"Analisi Performance per {url} (Mobile by default)...")
    # Usa l'API pubblica di Google PageSpeed Insights
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile"
    try:
        response = requests.get(api_url, timeout=60)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        return {"error": str(e), "url": url}

    lighthouse = data.get("lighthouseResult", {})
    categories = lighthouse.get("categories", {})
    performance_score = categories.get("performance", {}).get("score", 0) * 100

    audits = lighthouse.get("audits", {})
    
    lcp_val = audits.get("largest-contentful-paint", {}).get("displayValue", "N/A")
    lcp_score = audits.get("largest-contentful-paint", {}).get("score", 0)
    
    cls_val = audits.get("cumulative-layout-shift", {}).get("displayValue", "N/A")
    cls_score = audits.get("cumulative-layout-shift", {}).get("score", 0)
    
    # INP / TBT as proxy if INP is not directly in standard audits
    tbt_val = audits.get("total-blocking-time", {}).get("displayValue", "N/A")
    tbt_score = audits.get("total-blocking-time", {}).get("score", 0)
    
    # Check loading metric data from CrUX
    loading_experience = data.get("loadingExperience", {}).get("metrics", {})
    field_lcp = loading_experience.get("LARGEST_CONTENTFUL_PAINT_MS", {}).get("percentile", "N/A")
    field_inp = loading_experience.get("INTERACTION_TO_NEXT_PAINT", {}).get("percentile", "N/A")
    field_cls = loading_experience.get("CUMULATIVE_LAYOUT_SHIFT_SCORE", {}).get("percentile", "N/A")

    bottlenecks = []
    
    # Collect opportunities
    for audit_id, audit in audits.items():
        if audit.get("details", {}).get("type") == "opportunity" and audit.get("score", 1) < 0.9:
            bottlenecks.append({
                "title": audit.get("title"),
                "savings": audit.get("displayValue")
            })
            
    # Also collect diagnostics with low scores
    diagnostics = ["mainthread-work-breakdown", "bootup-time", "dom-size", "server-response-time", "render-blocking-resources"]
    for diag_id in diagnostics:
        audit = audits.get(diag_id, {})
        if audit.get("score", 1) < 0.8:
            bottlenecks.append({
                "title": audit.get("title"),
                "savings": audit.get("displayValue", "")
            })

    return {
        "url": url,
        "performance_score": round(performance_score),
        "lab_data": {
            "LCP": lcp_val,
            "LCP_score": lcp_score,
            "CLS": cls_val,
            "CLS_score": cls_score,
            "TBT": tbt_val,
            "TBT_score": tbt_score
        },
        "field_data": {
            "LCP_ms": field_lcp,
            "INP_ms": field_inp,
            "CLS_score": field_cls
        },
        "bottlenecks": bottlenecks
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        res = analyze_performance(sys.argv[1])
        with open(r"C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\performance_analysis.json", "w", encoding="utf-8") as f:
            json.dump(res, f, indent=2)
        print("Done.")
