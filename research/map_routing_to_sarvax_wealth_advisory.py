from pathlib import Path
from datetime import datetime, timezone
import json,re,shutil,hashlib

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'
DATA=ROOT/'models/uncanny_valley_routing.json'
AUDIT=ROOT/'audit/sarvax_product_mapping_code_evidence.json'
ARCHIVE=ROOT/'audit/archive'
current=json.loads(DATA.read_text())
roles={r['id']:r for r in current['roles']}

roles['brain'].update({
 'role':'Produces bounded portfolio, tax and compliance analysis drafts inside SARVAX agents. Deterministic calculators and advisor approval own the final decision.',
 'why':'Its retained TAU Banking result is 0.3340, the highest value in this report’s retained 40-configuration comparison set. This is a shortlist signal, not proof of production accuracy.',
 'tradeoff':'Use only where a wealth-advisory journey needs deeper financial reasoning. Meeting notes, routing and routine extraction should not pay this cost or inherit this latency.'})
roles['reader'].update({
 'role':'Normalizes high-volume text from meeting transcripts, email, WhatsApp exports, CRM notes, research and text-native statements before SARVAX agents reason over it.',
 'why':'The official rate card verifies the exact SKU, low cache-hit pricing, JSON output, tool calls and a 1M context window—useful for large client-context assembly.',
 'tradeoff':'It is a text-context worker, not the product. Image-origin evidence still needs the Vision Gate; extracted facts must retain source references and pass journey-specific validation.'})
roles['router'].update({
 'role':'Identifies the wealth-advisory journey, urgency, household context and required SARVAX agent/workflow before expensive processing begins.',
 'why':'Google describes it as its fastest, most cost-effective 3.5 model for high-throughput execution. The retained snapshot reports 362.2 tps; its verified input rate is ₹28.97/1M.',
 'tradeoff':'Use for routing, classification and low-risk extraction checks—not investment, tax or compliance conclusions. Low-confidence routing must fall back to review.'})
roles['vision'].update({
 'role':'Handles image-origin evidence—scanned KYC records, photographed forms, charts and statement pages—when a broader wealth-advisory journey actually needs it.',
 'why':'Google’s model page describes Gemini 3.6 Flash as supporting agentic and multimodal tasks. The retained snapshot reports 243.9 tps.',
 'tradeoff':'Multimodal identity does not prove financial-document OCR accuracy. Validate tables, decimal placement, signatures and low-quality scans; escalate low-confidence evidence.'})

