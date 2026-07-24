# Phase 4: SARVAX Enterprise Workload Benchmarks

Derived from financial services enterprise needs combined with actual SARVAX capabilities.

## 1. Large Report Generation (Mandated Benchmark)
* **Business Objective:** Generate 50-page deep-dive financial/compliance reports from raw unstructured enterprise documents.
* **Workflow:** Document Ingestion -> Gemini OCR -> Knowledge Retrieval (Agent Memory) -> Planning -> Research -> Reasoning -> Report Generation (OneChat Artifacts) -> Human Review.
* **Context Window:** 128k+ required (200k+ preferred).
* **Estimated Tokens:** Input: 120,000 | Output: 15,000
* **Evaluation Metrics:** Semantic hallucination rate, structure adherence, citation accuracy.

## 2. Autonomous Multi-Agent Workflow (Mandated Benchmark)
* **Business Objective:** End-to-end automated due diligence without human intervention until the final approval stage.
* **Workflow:** Planning Agent -> Retriever Agent (MCP) -> OCR Agent (Gemini) -> Research Agent -> Reasoning Agent -> Validation Agent -> Report Writer -> QA Agent -> Human Approval.
* **Implementation:** SARVAX Workflow 2.0 DAG Engine (`depends_on` gating).
* **Estimated Tokens:** Combined Input: 80,000 | Combined Output: 12,000
* **Reasoning Complexity:** Extremely High (Requires CoT or frontier models).

## 3. KYC Document Processing & Risk Scoring
* **Business Objective:** Rapidly onboard clients by extracting entities from unstructured IDs and tax forms.
* **Implementation:** Re-purposing the `uploadHrResumes` pipeline for KYC.
* **Workflow:** Ingest PDF -> Gemini OCR Extraction -> Strict JSON Structured Output -> Rule-based Compliance Risk Scoring -> Dashboard Flagging.
* **Estimated Tokens:** Input: 5,000 | Output: 500
* **Latency Expectation:** < 3 seconds (Fast extraction).

## 4. Meeting Intelligence & Advisor Writeback
* **Business Objective:** Transcribe wealth advisor meetings and auto-update CRM systems via MCP.
* **Implementation:** `createMeetingWithBot` -> LLM Summarization -> MCP Tool Call to Salesforce/HubSpot.
* **Workflow:** Ingest Audio Transcript -> Extract Action Items -> Format JSON -> Execute MCP Server -> Confirmation Artifact.
* **Estimated Tokens:** Input: 15,000 | Output: 800

## 5. Agentic Financial Market Research
* **Business Objective:** Retrieve live market data and synthesize impact on client portfolios.
* **Implementation:** OneChat + MCP Web Search/Morningstar Integrations.
* **Workflow:** User Prompt -> Tool Use (Market API) -> Context Injection -> Reasoning (DeepSeek/Qwen) -> Client-ready email generation.
* **Estimated Tokens:** Input: 25,000 | Output: 2,000
