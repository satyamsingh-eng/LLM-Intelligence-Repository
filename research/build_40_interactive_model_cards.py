from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import json,re,shutil,hashlib

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'; DB=ROOT/'models/verified_models_database.json'; AUDIT=ROOT/'models/model_source_audit.json'; MANIFEST=ROOT/'local_knowledge_repository/official_source_manifest.json'; OUT=ROOT/'models/section7_model_cards.json'
html=HTML.read_text();db=json.loads(DB.read_text());audit=json.loads(AUDIT.read_text());manifest=json.loads(MANIFEST.read_text())
fx=Decimal(manifest['fx']['usd_to_inr']);fx_date=manifest['fx']['ecb_reference_date'];ab={x['id']:x for x in audit['models']};sources={x['id']:x for x in manifest['sources']}
archive=ROOT/'audit/archive'/f'index-pre-40-model-cards-{datetime.now().strftime("%Y%m%d-%H%M%S")}.html';shutil.copy2(HTML,archive)

# Preserve existing presentation-only links/labels while sourcing data from the central model DB.
start=html.index('    const models = [')+len('    const models = ');end=html.index('\n];',start)+2
existing={x['id']:x for x in json.loads(html[start:end])}

def metric(m,key): return m.get('metrics',{}).get(key,{}).get('value')
def public_source(a,pricing=False):
 ids=a.get('official_hits') or a.get('official_source_ids') or []
 if pricing:
  chosen=next((sid for sid in ids if 'pricing' in sid and sources.get(sid,{}).get('usable')),None)
 else:
  chosen=next((sid for sid in ids if 'pricing' not in sid and sources.get(sid,{}).get('usable')),None)
 if not chosen: chosen=next((sid for sid in ids if sources.get(sid,{}).get('usable')),None)
 return (chosen,sources.get(chosen)) if chosen else (None,None)

def simple_fields(m,a):
 ec=m.get('evidence_chain',{})
 tau=metric(m,'tau_banking_score');intel=metric(m,'intelligence_index');tps=metric(m,'throughput_tps')
 summary=ec.get('simple_summary')
 if not summary:
  if a['proof_status']=='provider-family-documented-plus-benchmark-snapshot':
   article='An' if m['vendor'][:1].lower() in 'aeiou' else 'A'
   summary=f"{article} {m['vendor']} model row. The provider documents this model family, and the retained independent benchmark snapshot contains the exact row name."
  elif a['proof_status']=='provider-family-documented-only':
   article='An' if m['vendor'][:1].lower() in 'aeiou' else 'A'
   summary=f"{article} {m['vendor']} model documented by the provider. This report does not have an exact matching row in the retained independent benchmark snapshot."
  elif a['proof_status']=='benchmark-snapshot-only': summary=f"A model name found in the retained independent benchmark snapshot, but current official provider documentation was not established."
  else: summary='A model row without enough current evidence for decision use.'
 why=ec.get('why_compare')
 if not why:
  if tau is not None and tau>=0.25: why=f"Finance comparison: its retained TAU Banking score is {tau:.4f}. Treat this as a shortlist signal, not production proof."
  elif tps is not None and tps>=150: why=f"Speed comparison: the retained snapshot reports {tps:g} output tokens per second. Useful when throughput matters."
  elif intel is not None and intel>=50: why=f"General reasoning comparison: its retained Intelligence Index is {intel:g}. Use task-specific tests before choosing it."
  else: why='Use it as a cost and benchmark comparison row. No production recommendation is implied.'
 limit='This card does not prove production quality, customer access, SLA, security, compliance or suitability for SARVAX. Run task-specific tests before deployment.'
 return summary,why,limit,ec.get('evidence_excerpt')

