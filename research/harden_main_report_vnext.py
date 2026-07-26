from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP, getcontext
from datetime import datetime, timezone
import json, re, hashlib, shutil

getcontext().prec=40
ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'
CARDS=ROOT/'models/section7_model_cards.json'
ROUTING=ROOT/'models/uncanny_valley_routing.json'
CALCULATOR=ROOT/'models/calculator_scenarios.json'
MANIFEST=ROOT/'local_knowledge_repository/official_source_manifest.json'
RUNTIME=ROOT/'models'/'executive_report_runtime.json'
RUNTIME_JS=ROOT/'models'/'executive_report_runtime.js'

cards_doc=json.loads(CARDS.read_text())
models=cards_doc['models']
routing=json.loads(ROUTING.read_text())
calculator_config=json.loads(CALCULATOR.read_text())
manifest=json.loads(MANIFEST.read_text())
fx=Decimal(manifest['fx']['usd_to_inr'])

def inr(usd):
    return str((Decimal(str(usd))*fx).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))

pricing=[]
for source_rate in calculator_config['pricing_catalog']:
    rate=dict(source_rate)
    rate['input_inr']=inr(rate['input_usd'])
    rate['output_inr']=inr(rate['output_usd'])
    if rate.get('cache_read_usd') is not None:
        rate['cache_read_inr']=inr(rate['cache_read_usd'])
    if rate.get('pricing_tiers'):
        rate['pricing_tiers']=[dict(t,input_inr=inr(t['input_usd']),output_inr=inr(t['output_usd'])) for t in rate['pricing_tiers']]
    pricing.append(rate)
calculator={k:v for k,v in calculator_config.items() if k!='pricing_catalog'}
calculator['pricing_catalog']=pricing

workflows={
 'relationship':{
  'name':'Client Relationship Intelligence',
  'classification':'Governance and approval scenario — not production telemetry',
  'description':'From permitted client context to advisor-approved follow-up and controlled system writeback.',
  'decision':'Can SARVAX preserve evidence, ownership and human decision rights across the complete meeting journey?',
  'verdict':'Product orchestration is represented; connector execution, persistence, retry behavior and production reliability remain unverified.',
  'release_gap':'Connector execution, persistence, retry behavior and production reliability are not yet proven with representative backend traces.',
  'exit_gate':'Release only after consent, tenant isolation, source lineage, approval and writeback controls pass representative trace tests.',
  'owners':{'product':'Meeting Assistant + Workflow 2.0','deterministic':'Policy, authorization and write-integrity services','human':'Named advisor'},
  'steps':[
   {'name':'Permitted client-context intake','type':'product','desc':'Calendar, CRM and approved communication context are collected before preparation.','control':'Required: consent, tenant access, source timestamps and retention policy.'},
   {'name':'Pre-Meeting Analysis Agent','type':'agent','desc':'Drafts a source-linked preparation brief and explicit data gaps.','control':'Required: unsupported client facts blocked; every material claim links to retained evidence.'},
   {'name':'Meeting capture and artifact finalization','type':'product','desc':'Meeting Assistant creates the permitted transcript and meeting artifacts.','control':'Required: participant consent, speaker attribution review and artifact access policy.'},
   {'name':'Post-Meeting Analysis Agent','type':'agent','desc':'Drafts facts, decisions, risks and action items from the retained artifact.','control':'Required: transcript facts remain separate from model interpretation.'},
   {'name':'Client Intelligence Strategist','type':'agent','desc':'Drafts next-best-action options for advisor review.','control':'Required: no autonomous product recommendation, promise or client communication.'},
   {'name':'Advisor decision gate','type':'human','desc':'The named advisor accepts, edits or rejects facts and proposed actions.','control':'Required before any client communication or material CRM/task update.'},
   {'name':'Controlled Workflow 2.0 writeback','type':'tool','desc':'Only approved records are submitted to authorized connected systems.','control':'Release evidence required: idempotency key, immutable audit event, retry/dead-letter policy and compensating action.'}
  ]
 },
 'portfolio':{
  'name':'Portfolio & Market Intelligence',
  'classification':'Governance and approval scenario — not production telemetry',
  'description':'From holdings evidence to deterministic calculations, advisor review and approved system updates.',
  'decision':'Can model-generated observations remain subordinate to exact financial calculations and advisor suitability decisions?',
  'verdict':'The control placement is a target design. Connector coverage, calculation parity and order-system writeback are not production-proven.',
  'release_gap':'Connector coverage, calculation parity and order-system writeback are not yet proven with representative traces.',
  'exit_gate':'Release only after as-of controls, Decimal-oracle parity, suitability approval and writeback authorization pass representative cases.',
  'owners':{'product':'Portfolio + Market Intelligence agents','deterministic':'Data-quality and finance engines','human':'Named advisor'},
  'steps':[
   {'name':'Holdings and market-evidence intake','type':'product','desc':'Approved connectors, OneChat artifacts or uploaded evidence enter with source metadata.','control':'Required: connector identity, as-of timestamp, currency and data lineage.'},
   {'name':'Deterministic intake gate','type':'deterministic','desc':'Schema, completeness, duplicates, stale values and authorization are checked.','control':'Blocked inputs cannot proceed; every exception receives an owner and reason.'},
   {'name':'Bounded context normalization','type':'model','desc':'Extraction links narrative context to retained evidence without changing numeric holdings.','control':'Image-origin evidence uses a separately validated OCR/vision route only when required.'},
   {'name':'Market Intelligence Agent','type':'agent','desc':'Drafts time-stamped event and market-context observations.','control':'Required: public/source references and explicit freshness on every material claim.'},
   {'name':'Portfolio Analyst','type':'agent','desc':'Drafts allocation, concentration and risk observations.','control':'Narrative generation cannot alter holdings, prices, tax lots or computed values.'},
   {'name':'Deterministic finance and policy gate','type':'deterministic','desc':'Versioned Decimal services calculate returns, allocation, tax lots and policy checks.','control':'Required: formula version, input hash, regression fixture and materiality threshold.'},
   {'name':'Advisor suitability gate','type':'human','desc':'The named advisor accepts, edits or rejects the analysis and proposed action.','control':'Mandatory before client delivery, order staging or material record update.'},
   {'name':'Authorized writeback','type':'tool','desc':'Approved artifacts and tasks are submitted to authorized connected systems.','control':'Release evidence required: authorization, idempotency, immutable audit log and compensating action.'}
  ]
 },
 'operations':{
  'name':'Compliance & Advisor Operations',
  'classification':'Governance and approval scenario — not production telemetry',
  'description':'From case intake to evidence validation, policy gates, named review and controlled writeback.',
  'decision':'Can operational agents accelerate review without becoming final KYC, compliance or enforcement decision-makers?',
  'verdict':'The sequence is a target control design. Sanctions-source coverage, backend enforcement and connector execution remain unverified.',
  'release_gap':'Sanctions-source coverage, backend enforcement and connector execution are not yet proven with material edge-case traces.',
  'exit_gate':'Release only after identity, evidence, sanctions, authorization, reviewer and writeback tests pass material edge cases.',
  'owners':{'product':'KYC, document and operations agents','deterministic':'Identity, sanctions, schema and authorization gates','human':'Named compliance reviewer'},
  'steps':[
   {'name':'Case and evidence intake','type':'product','desc':'Connected systems, tasks, messages and client evidence enter with source metadata.','control':'Required: case identity, consent, source integrity and tenant boundary.'},
   {'name':'Deterministic identity and access gate','type':'deterministic','desc':'Identity, tenant, consent, schema and authorization are verified before model processing.','control':'Missing or conflicting controls block the case and create a review reason.'},
   {'name':'KYC and document intelligence','type':'agent','desc':'KYC Officer, KYC/CDD QA and Document Intelligence prepare review evidence.','control':'Required: field-level extraction confidence, source link and unresolved-field list.'},
   {'name':'Deterministic evidence and policy gate','type':'deterministic','desc':'Schema, sanctions-source results, policy rules and exceptions are evaluated.','control':'Models cannot override failed checks, missing evidence or reviewer-required cases.'},
   {'name':'Bounded operations agent group','type':'agent','desc':'Cadence, campaign, pipeline and workload agents prepare owned follow-up work.','control':'Every proposed action requires owner, due date, metric and dependency.'},
   {'name':'Named human review gate','type':'human','desc':'The authorized reviewer accepts, rejects or returns the case with a reason.','control':'Mandatory for material decisions, outbound actions and unresolved evidence.'},
   {'name':'Controlled notifications and writeback','type':'tool','desc':'Only approved state is submitted to tasks and authorized connected systems.','control':'Release evidence required: audit ID, retry/dead-letter policy, deduplication and compensating action.'}
  ]
 }
}

