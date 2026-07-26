from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
import json,re,hashlib,shutil

ROOT=Path(__file__).resolve().parents[1]
HTML=ROOT/'index.html'
AUDIT=json.loads((ROOT/'models'/'model_source_audit.json').read_text())
MANIFEST=json.loads((ROOT/'local_knowledge_repository'/'official_source_manifest.json').read_text())
FX=Decimal(AUDIT['fx']['usd_to_inr'])
FX_DISPLAY=FX.quantize(Decimal('0.000001'),rounding=ROUND_HALF_UP)
FX_DATE=AUDIT['fx']['ecb_reference_date']
STAMP=AUDIT['generated_at']
source_by_id={x['id']:x for x in MANIFEST['sources']}
audit_by_id={x['id']:x for x in AUDIT['models']}

html=HTML.read_text()
archive=ROOT/'audit'/'archive'/f"index-pre-section-8-9-{datetime.now().strftime('%Y%m%d-%H%M%S')}.html"
archive.parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(HTML,archive)

# Rebuild embedded model records from the existing array while preserving every row and report link.
start=html.index('    const models = [')+len('    const models = ')
end=html.index('\n];',start)+2
models=json.loads(html[start:end])
for m in models:
    a=audit_by_id[m['id']]
    m['inInr']=float((Decimal(str(m['inUsd']))*FX).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
    m['outInr']=float((Decimal(str(m['outUsd']))*FX).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP))
    m['cachedInr']=None
    m['cacheRateStatus']='not-validated'
    m['proofStatus']=a['proof_status']
    m['decisionUse']=a['decision_use']
    m['officialHits']=a['official_hits']
    m['benchmarkExact']=a['benchmark_snapshot_exact_name_match']
    m['benchmarkFresh']=a['benchmark_snapshot_fresh_api_retrieval']
    m['metricMismatches']=[k for k,v in a['metric_checks'].items() if not v['match_with_rounding_tolerance']]
    if a['official_hits']:
        src=source_by_id[a['official_hits'][0]]
        m['sourceName']=src['publisher']+' official documentation'
        m['sourceUrl']=src['final_url']
        m['sourceSha256']=src['sha256']
        m['retrievalDate']=src['retrieved_at']
html=html[:start]+json.dumps(models,indent=2,ensure_ascii=False)+html[end:]

# Global executive/evidence framing — surgical text corrections, no structural redesign.
replacements={
'<a href="#models">37 Verified Models</a>':'<a href="#models">37 Model Proofs</a>\n    <a href="#compliance">Compliance</a>',
'<p class="sub">Empirical evaluation of 586 global LLMs across wealth advisory math, dynamic model routing, and unit economics in <strong class="text-white">Indian Rupees (₹)</strong>.</p>':'<p class="sub">Evidence-scoped evaluation of 37 model rows across wealth advisory math, routing and unit economics. Provider identity is checked against current official pages; benchmark metrics use a retained 586-row Artificial Analysis API snapshot.</p>',
'<span>Primary Source: <strong>Artificial Analysis Official REST API v2</strong></span>\n      <span>Rate: <strong>1 USD = ₹96.61 INR</strong></span>\n      <span>Quality Gate: <strong>100% Passed (12/12 Checks)</strong></span>':f'<span>Evidence: <strong>Official provider pages + retained benchmark snapshot</strong></span>\n      <span>ECB FX ({FX_DATE}): <strong>1 USD = ₹{FX_DISPLAY} INR</strong></span>\n      <span>Model proof status: <strong>34 dual-source · 3 quarantined</strong></span>',
'<h2>Curated Enterprise Frontier Models (37 Strict SOTA)</h2>\n      <p class="muted">Calculated token rates converted natively at ₹96.61 per USD.</p>':f'<h2>Model Evidence Matrix — 37 Audited Rows</h2>\n      <p class="muted">Each row exposes its provider proof, benchmark-snapshot match, metric discrepancies and decision-use status. INR values use the ECB {FX_DATE} reference cross-rate of ₹{FX_DISPLAY}/USD. Cache discounts are excluded until exact SKU terms are verified.</p>\n      <div class="model-tools" role="search" aria-label="Model evidence filters">\n        <input id="modelSearchInput" type="search" placeholder="Search model or vendor" aria-label="Search model evidence">\n        <button class="proof-filter active" data-proof="all" type="button">All 37</button>\n        <button class="proof-filter" data-proof="dual" type="button">Dual-source 34</button>\n        <button class="proof-filter" data-proof="quarantine" type="button">Quarantined 3</button>\n      </div>',
'<tr><th style="color:#86868b;">Model Name</th><th style="color:#86868b;">Vendor</th><th style="color:#0071e3;">TAU Banking</th><th style="color:#86868b;">Intel Index</th><th style="color:#30d158;">Input Rate / 1M (₹)</th><th style="color:#86868b;">Output Rate / 1M (₹)</th><th style="color:#30d158;">Speed (tok/s)</th></tr>':'<tr><th>Model Name</th><th>Vendor</th><th>TAU Banking</th><th>Intel Index</th><th>Input / 1M (₹)</th><th>Output / 1M (₹)</th><th>Speed</th><th>Proof status</th></tr>'}
for old,new in replacements.items():
    if old not in html: raise RuntimeError('Missing replacement target: '+old[:80])
    html=html.replace(old,new,1)

