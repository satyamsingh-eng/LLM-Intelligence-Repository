# Phase 6: SARVAX Model Routing Strategy

Based on the 5 Canonical Workloads and July 2026 Model Intelligence.

| Routing Category | Recommended Model | Secondary / Fallback | Rationale (Derived from Codebase Needs) |
| :--- | :--- | :--- | :--- |
| **Primary Production Model** | **Gemini 2.0 Flash** | Qwen 3.7 Max | Replaced DeepSeek V4 due to 60 RPM concurrency limits breaking the DAG. Gemini 2.0 provides infinite scaling via Vertex AI. Qwen 3.7 acts as high-throughput fallback. |
| **Highest Quality / Deep Reasoning** | **Kimi K3** or **o3-mini** | Claude 3.7 Sonnet | Kimi K3 (57 Index) dominates for deep multi-agent planning. o3-mini provides excellent mathematical reasoning. |
| **Fastest Edge / UI Feedback** | **Qwen 3.7 Max** | GLM-5.2 | Clocking at 198 TPS; critical for OneChat WebSocket streaming where UX requires instant TTFT. |
| **Best Long Context** | **Gemini 1.5/2.0 Pro** | Claude 3.5 Sonnet | Unmatched 2M context window. Essential for the "Large Report Generation" workload ingesting 100+ page financial PDFs. |
| **Best OCR Companion** | **Gemini 2.0 Flash** | Pixtral 12B (Local) | Gemini is the native C3A OCR engine. Seamless handover to text-generation layers. |
| **Enterprise / Compliance Strict** | **Llama 3.3 70B (Self-Hosted)**| Mistral Large 2 | Ensures Zero Data Retention (ZDR) and strict HIPAA/SOC2 air-gapping for sensitive wealth management data. |
| **Lowest Cost / Agent Swarm** | **MiMo-V2.5** | Gemini 2.0 Flash | $0.01 per task. Ideal for background validation agents in the multi-agent DAG that do not require frontier reasoning. |

### Workload Specific Routing
1. **Large Report Generation:** `Gemini 1.5 Pro` (Ingestion) -> `o3-mini` / `Kimi K3` (Reasoning) -> `DeepSeek V4 Pro` (Drafting).
2. **Multi-Agent DAG:** `MiMo-V2.5` (Routine nodes) + `DeepSeek V4 Pro` (Complex nodes).
3. **KYC Document Extraction:** `Gemini 2.0 Flash` (Vision -> Structured JSON).
4. **Meeting Intelligence:** `Qwen 3.7 Max` (High TPS streaming summarization).
