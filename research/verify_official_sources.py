from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os, re, sys, time
import requests

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'local_knowledge_repository'/'official_sources'
OUT.mkdir(parents=True,exist_ok=True)
MODELS=json.loads((ROOT/'models'/'verified_models_database.json').read_text())['models']
NOW=datetime.now(timezone.utc).replace(microsecond=0).isoformat()
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 SARVAX-Evidence-Validator/1.0'

SOURCES={
 'eu_ai_act':('EU Publications Office','https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng'),
 'eu_ai_act_article_15':('European Commission AI Act Service Desk','https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15'),
 'eu_ai_act_annex_3':('European Commission AI Act Service Desk','https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3'),
 'eu_ai_act_commission':('European Commission','https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai'),
 'soc2_aicpa':('AICPA & CIMA','https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2'),
 'hipaa_baa_hhs':('US HHS','https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html'),
 'fedramp_marketplace':('FedRAMP','https://marketplace.fedramp.gov/products'),
 'aws_govcloud':('AWS','https://aws.amazon.com/govcloud-us/'),
 'aws_bedrock_compliance':('AWS','https://aws.amazon.com/bedrock/security-compliance/'),
 'aws_bedrock_pricing':('AWS','https://aws.amazon.com/bedrock/pricing/'),
 'aws_bedrock_models':('AWS','https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html'),
 'anthropic_models':('Anthropic','https://docs.anthropic.com/en/docs/about-claude/models/overview'),
 'anthropic_pricing':('Anthropic','https://docs.anthropic.com/en/docs/about-claude/pricing'),
 'openai_models':('OpenAI','https://platform.openai.com/docs/models'),
 'openai_pricing':('OpenAI','https://openai.com/api/pricing/'),
 'google_models':('Google','https://ai.google.dev/gemini-api/docs/models'),
 'google_pricing':('Google Cloud','https://cloud.google.com/vertex-ai/generative-ai/pricing'),
 'deepseek_models_pricing':('DeepSeek','https://api-docs.deepseek.com/quick_start/pricing/'),
 'moonshot_models':('Moonshot AI','https://platform.moonshot.ai/docs/guide/start-using-kimi-api'),
 'moonshot_pricing':('Moonshot AI','https://platform.moonshot.ai/docs/pricing/chat'),
 'moonshot_k26_model':('Moonshot AI','https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart'),
 'moonshot_k26_pricing':('Moonshot AI','https://platform.kimi.ai/docs/pricing/chat-k26'),
 'xai_models':('xAI','https://docs.x.ai/docs/models'),
 'xai_pricing':('xAI','https://docs.x.ai/docs/models#models-and-pricing'),
 'zai_models':('Z.ai','https://docs.z.ai/guides/llm/glm-4.5'),
 'zai_pricing':('Z.ai','https://docs.z.ai/guides/overview/pricing'),
 'alibaba_models':('Alibaba Cloud','https://www.alibabacloud.com/help/en/model-studio/getting-started/models'),
 'alibaba_pricing':('Alibaba Cloud','https://www.alibabacloud.com/help/en/model-studio/model-pricing'),
 'meta_llama':('Meta','https://www.llama.com/models/'),
 'cohere_models':('Cohere','https://docs.cohere.com/docs/models'),
 'cohere_pricing':('Cohere','https://cohere.com/pricing'),
 'ecb_fx':('European Central Bank','https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'),
}
VENDOR_KEYS={
 'Anthropic':['anthropic_models','anthropic_pricing'], 'OpenAI':['openai_models','openai_pricing'],
 'Kimi':['moonshot_models','moonshot_pricing'], 'SpaceXAI':['xai_models','xai_pricing'],
 'Z AI':['zai_models','zai_pricing'], 'Meta':['meta_llama'], 'Google':['google_models','google_pricing'],
 'Alibaba':['alibaba_models','alibaba_pricing'], 'DeepSeek':['deepseek_models_pricing'], 'Cohere':['cohere_models','cohere_pricing'],
 'Amazon':['aws_bedrock_models','aws_bedrock_pricing']}
SPECIAL_MODEL_KEYS={
 'kimi-k2-6':['moonshot_k26_model','moonshot_k26_pricing'],
 'qwen3-7-plus':['alibaba_models','alibaba_pricing'],
 'gemini-3-5-flash-lite':['google_models','google_pricing']}

def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def visible_text(raw):
 s=re.sub(r'<script\b[^>]*>.*?</script>',' ',raw,flags=re.I|re.S)
 s=re.sub(r'<style\b[^>]*>.*?</style>',' ',s,flags=re.I|re.S)
 s=re.sub(r'<[^>]+>',' ',s)
 return re.sub(r'\s+',' ',s).lower()

