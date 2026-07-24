# Phase 2: SARVAX Codebase Intelligence

## Architecture Map
- **Frontend / Client**: Next.js 14 + React 18 + Tailwind.
- **API Layer**: `/src/api/api.ts` acting as the central nexus (91 exported endpoints).
- **Communication Protocol**: WebSockets for OneChat streaming (`runAgentStream`), REST for CRUD.

## AI Orchestration Layer
- **LLM Integrations**: Providers detected via keyword analysis include OpenAI, Anthropic, Gemini, and DeepSeek (via OpenCode Go).
- **OCR Implementation**: Implicitly handled via Gemini Pro Vision / Google OCR pipelines for document ingestion (e.g., Resume parser).
- **Memory & Vector DB**: Vector integration explicitly handled via Agent Memory API endpoints.
- **Workflow Engine**: 
  - Executed via `runAgent` / `runAgentStream` payloads containing tokenized session data.
  - State managed via `WorkflowRun` types holding `execution_duration` and `workflow_run_token`.
- **Tool Calling**: Managed natively via MCP (Model Context Protocol). `listMcpServers`, `verifyMcpServer` exist in API.
