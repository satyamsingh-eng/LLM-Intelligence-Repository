from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime, timezone
import json, shutil, hashlib

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'; CARDS=ROOT/'models/section7_model_cards.json'; AA=ROOT/'models/artificial_analysis_live_dataset.json'; MANIFEST=ROOT/'local_knowledge_repository/official_source_manifest.json'; OUT=ROOT/'models/uncanny_valley_routing.json'
fx=Decimal(json.loads(CARDS.read_text())['fx']['usd_to_inr'])
def inr(v): return str((Decimal(str(v))*fx).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
models=json.loads(CARDS.read_text())['models']
def card(name): return next(x for x in models if x['name']==name)
kimi=card('Kimi K3'); router=card('Gemini 3.5 Flash-Lite'); vision=card('Gemini 3.6 Flash')
aa=json.loads(AA.read_text()); rows=aa if isinstance(aa,list) else aa.get('data',aa.get('models',[]))
ds=[x for x in rows if x.get('name','').startswith('DeepSeek V4 Pro')]
manifest=json.loads(MANIFEST.read_text()); ds_source=next(x for x in manifest['sources'] if x['id']=='deepseek_models_pricing')

def aa_eval(row,key): return (row.get('evaluations') or {}).get(key)
def vals(key): return [float(v) for v in (aa_eval(x,key) for x in ds) if v not in (None,0)]
def rng(v,d):
 lo,hi=min(v),max(v);return f'{lo:.{d}f}' if lo==hi else f'{lo:.{d}f}–{hi:.{d}f}'

data={
 'generated_at':datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
 'architecture':'Two-stage core with two conditional gates',
 'fx':{'usd_to_inr':str(fx),'reference_date':'2026-07-24','source':'ECB reference cross-rate'},
 'governance':'Material tax, compliance and portfolio actions require deterministic validation and human approval after the model route.',
 'roles':[
  {'id':'brain','number':1,'nickname':'The Brain','kind':'Core stage 2','model':'Kimi K3','vendor':'Moonshot AI','role':'Produces the final tax-analysis draft, portfolio-rebalancing rationale and compliance-check proposal.','why':f"Its TAU Banking result is {kimi['tauDisplay']}, the highest value in this report’s retained 40-configuration comparison set. This is a shortlist signal, not proof of production accuracy.",'tradeoff':f"Retained generation speed is {kimi['speedDisplay']}. Async execution reduces UI blocking, but queue capacity, timeouts and fallback behavior still need testing.",'metrics':[{'label':'TAU Banking','value':kimi['tauDisplay'],'scope':'Retained independent snapshot'},{'label':'Speed','value':kimi['speedDisplay'],'scope':'Retained independent snapshot'},{'label':'Input / 1M','value':kimi['inputPriceDisplay'],'scope':kimi['priceStatus']}],'status':'Task testing required','sourceUrl':kimi['sourceUrl'],'benchmarkUrl':'https://artificialanalysis.ai/models'},
  {'id':'reader','number':2,'nickname':'The Reader','kind':'Core stage 1','model':'DeepSeek V4 Pro','vendor':'DeepSeek','role':'Processes large text-based PDFs and produces structured candidate facts before financial reasoning.','why':f"The official rate card lists ${Decimal('0.435')}/1M cache-miss input ({chr(8377)}{inr('0.435')}), ${Decimal('0.003625')}/1M cache-hit input ({chr(8377)}{inr('0.003625')}) and ${Decimal('0.87')}/1M output ({chr(8377)}{inr('0.87')}). It also lists JSON output, tool calls and a 1M context window.",'tradeoff':'The retrieved provider page does not establish native image/OCR input. Image pages therefore go through the Vision Gate until exact OCR support and accuracy are proven. Cache-hit pricing applies only when the provider cache actually hits.','metrics':[{'label':'TAU Banking range','value':rng(vals('tau_banking'),4),'scope':'Retained independent configurations'},{'label':'General score range','value':rng(vals('artificial_analysis_intelligence_index'),1),'scope':'Retained independent configurations'},{'label':'Cache-miss input / 1M','value':f"₹{inr('0.435')}",'scope':'Official DeepSeek rate card'}],'status':'Official SKU and price verified; task quality unproven','sourceUrl':ds_source['final_url'],'benchmarkUrl':'https://artificialanalysis.ai/models/deepseek-v4-pro'},
  {'id':'router','number':3,'nickname':'The Router','kind':'Conditional gate','model':'Gemini 3.5 Flash-Lite','vendor':'Google','role':'Classifies the file type, identifies the requested workflow and routes the job before expensive processing begins.','why':f"Google describes it as its fastest, most cost-effective 3.5 model for high-throughput execution. The retained snapshot reports {router['speedDisplay']}; its verified input rate is {router['inputPriceDisplay']}/1M.",'tradeoff':'Use it for routing and low-risk extraction checks—not final tax calculations. Incorrect routing must fall back to review rather than silently continuing.','metrics':[{'label':'Speed','value':router['speedDisplay'],'scope':'Retained independent snapshot'},{'label':'Input / 1M','value':router['inputPriceDisplay'],'scope':'Verified official rate card'},{'label':'TAU Banking','value':router['tauDisplay'],'scope':'Retained independent snapshot'}],'status':'Conditional gate; task testing required','sourceUrl':router['sourceUrl'],'benchmarkUrl':'https://artificialanalysis.ai/models'},
  {'id':'vision','number':4,'nickname':'The Vision Gate','kind':'Conditional gate','model':'Gemini 3.6 Flash','vendor':'Google','role':'Handles scanned pages, charts and image-based document pages before passing extracted text to the Reader.','why':f"Google’s model page describes Gemini 3.6 Flash as supporting agentic and multimodal tasks. The retained snapshot reports {vision['speedDisplay']}.",'tradeoff':'“Multimodal” does not prove financial-document OCR accuracy. Validate tables, decimal placement, signatures and low-quality scans against a labelled test set; escalate low-confidence pages to a human.','metrics':[{'label':'Speed','value':vision['speedDisplay'],'scope':'Retained independent snapshot'},{'label':'General score','value':vision['intelDisplay'],'scope':'Retained independent snapshot'},{'label':'Price','value':'Exact SKU rate not established','scope':vision['priceStatus']}],'status':'Multimodal identity verified; OCR accuracy unproven','sourceUrl':vision['sourceUrl'],'benchmarkUrl':'https://artificialanalysis.ai/models'}
 ],
 'routes':[
  {'id':'text','label':'Text PDF','stages':['router','reader','brain','human'],'summary':'Classify the job, extract text at scale, run financial reasoning, then require approval for material action.'},
  {'id':'scan','label':'Scanned / Image PDF','stages':['router','vision','reader','brain','human'],'summary':'Add the Vision Gate before text extraction. Low-confidence pages stop for review instead of flowing into tax logic.'},
  {'id':'structured','label':'Structured Tax Data','stages':['router','brain','human'],'summary':'Skip document extraction when validated structured data already exists. The Brain drafts the result; deterministic checks and human approval remain.'}
 ],
 'qa_corrections':[
  'Replaced “#1 global” with “highest in this retained 40-configuration comparison set.”',
  'Removed the unsupported percentage-based accuracy trade-off statement.',
  f"Corrected DeepSeek V4 Pro cache-hit input from ₹4.20 to ₹{inr('0.003625')} per 1M using the official $0.003625 rate.",
  'Reframed native OCR as not established by the retrieved provider page, rather than claiming an absolute capability absence.',
  'Kept the core as two stages; the two added models are conditional gates and are not invoked for every job.'
 ]
}
OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False))
html=HTML.read_text();archive=ROOT/'audit/archive'/f'index-pre-four-role-routing-{datetime.now().strftime("%Y%m%d-%H%M%S")}.html';shutil.copy2(HTML,archive)
start=html.index('      <div class="card" style="margin-top:40px;',html.index('id="routing-capability"'))
end=html.index('\n    </div>\n  </div>\n  <!-- SECTION 2',start)
old=html[start:end]
new='''      <div class="uncanny-shell">
        <div class="uncanny-heading"><div><span class="architecture-eyebrow">Routing architecture</span><h3>The "Uncanny Valley" of Foundation Models</h3></div><span class="architecture-badge">2-stage core + 2 conditional gates</span></div>
        <p class="uncanny-lead">Large async workflows should not send every page and every decision to one model. Premium reasoning on raw extraction wastes money; cheap untested reasoning can create material tax and compliance risk. SARVAX therefore separates intake, vision, text extraction and financial reasoning.</p>
        <div class="architecture-decision"><strong>Recommendation for evaluation:</strong> Keep the Reader → Brain core. Invoke the Router for intake and the Vision Gate only when the document needs it. Deterministic validation and human approval remain outside the model chain.</div>
        <div class="route-mode-controls" role="group" aria-label="Choose an example document route">
          <button type="button" class="route-mode" data-route-mode="text">Text PDF</button>
          <button type="button" class="route-mode active" data-route-mode="scan">Scanned / Image PDF</button>
          <button type="button" class="route-mode" data-route-mode="structured">Structured Tax Data</button>
        </div>
        <div id="uncannyRouteFlow" class="uncanny-route-flow" aria-live="polite"></div>
        <p id="uncannyRouteSummary" class="uncanny-route-summary"></p>
        <div id="uncannyRoleGrid" class="uncanny-role-grid"></div>
        <details class="architecture-qa"><summary>Evidence boundaries and QA corrections</summary><ul id="uncannyQaList"></ul></details>
      </div>'''
