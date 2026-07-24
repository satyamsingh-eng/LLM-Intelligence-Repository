# Phase 3: SARVAX Capability Mapping

| Capability | Implementation Mechanism (Codebase Evidence) |
| :--- | :--- |
| **Real-time Chat** | `OneChat` component + `runAgentStream` (WebSocket) |
| **Workflow Automation** | `Workflow 2.0` DAG (Nodes with `depends_on`, `tools`) |
| **Document Intelligence** | HR Pipeline (`uploadHrResumes`) extensible to enterprise PDFs |
| **Meeting Intelligence** | `createMeetingWithBot` and `is_meeting_step` flags in Workflows |
| **Tool Calling (API)** | **MCP** integration (`createMcpServer`, API keys injection) |
| **Long-Term Memory** | `updateAgentMemory`, `fetchAgentMemoryEntry` (Vector-backed) |
| **Agentic Collaboration** | `getOrganizationAgents`, `addAgentToOrganization` |
| **Report Generation** | OneChat **Artifacts** rendering engine |
| **Skills Execution** | Skills Marketplace (Public/Private gating, execution environment) |

## Advanced Deep Research Extensions
| Capability | Engine / Implementation |
|---|---|
| **Autonomous Deep Research** | `GPT-Researcher` & `STORM` (Stanford) |
| **Knowledge Graph RAG** | `GraphRAG` (Microsoft), `LightRAG`, & `R2R` (SciPhi) |
| **Universal Document Conversion** | `MarkItDown` (Microsoft) |
| **LLM Web Crawling** | `Crawl4AI` & `Firecrawl` |
| **Enterprise Blueprints** | `NVIDIA AI-Q` & `NVIDIA Skills Catalog` |
| **Multi-Agent Swarms** | `CrewAI` |
