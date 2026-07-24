# Unresolved Questions Register: Missing Intelligence & Research Gaps (2026 Edition)

**Author:** Research Gap Agent (LLM Intelligence Repository)  
**Publication Date:** July 2026  
**Target Scope:** Global LLM Intelligence Repository — Vendor Gaps, Benchmark Deficits, Compliance Frameworks, and Routing Edge-Cases  
**Status:** Active Research Tracking Ledger (Version 2.0)  

---

## Executive Summary

As of July 2026, while open-weight pioneers (GLM-4.7, DeepSeek-V3/R1, Qwen-2.5/3.7) and closed frontier labs (OpenAI GPT-5.x, Anthropic Claude 4.x, Google Gemini 3) have established transparent technical and economic baselines, significant **intelligence blind spots** persist across the global AI landscape. 

This register tracks every unresolved unknown across **six missing vendor ecosystems** (Tencent Hunyuan, Baidu ERNIE, SenseTime SenseNova, AI21 Jamba, Aleph Alpha, Amazon Nova) and **two critical enterprise compliance/regulatory frameworks** (EU AI Act, FedRAMP High/Moderate), as well as missing standardized benchmarks and routing edge-cases.

### Summary of Key Intelligence Blind Spots
1. **Chinese Tech Conglomerates (Tencent, Baidu, SenseTime):** Severe information deficit caused by opaque enterprise sales channels, lack of third-party SWE-bench / LMSYS Arena participation, and non-existent self-service global developer APIs.
2. **Niche Frontier & Hybrid Architectures (AI21 Jamba, Aleph Alpha):** Absence of standardized agentic coding benchmarks for state-space model (SSM)-Transformer hybrids (Jamba) and EU sovereign explainability models (Aleph Alpha Pharia).
3. **Hyperscaler Native Models (Amazon Nova):** Missing independent benchmark verification on SWE-bench Verified, GPQA Diamond, and MMMU across the Nova model family (Micro, Lite, Pro, Premier, Omni), alongside unconfirmed cross-region AWS Bedrock provisioned throughput rate cards.
4. **Regulatory & Compliance Enforcement Frameworks:**
   - **EU AI Act:** Opaque classification of general-purpose AI (GPAI) models with systemic risk (>10^25 FLOPs training compute threshold), unverified copyright training data summaries, and unmapped technical conformity assessment procedures for open-weight vs. closed commercial deployments.
   - **FedRAMP Compliance:** Missing primary-source Authority to Operate (ATO) verification for direct vendor API endpoints, Zero Data Retention (ZDR) guarantees under FedRAMP High, and explicit agency sponsorship status for non-hyperscaler frontier models.

---

## 1. Master Unknowns Register Matrix