cards=[]
for m in db['models']:
 a=ab[m['id']];old=existing.get(m['id'],{});model_sid,model_src=public_source(a,False);price_sid,price_src=public_source(a,True);summary,why,limit,excerpt=simple_fields(m,a)
 in_usd=metric(m,'price_1m_input_usd');out_usd=metric(m,'price_1m_output_usd')
 in_inr=float((Decimal(str(in_usd))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)) if in_usd is not None else None
 out_inr=float((Decimal(str(out_usd))*fx).quantize(Decimal('0.01'),ROUND_HALF_UP)) if out_usd is not None else None
 official=m.get('official_pricing')
 price_status='Verified exact official rate card' if official and official.get('status')=='verified-exact-sku-rate-card' else 'Retained benchmark rate; exact SKU price needs claim-level verification'
 card={
  'id':m['id'],'name':m['name'],'slug':old.get('slug',m['id']),'link':old.get('link',(model_src or {}).get('final_url','#')),'vendor':m['vendor'],
  'intel':metric(m,'intelligence_index'),'coding':metric(m,'coding_index'),'tau':metric(m,'tau_banking_score'),'inUsd':in_usd,'outUsd':out_usd,'inInr':in_inr,'outInr':out_inr,'cachedInr':None,
  'tps':metric(m,'throughput_tps'),'ttft':metric(m,'ttft_latency_seconds'),'proofStatus':a['proof_status'],'decisionUse':a['decision_use'],'officialHits':a['official_hits'],'benchmarkExact':a['benchmark_snapshot_exact_name_match'],'benchmarkFresh':a['benchmark_snapshot_fresh_api_retrieval'],'metricMismatches':[k for k,v in a['metric_checks'].items() if not v['match_with_rounding_tolerance']],
  'sourceName':(model_src or {}).get('publisher','Official provider source unavailable'),'sourceUrl':(model_src or {}).get('final_url','#'),'sourceSha256':(model_src or {}).get('sha256'),'retrievalDate':(model_src or {}).get('retrieved_at'),'pricingSourceUrl':(price_src or {}).get('final_url'),'pricingSourceName':(price_src or {}).get('publisher'),'pricingSourceSha256':(price_src or {}).get('sha256'),
  'simpleSummary':summary,'whyCompare':why,'evidenceLimit':limit,'sourceExcerpt':excerpt,'priceStatus':price_status,'officialPriceScope':(official or {}).get('scope'),
  'metricHelp':{'tau':'TAU Banking is an independent benchmark for banking-agent tasks. Higher is better.','intel':'Intelligence Index combines several general capability tests. Higher is better.','speed':'Output tokens per second. Higher means faster generation in the retained benchmark setup.','price':'Token price per 1 million tokens. It excludes tools, retries, taxes and regional adjustments.'}
 }
 cards.append(card)

OUT.write_text(json.dumps({'generated_at':audit['generated_at'],'model_count':len(cards),'fx':manifest['fx'],'data_boundary':'Provider pages establish model identity. The retained benchmark snapshot supplies comparative metrics. Cards do not prove production suitability.','models':cards},indent=2,ensure_ascii=False))
html=html[:start]+json.dumps(cards,indent=2,ensure_ascii=False)+html[end:]

