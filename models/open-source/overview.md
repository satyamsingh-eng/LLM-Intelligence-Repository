# Open Source & Local Models Ecosystem: Enterprise Intelligence Report (2026)

**Repository Target:** `/models/open-source/overview.md`  
**Maintained By:** C3A Labs / NYXI AI Research OS  
**Role / Scope:** Agent 3 (Open Source & Enterprise Deployment)  
**Last Updated:** July 2026  
**Objective:** Authoritative enterprise consulting guide on Meta, Mistral AI, Google, and Microsoft open-weight models, self-hosting VRAM specs, fine-tuning memory budgets, high-throughput deployment architectures, and data compliance frameworks.

---

## 1. Executive Summary & Strategic Overview

The open-weight LLM ecosystem in 2026 has reached enterprise parity with proprietary frontier models across most developer, domain-specific, and agency workflows. Enterprises now deploy open-weight models locally or on private cloud infrastructure to ensure **100% data sovereignty, zero-data-retention (ZDR) compliance, sub-10ms time-to-first-token (TTFT) performance, and dramatic cost savings at scale**.

### Key Ecosystem Players

*   **Meta AI (Llama Family):** The enterprise standard for foundational open weights. From ultra-lightweight edge models (Llama 3.2 1B/3B) to heavyweights (Llama 3.1/3.3 70B and Llama 3.1 405B, alongside Llama 4 early MoE architectures), Meta sets the benchmark for instruction tuning, tool use, multimodality, and reasoning.
*   **Mistral AI (Mistral / Mixtral / Codestral / Pixtral):** Europe's open-weights leader, pioneering Sparse Mixture-of-Experts (MoE) architectures (Mixtral 8x7B/8x22B), compact state-of-the-art models (Mistral Small 3/4, Ministral 3B/8B), code specialization (Codestral 22B), and native multimodal models (Pixtral 12B/Large).
*   **Google (Gemma Family):** Lightweight, highly efficient open models derived from Gemini research (Gemma 2 2B/9B/27B and Gemma 3 series). Feature innovative sliding window attention, logit capping, and exceptional performance per parameter for enterprise edge and mid-tier deployments.
*   **Microsoft (Phi Family):** World-class small language models (SLMs) and multimodal reasoning engines (Phi-3.5, Phi-4 14B, Phi-4-mini 3.8B, Phi-4-multimodal). Optimized for high synthetic data training, complex logic, math, coding, and constrained device execution.

---

## 2. Master Model Specifications & Capabilities Matrix

The table below provides a comprehensive comparison of active open-weight model architectures across Meta, Mistral AI, Google, and Microsoft.

