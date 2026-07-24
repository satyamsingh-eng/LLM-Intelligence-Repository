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
