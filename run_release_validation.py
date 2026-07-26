#!/usr/bin/env python
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP, getcontext
import json, re, hashlib, subprocess, sys
getcontext().prec=40
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None): checks.append({'name':name,'pass':bool(ok),'detail':detail})
def load(rel): return json.loads((ROOT/rel).read_text())
html=(ROOT/'index.html').read_text()
runtime=load('models/executive_report_runtime.json');cards=load('models/section7_model_cards.json');configs=load('models/section7_model_configurations.json');routing=load('models/uncanny_valley_routing.json');manifest=load('local_knowledge_repository/official_source_manifest.json');claims=load('models/compliance_claim_audit.json');active=load('models/artificial_analysis_live_dataset.json');raw=load('models/artificial_analysis_raw_feed.json')
runtime_js=(ROOT/'models/executive_report_runtime.js').read_text()
runtime_js_data=json.loads(runtime_js.removeprefix('window.SARVAX_REPORT_RUNTIME=').removesuffix(';\n'))
fx=Decimal(runtime['fx']['usd_to_inr'])
check('HTML is canonical and nontrivial',len(html)>50000,len(html))
for i in range(1,9): check(f'Section {i} marker exists',f'Section {i}' in html)
check('Section 9 absent','Section 9' not in html)
check('Model corpora not embedded','const models =' not in html)
check('Runtime JSON loaded by HTML','models/executive_report_runtime.json' in html)
check('Chart.js is bundled locally',(ROOT/'vendor/chart.umd.min.js').is_file() and './vendor/chart.umd.min.js' in html)
check('Decimal.js is bundled locally',(ROOT/'vendor/decimal.min.js').is_file() and './vendor/decimal.min.js' in html)
check('No obsolete knowledge graph runtime','const knowledgeGraph' not in html and 'initKnowledgeGraph' not in html)
check('No obsolete glossary runtime','const glossary' not in html and 'openTermModal' not in html)
check('No gradients','linear-gradient' not in html and 'radial-gradient' not in html)
check('No glow-effect labels or classes','glow' not in html.lower())
for banned in ['100% Zero-Defect','Margin Recovery','Expected Annual Capital Saved','Unquestioned #1','₹4.20','Text PDF','Scanned / Image PDF','Structured Tax Data']:
 check(f'Banned claim absent: {banned}',banned not in html)