| Unknown ID | Target Entity / Subject | Category | Specific Missing Data Point / Question | Severity / Impact | Data Confidence | Recommended Verification Agent / Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UNK-TH-001** | Tencent Hunyuan | Benchmark | Verified SWE-bench Verified, LiveCodeBench, and HumanEval scores for Hunyuan-Pro and Hunyuan-Large. | **High** | **20%** | Automated Playwright probe on Tencent Cloud evaluation platform + repo testing. |
| **UNK-TH-002** | Tencent Hunyuan | Pricing / Econ | Transparent per-token self-service rate card for Hunyuan-Pro MoE vs. custom B2B enterprise tier quotes. | **Medium** | **30%** | Web scraper (Crawl4AI) targeting Tencent Cloud API pricing pages. |
| **UNK-TH-003** | Tencent Hunyuan | Architecture | Active expert counts, total parameters, and KV cache memory scaling beyond 256K context window. | **Medium** | **15%** | Technical paper audit & Hunyuan API response latency profiling under varying context. |
| **UNK-BE-001** | Baidu ERNIE | Benchmark | Independent LMSYS Chatbot Arena and SWE-bench evaluations for ERNIE 4.0 Turbo and ERNIE 5.0. | **High** | **15%** | Anonymous API benchmarking via LMSYS evaluation harness or proxy router. |
| **UNK-BE-002** | Baidu ERNIE | Access / Compliance | Global API billing options without Mainland China identity verification (+86 mobile / Citizen ID). | **High** | **10%** | Enterprise sales inquiry & Qianfan Cloud international developer portal audit. |
| **UNK-BE-003** | Baidu ERNIE | Architecture | MoE parameter distribution, training compute FLOPs, and CAC algorithmic registration disclosure data. | **Low** | **25%** | Scrape CAC algorithm registration public registry (`cac.gov.cn`). |
| **UNK-SN-001** | SenseTime SenseNova | Benchmark | Standardized agentic coding and multi-file refactoring scores for SenseNova 5.5 / 6.0. | **Medium** | **20%** | Benchmark load test using standardized Python evaluation harness. |
| **UNK-SN-002** | SenseTime SenseNova | Pricing / Econ | Self-service per-token pricing table for text and vision multimodal API SKUs. | **Medium** | **25%** | B2B sales inquiry & SenseNova Cloud portal scraping. |
| **UNK-J2-001** | AI21 Jamba | Benchmark | SWE-bench Verified, GPQA Diamond, and MMLU-Pro scores for Jamba 1.5 Mini / Instruct (SSM-Transformer). | **High** | **35%** | Direct evaluation via AI21 Studio API and AWS Bedrock API endpoints. |
| **UNK-J2-002** | AI21 Jamba | Performance | Memory footprint, TTFT (Time To First Token), and throughput scaling of SSM hybrid layers at 256K context. | **High** | **40%** | Latency and throughput benchmarking comparing Jamba against pure Transformer MoE (DeepSeek-V3). |
| **UNK-J2-003** | AI21 Jamba | Pricing / Econ | Comparative pricing breakdown across AI21 Studio, AWS Bedrock, and Azure Marketplace. | **Medium** | **50%** | Rate-card aggregator audit across cloud marketplaces. |
| **UNK-AA-001** | Aleph Alpha | Benchmark | Independent GPQA Diamond, SWE-bench, and MMLU-Pro scores for Pharia-1-LLM and Luminous series. | **High** | **30%** | API evaluation pass on Aleph Alpha API / sovereign deployment. |
| **UNK-AA-002** | Aleph Alpha | Compliance / EU | Technical conformity with EU AI Act Article 53 (GPAI transparency & copyright summarization). | **Critical** | **35%** | Legal and technical audit of Aleph Alpha compliance whitepapers and data provenance disclosures. |
| **UNK-AA-003** | Aleph Alpha | Feature / Tech | Commercial availability and latency overhead of AtMan token-level explainability/auditing features. | **Medium** | **40%** | Technical API feature testing via Python client SDK. |
| **UNK-AN-001** | Amazon Nova | Benchmark | Standardized SWE-bench Verified, GPQA Diamond, and MMMU scores across Nova Micro, Lite, Pro, Premier, Omni. | **Critical** | **25%** | Automated evaluation harness execution on AWS Bedrock Nova model endpoints. |
| **UNK-AN-002** | Amazon Nova | Pricing / Econ | Provisioned Throughput vs. Pay-as-you-go rate card, prompt caching discount, and Batch API pricing. | **High** | **40%** | AWS Bedrock pricing documentation scraper & AWS CLI price list API query. |
| **UNK-AN-003** | Amazon Nova | Compliance | FedRAMP High / Moderate ATO status and HIPAA BAA coverage across AWS GovCloud regions. | **Critical** | **45%** | Audit AWS Compliance Artifact Manager and FedRAMP Marketplace portal. |
| **UNK-EUA-001** | EU AI Act | Regulatory | List of frontier models exceeding 10^25 FLOPs training compute threshold triggering Systemic Risk rules. | **Critical** | **30%** | Regulatory tracking pass across EU AI Office publications and vendor technical reports. |
| **UNK-EUA-002** | EU AI Act | Compliance | Open-weight exemption boundaries (Article 2(12)) vs commercial deployment obligations under EU AI Act. | **High** | **40%** | Legal analysis of open-weight licenses (Apache 2.0 vs Qwen/Llama custom) under EU AI Act. |
| **UNK-EUA-003** | EU AI Act | Enforcement | Standards and technical specifications for machine-readable synthetic content watermarking (Article 50). | **Medium** | **20%** | Review C2PA and EU AI Office draft codes of practice. |
| **UNK-FED-001** | FedRAMP | Compliance | Verification of direct vendor API endpoints (OpenAI, Anthropic, DeepSeek) with FedRAMP High/Moderate ATO. | **Critical** | **35%** | FedRAMP Marketplace database query (`marketplace.fedramp.gov`). |
| **UNK-FED-002** | FedRAMP | Security | Zero Data Retention (ZDR) and customer payload logging policies under FedRAMP GovCloud enclaves. | **Critical** | **30%** | Vendor CISO security package audit and BAA/GovCloud agreement review. |
| **UNK-FED-003** | FedRAMP | Sovereignty | FIPS 140-3 validated cryptographic module implementation across managed LLM inference gateways. | **High** | **25%** | NIST Computer Security Resource Center (CSRC) cryptographic module verification. |
| **UNK-BM-001** | Multi-Vendor | Benchmark | Agentic tool-use stability benchmark across 200+ sequential tool calls for long-horizon enterprise workflows. | **High** | **15%** | Development of custom agentic stress-testing evaluation suite. |
| **UNK-RT-001** | Routing | Strategy | Optimal multi-region routing rule for EU AI Act compliance + FedRAMP High fallback with sub-500ms TTFT. | **High** | **20%** | Architecture simulation and empirical API latency testing. |