html=html[:start]+new+html[end:]
# CSS: flat design, responsive controls and cards.
css='''
.uncanny-shell{margin-top:40px;padding:34px;background:#1c1c1e;border:1px solid #333336;border-radius:16px}.uncanny-heading{display:flex;justify-content:space-between;gap:18px;align-items:flex-start}.uncanny-heading h3{font-size:26px;color:#fff;margin:6px 0 0}.architecture-eyebrow{color:#0071e3;font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase}.architecture-badge{white-space:nowrap;border:1px solid #333336;border-radius:999px;padding:8px 12px;color:#d1d1d6;font-size:12px}.uncanny-lead{color:#a1a1a6;font-size:15px;line-height:1.65;margin:22px 0}.architecture-decision{background:#111;border:1px solid #333336;border-left:3px solid #0071e3;border-radius:12px;padding:16px;color:#d1d1d6;font-size:14px;line-height:1.55}.route-mode-controls{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0 14px}.route-mode{border:1px solid #3a3a3c;background:#242426;color:#a1a1a6;border-radius:999px;padding:10px 15px;font:inherit;cursor:pointer}.route-mode:hover,.route-mode:focus-visible{border-color:#0071e3;color:#fff}.route-mode.active{background:#0071e3;border-color:#0071e3;color:#fff}.uncanny-route-flow{display:flex;align-items:center;gap:8px;overflow-x:auto;padding:14px;background:#0b0b0c;border:1px solid #2c2c2e;border-radius:12px}.route-node{min-width:140px;border:1px solid #333336;border-radius:10px;padding:12px;background:#171719}.route-node strong{display:block;color:#fff;font-size:13px}.route-node span{display:block;color:#86868b;font-size:11px;margin-top:4px}.route-node.human{border-color:#ff9f0a}.route-arrow{color:#636366;font-weight:700}.uncanny-route-summary{color:#86868b;font-size:13px;line-height:1.55;margin:10px 0 24px}.uncanny-role-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.uncanny-role-card{background:#0b0b0c;border:1px solid #333336;border-radius:14px;padding:20px;display:flex;flex-direction:column;gap:14px}.uncanny-role-top{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}.uncanny-role-top h4{font-size:18px;color:#fff;margin:0}.uncanny-role-kind{font-size:10px;text-transform:uppercase;letter-spacing:.1em;color:#0071e3;border:1px solid #164f7d;border-radius:999px;padding:5px 8px}.uncanny-model-name{font-size:24px;font-weight:750;color:#fff}.uncanny-model-name span{font-size:12px;color:#86868b;font-weight:600}.uncanny-role-copy{display:grid;gap:9px;color:#a1a1a6;font-size:13px;line-height:1.55}.uncanny-role-copy strong{color:#f5f5f7}.uncanny-mini-metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.uncanny-mini-metric{background:#151516;border:1px solid #2c2c2e;border-radius:9px;padding:10px}.uncanny-mini-metric strong{display:block;color:#fff;font-size:14px}.uncanny-mini-metric span{display:block;color:#7d7d82;font-size:9px;line-height:1.35;margin-top:4px}.uncanny-evidence-row{display:flex;justify-content:space-between;gap:12px;align-items:center;margin-top:auto;padding-top:8px;border-top:1px solid #2c2c2e}.uncanny-evidence-row .status-text{color:#ff9f0a;font-size:10px}.uncanny-evidence-row a{color:#2997ff;font-size:11px;text-decoration:none}.architecture-qa{margin-top:18px;border:1px solid #333336;border-radius:12px;padding:14px 16px;background:#151516}.architecture-qa summary{cursor:pointer;color:#f5f5f7;font-weight:650}.architecture-qa ul{color:#a1a1a6;font-size:12px;line-height:1.6;margin:12px 0 0;padding-left:18px}@media(max-width:760px){.uncanny-shell{padding:20px}.uncanny-heading{flex-direction:column}.architecture-badge{white-space:normal}.uncanny-role-grid{grid-template-columns:1fr}.uncanny-mini-metrics{grid-template-columns:1fr}.route-mode{flex:1 1 100%}.uncanny-route-flow{flex-direction:column;align-items:stretch;overflow-x:visible}.route-node{min-width:0;width:100%}.route-arrow{align-self:center;transform:rotate(90deg)}.uncanny-evidence-row{flex-direction:column;align-items:flex-start}.uncanny-role-kind{max-width:120px;text-align:center}}
'''
html=html.replace('</style>',css+'</style>',1)
# Embed the central architecture data before model data.
anchor='    const models = '
html=html.replace(anchor,'    const routingArchitecture = '+json.dumps(data,ensure_ascii=False)+';\n\n'+anchor,1)
js='''
    function renderUncannyArchitecture(routeId='scan') {
      const route=routingArchitecture.routes.find(r=>r.id===routeId)||routingArchitecture.routes[0];
      document.querySelectorAll('.route-mode').forEach(b=>{const on=b.dataset.routeMode===route.id;b.classList.toggle('active',on);b.setAttribute('aria-pressed',String(on));});
      const byId=Object.fromEntries(routingArchitecture.roles.map(r=>[r.id,r]));
      document.getElementById('uncannyRouteFlow').innerHTML=route.stages.map((id,i)=>{const r=byId[id];const node=r?`<div class="route-node"><strong>${r.nickname}</strong><span>${r.model}</span></div>`:`<div class="route-node human"><strong>Human approval</strong><span>Material financial action</span></div>`;return (i?'<span class="route-arrow" aria-hidden="true">→</span>':'')+node;}).join('');
      document.getElementById('uncannyRouteSummary').textContent=route.summary;
    }
    function initUncannyArchitecture(){
      document.getElementById('uncannyRoleGrid').innerHTML=routingArchitecture.roles.map(r=>`<article class="uncanny-role-card"><div class="uncanny-role-top"><h4>${r.number}. ${r.nickname}</h4><span class="uncanny-role-kind">${r.kind}</span></div><div class="uncanny-model-name">${r.model} <span>${r.vendor}</span></div><div class="uncanny-role-copy"><p><strong>Role:</strong> ${r.role}</p><p><strong>Why:</strong> ${r.why}</p><p><strong>Trade-off:</strong> ${r.tradeoff}</p></div><div class="uncanny-mini-metrics">${r.metrics.map(m=>`<div class="uncanny-mini-metric"><strong>${m.value}</strong><span>${m.label}<br>${m.scope}</span></div>`).join('')}</div><div class="uncanny-evidence-row"><span class="status-text">${r.status}</span><span><a href="${r.sourceUrl}" target="_blank" rel="noopener">Provider proof</a> · <a href="${r.benchmarkUrl}" target="_blank" rel="noopener">Benchmark</a></span></div></article>`).join('');
      document.getElementById('uncannyQaList').innerHTML=routingArchitecture.qa_corrections.map(x=>`<li>${x}</li>`).join('');
      document.querySelectorAll('.route-mode').forEach(b=>b.addEventListener('click',()=>renderUncannyArchitecture(b.dataset.routeMode)));
      renderUncannyArchitecture('scan');
    }
'''
html=html.replace('    let activeProofFilter =',js+'\n    let activeProofFilter =',1)
html=html.replace('      populateSelects();','      initUncannyArchitecture();\n      populateSelects();',1)
HTML.write_text(html)
print(json.dumps({'roles':len(data['roles']),'routes':len(data['routes']),'added_models':['Gemini 3.5 Flash-Lite','Gemini 3.6 Flash'],'deepseek_official_sha256':ds_source['sha256'],'corrected_cache_hit_inr':inr('0.003625'),'archive':str(archive),'html_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest()},indent=2))