| Provider | Model Name | Total Params | Active Params (Inference) | Architecture Type | Context Window | Native Modality | Primary License | Ideal Enterprise Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Meta** | Llama 3.2 1B | 1.23B | 1.23B | Dense Auto-regressive Transformer | 128k | Text | Llama 3.2 Community License | On-device mobile, local UI agents, ultra-fast pre-processing |
| **Meta** | Llama 3.2 3B | 3.21B | 3.21B | Dense Auto-regressive Transformer | 128k | Text | Llama 3.2 Community License | Edge search/summarization, lightweight intent classification |
| **Meta** | Llama 3.1 8B | 8.03B | 8.03B | Dense Auto-regressive Transformer | 128k | Text | Llama 3.1 Community License | General enterprise tasks, retrieval augmented generation (RAG) |
| **Meta** | Llama 3.2 11B Vision | 10.6B | 10.6B | Dense + Gated Cross-Attention Vision | 128k | Text + Image | Llama 3.2 Community License | Document OCR, chart understanding, visual Q&A |
| **Meta** | Llama 3.3 70B | 70.6B | 70.6B | Dense Auto-regressive Transformer | 128k | Text | Llama 3.3 Community License | Enterprise core intelligence, complex reasoning, coding |
| **Meta** | Llama 3.2 90B Vision | 89.4B | 89.4B | Dense + Gated Cross-Attention Vision | 128k | Text + Image | Llama 3.2 Community License | Complex visual document analysis, multimodal enterprise RAG |
| **Meta** | Llama 3.1 405B | 405.8B | 405.8B | Dense Auto-regressive Transformer | 128k | Text | Llama 3.1 Community License | Frontier open model baseline, synthetic data distillation, core LLM host |
| **Meta** | Llama 4 MoE (Preview) | ~400B MoE | ~55B - 90B | Sparse MoE (8/16 Experts) | 128k - 256k | Text + Vision | Llama 4 Community License | Next-gen high-throughput reasoning, multi-turn agent orchestrations |
| **Mistral**| Ministral 3B | 3.0B | 3.0B | Dense + Sliding Window Attention | 128k | Text | Commercial / Mistral Research | Edge AI, local browser assistants, latency-critical classification |
| **Mistral**| Ministral 8B | 8.0B | 8.0B | Dense + Interleaved Attention | 128k | Text | Commercial / Mistral Research | High-performance edge reasoning, local desktop agents |
| **Mistral**| Mistral 7B v0.3 | 7.25B | 7.25B | Dense + Sliding Window Attention | 32k | Text | Apache 2.0 | Standard open benchmark, fast fine-tuning baseline |
| **Mistral**| Mistral Small 3 / 4 | 24.0B | 24.0B | Dense Transformer | 32k - 128k | Text | Apache 2.0 / Commercial | High-speed enterprise operational intelligence, code & function calling |
| **Mistral**| Codestral 22B | 22.2B | 22.2B | Fill-in-the-Middle Dense Transformer | 32k | Text (Code Spec) | MNPL (Non-commercial) / Commercial | Code generation, repo refactoring, IDE autocomplete |
| **Mistral**| Pixtral 12B | 12.0B | 12.0B | Vision Encoder + Text Transformer | 128k | Text + Image | Apache 2.0 | Multimodal visual inspection, OCR, diagram parsing |
| **Mistral**| Mixtral 8x7B v0.1 | 46.7B | 12.9B | Sparse Mixture-of-Experts (8x7B) | 32k | Text | Apache 2.0 | Cost-effective high-throughput routing & general intelligence |
| **Mistral**| Mixtral 8x22B | 141.0B | 39.0B | Sparse Mixture-of-Experts (8x22B) | 64k | Text | Apache 2.0 | Large-scale open MoE, multi-lingual enterprise agent routing |
| **Mistral**| Mistral Large 2 | 123.0B | 123.0B | Dense Transformer | 128k | Text | MNA (Mistral Non-commercial) / Commercial | Heavy enterprise reasoning, multilinguality (12+ languages), complex code |
| **Google** | Gemma 2 2B | 2.6B | 2.6B | Dense + Sliding Window & Logit Capping| 8k | Text | Gemma Terms of Use | Mobile devices, edge IoT, micro-agent classifiers |
| **Google** | Gemma 2 9B | 9.2B | 9.2B | Dense + Grouped Query Attention | 8k | Text | Gemma Terms of Use | Fast local reasoning, high-precision structured data extraction |
| **Google** | Gemma 2 27B | 27.2B | 27.2B | Dense Transformer | 8k - 128k | Text | Gemma Terms of Use | Single-GPU workstation intelligence (RTX 4090 / A10G) |
| **Google** | Gemma 3 Series | 4B - 28B | 4B - 28B | Multi-Query + Rotary Embedding Dense | 32k - 128k | Text + Vision | Gemma Terms of Use | Next-gen edge visual grounding, code generation, local agent execution |
| **Microsoft**| Phi-3.5 Mini | 3.82B | 3.82B | Dense Transformer | 128k | Text | MIT License | Fast context reasoning, mobile / local edge agents |
| **Microsoft**| Phi-3.5 MoE | 41.9B | 6.6B | Sparse MoE (16x3.8B, 2 active) | 128k | Text | MIT License | High throughput reasoning, ultra-efficient token generation |
| **Microsoft**| Phi-3.5 Vision | 4.15B | 4.15B | Image Encoder + Dense Text | 128k | Text + Image | MIT License | Mobile visual document OCR, chart analysis, embedded vision |
| **Microsoft**| Phi-4 14B | 14.7B | 14.7B | Dense Transformer (Synthetic Trained) | 128k | Text | MIT License | SOTA mathematical reasoning, code synthesis, complex logic |
| **Microsoft**| Phi-4 Mini | 3.8B | 3.8B | Dense Transformer | 128k | Text | MIT License | Ultra-compact math & code reasoning on edge hardware |
| **Microsoft**| Phi-4 Multimodal | 5.6B | 5.6B | Speech + Vision + Text Transformer | 128k | Text + Image + Audio | MIT License | Omnimodal local assistant (real-time voice, vision, text) |

