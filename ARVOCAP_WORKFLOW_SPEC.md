# Arvocap Asset Managers — 100% Drive-Native Workflow 2.0 Specification

**Target Company**: Arvocap Asset Managers Ltd (`arvocap.com`, Nairobi, Kenya — CMA Cap 485A)  
**Product Target**: KARAX Workflow 2.0 Engine (`http://localhost:3000/dashboard/workflows`)  
**CRM Storage**: **Google Drive** (Functions as the core CRM & disclosure repository — zero external CRM connections required).  
**Core Objective**: End-to-end automated 10,000 monthly client report generation pipeline with real-time token cost telemetry.

---

## 1. Product Input Parameters (Runtime Inputs)

When executing a test or production run on the KARAX platform, the workflow prompts the user for runtime inputs:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       KARAX WORKFLOW RUNTIME INPUTS                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Google Drive Data Source (input_data_source)                             │
│    URL or Folder ID containing Flex ID records & CRM disclosures           │
│    (Default: TESTING DATA folder ID 1vYrkqdf3ZKo815_HKHpbbS9Qv0tEOjJB)      │
│                                                                             │
│ 2. Recipient Email Address (recipient_email)                                │
│    Email address to receive the final generated 5-page PDF statement       │
│                                                                             │
│ 3. Target Flex ID Filter (flex_id_filter) [Optional]                        │
│    Specific Flex ID (e.g. FLX-984210-KE for Dr. David K. Mutua) for 1 run    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 5-Step Drive-Native Multi-Model Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     KARAX 100% DRIVE-NATIVE WORKFLOW DAG                    │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
      ┌───────────────────────────┐         ┌───────────────────────────┐
      │  STEP 1A: DRIVE OCR       │         │  STEP 1B: DRIVE CRM       │
      │  Google Drive + Gemini    │         │  Google Drive + DeepSeek  │
      │  Flash-Lite (Cheap Tier)  │         │  V4 Pro (Cheap Tier)      │
      └─────────────┬─────────────┘         └─────────────┬─────────────┘
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       ▼
                        ┌───────────────────────────┐
                        │  STEP 2: BANKING REASONING│
                        │  Kimi K3 (Deep Tier)      │
                        │  (#1 SOTA TAU Banking)    │
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │  STEP 3: PYTHON CODE MATH │
                        │  100% Exact NAV & KRA Tax │
                        │  + 5-Page PDF Generator   │
                        └─────────────┬─────────────┘
                                      │
                                      ▼
                        ┌───────────────────────────┐
                        │  STEP 4: EMAIL DISPATCH   │
                        │  Gmail / Amazon SES API   │
                        │  + Advisor Sign-off Gate  │
                        └───────────────────────────┘
```

---

## 3. Production Copy-Paste Prompt (For KARAX Creator / OneChat)

```text
Build a 5-step multi-model DAG workflow for Arvocap Asset Managers (Nairobi, Kenya) to automate client portfolio statements using Google Drive as the CRM repository and Email for delivery.

Configure the following runtime input parameters:
- input_data_source: Google Drive folder URL or ID containing Flex ID data exports and client disclosure files (Default: TESTING DATA folder ID 1vYrkqdf3ZKo815_HKHpbbS9Qv0tEOjJB).
- recipient_email: Email address to receive the final generated PDF report.
- flex_id_filter: Optional client Flex ID filter (Default: FLX-984210-KE for Dr. David K. Mutua).

Execute the following multi-model step cascade:
1. Step 1A (Drive & OCR Ingestion): Ingest statement PDFs, scanned receipts, and holding sheets from input_data_source on Google Drive using Gemini 3.5 Flash-Lite (Cheap Model Tier).
2. Step 1B (Drive CRM & Disclosure Context): Ingest client interaction history files and fund disclosures directly from input_data_source on Google Drive using DeepSeek V4 Pro (Cheap Model Tier) in parallel with Step 1A.
3. Step 2 (Banking Reasoning & Commentary): Merge outputs from Step 1A and 1B. Use Kimi K3 (Deep Model Tier, #1 TAU Banking SOTA reasoning) to write personalized financial commentary, yield analysis, and Kenyan macroeconomic trends.
4. Step 3 (Exact Code Math & PDF Artifact): Run a Python Decimal Math Engine (Zero AI math error) to compute NAVs, 15% KRA Withholding Tax deductions, and net payouts, then render a print-ready 5-page PDF client wealth statement artifact.
5. Step 4 (Advisor Gate & Email Dispatch): Present the draft PDF to the Senior Wealth Lead for 1-click approval, then dispatch the finalized 5-page PDF statement as an email attachment to recipient_email via Gmail / Amazon SES.

Let the KARAX execution HUD log the real-time executed tokens and single-run cost in USD to calculate the exact monthly budget for 10,000 client reports.
```

---

## 4. Single-Run Real Cost Calculation Protocol

1. **Execute 1 Test Run** on KARAX Dashboard (`http://localhost:3000/dashboard/workflows`).
2. **Observe Telemetry HUD**:
   * Step 1A Tokens & Cost (Gemini Flash-Lite via Drive)
   * Step 1B Tokens & Cost (DeepSeek V4 Pro via Drive)
   * Step 2 Tokens & Cost (Kimi K3)
   * Step 3 Tokens & Cost (Python Code Engine)
   * Step 4 Email Dispatch Status
3. **Total Single-Run Cost ($USD)** = Sum of Steps 1A, 1B, 2, 3, 4.
4. **Projected 10,000 Monthly Budget ($USD)** = `Total Single-Run Cost` $\times 10,000$ (Benchmark: Managed Tier 2 Package @ **$950 / Month**).