nodes={
 'relationship_intake':{'title':'Relationship intake','subtitle':'Meeting Assistant + CRM/MCP context','type':'product'},
 'portfolio_intake':{'title':'Portfolio intake','subtitle':'Holdings + market + client context','type':'product'},
 'operations_intake':{'title':'Operations intake','subtitle':'KYC + tasks + workflow events','type':'product'},
 'relationship_agents':{'title':'Relationship agents','subtitle':'Pre/Post Meeting + Client Strategist','type':'agent'},
 'portfolio_agents':{'title':'Portfolio agents','subtitle':'Portfolio Analyst + Market Intelligence','type':'agent'},
 'operations_agents':{'title':'Compliance & Ops agents','subtitle':'KYC, QA, Document, Cadence, Pipeline','type':'agent'},
 'deterministic':{'title':'Deterministic controls','subtitle':'Calculators + policy rules + validation','type':'control'},
 'approval':{'title':'Advisor approval','subtitle':'Workflow 2.0 approval gate','type':'human'},
 'writeback':{'title':'System writeback','subtitle':'CRM, tasks, notifications, artifacts','type':'product'}
}
journeys=[
 {
  'id':'relationship','label':'Client Relationship Intelligence','short_label':'Relationship',
  'summary':'Turns meetings and ongoing client communication into advisor-ready context, follow-ups and controlled system updates.',
  'outcome':'Every advisor starts prepared, leaves with structured actions and keeps the client record current.',
  'inputs':['Meeting Assistant transcripts','Email and WhatsApp context','CRM household history','Advisor notes and tasks'],
  'agents':['Pre-Meeting Analysis Agent','Post-Meeting Analysis Agent','Client Intelligence Strategist'],
  'surfaces':['Meeting Assistant','Agent Builder','Agent Memory','Workflow 2.0','MCP / integrations layer','Notifications and writeback'],
  'guardrail':'Meeting intelligence drafts context and actions. The advisor approves material client communication and every financial recommendation.',
  'stages':['relationship_intake','router','reader','relationship_agents','approval','writeback']
 },
 {
  'id':'portfolio','label':'Portfolio & Market Intelligence','short_label':'Portfolio',
  'summary':'Combines holdings, market context and client objectives into review-ready portfolio and tax-analysis drafts.',
  'outcome':'Faster portfolio reviews with traceable evidence, deterministic calculations and advisor-controlled recommendations.',
  'inputs':['Holdings and transactions','Market and research feeds','Risk profile and goals','Statements and tax-lot data'],
  'agents':['Portfolio Analyst','Market Intelligence Agent'],
  'surfaces':['MCP / integrations layer','OneChat projects and artifacts','Agent Builder','Skills','Workflow 2.0','Approval and audit trail'],
  'guardrail':'Models can draft analysis. Deterministic portfolio/tax engines validate the math; the advisor owns suitability and final action.',
  'stages':['portfolio_intake','router','reader','portfolio_agents','brain','deterministic','approval','writeback']
 },
 {
  'id':'operations','label':'Compliance & Advisor Operations','short_label':'Compliance & Operations',
  'summary':'Routes KYC, review cadence, pipeline, workload and document events through bounded agents and approval-controlled workflows.',
  'outcome':'Fewer missed obligations, cleaner KYC evidence and visible ownership across the advisory team.',
  'inputs':['KYC/CDD records','Client and account changes','Review cadence and pipeline events','Forms, messages and team tasks'],
  'agents':['Cadence Ops Lead','Campaign Audience Architect','Pipeline & Escalation Tracker','Team Performance & Workload Insights Agent','KYC Intelligence Officer','KYC/CDD QA Auditor','Document Intelligence & Auto-Population Agent'],
  'surfaces':['Agent Builder','Agent Memory','Workflow 2.0 parallel groups','Approval gates','Skills','MCP / integrations layer','Notifications'],
  'guardrail':'Policy rules and deterministic validation remain outside the model chain. Compliance exceptions and material account changes require named human approval.',
  'stages':['operations_intake','router','vision','reader','operations_agents','deterministic','approval','writeback']
 }
]
current.pop('routes',None)
current.pop('architecture',None)
current.update({
 'architecture_name':'SARVAX Wealth-Advisory Routing Architecture',
 'architecture_type':'3 product journeys + bounded model roles',
 'scope':'SARVAX wealth-advisory product mapping; models are components, not the product.',
 'roles':[roles[k] for k in ['brain','reader','router','vision']],
 'nodes':nodes,
 'journeys':journeys,
 'default_journey':'relationship',
 'product_mapping':{
   'agent_count':12,
   'platform_capabilities':['Meeting Assistant','Agent Builder','Agent Memory','Workflow 2.0 DAG and approvals','MCP Server Management','Skills Marketplace','OneChat','Notifications'],
   'evidence_status':'Codebase-backed frontend contracts; backend production behavior and connector coverage require separate verification.',
   'codebase_snapshot':'Local SARVAX/KaraX frontend snapshot; git branch metadata unavailable.'
 },
 'qa_corrections':[
   'Replaced PDF/file-type routes with three wealth-advisory product journeys.',
   'Mapped all 12 SARVAX wealth-advisory agents to relationship, portfolio/market and compliance/operations journeys.',
   'Mapped product surfaces only where frontend code or API contracts exist; specific wealth connector availability is not implied.',
   'Kept deterministic math, policy, authorization and human approval outside the model chain.',
   'Retained model evidence boundaries: benchmark performance is a shortlist signal, not production authorization.'
 ]
})
DATA.write_text(json.dumps(current,indent=2,ensure_ascii=False)+'\n')
AUDIT.parent.mkdir(parents=True,exist_ok=True)
audit={
 'generated_at':datetime.now(timezone.utc).isoformat(),
 'classification':'restricted internal implementation evidence; do not expose paths in public report',
 'repository':'/Users/satyyy/Downloads/karaxai-website-staging',
 'repository_state':'local snapshot without .git metadata; active branch and freshness not verifiable',
 'findings':[
  {'capability':'Meeting Assistant','status':'frontend/API contract found','evidence':['src/api/api.ts:1036-1040 createMeetingWithBot endpoint','src/constant/onboardaSteps.ts:215-217 bot joins, transcribes, generates notes/actions','src/config/routes.ts:11,17-18 meeting/transcription routes']},
  {'capability':'Agent Builder + Memory','status':'frontend/API contracts found','evidence':['src/api/api.ts:456+ createAgent','src/api/api.ts:494-496 deleteAgent','src/api/api.ts:549-632 memory CRUD']},
  {'capability':'Workflow 2.0 controls','status':'frontend/runtime contracts found','evidence':['src/lib/workflowV2.ts:37,93,564 requires_approval','src/lib/workflowV2.ts:631-633 parallel groups','src/app/dashboard/agents/aura/hooks/useCOSChat.ts:894+ await_approval events']},
  {'capability':'MCP Server Management','status':'frontend contracts found','evidence':['src/components/dashboardv2/onechat/ConnectMcpDialog.tsx:21-25 verify/list MCP','src/components/dashboardv2/onechat/OneChatInput.tsx:648-655 MCP query/list']},
  {'capability':'Skills Marketplace','status':'frontend surface found','evidence':['src/constant/onboardaSteps.ts:349-352 marketplace discovery/install','src/__tests__/useNextStepSuggestion.test.ts:10-14 routes across meetings, skills, workflows, agents']}
 ],
 'boundaries':['Frontend/API contracts do not prove backend reliability, connector coverage, data correctness or production deployment.','The 12 wealth-advisory agent names come from the SARVAX product catalog supplied for this report; this local snapshot does not independently prove each vertical agent implementation.']
}
AUDIT.write_text(json.dumps(audit,indent=2,ensure_ascii=False)+'\n')