---

## 3. Self-Hosting Hardware Requirements & VRAM Specifications

Hardware requirement estimation is critical for sizing on-premise infrastructure, private cloud nodes, or edge hardware deployments.

### 3.1 Inference VRAM Sizing Formula & Rules of Thumb
*   **BF16 / FP16 Precision:** `VRAM (GB) ≈ (Parameter Size in B × 2.0) + KV Cache & Activation Overhead (~20%)`
*   **INT8 / FP8 Quantization:** `VRAM (GB) ≈ (Parameter Size in B × 1.0) + KV Cache & Activation Overhead (~15%)`
*   **INT4 / GGUF (Q4_K_M):** `VRAM (GB) ≈ (Parameter Size in B × 0.55 - 0.65) + KV Cache & Activation Overhead (~15%)`

*Note: KV Cache memory scales linearly with context length and batch size. Multi-Head Attention (MHA) consumes significantly more KV Cache than Grouped-Query Attention (GQA).*

### 3.2 Comprehensive Self-Hosting Hardware Matrix

| Model Name | Param Size | FP16/BF16 VRAM | INT8/FP8 VRAM | INT4 / GGUF VRAM | Minimum Hardware Setup | Recommended Enterprise Hardware | Optimal Inference Engine |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Llama 3.2 1B** | 1.2B | ~3.0 GB | ~1.8 GB | ~1.1 GB | Raspberry Pi 5 (8GB) / Mobile | Consumer Laptop / iPhone 15 Pro | llama.cpp / Ollama / ExecuTorch |
| **Llama 3.2 3B / Phi-4 Mini**| ~3.5B | ~8.0 GB | ~4.5 GB | ~2.5 GB | Apple M1/M2 Mac (16GB) | 1x NVIDIA RTX 4060 (8GB) | Ollama / vLLM |
| **Llama 3.1 8B / Gemma 2 9B**| ~8.0B | ~18.0 GB | ~10.5 GB | ~5.8 GB | 1x RTX 3090 / 4090 (24GB) | 1x NVIDIA A10G / L4 (24GB) | vLLM / SGLang |
| **Pixtral 12B / Llama 3.2 11B**| ~11-12B | ~26.0 GB | ~14.5 GB | ~8.2 GB | 1x RTX 4090 (24GB - Q4) | 1x NVIDIA A100 (40GB) or L40S (48GB) | vLLM (Vision) / SGLang |
| **Phi-4 14B / Gemma 3 14B** | ~14.5B | ~32.0 GB | ~17.5 GB | ~9.8 GB | 1x RTX 4090 (24GB - Q4) | 1x NVIDIA A100 (40GB) or L40S (48GB) | vLLM / SGLang |
| **Codestral 22B / Mistral Small 3**| ~22-24B | ~52.0 GB | ~28.0 GB | ~15.5 GB | 2x RTX 3090 / 4090 (48GB total) | 1x NVIDIA A100 (80GB) or L40S (48GB - INT8) | vLLM / TensorRT-LLM |
| **Gemma 2 27B** | 27.2B | ~60.0 GB | ~32.0 GB | ~18.0 GB | 1x RTX 4090 (24GB - Q4) | 1x NVIDIA A100 (80GB) or 2x L40S | vLLM / SGLang |
| **Mixtral 8x7B (MoE)** | 46.7B (13B Act) | ~96.0 GB | ~52.0 GB | ~28.0 GB | 2x RTX 4090 (48GB - INT4) | 2x NVIDIA A100 (80GB) or 1x H100 (80GB) | vLLM / TensorRT-LLM |
| **Llama 3.3 70B** | 70.6B | ~152.0 GB | ~82.0 GB | ~44.0 GB | 2x RTX 4090 (48GB - INT4) / Mac Studio 64GB | 2x NVIDIA A100 (80GB) or 2x H100 (80GB) | vLLM / SGLang / TensorRT-LLM |
| **Llama 3.2 90B Vision** | 89.4B | ~190.0 GB | ~102.0 GB | ~56.0 GB | Mac Studio M3 Ultra (128GB - INT4) | 4x NVIDIA A100 (80GB) or 2x H100 (80GB - FP8) | vLLM / TensorRT-LLM |
| **Mistral Large 2 (123B)** | 123.0B | ~265.0 GB | ~140.0 GB | ~78.0 GB | Mac Studio M3/M4 Ultra (192GB) | 4x NVIDIA A100 (80GB) or 2x H200 (141GB) | vLLM / SGLang |
| **Mixtral 8x22B (MoE)** | 141.0B (39B Act)| ~295.0 GB | ~155.0 GB | ~88.0 GB | Mac Studio M3/M4 Ultra (192GB) | 4x NVIDIA A100 (80GB) or 2x H100 (80GB - FP8) | vLLM / SGLang |
| **Llama 3.1 405B** | 405.8B | ~860.0 GB | ~445.0 GB | ~240.0 GB | 4x NVIDIA H100/H200 (80GB/141GB - FP8) | 8x NVIDIA H100 (80GB) or 8x H200 (141GB - BF16) | TensorRT-LLM / SGLang / vLLM |

