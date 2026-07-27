const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');

console.log("Initializing PowerScale PPTX Generator for Arvocap 10k Report Pilot...");

const pres = new pptxgen();

// Set widescreen 16:9 layout (13.33 x 7.5 inches)
pres.layout = 'LAYOUT_16x9';
pres.title = 'SARVAX x Arvocap Asset Managers — 10k Report Pilot Proposal';
pres.author = 'Satyam Singh Rajput (C3A Labs)';

// PowerScale Design System Colors
const COLOR = {
  BLUE: '0066FF',
  BLACK: '000000',
  WHITE: 'FFFFFF',
  CANVAS: 'FBFBFD',
  CARD_BG: 'F5F5F7',
  CARD_DARK: '1D1D1F',
  CARD_BORDER: 'E5E5E7',
  TEXT_BODY: '1D1D1F',
  TEXT_SECONDARY: '515154',
  TEXT_MUTED: '86868B',
  BADGE_BG: 'EBF3FF',
  GREEN: '30D158',
  YELLOW: 'FFD60A'
};

const FONT = {
  TITLE: 'Inter',
  BODY: 'Inter'
};

// Helper: Add Standard Slide Header
function addSlideHeader(slide, categoryText, titleText) {
  // Category Eyebrow Tag
  slide.addText(categoryText.toUpperCase(), {
    x: 0.8,
    y: 0.5,
    w: 11.7,
    h: 0.3,
    fontFace: FONT.TITLE,
    fontSize: 11,
    bold: true,
    color: COLOR.BLUE,
    charSpacing: 1.5,
    margin: 0
  });

  // Slide Main Title (H1)
  slide.addText(titleText, {
    x: 0.8,
    y: 0.82,
    w: 11.7,
    h: 0.6,
    fontFace: FONT.TITLE,
    fontSize: 26,
    bold: true,
    color: COLOR.BLACK,
    margin: 0
  });
}

// Helper: Add Standard Footer Rule & Disclaimer
function addSlideFooter(slide, slideNumStr) {
  // 1px Horizontal Divider Line
  slide.addShape(pres.ShapeType.line, {
    x: 0.8,
    y: 7.0,
    w: 11.733,
    h: 0,
    line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  // Footer Text Left
  slide.addText("SARVAX BY C3A LABS | CONFIDENTIAL INSTITUTIONAL PILOT PROPOSAL", {
    x: 0.8,
    y: 7.05,
    w: 9.0,
    h: 0.3,
    fontFace: FONT.BODY,
    fontSize: 8.5,
    color: COLOR.TEXT_MUTED,
    charSpacing: 1.0,
    margin: 0
  });

  // Slide Number Right
  slide.addText(slideNumStr, {
    x: 11.533,
    y: 7.05,
    w: 1.0,
    h: 0.3,
    fontFace: FONT.BODY,
    fontSize: 8.5,
    bold: true,
    color: COLOR.TEXT_MUTED,
    align: 'right',
    margin: 0
  });
}

// =========================================================================
// SLIDE 1: COVER SLIDE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  // Top Brand Header Block
  slide.addText("C3A LABS  ×  SARVAX PLATFORM", {
    x: 0.8,
    y: 1.2,
    w: 11.7,
    h: 0.35,
    fontFace: FONT.TITLE,
    fontSize: 12,
    bold: true,
    color: COLOR.BLUE,
    charSpacing: 2.0
  });

  // Main Cover Title
  slide.addText("Regulated Wealth AI &\n10k Monthly Report Engine", {
    x: 0.8,
    y: 1.7,
    w: 11.7,
    h: 1.8,
    fontFace: FONT.TITLE,
    fontSize: 44,
    bold: true,
    color: COLOR.BLACK,
    lineSpacing: 50
  });

  // Subtitle / Executive Summary Line
  slide.addText("Commercial Pilot Proposal & Token Economics Architecture for Arvocap Asset Managers (Nairobi, Kenya)", {
    x: 0.8,
    y: 3.7,
    w: 10.5,
    h: 0.6,
    fontFace: FONT.BODY,
    fontSize: 16,
    color: COLOR.TEXT_SECONDARY
  });

  // Info Card Container (Bottom)
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8,
    y: 4.7,
    w: 11.733,
    h: 1.8,
    rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG },
    line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  // Info Card Content
  slide.addText("PROPOSAL STAKEHOLDERS & PILOT SPECIFICATIONS", {
    x: 1.1,
    y: 4.95,
    w: 11.0,
    h: 0.3,
    fontFace: FONT.TITLE,
    fontSize: 10,
    bold: true,
    color: COLOR.BLUE,
    charSpacing: 1.5
  });

  slide.addText("CLIENT LEADERSHIP: Monicah Mwaniki (Co-Founder & CEO), John Ngure, Arnold Oduma (Tech Lead), Simar Juttla (Tech Lead)\nC3A LABS TEAM: Satyam Singh Rajput (Product & R&D), Pratyush Malviya (Sales Manager), Sarang Kulkarni, Ria Choudhari\nCORE SCOPE: 10,000 Monthly Client Portfolio Reports · Dual-Agent Architecture · Python Decimal Math Oracle · SOC 2 Security", {
    x: 1.1,
    y: 5.3,
    w: 11.1,
    h: 1.0,
    fontFace: FONT.BODY,
    fontSize: 11.5,
    color: COLOR.TEXT_BODY,
    lineSpacing: 18
  });

  addSlideFooter(slide, "01");
}

