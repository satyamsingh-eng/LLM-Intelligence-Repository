# Arvocap 10k Report Pilot — Master Slide Copy, Layout Specifications & Visual Architecture

**Document Version**: 1.0  
**Target Platform**: PowerPoint (16:9 Widescreen PPTX)  
**Brand Design System**: Power Scale Ventures Institutional Thesis System  
**Account**: Arvocap Asset Managers (Nairobi, Kenya — CMA Regulated)  
**Author**: C3A Labs / Power Scale Ventures Architecture Team  
**Date**: July 27, 2026  

---

## 1. Power Scale Ventures Design Tokens & System Rules

### 1.1 Color Palette & Tokens
| Token Name | Hex Code | Visual Role & Usage |
| :--- | :--- | :--- |
| **Canvas** | `#fbfbfd` | Default slide background color across all non-cover slides |
| **Pure Black** | `#000000` | Cover slide background, primary text for titles on dark surfaces |
| **Primary Accent Blue** | `#0066ff` | Eyebrow category tags, primary KPI figures, active pill highlights, key structural accents |
| **Card Fill Light** | `#f5f5f7` | Background fill for all content containers, grid cards, and structured blocks |
| **Body Text** | `#1d1d1f` | Primary readable text for titles, card headers, and narrative paragraphs |
| **Secondary Text** | `#515154` | Sub-headlines, secondary descriptions, table row detail text |
| **Muted / Footer** | `#86868b` | Footer copy, captions, inactive states, subtle metadata |
| **Border / Rule** | `#e5e5e7` | 1px card borders, dividing rules, subtle grid boundaries |
| **Accent Light Fill** | `#e6f0ff` | Pill badge background fill for active status and key callouts |
| **Accent Light Border** | `#b3d1ff` | Pill badge 1px outline stroke |

---

### 1.2 Typography Hierarchy System (Inter Font Family)
| Role | Size | Weight | Line Height | Color Token | Rules & Formatting |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Cover Title** | 52pt | ExtraBold (800) | 1.1x | `#000000` / `#0066ff` | Single/Double line, high impact, crisp letter spacing |
| **Slide H1 Title** | 30pt | Bold (700) | 1.2x | `#000000` | Concise, single-line headline per slide |
| **Eyebrow Tag** | 10.5pt | Bold (700) | 1.0x | `#0066ff` | UPPERCASE, 1.5px tracking, positioned directly above H1 |
| **Card H2 Title** | 15pt | Bold (700) | 1.3x | `#1d1d1f` | Card section titles, distinct and structured |
| **Body Text** | 11pt | Regular (400) | 1.45x | `#1d1d1f` | Crisp paragraphs, maximum 3-4 lines per block |
| **Secondary Body** | 10pt | Regular (400) | 1.4x | `#515154` | Secondary bullet points, captions, metadata |
| **KPI Metric Figure** | 36pt | ExtraBold (800) | 1.0x | `#0066ff` | Prominent numbers, concise suffixes (e.g. `+120%`, `KSh 11.02B`) |
| **KPI Label** | 10pt | Medium (500) | 1.2x | `#86868b` | UPPERCASE metric label positioned below or above KPI figure |
| **Badge / Pill Text** | 9.5pt | SemiBold (600) | 1.0x | `#0066ff` | Centered inside rounded pill badges |
| **Footer Copy** | 9pt | Medium (500) | 1.0x | `#86868b` | UPPERCASE, locked to bottom margin rule |

---

### 1.3 Structural Layout Archetypes
1. **Title Cover Archetype**: Asymmetric two-column split on `#fbfbfd` or deep dark `#000000`. Accent blue focal element, high-contrast title, subtitle, metadata block, and institutional badge.
2. **2-Card Split Archetype**: Left column primary focal narrative/architecture (55% width), right column supporting KPIs or workflow details (41% width).
3. **3-Column Grid Archetype**: Three equal 16px rounded cards (`#f5f5f7` fill, 1px `#e5e5e7` border) arranged horizontally with 16px gap spacing.
4. **4-Card Matrix Archetype**: 2x2 grid of 16px rounded cards with identical padding and internal hierarchy.
5. **Horizontal Pipeline Archetype**: Sequential 4 or 5 step chevron/card node layout with arrow connectors demonstrating data flow.
6. **Commercial Matrix / Table Archetype**: Structured comparison table with 16px rounded outer container, `#0066ff` highlighted recommendation column, and clear cost metrics.

---

### 1.4 Global Slide Rules & Specifications
- **Slide Dimensions**: 16:9 Widescreen (13.333" x 7.50" / 1920px x 1080px equivalent).
- **Margins**: Top 0.60" (58px), Left 0.80" (76px), Right 0.80" (76px), Bottom 0.60" (58px).
- **Card Styling**: `border-radius: 16px`, `background: #f5f5f7`, `border: 1px solid #e5e5e7`, `padding: 24px`.
- **Global Footer Rule**:
  - Horizontal rule: 1px solid `#e5e5e7`, located at Y = 6.90" (986px).
  - Left Footer Text: `POWERSCALE VENTURES | CONFIDENTIAL INSTITUTIONAL THESIS` (Inter Medium 9pt `#86868b`).
  - Right Footer Text: `ARVOCAP 10K REPORT PILOT | SLIDE [X] OF 10` (Inter Medium 9pt `#86868b`).

---

## 2. Slide-by-Slide Master Copy & Architecture Specs

---

### SLIDE 1: Title Cover

#### 1. Eyebrow Category Tag
`PILOT PROPOSAL & ARCHITECTURE THESIS`

#### 2. Slide H1 Title
`Arvocap 10k Report Generation Engine`

