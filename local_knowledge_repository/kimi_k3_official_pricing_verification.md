# Kimi K3 Official API Pricing Verification & Uncached Cost Analysis

**Document Status:** Official Verification & Mathematical Audit  
**Date of Verification:** July 27, 2026  
**Primary Source:** Moonshot AI Official API Platform (`platform.kimi.com` / `platform.moonshot.cn`)  
**Secondary Sources:** OpenRouter API (`openrouter.ai`), Artificial Analysis (`artificialanalysis.ai`), ExchangeRate API (`open.er-api.com`)

---

## 1. Executive Summary

This report provides official verification of Moonshot AI's **Kimi K3** flagship model API rate card and presents a 100% uncached financial cost analysis for generating **10,000 monthly reports** across three standard workload tiers (Tier 1 Lite Brief, Tier 2 Standard Review, and Tier 3 Institutional Analysis).

### Key Findings
1. **Official Moonshot AI Rate Card (`kimi-k3`):**
   - **Uncached Input Token Rate:** **¥20.00 / 1M tokens** ($0.000020 / token)
   - **Output Token Rate:** **¥100.00 / 1M tokens** ($0.000100 / token)
   - **Cached Input Token Rate:** **¥2.00 / 1M tokens** ($0.000002 / token — 90% discount)
   - **Context Window:** **1,048,576 tokens** (1M tokens)
2. **OpenRouter Global Benchmark Rates (`moonshotai/kimi-k3`):**
   - **Uncached Input Token Rate:** **$3.00 / 1M tokens** ($0.000003 / token)
   - **Output Token Rate:** **$15.00 / 1M tokens** ($0.000015 / token)
   - **Cached Input Token Rate:** **$0.30 / 1M tokens** ($0.0000003 / token)
3. **10,000 Monthly Reports Cost Breakdown (100% Uncached Standard Pricing):**
   - **Tier 1 (15k Input / 1.5k Output):** **¥4,500.00 CNY** (~**$663.12 USD** | **₹64,066.84 INR** | **KSh 85,844.51 KES**) on direct Moonshot platform; **$675.00 USD** on OpenRouter.
   - **Tier 2 (35k Input / 3.5k Output):** **¥10,500.00 CNY** (~**$1,547.28 USD** | **₹149,489.29 INR** | **KSh 200,303.87 KES**) on direct Moonshot platform; **$1,575.00 USD** on OpenRouter.
   - **Tier 3 (75k Input / 8.0k Output):** **¥23,000.00 CNY** (~**$3,389.27 USD** | **₹327,452.73 INR** | **KSh 438,760.85 KES**) on direct Moonshot platform; **$3,450.00 USD** on OpenRouter.

---

## 2. Official Moonshot AI API Rate Card

According to Moonshot AI's official documentation (`https://platform.kimi.com/docs/pricing/chat-k3.md`), the `kimi-k3` pricing details are as follows:

| Model ID | Billing Unit | Input Price (Cache Hit) | Input Price (Cache Miss / Uncached) | Output Price | Context Window |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **`kimi-k3`** | **1M tokens** | **¥2.00** | **¥20.00** | **¥100.00** | **1,048,576 tokens** |

### Additional Kimi Model Family Context
For comparative positioning within the Moonshot AI API suite:

| Model SKU | Billing Unit | Input (Cache Hit) | Input (Uncached) | Output Price | Context Window | Notes / Positioning |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **`kimi-k3`** | 1M tokens | ¥2.00 | ¥20.00 | ¥100.00 | 1,048,576 | Flagship 1M context, maximum reasoning capacity |
| **`kimi-k2.7-code`** | 1M tokens | ¥1.30 | ¥6.50 | ¥27.00 | 262,144 | Coding & multimodal reasoning model |
| **`kimi-k2.7-code-highspeed`**| 1M tokens | ¥2.60 | ¥13.00 | ¥54.00 | 262,144 | High-speed coding variant (~180–260 tok/s) |
| **`kimi-k2.6`** | 1M tokens | ¥1.10 | ¥6.50 | ¥27.00 | 262,144 | General multimodal model |
| **`kimi-k2.5`** | 1M tokens | ¥0.70 | ¥4.00 | ¥21.00 | 262,144 | Multimodal base model |

### Batch API & Promotional Discounts
- **Batch API:** Batch API requests receive a **40% discount** (billed at **60%** of standard pricing). *Note: Batch API is supported on `kimi-k2.7-code`, `kimi-k2.6`, and `kimi-k2.5`. K3 batch API support is restricted to high-tier allocations.*
- **Recharge Promotion (Event Window: July 16, 2026 – August 12, 2026):**
  - Single deposit ¥99 – ¥499: **10% bonus voucher**
  - Single deposit ¥500 – ¥1,999: **20% bonus voucher**
  - Single deposit ¥2,000 – ¥4,999: **25% bonus voucher**
  - Single deposit ≥ ¥5,000: **30% bonus voucher**