// =========================================================================
// SLIDE 2: THE GROWTH CHALLENGE & OPERATIONAL BOTTLENECK
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "EXECUTIVE CONTEXT", "Scaling KSh 11.02B AUM Without Middle-Office Drag");

  // Top 3 Stat Cards Grid
  const cardW = 3.644;
  const cardH = 2.2;
  const cardY = 1.6;

  // Stat Card 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("KSh 11.02B", {
    x: 1.0, y: cardY + 0.25, w: cardW - 0.4, h: 0.6,
    fontFace: FONT.TITLE, fontSize: 34, bold: true, color: COLOR.BLUE
  });
  slide.addText("Total AUM Across 10 Sub-Funds", {
    x: 1.0, y: cardY + 0.9, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 13, bold: true, color: COLOR.BLACK
  });
  slide.addText("120% AUM growth in trailing 6 months (up from KSh 4.94B) driven by Almasi Fixed Income & Money Market funds.", {
    x: 1.0, y: cardY + 1.25, w: cardW - 0.4, h: 0.8,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY
  });

  // Stat Card 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("10,000+", {
    x: 5.044, y: cardY + 0.25, w: cardW - 0.4, h: 0.6,
    fontFace: FONT.TITLE, fontSize: 34, bold: true, color: COLOR.BLUE
  });
  slide.addText("Active Investor Base", {
    x: 5.044, y: cardY + 0.9, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 13, bold: true, color: COLOR.BLACK
  });
  slide.addText("Mass-market, emerging affluent, and diaspora investors onboarding via Google Play app (10k+ downloads) and IFAs.", {
    x: 5.044, y: cardY + 1.25, w: cardW - 0.4, h: 0.8,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY
  });

  // Stat Card 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("48 Hours", {
    x: 9.088, y: cardY + 0.25, w: cardW - 0.4, h: 0.6,
    fontFace: FONT.TITLE, fontSize: 34, bold: true, color: COLOR.BLACK
  });
  slide.addText("Manual Portfolio Review Bottleneck", {
    x: 9.088, y: cardY + 0.9, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 13, bold: true, color: COLOR.BLACK
  });
  slide.addText("IFAs managing 100s of clients must manually request central office analysts for portfolio review reports before client meetings.", {
    x: 9.088, y: cardY + 1.25, w: cardW - 0.4, h: 0.8,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY
  });

  // Bottom Operational Insight Banner Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 4.1, w: 11.733, h: 2.5, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("THE OPERATIONAL CHALLENGE: FRONTIER GROWTH VS. MIDDLE-OFFICE CAPACITY", {
    x: 1.1, y: 4.35, w: 11.1, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });

  slide.addText("1. Multi-Channel Fragmentation: Client queries arrive across WhatsApp, Email, App, and phone. Manual note-taking causes dropped context.\n2. Wealth Manager Admin Burden: Advisors spend 9+ hours/week on portfolio reviews, report assembly, and CRM updates instead of client acquisition.\n3. The Scalability Dilemma: Scaling to 20,000 clients with traditional manual analysis would require tripling middle-office analyst headcount.", {
    x: 1.1, y: 4.75, w: 11.1, h: 1.6,
    fontFace: FONT.BODY, fontSize: 12, color: COLOR.TEXT_BODY, lineSpacing: 22
  });

  addSlideFooter(slide, "02");
}