check('No local absolute paths in public HTML','/Users/' not in html)
secret_patterns=[r'AIza[0-9A-Za-z_-]{20,}',r'sk-[0-9A-Za-z_-]{20,}',r'gh[pousr]_[0-9A-Za-z]{20,}',r'api[_-]?key\s*[:=]\s*["\'][^"\']+["\']']
for pat in secret_patterns: check(f'No secret pattern {pat[:12]}',re.search(pat,html,re.I) is None)
models=runtime['models'];ids=[m['id'] for m in models]
check('24 unique model cards',len(models)==24 and len(set(ids))==24,len(models))
check('Direct-open runtime JS matches central JSON',runtime_js_data==runtime)
check('Canonical HTML loads direct-open runtime payload','./models/executive_report_runtime.js' in html)
check('Runtime/model-card equality',models==cards['models'])
check('40 benchmark configurations',cards['benchmark_configuration_count']==40,len(cards.get('models',[])))
config_rows=configs['models'];check('Configuration file has 40 rows',len(config_rows)==40,len(config_rows))
check('Every configuration maps to one grouped card',{c['id'] for c in config_rows}=={c['id'] for m in models for c in m['configurations']})
check('No duplicate configuration IDs',len({c['id'] for c in config_rows})==len(config_rows))
check('Model configuration counts reconcile',sum(m['configurationCount'] for m in models)==40,sum(m['configurationCount'] for m in models))
proof_counts={k:sum(m['proofStatus']==v for m in models) for k,v in {'provider_plus_benchmark':'provider-family-documented-plus-benchmark-snapshot','provider_only':'provider-family-documented-only','benchmark_only':'benchmark-snapshot-only'}.items()}
expected_e=[{'name':'Provider + benchmark','value':proof_counts['provider_plus_benchmark']},{'name':'Provider only','value':proof_counts['provider_only']},{'name':'Benchmark only','value':proof_counts['benchmark_only']}]
check('Evidence chart counts reconcile',runtime['chart_data']['evidence_coverage']==expected_e,proof_counts)
expected_i=sorted([{'name':m['name'],'value':m['sortIntel']} for m in models if m.get('sortIntel')],key=lambda x:x['value'],reverse=True)[:15]
expected_t=sorted([{'name':m['name'],'value':m['sortTau']} for m in models if m.get('sortTau')],key=lambda x:x['value'],reverse=True)[:15]
check('Intelligence chart recomputes exactly',runtime['chart_data']['intelligence']==expected_i)
check('TAU chart recomputes exactly',runtime['chart_data']['tau_banking']==expected_t)
check('TAU chart higher-is-better ordering',all(expected_t[i]['value']>=expected_t[i+1]['value'] for i in range(len(expected_t)-1)))
check('Kimi retained TAU claim scoped',expected_t[0]['name']=='Kimi K3' and Decimal(str(expected_t[0]['value']))==Decimal('0.3340'),expected_t[0])
check('Active benchmark snapshot has 586 rows',len(active['data'])==586,len(active['data']))
check('Historical raw snapshot distinctly has 551 rows',len(raw['raw_api_dump'])==551,len(raw['raw_api_dump']))
check('Runtime names active snapshot explicitly',runtime['metadata']['active_benchmark_snapshot_rows']==586 and 'live_dataset' in runtime['metadata']['active_benchmark_snapshot_file'])
usable=[s for s in manifest['sources'] if s.get('usable')]
check('Runtime usable source count matches manifest',runtime['metadata']['usable_sources']==len(usable),(runtime['metadata']['usable_sources'],len(usable)))
for s in usable:
 p=ROOT/s['snapshot'];ok=p.exists() and p.stat().st_size==s['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest()==s['sha256'];check(f"Source snapshot integrity: {s['id']}",ok,{'expected_bytes':s['bytes'],'actual_bytes':p.stat().st_size if p.exists() else None})
check('EU Article 15 source usable',any(s['id']=='eu_ai_act_article_15' and s.get('usable') for s in manifest['sources']))
check('EU Annex III source usable',any(s['id']=='eu_ai_act_annex_3' and s.get('usable') for s in manifest['sources']))
claimmap={c['claim']:c['status'] for c in claims['claims']}
check('Article 15 claim verified',claimmap.get('EU AI Act Article 15 addresses accuracy, robustness and cybersecurity')=='verified',claimmap)
check('INT4 claim rejected',claimmap.get('Article 15 explicitly prohibits INT4 or requires FP8/BF16')=='contradicted-no-textual-support')
check('Annex III claim verified',claimmap.get('Annex III lists high-risk use categories')=='verified')
check('FedRAMP boundary retained',claimmap.get('AWS Bedrock as a model generically confers FedRAMP High')=='unsupported-boundary-specific')
check('Sovereignty overclaim rejected',claimmap.get('Self-hosting in a VPC guarantees 100% data sovereignty')=='unsupported')
check('ECB FX exact match',runtime['fx']['usd_to_inr']==manifest['fx']['usd_to_inr'])
check('ECB reference date exact match',runtime['fx']['reference_date']==manifest['fx']['ecb_reference_date']=='2026-07-24')
for p in runtime['pricing_catalog']:
 expected_in=(Decimal(p['input_usd'])*fx).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP);expected_out=(Decimal(p['output_usd'])*fx).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
 check(f"Exact input INR conversion: {p['id']}",Decimal(p['input_inr'])==expected_in,{'expected':str(expected_in),'actual':p['input_inr']})
 check(f"Exact output INR conversion: {p['id']}",Decimal(p['output_inr'])==expected_out,{'expected':str(expected_out),'actual':p['output_inr']})
 check(f"Official rate URL: {p['id']}",p['source_url'].startswith('https://') and p['status'] in ('verified-exact-rate-card','retained-benchmark-rate'))
 if 'cache_read_usd' in p:
  expected_cache=(Decimal(p['cache_read_usd'])*fx).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP);check(f"Exact cache INR conversion: {p['id']}",Decimal(p['cache_read_inr'])==expected_cache)
