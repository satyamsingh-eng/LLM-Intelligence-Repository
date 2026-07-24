# Research Backlog & Unknown Intelligence

As of July 2026, the following intelligence gaps exist and must be targeted in subsequent monthly research cycles.

## 1. Compliance Verification Gaps
- **Anthropic SOC2 & ISO42001:** Assumed based on enterprise presence, but primary-source documentation was not located in the baseline pass. *Requires direct verification on trust.anthropic.com.*
- **Google Cloud Gemini HIPAA/GDPR:** Assumed via GCP blanket compliance, but specific Vertex AI Gemini documentation is missing. *Requires GCP security portal audit.*
- **Chinese Labs (Qwen, DeepSeek, Kimi):** Zero public verification of Western compliance standards (SOC2, HIPAA). Data residency is presumed mainland China. *Requires enterprise sales contact.*

## 2. Unverified Pricing & Models
The following models have been identified in the market but lack verified, multi-source pricing and benchmark data:
- Tencent Hunyuan
- Baidu ERNIE
- SenseTime SenseNova
- 01.AI Yi
- StepFun
- ByteDance Doubao
- AI21 Jamba
- Aleph Alpha (Sovereign EU)

## 3. Disputed Technical Specifications
- **DeepSeek Context Window:** Sources conflict between 64K (Base API) and 1M (DeepSeek Sparse Attention). *Requires load-testing.*
- **Llama 4 Scout Context:** Claimed 10M context window by Meta. *Requires independent retrieval benchmark validation.*
- **Kimi Context:** Aggregators conflict between 128K, 262K, and 2M. *Requires Moonshot AI developer portal audit.*
