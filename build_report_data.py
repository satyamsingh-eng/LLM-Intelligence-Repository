#!/usr/bin/env python
"""Build the evidence-governed dataset consumed by the canonical report.

No external claim is promoted to VERIFIED unless its evidence record is present,
retrievable, content-addressed, and claim-specific. Financial calculations remain
locked whenever source pricing or the exchange rate is unverified.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MODELS = ROOT / "models"
AUDIT = ROOT / "audit"
NOW = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

STATUS = {
    "verified": "Verified",
    "calculated": "Calculated",
    "assumed": "Assumption",
    "scenario": "Scenario",
    "unsupported": "Unsupported",
    "contradicted": "Contradicted",
    "stale": "Stale",
    "blocked": "Verification blocked",
}

claims = [
    {"id":"C-001","section":"Header","claim":"The report empirically evaluated 586 global models.","status":"unsupported","severity":"critical","reason":"A raw third-party feed was ingested; ingestion is not an empirical evaluation and no per-model validation record exists.","action":"Removed from executive claims."},
    {"id":"C-002","section":"Header / Models","claim":"37 models are verified frontier models.","status":"contradicted","severity":"critical","reason":"The previous UI contained 35 models, the master file contained 37, and claim-specific vendor evidence was absent.","action":"Model ranking and pricing tables quarantined."},
    {"id":"C-003","section":"Header / Pricing","claim":"1 USD = ₹96.61 is a live verified exchange rate.","status":"unsupported","severity":"critical","reason":"The value was hardcoded; repository files also contain ₹83.50 and ₹83.05. No accepted timestamped FX evidence is stored.","action":"INR calculations locked until a timestamped source is ingested."},
    {"id":"C-004","section":"Header / QA","claim":"The prior report passed a 100% quality gate and was production-ready.","status":"contradicted","severity":"critical","reason":"The previous validator checked string presence and file existence while browser interactions and evidence handlers were broken.","action":"Replaced with evidence-aware QA and a NO-GO decision."},
    {"id":"C-005","section":"Executive verdict","claim":"Kimi K3 ranks first on TAU Banking with a 0.3340 score.","status":"unsupported","severity":"critical","reason":"The claim is present in local data but lacks a preserved claim-specific benchmark payload and cross-source verification.","action":"Removed from routing decisions."},
    {"id":"C-006","section":"Executive verdict","claim":"The proposed route saves ₹24.64 lakh annually per 100,000 reports.","status":"unsupported","severity":"critical","reason":"The value depends on unverified model identities, prices, cache policy, token volumes, workload volume, and FX rate.","action":"Removed. Financial recommendations remain locked."},
    {"id":"C-007","section":"Architecture","claim":"DeepSeek V4 Pro has a strict 60 RPM limit that will trigger production HTTP 429 failures.","status":"unsupported","severity":"high","reason":"No official model/rate-limit evidence or measured load test is retained for this SKU.","action":"Converted to a generic capacity-test requirement."},
    {"id":"C-008","section":"Architecture","claim":"Gemini 3.6 Flash has unlimited Vertex AI SLAs.","status":"contradicted","severity":"critical","reason":"Unlimited service capacity is not a defensible cloud SLA statement; quota and provisioned-throughput terms are workload- and account-specific.","action":"Removed."},
    {"id":"C-009","section":"Use cases","claim":"Six wealth workflows have exact token counts, costs, and 10,000-account monthly bills.","status":"assumed","severity":"critical","reason":"The values are scenario inputs, not measurements from representative production traces.","action":"Replaced by instrumentation requirements and explicit scenario labels."},
    {"id":"C-010","section":"Financial simulator","claim":"A universal 80% cache-hit rate and 90% cache-read discount apply across selected models.","status":"contradicted","severity":"critical","reason":"Cache eligibility, minimum prefix, TTL, write price, read price, and discount vary by provider and model.","action":"Simulator locked until model-specific cache evidence exists."},
    {"id":"C-011","section":"Workflow simulator","claim":"Displayed token, cost, latency, and cache savings are production telemetry.","status":"contradicted","severity":"critical","reason":"Values were synthetic counters. Missing model IDs silently fell back to the first model, distorting cost.","action":"Simulator now demonstrates control flow only and labels all unmeasured telemetry as unavailable."},
    {"id":"C-012","section":"Benchmarks","claim":"The prior five charts are empirical and suitable for model selection.","status":"unsupported","severity":"critical","reason":"Chart values were embedded client-side without claim-level benchmark payloads, task definitions, dates, or confidence boundaries.","action":"Removed benchmark charts; added an audit-status visualization only."},
    {"id":"C-013","section":"Compliance","claim":"EU AI Act Article 15 strictly prohibits INT4 for financial risk scoring.","status":"contradicted","severity":"critical","reason":"Article 15 establishes accuracy, robustness, and cybersecurity obligations; the report had no legal source establishing a blanket INT4 prohibition.","action":"Removed and replaced with outcome-based validation guidance."},
    {"id":"C-014","section":"Compliance","claim":"Self-hosting in a private VPC guarantees 100% data sovereignty.","status":"contradicted","severity":"high","reason":"Sovereignty depends on identity, logging, backups, support access, keys, regions, subprocessors, and operating controls—not deployment location alone.","action":"Replaced with a control checklist."},
    {"id":"C-015","section":"Board review","claim":"Five virtual auditors unanimously approved the report with a 98.5/100 score.","status":"unsupported","severity":"critical","reason":"No calibrated scoring rubric or independent human sign-off exists.","action":"Removed. Automated agents are listed as reviewers, not approvers."},
    {"id":"C-016","section":"Product architecture","claim":"The production product implements the report's 37-model central pricing and routing engine.","status":"unsupported","severity":"critical","reason":"The inspected frontend exposes model selections and query allowances but does not prove the report's routing, pricing, or backend ledger logic.","action":"Separated current product evidence from target architecture."},
    {"id":"C-017","section":"Product usage","claim":"One workflow run deducts one query or a known number of raw tokens from the user allowance.","status":"unsupported","severity":"high","reason":"The frontend exposes remaining/limit counters and can_make_query, but not the backend deduction algorithm.","action":"Marked backend accounting as an open evidence gap."},
    {"id":"C-018","section":"Product usage","claim":"The UI contract exposes daily/monthly query limits, remaining balances, and can_make_query.","status":"verified","severity":"info","reason":"Directly observed in the inspected frontend API contract and usage UI.","action":"Retained with an internal-implementation evidence label."},
    {"id":"C-019","section":"HTML / Evidence","claim":"Every metric exposes an eight-point evidence inspector.","status":"contradicted","severity":"critical","reason":"Browser testing found openEvidenceModal and closeEvidenceModal undefined.","action":"Replaced with a working evidence drawer sourced from this claim register."},
    {"id":"C-020","section":"Knowledge base","claim":"A versioned local source repository retains downloaded snapshots.","status":"contradicted","severity":"high","reason":"The registry references snapshot files that are absent; only source_registry.json is present.","action":"Knowledge-base status shown as incomplete."},
    {"id":"C-021","section":"HTML / Accessibility","claim":"The report is enterprise-accessible.","status":"contradicted","severity":"high","reason":"Previous modals lacked dialog semantics, chart alternatives, focus management, keyboard activation, and print styling.","action":"New report implements semantic controls, focus states, Escape handling, responsive tables, and print CSS."},
    {"id":"C-022","section":"QA","claim":"String-presence checks prove links return HTTP 200 and JavaScript works.","status":"contradicted","severity":"critical","reason":"The old QA suite did not perform network requests or execute interaction handlers.","action":"New pipeline distinguishes static integrity, browser behavior, and external evidence availability."},
]

issues = [
    {"id":"I-001","severity":"critical","title":"No deployment-approved model or price corpus","decision":"NO-GO","owner":"Research","exit_criteria":"Each deployed model has a current official model page, official rate card, content hash, retrieval timestamp, SKU match, and one independent benchmark record."},
    {"id":"I-002","severity":"critical","title":"Financial calculations depend on unverified FX, price, cache, token, and volume inputs","decision":"LOCKED","owner":"Finance + Engineering","exit_criteria":"All inputs are source-backed; Python Decimal oracle and browser result reconcile exactly."},
    {"id":"I-003","severity":"critical","title":"Workflow telemetry was simulated and fallback routing corrupted costs","decision":"NO-GO","owner":"Engineering","exit_criteria":"Unknown model IDs fail closed; traces provide measured token, latency, tool, retry, and route data."},
    {"id":"I-004","severity":"high","title":"Backend credit deduction and reset policy are unknown","decision":"OPEN","owner":"Backend","exit_criteria":"Trace ledger model, atomic deduction, failure/refund, reset timezone, organization pooling, and workflow charging."},
    {"id":"I-005","severity":"high","title":"Local knowledge snapshots referenced by the registry are missing","decision":"OPEN","owner":"Research Ops","exit_criteria":"Immutable snapshots exist, hashes match, diffs are reproducible, and unchanged content is not re-downloaded."},
    {"id":"I-006","severity":"high","title":"Security and compliance assertions are not control-mapped","decision":"OPEN","owner":"Security + Legal","exit_criteria":"Vendor services and regions are mapped to official attestations, contract terms, data-flow diagrams, and customer control responsibilities."},
]

workflows = [
    {"id":"wf-lab-inbox","name":"Lab results inbox","classification":"Target architecture scenario","purpose":"Collect lab-result artifacts, extract fields, apply deterministic validations, update records, and prepare an approval-ready summary.","volume":None,"tokens":None,"cost_inr":None,"latency_seconds":None,"architecture":"Deterministic orchestration with bounded model-assisted extraction","steps":[
        {"name":"Receive artifact","type":"tool","control":"Authenticate source and preserve original file hash."},
        {"name":"Extract document fields","type":"model-assisted","control":"Use a verified multimodal/OCR service; retain page-level evidence."},
        {"name":"Validate schema and rules","type":"deterministic","control":"Reject missing, malformed, or out-of-range fields."},
        {"name":"Human approval","type":"human","control":"Required before external writeback or communication."},
        {"name":"Write and audit","type":"tool","control":"Idempotent write, immutable event log, and rollback handle."},
    ]},
    {"id":"wf-daily-summary","name":"Daily operations summary","classification":"Target architecture scenario","purpose":"Aggregate verified events into a concise management view.","volume":None,"tokens":None,"cost_inr":None,"latency_seconds":None,"architecture":"Deterministic aggregation; optional bounded summarization","steps":[
        {"name":"Load verified events","type":"tool","control":"Use source timestamps and deduplicate event IDs."},
        {"name":"Compute KPIs","type":"deterministic","control":"All arithmetic runs outside the model."},
        {"name":"Draft narrative","type":"model-assisted","control":"The model may explain calculated facts but cannot alter them."},
        {"name":"Publish internal view","type":"tool","control":"Show data freshness and missing-source warnings."},
    ]},
    {"id":"wf-repeat-lot","name":"Repeat lot detection","classification":"Deterministic candidate","purpose":"Detect exact and near-duplicate lot identifiers across records.","volume":None,"tokens":None,"cost_inr":None,"latency_seconds":None,"architecture":"Rules and database indexes first; model only for ambiguous text normalization","steps":[
        {"name":"Normalize identifiers","type":"deterministic","control":"Versioned normalization rules."},
        {"name":"Exact match","type":"deterministic","control":"Unique indexes and collision report."},
        {"name":"Ambiguity review","type":"human","control":"No automatic rejection on fuzzy similarity alone."},
    ]},
    {"id":"wf-two-lab","name":"Two-lab confirmation","classification":"High-control scenario","purpose":"Reconcile two independent lab results before a governed decision.","volume":None,"tokens":None,"cost_inr":None,"latency_seconds":None,"architecture":"Evidence reconciliation with hard stop on conflict","steps":[
        {"name":"Ingest both reports","type":"tool","control":"Require independent source identity and complete artifacts."},
        {"name":"Extract comparable fields","type":"model-assisted","control":"Attach bounding boxes or page references to each value."},
        {"name":"Reconcile","type":"deterministic","control":"Tolerance rules are explicit and versioned."},
        {"name":"Escalate conflict","type":"human","control":"Conflicts never auto-resolve through model judgment."},
    ]},
    {"id":"wf-proactive-comms","name":"Proactive lab communication","classification":"Approval-gated scenario","purpose":"Draft a communication from verified lab status and approved policy.","volume":None,"tokens":None,"cost_inr":None,"latency_seconds":None,"architecture":"Verified facts plus constrained drafting and mandatory approval","steps":[
        {"name":"Load approved facts","type":"tool","control":"No unsupported clinical or financial inference."},
        {"name":"Draft message","type":"model-assisted","control":"Template and prohibited-claim checks."},
        {"name":"Approve","type":"human","control":"Mandatory outbound approval."},
        {"name":"Send and log","type":"tool","control":"Only after explicit confirmation; store message ID and timestamp."},
    ]},
]

terms = [
    ("Input tokens","Units representing the prompt and supplied context.","Tokenizer-produced IDs processed during model prefill.","They drive context capacity, prefill latency, and usually input cost.","Pages handed to an analyst before work begins.","Measure actual provider usage; remove irrelevant context; never estimate billing from character count alone."),
    ("Output tokens","Units generated by the model.","Autoregressively decoded token IDs returned as visible or reasoning output according to provider accounting.","They drive response length, decode time, and usually higher unit cost.","Pages the analyst writes back.","Set task-specific limits; require concise structured outputs; read provider reasoning-token rules."),
    ("Token consumption","Input plus provider-billed generated tokens for a defined request or workflow.","Usage metadata aggregated across model calls, retries, tool loops, and hidden reasoning where reported.","The variable meter behind model spend.","Electricity consumed across every machine in a process.","Meter per call and workflow; separate successful, failed, retried, and cached usage."),
    ("Prompt caching","Provider reuse of a matching prompt prefix under provider-specific rules.","The service avoids some repeated prefill computation and bills cache writes/reads according to the SKU policy.","Can lower repeated-prefix cost and time, but only when requests are eligible and hits occur.","A clerk reuses a verified standard binder instead of rereading it.","Model TTL, minimum length, write/read rates, and measured hit rate must be stored per SKU."),
    ("Context window","Maximum token sequence a model can process for a request under a specific API configuration.","The bounded attention and state budget shared by instructions, documents, tools, conversation, and generated tokens.","Determines whether data fits, not whether the model will use every part reliably.","Desk space, not memory quality.","Reserve output headroom; test retrieval quality; prefer targeted context over indiscriminate dumps."),
    ("Embeddings","Vectors that encode semantic features of data.","Numeric representations compared with similarity metrics for retrieval, clustering, or classification.","Enable semantic search over internal content.","Map coordinates for meaning.","Evaluate on domain queries; combine with keyword search for IDs, names, and exact values."),
    ("Vector database","A store and index for vectors plus metadata.","A system that supports approximate or exact nearest-neighbor search with filters and lifecycle controls.","Retrieves candidate evidence quickly from large corpora.","A catalog that finds nearby meanings.","Enforce tenant isolation, source ACLs, deletion, versioning, and retrieval evaluation."),
    ("RAG","Retrieval-augmented generation.","An application retrieves evidence at request time and supplies it to a generator, usually with citations.","Updates knowledge without retraining and can improve grounding; it does not eliminate hallucination.","An open-book answer with selected pages.","Measure retrieval recall and answer faithfulness separately; expose source passages."),
    ("GraphRAG","Retrieval using explicit entities, relationships, and graph-derived summaries.","A pipeline extracts a graph and uses neighborhood/community retrieval for multi-hop questions.","Useful when relationships matter more than isolated text similarity.","A detective board connecting people, accounts, and events.","Use only when graph construction quality and update cost are justified; preserve source links per edge."),
    ("MCP","Model Context Protocol.","A client-server protocol for exposing tools, resources, and prompts to model applications.","Standardizes integration surfaces but does not replace authentication, authorization, or business logic.","A common connector shape, not automatic permission.","Treat every server as a privileged integration; scope credentials, validate outputs, and log calls."),
    ("Function calling","Model generation of arguments for an application-defined function schema.","The host provides schemas; the model proposes a function name and typed arguments; host code validates and executes.","Converts intent into controlled application actions.","The model fills a form; software decides whether to submit it.","Validate authorization, ranges, identifiers, idempotency, and side effects outside the model."),
    ("Tool calling","A broader pattern in which a model requests external operations.","The runtime executes approved tools and returns observations for subsequent model turns.","Enables agents to act, while increasing security and reliability requirements.","An analyst asks approved specialists for data.","Allowlist tools, separate read/write permissions, require approval for irreversible actions, and cap loops."),
    ("Structured outputs","Model outputs constrained to a declared schema.","Decoding or post-validation enforces a JSON-schema-like structure; semantic correctness remains separate.","Reduces parsing failures in integrations.","A completed form can still contain a wrong value.","Validate every field after generation; reject unknown enums, invalid dates, and unsupported claims."),
    ("Reasoning models","Models optimized to spend more inference effort on multi-step problems.","They may use additional internal or exposed reasoning tokens and test-time compute.","Can improve hard problem performance at added cost and latency; benchmark fit is task-specific.","A specialist who takes more scratch-work time.","Route only evaluated tasks; keep deterministic math and policy checks outside the model."),
    ("Mixture of Experts (MoE)","A model architecture that activates a subset of expert blocks for each token.","A learned router selects sparse feed-forward experts while the full parameter set may still require storage.","Can improve capability per unit of active compute; deployment complexity remains.","A dispatcher sends each case to selected specialists.","Do not infer price, latency, or quality from MoE architecture alone."),
    ("KV cache","Stored attention keys and values for previously processed tokens during inference.","It avoids recomputing prior sequence states during autoregressive generation; provider prompt caching is a separate commercial feature.","Improves decoding efficiency and shapes memory capacity.","Keeping working notes on the desk while writing.","Separate runtime KV management from provider cache billing in documentation and telemetry."),
    ("Streaming","Incremental delivery of generated events or tokens.","SSE, WebSocket, or chunked responses expose partial output before completion.","Improves perceived responsiveness but not necessarily total completion time.","Reading a document as pages arrive.","Handle cancellation, retries, partial JSON, moderation, and audit assembly."),
    ("Batch API","A provider-specific asynchronous request facility.","Requests are submitted and retrieved later under SKU-specific pricing, eligibility, limits, and completion targets.","Useful for non-interactive workloads when delay is acceptable.","Economy freight instead of same-day courier.","Verify the exact provider/model discount and SLA; never apply a universal discount."),
    ("Latency","Elapsed time for a defined operation.","Separate queue time, network time, time to first token, decode time, tools, retries, and orchestration critical path.","Determines user experience and SLA risk.","Door-to-door travel time, not vehicle speed alone.","Report percentile distributions from measured traces; simulations must remain labeled estimates."),
    ("Throughput","Work completed per unit time under stated load.","Requests or tokens processed across concurrent workloads, constrained by quotas, batching, hardware, and latency targets.","Determines capacity and unit economics.","Customers served per hour.","Load-test with realistic concurrency; report both system throughput and per-user latency."),
    ("Fine-tuning","Additional training that changes model weights or adapters for a task or behavior.","SFT, preference optimization, or parameter-efficient methods train on curated examples.","Can improve consistency but adds dataset, evaluation, governance, and maintenance obligations.","Training a general analyst on a house style.","Use RAG for changing facts; tune only after prompts and retrieval are baselined; retain holdout evaluations."),
    ("Agentic AI","A system that iterates across planning, tool use, observation, and control gates.","An orchestrator maintains state and invokes models/tools until completion, stop, or escalation.","Automates multi-step work but compounds errors and operational risk.","A supervised operator, not just a chatbot.","Bound scope, budget, steps, permissions, retries, and approvals; log every action."),
    ("Multi-agent systems","Multiple specialized agents coordinated around a shared objective.","Agents exchange tasks or artifacts through an orchestrator, queue, or shared state with explicit conflict rules.","Can parallelize work, but coordination cost and correlated errors can erase gains.","A project team with defined roles and a manager.","Use only when decomposition is real; require independent evidence and deterministic merge rules."),
    ("OCR","Conversion of document images into machine-readable text and layout information.","OCR may combine image preprocessing, text detection, recognition, layout analysis, and confidence scores.","Required before text-only models can reason over scans.","A clerk transcribes a photographed form.","Benchmark on actual document types; retain page coordinates and confidence; route low-confidence fields to review."),
    ("Vision models","Models that accept images or visual documents as input.","Multimodal encoders integrate pixel or patch representations with language generation.","Can interpret layout and images, but vision support does not prove OCR accuracy or compliance fitness.","An analyst who can see the page, not necessarily read every character perfectly.","Evaluate extraction accuracy, layout, handwriting, small text, and adversarial content separately."),
]

glossary=[]
for i,(term,simple,technical,business,analogy,best) in enumerate(terms,1):
    glossary.append({"id":f"T-{i:03d}","term":term,"simple_definition":simple,"technical_definition":technical,"business_meaning":business,"why_it_matters":business,"analogy":analogy,"enterprise_example":f"In SARVAX, {term.lower()} should be used only inside a measured, governed workflow with source and audit records.","common_mistake":"Treating the concept as a guarantee or applying provider-specific behavior universally.","best_practices":best,"verification_status":"stable_definition_source_refresh_pending"})

sources = [
    {"id":"S-OPENAI-MODELS","tier":1,"publisher":"OpenAI","title":"Models documentation","url":"https://platform.openai.com/docs/models","status":"retrieval_blocked_this_run","claim_scope":"Current public model names and capabilities"},
    {"id":"S-OPENAI-PRICE","tier":1,"publisher":"OpenAI","title":"API pricing","url":"https://openai.com/api/pricing/","status":"retrieval_blocked_this_run","claim_scope":"Public API pricing and batch/cache terms"},
    {"id":"S-ANTHROPIC-MODELS","tier":1,"publisher":"Anthropic","title":"Claude models overview","url":"https://docs.anthropic.com/en/docs/about-claude/models/overview","status":"retrieval_blocked_this_run","claim_scope":"Current Claude model names and capabilities"},
    {"id":"S-ANTHROPIC-PRICE","tier":1,"publisher":"Anthropic","title":"Pricing","url":"https://www.anthropic.com/pricing","status":"retrieval_blocked_this_run","claim_scope":"Claude pricing and commercial cache terms"},
    {"id":"S-GOOGLE-MODELS","tier":1,"publisher":"Google","title":"Gemini models","url":"https://ai.google.dev/gemini-api/docs/models","status":"retrieval_blocked_this_run","claim_scope":"Current Gemini models and capabilities"},
    {"id":"S-GOOGLE-PRICE","tier":1,"publisher":"Google","title":"Gemini API pricing","url":"https://ai.google.dev/gemini-api/docs/pricing","status":"retrieval_blocked_this_run","claim_scope":"Gemini pricing and caching"},
    {"id":"S-DEEPSEEK","tier":1,"publisher":"DeepSeek","title":"API documentation and pricing","url":"https://api-docs.deepseek.com/quick_start/pricing","status":"retrieval_blocked_this_run","claim_scope":"DeepSeek model, pricing, and limits"},
    {"id":"S-MOONSHOT","tier":1,"publisher":"Moonshot AI","title":"Platform documentation","url":"https://platform.moonshot.cn/docs","status":"retrieval_blocked_this_run","claim_scope":"Kimi model identity, pricing, and API behavior"},
    {"id":"S-AWS-BEDROCK","tier":1,"publisher":"AWS","title":"Amazon Bedrock security and compliance","url":"https://aws.amazon.com/bedrock/security-compliance/","status":"retrieval_blocked_this_run","claim_scope":"AWS-managed control scope and attestations"},
    {"id":"S-INTERNAL-CODE","tier":1,"publisher":"C3A Labs","title":"Inspected frontend implementation","url":None,"status":"locally_verified","claim_scope":"Frontend contracts and UI behavior only; not backend accounting"},
]

# Evidence ledger is deliberately conservative.
evidence_summary = Counter(c["status"] for c in claims)
severity_summary = Counter(c["severity"] for c in claims)

report = {
    "metadata": {
        "title":"SARVAX Enterprise AI Intelligence — Founder Validation Edition",
        "version":"63.0-validation",
        "generated_at":NOW,
        "decision":"NO-GO for model procurement, pricing commitments, or production routing",
        "scope":"Entire canonical report, calculation layer, workflow data, QA pipeline, and inspected frontend contract",
        "method":"Claim-level classification with fail-closed evidence rules",
        "external_research_status":"Official-source retrieval blocked by execution permission during this run; no current external claim was promoted.",
        "source_of_truth":"models/report_data.json generated by build_report_data.py",
        "currency_status":"LOCKED — no timestamped accepted USD/INR source",
        "model_catalog_status":"QUARANTINED — raw/secondary records are not deployment-approved",
    },
    "status_definitions": STATUS,
    "claim_summary": dict(evidence_summary),
    "severity_summary": dict(severity_summary),
    "claims": claims,
    "issues": issues,
    "workflows": workflows,
    "glossary": glossary,
    "sources": sources,
    "architecture": {
        "current_proven":{"title":"What the inspected frontend proves","items":["Daily and monthly query allowance fields are exposed to the UI.","A can_make_query gate exists in the frontend contract.","The frontend contains model selection and workflow UI contracts.","The frontend alone does not prove backend routing, token metering, pricing, or deductions."]},
        "target":{"title":"Recommended evidence-governed architecture","items":["Deterministic orchestration owns state, policy, math, retries, and approvals.","Model gateway uses only verified SKUs and fails closed on unknown model IDs.","Tool gateway enforces identity, authorization, idempotency, and outbound approval.","Telemetry records provider usage, route, tools, retries, latency stages, cache events, and evidence IDs.","Finance engine reads versioned official rates and prices; HTML performs no business calculations.","Evidence registry stores immutable snapshots, hashes, claim links, retrieval dates, and supersession history."]},
    },
    "financial_model": {
        "status":"locked",
        "reason":"No decision-useful INR value can be shown until model SKU, official input/output/cache rates, timestamped FX, measured token traces, and workload volume are all verified.",
        "formula":"cost_inr = runs × Σsteps[((uncached_input_tokens × input_usd_per_million) + (cached_input_tokens × cached_read_usd_per_million) + (output_tokens × output_usd_per_million)) ÷ 1,000,000] × usd_inr",
        "required_inputs":["Exact provider SKU","Official rate-card effective date","Input/output token usage from provider response","Cache-write/read eligibility and measured hit events","Retries and failed requests","Timestamped USD/INR rate","Scenario or measured monthly run volume"],
    },
    "qa_expectation": {
        "acceptance_rule":"The report can pass integrity QA while retaining a NO-GO executive decision. QA must never turn missing evidence into approval.",
        "required_gates":["JSON schema and cross-file consistency","No unsupported number presented as fact","No hardcoded business metric in HTML","Unknown model IDs fail closed","Decimal arithmetic oracle","Browser console and interaction tests","Keyboard and dialog accessibility","Responsive and print checks","Link and snapshot verification when network permission exists","Executive readability and change log"],
    },
}

# Attach a deterministic digest over the business dataset, excluding the digest itself.
canonical=json.dumps(report,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
report["metadata"]["dataset_sha256"]=hashlib.sha256(canonical).hexdigest()
MODELS.mkdir(exist_ok=True)
(MODELS/"report_data.json").write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
(AUDIT/"claim_register.json").write_text(json.dumps({"generated_at":NOW,"claims":claims},indent=2,ensure_ascii=False),encoding="utf-8")
(AUDIT/"source_register.json").write_text(json.dumps({"generated_at":NOW,"sources":sources},indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps({"output":"models/report_data.json","claims":len(claims),"issues":len(issues),"workflows":len(workflows),"glossary_terms":len(glossary),"sha256":report["metadata"]["dataset_sha256"]},indent=2))
