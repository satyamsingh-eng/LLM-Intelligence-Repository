from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
import json, shutil, hashlib

ROOT=Path(__file__).resolve().parents[1]
DB=ROOT/'models/verified_models_database.json'
RAW=ROOT/'models/artificial_analysis_raw_feed.json'
MANIFEST=ROOT/'local_knowledge_repository/official_source_manifest.json'
TARGETS=['kimi-k2-6','qwen3-7-plus','gemini-3-5-flash-lite']
SPEC={
 'kimi-k2-6':{
  'model_source_ids':['moonshot_k26_model'],'pricing_source_ids':['moonshot_k26_pricing'],
  'simple_summary':'A general-purpose Kimi model. The provider documents text, image and video input, thinking modes, tool calls and a 262,144-token context window.',
  'why_compare':'Useful as a lower-cost finance and agent-workflow candidate. Its retained TAU Banking score is 0.2062.',
  'official_price_scope':'Kimi official rate card: $0.95 input, $4.00 output and $0.16 cache-hit input per 1M tokens; 262,144-token context.',
  'official_cache_input_usd':0.16,
  'evidence_excerpt':'Kimi K2.6 is listed as a general-purpose model supporting text, image and video input, thinking/non-thinking modes, dialogue and Agent tasks.'},
 'qwen3-7-plus':{
  'model_source_ids':['alibaba_models'],'pricing_source_ids':['alibaba_pricing'],
  'simple_summary':'A lower-cost Qwen3.7 API tier listed by Alibaba Cloud Model Studio with the exact model ID qwen3.7-plus.',
  'why_compare':'Useful when price matters more than using the Max tier. Its retained TAU Banking score is 0.1787.',
  'official_price_scope':'Alibaba international list price for requests up to 256K tokens: $0.40 input and $1.60 output per 1M tokens.',
  'official_cache_input_usd':None,
  'evidence_excerpt':'Alibaba lists qwen3.7-plus as an OpenAI-compatible, Anthropic-compatible and DashScope model ID.'},
 'gemini-3-5-flash-lite':{
  'model_source_ids':['google_models'],'pricing_source_ids':['google_pricing'],
  'simple_summary':'Google describes Gemini 3.5 Flash-Lite as its fastest and most cost-effective 3.5 model for high-throughput execution.',
  'why_compare':'Useful for high-volume work. The retained benchmark snapshot reports 362.2 output tokens per second.',
  'official_price_scope':'Google global list price: $0.30 input and $2.50 text output per 1M tokens.',
  'official_cache_input_usd':None,
  'evidence_excerpt':'Google lists Gemini 3.5 Flash-Lite as a stable model for high-throughput execution.'}
}

db=json.loads(DB.read_text()); raw={x['id']:x for x in json.loads(RAW.read_text())['raw_api_dump']}
manifest=json.loads(MANIFEST.read_text()); source_by_id={x['id']:x for x in manifest['sources']}
fx=Decimal(manifest['fx']['usd_to_inr']); now=datetime.now(timezone.utc).replace(microsecond=0).isoformat()
archive=ROOT/'audit/archive'/f'verified_models_database-pre-40-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json'
shutil.copy2(DB,archive)
existing={x['id'] for x in db['models']}
for mid in TARGETS:
 if mid in existing: continue
 src=raw[mid]; spec=SPEC[mid]; m=json.loads(json.dumps(src))
 m['evidence_chain']={
  'status':'provider-model-and-price-documented-plus-retained-benchmark-row',
  'provider_model_sources':spec['model_source_ids'],
  'provider_pricing_sources':spec['pricing_source_ids'],
  'benchmark_source':'artificial_analysis_retained_snapshot',
  'retrieved_at':now,
  'simple_summary':spec['simple_summary'],
  'why_compare':spec['why_compare'],
  'official_price_scope':spec['official_price_scope'],
  'evidence_excerpt':spec['evidence_excerpt'],
  'content_hashes':{sid:source_by_id[sid]['sha256'] for sid in spec['model_source_ids']+spec['pricing_source_ids']}
 }
 for usd_key,inr_key in [('price_1m_input_usd','price_1m_input_inr'),('price_1m_output_usd','price_1m_output_inr')]:
  usd=Decimal(str(m['metrics'][usd_key]['value'])); value=(usd*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)
  m['metrics'][inr_key].update(value=float(value),formula=f'{usd} * {fx}',last_verified=now,confidence='calculated-from-official-price-and-ecb-reference-fx')
 m['metrics']['price_1m_cached_input_inr'].update(value=None,formula=None,last_verified=now,confidence='not-used-in-report-calculations')
 for key in ['throughput_tps','ttft_latency_seconds','tau_banking_score','coding_index','intelligence_index']:
  if m['metrics'][key]['value'] in (0,0.0):
   m['metrics'][key]['value']=None;m['metrics'][key]['confidence']='unavailable-in-retained-benchmark-snapshot'
 m['official_pricing']={
  'input_usd_per_1m':m['metrics']['price_1m_input_usd']['value'],
  'output_usd_per_1m':m['metrics']['price_1m_output_usd']['value'],
  'cache_hit_input_usd_per_1m':spec['official_cache_input_usd'],
  'scope':spec['official_price_scope'],
  'source_ids':spec['pricing_source_ids'],
  'status':'verified-exact-sku-rate-card'
 }
 db['models'].append(m)

db['system_metadata']['model_count']=len(db['models'])
db['system_metadata']['last_updated']=now
db['system_metadata']['curation_note']='40 model rows. Three added models have exact official model and price documentation plus retained benchmark rows.'
DB.write_text(json.dumps(db,indent=2,ensure_ascii=False))
print(json.dumps({'model_count':len(db['models']),'added':[x for x in TARGETS if x not in existing],'archive':str(archive),'sha256':hashlib.sha256(DB.read_bytes()).hexdigest()},indent=2))