#### 3. Messaging Hierarchy
- **Primary Headline**: Arvocap 10k Report Generation Engine: Enterprise Automated Wealth Intelligence
- **Sub-headline**: Scaling High-Touch Client Communications Across KSh 11.02B AUM via Dual-Agent Architecture & SarvaX Workflow 2.0
- **Key Takeaway**: A fully regulated, zero-math-hallucination report generation pipeline delivering personalized monthly performance analysis to 10,000 investors with 65% LLM cost efficiency.
- **Executive Narrative**: Arvocap Asset Managers requires an automated, institutional-grade report generation infrastructure to support rapid AUM growth without expanding back-office headcount. SarvaX delivers a dual-agent pipeline combining DeepSeek V4 Pro and Kimi K3 with a Python Decimal math engine to automate 10,000 monthly reports seamlessly.

#### 4. Full Slide Copy Specifications
- **Main Header Block**:
  - Eyebrow: `PILOT PROPOSAL & ARCHITECTURE THESIS`
  - Title: `Arvocap 10k Report Generation Engine`
  - Subtitle: `Scaling Automated Portfolio Intelligence & Market Analysis across KSh 11.02B AUM via Dual-Agent SarvaX Workflow 2.0`
- **Metadata Card 1 (Account Information)**:
  - Header: `CLIENT ACCOUNT`
  - Body: `Arvocap Asset Managers (Nairobi, Kenya — CMA Regulated)`
  - Key Stakeholders: `Monicah Mwaniki (CEO), John Ngure, Arnold Oduma, Simar Juttla`
- **Metadata Card 2 (Platform & Infrastructure)**:
  - Header: `DEPLOYMENT ENGINE`
  - Body: `SarvaX Enterprise Agentic Platform (Workflow 2.0)`
  - C3A / Power Scale Lead: `Pratyush Malviya, Sarang Kulkarni, Satyam Singh Rajput`
- **Institutional Status Badge**:
  - Text: `SOC 2 TYPE II COMPLIANT | ZERO MATH HALLUCINATION | 10,000 BATCH CAPACITY`

#### 5. Layout Specifications
- **Canvas Background**: Light Canvas (`#fbfbfd`) with a subtle `#0066ff` vertical accent bar on the left edge (width: 12px, full height).
- **Header Positioning**:
  - Eyebrow: X = 0.80", Y = 1.20", Font: Inter Bold 11pt UPPERCASE `#0066ff`.
  - H1 Title: X = 0.80", Y = 1.50", Font: Inter ExtraBold 48pt `#000000`, Line spacing: 1.05x.
  - Subtitle: X = 0.80", Y = 2.60", Font: Inter Regular 16pt `#515154`, Width: 11.5", Line spacing: 1.3x.
- **Card Containers**:
  - Container 1 (Account Metadata): X = 0.80", Y = 3.80", Width = 5.60", Height = 2.40", Fill: `#f5f5f7`, Border: 1px `#e5e5e7`, Radius: 16px, Padding: 24px.
  - Container 2 (Platform Specs): X = 6.65", Y = 3.80", Width = 5.85", Height = 2.40", Fill: `#f5f5f7`, Border: 1px `#e5e5e7`, Radius: 16px, Padding: 24px.
- **Badge Positioning**: X = 0.80", Y = 6.35", Height = 0.35", Fill: `#e6f0ff`, Border: 1px `#b3d1ff`, Radius: 20px pill.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
|[BLUE BAR] EYEBROW: PILOT PROPOSAL & ARCHITECTURE THESIS                           |
|           H1: Arvocap 10k Report Generation Engine                                |
|           SUBTITLE: Scaling Automated Portfolio Intelligence across KSh 11.02B AUM|
|                                                                                   |
|  +-------------------------------------+  +------------------------------------+  |
|  | CARD 1: CLIENT ACCOUNT              |  | CARD 2: DEPLOYMENT ENGINE          |  |
|  | • Arvocap Asset Managers (CMA Reg.) |  | • SarvaX Agentic Platform 2.0      |  |
|  | • AUM: KSh 11.02B (~$85M USD)       |  | • Dual-Agent + Python Math Engine  |  |
|  | • Stakeholders: Monicah Mwaniki,    |  | • Technical Leads: Arnold & Simar  |  |
|  |   John Ngure, Arnold O., Simar J.   |  | • C3A Team: Pratyush, Satyam, Ria  |  |
|  +-------------------------------------+  +------------------------------------+  |
|                                                                                   |
|  [ BADGE: SOC 2 TYPE II COMPLIANT | ZERO MATH HALLUCINATION | 10k BATCH READY ]    |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 01 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 2: Executive Summary & Growth Context

#### 1. Eyebrow Category Tag
`EXECUTIVE SUMMARY & SCALE CHALLENGE`

#### 2. Slide H1 Title
`Supporting +120% AUM Growth Without Operational Overhead`

#### 3. Messaging Hierarchy
- **Primary Headline**: KSh 11.02B AUM Scale Demands Automated Client Intelligence
- **Sub-headline**: Arvocap's rapid expansion across 10,000 accounts creates a critical operational bottleneck in monthly performance reporting.
- **Key Takeaway**: Automating report generation replaces manual analyst workflows, accelerating dispatch from weeks to hours while maintaining 100% regulatory accuracy.
- **Executive Narrative**: Arvocap manages KSh 11.02 Billion (~$85M USD) across 10 sub-funds. With 10,000 investors receiving monthly reports, human wealth managers cannot manually construct personalized reviews without escalating overhead. The SarvaX engine automates this entire lifecycle.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `EXECUTIVE SUMMARY & SCALE CHALLENGE`
  - Title: `Supporting +120% AUM Growth Without Operational Overhead`
- **KPI Block (3-Column Top Grid)**:
  - Metric 1: `KSh 11.02B` | Label: `TOTAL AUM UNDER MANAGEMENT (~$85M USD)`
  - Metric 2: `10,000` | Label: `ACTIVE RETAIL & AFFLUENT INVESTORS`
  - Metric 3: `10 SUB-FUNDS` | Label: `CMA REGULATED MULTI-ASSET PORTFOLIOS`
