# Workload 5: Agentic Portfolio Intelligence

**Confidence Score:** High (Combines OneChat Memory + MCP API connections)
**Last Validated:** July 2026

## Overview
- **Business Objective:** Provide wealth advisors with a real-time, conversational agent that cross-references a client's specific portfolio holdings (via Memory/RAG) against live market data (via MCP) to suggest tax-loss harvesting or reallocation.
- **Industry:** Wealth Management.
- **Target Users:** Financial Advisors.
- **Problem Being Solved:** Advisors lack instant, context-aware answers to "How does today's fed rate hike impact Client X's tech exposure?"

## SARVAX Architecture Mapping
- **Workflow Diagram:** User Query (OneChat) -> Context Assembly (Agent Memory) -> MCP Call (Market Data API) -> Reasoning -> Formatted Answer Generation.
- **AI Models Required:**
  - Reasoning: Kimi K3 / Claude Opus 4.6 (Needs deep financial logic).
  - Fast Generation: Qwen3.7 Max (For UX responsiveness).
- **Agent Architecture:** Conversational RAG + Tool Use.
- **Reasoning Complexity:** Very High (Numerical reasoning, market context, client risk profile).
- **OCR Requirements:** Low.

## Performance & Economic Parameters
- **Estimated Context Size:** 20,000 tokens (Portfolio history + Market news context).
- **Estimated Input Tokens:** 15,000 tokens per turn (heavy caching utilization expected).
- **Estimated Output Tokens:** 1,500 tokens (Charts/Markdown).
- **Average Runtime:** 5 - 12 seconds.
- **Expected Cost:** ~$0.01 - $0.03 per query.

## Quality & Evaluation
- **Latency Targets:** < 5s for streaming TTFT (Time to First Token).
- **Quality Metrics:** Financial accuracy, strict adherence to client risk limits (zero hallucination in ticker symbols or numbers).
- **Failure Modes:** Tool API timeouts, mathematical reasoning failures during portfolio weight calculations.
- **Evaluation Criteria:** Accuracy measured against quantitative model outputs (e.g., Bloomberg/Morningstar).