price_chart=runtime['chart_data']['verified_pricing'];check('Price chart contains catalog rates',len(price_chart)==len(runtime['pricing_catalog'])==25)
check('Price chart values reconcile',all(any((x['name']==p['name'] or x['name']==p.get('chart_label')) and Decimal(x['input_inr'])==Decimal(p['input_inr']) and Decimal(x['output_inr'])==Decimal(p['output_inr']) for x in price_chart) for p in runtime['pricing_catalog']))
# Recompute known calculator scenario with exact decimals.
def scenario(mid,it='75000',ot='8000',runs='10000'):
 p=next(p for p in runtime['pricing_catalog'] if p['id']==mid);per=(Decimal(it)*Decimal(p['input_usd'])+Decimal(ot)*Decimal(p['output_usd']))/Decimal(1_000_000)*fx;return per,per*Decimal(runs)
ga,gam=scenario('gemini-3-5-flash-lite');ki,kim=scenario('kimi-k2-6')
check('Known Gemini scenario rounds exactly',ga.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)==Decimal('4.10'),str(ga))
check('Known Kimi scenario rounds exactly',ki.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)==Decimal('9.97'),str(ki))
check('Known monthly difference rounds exactly',(kim-gam).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)==Decimal('58664.84'),str(kim-gam))
journeys=routing['journeys'];agents=[a for j in journeys for a in j['agents']]
check('3 approved wealth-advisory journeys',set(j['id'] for j in journeys)=={'relationship','portfolio','operations'})
check('12 unique SARVAX agents',len(agents)==12 and len(set(agents))==12,agents)
check('Workflow scenarios match journeys',set(runtime['workflow_player'])==set(j['id'] for j in journeys))
check('Every workflow has mandatory human approval',all(any(s['type']=='human' for s in w['steps']) for w in runtime['workflow_player'].values()))
check('Financial and compliance workflows have deterministic controls',all(any(s['type']=='deterministic' for s in runtime['workflow_player'][k]['steps']) for k in ['portfolio','operations']))
check('No synthetic telemetry fields',all(not any(k in s for k in ['input_tokens','output_tokens','latency','cost']) for w in runtime['workflow_player'].values() for s in w['steps']))
check('Frontend snapshot limitation explicit','unverified' in runtime['metadata']['product_snapshot_branch_status'])
# JavaScript syntax: extract inline scripts and validate with node --check.
blocks=re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>',html,re.S);js='\n'.join(x for x in blocks if x.strip());tmp=ROOT/'qa'/'_inline_release_check.js';tmp.write_text(js);proc=subprocess.run(['node','--check',str(tmp)],capture_output=True,text=True);check('Inline JavaScript syntax',proc.returncode==0,proc.stderr);tmp.unlink(missing_ok=True)
# Git whitespace check when repository exists.
proc=subprocess.run(['git','diff','--check'],cwd=ROOT,capture_output=True,text=True);check('git diff --check',proc.returncode==0,proc.stdout+proc.stderr)
out={'generated_at':runtime['metadata']['generated_at'],'pass':sum(c['pass'] for c in checks),'total':len(checks),'errors':[c for c in checks if not c['pass']],'checks':checks}
(ROOT/'qa'/'release_data_validation.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
print(json.dumps({'pass':out['pass'],'total':out['total'],'errors':out['errors']},indent=2,ensure_ascii=False))
sys.exit(0 if not out['errors'] else 1)