repls={
 '<a href="#models">37 Model Proofs</a>':'<a href="#models">40 Model Cards</a>',
 '<span>Model proof status: <strong>34 dual-source · 3 quarantined</strong></span>':'<span>Model proof status: <strong>37 provider + benchmark · 3 need more proof</strong></span>',
 '<div class="kpi green"><div class="num">34</div><div class="label">Provider + Benchmark Proof</div></div>':'<div class="kpi green"><div class="num">37</div><div class="label">Provider + Benchmark Proof</div></div>',
 '<!-- SECTION 7: CURATED 35 ENTERPRISE MODELS & TABBED PRICING MATRIX -->':'<!-- SECTION 7: 40 INTERACTIVE MODEL EVIDENCE CARDS -->',
 '<h2>Model Evidence Matrix — 37 Audited Rows</h2>':'<h2>40 Interactive Model Evidence Cards</h2>',
 f'<p class="muted">Each row exposes its provider proof, benchmark-snapshot match, metric discrepancies and decision-use status. INR values use the ECB {fx_date} reference cross-rate of ₹96.567636/USD. Cache discounts are excluded until exact SKU terms are verified.</p>':f'<p class="muted">Every card explains the model in simple words: what the numbers mean, why to compare it, what is proven, and what is still unknown. INR values use the ECB {fx_date} cross-rate of ₹{Decimal(manifest["fx"]["usd_to_inr"]).quantize(Decimal("0.000001"),ROUND_HALF_UP)}/USD.</p>',
 '<button class="proof-filter active" data-proof="all" type="button">All 37</button>':'<button class="proof-filter active" data-proof="all" type="button">All 40</button>',
 '<button class="proof-filter" data-proof="dual" type="button">Dual-source 34</button>':'<button class="proof-filter" data-proof="dual" type="button">Provider + benchmark 37</button>',
 '<button class="proof-filter" data-proof="quarantine" type="button">Quarantined 3</button>':'<button class="proof-filter" data-proof="quarantine" type="button">Needs more proof 3</button>'}
for old,new in repls.items():
 if old not in html: raise RuntimeError('missing text target: '+old)
 html=html.replace(old,new,1)

old_block='''      <div class="table-wrap" style="margin-top:32px; background:#1c1c1e; border-color:rgba(255,255,255,0.1);">
        <table>
          <thead style="background:rgba(255,255,255,0.03);">
            <tr><th>Model Name</th><th>Vendor</th><th>TAU Banking</th><th>Intel Index</th><th>Input / 1M (₹)</th><th>Output / 1M (₹)</th><th>Speed</th><th>Proof status</th></tr>
          </thead>
          <tbody id="modelsTableBody"></tbody>
        </table>
      </div>'''
new_block='''      <div class="model-card-toolbar">
        <label>Sort cards<select id="modelSort"><option value="intel">General score</option><option value="tau">Finance score</option><option value="speed">Speed</option><option value="price">Lowest input price</option><option value="name">Name</option></select></label>
        <span id="modelResultCount" aria-live="polite">40 models</span>
      </div>
      <div id="modelCardsGrid" class="model-cards-grid" aria-live="polite"></div>'''
if old_block not in html: raise RuntimeError('table block missing')
html=html.replace(old_block,new_block,1)

css='''
  .model-card-toolbar{display:flex;justify-content:space-between;align-items:end;gap:16px;margin:22px 0 14px}.model-card-toolbar label{display:grid;gap:6px;color:#86868b;font-size:12px}.model-card-toolbar select{background:#1c1c1e;color:#fff;border:1px solid #333336;border-radius:10px;padding:10px 34px 10px 12px}.model-card-toolbar span{font-size:13px;color:#86868b}.model-cards-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.model-card{display:flex;flex-direction:column;gap:18px;background:#1c1c1e;border:1px solid #333336;border-radius:16px;padding:24px;transition:transform .2s ease,border-color .2s ease}.model-card:hover{transform:translateY(-2px);border-color:#4b4b50}.model-card-head{display:flex;justify-content:space-between;gap:14px;align-items:flex-start}.model-card-vendor{font-size:11px;color:#86868b;text-transform:uppercase;letter-spacing:1px}.model-card h3{font-size:21px;margin:5px 0 0;color:#fff}.model-card-summary{color:#b0b0b5;font-size:14px;line-height:1.55}.model-metrics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.model-metric{background:#111;border:1px solid #2c2c2e;border-radius:11px;padding:12px;text-align:left;color:#fff;cursor:pointer}.model-metric:hover,.model-metric:focus-visible{border-color:#2997ff}.model-metric strong{display:block;font-size:18px}.model-metric span{display:block;color:#86868b;font-size:10px;margin-top:3px}.model-why{border-left:2px solid #2997ff;padding-left:12px;color:#d1d1d6;font-size:13px;line-height:1.5}.model-card-actions{display:flex;gap:10px;align-items:center;margin-top:auto}.model-detail-btn{flex:1;background:#0071e3;color:#fff;border:0;border-radius:10px;padding:11px 14px;font-weight:700;cursor:pointer}.model-detail-btn:hover{background:#147ce5}.model-price-note{font-size:10px;color:#86868b}.evidence-plain-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:18px 0}.evidence-plain-card{background:#111;border:1px solid #333336;border-radius:12px;padding:15px}.evidence-plain-card strong{display:block;color:#fff;margin-bottom:6px}.evidence-plain-card p{color:#b0b0b5;font-size:13px;line-height:1.5}.evidence-links{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0}.evidence-links a{color:#2997ff;border:1px solid rgba(41,151,255,.35);border-radius:9px;padding:8px 10px;text-decoration:none}.metric-focus{border-color:#2997ff!important}@media(max-width:768px){.model-cards-grid{grid-template-columns:1fr}.model-card-toolbar{align-items:stretch;flex-direction:column}.evidence-plain-grid{grid-template-columns:1fr}}
'''
html=html.replace('</style>',css+'</style>',1)

