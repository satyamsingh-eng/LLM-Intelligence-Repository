#!/usr/bin/env python
from decimal import Decimal, ROUND_HALF_UP, getcontext
from pathlib import Path
import json,re,sys
getcontext().prec=50
ROOT=Path(__file__).resolve().parents[1]
runtime=json.loads((ROOT/'models/executive_report_runtime.json').read_text())
config=json.loads((ROOT/'models/calculator_scenarios.json').read_text())
manifest=json.loads((ROOT/'local_knowledge_repository/official_source_manifest.json').read_text())
passed=failed=0; failures=[]
def check(name,ok,detail=''):
 global passed,failed
 if ok: passed+=1; print('PASS',name)
 else: failed+=1; failures.append((name,detail)); print('FAIL',name,detail)
def q2(x): return x.quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)
def q4(x): return x.quantize(Decimal('0.0001'),rounding=ROUND_HALF_UP)
fx=Decimal(runtime['fx']['usd_to_inr'])
fx_oracle=Decimal(manifest['fx']['usd_to_inr'])
check('runtime FX equals the retained official-manifest cross-rate',fx==fx_oracle,f'{fx} != {fx_oracle}')
check('FX reference date',runtime['fx']['reference_date']=='2026-07-24',runtime['fx']['reference_date'])
js=(ROOT/'models/executive_report_runtime.js').read_text(); match=re.fullmatch(r'window\.SARVAX_REPORT_RUNTIME=(.*);\s*',js,re.S); assert match is not None
payload=json.loads(match.group(1))
check('runtime JSON/JS parity',payload==runtime)
models={m['id']:m for m in runtime['pricing_catalog']}
check('exactly 25 catalog models in pricing_catalog',len(models)==25,str(len(models)))
for mid,m in models.items():
 inp=m['input_usd'];out=m['output_usd']
 check(f'{mid}: exact INR input conversion',Decimal(str(m['input_inr']))==q2(Decimal(str(inp))*fx),str(m['input_inr']))
 check(f'{mid}: exact INR output conversion',Decimal(str(m['output_inr']))==q2(Decimal(str(out))*fx),str(m['output_inr']))
qwen=models['qwen3-7-plus'];check('Qwen has two pricing tiers',len(qwen['pricing_tiers'])==2);check('Qwen high tier input exact',Decimal(qwen['pricing_tiers'][1]['input_usd'])==Decimal('1.20'));check('Qwen high tier output exact',Decimal(qwen['pricing_tiers'][1]['output_usd'])==Decimal('4.80'))
check('Kimi total context limit exact',models['kimi-k2-6']['context_limit_tokens']==262144)
def rate(m,input_tokens,output_tokens):
 total=input_tokens+output_tokens
 if m.get('context_limit_basis')=='input_plus_output' and m.get('context_limit_tokens') and total>m['context_limit_tokens']: return None
 if m.get('pricing_tiers'):
  for t in m['pricing_tiers']:
   if input_tokens<=t['max_input_tokens']: return Decimal(t['input_usd']),Decimal(t['output_usd'])
  return None
 return Decimal(m['input_usd']),Decimal(m['output_usd'])
def cost(mid,i,o):
 r=rate(models[mid],i,o)
 if r is None:return None
 return (Decimal(i)*r[0]+Decimal(o)*r[1])/Decimal(1_000_000)*fx
presets=config['presets'];check('three scenario presets',len(presets)==3)
for p in presets:
 for mid in models:
  c=cost(mid,p['input_tokens'],p['output_tokens'])
  check(f"{p['id']} × {mid}: valid positive oracle",c is not None and c>0,str(c))
ca=cost('gemini-3-5-flash-lite',75000,8000);cb=cost('kimi-k2-6',75000,8000);assert ca is not None and cb is not None
check('default Gemini display oracle',q2(ca)==Decimal('4.10'),str(q2(ca)))
check('default Kimi display oracle',q2(cb)==Decimal('9.97'),str(q2(cb)))
check('default Gemini monthly lakh oracle',q4(ca*Decimal(10000)/Decimal(100000))==Decimal('0.4104'),str(q4(ca*Decimal(10000)/Decimal(100000))))
check('default Kimi monthly lakh oracle',q4(cb*Decimal(10000)/Decimal(100000))==Decimal('0.9971'),str(q4(cb*Decimal(10000)/Decimal(100000))))
check('default monthly difference oracle',q4(abs(cb-ca)*Decimal(10000)/Decimal(100000))==Decimal('0.5866'),str(q4(abs(cb-ca)*Decimal(10000)/Decimal(100000))))
check('default annual difference oracle',q4(abs(cb-ca)*Decimal(10000)*Decimal(12)/Decimal(100000))==Decimal('7.0398'),str(q4(abs(cb-ca)*Decimal(10000)*Decimal(12)/Decimal(100000))))
qbase=cost('qwen3-7-plus',250000,5000);qhigh=cost('qwen3-7-plus',260000,5000);assert qbase is not None and qhigh is not None
base_manual=(Decimal(250000)*Decimal('.40')+Decimal(5000)*Decimal('1.60'))/Decimal(1_000_000)*fx
high_manual=(Decimal(260000)*Decimal('1.20')+Decimal(5000)*Decimal('4.80'))/Decimal(1_000_000)*fx
check('Qwen base tier oracle',qbase==base_manual,str(qbase))
check('Qwen high tier oracle',qhigh==high_manual,str(qhigh))
check('Kimi context overflow is blocked',cost('kimi-k2-6',260000,5000) is None)
check('calculator limitations explicitly exclude taxes',any('taxes' in x for x in config['excluded_costs']))
print(json.dumps({'passed':passed,'failed':failed,'failures':failures},indent=2))
sys.exit(1 if failed else 0)
