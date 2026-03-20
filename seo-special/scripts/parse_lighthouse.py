import json
import os

def extract_lighthouse_metrics(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    performance_score = data.get('categories', {}).get('performance', {}).get('score', 0) * 100
    audits = data.get('audits', {})
    
    metrics = {
        "Performance Score": round(performance_score),
        "LCP": audits.get('largest-contentful-paint', {}).get('displayValue'),
        "CLS": audits.get('cumulative-layout-shift', {}).get('displayValue'),
        "TBT": audits.get('total-blocking-time', {}).get('displayValue'),
        "FCP": audits.get('first-contentful-paint', {}).get('displayValue'),
        "Speed Index": audits.get('speed-index', {}).get('displayValue'),
    }
    
    opportunities = []
    for audit_id, audit in audits.items():
        if audit.get('details', {}).get('type') == 'opportunity' and audit.get('score', 1) < 0.9:
            opportunities.append({
                "title": audit.get('title'),
                "description": audit.get('description'),
                "savings": audit.get('displayValue')
            })
            
    return {"metrics": metrics, "opportunities": opportunities}

if __name__ == "__main__":
    report_path = r'C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\lighthouse.json'
    if os.path.exists(report_path):
        results = extract_lighthouse_metrics(report_path)
        with open(r'C:\Users\M.Macelloni\Desktop\SEO_WORKSPACE\report\asernet.it\lighthouse_summary.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print("Metriche estratte con successo.")
    else:
        print("File lighthouse.json non trovato.")
