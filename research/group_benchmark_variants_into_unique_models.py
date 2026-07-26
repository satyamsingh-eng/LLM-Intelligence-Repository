from pathlib import Path
from datetime import datetime
import json,re,shutil,hashlib

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'; CARDS=ROOT/'models/section7_model_cards.json'; CONFIGS=ROOT/'models/section7_model_configurations.json'
html=HTML.read_text();data=json.loads(CARDS.read_text());rows=data['models']
archive=ROOT/'audit/archive'/f'index-pre-unique-model-grouping-{datetime.now().strftime("%Y%m%d-%H%M%S")}.html';shutil.copy2(HTML,archive)
CONFIGS.write_text(json.dumps({**{k:v for k,v in data.items() if k!='models'},'configuration_count':len(rows),'definition':'One row per retained benchmark configuration. Effort labels are kept here and grouped into unique model cards in section7_model_cards.json.','models':rows},indent=2,ensure_ascii=False))

def base_name(name): return re.sub(r'\s*\([^)]*\)\s*$','',name).strip()
def setting(name,base):
 tail=name[len(base):].strip()
 return tail[1:-1].strip() if tail.startswith('(') and tail.endswith(')') else 'Default benchmark configuration'
def values(items,key): return [float(x[key]) for x in items if x.get(key) not in (None,0,0.0)]
def rng(items,key,digits=1,prefix='',suffix=''):
 vals=values(items,key)
 if not vals:return 'Not available'
 lo,hi=min(vals),max(vals)
 fmt=lambda x:f'{x:.{digits}f}'
 return f'{prefix}{fmt(lo)}{suffix}' if abs(lo-hi)<10**(-digits) else f'{prefix}{fmt(lo)}–{fmt(hi)}{suffix}'

groups={}
for r in rows:groups.setdefault((r['vendor'],base_name(r['name'])),[]).append(r)
unique=[]
for (vendor,base),items in groups.items():
 primary=items[0]
 eligible=[x for x in items if x['decisionUse']!='quarantine']
 decision='eligible-with-metric-scope-shown' if eligible else 'quarantine'
 proofs={x['proofStatus'] for x in items}
 if 'provider-family-documented-plus-benchmark-snapshot' in proofs: proof='provider-family-documented-plus-benchmark-snapshot'
 elif 'provider-family-documented-only' in proofs: proof='provider-family-documented-only'
 elif 'benchmark-snapshot-only' in proofs: proof='benchmark-snapshot-only'
 else: proof='unverified'
 configs=[]
 for x in items:
  configs.append({'id':x['id'],'fullName':x['name'],'setting':setting(x['name'],base),'tau':x.get('tau'),'intel':x.get('intel'),'coding':x.get('coding'),'tps':x.get('tps'),'ttft':x.get('ttft'),'inUsd':x.get('inUsd'),'outUsd':x.get('outUsd'),'inInr':x.get('inInr'),'outInr':x.get('outInr'),'benchmarkExact':x.get('benchmarkExact'),'metricMismatches':x.get('metricMismatches',[])})
 count=len(items)
 if count>1:
  summary=f'One {vendor} model represented by {count} retained benchmark configurations. The configuration labels are grouped here instead of being counted as separate model cards.'
  why=f'Use the ranges to see how benchmark settings changed the result. Open the guide to compare all {count} configurations side by side.'
 else:
  summary=primary['simpleSummary']
  if setting(primary['name'],base)!='Default benchmark configuration': summary+=f" The retained benchmark row uses the setting: {setting(primary['name'],base)}."
  why=primary['whyCompare']
 union_mismatch=sorted({m for x in items for m in x.get('metricMismatches',[])})
 unique.append({
  **{k:v for k,v in primary.items() if k not in ['name','simpleSummary','whyCompare','metricMismatches','proofStatus','decisionUse']},
  'id':re.sub(r'[^a-z0-9]+','-',base.lower()).strip('-'),'name':base,'simpleSummary':summary,'whyCompare':why,'proofStatus':proof,'decisionUse':decision,'metricMismatches':union_mismatch,
  'configurationCount':count,'configurations':configs,'configurationNames':[x['name'] for x in items],
  'tauDisplay':rng(items,'tau',4),'intelDisplay':rng(items,'intel',1),'speedDisplay':rng(items,'tps',1,suffix=' tps'),'inputPriceDisplay':rng(items,'inInr',2,prefix='₹'),'outputPriceDisplay':rng(items,'outInr',2,prefix='₹'),
  'sortTau':max(values(items,'tau'),default=-1),'sortIntel':max(values(items,'intel'),default=-1),'sortSpeed':max(values(items,'tps'),default=-1),'sortPrice':min(values(items,'inInr'),default=10**12),
  'groupingNote':'Configuration labels are retained benchmark settings in this dataset and are not counted as separate model cards.'
 })
