# Chinese AI Ecosystem (DeepSeek, Qwen, Kimi, MiniMax, Zhipu AI)

**Document Version:** 2026.7.1  
**Target Platform:** C3A Labs SARVAX Platform, OpenCode Go & Model Routing Engine  
**Maintainer:** Agent 2 (Chinese Ecosystem & Benchmarks)  
**Last Verified:** July 2026 (Data synchronized with Artificial Analysis Leaderboard & OpenCode Go)  

---

## 1. Executive Summary & Ecosystem Overview

The Chinese AI Ecosystem in mid-2026 represents the primary global counterweight to US proprietary AI laboratories. Characterized by rapid architecture iteration (MoE + Multi-Head Latent Attention, Hybrid Linear Attention, and Dual-Mode Thinking), hyper-aggressive inference cost structures, and ultra-high generation throughput (up to 198 tok/s), Chinese foundational models deliver unmatched **Intelligence-per-Dollar** efficiency.

As of July 2026, five core frontier labs define the ecosystem:
1. **DeepSeek:** World leader in cost-performance ratio. `DeepSeek V4 Pro` achieves an Intelligence Index of 44 at an astonishing $0.04 per task.
2. **Moonshot AI (Kimi):** Frontier intelligence leader in China. `Kimi K3` hits an Intelligence Index of **57**, competing directly with top-tier US frontier models.
3. **Zhipu AI (Z AI):** Reasoning and speed powerhouse. `GLM-5.2 (max)` delivers a **51** Intelligence Index with reasoning capabilities at an ultra-fast **172 tok/s**.
4. **Alibaba Cloud (Qwen):** Speed and enterprise scalability leader. `Qwen 3.7 Max` achieves **198 tok/s** output speed with strong agentic and coding capabilities.
5. **MiniMax:** Long-context and high-throughput leader. `MiniMax-M3` pairs a 1M–2M context window with 96 tok/s throughput at $0.12/task.

Through platforms like **OpenCode Go** ($5–$10/mo with a $60 monthly usage cap), Western developers and C3A Labs bypass native Chinese geofencing, RMB payment barriers, and strict real-name KYC requirements, gaining frictionless API access to these frontier models.

---

## 2. Master Model Comparison Matrix

The table below compiles intelligence scores, speed, pricing (converted to USD / normalized per 1M tokens), and estimated capacity under OpenCode Go.