old_verdict='''      <h2>Verdict: SARVAX Hybrid Cascade Architecture</h2>
      <p>Deploying <strong>Kimi K3</strong> for wealth advisory math and <strong>Gemini 3.6 Flash</strong> for live chat recovers <strong>₹24.64 Lakhs annually per 100,000 reports</strong> (90.8% cost reduction vs raw closed APIs).</p>
      <div id="verdictText" style="margin-top:12px; font-size:13px; color:#86868b;">
        <strong>Actionable Verdict:</strong> Kimi K3 leads globally on TAU Banking (0.3340 score). Deploying Kimi K3 saves ₹24.64 Lakhs annually per 100k reports.
      </div>
      <p style="margin-top:16px"><strong>Skeptic Agent Invalidation:</strong> DeepSeek V4 Pro features a strict <strong>60 RPM</strong> rate limit bottleneck triggering <strong>HTTP 429</strong> crashes under multi-user DAG loads. Route live user chat to <strong>Gemini 3.6 Flash</strong> (unlimited Vertex AI SLAs) and isolate DeepSeek strictly to background cron queues.</p>'''
new_verdict='''      <h2>Verdict: Conditional Hybrid Cascade — Evidence Gates Remain</h2>
      <p>A hybrid cascade remains a valid <strong>architecture pattern</strong>, not a verified model-selection decision. Thirty-four model rows have both current provider-family documentation and an exact retained benchmark-snapshot row; three remain quarantined. Financial savings, provider rate limits and production SLAs require exact SKU, contract and trace evidence before GTM approval.</p>
      <div id="verdictText" style="margin-top:12px; font-size:13px; color:#86868b;"><strong>Decision:</strong> architecture exploration may continue; procurement, financial commitment and regulated production routing remain conditional.</div>
      <p style="margin-top:16px"><strong>Evidence boundary:</strong> provider pages establish model-family documentation. Artificial Analysis metrics are from a retained API snapshot that could not be freshly refreshed because the API credential was unavailable. A benchmark row does not establish provider availability, SLA, compliance or customer access.</p>'''
if old_verdict not in html: raise RuntimeError('Verdict block missing')
html=html.replace(old_verdict,new_verdict,1)
old_kpis='''      <div class="kpi green"><div class="num">0.3340</div><div class="label">TAU Banking #1 Score</div></div>
      <div class="kpi accent"><div class="num">₹24.64L</div><div class="label">Annual Savings / 100k Reports</div></div>
      <div class="kpi orange"><div class="num">88.0%</div><div class="label">GLM-4.7 SWE-bench</div></div>
      <div class="kpi red"><div class="num">60 RPM</div><div class="label">DeepSeek Rate Limit Cap</div></div>'''
new_kpis='''      <div class="kpi green"><div class="num">34</div><div class="label">Provider + Benchmark Proof</div></div>
      <div class="kpi accent"><div class="num">27</div><div class="label">Usable Source Snapshots</div></div>
      <div class="kpi orange"><div class="num">3</div><div class="label">Quarantined Model Rows</div></div>
      <div class="kpi red"><div class="num">0</div><div class="label">Human Executive Sign-offs</div></div>'''