unique.sort(key=lambda x:x['sortIntel'],reverse=True)
CARDS.write_text(json.dumps({**{k:v for k,v in data.items() if k!='models'},'model_count':len(unique),'benchmark_configuration_count':len(rows),'data_boundary':'24 unique model cards group 40 retained benchmark configurations. Provider pages establish model identity; benchmark settings remain visible inside each card.','models':unique},indent=2,ensure_ascii=False))

# Replace embedded presentation data.
start=html.index('    const models = [')+len('    const models = ');end=html.index('\n];',start)+2
html=html[:start]+json.dumps(unique,indent=2,ensure_ascii=False)+html[end:]
repls={
 '<a href="#models">40 Model Cards</a>':'<a href="#models">24 Model Cards</a>',
 'Evidence-scoped evaluation of 40 model cards across wealth advisory math, routing and unit economics.':'Evidence-scoped evaluation of 24 unique models across 40 retained benchmark configurations.',
 'Model proof status: <strong>37 provider + benchmark · 3 need more proof</strong>':'Model proof status: <strong>21 unique models with provider + benchmark · 3 need more proof</strong>',
 'Thirty-seven model rows have both current provider-family documentation and an exact retained benchmark-snapshot row; three need more proof.':'Twenty-one unique models have both provider-family documentation and at least one exact retained benchmark row; three need more proof.',
 '<div class="kpi green"><div class="num">37</div><div class="label">Provider + Benchmark Proof</div></div>':'<div class="kpi green"><div class="num">21</div><div class="label">Unique Models with Two Proof Types</div></div>',
 '<div class="kpi"><div class="num">40</div><div class="label">Interactive Model Cards</div></div>':'<div class="kpi"><div class="num">40</div><div class="label">Benchmark Configurations Mapped</div></div>',
 '<!-- SECTION 7: 40 INTERACTIVE MODEL EVIDENCE CARDS -->':'<!-- SECTION 7: 24 UNIQUE MODELS / 40 BENCHMARK CONFIGURATIONS -->',
 '<h2>40 Interactive Model Evidence Cards</h2>':'<h2>24 Unique Model Cards — 40 Benchmark Configurations</h2>',
 'Every card explains the model in simple words: what the numbers mean, why to compare it, what is proven, and what is still unknown.':'Each model appears once. Adaptive Reasoning and effort labels are mapped inside the card as benchmark configurations, not counted as separate models. Every card explains the score range, evidence and open gaps in simple words.',
 '<button class="proof-filter active" data-proof="all" type="button">All 40</button>':'<button class="proof-filter active" data-proof="all" type="button">All 24 models</button>',
 '<button class="proof-filter" data-proof="dual" type="button">Provider + benchmark 37</button>':'<button class="proof-filter" data-proof="dual" type="button">Provider + benchmark 21</button>',
 '<span id="modelResultCount" aria-live="polite">40 models</span>':'<span id="modelResultCount" aria-live="polite">24 unique models · 40 configurations</span>'}