| Provider | Model | Context Window (In/Out) | Intelligence Index (AA) | Speed (tok/s) | Latency (TTFT) | Native API Price ($/1M In / Out) | OpenCode Go Price ($/1M In / Out) | AA Cost per Task | Est. Max Req / Mo ($60 Cap) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Moonshot AI** | **Kimi K3** | 200,000 / 64,000 | **57** | 34 tps | 600–1200ms | $2.50 / $12.00 | $3.00 / $15.00 | $0.95 | 490 |
| **Zhipu AI** | **GLM-5.2 (max)** | 128,000 / 32,000 | **51** | **172 tps** | 350–650ms | $1.00 / $3.50 | $1.40 / $4.40 | $0.47 | 4,300 |
| **Alibaba** | **Qwen 3.7 Max** | 128,000 / 16,384 | **46** | **198 tps** | 200–400ms | $1.60 / $6.40 | $2.50 / $7.50 | $1.03 | 4,770 |
| **DeepSeek** | **DeepSeek V4 Pro (max)** | 128,000 / 16,384 | **44** | 68 tps | 400–900ms | $0.14 / $0.28 | $0.435 / $0.87 | **$0.04** | 17,150 |
| **MiniMax** | **MiniMax-M3** | 1,000,000 / 32,000 | **44** | 96 tps | 250–500ms | $0.20 / $1.00 | $0.30 / $1.20 | $0.12 | 16,000 |
| **DeepSeek** | **DeepSeek V4 Pro (high)** | 128,000 / 16,384 | **43** | 69 tps | 350–700ms | $0.14 / $0.28 | $0.435 / $0.87 | **$0.04** | 17,150 |
| **Xiaomi** | **MiMo-V2.5-Pro (reasoning)** | 128,000 / 16,384 | **42** | 64 tps | 300–600ms | $0.12 / $0.30 | $0.435 / $0.87 | **$0.03** | 16,300 |
| **Moonshot AI** | **Kimi K2.7 Code** | 200,000 / 32,000 | **42** | 46 tps | 350–600ms | $0.80 / $3.20 | $0.95 / $4.00 | — | 6,750 |
| **Tencent** | **Hy3** | 128,000 / 16,384 | **41** | 63 tps | 250–450ms | $0.10 / $0.40 | $0.14 / $0.58 | **$0.03** | 21,500 |
| **Alibaba** | **Qwen 3.6 Plus** | 128,000 / 8,192 | **40** | 53 tps | 250–450ms | $0.35 / $2.10 | $0.50 / $3.00 | $0.31 | 16,300 |
| **Alibaba** | **Qwen 3.7 Plus** | 128,000 / 16,384 | **39** | 54 tps | 250–450ms | $0.30 / $1.20 | $0.40 / $1.60 | $0.21 | 21,600 |
| **Xiaomi** | **MiMo-V2.5** | 128,000 / 8,192 | **37** | 66 tps | 180–350ms | $0.05 / $0.15 | $0.14 / $0.28 | **$0.01** | 150,400 |
| **DeepSeek** | **DeepSeek V4 Flash** | 64,000 / 8,192 | **37** | 120 tps | 150–250ms | $0.05 / $0.10 | $0.14 / $0.28 | **$0.04** | 158,150 |
| **Moonshot AI** | **Kimi K2.6** | 128,000 / 16,384 | **35\*** | 34 tps | 300–500ms | $0.80 / $3.20 | $0.95 / $4.00 | — | 5,750 |
| **Zhipu AI** | **GLM-5.2 (non-reasoning)** | 128,000 / 16,384 | **34\*** | 90 tps | 200–350ms | $1.00 / $3.50 | $1.40 / $4.40 | — | 4,300 |
| **DeepSeek** | **DeepSeek V4 Pro (non-reasoning)** | 128,000 / 16,384 | **31\*** | 68 tps | 250–400ms | $0.14 / $0.28 | $0.435 / $0.87 | — | 17,150 |

*\*Note: Scores marked with asterisk (\*) represent performance in non-reasoning mode. Benchmark data sourced from Artificial Analysis LLM Leaderboard (July 2026).*

---

## 3. Deep Provider Intelligence Profiles

### 3.1 DeepSeek
* **Core Architecture:** Sparse Mixture-of-Experts (MoE) combined with Multi-Head Latent Attention (MLA) and DeepSeek-Math / reasoning CoT kernels.
* **Flagship Models:** `DeepSeek V4 Pro (max / high)`, `DeepSeek V4 Flash`.
* **Key Advantages:**
  * Unmatched value: 44 Intelligence Index score at just **$0.04 per task** (1/10th to 1/25th the cost of US equivalent models).
  * Flexible reasoning depth (`max` reasoning for complex logic vs `high` or `non-reasoning` for low-latency turns).
* **Latency & Speed:** Steady 68–69 tok/s generation speed; TTFT ranges from 350ms (non-reasoning) to 900ms (max reasoning).
* **Native API Constraints:** Direct API (`api.deepseek.com`) suffers from frequent concurrency throttling during peak Asian business hours. OpenCode Go routing provides prioritized access pools.

### 3.2 Moonshot AI (Kimi)
* **Core Architecture:** Proprietary long-context transformer with dynamic KV-cache compression and step-by-step reasoning extensions.
* **Flagship Models:** `Kimi K3`, `Kimi K2.7 Code`, `Kimi K2.6`.
* **Key Advantages:**
  * **Ecosystem Intelligence Leader:** `Kimi K3` scores **57** on the Artificial Analysis Intelligence Index, making it the top-performing Chinese model and a direct competitor to GPT-5.6 Sol / Claude 3.7 Sonnet tier models.
  * Native handling of extremely long documents (200k to 1M+ input tokens) with full retention.
