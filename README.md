# C3A Labs LLM Intelligence Repository

**Maintained by:** NYXI (AI Research OS)
**Last Updated:** July 2026
**Confidence Standards:** Multi-source verification required. Unknowns explicitly flagged.

## Executive Summary
This repository serves as the definitive internal intelligence layer powering **SARVAX**, **KARAX**, and C3A Labs' Enterprise AI architecture decisions. It is not a static document, but a **continuously updated** intelligence platform mapping the intersection of global AI model releases, financial services workloads, token economics, and enterprise compliance constraints.

## Core Capabilities
- **Workload Driven:** All benchmarks are mapped directly against 5 canonical enterprise workloads derived from the SARVAX `karaxai-website` codebase. (No assumed generic use-cases).
- **Global Frontier Mapping:** Tracks US, EU, and Chinese AI ecosystems independently, capturing rapid pricing fluctuations and benchmark shifts (e.g., the open-weight SWE-bench frontier crossover).
- **Compliance Aware:** Strictly filters models based on Enterprise data residency, SOC2, HIPAA, and Zero Data Retention (ZDR) capabilities.
- **Economic Scaling:** Projects token costs out to 100,000+ document workloads using precise real-world cache hit ratios and batch-API optimizations.

## Repository Structure
1. `/01-Product-Discovery/` — Base architecture mapped from SARVAX dev branch.
2. `/02-Codebase-Intelligence/` — API endpoints, DAG implementations, memory vectors.
3. `/03-Capability-Mapping/` — Inventory of implemented features vs theoretical.
4. `/04-Workload-Benchmarks/` — The 5 Canonical SARVAX Enterprise Workloads.
5. `/models/us/` — OpenAI, Anthropic, Google, xAI, Meta.
6. `/models/china/` — DeepSeek, Qwen, Kimi, GLM, MiniMax.
7. `/models/open-source/` — Llama, Mistral, Gemma, Phi local hardware specs.
8. `/06-Routing-Strategy/` — Decision logic for dynamic model orchestration.
9. `/07-Token-Economics/` — Multi-scenario cost calculators (Batch + Cache).
10. `/08-Research-Backlog/` — Unresolved gaps and disputed claims (e.g., Llama 4 10M context).
11. `/09-Maintenance-Framework/` — The 30-day continuous revalidation schedule.

## Source of Truth Hierarchy
1. GitHub Codebase (`c3alabs/karaxai-website`)
2. Official Vendor Documentation & API Endpoints
3. Official Pricing Pages
4. Independent Benchmark Aggregators (LMSYS, SWE-bench)
