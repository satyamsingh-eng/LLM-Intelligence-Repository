# Workload 3: KYC & AML Compliance Automation

**Confidence Score:** High (Architecturally mirrors `uploadHrResumes` endpoint)
**Last Validated:** July 2026

## Overview
- **Business Objective:** Rapid, zero-hallucination extraction of entities from identity documents, tax forms, and proof-of-address to populate CRM fields and run automated risk scoring.
- **Industry:** Banking, Wealth Management, Insurance.
- **Target Users:** Onboarding Specialists, Compliance Officers.
- **Problem Being Solved:** Data entry bottlenecks preventing same-day account opening.

## SARVAX Architecture Mapping
- **Workflow Diagram:** Document Upload (UI) -> Gemini 3 Flash OCR -> Strict JSON Generation Agent -> Rule-based Compliance Engine -> MCP CRM Injection.
- **AI Models Required:**
  - OCR / Vision: Gemini 3 Flash (Mandatory)
  - JSON Extraction: Qwen3.7 Max / Llama 4 (Fast, structured output)
- **Agent Architecture:** Single-step functional extraction. No multi-agent reasoning required.
- **Reasoning Complexity:** Low (Pure extraction and formatting).
- **OCR Requirements:** Heavy (Passports, IDs, scanned PDFs).

## Performance & Economic Parameters
- **Estimated Context Size:** 4,000 tokens per document.
- **Estimated Input Tokens:** ~5,000 tokens (including JSON schema prompt).
- **Estimated Output Tokens:** ~500 tokens (JSON payload).
- **Average Runtime:** < 3 seconds.
- **Expected Cost:** < $0.005 per document.

## Quality & Evaluation
- **Latency Targets:** < 3s (Synchronous UI block).
- **Quality Metrics:** JSON schema adherence (100%), character-for-character extraction match.
- **Failure Modes:** Blurry ID scans causing Gemini OCR failure, hallucinated digits in SSN/Tax ID.
- **Evaluation Criteria:** Pass/Fail strict character matching against human baseline.