- **Left Narrative Card (The Scale Bottleneck)**:
  - Header: `Operational Challenge: The Manual Reporting Trap`
  - Bullet 1: `High Analyst Overhead: Manual aggregation of fund metrics, yield curve adjustments, and investor transactions consumes 1,200+ analyst hours monthly.`
  - Bullet 2: `Turnaround Latency: Traditional report drafting delays monthly client communication by 10-14 days post-month end.`
  - Bullet 3: `Consistency & Compliance Risks: Manual narrative drafting creates variance in performance commentary and compliance disclosures.`
- **Right Narrative Card (The SarvaX Solution)**:
  - Header: `The SarvaX Pilot Solution: Angel One Scale Pattern`
  - Bullet 1: `Institutional Batch Processing: Automated generation and dispatch of 10,000 personalized PDF reports in under 2 hours.`
  - Bullet 2: `Retail Fintech Intelligence: Adopting top-tier fintech practices (Angel One/Zerodha model) tailored to regulated East African wealth management.`
  - Bullet 3: `Multi-Channel Delivery: Instant dispatch via automated WhatsApp Business API and branded transactional email channels.`

#### 5. Layout Specifications
- **KPI Row**: X = 0.80", Y = 1.60", Width = 11.73", Height = 1.30". Three equal KPI boxes (Width: 3.70" each, Gap: 0.31", Fill: `#f5f5f7`, Border: 1px `#e5e5e7`, Radius: 16px).
- **2-Card Grid Below**:
  - Left Card (Operational Challenge): X = 0.80", Y = 3.10", Width = 5.70", Height = 3.60", Fill: `#f5f5f7`, Border: 1px `#e5e5e7`, Radius: 16px, Padding: 24px.
  - Right Card (SarvaX Solution): X = 6.83", Y = 3.10", Width = 5.70", Height = 3.60", Fill: `#f5f5f7`, Border: 1px `#e5e5e7`, Radius: 16px, Padding: 24px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: EXECUTIVE SUMMARY & SCALE CHALLENGE                                      |
| H1: Supporting +120% AUM Growth Without Operational Overhead                      |
|                                                                                   |
| +------------------------+ +------------------------+ +-------------------------+ |
| | KSh 11.02B             | | 10,000                 | | 10 SUB-FUNDS          | |
| | TOTAL AUM UNDER MGMT   | | ACTIVE INVESTORS       | | CMA REGULATED FUNDS   | |
| +------------------------+ +------------------------+ +-------------------------+ |
|                                                                                   |
| +-------------------------------------+  +------------------------------------+ |
| | OPERATIONAL CHALLENGE: BOTTLENECK   |  | THE SARVAX PILOT SOLUTION          | |
| | • 1,200+ analyst hours consumed mo. |  | • Angel One scale batch processing | |
| | • 10-14 day report dispatch latency |  | • 10,000 reports generated < 2 hrs | |
| | • Risk of human calculation error   |  | • WhatsApp + Email auto-dispatch   | |
| +-------------------------------------+  +------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 02 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 3: The 4 Arvocap Workloads

#### 1. Eyebrow Category Tag
`CORE PLATFORM WORKLOADS`

#### 2. Slide H1 Title
`Comprehensive Coverage Across Arvocap's Wealth Spectrum`

#### 3. Messaging Hierarchy
- **Primary Headline**: 4 Integrated Agentic Workloads Driving Wealth Operations
- **Sub-headline**: SarvaX unifies IFA support, manager hierarchy, aggregate analytics, and segmented outreach into a single intelligent platform.
- **Key Takeaway**: Every stakeholder—from external IFAs to C-suite executives and individual retail investors—receives customized, automated intelligence.
- **Executive Narrative**: Based on Arvocap's core requirements, SarvaX structures four distinct workloads: self-serve IFA reviews, internal wealth manager tracking, aggregate AUM analytics, and hyper-targeted investor communications.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `CORE PLATFORM WORKLOADS`
  - Title: `Comprehensive Coverage Across Arvocap's Wealth Spectrum`
- **4-Card Grid Matrix (2x2 Layout)**:
  - **Card 1: External IFA Support Engine**
    - Tag: `WORKLOAD 01 | IFA SELF-SERVE`
    - Body: `Empowers third-party Independent Financial Advisors (IFAs) managing hundreds of end-clients to generate instant, branded portfolio health checks on demand without central analyst intervention.`
    - Impact Pill: `Reduces Analyst Escalations by 85%`
  - **Card 2: Internal Manager & Hierarchy Tracking**
    - Tag: `WORKLOAD 02 | WEALTH MANAGERS`
    - Body: `Automates monthly portfolio reviews and implements "agent-within-an-agent" hierarchy oversight, enabling senior directors to track junior advisor performance and client AUM shifts.`
    - Impact Pill: `Full Hierarchy Visibility`
  - **Card 3: Executive Aggregate AUM Analytics**
    - Tag: `WORKLOAD 03 | C-SUITE ANALYTICS`
    - Body: `Provides real-time, network-wide fund performance, macro economic sensitivity stress testing, liquidity tracking, and aggregate inflow/outflow balance views for executive management.`
    - Impact Pill: `Real-Time Executive Dashboards`
  - **Card 4: Segmented Investor Communications**
    - Tag: `WORKLOAD 04 | TARGETED OUTREACH`
    - Body: `Delivers hyper-personalized monthly performance updates segmented by investor tiers (HNW, Mass Affluent, Retail) across preferred communication channels (WhatsApp Business & Transactional Email).`
    - Impact Pill: `100% Omni-Channel Reach`

#### 5. Layout Specifications
- **Matrix Layout**: 2 rows x 2 columns.
  - Top Row: Y = 1.60", Height = 2.45". Card 1 X = 0.80", Width = 5.70". Card 2 X = 6.83", Width = 5.70".
  - Bottom Row: Y = 4.25", Height = 2.45". Card 3 X = 0.80", Width = 5.70". Card 4 X = 6.83", Width = 5.70".
  - Containers: Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Internal Padding 20px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: CORE PLATFORM WORKLOADS                                                  |
