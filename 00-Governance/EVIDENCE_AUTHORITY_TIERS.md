# SARVAX Evidence Authority Tiering System
**Effective Date:** 2026-07-25
**Scope:** Strict governance rules for primary and secondary source validation across the SARVAX AI Intelligence Platform.

## Core Principle
"Never trust a single source. Validate against multiple independent sources. Tier 1 overrides all lower tiers."

---

### Tier 1: Absolute Truth (Authority Score: 100)
**Definition:** Direct vendor publications that represent contractual, technical, or financial guarantees.
* Official Documentation
* Official Pricing Pages
* Official APIs & API Schemas
* Official SDKs
* Official Release Notes
* Official GitHub Repositories (owned by the vendor)
* Official Engineering Blogs (owned by the vendor)

### Tier 2: Empirical Truth (Authority Score: 90)
**Definition:** Independent, high-trust empirical measurement organizations and leaderboards.
* Artificial Analysis
* LMSYS Chatbot Arena
* OpenRouter Benchmarks
* SWE-Bench (Verified & Pro)
* Papers With Code
* TAU-Bench (including TAU Banking)
* OpenAI Evals & HuggingFace Open LLM Leaderboard

### Tier 3: Academic Truth (Authority Score: 75)
**Definition:** Peer-reviewed or pre-print academic research containing rigorous methodology.
* Academic Papers (NeurIPS, ICML, ICLR)
* arXiv Preprints
* Conference Papers
* University Research Labs (Stanford, MIT, Berkeley, Tsinghua)

### Tier 4: Community Signal (Authority Score: 50)
**Definition:** Anecdotal evidence, developer experience, and unofficial guidance. **Cannot be used to justify pricing, benchmarks, or SLA guarantees.**
* GitHub Discussions & Issues (non-vendor)
* Reddit (r/LocalLLaMA, r/MachineLearning)
* Hacker News (Y Combinator)
* Established Community Blogs (e.g., Lilian Weng, Simon Willison)

### Tier 5: Unverified Anecdote (Authority Score: 0 / Never Trust Alone)
**Definition:** High-noise, high-bias, or engagement-driven platforms. Must be immediately validated against Tier 1/2.
* Medium Articles
* YouTube Videos
* Personal Blogs
* Twitter/X Threads

---

## Conflict Resolution & Merging Rules
1. **Tier 1 Overrides All:** If a Tier 2 benchmark claims an API supports streaming, but Tier 1 documentation states it does not, the Tier 1 documentation is recorded as the absolute truth.
2. **Dual-Source Minimum:** Any numerical value (Pricing, Context Window, Benchmark) must have at least one Tier 1 source and one cross-validating source (Tier 1 or Tier 2).
3. **No Tier 5 Commits:** No architectural decision or code change may be merged if the primary justification stems from a Tier 4 or Tier 5 source.