# Replace the table renderer with card rendering while retaining existing function name for compatibility.
pat=re.compile(r"    let activeProofFilter = 'all';.*?(?=    function renderCharts\(\))",re.S)
if not pat.search(html): raise RuntimeError('renderer block missing')
renderer='''    let activeProofFilter = 'all';
    function proofClass(m){ return m.decisionUse === 'quarantine' ? 'quarantine' : 'dual'; }
    function proofLabel(m){
      if(m.proofStatus === 'provider-family-documented-plus-benchmark-snapshot') return 'Provider + benchmark';
      if(m.proofStatus === 'provider-family-documented-only') return 'Provider only';
      if(m.proofStatus === 'benchmark-snapshot-only') return 'Benchmark only';
      return 'Not verified';
    }
    function displayMetric(value, digits=1){ return value === null || value === undefined || Number(value) === 0 ? 'Not available' : Number(value).toFixed(digits); }
    function renderModelsTable() {
      const input=(document.getElementById('modelSearchInput')?.value||'').toLowerCase().trim();
      const sort=document.getElementById('modelSort')?.value||'intel';
      let visible=models.filter(m=>(!input||`${m.name} ${m.vendor} ${m.simpleSummary}`.toLowerCase().includes(input))&&(activeProofFilter==='all'||(activeProofFilter==='dual'&&m.decisionUse!=='quarantine')||(activeProofFilter==='quarantine'&&m.decisionUse==='quarantine')));
      const numeric=(m,k)=>m[k]===null||m[k]===undefined?-Infinity:Number(m[k]);
      visible.sort((a,b)=>sort==='name'?a.name.localeCompare(b.name):sort==='price'?(numeric(a,'inInr')-numeric(b,'inInr')):(numeric(b,sort==='speed'?'tps':sort)-numeric(a,sort==='speed'?'tps':sort)));
      document.getElementById('modelResultCount').textContent=`${visible.length} of ${models.length} models`;
      document.getElementById('modelCardsGrid').innerHTML=visible.map(m=>{
        const tau=displayMetric(m.tau,4),intel=displayMetric(m.intel,1),speed=m.tps?`${Number(m.tps).toFixed(1)} tps`:'Not available';
        const inputPrice=m.inInr===null?'Not available':`₹${Number(m.inInr).toFixed(2)}`;
        return `<article class="model-card" data-proof="${proofClass(m)}">
          <div class="model-card-head"><div><div class="model-card-vendor">${m.vendor}</div><h3>${m.name}</h3></div><span class="proof-badge ${proofClass(m)}">${proofLabel(m)}</span></div>
          <p class="model-card-summary">${m.simpleSummary}</p>
          <div class="model-metrics">
            <button class="model-metric" type="button" onclick="openEvidenceModal('${m.id}','tau')"><strong>${tau}</strong><span>Finance score · higher is better</span></button>
            <button class="model-metric" type="button" onclick="openEvidenceModal('${m.id}','intel')"><strong>${intel}</strong><span>General score · higher is better</span></button>
            <button class="model-metric" type="button" onclick="openEvidenceModal('${m.id}','speed')"><strong>${speed}</strong><span>Generation speed</span></button>
            <button class="model-metric" type="button" onclick="openEvidenceModal('${m.id}','price')"><strong>${inputPrice}</strong><span>Input price / 1M tokens</span></button>
          </div>
          <p class="model-why"><strong>Why compare it:</strong> ${m.whyCompare}</p>
          <div class="model-card-actions"><button class="model-detail-btn" type="button" onclick="openEvidenceModal('${m.id}','overview')">Open simple evidence guide</button></div>
          <div class="model-price-note">${m.priceStatus}</div>
        </article>`;
      }).join('')||'<div class="card"><h4>No models match</h4><p class="muted">Change the search or proof filter.</p></div>';
    }

'''
html=pat.sub(lambda _:renderer,html,1)