---

## 3. Third-Party Aggregator Pricing Verification

### 3.1 OpenRouter (`moonshotai/kimi-k3`)
Direct query to OpenRouter's model endpoint (`https://openrouter.ai/api/v1/models`) returned the following exact rates:
- **Model ID:** `moonshotai/kimi-k3`
- **Prompt (Uncached Input):** `$0.000003` per token (**$3.00 per 1,000,000 tokens**)
- **Completion (Output):** `$0.000015` per token (**$15.00 per 1,000,000 tokens**)
- **Input Cache Read:** `$0.0000003` per token (**$0.30 per 1,000,000 tokens**)

### 3.2 Artificial Analysis Benchmark Records
Query to `https://artificialanalysis.ai/models/kimi-k3`:
- **Intelligence Index Score:** 57.1
- **Median Output Speed:** 32.96 tokens/second
- **Recorded Price Cards:** Matches standard $3.00 / 1M Input and $15.00 / 1M Output ($0.30 / 1M Cache Hit).

---

## 4. Live Exchange Rates & Data Integrity

To ensure exact conversion across currencies (USD $, Kenyan Shillings KSh, Indian Rupees ₹ INR), exchange rates were fetched from live, timestamped financial data providers (`open.er-api.com`).

- **Retrieval Timestamp:** Sun, 26 Jul 2026 00:02:32 UTC
- **Base FX Rates:**
  - `1 USD = 6.786115 CNY` (Chinese Yuan RMB)
  - `1 USD = 96.614430 INR` (Indian Rupee)
  - `1 USD = 129.455721 KES` (Kenyan Shilling)
- **Derived FX Conversion Multipliers:**
  - `1 CNY = $0.147360 USD`
  - `1 CNY = ₹14.237075 INR`
  - `1 CNY = KSh 19.076559 KES`

---

## 5. Mathematical Uncached Cost Proofs (10,000 Monthly Reports)

All calculations assume **100% UNCACHED normal pricing** (no prompt cache discount, no batch discount) for a production run of **10,000 monthly reports**.

### Formula Definitions
$$\text{Per Report Cost} = \left(\frac{\text{Input Tokens}}{1,000,000} \times \text{Input Rate}\right) + \left(\frac{\text{Output Tokens}}{1,000,000} \times \text{Output Rate}\right)$$
$$\text{Monthly Total (10,000 Reports)} = \text{Per Report Cost} \times 10,000$$

---

### Tier 1: Lite Brief
- **Specification:** 15,000 Input Tokens / 1,500 Output Tokens per report
- **Monthly Volume:** 10,000 reports
- **Total Tokens:** 150,000,000 Input Tokens / 15,000,000 Output Tokens

#### A. Direct Moonshot AI Platform Pricing (CNY Base: ¥20/1M In, ¥100/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(15,000 / 1,000,000) \times \text{¥20.00} = \text{¥0.3000}$
   - Output Cost = $(1,500 / 1,000,000) \times \text{¥100.00} = \text{¥0.1500}$
   - **Per Report Total (CNY):** **¥0.4500**
   - **Per Report Equivalents:** **$0.066312 USD** | **₹6.4067 INR** | **KSh 8.5845 KES**
2. **10,000 Monthly Reports Total:**
   - **CNY Total:** **¥4,500.00 CNY**
   - **USD Total:** **$663.12 USD**
   - **INR Total:** **₹64,066.84 INR**
   - **KES Total:** **KSh 85,844.51 KES**

#### B. OpenRouter USD Standard Pricing (USD Base: $3.00/1M In, $15.00/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(15,000 / 1,000,000) \times \$3.00 = \$0.0450$
   - Output Cost = $(1,500 / 1,000,000) \times \$15.00 = \$0.0225$
   - **Per Report Total (USD):** **$0.0675**
   - **Per Report Equivalents:** **₹6.5215 INR** | **KSh 8.7383 KES**
2. **10,000 Monthly Reports Total:**
   - **USD Total:** **$675.00 USD**
   - **INR Total:** **₹65,214.74 INR**
   - **KES Total:** **KSh 87,382.61 KES**

---

### Tier 2: Standard Review
- **Specification:** 35,000 Input Tokens / 3,500 Output Tokens per report
- **Monthly Volume:** 10,000 reports
- **Total Tokens:** 350,000,000 Input Tokens / 35,000,000 Output Tokens

#### A. Direct Moonshot AI Platform Pricing (CNY Base: ¥20/1M In, ¥100/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(35,000 / 1,000,000) \times \text{¥20.00} = \text{¥0.7000}$
   - Output Cost = $(3,500 / 1,000,000) \times \text{¥100.00} = \text{¥0.3500}$
   - **Per Report Total (CNY):** **¥1.0500**
   - **Per Report Equivalents:** **$0.154728 USD** | **₹14.9489 INR** | **KSh 20.0304 KES**