html=html.replace(old_kpis,new_kpis,1)

# Replace Sections 6, 8 and 9 while preserving section positions and full-width visual rhythm.
def replace_between(text,start_marker,end_marker,replacement):
    a=text.index(start_marker);b=text.index(end_marker,a)
    return text[:a]+replacement+'\n\n'+text[b:]
section6='''  <!-- SECTION 6: OFFICIAL PUBLIC PROOFS -->
  <div class="section-dark" id="proofs">
    <div class="section">
      <div class="section-label">Section 6</div>
      <h2>Official Public Proofs &amp; Evidence Boundaries</h2>
      <p class="muted">Twenty-seven current source snapshots were retrieved successfully and content-addressed. Model-family identity comes from official providers; benchmark values come from a retained Artificial Analysis API snapshot and are labelled accordingly.</p>
      <div class="evidence-summary" style="margin-top:32px;">
        <details open><summary>Official provider documentation — current retrieval</summary><p>Anthropic, OpenAI, Google, Moonshot/Kimi, xAI, Z.ai, Alibaba Cloud, Cohere and AWS pages were fetched, redirected URLs retained, and SHA-256 hashes recorded. Click any model proof badge in Section 7 to inspect its exact provider link.</p></details>
        <details><summary>Independent benchmark snapshot — retained, not freshly refreshed</summary><p>The local Artificial Analysis API snapshot contains 586 rows; 35 report rows match exact benchmark names. The API credential was unavailable for a fresh refresh, so benchmark freshness is disclosed rather than promoted as live.</p></details>
        <details><summary>Pricing and FX boundary</summary><p>Provider rate-card pages were captured, but exact SKU price extraction is not complete for every row. INR conversion uses the ECB {FX_DATE} daily EUR reference rates: INR/EUR divided by USD/EUR = ₹{FX_DISPLAY}/USD. Cache and batch discounts are excluded until exact provider terms are attached.</p></details>
      </div>
    </div>
  </div>'''.format(FX_DATE=FX_DATE,FX_DISPLAY=FX_DISPLAY)
html=replace_between(html,'  <!-- SECTION 6: OFFICIAL PUBLIC PROOFS -->','  <!-- SECTION 7:',section6)