# Replace evidence modal function with a simple-language detailed guide.
fn_pat=re.compile(r"    function openEvidenceModal\(modelId, metric\) \{.*?\n    \}\n    function closeEvidenceModal",re.S)
if not fn_pat.search(html): raise RuntimeError('evidence function missing')
fn='''    function openEvidenceModal(modelId, metric) {
      const m=models.find(x=>x.id===modelId); if(!m) return;
      lastEvidenceFocus=document.activeElement;
      document.getElementById('evModelName').textContent=m.name;
      document.getElementById('evMetricTitle').textContent=`${m.vendor} · ${proofLabel(m)}`;
      document.getElementById('evSimple').textContent=m.simpleSummary;
      document.getElementById('evWhy').textContent=m.whyCompare;
      document.getElementById('evPrice').textContent=`Input: ${m.inUsd===null?'not available':'$'+m.inUsd+'/1M'} (${m.inInr===null?'not available':'₹'+Number(m.inInr).toFixed(2)}) · Output: ${m.outUsd===null?'not available':'$'+m.outUsd+'/1M'} (${m.outInr===null?'not available':'₹'+Number(m.outInr).toFixed(2)}). ${m.priceStatus}.`;
      document.getElementById('evScores').textContent=`TAU Banking: ${displayMetric(m.tau,4)} · Intelligence Index: ${displayMetric(m.intel,1)} · Speed: ${m.tps?Number(m.tps).toFixed(1)+' output tokens/second':'not available'}.`;
      document.getElementById('evLimits').textContent=m.evidenceLimit;
      document.getElementById('evHelp').textContent=m.metricHelp[metric]||'This guide separates provider proof, benchmark data and open gaps.';
      const status=document.getElementById('evStatus');status.textContent=proofLabel(m);status.className=`status ${m.decisionUse==='quarantine'?'contradicted':'verified'}`;
      const link=document.getElementById('evSourceLink');link.href=m.sourceUrl||'#';link.textContent=m.sourceName||'Provider source unavailable';
      const priceLink=document.getElementById('evPricingLink');priceLink.hidden=!m.pricingSourceUrl;priceLink.href=m.pricingSourceUrl||'#';priceLink.textContent=m.pricingSourceUrl?'Official pricing source':'Pricing source unavailable';
      document.getElementById('evTimestamp').textContent=m.retrievalDate||'Not retrieved';
      document.getElementById('evSig').textContent=m.sourceSha256||'No retained provider-source hash';
      document.getElementById('evBenchmark').textContent=m.benchmarkExact?(m.benchmarkFresh?'Exact row in a freshly retrieved snapshot':'Exact row in the retained benchmark snapshot; fresh API refresh unavailable'):'No exact benchmark row in the retained snapshot';
      document.getElementById('evMetricCheck').textContent=m.metricMismatches.length?`Open metric gaps: ${m.metricMismatches.join(', ')}`:'Stored comparison values match the retained benchmark row within rounding tolerance';
      document.getElementById('evDecisionUse').textContent=m.decisionUse==='quarantine'?'Needs more proof — do not use this card alone for procurement or routing':'Can enter task-specific testing; not approved for production from this evidence alone';
      document.querySelectorAll('.evidence-plain-card').forEach(x=>x.classList.remove('metric-focus'));
      const focus=document.querySelector(`[data-evidence-topic="${metric}"]`);if(focus)focus.classList.add('metric-focus');
      const modal=document.getElementById('evidenceModal');modal.hidden=false;modal.querySelector('.evidence-dialog').focus();
    }
    function closeEvidenceModal'''