---

## 2. Detailed Domain Deep Dives into Missing Intelligence

### 2.1 Tencent Hunyuan (腾讯混元) Series

#### Current Intelligence Summary
Tencent Hunyuan is deployed across Tencent Cloud, WeChat Work, Tencent Meeting, and domestic B2B enterprise suites. It operates Hunyuan-Large (MoE architecture with 389B total parameters, 52B active parameters per token) and Hunyuan-Pro, claiming a 256K native context window.

#### Explicit Data Gaps & Unresolved Questions
1. **Agentic Coding Evaluation Deficit (UNK-TH-001):**
   - *Question:* What is Hunyuan-Pro’s exact performance on SWE-bench Verified and LiveCodeBench?
   - *Context:* Tencent claims strong performance on domestic Chinese coding benchmarks (C-Eval, HumanEval-CN), but has withheld submission to standardized multi-file repository benchmarks (SWE-bench Verified). Without this, Hunyuan cannot be evaluated for automated software refactoring.
2. **Enterprise Pricing Transparency (UNK-TH-002):**
   - *Question:* What is the exact pay-as-you-go per-token rate for Hunyuan-Pro on Tencent Cloud?
   - *Context:* Public pricing is hidden behind customized B2B enterprise cloud packages, preventing transparent token economics comparisons against DeepSeek-V3 ($0.14/$0.28) or Qwen-2.5-72B ($0.30/$0.90).
3. **Architecture & Long-Context Retention Mechanics (UNK-TH-003):**
   - *Question:* Does Hunyuan maintain linear memory overhead and sub-100ms TTFT beyond 128K tokens?
   - *Context:* Technical details regarding sparse attention mechanisms, MLA implementation, or KV cache compression remain unpublished.

---

### 2.2 Baidu ERNIE (百度文心一言 4.0 / 5.0)

#### Current Intelligence Summary
Baidu’s ERNIE platform is served via the Baidu AI Cloud (Qianfan Platform), featuring ERNIE 4.0 Turbo and ERNIE 5.0 preview models. It emphasizes native multi-modal integration and domestic enterprise knowledge graph retrieval.

#### Explicit Data Gaps & Unresolved Questions
1. **Verifiable Standardized Evals (UNK-BE-001):**
   - *Question:* Where does ERNIE 4.0/5.0 rank on LMSYS Chatbot Arena and SWE-bench Verified under independent audit?
   - *Context:* Baidu does not participate in transparent LMSYS evaluation under verifiable IDs. Benchmark claims rely on internal Baidu evaluation papers, which exhibit high variance when tested independently.
2. **Global Developer Accessibility & Geofencing (UNK-BE-002):**
   - *Question:* Can international enterprises deploy ERNIE via self-service API using non-+86 credentials and global billing?
   - *Context:* Qianfan Cloud enforces strict Mainland China real-name identity verification (+86 mobile / domestic citizen ID / CAC filing), excluding non-domestic developers without specialized B2B enterprise contracts.
3. **Training & Architectural Efficiency (UNK-BE-003):**
   - *Question:* What are the exact active parameter counts, expert routing strategies, and training compute requirements for ERNIE 4.0/5.0?
   - *Context:* Architectural specifics are kept proprietary, preventing comparative research into MoE efficiency vs DeepSeekMoE or Qwen MoE.