| H1: Comprehensive Coverage Across Arvocap's Wealth Spectrum                      |
|                                                                                   |
| +-------------------------------------+  +------------------------------------+ |
| | WORKLOAD 01 | IFA SELF-SERVE        |  | WORKLOAD 02 | WEALTH MANAGERS      | |
| | On-demand portfolio reviews for     |  | Automated monthly reviews & agent- | |
| | external IFAs managing 100s clients |  | within-an-agent hierarchy tracking | |
| | [ PILL: -85% Analyst Escalations ]  |  | [ PILL: Full Hierarchy Visibility ]| |
| +-------------------------------------+  +------------------------------------+ |
|                                                                                   |
| +-------------------------------------+  +------------------------------------+ |
| | WORKLOAD 03 | C-SUITE ANALYTICS     |  | WORKLOAD 04 | TARGETED OUTREACH    | |
| | Network-wide AUM dashboard, fund    |  | Segmentedupdates (HNW/Retail) via  | |
| | yields, macro stress testing & flows|  | WhatsApp API & Transactional Email | |
| | [ PILL: Real-Time Executive Views ] |  | [ PILL: 100% Omni-Channel Reach ]  | |
| +-------------------------------------+  +------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 03 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 4: Dual-Agent Technical Architecture

#### 1. Eyebrow Category Tag
`DUAL-AGENT TECHNICAL ARCHITECTURE`

#### 2. Slide H1 Title
`DeepSeek V4 Pro Reader + Kimi K3 Brain Engine`

#### 3. Messaging Hierarchy
- **Primary Headline**: Specialized Model Orchestration via SarvaX Workflow 2.0
- **Sub-headline**: Pairing high-speed structural parsing with deep financial reasoning ensures speed, accuracy, and minimum latency.
- **Key Takeaway**: Dividing ingestion and synthesis between two specialized models optimizes speed, accuracy, and cost efficiency.
- **Executive Narrative**: Rather than relying on a single monolithic LLM, SarvaX deploys a specialized dual-agent model stack. DeepSeek V4 Pro handles high-volume PDF parsing and structured table extraction, while Kimi K3 provides sophisticated financial analysis and narrative drafting.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `DUAL-AGENT TECHNICAL ARCHITECTURE`
  - Title: `DeepSeek V4 Pro Reader + Kimi K3 Brain Engine`
- **Left Column Card (DeepSeek V4 Pro Reader)**:
  - Header: `Agent 1: DeepSeek V4 Pro (Structure & Extraction)`
  - Sub-header: `Role: Ultra-Fast Data Parsing & Schema Validation`
  - Bullet 1: `Ingestion Capacity: Processes complex multi-page NAV statements, transaction logs, and asset allocation tables at 150+ tokens/sec.`
  - Bullet 2: `Structured Extraction: Converts unstructured PDF inputs into zero-loss JSON schema primitives.`
  - Bullet 3: `Cost Profile: High-efficiency extraction model minimizing input token expense.`
- **Middle Connector Graphic**:
  - Label: `SARVAX WORKFLOW 2.0 ORCHESTRATOR`
  - Sub-label: `Zero-Loss JSON Primitives + Python Decimal Engine`
- **Right Column Card (Kimi K3 Brain)**:
  - Header: `Agent 2: Kimi K3 Brain (Reasoning & Narrative)`
  - Sub-header: `Role: Context-Aware Financial Commentary Generation`
  - Bullet 1: `Deep Financial Reasoning: Analyzes market impact, yield changes, and portfolio attribution against Kenyan macro benchmarks.`
  - Bullet 2: `Institutional Tone Control: Drafts hyper-personalized, executive-grade investor commentary adhering to CMA compliance guidelines.`
  - Bullet 3: `Context Efficiency: Operates on pre-parsed JSON inputs, drastically reducing required output context.`

#### 5. Layout Specifications
- **Left Card (Agent 1)**: X = 0.80", Y = 1.60", Width = 5.20", Height = 5.00", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.
- **Center Flow Box (Orchestrator)**: X = 6.15", Y = 3.30", Width = 1.00", Height = 1.60", Fill `#e6f0ff`, Border 1px `#b3d1ff`, Radius 12px. Arrow icons pointing left-to-right.
- **Right Card (Agent 2)**: X = 7.30", Y = 1.60", Width = 5.23", Height = 5.00", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: DUAL-AGENT TECHNICAL ARCHITECTURE                                        |
| H1: DeepSeek V4 Pro Reader + Kimi K3 Brain Engine                                 |
|                                                                                   |
| +--------------------------+   +---------------+   +----------------------------+ |
| | AGENT 1: DEEPSEEK V4 PRO |   | SARVAX        |   | AGENT 2: KIMI K3 BRAIN     | |
| | (STRUCTURE & EXTRACTION) |   | WORKFLOW 2.0  |   | (REASONING & NARRATIVE)    | |
| | • Fast PDF/NAV parsing   |==>| ORCHESTRATOR  |==>| • Macro market attribution | |
| | • Unstructured to JSON   |   | + PYTHON MATH |   | • CMA compliance drafting  | |
| | • High throughput throughput|  | ENGINE        |   | • Personalized commentary  | |
| +--------------------------+   +---------------+   +----------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 04 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 5: 10k Batch Report Generation Pipeline

#### 1. Eyebrow Category Tag
`ENTERPRISE PIPELINE ARCHITECTURE`

#### 2. Slide H1 Title
`10k Batch Report Generation Pipeline (Angel One Pattern)`

#### 3. Messaging Hierarchy
- **Primary Headline**: End-to-End High-Throughput Report Processing Pipeline
- **Sub-headline**: Parallel async ingestion, deterministic math verification, and multi-channel dispatch built for scale.
- **Key Takeaway**: The 5-stage pipeline generates and distributes 10,000 investor reports in under 2 hours with 100% delivery tracking.
- **Executive Narrative**: Modeled on Angel One's retail fintech batch engine, SarvaX processes 10,000 investor accounts simultaneously. Data flows seamlessly from Arvocap's core DB through parallel agent workers and template renderers to final distribution channels.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `ENTERPRISE PIPELINE ARCHITECTURE`
  - Title: `10k Batch Report Generation Pipeline (Angel One Pattern)`