proof_counts={
 'provider_plus_benchmark':sum(m['proofStatus']=='provider-family-documented-plus-benchmark-snapshot' for m in models),
 'provider_only':sum(m['proofStatus']=='provider-family-documented-only' for m in models),
 'benchmark_only':sum(m['proofStatus']=='benchmark-snapshot-only' for m in models),
}
chart_data={
 'intelligence':sorted([{'name':m['name'],'value':m['sortIntel']} for m in models if m.get('sortIntel')],key=lambda x:x['value'],reverse=True)[:15],
 'tau_banking':sorted([{'name':m['name'],'value':m['sortTau']} for m in models if m.get('sortTau')],key=lambda x:x['value'],reverse=True)[:15],
 'evidence_coverage':[{'name':'Provider + benchmark','value':proof_counts['provider_plus_benchmark']},{'name':'Provider only','value':proof_counts['provider_only']},{'name':'Benchmark only','value':proof_counts['benchmark_only']}],
 'verified_pricing':[{'name':p.get('chart_label',p['name']),'input_inr':p['input_inr'],'output_inr':p['output_inr']} for p in pricing],
}
runtime={'metadata':{'generated_at':datetime.now(timezone.utc).replace(microsecond=0).isoformat(),'status':'evidence-scoped','models':len(models),'unique_model_cards':len(models),'benchmark_configurations':cards_doc['benchmark_configuration_count'],'usable_sources':sum(bool(s.get('usable')) for s in manifest['sources']),'active_benchmark_snapshot_rows':586,'active_benchmark_snapshot_file':'models/artificial_analysis_live_dataset.json','product_snapshot_branch_status':'unverified-no-git-metadata'},'fx':{'usd_to_inr':str(fx),'reference_date':manifest['fx']['ecb_reference_date'],'formula':manifest['fx']['formula'],'source_id':'ecb_fx','corroborating_market_rate':'96.61382','corroborating_rate_timestamp':'2026-07-25T00:02:32Z','corroborating_source':'https://open.er-api.com/v6/latest/USD'},'models':models,'routing':routing,'pricing_catalog':pricing,'calculator':calculator,'workflow_player':workflows,'chart_data':chart_data,'chart_boundaries':{'intelligence':'Highest retained Intelligence Index configuration per model; retained snapshot, not current production validation.','tau_banking':'Highest retained TAU Banking configuration per model; higher is better; retained snapshot.','pricing':'Exact public standard-token rates converted with the retained ECB FX. Qwen uses the ≤256K input tier in this chart; the calculator applies its higher verified tier above 256K.','evidence':'Counts unique model cards by provider/benchmark proof type.'}}
RUNTIME.write_text(json.dumps(runtime,indent=2,ensure_ascii=False))
RUNTIME_JS.write_text('window.SARVAX_REPORT_RUNTIME='+json.dumps(runtime,ensure_ascii=False,separators=(',',':'))+';\n')