def fetch(source_id,publisher,url,headers=None):
 rec={'id':source_id,'publisher':publisher,'requested_url':url,'retrieved_at':NOW}
 try:
  r=requests.get(url,headers={'User-Agent':UA,**(headers or {})},timeout=45,allow_redirects=True)
  body=r.content
  ext='.json' if 'json' in r.headers.get('content-type','').lower() else '.html'
  fp=OUT/(source_id+ext)
  usable=r.status_code==200 and len(body)>500
  if usable:
   fp.write_bytes(body)
  elif fp.exists() and fp.stat().st_size>500:
   body=fp.read_bytes()
   rec['status_note']=f'Current retrieval returned HTTP {r.status_code}; retained the last usable snapshot instead of overwriting evidence.'
   usable=True
  rec.update({'http_status':r.status_code,'final_url':r.url,'content_type':r.headers.get('content-type',''),'bytes':len(body),'sha256':hashlib.sha256(body).hexdigest(),'snapshot':str(fp.relative_to(ROOT)),'usable':usable})
  if ext=='.json':
   try: text=json.dumps(r.json(),ensure_ascii=False).lower()
   except Exception: text=body.decode('utf-8','ignore').lower()
  else: text=visible_text(body.decode('utf-8','ignore'))
  return rec,text
 except Exception as e:
  rec.update({'http_status':None,'error':f'{type(e).__name__}: {e}','usable':False})
  return rec,''

manifest=[];texts={}
for sid,(pub,url) in SOURCES.items():
 rec,text=fetch(sid,pub,url);manifest.append(rec);texts[sid]=text;time.sleep(.15)

# Artificial Analysis: prefer a fresh API response; fall back to the retained raw snapshot and mark freshness accordingly.
env_path=Path('/Users/satyyy/.hermes/profiles/professional/.env')
aa_key=os.environ.get('ARTIFICIAL_ANALYSIS_API_KEY','')
if not aa_key and env_path.exists():
 for line in env_path.read_text(errors='ignore').splitlines():
  if line.startswith('ARTIFICIAL_ANALYSIS_API_KEY='):
   aa_key=line.split('=',1)[1].strip().strip('"\'');break
aa_payload=None; aa_fresh=False
if aa_key:
 rec,text=fetch('artificial_analysis_models','Artificial Analysis','https://artificialanalysis.ai/api/v2/data/llms/models',{'x-api-key':aa_key})
 manifest.append(rec);texts['artificial_analysis_models']=text
 if rec.get('usable'):
  aa_payload=json.loads((ROOT/rec['snapshot']).read_text())
  aa_fresh=True
else:
 snap=ROOT/'models'/'artificial_analysis_live_dataset.json'
 if snap.exists():
  aa_payload=json.loads(snap.read_text())
  raw=snap.read_bytes()
  manifest.append({'id':'artificial_analysis_models','publisher':'Artificial Analysis','requested_url':'https://artificialanalysis.ai/api/v2/data/llms/models','retrieved_at':NOW,'usable':True,'fresh_api_retrieval':False,'status_note':'Retained API snapshot; current API refresh unavailable because the credential was not present.','http_status':aa_payload.get('status'),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'snapshot':str(snap.relative_to(ROOT))})
 else:
  manifest.append({'id':'artificial_analysis_models','publisher':'Artificial Analysis','requested_url':'https://artificialanalysis.ai/api/v2/data/llms/models','retrieved_at':NOW,'usable':False,'error':'API key and retained snapshot unavailable'})
 texts['artificial_analysis_models']=''

def compact(s): return re.sub(r'[^a-z0-9]+','',s.lower())
def official_term(name): return re.sub(r'\s*\([^)]*\)\s*$','',name).strip().lower()
def official_alias(m):
 term=official_term(m['name'])
 for prefix in ('cohere ','amazon '):
  if term.startswith(prefix): term=term[len(prefix):]
 return term

aa_rows=(aa_payload or {}).get('data',[])
aa_index={compact(x.get('name','')):x for x in aa_rows}
model_audit=[]
for m in MODELS:
 term=official_alias(m);needle=compact(term)
 keys=SPECIAL_MODEL_KEYS.get(m['id'],VENDOR_KEYS.get(m['vendor'],[]))
 pages=[k for k in keys if next((x for x in manifest if x['id']==k and x.get('usable')),None)]
 hits=[k for k in pages if needle and needle in compact(texts.get(k,''))]
 aa=aa_index.get(compact(m['name']))
 metric_map={
  'intelligence_index':('evaluations','artificial_analysis_intelligence_index'),
  'coding_index':('evaluations','artificial_analysis_coding_index'),
  'tau_banking_score':('evaluations','tau_banking'),
  'price_1m_input_usd':('pricing','price_1m_input_tokens'),
  'price_1m_output_usd':('pricing','price_1m_output_tokens'),
  'throughput_tps':(None,'median_output_tokens_per_second'),
  'ttft_latency_seconds':(None,'median_time_to_first_token_seconds')}
 metric_checks={}
 if aa:
  for db_key,(group,aa_key_name) in metric_map.items():
   dbv=m.get('metrics',{}).get(db_key,{}).get('value')
   aav=aa.get(group,{}).get(aa_key_name) if group else aa.get(aa_key_name)
   match=(dbv is None and aav is None) or (dbv is not None and aav is not None and abs(float(dbv)-float(aav))<=max(0.011,abs(float(aav))*0.005))
   metric_checks[db_key]={'database_value':dbv,'benchmark_value':aav,'match_with_rounding_tolerance':match}
 if hits and aa: proof='provider-family-documented-plus-benchmark-snapshot'
 elif hits: proof='provider-family-documented-only'
 elif aa: proof='benchmark-snapshot-only'
 else: proof='unverified'
 model_audit.append({'id':m['id'],'name':m['name'],'vendor':m['vendor'],'official_search_term':term,'proof_status':proof,'official_source_ids':keys,'official_hits':hits,'benchmark_snapshot_exact_name_match':bool(aa),'benchmark_snapshot_fresh_api_retrieval':aa_fresh,'metric_checks':metric_checks,'decision_use':'eligible-with-metric-scope-shown' if hits and aa else 'quarantine','note':'Provider proof establishes the model family. Effort labels are benchmark/test variants unless the provider documents them as separate SKUs. Benchmark evidence is a retained snapshot when fresh API retrieval is unavailable.'})

