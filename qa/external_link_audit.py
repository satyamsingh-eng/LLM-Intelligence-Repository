from pathlib import Path
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import re,json,requests,sys
ROOT=Path(__file__).resolve().parents[1]
html=(ROOT/'index.html').read_text()
runtime=json.loads((ROOT/'models/executive_report_runtime.json').read_text())
urls=set(re.findall(r'href=["\'](https?://[^"\']+)',html))
urls.update(p['source_url'] for p in runtime['pricing_catalog'] if (p.get('source_url') or '').startswith('http'))
for m in runtime['models']:
 for k in ('sourceUrl','pricingSourceUrl'):
  if (m.get(k) or '').startswith('http'): urls.add(m[k])
for r in runtime['routing']['roles']:
 for k in ('sourceUrl','benchmarkUrl'):
  if (r.get(k) or '').startswith('http'): urls.add(r[k])
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 SARVAX-Link-Validator/1.0'}
def fetch(url):
 try:
  r=requests.get(url,headers=headers,timeout=35,allow_redirects=True,stream=True)
  status=r.status_code;kind='reachable' if 200<=status<400 else 'access-controlled' if status in (401,403,429) else 'hard-fail'
  return {'url':url,'status':status,'final_url':r.url,'kind':kind,'content_type':r.headers.get('content-type')}
 except Exception as e:return {'url':url,'status':None,'final_url':None,'kind':'network-error','error':f'{type(e).__name__}: {e}'}
rows=[]
with ThreadPoolExecutor(max_workers=10) as ex:
 futs={ex.submit(fetch,u):u for u in sorted(urls)}
 for f in as_completed(futs): rows.append(f.result())
rows.sort(key=lambda x:x['url'])
hard=[r for r in rows if r['kind'] in ('hard-fail','network-error')]
out={'total':len(rows),'reachable':sum(r['kind']=='reachable' for r in rows),'access_controlled':sum(r['kind']=='access-controlled' for r in rows),'hard_failures':len(hard),'rows':rows}
(ROOT/'qa'/'external_link_audit.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
print(json.dumps({'total':out['total'],'reachable':out['reachable'],'access_controlled':out['access_controlled'],'hard_failures':hard},indent=2,ensure_ascii=False))
sys.exit(1 if hard else 0)