text=HTML.read_text()
if '    const routingArchitecture =' not in text:
    print(json.dumps({'mode':'runtime-refresh-only','runtime':str(RUNTIME.relative_to(ROOT)),'runtime_js':str(RUNTIME_JS.relative_to(ROOT)),'runtime_sha256':hashlib.sha256(RUNTIME.read_bytes()).hexdigest(),'runtime_js_sha256':hashlib.sha256(RUNTIME_JS.read_bytes()).hexdigest(),'html_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest(),'models':len(models),'configs':cards_doc['benchmark_configuration_count'],'exact_pricing_models':len(pricing),'workflow_scenarios':len(workflows)},indent=2))
    raise SystemExit(0)
backup=ROOT/'audit'/'archive'/f"index-pre-vnext-hardening-{datetime.now().strftime('%Y%m%d-%H%M%S')}.html"
backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(HTML,backup)

def replace_segment(text,start,end,new):
    a=text.index(start);b=text.index(end,a)
    return text[:a]+new+'\n\n  '+text[b:]

section2='''<!-- SECTION 2: PRODUCT-MAPPED WEALTH ADVISORY OPERATING MATRIX -->
  <div class="section-dark" id="wealth-use-cases">
    <div class="section">
      <div class="section-label">Section 2</div>
      <h2>SARVAX Wealth-Advisory Agent Operating Matrix</h2>
      <p class="muted">Twelve product agents mapped across three advisor journeys. No invented time-saved, accuracy, SLA or unit-economics claims are shown. Economics stay in the scenario calculator until measured traces exist.</p>
      <div class="route-mode-controls" role="group" aria-label="Filter wealth-advisory agent journeys">
        <button type="button" class="usecase-filter active" data-journey-filter="all">All journeys</button>
        <button type="button" class="usecase-filter" data-journey-filter="relationship">Client Relationship</button>
        <button type="button" class="usecase-filter" data-journey-filter="portfolio">Portfolio &amp; Market</button>
        <button type="button" class="usecase-filter" data-journey-filter="operations">Compliance &amp; Operations</button>
      </div>
      <div id="wealthJourneyGrid" class="usecase-grid" style="display:grid;grid-template-columns:1fr;gap:16px;margin-top:24px" aria-live="polite"></div>
    </div>
  </div>'''
text=replace_segment(text,'<!-- SECTION 2:','<!-- SECTION 3:',section2)

section3='''<!-- SECTION 3: EVIDENCE-BOUND PRICE SCENARIO CALCULATOR -->
  <div class="section-dark" id="simulator" style="border-top:1px solid #333336">
    <div class="section-inner">
      <div class="section-label">Section 3</div>
      <h2>Verified-Rate Scenario Calculator (INR ₹)</h2>
      <p class="muted">Exact Decimal arithmetic using the latest ECB business-day USD/INR cross-rate and four exact official SKU rate cards. Token volumes and monthly runs are editable planning assumptions—not production measurements.</p>
      <div class="architecture-decision" style="margin-top:20px"><strong>Formula:</strong> ((input tokens × input USD/1M) + (output tokens × output USD/1M)) × USD/INR. No cache, batch, retry, tool or platform charges are assumed.</div>
      <div class="card-grid" style="grid-template-columns:1fr 1fr;gap:24px;margin-top:24px">
        <div class="card" style="background:#1c1c1e;color:#fff;border:1px solid #333336;border-radius:16px;padding:24px">
          <h4 style="color:#0071e3;margin-top:0">Planning inputs</h4>
          <label class="control-label">Scenario preset<select id="simPreset" onchange="applyPreset()"><option value="relationship">Client Relationship (20k in / 2k out)</option><option value="portfolio" selected>Portfolio Review (75k in / 8k out)</option><option value="operations">Compliance Case (50k in / 4k out)</option></select></label>
          <div class="sim-model-grid"><label class="control-label">Model A — verified rate<select id="simModelA" onchange="runSim()"></select></label><label class="control-label">Model B — verified rate<select id="simModelB" onchange="runSim()"></select></label></div>
          <label class="range-label"><span>Input tokens per run</span><strong id="inTokLabel">75,000</strong><input type="range" id="simInTok" min="5000" max="300000" step="5000" value="75000" oninput="updateLabels();runSim()"></label>
          <label class="range-label"><span>Output tokens per run</span><strong id="outTokLabel">8,000</strong><input type="range" id="simOutTok" min="500" max="50000" step="500" value="8000" oninput="updateLabels();runSim()"></label>
          <label class="range-label"><span>Monthly execution volume</span><strong id="runsLabel">10,000 runs</strong><input type="range" id="simRuns" min="100" max="100000" step="100" value="10000" oninput="updateLabels();runSim()"></label>
          <p id="fxBasis" class="muted" style="margin-top:16px"></p>
        </div>
        <div style="display:flex;flex-direction:column;gap:16px">
          <div class="card" style="background:#1c1c1e;color:#fff;border:1px solid #333336;border-radius:16px;padding:24px"><h4 style="color:#30d158;margin-top:0">Calculated standard-token cost</h4><div class="sim-results"><article><strong id="nameA">Model A</strong><span>Per run</span><b id="costA">₹0.00</b><span>Monthly</span><b id="lakhsA">₹0.0000 Lakhs</b></article><article><strong id="nameB">Model B</strong><span>Per run</span><b id="costB">₹0.00</b><span>Monthly</span><b id="lakhsB">₹0.0000 Lakhs</b></article></div></div>
          <div class="card" style="background:#000;border:1px solid #0071e3;border-radius:16px;padding:24px"><div class="section-label">Calculated price difference</div><div id="savingsText" style="font-size:32px;font-weight:800;color:#fff;margin:8px 0">₹0.0000 Lakhs / month</div><p id="savingsDesc" class="muted"></p><div class="sim-difference"><div><span>Annualized difference</span><strong id="annualSavings">₹0.0000 Lakhs/year</strong></div><div><span>Model A per 1,000 runs</span><strong id="costPerThousand">₹0.00</strong></div></div></div>
        </div>
      </div>
    </div>
  </div>'''
text=replace_segment(text,'<!-- SECTION 3:','<!-- SECTION 4:',section3)

section4='''<!-- SECTION 4: CONTROL-FLOW DAG PLAYER -->
  <div class="section-dark" id="workflows">
    <div class="section">
      <div class="section-label">Section 4</div>
      <h2>SARVAX Workflow Control-Flow Player</h2>
      <p class="muted">A simulated playback of product stages, deterministic controls, human approval and writeback. Cost, tokens, latency, retries and SLAs are explicitly not measured.</p>
      <div class="card" style="margin-top:24px;padding:24px;background:#1c1c1e;border:1px solid #333336;border-radius:16px">
        <div class="workflow-toolbar"><label class="control-label">Select wealth-advisory journey<select id="wfSelect" onchange="resetSim()"></select></label><div class="workflow-buttons"><button onclick="playSim()" id="btnPlay">RUN CONTROL-FLOW</button><button onclick="pauseSim()" id="btnPause" hidden>PAUSE</button><button onclick="resetSim()">RESET</button><select id="simSpeed" aria-label="Playback speed"><option value="1500">0.5x</option><option value="800" selected>1.0x</option><option value="400">2.0x</option></select></div></div>
        <div class="workflow-progress"><span>SIMULATED PROGRESS</span><strong id="wfStatus">READY</strong><div><i id="wfProgressBar"></i></div></div>
        <div class="workflow-layout"><aside><div class="workflow-verdict"><span>Product boundary</span><p id="wfVerdict"></p></div><dl class="not-measured"><div><dt>Tokens</dt><dd>Not measured</dd></div><div><dt>Cost</dt><dd>Not measured</dd></div><div><dt>Latency</dt><dd>Not measured</dd></div><div><dt>Cache</dt><dd>Not assumed</dd></div></dl><p id="wfDescription" class="muted"></p></aside><main><div class="workflow-chain-head"><strong>CONTROL-FLOW CHAIN</strong><span>Scenario—not production telemetry</span></div><div id="dagContainer"></div></main></div>
      </div>
    </div>
  </div>'''
text=replace_segment(text,'<!-- SECTION 4:','<!-- SECTION 5:',section4)

section5='''<!-- SECTION 5: EVIDENCE-BACKED CHARTS -->
  <div class="section-light" id="charts">
    <div class="section-inner">
      <div class="section-label">Section 5</div>
      <h2>Four Evidence-Backed Comparison Charts</h2>
      <p class="muted">Charts read the central runtime dataset. Each chart discloses population, metric direction, snapshot boundary and unavailable data. Accessible tables mirror every plotted value.</p>
      <div class="chart-box"><h4>1. Highest Retained Intelligence Index by Model</h4><p class="chart-boundary" id="intelBoundary"></p><div class="chart-frame"><canvas id="intelligenceChart" role="img" aria-label="Highest retained Intelligence Index by model"></canvas></div><div id="intelligenceTable"></div></div>
      <div class="chart-box"><h4>2. Highest Retained TAU Banking Score by Model</h4><p class="chart-boundary" id="tauBoundary"></p><div class="chart-frame"><canvas id="agenticChart" role="img" aria-label="Highest retained TAU Banking score by model"></canvas></div><div id="tauTable"></div></div>
      <div class="card-grid"><div class="chart-box"><h4>3. Model Evidence Coverage</h4><p class="chart-boundary" id="evidenceBoundary"></p><div class="chart-frame small"><canvas id="evidenceCoverageChart" role="img" aria-label="Unique model evidence coverage"></canvas></div><div id="evidenceTable"></div></div><div class="chart-box"><h4>4. Exact Official Standard Token Rates (₹ / 1M)</h4><p class="chart-boundary" id="priceBoundary"></p><div class="chart-frame small"><canvas id="verifiedPriceChart" role="img" aria-label="Exact official input and output token rates in Indian rupees"></canvas></div><div id="priceTable"></div></div></div>
    </div>
  </div>'''
text=replace_segment(text,'<!-- SECTION 5:','<!-- SECTION 6:',section5)

# Remove obsolete glossary modal and embedded corpora; runtime data now loads from JSON.
text=re.sub(r'\n\s*<!-- 14-POINT TERM EXPLANATION MODAL -->.*?<script>','\n  <div id="runtimeError" class="runtime-error" hidden role="alert"></div>\n  <script>',text,count=1,flags=re.S)
a=text.index('    const routingArchitecture =')
b=text.index('    let simState',a)
text=text[:a]+"    let reportRuntime=null;\n    let routingArchitecture=null;\n    let models=[];\n    let workflows={};\n\n"+text[b:]
# Remove obsolete glossary helpers through the old calculator start.
text=re.sub(r'\n\s*function openTermModal\(.*?\n\s*function populateSelects\(\) \{',"\n\n    function populateSelects() {",text,count=1,flags=re.S)
# Replace calculator code up to workflow-player state.
calc_js=r'''    function populateSelects() {
      const pricing=reportRuntime.pricing_catalog;
      const options=pricing.map(p=>`<option value="${p.id}">${p.name} — ₹${p.input_inr} in / ₹${p.output_inr} out</option>`).join('');
      const a=document.getElementById('simModelA'),b=document.getElementById('simModelB');a.innerHTML=options;b.innerHTML=options;a.value='gemini-3-5-flash-lite';b.value='kimi-k2-6';
      const wf=document.getElementById('wfSelect');wf.innerHTML=Object.entries(workflows).map(([k,v])=>`<option value="${k}">${v.name}</option>`).join('');
    }
    const presets={relationship:[20000,2000],portfolio:[75000,8000],operations:[50000,4000]};
    function applyPreset(){const p=presets[document.getElementById('simPreset').value]||presets.portfolio;document.getElementById('simInTok').value=p[0];document.getElementById('simOutTok').value=p[1];updateLabels();runSim();}
    function updateLabels(){document.getElementById('inTokLabel').textContent=Number(document.getElementById('simInTok').value).toLocaleString();document.getElementById('outTokLabel').textContent=Number(document.getElementById('simOutTok').value).toLocaleString();document.getElementById('runsLabel').textContent=Number(document.getElementById('simRuns').value).toLocaleString()+' runs';}
    function simulateUseCase(inTok,outTok,preset){document.getElementById('simInTok').value=inTok;document.getElementById('simOutTok').value=outTok;if(presets[preset])document.getElementById('simPreset').value=preset;updateLabels();runSim();document.getElementById('simulator').scrollIntoView({behavior:'smooth'});}
    function runSim(){
      if(!reportRuntime||typeof Decimal==='undefined')return;
      const pricing=reportRuntime.pricing_catalog;const A=pricing.find(x=>x.id===document.getElementById('simModelA').value);const B=pricing.find(x=>x.id===document.getElementById('simModelB').value);
      if(!A||!B){document.getElementById('savingsDesc').textContent='Unknown model identifier — calculation blocked.';return;}
      const million=new Decimal(1000000),inTok=new Decimal(document.getElementById('simInTok').value),outTok=new Decimal(document.getElementById('simOutTok').value),runs=new Decimal(document.getElementById('simRuns').value),fx=new Decimal(reportRuntime.fx.usd_to_inr);
      const cost=m=>inTok.mul(m.input_usd).add(outTok.mul(m.output_usd)).div(million).mul(fx);
      const ca=cost(A),cb=cost(B),ma=ca.mul(runs),mb=cb.mul(runs),diff=mb.sub(ma),annual=diff.mul(12);
      document.getElementById('nameA').textContent=A.name;document.getElementById('nameB').textContent=B.name;document.getElementById('costA').textContent='₹'+ca.toDecimalPlaces(2).toFixed(2);document.getElementById('costB').textContent='₹'+cb.toDecimalPlaces(2).toFixed(2);document.getElementById('lakhsA').textContent='₹'+ma.div(100000).toDecimalPlaces(4).toFixed(4)+' Lakhs';document.getElementById('lakhsB').textContent='₹'+mb.div(100000).toDecimalPlaces(4).toFixed(4)+' Lakhs';
      document.getElementById('savingsText').textContent='₹'+diff.abs().div(100000).toDecimalPlaces(4).toFixed(4)+' Lakhs / month';document.getElementById('annualSavings').textContent='₹'+annual.abs().div(100000).toDecimalPlaces(4).toFixed(4)+' Lakhs/year';document.getElementById('costPerThousand').textContent='₹'+ca.mul(1000).toDecimalPlaces(2).toFixed(2);
      const lower=diff.gt(0)?A.name:diff.lt(0)?B.name:'Neither';document.getElementById('savingsDesc').textContent=diff.eq(0)?'Both exact rate cards produce the same standard-token price for this scenario.':`${lower} is lower for these planning inputs. This difference excludes cache, batch, retries, tools, storage and platform fees.`;
    }

    let simInterval = null;'''
text=re.sub(r'    function populateSelects\(\) \{.*?    let simInterval = null;',calc_js,text,count=1,flags=re.S)
# Replace old synthetic workflow player and remove unused knowledge-graph functions.
player_js=r'''    let simInterval=null;
    let currentStep=0;
    function renderWorkflow(){
      const key=document.getElementById('wfSelect').value||Object.keys(workflows)[0],wf=workflows[key];if(!wf)return;
      document.getElementById('wfVerdict').textContent=wf.verdict;document.getElementById('wfDescription').textContent=wf.description;
      document.getElementById('dagContainer').innerHTML=wf.steps.map((s,i)=>`<article id="step-${i}" class="dag-step ${s.type}"><div><span>${i+1}</span><strong>${s.name}</strong><em>${s.type}</em></div><p>${s.desc}</p><small><b>Control:</b> ${s.control}</small></article>`).join('');
    }
    function updateHud(){const wf=workflows[document.getElementById('wfSelect').value];const pct=wf&&wf.steps.length?currentStep/wf.steps.length*100:0;document.getElementById('wfProgressBar').style.width=pct+'%';}
    function resetSim(){clearInterval(simInterval);currentStep=0;document.getElementById('wfStatus').textContent='READY';document.getElementById('btnPlay').hidden=false;document.getElementById('btnPause').hidden=true;renderWorkflow();updateHud();}
    function playSim(){const wf=workflows[document.getElementById('wfSelect').value];if(!wf)return;clearInterval(simInterval);document.getElementById('btnPlay').hidden=true;document.getElementById('btnPause').hidden=false;document.getElementById('wfStatus').textContent='PLAYING';const speed=Number(document.getElementById('simSpeed').value)||800;simInterval=setInterval(()=>{if(currentStep>=wf.steps.length){clearInterval(simInterval);document.getElementById('wfStatus').textContent='COMPLETE';document.getElementById('btnPlay').hidden=false;document.getElementById('btnPause').hidden=true;return;}if(currentStep>0)document.getElementById(`step-${currentStep-1}`)?.classList.remove('active');document.getElementById(`step-${currentStep}`)?.classList.add('active');document.getElementById(`step-${currentStep}`)?.scrollIntoView({block:'nearest',behavior:'smooth'});currentStep++;updateHud();},speed);}
    function pauseSim(){clearInterval(simInterval);document.getElementById('wfStatus').textContent='PAUSED';document.getElementById('btnPlay').hidden=false;document.getElementById('btnPause').hidden=true;}

    function renderWealthJourneys(filter='all'){
      const grid=document.getElementById('wealthJourneyGrid');const journeys=routingArchitecture.journeys.filter(j=>filter==='all'||j.id===filter);grid.innerHTML=journeys.map(j=>`<article class="usecase-card" data-cat="${j.id}"><div><span class="architecture-eyebrow">${j.label}</span><h3>${j.outcome}</h3><p>${j.summary}</p><div class="journey-tags">${j.agents.map(a=>`<span>${a}</span>`).join('')}</div><dl class="journey-evidence"><div><dt>Product surfaces</dt><dd>${j.surfaces.join(' · ')}</dd></div><div><dt>Inputs</dt><dd>${j.inputs.join(' · ')}</dd></div><div><dt>Control boundary</dt><dd>${j.guardrail}</dd></div></dl></div><aside><strong>Evidence status</strong><p>Frontend product contracts observed. Backend execution, connector availability, production reliability and branch freshness remain unproven.</p><button type="button" onclick="document.getElementById('wfSelect').value='${j.id}';resetSim();document.getElementById('workflows').scrollIntoView({behavior:'smooth'})">View control flow</button></aside></article>`).join('');
    }
    function initJourneyFilters(){document.querySelectorAll('[data-journey-filter]').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('[data-journey-filter]').forEach(x=>x.classList.toggle('active',x===b));renderWealthJourneys(b.dataset.journeyFilter)}));}

    function filterModelsTable() {'''
text=re.sub(r'    let simInterval = null;.*?    function filterModelsTable\(\) \{',player_js,text,count=1,flags=re.S)
# Replace all charts with central, evidence-scoped charts + accessible tables.
chart_js=r'''    const chartInstances=[];
    function renderDataTable(target,headers,rows){document.getElementById(target).innerHTML=`<div class="chart-table-wrap"><table><thead><tr>${headers.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows.map(r=>`<tr>${r.map(v=>`<td>${v}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;}
    function renderCharts(){
      if(typeof Chart==='undefined')throw new Error('Chart.js unavailable');chartInstances.splice(0).forEach(c=>c.destroy());const d=reportRuntime.chart_data,grid={color:'rgba(255,255,255,.08)'},ticks={color:'#86868b'};
      document.getElementById('intelBoundary').textContent=reportRuntime.chart_boundaries.intelligence;document.getElementById('tauBoundary').textContent=reportRuntime.chart_boundaries.tau_banking;document.getElementById('priceBoundary').textContent=reportRuntime.chart_boundaries.pricing;document.getElementById('evidenceBoundary').textContent=reportRuntime.chart_boundaries.evidence;
      chartInstances.push(new Chart(document.getElementById('intelligenceChart'),{type:'bar',data:{labels:d.intelligence.map(x=>x.name),datasets:[{label:'Highest retained score',data:d.intelligence.map(x=>x.value),backgroundColor:'#0071e3'}]},options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#86868b'}}},scales:{x:{grid,ticks},y:{grid:{display:false},ticks}}}}));
      chartInstances.push(new Chart(document.getElementById('agenticChart'),{type:'bar',data:{labels:d.tau_banking.map(x=>x.name),datasets:[{label:'TAU Banking (higher is better)',data:d.tau_banking.map(x=>x.value),backgroundColor:'#30d158'}]},options:{indexAxis:'y',responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#86868b'}}},scales:{x:{min:0,grid,ticks},y:{grid:{display:false},ticks}}}}));
      chartInstances.push(new Chart(document.getElementById('evidenceCoverageChart'),{type:'bar',data:{labels:d.evidence_coverage.map(x=>x.name),datasets:[{label:'Unique model cards',data:d.evidence_coverage.map(x=>x.value),backgroundColor:['#0071e3','#ff9f0a','#ff453a']}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{y:{beginAtZero:true,grid,ticks:{...ticks,precision:0}},x:{grid:{display:false},ticks}}}}));
      chartInstances.push(new Chart(document.getElementById('verifiedPriceChart'),{type:'bar',data:{labels:d.verified_pricing.map(x=>x.name),datasets:[{label:'Input ₹/1M',data:d.verified_pricing.map(x=>x.input_inr),backgroundColor:'#0071e3'},{label:'Output ₹/1M',data:d.verified_pricing.map(x=>x.output_inr),backgroundColor:'#30d158'}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{labels:{color:'#86868b'}}},scales:{y:{beginAtZero:true,grid,ticks:{...ticks,callback:v=>'₹'+v}},x:{grid:{display:false},ticks}}}}));
      renderDataTable('intelligenceTable',['Model','Highest retained score'],d.intelligence.map(x=>[x.name,Number(x.value).toFixed(1)]));renderDataTable('tauTable',['Model','Highest retained TAU Banking'],d.tau_banking.map(x=>[x.name,Number(x.value).toFixed(4)]));renderDataTable('evidenceTable',['Evidence state','Unique models'],d.evidence_coverage.map(x=>[x.name,x.value]));renderDataTable('priceTable',['Exact SKU','Input ₹/1M','Output ₹/1M'],d.verified_pricing.map(x=>[x.name,'₹'+x.input_inr,'₹'+x.output_inr]));
    }

    let lastEvidenceFocus = null;'''
text=re.sub(r'    function renderCharts\(\) \{.*?    let lastEvidenceFocus = null;',chart_js,text,count=1,flags=re.S)
# Dynamic FX evidence text in the model dialog.
text=text.replace('<div><dt>FX basis</dt><dd>ECB 2026-07-24: ₹96.567636/USD</dd></div>','<div><dt>FX basis</dt><dd id="evFxBasis">—</dd></div>')
# Replace init with fail-closed runtime loading.
init_js=r'''    async function loadReportRuntime(){
      if(window.SARVAX_REPORT_RUNTIME){reportRuntime=window.SARVAX_REPORT_RUNTIME;}else{const res=await fetch('./models/executive_report_runtime.json',{cache:'no-store'});if(!res.ok)throw new Error(`Runtime data HTTP ${res.status}`);reportRuntime=await res.json();}models=reportRuntime.models;routingArchitecture=reportRuntime.routing;workflows=reportRuntime.workflow_player;
      const coverage=reportRuntime.chart_data.evidence_coverage;const dual=coverage.find(x=>x.name==='Provider + benchmark').value;const needs=coverage.filter(x=>x.name!=='Provider + benchmark').reduce((n,x)=>n+x.value,0);const journeys=reportRuntime.routing.journeys||[];const agents=new Set(journeys.flatMap(j=>j.agents||[]));document.getElementById('providerBenchmarkKpi').textContent=dual;document.getElementById('journeyKpi').textContent=journeys.length;document.getElementById('agentKpi').textContent=agents.size;document.getElementById('needsProofKpi').textContent=needs;document.getElementById('heroModelCount').textContent=reportRuntime.metadata.unique_model_cards;document.getElementById('heroConfigCount').textContent=reportRuntime.metadata.benchmark_configurations;document.getElementById('heroFxBasis').innerHTML=`<small>FX BASIS</small><strong>ECB ${reportRuntime.fx.reference_date} · ₹${new Decimal(reportRuntime.fx.usd_to_inr).toDecimalPlaces(6).toFixed(6)}/USD</strong>`;document.getElementById('heroProofState').innerHTML=`<small>PROOF STATE</small><strong>${dual} dual-proof · ${needs} pending verification</strong>`;document.getElementById('sourceBoundaryCopy').textContent=`${reportRuntime.metadata.usable_sources} usable source snapshots are content-addressed. Model-family identity comes from official providers; benchmark values come from a retained Artificial Analysis API snapshot and are labelled accordingly.`;
      document.getElementById('fxBasis').textContent=`FX basis: ECB ${reportRuntime.fx.reference_date} — ₹${new Decimal(reportRuntime.fx.usd_to_inr).toDecimalPlaces(6).toFixed(6)}/USD. Latest business-day official cross-rate.`;document.getElementById('evFxBasis').textContent=`ECB ${reportRuntime.fx.reference_date}: ₹${new Decimal(reportRuntime.fx.usd_to_inr).toDecimalPlaces(6).toFixed(6)}/USD`;
    }
    window.onload=async function(){try{await loadReportRuntime();initUncannyArchitecture();populateSelects();updateLabels();runSim();resetSim();renderWealthJourneys();initJourneyFilters();renderModelsTable();initEvidenceInteractions();renderCharts();}catch(err){const box=document.getElementById('runtimeError');box.hidden=false;box.textContent='Report data failed closed: '+err.message;console.error(err);}};'''
text=re.sub(r'    window.onload = function\(\) \{.*?\n    \}',init_js,text,count=1,flags=re.S)
# Update counts/titles and public EU proof URLs.
text=text.replace('6 Interactive Charts','4 Evidence Charts').replace('6 Interactive Empirical Benchmark Charts','4 Evidence-Backed Comparison Charts')
text=text.replace('<p class="sub">Evidence-scoped evaluation of 24 unique models across 40 retained benchmark configurations. Provider identity is checked against current official pages; benchmark metrics use a retained 586-row Artificial Analysis API snapshot.</p>','<p class="sub">Evidence-scoped catalog of <span id="heroModelCount">—</span> model cards across <span id="heroConfigCount">—</span> retained benchmark configurations. Proposed routing is evaluated separately and may include provider-verified models without catalog-grade benchmark matching.</p>')
text=text.replace('<span>ECB FX (2026-07-24): <strong>1 USD = ₹96.567636 INR</strong></span>','<span id="heroFxBasis">ECB FX: loading verified data</span>')
text=text.replace('<span>Model proof status: <strong>21 unique models with provider + benchmark · 3 need more proof</strong></span>','<span id="heroProofState">Catalog proof state: loading verified data</span>')
text=text.replace('<div class="kpi green"><div class="num">21</div><div class="label">Unique Models with Two Proof Types</div></div>','<div class="kpi"><div class="num" id="providerBenchmarkKpi">—</div><div class="label">Dual-Proof Model Cards</div></div>')
text=text.replace('<div class="kpi accent"><div class="num">30</div><div class="label">Usable Source Snapshots</div></div>','<div class="kpi accent"><div class="num" id="journeyKpi">—</div><div class="label">Wealth-Advisory Journeys</div></div>')
text=text.replace('<div class="kpi orange"><div class="num">3</div><div class="label">Models Need More Proof</div></div>','<div class="kpi"><div class="num" id="agentKpi">—</div><div class="label">Domain Agent Roles</div></div>')
text=text.replace('<div class="kpi"><div class="num">40</div><div class="label">Benchmark Configurations Mapped</div></div>','<div class="kpi"><div class="num" id="needsProofKpi">—</div><div class="label">Pending Verification</div></div>')
text=text.replace('<p class="muted">Thirty usable source snapshots are content-addressed. Model-family identity comes from official providers; benchmark values come from a retained Artificial Analysis API snapshot and are labelled accordingly.</p>','<p class="muted" id="sourceBoundaryCopy">Usable source snapshots are content-addressed. Model-family identity comes from official providers; benchmark values come from a retained Artificial Analysis API snapshot and are labelled accordingly.</p>')
text=text.replace('https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Official EU AI Act','https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3" target="_blank" rel="noopener">Official EU Annex III')
text=text.replace('https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Article 15 source','https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15" target="_blank" rel="noopener">European Commission Article 15')
text=text.replace('https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Verify Article 15','https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-15" target="_blank" rel="noopener">Verify Article 15')
# Flat visual corrections.
text=text.replace("background: linear-gradient(180deg, #fff 0%, #86868b 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;","color:#fff;")
text=text.replace("background: linear-gradient(135deg, #0a1628 0%, #162033 100%);","background:#111;")
text=text.replace('background:linear-gradient(90deg, #0071e3, #30d158);','background:#0071e3;')
# Append hardened controls and responsive styles.
extra='''\n.control-label{display:grid;gap:7px;color:#86868b;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:16px}.control-label select{background:#000;color:#fff;border:1px solid #333336;border-radius:8px;padding:10px}.sim-model-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.range-label{display:grid;grid-template-columns:1fr auto;gap:6px;color:#86868b;font-size:12px;margin:18px 0}.range-label strong{color:#0071e3}.range-label input{grid-column:1/-1;width:100%;accent-color:#0071e3}.sim-results{display:grid;grid-template-columns:1fr 1fr;gap:12px}.sim-results article{background:#000;border:1px solid #333336;border-radius:12px;padding:16px;display:grid;gap:6px}.sim-results span,.sim-difference span{color:#86868b;font-size:10px;text-transform:uppercase}.sim-results b{color:#fff;font-size:18px}.sim-difference{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:18px}.sim-difference div{display:grid;gap:5px}.workflow-toolbar{display:flex;justify-content:space-between;gap:16px;align-items:end}.workflow-toolbar .control-label{min-width:300px;margin:0}.workflow-buttons{display:flex;gap:8px;align-items:center}.workflow-buttons button,.workflow-buttons select,.usecase-card aside button{background:#1c1c1e;color:#fff;border:1px solid #333336;border-radius:8px;padding:10px 13px;font-weight:700}.workflow-buttons #btnPlay,.usecase-card aside button{background:#0071e3;border-color:#0071e3}.workflow-progress{display:grid;grid-template-columns:1fr auto;gap:7px;color:#86868b;font-size:11px;margin:16px 0}.workflow-progress>div{grid-column:1/-1;height:6px;background:#000;border:1px solid #333336;border-radius:5px;overflow:hidden}.workflow-progress i{display:block;height:100%;width:0;background:#0071e3;transition:width .3s}.workflow-layout{display:grid;grid-template-columns:320px 1fr;gap:20px}.workflow-verdict,.not-measured{background:#000;border:1px solid #333336;border-radius:12px;padding:16px}.workflow-verdict span{color:#30d158;font-size:10px;text-transform:uppercase;font-weight:700}.workflow-verdict p{color:#fff;font-size:12px;line-height:1.5}.not-measured{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:12px 0}.not-measured div{display:grid;gap:3px}.not-measured dt{color:#86868b;font-size:10px}.not-measured dd{color:#fff;font-size:12px;margin:0}.workflow-chain-head{display:flex;justify-content:space-between;color:#86868b;font-size:10px;margin-bottom:10px}.workflow-chain-head strong{color:#fff}.dag-step{background:#111;border:1px solid #333336;border-radius:11px;padding:14px;margin-bottom:9px;transition:border-color .2s}.dag-step.active{border-color:#0071e3}.dag-step>div{display:flex;gap:9px;align-items:center}.dag-step>div span{background:#242426;color:#fff;border-radius:999px;width:24px;height:24px;display:grid;place-items:center;font-size:11px}.dag-step strong{color:#fff;font-size:13px}.dag-step em{margin-left:auto;color:#0071e3;font-size:9px;text-transform:uppercase;font-style:normal}.dag-step p,.dag-step small{color:#86868b;font-size:11px;line-height:1.45}.dag-step small b{color:#ff9f0a}.usecase-card{background:#1c1c1e;border:1px solid #333336;border-radius:14px;padding:22px;display:grid;grid-template-columns:1fr 270px;gap:20px}.usecase-card h3{color:#fff;font-size:18px;margin:8px 0}.usecase-card p{color:#a1a1a6;font-size:13px;line-height:1.55}.usecase-card aside{background:#111;border:1px solid #333336;border-radius:11px;padding:15px}.usecase-card aside strong{color:#ff9f0a;font-size:10px;text-transform:uppercase}.journey-evidence{display:grid;gap:8px;margin-top:14px}.journey-evidence div{display:grid;grid-template-columns:130px 1fr;gap:8px}.journey-evidence dt{color:#0071e3;font-size:10px;text-transform:uppercase}.journey-evidence dd{color:#a1a1a6;font-size:11px;margin:0}.chart-box{background:#1c1c1e!important;border:1px solid #333336!important;border-radius:16px;padding:24px;margin-top:24px;min-width:0;max-width:100%;overflow:hidden}.chart-box h4{color:#fff!important}.chart-boundary{color:#86868b;font-size:12px;line-height:1.5}.chart-frame{height:520px;width:100%}.chart-frame.small{height:380px}.chart-table-wrap{overflow:auto;margin-top:16px;max-height:260px;max-width:100%}.chart-table-wrap table{min-width:480px}.runtime-error{position:fixed;inset:70px 20px auto;z-index:5000;background:#2b1111;border:1px solid #ff453a;color:#fff;padding:16px;border-radius:12px}.usecase-filter{background:#1c1c1e;color:#86868b;border:1px solid #333336;border-radius:999px;padding:9px 14px;cursor:pointer}.usecase-filter.active{background:#0071e3;border-color:#0071e3;color:#fff}.nav{overflow-x:auto;overflow-y:hidden;max-width:100vw}@media(max-width:760px){.sim-model-grid,.sim-results,.sim-difference,.workflow-layout,.usecase-card{grid-template-columns:1fr}.workflow-toolbar{align-items:stretch;flex-direction:column}.workflow-toolbar .control-label{min-width:0}.workflow-buttons{flex-wrap:wrap}.journey-evidence div{grid-template-columns:1fr}.chart-frame{height:420px}.card-grid{grid-template-columns:1fr!important}.section,.section-inner{min-width:0}}@media print{.nav,.workflow-buttons,.route-mode-controls,.model-tools,.model-card-toolbar,.usecase-card aside button{display:none!important}.hero,.section-dark,.section-light{background:#fff!important;color:#000!important}.section,.section-inner{max-width:none!important;padding:20px!important}.chart-box,.card,.usecase-card,.uncanny-role-card{break-inside:avoid;background:#fff!important;color:#000!important;border-color:#b8b8b8!important}.chart-frame{height:360px!important}.chart-table-wrap{max-height:none!important;overflow:visible!important}}'''
text=text.replace('</style>',extra+'\n</style>',1)
text=text.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/decimal.js/10.4.3/decimal.min.js"></script>','<script src="https://cdnjs.cloudflare.com/ajax/libs/decimal.js/10.4.3/decimal.min.js"></script>\n  <script src="./models/executive_report_runtime.js"></script>',1)
HTML.write_text(text)
print(json.dumps({'backup':str(backup.relative_to(ROOT)),'runtime':str(RUNTIME.relative_to(ROOT)),'runtime_js':str(RUNTIME_JS.relative_to(ROOT)),'runtime_sha256':hashlib.sha256(RUNTIME.read_bytes()).hexdigest(),'runtime_js_sha256':hashlib.sha256(RUNTIME_JS.read_bytes()).hexdigest(),'html_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest(),'models':len(models),'configs':cards_doc['benchmark_configuration_count'],'exact_pricing_models':len(pricing),'workflow_scenarios':len(workflows)},indent=2))
