from pathlib import Path
from decimal import Decimal,ROUND_HALF_UP
from datetime import datetime,timezone
import json,hashlib,shutil
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'models/verified_models_database.json';d=json.loads(p.read_text());audit=json.loads((ROOT/'models/model_source_audit.json').read_text());ab={x['id']:x for x in audit['models']};fx=Decimal(audit['fx']['usd_to_inr'])
backup=ROOT/'audit/archive'/f'verified_models_database-pre-evidence-fix-{datetime.now().strftime("%Y%m%d-%H%M%S")}.json';shutil.copy2(p,backup)
d['system_metadata']['usd_to_inr_rate']=str(fx);d['system_metadata']['usd_to_inr_reference_date']=audit['fx']['ecb_reference_date'];d['system_metadata']['usd_to_inr_source']='European Central Bank daily EUR reference rates; INR/EUR divided by USD/EUR';d['system_metadata']['overall_confidence']='Scoped per model and metric; see validation_evidence';d['system_metadata']['underlying_assumptions']=['INR conversion uses the retained ECB reference-date cross-rate.','Cache and batch discounts are not applied without exact provider, SKU, region, TTL and eligibility evidence.','Benchmark metrics use the retained Artificial Analysis API snapshot; fresh API refresh was unavailable.']
for m in d['models']:
 a=ab[m['id']];m['validation_evidence']={'proof_status':a['proof_status'],'decision_use':a['decision_use'],'official_source_ids':a['official_source_ids'],'official_hits':a['official_hits'],'benchmark_snapshot_exact_name_match':a['benchmark_snapshot_exact_name_match'],'benchmark_snapshot_fresh_api_retrieval':a['benchmark_snapshot_fresh_api_retrieval'],'metric_checks':a['metric_checks']}
 met=m['metrics'];iu=met['price_1m_input_usd']['value'];ou=met['price_1m_output_usd']['value']
 met['price_1m_input_inr'].update(value=float((Decimal(str(iu))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)),formula=f'{iu} * {fx}',last_verified=audit['generated_at'],confidence='Calculated from retained USD rate and ECB reference-date FX')
 met['price_1m_output_inr'].update(value=float((Decimal(str(ou))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)),formula=f'{ou} * {fx}',last_verified=audit['generated_at'],confidence='Calculated from retained USD rate and ECB reference-date FX')
 met['price_1m_cached_input_inr'].update(value=None,formula=None,last_verified=audit['generated_at'],confidence='Not validated for exact provider/SKU/region/TTL')
 if m['id']=='gemini-3-5-flash-medium':
  met['coding_index']['value']=None;met['coding_index']['confidence']='Unavailable in retained benchmark snapshot'
  met['tau_banking_score']['value']=None;met['tau_banking_score']['confidence']='Unavailable in retained benchmark snapshot'
p.write_text(json.dumps(d,indent=2,ensure_ascii=False))
print(json.dumps({'models':len(d['models']),'backup':str(backup),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()},indent=2))