for old,new in repls.items():
 if old not in html:raise RuntimeError('Missing replacement target: '+old)
 html=html.replace(old,new,1)

# Renderer: show metric ranges and configuration count.
old="""      const numeric=(m,k)=>m[k]===null||m[k]===undefined?-Infinity:Number(m[k]);
      visible.sort((a,b)=>sort==='name'?a.name.localeCompare(b.name):sort==='price'?(numeric(a,'inInr')-numeric(b,'inInr')):(numeric(b,sort==='speed'?'tps':sort)-numeric(a,sort==='speed'?'tps':sort)));
      document.getElementById('modelResultCount').textContent=`${visible.length} of ${models.length} models`;
      document.getElementById('modelCardsGrid').innerHTML=visible.map(m=>{
        const tau=displayMetric(m.tau,4),intel=displayMetric(m.intel,1),speed=m.tps?`${Number(m.tps).toFixed(1)} tps`:'Not available';
        const inputPrice=m.inInr===null?'Not available':`₹${Number(m.inInr).toFixed(2)}`;
        return `<article class=\"model-card\" data-proof=\"${proofClass(m)}\">"""
new="""      visible.sort((a,b)=>sort==='name'?a.name.localeCompare(b.name):sort==='price'?(a.sortPrice-b.sortPrice):(b[sort==='speed'?'sortSpeed':sort==='tau'?'sortTau':'sortIntel']-a[sort==='speed'?'sortSpeed':sort==='tau'?'sortTau':'sortIntel']));
      const configTotal=visible.reduce((n,m)=>n+m.configurationCount,0);
      document.getElementById('modelResultCount').textContent=`${visible.length} of ${models.length} unique models · ${configTotal} configurations`;
      document.getElementById('modelCardsGrid').innerHTML=visible.map(m=>{
        return `<article class=\"model-card\" data-proof=\"${proofClass(m)}\">"""
if old not in html:raise RuntimeError('Renderer metrics block missing')
html=html.replace(old,new,1)
html=html.replace("<div class=\"model-card-head\"><div><div class=\"model-card-vendor\">${m.vendor}</div><h3>${m.name}</h3></div><span class=\"proof-badge ${proofClass(m)}\">${proofLabel(m)}</span></div>","<div class=\"model-card-head\"><div><div class=\"model-card-vendor\">${m.vendor}</div><h3>${m.name}</h3><span class=\"configuration-count\">${m.configurationCount} benchmark configuration${m.configurationCount===1?'':'s'}</span></div><span class=\"proof-badge ${proofClass(m)}\">${proofLabel(m)}</span></div>",1)
html=html.replace("<button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','tau')\"><strong>${tau}</strong><span>Finance score · higher is better</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','intel')\"><strong>${intel}</strong><span>General score · higher is better</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','speed')\"><strong>${speed}</strong><span>Generation speed</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','price')\"><strong>${inputPrice}</strong><span>Input price / 1M tokens</span></button>","<button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','tau')\"><strong>${m.tauDisplay}</strong><span>Finance score ${m.configurationCount>1?'range':''} · higher is better</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','intel')\"><strong>${m.intelDisplay}</strong><span>General score ${m.configurationCount>1?'range':''} · higher is better</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','speed')\"><strong>${m.speedDisplay}</strong><span>Generation speed ${m.configurationCount>1?'range':''}</span></button>\n            <button class=\"model-metric\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','price')\"><strong>${m.inputPriceDisplay}</strong><span>Input price / 1M tokens</span></button>",1)
html=html.replace("<div class=\"model-card-actions\"><button class=\"model-detail-btn\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','overview')\">Open simple evidence guide</button></div>","<div class=\"model-card-actions\"><button class=\"model-detail-btn\" type=\"button\" onclick=\"openEvidenceModal('${m.id}','overview')\">View ${m.configurationCount} configuration${m.configurationCount===1?'':'s'} + evidence</button></div>",1)