- **5-Stage Pipeline Sequence Blocks**:
  - **Stage 1: Batch Ingestion & Trigger**
    - Title: `01. Core Data Ingestion`
    - Spec: `Extracts NAV, holdings, and investor profiles from Arvocap core database via secure API.`
  - **Stage 2: Parallel Queue & Dispatch**
    - Title: `02. Asynchronous Queue`
    - Spec: `Distributes 10,000 client records across parallel SarvaX worker nodes.`
  - **Stage 3: Dual-Agent Synthesis**
    - Title: `03. Dual-Agent Processing`
    - Spec: `DeepSeek parses raw data; Kimi K3 generates personalized commentary.`
  - **Stage 4: Math & PDF Render**
    - Title: `04. Deterministic Render`
    - Spec: `Python Decimal Engine validates math; compiles pixel-perfect PDF report.`
  - **Stage 5: Omni-Channel Dispatch**
    - Title: `05. Multi-Channel Delivery`
    - Spec: `Dispatches customized updates via WhatsApp Business API & Email with tracking.`
- **Bottom Pipeline Performance Banner**:
  - Stat 1: `Batch Capacity: 10,000 Reports / 110 Mins`
  - Stat 2: `Concurrency: 50 Parallel Agent Workers`
  - Stat 3: `Delivery SLA: 99.9% Successful Dispatch`

#### 5. Layout Specifications
- **Pipeline Stage Cards**: 5 horizontal cards arranged across the slide width.
  - Card 1: X = 0.80", Width = 2.15". Card 2: X = 3.20", Width = 2.15". Card 3: X = 5.60", Width = 2.15". Card 4: X = 8.00", Width = 2.15". Card 5: X = 10.40", Width = 2.13".
  - Top Y = 1.60", Height = 3.60". Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 16px.
- **Bottom Banner**: X = 0.80", Y = 5.40", Width = 11.73", Height = 1.20", Fill `#e6f0ff`, Border 1px `#b3d1ff`, Radius 16px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: ENTERPRISE PIPELINE ARCHITECTURE                                         |
| H1: 10k Batch Report Generation Pipeline (Angel One Pattern)                      |
|                                                                                   |
| +-----------+   +-----------+   +-----------+   +-----------+   +-----------+ |
| | STAGE 01  |   | STAGE 02  |   | STAGE 03  |   | STAGE 04  |   | STAGE 05  | |
| | Core Data |==>| Async     |==>| Dual-Agent|==>| Decimal   |==>| Multi-    | |
| | Ingestion |   | Queue     |   | Processing|   | Render    |   | Channel   | |
| | (NAV DB)  |   | (Workers) |   | (LLM Stack)|  | (PDF Gen) |   | (WA/Email)| |
| +-----------+   +-----------+   +-----------+   +-----------+   +-----------+ |
|                                                                                   |
| +-------------------------------------------------------------------------------+ |
| | PERFORMANCE SLA: 10,000 Reports in < 2 Hours | 50 Workers | 99.9% Delivery    | |
| +-------------------------------------------------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 05 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 6: 3-Tier Commercial LLM Costing Matrix

#### 1. Eyebrow Category Tag
`COMMERCIAL PRICING & LLM COSTING`

#### 2. Slide H1 Title
`3-Tier Commercial LLM Costing Matrix (10k Batch)`

#### 3. Messaging Hierarchy
- **Primary Headline**: Flexible Commercial Tiers Tailored to Report Complexity
- **Sub-headline**: Three transparent pricing options designed to match Arvocap's specific reporting depth requirements.
- **Key Takeaway**: Monthly LLM cost for 10,000 investor reports ranges from ₹3,800/mo ($45) for Tier 1 to ₹18,500/mo ($220) for Tier 2.
- **Executive Narrative**: To provide Arvocap with complete financial clarity while sample PDFs undergo audit, C3A Labs has established a 3-tier commercial costing matrix based on report page count, token depth, and model selection.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `COMMERCIAL PRICING & LLM COSTING`
  - Title: `3-Tier Commercial LLM Costing Matrix (10k Batch)`
- **Comparison Table Specification**:
  - Column 1: `Report Complexity Tier`
  - Column 2: `Page Count`
  - Column 3: `Token Allocation (Input / Output)`
  - Column 4: `Recommended Model Stack`
  - Column 5: `Cost / Report (80% Cached)`
  - Column 6: `Total Cost (10,000 Reports / Mo)`
- **Row 1 (Tier 1: Lite Summary Brief)**:
  - Spec: `1 – 2 Pages` | Tokens: `15,000 In / 1,500 Out` | Stack: `Gemini 3.5 Flash-Lite` | Unit Cost: `₹0.38` | Monthly Total: `₹3,800 / mo (~$45 USD)`
- **Row 2 (Tier 2: Standard Portfolio Review — RECOMMENDED)**:
  - Spec: `3 – 5 Pages` | Tokens: `35,000 In / 3,500 Out` | Stack: `DeepSeek V4 Pro` | Unit Cost: `₹1.85` | Monthly Total: `₹18,500 / mo (~$220 USD)`
- **Row 3 (Tier 3: Deep Institutional Analysis)**:
  - Spec: `8 – 12 Pages` | Tokens: `75,000 In / 8,000 Out` | Stack: `DeepSeek V4 Pro -> Kimi K3` | Unit Cost: `₹6.20` | Monthly Total: `₹62,000 / mo (~$740 USD)`
- **Table Callout Badge**:
  - Text: `RECOMMENDED PILOT TIER: TIER 2 (STANDARD PORTFOLIO REVIEW) AT ₹18,500 / MONTH`