---

### 2.3 SenseTime SenseNova (商汤日日新 5.5 / 6.0)

#### Current Intelligence Summary
SenseTime’s SenseNova suite targets enterprise vision-language applications, smart city infrastructure, and B2B enterprise automation. SenseNova 5.5 boasts a 1M token context window and specialized multimodal capabilities.

#### Explicit Data Gaps & Unresolved Questions
1. **Coding & Agentic Benchmarks (UNK-SN-001):**
   - *Question:* How does SenseNova 5.5 perform on standardized agentic benchmarks (SWE-bench, GAIA, AgentBench)?
   - *Context:* SenseTime focuses marketing on vision and document processing benchmarks, omitting software engineering evaluations.
2. **Public Self-Service Rate Cards (UNK-SN-002):**
   - *Question:* What are the per-1M-token input/output costs for SenseNova text and multimodal endpoints?
   - *Context:* Commercial terms require direct engagement with SenseTime B2B sales reps, creating high friction for platform engine integration and dynamic cost routing.

---

### 2.4 AI21 Jamba (AI21 Labs - Hybrid SSM-Transformer)

#### Current Intelligence Summary
AI21 Labs (Israel) introduced the Jamba model family (Jamba 1.5 Mini, Jamba 1.5 Large), pioneering a joint **Joint Attention and Mamba (SSM)** architecture. Jamba interleaves Mamba state-space model layers with classic Transformer attention layers and MoE routing, aiming for 256K context windows with a significantly smaller memory footprint during inference.

```
       ┌─────────────────────────────────────────────────────────┐
       │             Jamba Hybrid Architecture Block             │
       └────────────────────────────┬────────────────────────────┘
                                    │
           ┌────────────────────────┴────────────────────────┐
           │                                                 │
           ▼                                                 ▼
┌─────────────────────────────┐                   ┌─────────────────────────────┐
│    Mamba SSM Layers (80%)   │                   │  Transformer Attention (20%)│
├─────────────────────────────┤                   ├─────────────────────────────┤
│ • Linear time complexity O(N)│                  │ • Quadratic precision O(N²) │
│ • Ultra-low memory KV cache │                   │ • High-fidelity retrieval   │
│ • High throughput processing│                   │ • Long-range reasoning      │
└─────────────────────────────┘                   └─────────────────────────────┘
```

#### Explicit Data Gaps & Unresolved Questions
1. **Standardized Benchmark Verification (UNK-J2-001):**
   - *Question:* How does Jamba 1.5 Large score on SWE-bench Verified, GPQA Diamond, and MMLU-Pro compared to pure MoE models (DeepSeek-V3, Qwen-2.5-72B)?
   - *Context:* While AI21 published internal evaluations showing competitive MMLU and Needle-In-A-Haystack results, independent multi-file agentic coding benchmarks remain unverified.
2. **SSM Inference Latency & Memory Efficiency (UNK-J2-002):**
   - *Question:* What is the exact KV cache memory reduction and TTFT advantage of Jamba at 256K context compared to Claude Sonnet 4.6 or Gemini 3 Pro?
   - *Context:* The theoretical advantage of Mamba SSM layers (80% reduction in KV cache size) needs empirical load-testing validation under concurrent enterprise request streams.
3. **Multi-Cloud Marketplace Pricing Variance (UNK-J2-003):**
   - *Question:* What is the exact price-per-token delta between direct AI21 Studio API, AWS Bedrock, and Azure Marketplace deployments?
   - *Context:* Pricing across cloud marketplaces shows undocumented variances depending on region and enterprise commit tiers.

---

### 2.5 Aleph Alpha (Luminous / Pharia - EU Sovereign AI)

#### Current Intelligence Summary
Aleph Alpha (Heidelberg, Germany) focuses on European sovereign AI deployments, data privacy, and explainability for government and enterprise clients. Its flagship models include Pharia-1-LLM and the Luminous series, featuring native AtMan token-level explainability vectors.

#### Explicit Data Gaps & Unresolved Questions
1. **Frontier Benchmark Parity (UNK-AA-001):**
   - *Question:* What are Pharia-1-LLM’s scores on GPQA Diamond, SWE-bench Verified, and HumanEval?
   - *Context:* Public benchmark coverage is limited. Existing data suggests Pharia trails top open-weight models (GLM-4.7, Qwen-2.5-72B) on reasoning and coding, but authoritative third-party evaluation is missing.