---

## 4. Fine-Tuning Capabilities & Memory Overhead

Fine-tuning open-weight models allows enterprise customization for proprietary domain terminology, JSON schema adherence, policy alignment, and specialized task execution.

### 4.1 Fine-Tuning Paradigms Comparison

1.  **Full Fine-Tuning (FFT):** Updates 100% of model parameters. Requires storing gradients, optimizer states (AdamW), and activations in FP32/BF16.
    *   *Memory Overhead:* ~16–18 Bytes per parameter (without DeepSpeed ZeRO-3) or ~6–8 Bytes per parameter (with ZeRO-3 offloading).
2.  **LoRA (Low-Rank Adaptation):** Freezes base model weights and trains low-rank adapter matrices (rank $r=8, 16, 32, 64$).
    *   *Memory Overhead:* Base FP16 weights (2B/param) + ~0.2B/param for LoRA gradients/states + activation memory.
3.  **QLoRA (Quantized LoRA):** Freezes base model weights quantized to NormalFloat4 (NF4) / INT4, while training FP16/BF16 LoRA adapters.
    *   *Memory Overhead:* Base 4-bit weights (~0.55B/param) + LoRA adapter states (~0.1–0.3B/param) + activation memory with gradient checkpointing.

### 4.2 Fine-Tuning VRAM Requirements Matrix (128k / 8k Context)

| Target Model Size | Full Fine-Tuning (BF16 + AdamW) | Full FT (ZeRO-3 + Offload) | Standard LoRA (BF16) | QLoRA (4-bit Base + NF4) | Recommended FT Framework | Minimum Hardware for QLoRA | Minimum Hardware for Full FT |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1B - 3B** (Llama 3.2 / Phi-3.5) | ~48 - 64 GB | ~16 - 24 GB | ~12 - 16 GB | ~6 - 8 GB | Unsloth / Torchtune / TRL | 1x Consumer GPU (12GB) | 1x A100 (80GB) or 2x RTX 4090 |
| **8B - 9B** (Llama 3.1 8B / Gemma 2 9B) | ~140 - 160 GB | ~36 - 48 GB | ~28 - 36 GB | ~12 - 16 GB | Unsloth / Axolotl / LLaMA-Factory | 1x RTX 3090 / 4090 (24GB) | 2x A100 (80GB) or 4x L40S |
| **14B - 27B** (Phi-4 14B / Gemma 2 27B) | ~280 - 450 GB | ~80 - 120 GB | ~54 - 72 GB | ~22 - 28 GB | Axolotl / LLaMA-Factory / DeepSpeed | 1x RTX 4090 (24GB) / A10G | 4x - 8x A100 (80GB) |
| **70B** (Llama 3.3 70B) | ~1,200+ GB | ~280 - 360 GB | ~160 - 200 GB | ~48 - 56 GB | Axolotl / DeepSpeed ZeRO-3 | 1x A100 (80GB) or 2x RTX 4090 | 2x 8x H100 (80GB) Cluster |
| **123B - 141B** (Mistral Large 2 / Mixtral) | ~2,200+ GB | ~550 - 700 GB | ~300 - 380 GB | ~88 - 110 GB | DeepSpeed ZeRO-3 / Megatron-LM | 2x A100 (80GB) or 2x H100 | Multi-Node GPU Cluster (16x H100) |
| **405B** (Llama 3.1 405B) | ~7,000+ GB | ~1,800 - 2,200 GB | ~900 - 1,100 GB | ~260 - 320 GB | Megatron-LM / Torch FSDP2 | 4x A100 (80GB) / 4x H100 | Large Multi-Node Cluster (64x+ H100) |