# Modal uses ranges and builds the configuration table.
html=html.replace("document.getElementById('evPrice').textContent=`Input: ${m.inUsd===null?'not available':'$'+m.inUsd+'/1M'} (${m.inInr===null?'not available':'₹'+Number(m.inInr).toFixed(2)}) · Output: ${m.outUsd===null?'not available':'$'+m.outUsd+'/1M'} (${m.outInr===null?'not available':'₹'+Number(m.outInr).toFixed(2)}). ${m.priceStatus}.`;","document.getElementById('evPrice').textContent=`Input range: ${m.inputPriceDisplay} per 1M tokens · Output range: ${m.outputPriceDisplay} per 1M tokens. ${m.priceStatus}.`;",1)
html=html.replace("document.getElementById('evScores').textContent=`TAU Banking: ${displayMetric(m.tau,4)} · Intelligence Index: ${displayMetric(m.intel,1)} · Speed: ${m.tps?Number(m.tps).toFixed(1)+' output tokens/second':'not available'}.`;","document.getElementById('evScores').textContent=`Across ${m.configurationCount} retained configuration${m.configurationCount===1?'':'s'} — TAU Banking: ${m.tauDisplay} · Intelligence Index: ${m.intelDisplay} · Speed: ${m.speedDisplay}.`;",1)
insert="""      document.getElementById('evGrouping').textContent=m.groupingNote;
      document.getElementById('evConfigBody').innerHTML=m.configurations.map(c=>`<tr><td>${c.setting}</td><td>${displayMetric(c.tau,4)}</td><td>${displayMetric(c.intel,1)}</td><td>${c.tps?Number(c.tps).toFixed(1)+' tps':'Not available'}</td><td>${c.inInr===null?'Not available':'₹'+Number(c.inInr).toFixed(2)}</td></tr>`).join('');
"""
target="      document.getElementById('evLimits').textContent=m.evidenceLimit;\n"
if target not in html:raise RuntimeError('Modal insert point missing')
html=html.replace(target,target+insert,1)
modal_target='''      <div class="evidence-links"><a id="evSourceLink" href="#" target="_blank" rel="noopener">Official provider source</a><a id="evPricingLink" href="#" target="_blank" rel="noopener">Official pricing source</a></div>'''
modal_new='''      <section class="configuration-map"><h3>Benchmark configurations mapped to this one model</h3><p id="evGrouping" class="muted"></p><div class="configuration-table-wrap"><table><thead><tr><th>Configuration</th><th>Finance</th><th>General</th><th>Speed</th><th>Input / 1M</th></tr></thead><tbody id="evConfigBody"></tbody></table></div></section>
      <div class="evidence-links"><a id="evSourceLink" href="#" target="_blank" rel="noopener">Official provider source</a><a id="evPricingLink" href="#" target="_blank" rel="noopener">Official pricing source</a></div>'''
if modal_target not in html:raise RuntimeError('Modal markup insert missing')
html=html.replace(modal_target,modal_new,1)
css='''.configuration-count{display:inline-block;margin-top:8px;color:#86868b;font-size:11px}.configuration-map{margin:18px 0;background:#111;border:1px solid #333336;border-radius:12px;padding:16px}.configuration-map h3{font-size:16px;margin-bottom:6px}.configuration-table-wrap{overflow-x:auto;margin-top:12px}.configuration-table-wrap table{min-width:620px}.configuration-table-wrap th,.configuration-table-wrap td{padding:10px;font-size:12px;text-align:left;border-bottom:1px solid #2c2c2e}.configuration-table-wrap th{color:#86868b}.configuration-table-wrap td{color:#d1d1d6}'''
html=html.replace('</style>',css+'</style>',1)
HTML.write_text(html)
print(json.dumps({'unique_model_cards':len(unique),'benchmark_configurations':len(rows),'two_proof_unique_models':sum(x['decisionUse']!='quarantine' for x in unique),'needs_more_proof':sum(x['decisionUse']=='quarantine' for x in unique),'archive':str(archive),'html_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest()},indent=2))