// =========================================================================
// SLIDE 3: THE 4 ARVOCAP WORKLOADS
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "WORKLOAD ARCHITECTURE", "4 Bounded AI Workloads for Arvocap Asset Managers");

  const cardW = 5.666;
  const cardH = 2.3;

  // Workload 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("UC-1: IFA Operational Support & Portfolio Reviews", {
    x: 1.1, y: 1.85, w: cardW - 0.6, h: 0.35,
    fontFace: FONT.TITLE, fontSize: 14, bold: true, color: COLOR.BLUE
  });
  slide.addText("Eliminates the manual analyst bottleneck. IFAs managing 100s of clients trigger instant, automated portfolio review reports for upcoming client meetings based on quarterly/bi-annual review schedules.", {
    x: 1.1, y: 2.25, w: cardW - 0.6, h: 1.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Workload 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("UC-2: Internal Wealth Manager Hierarchy & Reporting", {
    x: 7.166, y: 1.85, w: cardW - 0.6, h: 0.35,
    fontFace: FONT.TITLE, fontSize: 14, bold: true, color: COLOR.BLUE
  });
  slide.addText("Supports 'Agent-within-an-Agent' hierarchy. Senior Managers monitor sub-agent AUM growth, track report delivery consistency, and automatically disseminate market/yield updates to client portfolios.", {
    x: 7.166, y: 2.25, w: cardW - 0.6, h: 1.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Workload 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 4.2, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("UC-3: Aggregate Network AUM & Product Analytics", {
    x: 1.1, y: 4.45, w: cardW - 0.6, h: 0.35,
    fontFace: FONT.TITLE, fontSize: 14, bold: true, color: COLOR.BLUE
  });
  slide.addText("Gives Monicah and John executive visibility across the entire network. Slices quarterly AUM growth by agent, product (Almasi Fixed Income, Money Market, Tech), and region (Nairobi, Jo'burg, London).", {
    x: 1.1, y: 4.85, w: cardW - 0.6, h: 1.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Workload 4
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 4.2, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("UC-4: Segmented Outreach & Targeted Communications", {
    x: 7.166, y: 4.45, w: cardW - 0.6, h: 0.35,
    fontFace: FONT.TITLE, fontSize: 14, bold: true, color: COLOR.BLUE
  });
  slide.addText("Replaces blanket messaging with precise segmentation. Filters clients by Investment Tier (HNW, Mass Affluent, Retail), location, and product interest to dispatch tailored webinar invites & fund alerts.", {
    x: 7.166, y: 4.85, w: cardW - 0.6, h: 1.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  addSlideFooter(slide, "03");
}

// =========================================================================
// SLIDE 4: DUAL-AGENT TECHNICAL ARCHITECTURE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "SYSTEM ARCHITECTURE", "Reader-Brain Paradigm & Workflow 2.0 DAG Engine");

  const colW = 3.644;
  const colH = 5.0;

  // Column 1: Reader Agent
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("READER TIER", {
    x: 1.0, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("DeepSeek V4 Pro", {
    x: 1.0, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("High-Speed Context Ingestion", {
    x: 1.0, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Ingests 50-page fund statements, CRM logs, and holdings data.\n• $0.435 / 1M Input Rate ($0.0036 Cached Rate).\n• 99.17% Prompt Caching discount for static system schemas.\n• Rapid structured data extraction without high token spend.", {
    x: 1.0, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Column 2: Brain Agent
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("BRAIN TIER", {
    x: 5.044, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Kimi K3", {
    x: 5.044, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("SOTA TAU Banking Reasoning", {
    x: 5.044, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Global #1 SOTA on TAU Banking evaluation benchmark (0.3340 score).\n• Synthesizes complex portfolio allocation, tax-lot logic, and risk commentary.\n• Executes multi-turn financial reasoning over extracted Reader data.\n• Ensures institutional advisory quality for executive reports.", {
    x: 5.044, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Column 3: Workflow 2.0 Engine
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("GOVERNANCE RAIL", {
    x: 9.088, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Workflows 2.0 DAG", {
    x: 9.088, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("Deterministic Execution Engine", {
    x: 9.088, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Python Decimal exact math oracle eliminates model calculation hallucinations.\n• Mandatory await_approval gates require human advisor click-to-confirm.\n• Direct MCP tool integration (BFF system, CRM, WhatsApp).\n• Immutable audit trail logged for CMA regulatory inspection.", {
    x: 9.088, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  addSlideFooter(slide, "04");
}

// =========================================================================
// SLIDE 5: 10k BATCH REPORT DISPATCH ENGINE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "COMMUNICATION ENGINE", "10,000 Automated Monthly Client Communication Engine");

  const rowH = 1.5;

  // Row 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("01  PRE-BATCH PROMPT WARM-UP PIPELINE", {
    x: 1.1, y: 1.8, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Executes a 30-minute prefill warming cycle before month-end batch execution. Ingests static fund schemas, CMA disclosures, and report templates to lock in an 80%+ Prompt Caching SLA across all 10,000 client runs.", {
    x: 1.1, y: 2.15, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Row 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 3.3, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("02  DISTRIBUTED BATCH QUEUEING & RATE LIMIT PROTECTION", {
    x: 1.1, y: 3.5, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Manages API rate limits (60 RPM caps) via asynchronous worker pools. Parallel sub-agents process client batches in background chunks with automatic retry backoff, completing 10,000 runs within 3.5 hours without system overload.", {
    x: 1.1, y: 3.85, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Row 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 5.0, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("03  MULTI-CHANNEL DISPATCH & PDF GENERATION", {
    x: 1.1, y: 5.2, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Compiles structured JSON outputs into high-fidelity PDF statements. Dispatches personalized portfolio performance reports via Arvocap Client App, Email, and Periskope WhatsApp API (matching retail fintech patterns).", {
    x: 1.1, y: 5.55, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  addSlideFooter(slide, "05");
}

// =========================================================================
// SLIDE 6: 3-TIER COMMERCIAL LLM PRICING MATRIX
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "COMMERCIAL PRICING", "3-Tier Report Complexity Matrix for 10k Monthly Reports");

  const cardW = 3.644;
  const cardH = 5.0;

  // Tier 1 Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("TIER 1: LITE BRIEF", {
    x: 1.0, y: 1.85, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.2
  });
  slide.addText("1 – 2 Pages", {
    x: 1.0, y: 2.15, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK
  });
  slide.addText("Gemini 3.5 Flash-Lite", {
    x: 1.0, y: 2.55, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE
  });
  slide.addText("• Token Footprint: 15k in / 1.5k out\n• Scope: Monthly summary statement & NAV update.\n• Cost per Report: ₹0.38 (80% Cached)\n• 10k Monthly Total: ₹3,800 / month\n• Monthly USD Equivalent: ~$39 / month", {
    x: 1.0, y: 2.95, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Tier 2 Card (RECOMMENDED)
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("TIER 2: STANDARD REVIEW", {
    x: 5.044, y: 1.85, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("3 – 5 Pages", {
    x: 5.044, y: 2.15, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK
  });
  slide.addText("DeepSeek V4 Pro Reader", {
    x: 5.044, y: 2.55, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE
  });
  slide.addText("• Token Footprint: 35k in / 3.5k out\n• Scope: Detailed holding breakdown & yield notes.\n• Cost per Report: ₹1.85 (80% Cached)\n• 10k Monthly Total: ₹18,500 / month\n• Monthly USD Equivalent: ~$191 / month", {
    x: 5.044, y: 2.95, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Tier 3 Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("TIER 3: INSTITUTIONAL", {
    x: 9.088, y: 1.85, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.2
  });
  slide.addText("8 – 12 Pages", {
    x: 9.088, y: 2.15, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK
  });
  slide.addText("DeepSeek V4 → Kimi K3", {
    x: 9.088, y: 2.55, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE
  });
  slide.addText("• Token Footprint: 75k in / 8.0k out\n• Scope: Comprehensive portfolio & tax analysis.\n• Cost per Report: ₹6.20 (80% Cached)\n• 10k Monthly Total: ₹62,000 / month\n• Monthly USD Equivalent: ~$642 / month", {
    x: 9.088, y: 2.95, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  addSlideFooter(slide, "06");
}

// =========================================================================
// SLIDE 7: ARCHITECTURAL EFFICIENCY & PROMPT CACHING ECONOMICS
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "COST OPTIMIZATION", "65% Capital Recovery via Prefill Prompt Caching");

  const cardW = 5.666;
  const cardH = 4.8;

  // Uncached Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("UNCACHED STANDARD RATE", {
    x: 1.1, y: 1.85, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.2
  });
  slide.addText("₹17.96 / Report", {
    x: 1.1, y: 2.2, w: cardW - 0.6, h: 0.5,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.BLACK
  });
  slide.addText("10k Monthly Total: ₹1,79,600 / mo ($1,860/mo)", {
    x: 1.1, y: 2.75, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 12, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Full token pricing charged on every single report run.\n• Input token volume re-processed 10,000 times from scratch.\n• Higher API spend due to repeated system prompts & schemas.", {
    x: 1.1, y: 3.2, w: cardW - 0.6, h: 2.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 22
  });

  // Cached Card (HIGHLIGHT)
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("WITH 80% PROMPT CACHING (SARVAX OPTIMIZED)", {
    x: 7.166, y: 1.85, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("₹6.20 / Report", {
    x: 7.166, y: 2.2, w: cardW - 0.6, h: 0.5,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.GREEN
  });
  slide.addText("10k Monthly Total: ₹62,000 / mo ($642/mo)", {
    x: 7.166, y: 2.75, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 12, bold: true, color: COLOR.BLUE
  });
  slide.addText("• 65.5% Spend Reduction: Saves ₹1,17,600/mo ($1,218/mo).\n• Static fund schemas & system prompts cached in GPU VRAM.\n• DeepSeek 99.17% / Gemini 75% prefill caching discounts applied.\n• Guarantees predictable, low-cost execution at enterprise scale.", {
    x: 7.166, y: 3.2, w: cardW - 0.6, h: 2.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 22
  });

  addSlideFooter(slide, "07");
}

// =========================================================================
// SLIDE 8: GOVERNANCE, SOC 2 & ZERO MATH HALLUCINATION
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "GOVERNANCE & SECURITY", "Zero Math Hallucination & SOC 2 Type II Security");

  const colW = 3.644;
  const colH = 5.0;

  // Card 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("PRECISION ENGINE", {
    x: 1.0, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Python Decimal Oracle", {
    x: 1.0, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("100% Deterministic Math", {
    x: 1.0, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Language models NEVER perform financial calculations.\n• All NAVs, yields, and portfolio returns are computed by Python Decimal.\n• Eliminates floating-point rounding errors and math hallucinations.\n• Models only format and synthesize the verified numeric outputs.", {
    x: 1.0, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Card 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("SECURITY PACKAGE", {
    x: 5.044, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("SOC 2 Type II Compliance", {
    x: 5.044, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("Sovereign Tenant Isolation", {
    x: 5.044, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Zero Data Retention (ZDR) agreements with model providers.\n• Compliant with Kenya Data Protection Act 2019 (KDPA).\n• Isolated tenant databases & encrypted client record storage.\n• Complete SOC 2 Type II audit report provided to Arnold & Simar.", {
    x: 5.044, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  // Card 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: 1.6, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("HUMAN CONTROL", {
    x: 9.088, y: 1.85, w: colW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("await_approval Gates", {
    x: 9.088, y: 2.15, w: colW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 20, bold: true, color: COLOR.BLACK
  });
  slide.addText("Human Advisor Sign-Off", {
    x: 9.088, y: 2.55, w: colW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• Material client communications hit an await_approval gate.\n• Named wealth advisors must accept, edit, or reject drafts.\n• Preserves advisor authority in CMA-regulated workflows.\n• Immutable audit logging for regulatory compliance reviews.", {
    x: 9.088, y: 2.95, w: colW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20
  });

  addSlideFooter(slide, "08");
}

// =========================================================================
// SLIDE 9: PILOT IMPLEMENTATION ROADMAP
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "PILOT ROADMAP", "4-Week Go-Live Plan for Arnold, Simar & C3A Engineering");

  const cardW = 2.708;
  const cardH = 5.0;

  // Week 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("WEEK 1", {
    x: 0.95, y: 1.85, w: cardW - 0.3, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Schema Mapping", {
    x: 0.95, y: 2.15, w: cardW - 0.3, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK
  });
  slide.addText("• Review sample Arvocap report PDFs.\n• Configure BFF API data endpoints.\n• Establish encrypted tenant isolation.", {
    x: 0.95, y: 2.7, w: cardW - 0.3, h: 3.6,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Week 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 3.808, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("WEEK 2", {
    x: 3.958, y: 1.85, w: cardW - 0.3, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Agent Calibration", {
    x: 3.958, y: 2.15, w: cardW - 0.3, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK
  });
  slide.addText("• Fine-tune DeepSeek V4 Pro extraction prompts.\n• Calibrate Kimi K3 for Arvocap fund rules.\n• Connect Python Decimal math oracle.", {
    x: 3.958, y: 2.7, w: cardW - 0.3, h: 3.6,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Week 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.816, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("WEEK 3", {
    x: 6.966, y: 1.85, w: cardW - 0.3, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("100-Report Batch", {
    x: 6.966, y: 2.15, w: cardW - 0.3, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK
  });
  slide.addText("• Execute test batch of 100 client reports.\n• Verify PDF layout fidelity & math exactness.\n• Audit 80% prompt caching SLA.", {
    x: 6.966, y: 2.7, w: cardW - 0.3, h: 3.6,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  // Week 4
  slide.addShape(pres.ShapeType.roundRect, {
    x: 9.824, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("WEEK 4", {
    x: 9.974, y: 1.85, w: cardW - 0.3, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("10k Go-Live", {
    x: 9.974, y: 2.15, w: cardW - 0.3, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK
  });
  slide.addText("• Executive prototype review with Monicah & John.\n• Activate 10,000 monthly report dispatch.\n• Transition to production SLA monitoring.", {
    x: 9.974, y: 2.7, w: cardW - 0.3, h: 3.6,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 18
  });

  addSlideFooter(slide, "09");
}

// =========================================================================
// SLIDE 10: EXECUTIVE ROI & COMMERCIAL ACTION ITEMS
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "EXECUTIVE SUMMARY", "2,300+ Analyst Hours Recovered at <1% Staff Cost");

  const cardW = 5.666;
  const cardH = 4.8;

  // Left Card: ROI Metrics
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("QUANTIFIED ROI FOR ARVOCAP", {
    x: 1.1, y: 1.85, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("2,340 Hours / Year", {
    x: 1.1, y: 2.2, w: cardW - 0.6, h: 0.5,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.BLACK
  });
  slide.addText("Recovered Across Wealth Advisors & Operations", {
    x: 1.1, y: 2.75, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 12, bold: true, color: COLOR.TEXT_SECONDARY
  });
  slide.addText("• 98% Turnaround Time Reduction: Slashes review generation from 48 hours down to <10 seconds.\n• Less Than 1% Analyst Cost: 10k reports executed at ₹62,000/mo ($642/mo) vs. hiring 3+ additional middle-office analysts.\n• 100% Client Coverage: Guarantees every single active investor receives a personalized, audit-safe monthly statement.", {
    x: 1.1, y: 3.2, w: cardW - 0.6, h: 2.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 22
  });

  // Right Card: Next Steps
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 1.6, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("RECOMMENDED ACTION ITEMS FOR TODAY'S CALL", {
    x: 7.166, y: 1.85, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2
  });
  slide.addText("Pilot Action Plan", {
    x: 7.166, y: 2.2, w: cardW - 0.6, h: 0.5,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.GREEN
  });
  slide.addText("Next Steps for Monicah, John, Arnold & Simar", {
    x: 7.166, y: 2.75, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 12, bold: true, color: COLOR.BLUE
  });
  slide.addText("1. Confirm Target Complexity Tier (Select Tier 1, Tier 2, or Tier 3 for 10k report dispatch).\n2. Share Sample Report PDF (Allow C3A engineering to lock in exact token bounds).\n3. Authorize 4-Week Pilot Scope (Sign off on SOC 2 security & data management policy).\n4. Schedule Technical Onboarding with Arnold Oduma & Simar Juttla.", {
    x: 7.166, y: 3.2, w: cardW - 0.6, h: 2.8,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 22
  });

  addSlideFooter(slide, "10");
}

// Save Presentation
const outputPath = path.join(__dirname, 'Arvocap_10k_Report_Pilot_Deck.pptx');
pres.writeFile({ fileName: outputPath })
  .then(fileName => {
    console.log(`\n✅ Presentation successfully created at: ${fileName}`);
  })
  .catch(err => {
    console.error("❌ Error writing presentation:", err);
  });
