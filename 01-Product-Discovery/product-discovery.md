# Phase 1: SARVAX Product Discovery

**Source of Truth:** `/Users/satyyy/Downloads/karaxai-website-staging` (dev branch)

## Core Modules & Journeys
1. **OneChat Engine**: 
   - A unified interface (281KB React component) utilizing WebSockets for real-time token streaming.
   - **Artifacts:** Code/Markdown rendering interface for dynamic generation.
   - **Projects/Bundles:** Organization context for isolated LLM execution.
2. **Workflow 2.0 (DAG Engine)**: 
   - Multi-step Directed Acyclic Graph (DAG) executor.
   - Features: `stepByStepFlow`, `depends_on`, `action_type`, `is_meeting_step`.
   - Tool connections with gating logic (`WORKFLOW_V2_PER_NODE_SKILL_PICKER_PRD.md`).
3. **Agent Builder & Memory**: 
   - Full CRUD for Agent definitions.
   - **Agent Memory**: Endpoints for CRUD on long-term memory (`createAgentMemory`, `fetchAgentMemoryEntry`).
4. **Skills Marketplace & MCP**: 
   - Marketplace for skills (forking, versioning, visibility).
   - **MCP Server Management**: Native Model Context Protocol (MCP) server creation and API key injection for enterprise tool calling.
5. **Specialized Pipelines**: 
   - **Meeting Bot**: `createMeetingWithBot` endpoint for conversational ingestion.
   - **HR Intelligence**: `uploadHrResumes`, `getHrBotInterviews` (Pattern replicable for KYC).