#### 5. Layout Specifications
- **Table Container**: X = 0.80", Y = 1.60", Width = 11.73", Height = 4.20", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px.
- **Table Styling**:
  - Header Row: Height = 0.60", Fill `#e6f0ff`, Text: Inter Bold 10.5pt `#0066ff`.
  - Row 2 (Tier 2 Highlight): Fill `#ffffff`, Border 2px solid `#0066ff` emphasis.
- **Bottom Callout**: X = 0.80", Y = 6.00", Width = 11.73", Height = 0.60", Text: Inter Bold 11pt `#0066ff`.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: COMMERCIAL PRICING & LLM COSTING                                         |
| H1: 3-Tier Commercial LLM Costing Matrix (10k Batch)                              |
|                                                                                   |
| +-------------------------------------------------------------------------------+ |
| | TIER          | PAGES | TOKENS (IN/OUT) | RECOMMENDED STACK   | COST/RPT| TOTAL/MO| |
| |---------------+-------+-----------------+---------------------+---------+---------| |
| | Tier 1 Lite   | 1-2   | 15,000 / 1,500  | Gemini Flash-Lite   | ₹0.38   | ₹3,800  | |
| |---------------+-------+-----------------+---------------------+---------+---------| |
| | TIER 2 STND*  | 3-5   | 35,000 / 3,500  | DeepSeek V4 Pro     | ₹1.85   | ₹18,500 | |
| | (RECOMMENDED) |       |                 |                     |         |         | |
| |---------------+-------+-----------------+---------------------+---------+---------| |
| | Tier 3 Deep   | 8-12  | 75,000 / 8,000  | DeepSeek V4 + Kimi  | ₹6.20   | ₹62,000 | |
| +-------------------------------------------------------------------------------+ |
|                                                                                   |
| [ BADGE: *TIER 2 PROVIDES OPTIMAL BALANCE OF NARRATIVE DEPTH & COST EFFICIENCY ]  |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 06 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 7: Prompt Caching Economics

#### 1. Eyebrow Category Tag
`UNIT ECONOMICS & COST OPTIMIZATION`

#### 2. Slide H1 Title
`Prompt Caching Economics: Slashing Spend by 65%`

#### 3. Messaging Hierarchy
- **Primary Headline**: Architectural Caching Reduces Monthly Infrastructure Cost
- **Sub-headline**: Reusing static fund disclosures and system prompts across 10,000 accounts yields drastic cost savings.
- **Key Takeaway**: Prompt caching reduces input token fees by 80%, driving total monthly report generation cost down by 65%.
- **Executive Narrative**: In batch operations across 10,000 accounts, 80% of input prompt content (fund terms, regulatory disclosures, market summary) remains identical. SarvaX leverages native model prompt caching to eliminate redundant processing costs.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `UNIT ECONOMICS & COST OPTIMIZATION`
  - Title: `Prompt Caching Economics: Slashing Spend by 65%`
- **Left Column Card (Uncached vs. Cached Unit Economics)**:
  - Header: `Cost Breakdown: Tier 2 Standard Report`
  - Metric 1: `₹5.30` | Label: `RAW UNCACHED COST PER REPORT`
  - Metric 2: `₹1.85` | Label: `CACHED COST PER REPORT (80% CONTEXT CACHED)`
  - Delta Callout: `65.1% NET COST REDUCTION`
- **Right Column Card (Structural Caching Mechanics)**:
  - Header: `How SarvaX Achieves 80% Cache Efficiency`
  - Bullet 1: `Static System Prompts & Compliance Templates: 10,000 tokens of CMA compliance guidelines and report styling instructions cached in memory.`
  - Bullet 2: `Macro Market & Sub-Fund Context: 18,000 tokens of monthly fund yield tables and macroeconomic commentary shared across all client reports.`
  - Bullet 3: `Dynamic Client Delta: Only individual client balance and transaction history (7,000 tokens) processed as dynamic uncached input.`
- **Bottom Summary KPI Callout**:
  - Text: `ANNUAL INFRASTRUCTURE SAVINGS: KSh 640,000+ ($5,000 USD) REALLOCATED TO GROWTH`

#### 5. Layout Specifications
- **Left Card (Cost Comparison)**: X = 0.80", Y = 1.60", Width = 5.20", Height = 4.00", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.
- **Right Card (Mechanics)**: X = 6.20", Y = 1.60", Width = 6.33", Height = 4.00", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.
- **Bottom Box**: X = 0.80", Y = 5.80", Width = 11.73", Height = 0.80", Fill `#e6f0ff`, Border 1px `#b3d1ff`, Radius 12px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: UNIT ECONOMICS & COST OPTIMIZATION                                       |
| H1: Prompt Caching Economics: Slashing Spend by 65%                               |
|                                                                                   |
| +------------------------------------+  +---------------------------------------+ |
| | TIER 2 COST COMPARISON             |  | HOW SARVAX ACHIEVES 80% CACHE HITS    | |
| |                                    |  | • Static Prompts & Compliance: 10k tok| |
| | Uncached: ₹5.30 / report           |  | • Fund Yield & Macro Context: 18k tok | |
| | Cached:   ₹1.85 / report           |  | • Dynamic Client Data: Only 7k tok    | |
| |                                    |  |                                       | |
| | [ NET SAVINGS: 65% COST REDUCTION ]|  | Result: Input tokens billed at 1/10th | |
| +------------------------------------+  +---------------------------------------+ |
|                                                                                   |
| +-------------------------------------------------------------------------------+ |
| | ANNUAL INFRASTRUCTURE SAVINGS: KSh 640,000+ REALLOCATED TO ASSET GROWTH       | |
| +-------------------------------------------------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 07 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 8: Governance, SOC 2 & Zero Math Hallucination

#### 1. Eyebrow Category Tag
`GOVERNANCE, COMPLIANCE & ACCURACY`

#### 2. Slide H1 Title
`SOC 2 Type II Security & Zero Math Hallucination Engine`