section8='''  <!-- SECTION 8: ENTERPRISE COMPLIANCE & EU AI ACT -->
  <div class="section-dark" id="compliance">
    <div class="section">
      <div class="section-label">Section 8</div>
      <h2>Enterprise Compliance &amp; EU AI Act Governance</h2>
      <p class="muted">EU AI Act Annex III, Article 15, SOC 2 Type II, HIPAA BAA and FedRAMP High are different governance mechanisms. This section separates legal scope, attestations, contracts, cloud authorization and SARVAX engineering policy.</p>
      <div class="compliance-tabs" role="tablist" aria-label="Compliance framework views">
        <button role="tab" aria-selected="true" data-compliance-tab="eu">EU AI Act</button>
        <button role="tab" aria-selected="false" data-compliance-tab="assurance">SOC 2 &amp; HIPAA</button>
        <button role="tab" aria-selected="false" data-compliance-tab="fedramp">FedRAMP &amp; Sovereignty</button>
        <button role="tab" aria-selected="false" data-compliance-tab="precision">Precision Policy</button>
      </div>
      <div class="compliance-panel active" data-compliance-panel="eu">
        <div class="governance-grid">
          <article class="governance-card"><span class="status verified">Verified legal text</span><h3>Annex III applicability is use-case specific</h3><p>Annex III includes AI used to evaluate the creditworthiness or credit score of natural persons and AI used for risk assessment and pricing for natural persons in life and health insurance. A portfolio-analysis or wealth-advisory system is not automatically Annex III high-risk solely because it operates in finance; intended purpose and material influence must be assessed.</p><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Official EU AI Act</a></article>
          <article class="governance-card"><span class="status verified">Verified legal text</span><h3>Article 15: accuracy, robustness and cybersecurity</h3><p>Article 15 requires high-risk AI systems to achieve an appropriate level of accuracy, robustness and cybersecurity throughout their lifecycle, declare relevant accuracy metrics and be resilient to errors, faults and attacks. It does not name INT4, FP8 or BF16.</p><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Article 15 source</a></article>
        </div>
        <details class="control-detail"><summary>SARVAX evidence required before EU deployment</summary><ul><li>Document intended purpose, affected persons and Annex III applicability.</li><li>Define task-specific accuracy, calibration, numeric error and robustness thresholds.</li><li>Retain validation datasets, versioned test results, human oversight and incident controls.</li><li>Map provider, deployer and importer responsibilities before claiming conformity.</li></ul></details>
      </div>
      <div class="compliance-panel" data-compliance-panel="assurance" hidden>
        <div class="governance-grid">
          <article class="governance-card"><span class="status scoped">Third-party attestation</span><h3>SOC 2 Type II</h3><p>SOC 2 Type II concerns controls for a defined service-organization system over a review period. It is not a compliance badge inherited by an individual model. Review the report scope, Trust Services Criteria, examination period, exceptions and bridge coverage.</p><a href="https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services" target="_blank" rel="noopener">AICPA SOC resources</a></article>
          <article class="governance-card"><span class="status scoped">Contractual mechanism</span><h3>HIPAA Business Associate Agreement</h3><p>Where PHI is handled, a covered entity must obtain appropriate assurances through a business-associate contract and confirm the relevant service and data flow are in scope. “HIPAA eligible” model availability alone is insufficient.</p><a href="https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html" target="_blank" rel="noopener">HHS business-associate guidance</a></article>
        </div>
        <details class="control-detail"><summary>Evidence required</summary><ul><li>Executed BAA and in-scope service list.</li><li>PHI data-flow diagram, minimum-necessary controls and access logging.</li><li>Subprocessor, retention, deletion, breach and incident obligations.</li><li>SOC report scope, auditor, period, exceptions and customer controls.</li></ul></details>
      </div>
      <div class="compliance-panel" data-compliance-panel="fedramp" hidden>
        <div class="governance-grid">
          <article class="governance-card"><span class="status verified">AWS statement verified</span><h3>Amazon Bedrock in GovCloud</h3><p>AWS states that Amazon Bedrock is a FedRAMP High authorized service in AWS GovCloud (US-West). That statement applies to the authorized cloud service and boundary—not generically to every model, application architecture or customer deployment.</p><a href="https://aws.amazon.com/bedrock/security-compliance/" target="_blank" rel="noopener">AWS Bedrock security &amp; compliance</a></article>
          <article class="governance-card"><span class="status contradicted">100% sovereignty claim rejected</span><h3>Private VPC is not automatic air-gapping</h3><p>Self-hosting a model in a VPC does not by itself guarantee air-gapping or “100% cloud data sovereignty.” Sovereignty depends on region, identity, egress, private endpoints, encryption keys, logs, backups, telemetry, support access, subprocessors and the model-artifact supply chain.</p><a href="https://aws.amazon.com/govcloud-us/" target="_blank" rel="noopener">AWS GovCloud</a></article>
        </div>
        <details class="control-detail"><summary>FedRAMP High review boundary</summary><ul><li>Named service and FedRAMP Marketplace status.</li><li>Authorization boundary, region and agency authorization path.</li><li>Inherited controls versus SARVAX/customer-responsible controls.</li><li>Model endpoint, data stores, logging, networking and operations inside the boundary.</li></ul></details>
      </div>
      <div class="compliance-panel" data-compliance-panel="precision" hidden>
        <div class="governance-grid">
          <article class="governance-card"><span class="status contradicted">Not statutory text</span><h3>Article 15 does not prohibit INT4</h3><p>The statement “INT4 is strictly prohibited and FP8/BF16 are required” is not present in Article 15. Quantization can affect numeric fidelity, but the legal requirement is outcome-based accuracy, robustness and cybersecurity.</p><a href="https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng" target="_blank" rel="noopener">Verify Article 15</a></article>
          <article class="governance-card"><span class="status policy">SARVAX engineering policy</span><h3>Material financial-risk scoring precision gate</h3><p>SARVAX policy: do not deploy INT4 for material financial-risk scoring unless model-specific validation demonstrates no material degradation against the approved reference precision. FP8/BF16 may be approved only after the same tests; neither is automatically safe.</p></article>
        </div>
        <details class="control-detail"><summary>Required precision-validation pack</summary><ul><li>Exact model/version, quantization method and reference precision.</li><li>Representative financial dataset and materiality threshold.</li><li>Numeric error, ranking/discrimination, calibration and tail-risk results.</li><li>Adversarial robustness, drift monitoring, sign-off owner and residual risk.</li></ul></details>
      </div>
    </div>
  </div>'''