2. **EU AI Act Article 53 Technical Compliance (UNK-AA-002):**
   - *Question:* Does Aleph Alpha provide full copyright training data summaries and technical documentation required for general-purpose AI models under EU AI Act Article 53?
   - *Context:* As a leading EU AI vendor, Aleph Alpha’s compliance artifacts serve as a benchmark for European enterprise adoption, but public availability of these audit packages remains incomplete.
3. **AtMan Explainability Overhead (UNK-AA-003):**
   - *Question:* What is the latency and token cost penalty when enabling AtMan explainability vector calculations during real-time inference?
   - *Context:* Explainability features increase computational overhead, but exact performance metrics for real-time applications are undocumented.

---

### 2.6 Amazon Nova (AWS Native Model Family)

#### Current Intelligence Summary
Amazon Nova represents AWS’s proprietary model family deployed natively on AWS Bedrock. The family spans **Amazon Nova Micro** (text-only, fast), **Amazon Nova Lite** (cost-effective multimodal), **Amazon Nova Pro** (multimodal workhorse), **Amazon Nova Premier** (frontier reasoning/agentic), and **Amazon Nova Omni** (native speech, vision, text multimodal).

#### Explicit Data Gaps & Unresolved Questions
1. **Independent Benchmark Audit across SKUs (UNK-AN-001):**
   - *Question:* What are the exact scores for Nova Micro, Lite, Pro, Premier, and Omni on SWE-bench Verified, GPQA Diamond, MMLU-Pro, and MMMU?
   - *Context:* AWS provides vendor-reported comparisons against Claude and GPT models, but independent evaluation on open leaderboards (SWE-bench, LMSYS) is incomplete for the Nova Premier and Omni SKUs.
2. **Bedrock Provisioned Throughput & Discounting (UNK-AN-002):**
   - *Question:* What are the exact rate cards for Nova Provisioned Throughput (commitment-based) vs. pay-as-you-go per 1M tokens, prompt caching discounts, and Batch API pricing?
   - *Context:* AWS pricing documentation varies across regions (us-east-1 vs. eu-central-1 vs. ap-southeast-1) and lacks transparent prompt caching discount tables compared to Anthropic/OpenAI rate cards.
3. **FedRAMP High & GovCloud Region Availability (UNK-AN-003):**
   - *Question:* Which Nova SKUs are certified for FedRAMP High workloads in AWS GovCloud (US-East / US-West) with HIPAA BAA compliance?
   - *Context:* Federal procurement requires verified ATO status before routing sensitive government data to Nova endpoints.

---

### 2.7 EU AI Act Regulatory & Compliance Framework

#### Regulatory Context
The **European Union AI Act** imposes strict tiered compliance obligations based on risk profiles, with dedicated rules for **General-Purpose AI (GPAI) models** entering the European market.

```
                    ┌──────────────────────────────────────────┐
                    │            EU AI Act Framework           │
                    └────────────────────┬─────────────────────┘
                                         │
           ┌─────────────────────────────┴─────────────────────────────┐
           │                                                           │
           ▼                                                           ▼
┌───────────────────────────────┐           ┌───────────────────────────────┐
│     Standard GPAI Models      │           │ GPAI with Systemic Risk       │
│     (Article 53 Obligations)  │           │ (Cumulative >10²⁵ FLOPs)      │
├───────────────────────────────┤           ├───────────────────────────────┤
│ • Technical Documentation     │           │ • Mandatory Model Evaluation  │
│ • Copyright Law Compliance    │           │ • Adversarial Testing (Red)   │
│ • Training Data Summary       │           │ • Cybersecurity Assessment    │
│ • Open License Exemptions*    │           │ • Incident Reporting to EU    │
└───────────────────────────────┘           └───────────────────────────────┘
```

#### Explicit Compliance Blind Spots & Unresolved Questions
1. **Systemic Risk Threshold Mapping (UNK-EUA-001):**
   - *Question:* Which global frontier models (including DeepSeek-V3/V4, GLM-4.7, Qwen 3.7, Claude Sonnet 4.6, GPT-5) trigger the **10^25 FLOPs** training compute threshold for GPAI with Systemic Risk?
   - *Context:* Models exceeding 10^25 FLOPs face mandatory model evaluation, systemic risk assessment, adversarial testing, and incident reporting to the European AI Office. Exact FLOP calculations for open-weight Chinese models are unverified.
