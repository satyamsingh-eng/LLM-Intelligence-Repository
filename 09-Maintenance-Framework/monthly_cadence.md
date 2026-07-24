# Continuous Maintenance Framework

To ensure the LLM Intelligence Repository remains the authoritative source of truth for SARVAX, the following validation protocols must be executed on a 30-day cadence.

## 1. Pricing Revalidation
**Procedure:** Agents must directly scrape the official developer pricing pages (e.g., `openai.com/api/pricing`, `platform.claude.com/docs/pricing`) and update the `07-Token-Economics` matrices.
**Triggers:** If API pricing drops by >20%, immediately trigger a Routing Strategy review to determine if a Fallback model should become a Primary model.

## 2. Benchmark Recalibration
**Procedure:** Aggregate new scores from trusted sources (SWE-bench, LMSYS Chatbot Arena, MMLU-Pro, GPQA Diamond).
**Focus:** Specifically track the "Open-Weight vs Closed" delta on SWE-bench. If open-weight models maintain a >10% lead (e.g., GLM-4.7), aggressively pivot enterprise workloads toward local hosting.

## 3. SARVAX Codebase Synchronization
**Procedure:** Scan `c3alabs/karaxai-website` (dev branch).
**Focus:** Identify new LLM integrations, changes to the `Workflow 2.0` DAG schema, or new MCP servers. Adjust the Workload Benchmarks accordingly.