html=replace_between(html,'  <!-- SECTION 8: ENTERPRISE COMPLIANCE & EU AI ACT -->','  <!-- SECTION 9:',section8)

section9=''
html=replace_between(html,'  <!-- SECTION 9: FOUNDER REVIEW BOARD SIGN-OFFS -->','  <!-- Footer -->',section9)

# Accurate evidence modal replaces fabricated confidence and source counts.
modal_start='  <!-- 8-POINT EVIDENCE PROVENANCE INSPECTOR MODAL -->'
modal_end='\n</body>'
a=html.index(modal_start);b=html.index(modal_end,a)
modal='''  <!-- MODEL EVIDENCE INSPECTOR -->
  <div id="evidenceModal" class="evidence-modal" hidden role="dialog" aria-modal="true" aria-labelledby="evModelName">
    <div class="evidence-dialog" tabindex="-1">
      <button id="evidenceClose" type="button" aria-label="Close evidence inspector">Close</button>
      <span id="evStatus" class="status scoped">Evidence status</span>
      <h2 id="evModelName">Model evidence</h2>
      <p id="evMetricTitle" class="muted"></p>
      <dl class="evidence-list">
        <div><dt>Provider proof</dt><dd><a id="evSourceLink" href="#" target="_blank" rel="noopener">Official source</a></dd></div>
        <div><dt>Retrieved</dt><dd id="evTimestamp">—</dd></div>
        <div><dt>Source SHA-256</dt><dd id="evSig">—</dd></div>
        <div><dt>Benchmark snapshot</dt><dd id="evBenchmark">—</dd></div>
        <div><dt>Metric check</dt><dd id="evMetricCheck">—</dd></div>
        <div><dt>Decision use</dt><dd id="evDecisionUse">—</dd></div>
        <div><dt>FX basis</dt><dd>ECB {FX_DATE}: ₹{FX_DISPLAY}/USD</dd></div>
        <div><dt>Boundary</dt><dd>Provider proof confirms model-family documentation; benchmark snapshot does not prove customer access, SLA, compliance or current price.</dd></div>
      </dl>
    </div>
  </div>'''.format(FX_DATE=FX_DATE,FX_DISPLAY=FX_DISPLAY)
html=html[:a]+modal+html[b:]