### 4.3 Recommended Enterprise Fine-Tuning Tooling Stack
*   **Unsloth:** Up to 2x-5x faster training speed and 60%-80% memory reduction for single-GPU QLoRA/LoRA fine-tuning (supports Llama, Gemma, Mistral, Phi).
*   **Axolotl:** Streamlined config-driven framework for multi-GPU LoRA and Full FT (integrates FlashAttention-2, Deepspeed, QLoRA).
*   **LLaMA-Factory:** User-friendly UI and unified CLI interface supporting over 100+ open-source models, DPO, PPO, ORPO, and QLoRA fine-tuning.
*   **Torchtune:** PyTorch-native modular library maintained by Meta for easy customization, fine-tuning, and export to GGML/vLLM.

---

## 5. Enterprise Deployment Architecture & Optimization Strategies

When deploying open-weight models at production scale (100+ requests/sec, strict SLAs), architecture selection directly impacts operational expense (OpEx) and system stability.

```
+-----------------------------------------------------------------------------------+
|                            C3A LABS HYBRID ROUTING GATEWAY                        |
|                                                                                   |
|  [Incoming Request] ---> [PII / IP Classifier & Policy Routing Engine]             |
+------------------------------------------+----------------------------------------+
                                           |
                    +----------------------+----------------------+
                    |                                             |
                    v (Sensitive Data / Internal IP)              v (Non-Sensitive / General)
  +-----------------------------------+         +-----------------------------------+
  |   LOCAL AIR-GAPPED ENTERPRISE     |         |     MANAGED CLOUD PROPRIETARY     |
  |       INFERENCE CLUSTER           |         |          MODEL ROUTE            |
  |                                   |         |                                   |
  |  +-----------------------------+  |         |  +-----------------------------+  |
  |  | Serving Engine: vLLM /      |  |         |  | Claude 3.5 Sonnet /           |  |
  |  | SGLang / TensorRT-LLM       |  |         |  | GPT-4o / Gemini 1.5 Pro       |  |
  |  +--------------+--------------+  |         |  +-----------------------------+  |
  |                 |                 |         +-----------------------------------+
  |  +--------------v--------------+  |
  |  | Local Models:               |  |
  |  | - Llama 3.3 70B (Core Logic) |  |
  |  | - Mistral Small 3 (Fast RAG)|  |
  |  | - Phi-4 14B (Code/Math)     |  |
  |  +-----------------------------+  |
  +-----------------------------------+
```

### 5.1 High-Throughput Serving Engine Comparison

| Feature / Engine | vLLM | SGLang | TensorRT-LLM | TGI (HuggingFace) | Ollama / llama.cpp |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Primary Focus** | General Enterprise Production | Complex Prompt / Multi-Turn / Structured | Peak Performance on NVIDIA Hardware | HuggingFace Native Cloud Integration | Local Desktop / Edge / CPU+GPU |
| **Throughput / Latency** | Very High | Exceptional (RadixAttention) | Maximum (Engine compiled) | High | Moderate (Single User/Small Batch) |
| **PagedAttention** | Native (Pioneer) | Native | Native | Native | Custom KV Cache |
| **Prefix Caching** | Supported | Advanced (RadixTree) | Supported | Supported | Partial |
| **Quantization Support**| AWQ, GPTQ, FP8, INT8 | AWQ, GPTQ, FP8, INT4 | FP8, INT8, INT4 AWQ | AWQ, EETQ, FP8 | GGUF (Q2-Q8), AWQ |
| **Multi-GPU Scale** | Tensor / Pipeline Parallel | Tensor / Pipeline Parallel | Advanced Tensor / Pipeline | Tensor Parallelism | Basic Split Layering |
| **Deployment Fit** | Industry Standard API Server | Enterprise Agent / Multi-step Workflows | Extreme Low Latency Mission Critical | Kubernetes / HF Cloud Endpoints | Developer Laptops, Edge Nodes |