html=fn_pat.sub(lambda _:fn,html,1)
html=html.replace("      document.getElementById('modelSearchInput').addEventListener('input',renderModelsTable);","      document.getElementById('modelSearchInput').addEventListener('input',renderModelsTable);\n      document.getElementById('modelSort').addEventListener('change',renderModelsTable);",1)

modal_start='  <!-- MODEL EVIDENCE INSPECTOR -->';modal_end='\n</body>';a=html.index(modal_start);b=html.index(modal_end,a)
modal='''  <!-- MODEL EVIDENCE INSPECTOR -->
  <div id="evidenceModal" class="evidence-modal" hidden role="dialog" aria-modal="true" aria-labelledby="evModelName">
    <div class="evidence-dialog" tabindex="-1">
      <button id="evidenceClose" type="button" aria-label="Close evidence guide">Close</button>
      <span id="evStatus" class="status scoped">Evidence status</span>
      <h2 id="evModelName">Model evidence</h2>
      <p id="evMetricTitle" class="muted"></p>
      <div class="evidence-plain-grid">
        <section class="evidence-plain-card" data-evidence-topic="overview"><strong>What is this model?</strong><p id="evSimple"></p></section>
        <section class="evidence-plain-card" data-evidence-topic="overview"><strong>Why compare it?</strong><p id="evWhy"></p></section>
        <section class="evidence-plain-card" data-evidence-topic="price"><strong>What does it cost?</strong><p id="evPrice"></p></section>
        <section class="evidence-plain-card" data-evidence-topic="tau"><strong>What do the scores say?</strong><p id="evScores"></p></section>
        <section class="evidence-plain-card" data-evidence-topic="speed"><strong>How should I read this metric?</strong><p id="evHelp"></p></section>
        <section class="evidence-plain-card"><strong>What is not proven?</strong><p id="evLimits"></p></section>
      </div>
      <div class="evidence-links"><a id="evSourceLink" href="#" target="_blank" rel="noopener">Official provider source</a><a id="evPricingLink" href="#" target="_blank" rel="noopener">Official pricing source</a></div>
      <dl class="evidence-list">
        <div><dt>Retrieved</dt><dd id="evTimestamp">—</dd></div>
        <div><dt>Provider snapshot SHA-256</dt><dd id="evSig">—</dd></div>
        <div><dt>Independent benchmark</dt><dd id="evBenchmark">—</dd></div>
        <div><dt>Metric check</dt><dd id="evMetricCheck">—</dd></div>
        <div><dt>Decision use</dt><dd id="evDecisionUse">—</dd></div>
        <div><dt>FX basis</dt><dd>ECB '''+fx_date+''': ₹'''+str(Decimal(manifest['fx']['usd_to_inr']).quantize(Decimal('0.000001'),ROUND_HALF_UP))+'''/USD</dd></div>
      </dl>
    </div>
  </div>'''
html=html[:a]+modal+html[b:]
HTML.write_text(html)
print(json.dumps({'models':len(cards),'data_file':str(OUT),'archive':str(archive),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'html_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest()},indent=2))