* **Latency & Speed:** Generation speed is moderate (34 tok/s for K3, 46 tok/s for K2.7 Code) due to heavy CoT reasoning passes.
* **Native API Constraints:** Moonshot native API requires CN phone verification for direct developer portal registration.

### 3.3 Zhipu AI (Z AI)
* **Core Architecture:** General Language Model (GLM) architecture with dynamic dual-mode execution (Switchable reasoning CoT).
* **Flagship Models:** `GLM-5.2 (max / non-reasoning)`, `GLM-5.1`.
* **Key Advantages:**
  * **Ultra-Fast Reasoning:** `GLM-5.2 (max)` yields an impressive **51 Intelligence Index** while pushing **172 tok/s** output speed — making it the fastest high-intelligence reasoning model available globally.
  * Excellent bilingual Chinese/English comprehension, structured JSON output, and tool calling.
* **Latency & Speed:** Fast initial TTFT (350–650ms) and unmatched generation throughput.
* **Native API Constraints:** Zhipu BigModel API endpoints (`open.bigmodel.cn`) enforce IP strictness; OpenCode Go provides clean global access.

### 3.4 Alibaba Cloud (Qwen)
* **Core Architecture:** Dense & MoE hybrid architecture fine-tuned on multi-trillion token bilingual/code corpora.
* **Flagship Models:** `Qwen 3.7 Max`, `Qwen 3.7 Plus`, `Qwen 3.6 Plus`.
* **Key Advantages:**
  * **Ecosystem Speed Leader:** `Qwen 3.7 Max` hits **198 tok/s** median generation speed with a **46** Intelligence Index.
  * Exceptional performance in agentic tool-use, multi-file software engineering, and mathematical reasoning.
* **Latency & Speed:** Lowest TTFT in ecosystem (200–400ms) with highest generation throughput.
* **Native API Constraints:** Alibaba Bailian platform (`dashscope.aliyuncs.com`) requires enterprise verification or CN billing for primary tiers.

### 3.5 MiniMax
* **Core Architecture:** Lightning-attention hybrid MoE architecture optimized for massive context retrieval.
* **Flagship Models:** `MiniMax-M3`, `MiniMax M2.7`.
* **Key Advantages:**
  * High intelligence (44 Index) paired with 1M–2M context window support at very low cost ($0.12/task).
  * Balanced performance: 96 tok/s output speed with smooth multimodal context handling.
* **Latency & Speed:** Responsive TTFT (250–500ms) and strong sustained output rate.

### 3.6 Emerging Disruptors (Xiaomi MiMo & Tencent Hy3)
* **Xiaomi MiMo-V2.5-Pro:** Scores **42** in Intelligence Index at an extraordinary **$0.03 per task**, outperforming many mid-tier models at a fraction of the cost.
* **Tencent Hy3:** Solid all-rounder (41 Index, $0.03/task, 63 tok/s) tailored for consumer dialogue and intent detection.

---

## 4. API Access, Infrastructure & Compliance Matrix

Operating Chinese foundational models from global or enterprise environments requires navigating distinct regulatory, geographical, and network boundaries.