2. **10,000 Monthly Reports Total:**
   - **CNY Total:** **¥10,500.00 CNY**
   - **USD Total:** **$1,547.28 USD**
   - **INR Total:** **₹149,489.29 INR**
   - **KES Total:** **KSh 200,303.87 KES**

#### B. OpenRouter USD Standard Pricing (USD Base: $3.00/1M In, $15.00/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(35,000 / 1,000,000) \times \$3.00 = \$0.1050$
   - Output Cost = $(3,500 / 1,000,000) \times \$15.00 = \$0.0525$
   - **Per Report Total (USD):** **$0.1575**
   - **Per Report Equivalents:** **₹15.2168 INR** | **KSh 20.3893 KES**
2. **10,000 Monthly Reports Total:**
   - **USD Total:** **$1,575.00 USD**
   - **INR Total:** **₹152,167.73 INR**
   - **KES Total:** **KSh 203,892.76 KES**

---

### Tier 3: Institutional Analysis
- **Specification:** 75,000 Input Tokens / 8,000 Output Tokens per report
- **Monthly Volume:** 10,000 reports
- **Total Tokens:** 750,000,000 Input Tokens / 80,000,000 Output Tokens

#### A. Direct Moonshot AI Platform Pricing (CNY Base: ¥20/1M In, ¥100/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(75,000 / 1,000,000) \times \text{¥20.00} = \text{¥1.5000}$
   - Output Cost = $(8,000 / 1,000,000) \times \text{¥100.00} = \text{¥0.8000}$
   - **Per Report Total (CNY):** **¥2.3000**
   - **Per Report Equivalents:** **$0.338927 USD** | **₹32.7453 INR** | **KSh 43.8761 KES**
2. **10,000 Monthly Reports Total:**
   - **CNY Total:** **¥23,000.00 CNY**
   - **USD Total:** **$3,389.27 USD**
   - **INR Total:** **₹327,452.73 INR**
   - **KES Total:** **KSh 438,760.85 KES**

#### B. OpenRouter USD Standard Pricing (USD Base: $3.00/1M In, $15.00/1M Out)
1. **Per Report Calculation:**
   - Input Cost = $(75,000 / 1,000,000) \times \$3.00 = \$0.2250$
   - Output Cost = $(8,000 / 1,000,000) \times \$15.00 = \$0.1200$
   - **Per Report Total (USD):** **$0.3450**
   - **Per Report Equivalents:** **₹33.3320 INR** | **KSh 44.6622 KES**
2. **10,000 Monthly Reports Total:**
   - **USD Total:** **$3,450.00 USD**
   - **INR Total:** **₹333,319.78 INR**
   - **KES Total:** **KSh 446,622.24 KES**

---

## 6. Comprehensive Financial Comparison Matrix

### Direct Moonshot AI Platform Billing (CNY Base)

| Report Tier | Input / Output Tokens | Per Report Cost (CNY) | Per Report Cost (USD) | 10k Monthly Total (CNY) | 10k Monthly Total (USD) | 10k Monthly Total (₹ INR) | 10k Monthly Total (KSh KES) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Tier 1: Lite Brief** | 15,000 / 1,500 | ¥0.4500 | $0.066312 | ¥4,500.00 | $663.12 | ₹64,066.84 | KSh 85,844.51 |
| **Tier 2: Standard Review** | 35,000 / 3,500 | ¥1.0500 | $0.154728 | ¥10,500.00 | $1,547.28 | ₹149,489.29 | KSh 200,303.87 |
| **Tier 3: Institutional Analysis** | 75,000 / 8,000 | ¥2.3000 | $0.338927 | ¥23,000.00 | $3,389.27 | ₹327,452.73 | KSh 438,760.85 |

### OpenRouter Standard USD Benchmark Billing

| Report Tier | Input / Output Tokens | Per Report Cost (USD) | Per Report Cost (₹ INR) | Per Report Cost (KSh KES) | 10k Monthly Total (USD) | 10k Monthly Total (₹ INR) | 10k Monthly Total (KSh KES) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Tier 1: Lite Brief** | 15,000 / 1,500 | $0.0675 | ₹6.5215 | KSh 8.7383 | $675.00 | ₹65,214.74 | KSh 87,382.61 |
| **Tier 2: Standard Review** | 35,000 / 3,500 | $0.1575 | ₹15.2168 | KSh 20.3893 | $1,575.00 | ₹152,167.73 | KSh 203,892.76 |
| **Tier 3: Institutional Analysis** | 75,000 / 8,000 | $0.3450 | ₹33.3320 | KSh 44.6622 | $3,450.00 | ₹333,319.78 | KSh 446,622.24 |

---
*Report compiled autonomously using live web research, direct API queries, and timestamped currency conversion data.*