# CSS extension, preserving the original visual system.
css='''
  .model-tools{display:flex;gap:10px;flex-wrap:wrap;margin:28px 0 8px}.model-tools input{min-width:260px;flex:1;background:#1c1c1e;color:#fff;border:1px solid #333336;border-radius:10px;padding:11px 14px}.proof-filter,.compliance-tabs button{background:#1c1c1e;color:#86868b;border:1px solid #333336;border-radius:999px;padding:9px 14px;cursor:pointer}.proof-filter.active,.compliance-tabs button[aria-selected="true"]{color:#fff;border-color:#2997ff;background:rgba(41,151,255,.12)}.proof-badge{display:inline-block;border:1px solid #333336;border-radius:999px;padding:5px 8px;font-size:10px;font-weight:700;white-space:nowrap}.proof-badge.dual,.status.verified{color:#30d158;border-color:rgba(48,209,88,.35);background:rgba(48,209,88,.08)}.proof-badge.quarantine,.status.contradicted,.review-state.blocked{color:#ff453a;border-color:rgba(255,69,58,.35);background:rgba(255,69,58,.08)}.status,.review-state{display:inline-block;border:1px solid #333336;border-radius:999px;padding:5px 9px;font-size:10px;font-weight:700}.status.scoped,.status.policy,.review-state.conditional{color:#ffd60a;border-color:rgba(255,214,10,.35);background:rgba(255,214,10,.08)}.evidence-summary,.review-grid{display:grid;gap:12px}.evidence-summary details,.review-grid details,.control-detail{border:1px solid #333336;border-radius:14px;background:#1c1c1e;padding:18px 20px}.evidence-summary summary,.review-grid summary,.control-detail summary{cursor:pointer;font-weight:700}.evidence-summary p,.review-grid p,.control-detail li{color:#86868b;margin-top:12px}.compliance-tabs{display:flex;gap:10px;flex-wrap:wrap;margin:30px 0}.compliance-panel{animation:fadeIn .25s ease}.governance-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}.governance-card{border:1px solid #333336;border-radius:16px;background:#1c1c1e;padding:26px}.governance-card h3{font-size:21px;margin:16px 0 10px}.governance-card p{color:#86868b}.governance-card a{display:inline-block;color:#2997ff;margin-top:14px}.control-detail{margin-top:18px}.control-detail ul{padding-left:20px}.board-summary{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:28px 0}.board-summary div{border:1px solid #d2d2d7;border-radius:14px;padding:20px;background:#fff}.board-summary strong{display:block;font-size:28px}.board-summary span{font-size:11px;color:#86868b;text-transform:uppercase;letter-spacing:1px}.review-grid details{background:#fff;border-color:#d2d2d7}.review-grid summary{display:flex;justify-content:space-between;align-items:center;gap:16px}.signoff-gate{margin-top:20px;border:1px solid #d2d2d7;border-radius:14px;padding:22px;background:#fff}.signoff-gate p{color:#86868b;margin-top:8px}.evidence-modal{position:fixed;inset:0;z-index:2000;background:rgba(0,0,0,.86);display:grid;place-items:center;padding:20px}.evidence-dialog{position:relative;width:min(720px,100%);max-height:88vh;overflow:auto;background:#1c1c1e;border:1px solid #333336;border-radius:18px;padding:28px}.evidence-dialog>button{position:absolute;right:18px;top:18px;background:#000;color:#fff;border:1px solid #333336;border-radius:9px;padding:8px 11px}.evidence-dialog h2{font-size:30px;margin:14px 80px 8px 0}.evidence-list{display:grid;gap:0;margin-top:20px;border:1px solid #333336;border-radius:12px;overflow:hidden}.evidence-list div{display:grid;grid-template-columns:170px 1fr;gap:16px;padding:12px 14px;border-bottom:1px solid #333336}.evidence-list div:last-child{border-bottom:0}.evidence-list dt{color:#86868b}.evidence-list dd{overflow-wrap:anywhere}.evidence-list a{color:#2997ff}@keyframes fadeIn{from{opacity:.25}to{opacity:1}}@media(max-width:768px){.nav{justify-content:flex-start;overflow-x:auto;padding:0 16px}.hero{padding-left:20px;padding-right:20px}.section,.section-inner{padding-left:20px;padding-right:20px}.governance-grid,.board-summary{grid-template-columns:1fr}.evidence-list div{grid-template-columns:1fr;gap:4px}.review-grid summary{align-items:flex-start;flex-direction:column}.model-tools input{min-width:100%}}@media print{.model-tools,.compliance-tabs,.evidence-modal{display:none!important}.compliance-panel[hidden]{display:block!important}.review-grid details,.evidence-summary details,.control-detail{break-inside:avoid}}
'''
html=html.replace('</style>',css+'</style>',1)