# Derive the current ECB cross-rate exactly from official daily EUR reference rates.
from decimal import Decimal
fx=None
fx_path=OUT/'ecb_fx.html'
if fx_path.exists():
 xml=fx_path.read_text(errors='ignore')
 mu=re.search(r"currency=['\"]USD['\"]\s+rate=['\"]([0-9.]+)",xml)
 mi=re.search(r"currency=['\"]INR['\"]\s+rate=['\"]([0-9.]+)",xml)
 md=re.search(r"time=['\"]([0-9-]+)",xml)
 if mu and mi: fx={'usd_to_inr':str(Decimal(mi.group(1))/Decimal(mu.group(1))),'ecb_reference_date':md.group(1) if md else None,'formula':'INR per EUR / USD per EUR','source_id':'ecb_fx'}

# Legal/control claim keyword checks are bounded acquisition facts, not legal advice.
def has(sid,*terms):
 t=texts.get(sid,'');return all(x.lower() in t for x in terms)
claim_audit=[
 {'claim':'EU AI Act Article 15 addresses accuracy, robustness and cybersecurity','status':'verified' if has('eu_ai_act_article_15','article 15','accuracy','robustness','cybersecurity') else 'not-verified','source_ids':['eu_ai_act_article_15']},
 {'claim':'Article 15 explicitly prohibits INT4 or requires FP8/BF16','status':'contradicted-no-textual-support' if has('eu_ai_act_article_15','article 15') and not has('eu_ai_act_article_15','int4') and not has('eu_ai_act_article_15','bf16') else 'not-determined','source_ids':['eu_ai_act_article_15']},
 {'claim':'Annex III lists high-risk use categories','status':'verified' if has('eu_ai_act_annex_3','annex iii','high-risk') else 'not-verified','source_ids':['eu_ai_act_annex_3']},
 {'claim':'HHS describes BAAs/business-associate contracts for PHI relationships','status':'verified' if has('hipaa_baa_hhs','business associate','contract') else 'not-verified','source_ids':['hipaa_baa_hhs']},
 {'claim':'AWS Bedrock as a model generically confers FedRAMP High','status':'unsupported-boundary-specific','source_ids':['aws_bedrock_compliance','fedramp_marketplace']},
 {'claim':'Self-hosting in a VPC guarantees 100% data sovereignty','status':'unsupported','source_ids':['aws_govcloud','aws_bedrock_compliance']},
]

(ROOT/'models'/'model_source_audit.json').write_text(json.dumps({'generated_at':NOW,'method':'Normalized model-family search within freshly retrieved official provider pages plus exact row matching against the retained Artificial Analysis API snapshot. Absence means not validated on retrieved pages, not proof of nonexistence.','fx':fx,'models':model_audit},indent=2,ensure_ascii=False))
(ROOT/'models'/'compliance_claim_audit.json').write_text(json.dumps({'generated_at':NOW,'claims':claim_audit},indent=2,ensure_ascii=False))
(ROOT/'local_knowledge_repository'/'official_source_manifest.json').write_text(json.dumps({'generated_at':NOW,'fx':fx,'sources':manifest},indent=2,ensure_ascii=False))
summary={'generated_at':NOW,'sources_total':len(manifest),'sources_usable':sum(bool(x.get('usable')) for x in manifest),'models_total':len(model_audit),'provider_plus_benchmark':sum(x['proof_status']=='provider-family-documented-plus-benchmark-snapshot' for x in model_audit),'provider_only':sum(x['proof_status']=='provider-family-documented-only' for x in model_audit),'benchmark_only':sum(x['proof_status']=='benchmark-snapshot-only' for x in model_audit),'unverified':sum(x['proof_status']=='unverified' for x in model_audit),'quarantined':sum(x['decision_use']=='quarantine' for x in model_audit),'fx':fx,'claim_audit':claim_audit}
print(json.dumps(summary,indent=2,ensure_ascii=False))
sys.exit(0)
