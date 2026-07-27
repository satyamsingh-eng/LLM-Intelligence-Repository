# Arvocap Asset Managers — 10k Batch Report Generation Analysis
**Date**: July 27, 2026  
**Account**: Arvocap Asset Managers (Nairobi, Kenya — CMA Regulated)  
**Stakeholders**: Monicah Mwaniki (Co-Founder & CEO), John Ngure, Arnold Oduma (Technical Lead), Simar Juttla (Technical Lead)  
**C3A Sales/Product Leads**: Pratyush Malviya (Sales Manager), Sarang Kulkarni, Ria Choudhari (Dev), Satyam Singh Rajput (Product & LLM Pricing)

---

## 1. Executive Summary & Vision

Arvocap manages KSh 11.02 Billion (~$85M USD) AUM across 10 sub-funds with ~10,000 active retail and emerging affluent investors.

The core commercial objective for the SarvaX platform pilot is **Automated Monthly Portfolio Performance & Market Impact Report Generation dispatched to all 10,000 clients** (similar to automated periodic portfolio updates dispatched by retail fintech giants like Angel One, Zerodha, or Groww, but tailored to wealth advisory and regulated fund management).

---

## 2. Primary Source Email Chronology (`Re: Pricing Sheet + Next Steps: Arvocap x C3ALabs`)

1. **July 21, 2026**: Pratyush Malviya schedules pilot alignment meeting.
2. **July 23, 2026**: Pratyush confirms agreed pilot next steps:
   - Dual-agent architecture approved.
   - Compliance package (SOC 2 report + data management policy) prepared for sharing.
   - Cost estimates & LLM model comparison for 10k monthly reports assigned to C3A Labs (Satyam).
   - KYC tracking implementation timeline.
3. **July 23, 2026**: John Ngure onboarded Arvocap Technical Leads: Arnold Oduma (`a.oduma@arvocap.com`) and Simar Juttla (`s.juttla@arvocap.com`).
4. **July 24, 2026**: Pratyush requests sample reports from John Ngure to gauge complexity and exact token length.

---

## 3. Mapping to 4 Core Workloads (Doc `1LZ2lxCqdhW4GTtTXe2J12b9W8xQgFlO-HXCglel65OA`)

- **Use Case 1 (IFA Support)**: External IFAs managing hundreds of clients request automated portfolio reviews via SarvaX instead of calling central office analysts.
- **Use Case 2 (Internal Wealth Managers)**: Automated monthly client portfolio reports, executive AUM tracking, and "agent-within-an-agent" hierarchy oversight.
- **Use Case 3 (Aggregate Analytics)**: Executive network-wide AUM & fund performance dashboards.
- **Use Case 4 (Targeted Communications)**: Segmented outreach by investment tier (HNW / Mass Affluent / Retail) and channel (WhatsApp / Email).

---

## 4. 3-Tiered Report Complexity & LLM Costing Matrix (10k Batch Generation)

To protect C3A Labs while awaiting sample PDF files from John Ngure, the LLM Comparison Sheet presents 3 complexity tiers:

| Report Complexity Tier | Page Count | Input Tokens / Report | Output Tokens / Report | Recommended Model Stack | Cost / Report (80% Cached) | Total Cost for 10,000 Reports / Month |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: |
| **Tier 1: Lite Summary Brief** | 1 – 2 Pages | 15,000 | 1,500 | `Gemini 3.5 Flash-Lite` | **₹0.38** | **₹3,800 / mo** (₹0.04 Lakhs) |
| **Tier 2: Standard Portfolio Review** | 3 – 5 Pages | 35,000 | 3,500 | `DeepSeek V4 Pro` | **₹1.85** | **₹18,500 / mo** (₹0.19 Lakhs) |
| **Tier 3: Deep Institutional Analysis** | 8 – 12 Pages | 75,000 | 8,000 | `DeepSeek V4 Pro` $\rightarrow$ `Kimi K3` | **₹6.20** | **₹62,000 / mo** (₹0.62 Lakhs) |

---

## 5. Current Tracker Status
- **Google Sheet (`1ApSkZww...` Row 4)**: Usecase Status listed as `Completed` (initial dev mapping by Ria), with explicit Blocker: **`LLM comparasion sheet - satyam`**.
- **Pending Action**: Satyam delivering this 3-Tier LLM Model Comparison & Cost Matrix to Pratyush and Sarang for the client commercial call.