# Replace table renderer with evidence/status-aware output.
old_render=re.search(r"    function renderModelsTable\(\) \{.*?(?=    function renderCharts\(\))",html,re.S)
if not old_render: raise RuntimeError('renderModelsTable block missing')
new_render='''    let activeProofFilter = 'all';
    function proofClass(m){ return m.decisionUse === 'quarantine' ? 'quarantine' : 'dual'; }
    function proofLabel(m){
      if(m.proofStatus === 'provider-family-documented-plus-benchmark-snapshot') return 'Provider + benchmark';
      if(m.proofStatus === 'provider-family-documented-only') return 'Provider only';
      if(m.proofStatus === 'benchmark-snapshot-only') return 'Benchmark only';
      return 'Unverified';
    }
    function renderModelsTable() {
      const searchInput = document.getElementById('modelSearchInput');
      const input = searchInput ? searchInput.value.toLowerCase().trim() : '';
      document.getElementById('modelsTableBody').innerHTML = models.map(m => {
        if(input && !(`${m.name} ${m.vendor}`.toLowerCase().includes(input))) return '';
        if(activeProofFilter === 'dual' && m.decisionUse === 'quarantine') return '';
        if(activeProofFilter === 'quarantine' && m.decisionUse !== 'quarantine') return '';
        const tau = (m.tau === null || m.tau === undefined || Number(m.tau) === 0) ? 'N/A' : m.tau;
        const intel = (m.intel === null || m.intel === undefined || Number(m.intel) === 0) ? 'N/A' : m.intel;
        const speed = (m.tps === null || m.tps === undefined || Number(m.tps) === 0) ? 'N/A' : `${m.tps} tps`;
        const mismatch = m.metricMismatches.length ? `<div style="color:#ffd60a;font-size:10px;margin-top:5px">${m.metricMismatches.length} metric gap(s)</div>` : '';
        return `<tr data-proof="${proofClass(m)}">
          <td style="padding:16px"><a href="${m.link}" style="color:#fff;font-weight:700">${m.name}</a>${mismatch}<div style="font-size:10px;color:#86868b;margin-top:5px">Click a metric or proof badge for evidence</div></td>
          <td style="color:#86868b;padding:16px">${m.vendor}</td>
          <td onclick="openEvidenceModal('${m.id}','tau')" tabindex="0" role="button" style="color:#30d158;font-weight:800;padding:16px;cursor:pointer">${tau}</td>
          <td onclick="openEvidenceModal('${m.id}','intel')" tabindex="0" role="button" style="font-weight:700;padding:16px;cursor:pointer">${intel}</td>
          <td onclick="openEvidenceModal('${m.id}','input')" tabindex="0" role="button" style="color:#30d158;font-weight:700;padding:16px;cursor:pointer">₹${m.inInr}</td>
          <td onclick="openEvidenceModal('${m.id}','output')" tabindex="0" role="button" style="padding:16px;cursor:pointer">₹${m.outInr}</td>
          <td onclick="openEvidenceModal('${m.id}','tps')" tabindex="0" role="button" style="color:#2997ff;padding:16px;cursor:pointer">${speed}</td>
          <td style="padding:16px"><button class="proof-badge ${proofClass(m)}" onclick="openEvidenceModal('${m.id}','proof')" type="button">${proofLabel(m)}</button></td>
        </tr>`;
      }).join('');
    }

'''
html=html[:old_render.start()]+new_render+html[old_render.end():]

# Fail-closed simulator: no silent model fallback and no universal cache discount.
html=html.replace("      const modA = models.find(m => m.id === modA_id) || models[0];\n      const modB = models.find(m => m.id === modB_id) || models[1];","      const modA = models.find(m => m.id === modA_id);\n      const modB = models.find(m => m.id === modB_id);\n      if (!modA || !modB) { throw new Error('Unknown model ID: calculation blocked'); }\n      if (cachePct > 0) {\n        const savingsElem=document.getElementById('savingsText');\n        if(savingsElem) savingsElem.innerText='Blocked: exact cache rate not validated';\n        const descElem=document.getElementById('savingsDesc')||document.getElementById('verdictText');\n        if(descElem) descElem.innerText='Set cache reuse to 0%. Provider-, SKU-, region- and TTL-specific cache pricing must be attached before discounted calculations run.';\n        return;\n      }")
html=html.replace('value="80" oninput="updateLabels(); runSim();"','value="0" oninput="updateLabels(); runSim();"',1)