| Provider / Model | Native Endpoint | Geofencing Policy | KYC / Identity Control | Primary Rate Limits | OpenCode Go Proxy Status | Compliance & Data Residency |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **DeepSeek** | `api.deepseek.com` | IP block on select US cloud regions | Credit Card / RMB Alipay | 60–120 RPM (Varies by tier) | **Supported** (Bypasses regional IP limits) | CAC LLM Registered; 30-day log retention |
| **Qwen (Bailian)** | `dashscope.aliyuncs.com` | CN Mainland & HK primary | Enterprise / Real-Name CN ID | 100–300 RPM; 100k TPM | **Supported** (US/EU edge routing) | CAC Registered; Multi-region CN Cloud data residency |
| **Kimi (Moonshot)** | `api.moonshot.cn` | Geo-restricted outside CN/HK | Real-name CN Phone / Credit | 30–60 RPM (Strict tiering) | **Supported** (Global endpoint bridge) | CAC Registered; Standard commercial privacy |
| **Zhipu AI** | `open.bigmodel.cn` | Strict CN endpoint policy | Enterprise License / Identity | 60–200 RPM | **Supported** (Routed via OpenCode edge) | CAC Registered; Enterprise private tenant options |
| **MiniMax** | `api.minimax.chat` | CN Mainland & Global API | Account registration / Org ID | 60–120 RPM | **Supported** (Full proxy support) | CAC Registered; Commercial API ZDR on enterprise |

---

## 5. Cost vs. Intelligence Efficiency Analysis

### 5.1 Efficiency Ranking (Intelligence per Dollar)

To evaluate value for C3A Labs agent workloads, we analyze the **Cost-to-Intelligence Index Ratio** (Task Cost / Intelligence Score):

1. **MiMo-V2.5-Pro:** Index 42 @ $0.03/task = **$0.00071 per Index Point** *(Best Value overall)*
2. **DeepSeek V4 Pro:** Index 44 @ $0.04/task = **$0.00090 per Index Point** *(Best Flagship Value)*
3. **Hy3:** Index 41 @ $0.03/task = **$0.00073 per Index Point**
4. **MiniMax-M3:** Index 44 @ $0.12/task = **$0.00272 per Index Point**
5. **Qwen 3.7 Plus:** Index 39 @ $0.21/task = **$0.00538 per Index Point**
6. **GLM-5.2 (max):** Index 51 @ $0.47/task = **$0.00921 per Index Point**
7. **Kimi K3:** Index 57 @ $0.95/task = **$0.01666 per Index Point** *(Frontier Capability Leader)*
8. **Qwen 3.7 Max:** Index 46 @ $1.03/task = **$0.02239 per Index Point** *(Speed Leader)*

---

## 6. Architectural & Routing Recommendations for SARVAX / OpenCode Go

```
                        [Incoming C3A Agent Task]
                                    |
                    +---------------+---------------+
                    |  Routing Engine & Usage Cap   |
                    +---------------+---------------+
                                    |
      +-----------------------------+-----------------------------+
      |                             |                             |
[Frontier Reasoning]       [High-Speed / Interactive]     [Bulk Execution / Low Cost]
  (Kimi K3 / GLM-5.2)       (Qwen 3.7 Max / MiniMax-M3)     (DeepSeek V4 Pro / MiMo Pro)
      |                             |                             |
      v                             v                             v
• Hard Math & Code Logic    • Real-Time Interactive Agents • High-Volume Batch RAG
• Extended CoT Planning     • Speed-critical Code Completion • Automated Doc Generation
• Intelligence Index: 51–57 • Speed: 96–198 tok/s          • Cost: $0.03–$0.04/task
```

### Routing Rules for C3A Labs Workflows:
1. **Primary Workhorse (80% of tasks):** Route to `DeepSeek V4 Pro (max)` or `MiMo-V2.5-Pro`. Provides 42–44 Intelligence Index at $0.03–$0.04/task, conserving OpenCode Go monthly caps.
2. **Speed-Critical / Real-Time Coding:** Route to `GLM-5.2 (max)` or `Qwen 3.7 Max`. Outputs code at 172–198 tok/s with minimal latency.
3. **Complex Reasoning & Benchmark Tasks:** Route to `Kimi K3` (57 Index). Delivers frontier-class CoT reasoning for challenging algorithmic tasks.
4. **Massive Context RAG (>250k tokens):** Route to `MiniMax-M3` (1M–2M context window) at $0.12/task.

---
*End of Chinese AI Ecosystem Intelligence Report.*
