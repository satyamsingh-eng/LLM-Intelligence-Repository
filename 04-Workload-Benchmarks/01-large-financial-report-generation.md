# Workload 1: Large Financial Report Generation

**Confidence Score:** High (Directly maps to SARVAX OneChat Artifacts & Memory API)
**Last Validated:** July 2026

## Overview
- **Business Objective:** Generate 50+ page comprehensive portfolio reviews and investment strategy reports based on multiple unstructured financial PDFs, SEC filings, and internal guidelines.
- **Industry:** Wealth Management & Investment Banking.
- **Target Users:** Financial Advisors, Portfolio Managers, Research Analysts.
- **Problem Being Solved:** Manual synthesis of 100+ pages of unstructured financial data takes 12-16 hours per report.

## SARVAX Architecture Mapping
- **Workflow Diagram:** Document Ingestion (UI) -> Gemini OCR Extraction -> `MarkItDown` (Ingestion) -> `GraphRAG` / `R2R` (Knowledge Graph) -> `STORM` (Stanford Research Writer) & `GPT-Researcher` -> OneChat Artifacts (Report Assembly) -> Human-in-the-loop QA.
- **AI Models Required:** 
  - OCR: Gemini 3 Pro / Gemini 3 Flash
  - Reasoning/Generation: GPT-5.x / Claude Opus 4.6 / DeepSeek V3.2
- **Agent Architecture:** Sequential handoffs (Planning -> Extraction -> Reasoning -> Generation).
- **Reasoning Complexity:** Extremely High (Requires multi-step logic across disconnected documents).
- **OCR Requirements:** Gemini is the mandatory OCR engine (handles tables, charts, and unstructured text).

## Performance & Economic Parameters
- **Estimated Context Size:** 150,000 to 250,000 tokens (Heavy document load).
- **Estimated Input Tokens:** ~120,000 per report (using Prompt Caching).
- **Estimated Output Tokens:** ~15,000 per report (Structured Markdown/HTML).
- **Average Runtime:** 45 - 90 seconds (Highly dependent on batch processing and model TPS).
- **Expected Cost (DeepSeek V3.2):** ~$0.05 per report.
- **Expected Cost (GPT-5):** ~$0.30 per report.

## Quality & Evaluation
- **Latency Targets:** < 60s for initial draft generation.
- **Quality Metrics:** Semantic hallucination rate (must be < 0.1%), strict adherence to provided compliance guidelines, citation tracking to source PDFs.
- **Failure Modes:** Context window truncation, table misalignment during OCR, numerical hallucinations in financial projections.
- **Evaluation Criteria:** Pass/Fail via Human Review (Advisor signature required before client delivery).