2. **Open-Weight License Exemption Boundaries (UNK-EUA-002):**
   - *Question:* Do custom open licenses (e.g., Qwen License, Llama 3/4 License with MAU caps) qualify for Article 2(12) open-source exemptions under the EU AI Act?
   - *Context:* The EU AI Act provides partial compliance exemptions for open-source models provided they are made publicly available under free and open licenses and lack commercial restrictions. Custom licenses with commercial clauses (700M MAU caps) fall into an ambiguous legal gray zone.
3. **Synthetic Content Watermarking Standards (UNK-EUA-003):**
   - *Question:* What technical standards (C2PA, digital watermarking) will be required under Article 50 for AI-generated text, code, and multimodal media, and which API providers natively support them?
   - *Context:* Implementation codes of practice from the EU AI Office are still evolving, leaving enterprise integration pipelines without clear technical targets.

---

### 2.8 FedRAMP Security & Federal Compliance Framework

#### Regulatory Context
**FedRAMP (Federal Risk and Authorization Management Program)** governs the adoption of cloud products across US Federal Agencies, establishing standardized security requirements at Moderate and High Impact Levels.

#### Explicit Compliance Blind Spots & Unresolved Questions
1. **Direct Vendor API ATO Verification (UNK-FED-001):**
   - *Question:* Which commercial direct API endpoints (OpenAI, Anthropic, DeepSeek, AI21) hold active FedRAMP Moderate/High ATOs vs relying exclusively on cloud hyperscaler wrappers (AWS Bedrock, Azure OpenAI, GCP Vertex AI)?
   - *Context:* Federal agencies and defense contractors cannot route CUI (Controlled Unclassified Information) to direct vendor endpoints without verified agency sponsorship or JAB (Joint Authorization Board) P-ATO.
2. **Zero Data Retention (ZDR) Enclave Enforcement (UNK-FED-002):**
   - *Question:* Do cloud hyperscaler FedRAMP High enclaves enforce absolute Zero Data Retention for prompt logs and completion outputs across all frontier models?
   - *Context:* Certain models (e.g., third-party models hosted on Bedrock) require explicit opt-out configurations to disable abuse monitoring log retention, creating potential security compliance breaches.
3. **Cryptographic Validation (UNK-FED-003):**
   - *Question:* Which LLM API gateways natively implement FIPS 140-3 validated cryptographic modules for data in transit and at rest?
   - *Context:* Mandatory for US Federal compliance; non-FIPS compliant API proxies invalidate overall FedRAMP authorization status.

---

## 3. Missing Benchmark Protocols & Routing Edge-Cases

### 3.1 Missing Benchmark Protocols
1. **Agentic Tool-Use Stability Benchmark (UNK-BM-001):**
   - Existing evaluations (SWE-bench, GAIA) test single-turn or short-horizon agentic loops (10-30 tool calls). There is a critical gap in standardized benchmarks testing **long-horizon agentic stability over 200+ sequential tool calls** (e.g., deep repository refactoring, automated portfolio audits, continuous due diligence loops).
2. **Multilingual APAC Enterprise Workload Evals:**
   - Standard benchmarks heavily favor English and Simplified Chinese. Cross-border enterprise workloads (Japanese, Korean, Southeast Asian languages) lack multi-file agentic coding and financial reasoning benchmarks across missing vendors (Tencent, Baidu, SenseTime).

### 3.2 Missing Routing Edge-Cases
1. **Compliance-Gated Multi-Region Failover Routing (UNK-RT-001):**
   - *Scenario:* Routing a regulated enterprise request that requires **EU AI Act compliance**, **FedRAMP High security**, and **sub-500ms TTFT**.
   - *Deficit:* No verified routing rule exists that seamlessly fails over between EU-hosted open-weight instances (Mistral Large 3 / Llama 4 on EU VPC) and US FedRAMP High hyperscaler endpoints (AWS Bedrock Nova Premier / Azure OpenAI) without violating data residency or latency SLAs.

---

*Register maintained continuously by the Research Gap Agent. Last updated: July 2026.*
