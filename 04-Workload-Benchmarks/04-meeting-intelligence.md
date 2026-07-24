# Workload 4: Meeting Intelligence & CRM Writeback

**Confidence Score:** High (Directly mapped to `createMeetingWithBot` and `is_meeting_step`)
**Last Validated:** July 2026

## Overview
- **Business Objective:** Transcribe wealth advisor-client meetings, extract action items, generate a compliance-safe summary, and automatically update Salesforce/HubSpot via MCP.
- **Industry:** Wealth Management Advisory.
- **Target Users:** Wealth Advisors, Client Relationship Managers.
- **Problem Being Solved:** Advisors spend 30-45 minutes post-meeting on data entry and CRM hygiene.

## SARVAX Architecture Mapping
- **Workflow Diagram:** Audio Transcript Ingestion -> Summarization Agent -> Action Item Extraction Agent -> MCP Tool Call (CRM Update) -> Notification.
- **AI Models Required:**
  - Summarization / Extraction: Claude Haiku 4.5 / Grok-code-fast-1 (High TPS).
  - CRM Mapping: GLM-4.7 / MiniMax M3.
- **Agent Architecture:** Two-step linear pipeline.
- **Reasoning Complexity:** Medium (Understanding conversational context and mapping to structured CRM fields).
- **OCR Requirements:** None.

## Performance & Economic Parameters
- **Estimated Context Size:** 15,000 - 25,000 tokens (1-hour transcript).
- **Estimated Input Tokens:** ~20,000.
- **Estimated Output Tokens:** ~1,000.
- **Average Runtime:** 5 - 10 seconds.
- **Expected Cost:** ~$0.02 - $0.05 per meeting.

## Quality & Evaluation
- **Latency Targets:** Available immediately post-meeting (< 30 seconds).
- **Quality Metrics:** Accurate action item assignment, CRM field matching accuracy.
- **Failure Modes:** Transcript speaker diarization errors leading to wrong action item assignments.
- **Evaluation Criteria:** Advisor acceptance rate (how often they edit the CRM payload before confirming).