html=HTML.read_text()
ARCHIVE.mkdir(parents=True,exist_ok=True)
h=hashlib.sha256(html.encode()).hexdigest()[:16]
backup=ARCHIVE/f'index-before-sarvax-product-map-{h}.html'
if not backup.exists(): shutil.copy2(HTML,backup)
buttons=''.join(f'<button type="button" class="route-mode" data-route-mode="{j["id"]}">{j["label"]}</button>' for j in journeys)
markup=f'''<div class="uncanny-shell" data-source="models/uncanny_valley_routing.json">
        <div class="uncanny-heading"><div><span class="architecture-eyebrow">SARVAX WEALTH-ADVISORY ARCHITECTURE</span><h3>Models underneath the product—not the product itself</h3></div><span class="architecture-badge">12 agents · 3 advisory journeys</span></div>
        <p class="uncanny-lead">Wealth advisory work arrives through meetings, CRM history, email, WhatsApp, holdings, market data, KYC records, tasks and client documents. SARVAX owns the journey: intake, agent orchestration, memory, approvals, integrations and writeback. Foundation models perform bounded routing, context assembly, vision and reasoning roles underneath it.</p>
        <div class="architecture-decision"><strong>Product recommendation:</strong> Design around advisor journeys—not PDF types. Keep deterministic calculations, policy enforcement, authorization and human approval outside the model chain.</div>
        <div class="route-mode-controls" role="group" aria-label="Select a SARVAX wealth-advisory journey">{buttons}</div>
        <div id="uncannyRouteFlow" class="uncanny-route-flow" aria-live="polite"></div>
        <p id="uncannyRouteSummary" class="uncanny-route-summary"></p>
        <div id="productJourneyMap" class="product-journey-map" aria-live="polite"></div>
        <div class="model-role-divider"><span>Bounded model roles underneath these journeys</span></div>
        <div id="uncannyRoleGrid" class="uncanny-role-grid"></div>
        <details class="architecture-qa"><summary>Evidence boundaries and QA corrections</summary><ul id="uncannyQaList"></ul></details>
      </div>'''