# Interaction/evidence functions inserted before window.onload.
marker='    window.onload = function() {'
functions=f'''    const ACTIVE_FX = {str(FX)};
    let lastEvidenceFocus = null;
    function openEvidenceModal(modelId, metric) {{
      const m=models.find(x=>x.id===modelId); if(!m) return;
      lastEvidenceFocus=document.activeElement;
      const auditLabel=proofLabel(m);
      document.getElementById('evModelName').textContent=m.name;
      document.getElementById('evMetricTitle').textContent=`${{metric.toUpperCase()}} evidence · ${{m.vendor}}`;
      const status=document.getElementById('evStatus'); status.textContent=auditLabel; status.className=`status ${{m.decisionUse==='quarantine'?'contradicted':'verified'}}`;
      const link=document.getElementById('evSourceLink');link.href=m.sourceUrl||'#';link.textContent=m.sourceName||'Official source unavailable';
      document.getElementById('evTimestamp').textContent=m.retrievalDate||'Not retrieved';
      document.getElementById('evSig').textContent=m.sourceSha256||'No retained official snapshot hash';
      document.getElementById('evBenchmark').textContent=m.benchmarkExact?(m.benchmarkFresh?'Exact row in freshly retrieved snapshot':'Exact row in retained snapshot; fresh API refresh unavailable'):'No exact benchmark row';
      document.getElementById('evMetricCheck').textContent=m.metricMismatches.length?`Gaps: ${{m.metricMismatches.join(', ')}}`:'Database values match retained benchmark snapshot within rounding tolerance';
      document.getElementById('evDecisionUse').textContent=m.decisionUse==='quarantine'?'Quarantined — do not use for procurement/routing decision':'Eligible for further task, price and deployment validation';
      const modal=document.getElementById('evidenceModal');modal.hidden=false;modal.querySelector('.evidence-dialog').focus();
    }}
    function closeEvidenceModal() {{ const modal=document.getElementById('evidenceModal');modal.hidden=true;if(lastEvidenceFocus)lastEvidenceFocus.focus(); }}
    function initEvidenceInteractions() {{
      document.getElementById('evidenceClose').addEventListener('click',closeEvidenceModal);
      document.getElementById('evidenceModal').addEventListener('click',e=>{{if(e.target.id==='evidenceModal')closeEvidenceModal();}});
      document.addEventListener('keydown',e=>{{if(e.key==='Escape'&&!document.getElementById('evidenceModal').hidden)closeEvidenceModal();if((e.key==='Enter'||e.key===' ')&&e.target.matches('[role="button"][onclick*="openEvidenceModal"]')){{e.preventDefault();e.target.click();}}}});
      document.getElementById('modelSearchInput').addEventListener('input',renderModelsTable);
      document.querySelectorAll('.proof-filter').forEach(b=>b.addEventListener('click',()=>{{activeProofFilter=b.dataset.proof;document.querySelectorAll('.proof-filter').forEach(x=>x.classList.toggle('active',x===b));renderModelsTable();}}));
      document.querySelectorAll('[data-compliance-tab]').forEach(btn=>btn.addEventListener('click',()=>{{document.querySelectorAll('[data-compliance-tab]').forEach(x=>x.setAttribute('aria-selected',String(x===btn)));document.querySelectorAll('[data-compliance-panel]').forEach(p=>{{const active=p.dataset.compliancePanel===btn.dataset.complianceTab;p.hidden=!active;p.classList.toggle('active',active);}});}}));
    }}

'''
html=html.replace(marker,functions+marker,1)
html=html.replace('      renderModelsTable();\n      if(typeof initKnowledgeGraph','      renderModelsTable();\n      initEvidenceInteractions();\n      if(typeof initKnowledgeGraph',1)

# Footer and stale formula wording.
html=html.replace('Based on Artificial Analysis Official REST API v2 &amp; Primary Vendor Evidence',f'Provider documentation retrieved {STAMP} · ECB FX reference {FX_DATE} · retained Artificial Analysis benchmark snapshot')
html=html.replace('Price in INR = Rate (USD) * 96.610 Exchange Rate. Prompt Caching Rate = Base Rate * 0.10 (90% read discount).',f'Price in INR = provider/benchmark USD rate × ECB {FX_DATE} cross-rate ({FX_DISPLAY}). Cache and batch discounts are excluded until exact SKU terms are validated.')

HTML.write_text(html)
print(json.dumps({'updated':str(HTML),'archive':str(archive),'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'new_sha256':hashlib.sha256(HTML.read_bytes()).hexdigest(),'models':len(models),'fx':str(FX_DISPLAY)},indent=2))
