#!/usr/bin/env python3
"""
Check mobile parity (Desktop vs Mobile) using Playwright.

Usage:
    python analyze_mobile_parity.py https://example.com
"""

import argparse
import json
import sys
from urllib.parse import urlparse

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("Error: playwright required.")
    sys.exit(1)

def get_page_data(p, browser_instance, url, is_mobile):
    viewport = {"width": 375, "height": 812} if is_mobile else {"width": 1920, "height": 1080}
    user_agent = (
        "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        if is_mobile else
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    )
    
    context = browser_instance.new_context(viewport=viewport, user_agent=user_agent)
    page = context.new_page()
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(3000)
    except Exception as e:
        context.close()
        return {"error": str(e)}

    title = page.title()
    description = page.evaluate("() => { const meta = document.querySelector('meta[name=\"description\"]'); return meta ? meta.content : null; }")
    robots = page.evaluate("() => { const meta = document.querySelector('meta[name=\"robots\"]'); return meta ? meta.content : null; }")
    
    schemas = page.evaluate("""() => {
        const scripts = document.querySelectorAll('script[type="application/ld+json"]');
        return Array.from(scripts).map(s => s.textContent);
    }""")
    
    word_count = page.evaluate("() => document.body.innerText.split(/\\s+/).length")
    
    context.close()
    
    return {
        "title": title,
        "description": description,
        "robots": robots,
        "schema_count": len(schemas),
        "word_count": word_count
    }

def analyze_parity(url):
    result = {"url": url, "desktop": {}, "mobile": {}, "parity": {}}
    try:
        with sync_playwright() as p:
            browser_instance = p.chromium.launch(headless=True)
            
            desktop_data = get_page_data(p, browser_instance, url, False)
            mobile_data = get_page_data(p, browser_instance, url, True)
            
            browser_instance.close()
            
            if "error" in desktop_data:
                return {"error": f"Desktop fetch error: {desktop_data['error']}"}
            if "error" in mobile_data:
                return {"error": f"Mobile fetch error: {mobile_data['error']}"}
                
            result["desktop"] = desktop_data
            result["mobile"] = mobile_data
            
            result["parity"]["title_match"] = desktop_data["title"] == mobile_data["title"]
            result["parity"]["description_match"] = desktop_data["description"] == mobile_data["description"]
            result["parity"]["robots_match"] = desktop_data["robots"] == mobile_data["robots"]
            result["parity"]["schema_match"] = desktop_data["schema_count"] == mobile_data["schema_count"]
            
            # Word count within 10%
            diff = abs(desktop_data["word_count"] - mobile_data["word_count"])
            avg = (desktop_data["word_count"] + mobile_data["word_count"]) / 2
            result["parity"]["content_parity_ok"] = diff / max(avg, 1) < 0.1
            
            return result
    except Exception as e:
        return {"error": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Check mobile parity (Desktop vs Mobile)")
    parser.add_argument("url", help="URL to analyze")
    args = parser.parse_args()
    
    res = analyze_parity(args.url)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
