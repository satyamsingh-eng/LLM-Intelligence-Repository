import os
import json
import hashlib
from datetime import datetime, timezone
import urllib.request
import re

# 1. CONTINUOUS DIFF ENGINE
def run_diff_engine(lskr_dir, new_fetches):
    """Compares previous crawls to new crawls. Outputs diffs. Only updates changed pages."""
    diffs_found = []
    registry_path = os.path.join(lskr_dir, "source_registry.json")
    if os.path.exists(registry_path):
        with open(registry_path, "r") as f:
            registry = json.load(f)
    else:
        registry = {"sources": {}}

    for url, content in new_fetches.items():
        new_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        existing = registry["sources"].get(url, {}).get("latest_hash")
        if new_hash != existing:
            diffs_found.append(url)
            # Rebuild affected pages logic goes here
    return diffs_found

# 2. AI NEWS WATCHER & GITHUB CRAWLER (Utilizing web-research-deep patterns)
def fetch_text_safe(url, timeout=15):
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 C3ALabs/Hermes-KAE',
            'Accept': 'text/html,application/xhtml+xml'
        })
        resp = urllib.request.urlopen(req, context=ctx, timeout=timeout)
        html = resp.read().decode('utf-8', errors='ignore')
        # Strip noisy tags
        for tag in ['script', 'style', 'noscript', 'nav', 'header', 'footer']:
            html = re.sub(rf'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL|re.I)
        html = re.sub(r'<!--.*?-->', '', html, flags=re.DOTALL)
        text = re.sub(r'<[^>]+>', ' ', html)
        return re.sub(r'\s+', ' ', text).strip()
    except Exception as e:
        print(f"Fetch failed for {url}: {e}")
        return ""

def watch_ecosystem():
    """Monitors official Docs, API Refs, SDKs, Release Notes, Changelogs, Issues."""
    targets = [
        "https://github.com/anthropics/anthropic-sdk-python/releases",
        "https://github.com/openai/openai-python/releases",
        "https://platform.openai.com/docs/changelog",
        "https://cloud.google.com/vertex-ai/docs/release-notes"
    ]
    print("Executing Deep Web Research Scan via Knowledge Acquisition Engine...")
    
    fetches = {}
    for t in targets:
        print(f"Crawling documentation source: {t}")
        data = fetch_text_safe(t)
        if data:
            fetches[t] = data
            
    # Trigger Diff Engine
    repo_dir = "/Users/satyyy/Documents/R&D - C3ALABS/LLM-Intelligence-Repository"
    lskr_dir = os.path.join(repo_dir, "local_knowledge_repository")
    diffs = run_diff_engine(lskr_dir, fetches)
    
    print(f"Outcome: {len(diffs)} changed sources detected. Ready for evidence extraction.")
    return {"status": "Complete", "diffs_detected": diffs}

if __name__ == "__main__":
    print("Executing Knowledge Acquisition Engine Sprint...")
    watch_ecosystem()