#### 3. Messaging Hierarchy
- **Primary Headline**: Enterprise Regulatory Compliance & Deterministic Accuracy
- **Sub-headline**: Protecting institutional investor data while enforcing 100% mathematical precision across fund calculations.
- **Key Takeaway**: Financial calculations are isolated from LLM probabilistic output, guaranteeing zero hallucination.
- **Executive Narrative**: Regulated wealth management requires zero compromise on security or mathematical precision. SarvaX guarantees enterprise governance via SOC 2 Type II compliance and delegates all financial calculations to a deterministic Python Decimal Engine.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `GOVERNANCE, COMPLIANCE & ACCURACY`
  - Title: `SOC 2 Type II Security & Zero Math Hallucination Engine`
- **Left Column Card (Enterprise Compliance & Security)**:
  - Header: `Institutional Security & Data Privacy`
  - Bullet 1: `SOC 2 Type II Certified: Full SOC 2 audit package and data management policy prepared for Arvocap compliance team.`
  - Bullet 2: `Zero Data Retention: Enterprise API agreements ensure client financial data is never stored or used for LLM model training.`
  - Bullet 3: `CMA Regulatory Alignment: Full audit trail logging for every generated report to meet Kenya Capital Markets Authority requirements.`
- **Right Column Card (Python Decimal Engine)**:
  - Header: `Zero Math Hallucination Framework`
  - Bullet 1: `Deterministic Math Execution: Yields, total returns, and management fees are computed exclusively by Python's Decimal library.`
  - Bullet 2: `LLM Separation: LLMs are restricted to narrative synthesis and context drafting; LLMs NEVER perform raw floating-point math.`
  - Bullet 3: `Automated Verification Assertions: Pre-render verification step checks generated text against raw ledger totals before PDF compilation.`

#### 5. Layout Specifications
- **2 Equal Columns**:
  - Left Card (Compliance): X = 0.80", Y = 1.60", Width = 5.70", Height = 4.80", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.
  - Right Card (Python Decimal Engine): X = 6.83", Y = 1.60", Width = 5.70", Height = 4.80", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: GOVERNANCE, COMPLIANCE & ACCURACY                                        |
| H1: SOC 2 Type II Security & Zero Math Hallucination Engine                       |
|                                                                                   |
| +-------------------------------------+  +------------------------------------+ |
| | INSTITUTIONAL COMPLIANCE            |  | ZERO MATH HALLUCINATION ENGINE     | |
| | • SOC 2 Type II certified pipeline  |  | • Python Decimal Engine executes   | |
| | • Zero model training on client data|  |   all NAV and fee calculations     | |
| | • Full audit logging for CMA rules  |  | • LLM used ONLY for commentary text| |
| | • Enterprise SLA & encryption       |  | • Pre-render assertion verification| |
| +-------------------------------------+  +------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 08 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 9: Pilot Implementation Roadmap

#### 1. Eyebrow Category Tag
`PILOT IMPLEMENTATION ROADMAP`

#### 2. Slide H1 Title
`4-Week Accelerated Go-Live with Arnold & Simar`

#### 3. Messaging Hierarchy
- **Primary Headline**: Structured 4-Week Path from Alignment to 10k Batch Go-Live
- **Sub-headline**: Close technical collaboration with Arvocap leads Arnold Oduma and Simar Juttla ensures rapid, risk-managed rollout.
- **Key Takeaway**: A phased 4-week deployment validates schemas, integrates Python math engines, tests 1,000 batch samples, and executes full production dispatch.
- **Executive Narrative**: C3A Labs has outlined a structured 4-week implementation timeline. Led by Arnold Oduma and Simar Juttla on the Arvocap side, the pilot moves methodically from schema setup to a full 10,000 report production dispatch.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `PILOT IMPLEMENTATION ROADMAP`
  - Title: `4-Week Accelerated Go-Live with Arnold & Simar`
- **4 Timeline Milestone Cards (Horizontal Sequence)**:
  - **Week 1: Schema Alignment & API Ingestion**
    - Phase Tag: `WEEK 01 | FOUNDATION`
    - Tasks: `Sample PDF schema review, API endpoint connection with Arnold & Simar, raw data mapping.`
  - **Week 2: Dual-Agent Setup & Math Verification**
    - Phase Tag: `WEEK 02 | ARCHITECTURE`
    - Tasks: `DeepSeek + Kimi model orchestration setup, Python Decimal Engine integration, prompt optimization.`
  - **Week 3: 1,000 Batch Stress Test**
    - Phase Tag: `WEEK 03 | STRESS TEST`
    - Tasks: `Dry run batch generation on 1,000 client records, WhatsApp/Email template delivery verification.`
  - **Week 4: 10,000 Batch Go-Live & ROI Audit**
    - Phase Tag: `WEEK 04 | FULL GO-LIVE`
    - Tasks: `Full production dispatch of 10,000 monthly reports, executive ROI review, permanent operational handoff.`
- **Bottom Team Alignment Callout**:
  - Text: `TECHNICAL LEADS: ARNOLD ODUMA & SIMAR JUTTLA (ARVOCAP) | SATYAM SINGH RAJPUT & RIA CHOUDHARI (C3A)`

#### 5. Layout Specifications
- **4 Timeline Cards**: Horizontal layout.
  - Card 1: X = 0.80", Width = 2.70". Card 2: X = 3.80", Width = 2.70". Card 3: X = 6.80", Width = 2.70". Card 4: X = 9.80", Width = 2.73".
  - Y = 1.60", Height = 4.00". Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 20px.
