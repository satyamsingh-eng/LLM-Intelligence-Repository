from pathlib import Path
from decimal import Decimal,ROUND_HALF_UP
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]; HTML=ROOT/'index.html'
audit=json.loads((ROOT/'models/model_source_audit.json').read_text()); adb={x['id']:x for x in audit['models']}
db=json.loads((ROOT/'models/verified_models_database.json').read_text())['models'];dbd={x['id']:x for x in db}
man=json.loads((ROOT/'local_knowledge_repository/official_source_manifest.json').read_text());src={x['id']:x for x in man['sources']}
fx=Decimal(audit['fx']['usd_to_inr'])
s=HTML.read_text();a=s.index('    const models = [')+len('    const models = ');b=s.index('\n];',a)+2
rows=json.loads(s[a:b]);ids={x['id'] for x in rows}
for mid in [x['id'] for x in db if x['id'] not in ids]:
 d=dbd[mid];q=adb[mid];m=d['metrics'];hits=q['official_hits'];proof=src[hits[0]] if hits else None
 def v(k): return m.get(k,{}).get('value')
 row={'id':mid,'name':d['name'],'slug':mid,'link':'#models','vendor':d['vendor'],'intel':v('intelligence_index'),'coding':v('coding_index'),'tau':None if v('tau_banking_score') in (None,0) else f"{v('tau_banking_score'):.4f}",'inUsd':v('price_1m_input_usd'),'outUsd':v('price_1m_output_usd'),'inInr':float((Decimal(str(v('price_1m_input_usd')))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)),'outInr':float((Decimal(str(v('price_1m_output_usd')))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)),'cachedInr':None,'cacheRateStatus':'not-validated','tps':None if v('throughput_tps') in (None,0) else v('throughput_tps'),'ttft':None if v('ttft_latency_seconds') in (None,0) else v('ttft_latency_seconds'),'sourceName':(proof['publisher']+' official documentation') if proof else 'Official source unavailable','sourceUrl':proof.get('final_url','#') if proof else '#','sourceSha256':proof.get('sha256') if proof else None,'retrievalDate':proof.get('retrieved_at') if proof else None,'proofStatus':q['proof_status'],'decisionUse':q['decision_use'],'officialHits':hits,'benchmarkExact':q['benchmark_snapshot_exact_name_match'],'benchmarkFresh':q['benchmark_snapshot_fresh_api_retrieval'],'metricMismatches':[k for k,vv in q['metric_checks'].items() if not vv['match_with_rounding_tolerance']]}
 rows.append(row)
s=s[:a]+json.dumps(rows,indent=2,ensure_ascii=False)+s[b:]
HTML.write_text(s)
print(json.dumps({'models_after':len(rows),'added':[x['id'] for x in rows if x['id'] not in ids],'sha256':hashlib.sha256(HTML.read_bytes()).hexdigest()},indent=2))