### 5.2 Key Serving Optimizations Enabled in Production
1.  **PagedAttention:** Eliminates KV cache memory fragmentation by allocating memory in dynamic blocks (similar to virtual memory in operating systems), enabling up to 24x higher throughput.
2.  **Continuous / In-Flight Batching:** Dynamically batches incoming prefill and decode requests at the iteration level rather than request level, maintaining >90% GPU utilization.
3.  **Chunked Prefill:** Breaks long prompts into smaller chunks to prevent prefill requests from starving decode iterations, significantly improving Time to First Token (TTFT) and Inter-Token Latency (ITL).
4.  **Speculative Decoding:** Uses a small, fast draft model (e.g., Llama 3.2 1B) to generate candidate tokens, which are verified in parallel by a larger target model (e.g., Llama 3.3 70B), boosting speed by 1.5x–2.5x without quality loss.
5.  **FP8 Precision KV Caching:** Halves the memory consumption of KV caches with negligible impact on accuracy, doubling effective batch capacity per GPU node.

---

## 6. Data Compliance, Privacy & Hybrid Architecture Consulting

For enterprise clients in financial services, healthcare, defense, and SaaS product engineering, hosting local open-weight models provides structural compliance advantages that API providers cannot match.

### 6.1 Compliance Standards Alignment Matrix

| Compliance Domain | Enterprise Requirement | Local Open-Weight Solution | Verification & Architecture |
| :--- | :--- | :--- | :--- |
| **Data Sovereignty** | Data must never leave designated geographical region or private VPC. | On-premise or sovereign cloud hosting (AWS Outposts, GCP Anthos, Bare Metal). | Complete network perimeter control; zero external egress endpoints. |
| **SOC 2 Type II** | Continuous verification of security, confidentiality, and processing integrity. | Private vLLM/SGLang clusters isolated inside Kubernetes VPCs with RBAC. | Log auditing via Prometheus/Grafana; no third-party vendor data sharing. |
| **HIPAA Compliance** | Protection of Protected Health Information (PHI) from unauthorized disclosure. | Air-gapped self-hosted model instances (e.g., Llama 3.3 70B / Phi-4 14B). | Executes entirely within BAA-bounded VPC environment. |
| **Zero Data Retention** | Guarantee that user prompts/completions are not logged or used for model training. | Model runs statelessly in RAM/VRAM. Complete control over logging pipelines. | Verification via custom telemetry disablement and memory wiping. |
| **EU AI Act** | Technical documentation, risk assessment, transparency, and copyright compliance. | Open-weight models with documented training datasets and weight inspection. | Complete auditability of model weights and internal activations. |

### 6.2 C3A Labs Hybrid Routing Architecture Framework

To balance performance, cost, and strict compliance, C3A Labs recommends a **Hybrid Multi-Tier Routing Architecture**:

1.  **Tier 1: On-Device & Edge Routing (Local SLMs)**
    *   *Models:* Llama 3.2 1B/3B, Ministral 3B, Phi-4 Mini.
    *   *Function:* Intent classification, regex validation, sensitive PII anonymization, local document filtering.
2.  **Tier 2: Private Cloud / Air-Gapped Local Cluster (Medium/Large Open Models)**
    *   *Models:* Llama 3.3 70B, Phi-4 14B, Codestral 22B, Gemma 2 27B, Pixtral 12B.
    *   *Function:* Core proprietary logic, source code generation, internal document RAG, clinical/financial data processing.
3.  **Tier 3: Sanitized External Frontier Routing (Proprietary APIs)**
    *   *Models:* Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro.
    *   *Function:* Non-sensitive, high-complexity multi-modal reasoning or ultra-large context synthesis, routed only after local PII/IP scrubbing.

---

## 7. Summary & Recommendations for C3A Labs Deployments

*   **For General Enterprise Core Reasoning:** Deploy **Llama 3.3 70B** on 2x H100 (80GB) or 2x A100 (80GB) using **vLLM** with FP8 quantization and continuous batching.
*   **For High-Speed Code Generation & IDE Integration:** Deploy **Codestral 22B** or **Phi-4 14B** on a single NVIDIA L40S or A100 (40GB).
*   **For Local Workstation / Developer Laptops:** Standardize on **Ollama / llama.cpp** with **Llama 3.1 8B**, **Phi-4 Mini**, or **Gemma 2 9B** (Q4_K_M GGUF format).
*   **For Complex Agentic Workflows & Multi-Turn Prompting:** Utilize **SGLang** serving engine with **RadixAttention** for high cache hit rates and minimal TTFT latency.
*   **For Fine-Tuning Domain Adapters:** Utilize **Unsloth** for rapid single-GPU QLoRA iteration, exporting final adapters to HuggingFace or GGUF formats for production serving.