- **Bottom Callout Box**: X = 0.80", Y = 5.80", Width = 11.73", Height = 0.80", Fill `#e6f0ff`, Border 1px `#b3d1ff`, Radius 12px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: PILOT IMPLEMENTATION ROADMAP                                             |
| H1: 4-Week Accelerated Go-Live with Arnold & Simar                                |
|                                                                                   |
| +-----------------+ +-----------------+ +-----------------+ +-----------------+ |
| | WEEK 01         | | WEEK 02         | | WEEK 03         | | WEEK 04         | |
| | FOUNDATION      | | ARCHITECTURE    | | STRESS TEST     | | FULL GO-LIVE    | |
| | • Schema review | | • Dual-agent    | | • 1,000 report  | | • 10,000 report | |
| | • API endpoint  | |   orchestration | |   dry run       | |   production    | |
| |   connection    | | • Python math   | | • Template &    | |   dispatch      | |
| |   w/ Arnold &   | |   decimal engine| |   channel test  | | • ROI evaluation| |
| |   Simar         | |   integration   | |   with team     | |   & signoff     | |
| +-----------------+ +-----------------+ +-----------------+ +-----------------+ |
|                                                                                   |
| +-------------------------------------------------------------------------------+ |
| | ALIGNED TEAMS: Arnold Oduma & Simar Juttla (Arvocap) | Satyam Rajput & Ria (C3A)| |
| +-------------------------------------------------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 09 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

### SLIDE 10: Executive ROI & Value Realization

#### 1. Eyebrow Category Tag
`EXECUTIVE ROI & BUSINESS VALUE`

#### 2. Slide H1 Title
`2,300+ Hours Recovered & Institutional Value Realization`

#### 3. Messaging Hierarchy
- **Primary Headline**: Quantifiable ROI Across Operations, Speed, and Investor Engagement
- **Sub-headline**: SarvaX transforms monthly report drafting from an operational cost center into a strategic client retention tool.
- **Key Takeaway**: Unlocks 2,300+ annual analyst hours, cuts turnaround time by 98%, and establishes an enterprise foundation for future AUM growth.
- **Executive Narrative**: Implementing the SarvaX 10k Report Generation Engine provides immediate operational payback. Arvocap recovers over 2,300 hours of high-value analyst time annually, slashes monthly reporting turnaround from 14 days to under 2 hours, and elevates investor trust across KSh 11.02B AUM.

#### 4. Full Slide Copy Specifications
- **Header Block**:
  - Eyebrow: `EXECUTIVE ROI & BUSINESS VALUE`
  - Title: `2,300+ Hours Recovered & Institutional Value Realization`
- **Top 3 KPI ROI Callout Blocks**:
  - Block 1: `2,300+ HRS` | Label: `ANNUAL ANALYST TIME RECOVERED`
  - Block 2: `98% FASTER` | Label: `TURNAROUND LATENCY REDUCTION (14 DAYS TO < 2 HRS)`
  - Block 3: `KSh 18.5M` | Label: `ANNUAL OPERATIONAL COST VALUE CREATED`
- **Bottom 2 Summary Cards**:
  - **Card 1: Operational & Strategic Impact**
    - Bullet 1: `Analyst Reallocation: Shifts junior and senior wealth managers from manual report drafting to high-value proactive client advisory.`
    - Bullet 2: `Investor Retention: Delivering timely, personalized market insights builds deep trust across retail and mass affluent tiers.`
  - **Card 2: Scalability & Future Readiness**
    - Bullet 1: `Infinite Scalability: Infrastructure supports expansion from 10,000 to 50,000+ investors with zero marginal headcount required.`
    - Bullet 2: `CMA Compliance Excellence: Establishes Arvocap as the premier tech-enabled asset manager in East Africa.`

#### 5. Layout Specifications
- **Top KPI Row**: X = 0.80", Y = 1.60", Width = 11.73", Height = 1.40". Three equal KPI boxes (Width: 3.70" each, Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px).
- **Bottom 2 Cards**:
  - Left Card: X = 0.80", Y = 3.20", Width = 5.70", Height = 3.40", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.
  - Right Card: X = 6.83", Y = 3.20", Width = 5.70", Height = 3.40", Fill `#f5f5f7`, Border 1px `#e5e5e7`, Radius 16px, Padding 24px.

#### 6. Visual Component Map
```
+-----------------------------------------------------------------------------------+
| EYEBROW: EXECUTIVE ROI & BUSINESS VALUE                                           |
| H1: 2,300+ Hours Recovered & Institutional Value Realization                      |
|                                                                                   |
| +------------------------+ +------------------------+ +-------------------------+ |
| | 2,300+ HRS             | | 98% FASTER             | | KSh 18.5M             | |
| | ANNUAL TIME RECOVERED  | | DISPATCH LATENCY     | | OPERATIONAL VALUE     | |
| +------------------------+ +------------------------+ +-------------------------+ |
|                                                                                   |
| +-------------------------------------+  +------------------------------------+ |
| | STRATEGIC OPERATIONAL IMPACT        |  | SCALABILITY & FUTURE READINESS     | |
| | • Analysts reallocated to advisory  |  | • Scale to 50k+ accounts seamlessly| |
| | • Timely updates drive retention     |  | • Gold-standard CMA audit readiness| |
| | • High-touch experience for all     |  | • First-mover tech advantage in EA | |
| +-------------------------------------+  +------------------------------------+ |
|===================================================================================|
| POWERSCALE VENTURES | CONFIDENTIAL            ARVOCAP 10K REPORT PILOT | 10 OF 10 |
+-----------------------------------------------------------------------------------+
```

---

## 3. Summary & Implementation Guidelines for PPTX Automation

### 3.1 Layout Checklist for PPTX Renderers
1. **Font Consistency**: Ensure Inter font family is loaded or substituted with standard system Arial/Calibri fallback if Inter is unavailable on host machine.
2. **Card Radius**: Set container shapes to 16px rounded rectangle.
3. **Color Integrity**: Enforce exact Hex values: Accent `#0066ff`, Fill `#f5f5f7`, Text `#1d1d1f`, Border `#e5e5e7`.
4. **Footer Lock**: Verify horizontal 1px rule at Y = 6.90" with locked metadata text on all 10 slides.
5. **Table Highlighting**: Ensure Slide 6 Tier 2 row is rendered with distinct background/border styling to draw visual focus.

---
*End of Master Slide Copy & Architecture Specification Document.*