pat=r'<div class="uncanny-shell"[^>]*>.*?<details class="architecture-qa">.*?</details>\s*</div>'
html,n=re.subn(pat,markup,html,count=1,flags=re.S)
if n!=1: raise SystemExit(f'architecture markup replacement failed: {n}')
# Replace embedded presentation data from central JSON.
blob=json.dumps(current,ensure_ascii=False,separators=(',',':'))
html,n=re.subn(r'const routingArchitecture\s*=\s*.*?;\n\s*const models\s*=',f'const routingArchitecture = {blob};\n    const models =',html,count=1,flags=re.S)
if n!=1: raise SystemExit(f'embedded architecture data replacement failed: {n}')
# Product-mapped renderer.
renderer='''function renderUncannyArchitecture(routeId='relationship'){
  const journey=routingArchitecture.journeys.find(j=>j.id===routeId)||routingArchitecture.journeys[0];
  document.querySelectorAll('.route-mode').forEach(b=>{const active=b.dataset.routeMode===journey.id;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active))});
  const roleMap=Object.fromEntries(routingArchitecture.roles.map(r=>[r.id,{title:r.nickname,subtitle:r.model,type:'model'}]));
  const nodeMap={...routingArchitecture.nodes,...roleMap};
  const flow=document.getElementById('uncannyRouteFlow');
  flow.innerHTML=journey.stages.map((id,i)=>{const n=nodeMap[id]||{title:id,subtitle:'',type:'product'};return `<div class="route-node ${n.type||''}"><strong>${n.title}</strong><span>${n.subtitle}</span></div>${i<journey.stages.length-1?'<span class="route-arrow" aria-hidden="true">→</span>':''}`}).join('');
  document.getElementById('uncannyRouteSummary').textContent=journey.summary;
  const tags=a=>a.map(x=>`<span>${x}</span>`).join('');
  document.getElementById('productJourneyMap').innerHTML=`<div class="journey-map-head"><span>Selected SARVAX journey</span><strong>${journey.label}</strong></div><div class="journey-map-grid"><article><label>Advisor outcome</label><p>${journey.outcome}</p></article><article><label>SARVAX agents</label><div class="journey-tags">${tags(journey.agents)}</div></article><article><label>Product surfaces</label><div class="journey-tags">${tags(journey.surfaces)}</div></article><article><label>Inputs across the journey</label><div class="journey-tags">${tags(journey.inputs)}</div></article><article class="journey-guardrail"><label>Control boundary</label><p>${journey.guardrail}</p></article></div>`;
  const cards=document.getElementById('uncannyRoleGrid');
  cards.innerHTML=routingArchitecture.roles.map(r=>`<article class="uncanny-role-card"><div class="uncanny-role-top"><h4>${r.number}. ${r.nickname}</h4><span class="uncanny-role-kind">${r.kind}</span></div><div class="uncanny-model-name">${r.model} <span>${r.vendor}</span></div><div class="uncanny-role-copy"><p><strong>Product role:</strong> ${r.role}</p><p><strong>Why:</strong> ${r.why}</p><p><strong>Boundary:</strong> ${r.tradeoff}</p></div><div class="uncanny-mini-metrics">${r.metrics.map(m=>`<div class="uncanny-mini-metric"><strong>${m.value}</strong><span>${m.label}<br>${m.scope}</span></div>`).join('')}</div><div class="uncanny-evidence-row"><span class="status-text">${r.status}</span><span>${r.sourceUrl?`<a href="${r.sourceUrl}" target="_blank" rel="noopener noreferrer">Provider proof</a>`:''}${r.benchmarkUrl?` · <a href="${r.benchmarkUrl}" target="_blank" rel="noopener noreferrer">Benchmark</a>`:''}</span></div></article>`).join('');
  document.getElementById('uncannyQaList').innerHTML=routingArchitecture.qa_corrections.map(x=>`<li>${x}</li>`).join('');
}
function initUncannyArchitecture(){
  document.querySelectorAll('.route-mode').forEach(b=>b.addEventListener('click',()=>renderUncannyArchitecture(b.dataset.routeMode)));
  renderUncannyArchitecture(routingArchitecture.default_journey||'relationship');
}
'''
html,n=re.subn(r"function renderUncannyArchitecture\(routeId='[^']+'\)\s*\{.*?\n\s*function initUncannyArchitecture\(\)\{.*?\n\s*\}\n\n\s*let activeProofFilter",renderer+'\n    let activeProofFilter',html,count=1,flags=re.S)
if n!=1: raise SystemExit(f'renderer replacement failed: {n}')
# Add product-map styles once.
css='''.product-journey-map{background:#111;border:1px solid #333336;border-radius:14px;padding:20px;margin:0 0 24px}.journey-map-head{display:flex;justify-content:space-between;gap:16px;align-items:center;margin-bottom:16px}.journey-map-head span,.journey-map-grid label{color:#0071e3;font-size:10px;font-weight:700;letter-spacing:.12em;text-transform:uppercase}.journey-map-head strong{color:#fff;font-size:18px}.journey-map-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.journey-map-grid article{background:#171719;border:1px solid #2c2c2e;border-radius:11px;padding:14px}.journey-map-grid p{color:#d1d1d6;font-size:13px;line-height:1.55;margin:8px 0 0}.journey-tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}.journey-tags span{color:#d1d1d6;background:#222224;border:1px solid #3a3a3c;border-radius:999px;padding:6px 9px;font-size:10px}.journey-guardrail{grid-column:1/-1;border-left:3px solid #ff9f0a!important}.model-role-divider{display:flex;align-items:center;gap:12px;color:#86868b;font-size:11px;text-transform:uppercase;letter-spacing:.1em;margin:24px 0 14px}.model-role-divider:before,.model-role-divider:after{content:'';height:1px;background:#333336;flex:1}.uncanny-shell .uncanny-route-flow{gap:4px}.uncanny-shell .route-node{min-width:85px;flex:1 1 85px;padding:10px}.route-node.product{border-color:#164f7d}.route-node.agent{border-color:#0071e3}.route-node.control{border-color:#ff9f0a}.route-node.human{border-color:#ff9f0a}@media(max-width:760px){.journey-map-head{align-items:flex-start;flex-direction:column}.journey-map-grid{grid-template-columns:1fr}.journey-guardrail{grid-column:auto}.uncanny-shell .route-node{min-width:0;width:100%;flex:0 0 auto}}'''
if '.product-journey-map{' not in html: html=html.replace('</style>',css+'</style>',1)
HTML.write_text(html)
print(json.dumps({'backup':str(backup),'html_sha256':hashlib.sha256(html.encode()).hexdigest(),'journeys':len(journeys),'mapped_agents':len(set(a for j in journeys for a in j['agents'])),'roles':len(current['roles'])},indent=2))
