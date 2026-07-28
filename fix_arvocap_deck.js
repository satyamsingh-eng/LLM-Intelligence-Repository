const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');

console.log("Rebuilding Arvocap Deck: Updating tier page ranges (1-3, 3-6, 7-12) while preserving all pricing and layout...");

const pres = new pptxgen();

// Enforce LAYOUT_WIDE canvas (13.333 x 7.500 inches)
pres.layout = 'LAYOUT_WIDE';
pres.title = 'SARVAX x Arvocap — 22-Model Frontier Comparison & 10k Report Guide';
pres.author = 'Satyam Singh Rajput (C3A Labs)';

const LOGO_PATH = path.join(__dirname, 'assets/sarvax_logo.png');

// PowerScale Design Tokens (Apple-Inspired Bold Palette)
const COLOR = {
  BLUE: '0066FF',        // Primary Electric Blue Accent
  BLACK: '000000',       // Headline Black
  WHITE: 'FFFFFF',       // Card Fill / White Text
  CANVAS: 'FBFBFD',      // Apple Off-White Canvas Background
  CARD_BG: 'F5F5F7',     // Light Gray Card Background
  CARD_DARK: '1D1D1F',   // Dark Accent Card / Table Header Background
  CARD_BORDER: 'E5E5E7', // 1px Card Outline / Divider Rule
  TEXT_BODY: '1D1D1F',   // Primary Body Copy
  TEXT_SECONDARY: '515154', // Subtitles & Secondary Descriptions
  TEXT_MUTED: '86868B',  // Footers & Muted Labels
  GREEN: '30D158',       // Accent Green for Positive Financial Value
  BADGE_BG: 'EBF3FF'     // Light Blue Tint for Pill Badges
};

const FONT = {
  TITLE: 'Inter',
  BODY: 'Inter'
};

// Helper: Add Standard Slide Header with Status Pill Badge
function addSlideHeader(slide, categoryText, titleText) {
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 0.38, w: 4.8, h: 0.30, rectRadius: 0.15,
    fill: { color: COLOR.BADGE_BG }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText(`●  ${categoryText.toUpperCase()}`, {
    x: 0.9, y: 0.41, w: 4.6, h: 0.24,
    fontFace: FONT.TITLE, fontSize: 9.5, bold: true, color: COLOR.BLUE,
    charSpacing: 1.2, margin: 0
  });

  slide.addText(titleText, {
    x: 0.8, y: 0.75, w: 11.733, h: 0.55,
    fontFace: FONT.TITLE, fontSize: 23, bold: true, color: COLOR.BLACK,
    margin: 0
  });
}

// Helper: Add Footer with Narrative Bridge
function addSlideFooter(slide, slideNumStr, transitionBridge) {
  if (transitionBridge) {
    slide.addText(`NEXT NARRATIVE STEP: ${transitionBridge}`, {
      x: 0.8, y: 6.60, w: 11.733, h: 0.25,
      fontFace: FONT.BODY, fontSize: 8.5, bold: true, color: COLOR.BLUE,
      margin: 0
    });
  }

  slide.addShape(pres.ShapeType.line, {
    x: 0.8, y: 6.90, w: 11.733, h: 0,
    line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("SARVAX BY C3A LABS | 22-MODEL COMPARISON & COMMERCIAL SPECIFICATION", {
    x: 0.8, y: 6.95, w: 9.0, h: 0.3,
    fontFace: FONT.BODY, fontSize: 8, color: COLOR.TEXT_MUTED,
    charSpacing: 1.0, margin: 0
  });

  slide.addText(slideNumStr, {
    x: 11.533, y: 6.95, w: 1.0, h: 0.3,
    fontFace: FONT.BODY, fontSize: 8, bold: true, color: COLOR.TEXT_MUTED,
    align: 'right', margin: 0
  });
}

// =========================================================================
// SLIDE 1: COVER SLIDE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 0.5, w: 5.2, h: 0.32, rectRadius: 0.16,
    fill: { color: COLOR.BADGE_BG }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("●  EXECUTION_ENGINE: ONLINE  |  10k REPORT SUITE", {
    x: 0.9, y: 0.54, w: 5.0, h: 0.24,
    fontFace: FONT.TITLE, fontSize: 9.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });

  if (fs.existsSync(LOGO_PATH)) {
    slide.addImage({ path: LOGO_PATH, x: 9.5, y: 0.45, w: 3.0, h: 0.9 });
  }

  slide.addText([
    { text: "AI THAT ", options: { bold: true, color: COLOR.BLACK } },
    { text: "EXECUTES.", options: { bold: true, color: COLOR.BLUE } }
  ], {
    x: 0.8, y: 1.1, w: 11.733, h: 0.8,
    fontFace: FONT.TITLE, fontSize: 38, margin: 0
  });

  slide.addText("22 Frontier AI Model Guide & 10,000 Monthly Report Costing", {
    x: 0.8, y: 1.95, w: 11.733, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK, margin: 0
  });

  slide.addText("Complete Rate Cards, Model Superpowers & Realistic Managed Costing for Arvocap Asset Managers", {
    x: 0.8, y: 2.45, w: 11.733, h: 0.4,
    fontFace: FONT.BODY, fontSize: 13, color: COLOR.TEXT_SECONDARY, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 3.1, w: 11.733, h: 3.3, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("EXECUTIVE BRIEF FOR BOARD & TECHNICAL LEADERSHIP", {
    x: 1.1, y: 3.35, w: 11.133, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 10.5, bold: true, color: COLOR.BLUE, charSpacing: 1.5, margin: 0
  });

  slide.addText("ARVOCAP LEADERSHIP: Monicah Mwaniki (Co-Founder & CEO), John Ngure, Arnold Oduma (Tech Lead), Simar Juttla (Tech Lead)\nC3A LABS TEAM: Satyam Singh Rajput (Product & Systems Lead), Pratyush Malviya (Sales Manager)\nEXECUTIVE SUMMARY: Establishing report complexity tiers, evaluating 22 frontier AI models side-by-side (External Direct vs SARVAX Managed), and proving how Gemini OCR Ingestion + DeepSeek Text + Kimi K3 Brain delivers 10,000 monthly reports at $950/mo. Delivery via Email & WhatsApp API.", {
    x: 1.1, y: 3.75, w: 11.133, h: 2.4,
    fontFace: FONT.BODY, fontSize: 11.5, color: COLOR.TEXT_BODY, lineSpacing: 22, margin: 0
  });

  addSlideFooter(slide, "01", "To scale AUM from KSh 11.02B to 20B+, we face a monthly client communication bottleneck.");
}

// =========================================================================
// SLIDE 2: THE BUSINESS CHALLENGE (UPDATED 3-6 PAGE BENCHMARK)
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "EXECUTIVE BRIEF", "Sending 10,000 Personalised Client Reports Every Month");

  const cardW = 3.644;
  const cardH = 2.1;
  const cardY = 1.40;

  // Stat Card 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("10,000 Clients", {
    x: 1.0, y: cardY + 0.18, w: cardW - 0.4, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("Complete Investor Coverage", {
    x: 1.0, y: cardY + 0.68, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12.5, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Every investor across Money Market, Almasi Fixed Income, and Equity funds receives a clear monthly update.", {
    x: 1.0, y: cardY + 1.02, w: cardW - 0.4, h: 0.9,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY, lineSpacing: 15, margin: 0
  });

  // Stat Card 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("< 2 Minutes", {
    x: 5.044, y: cardY + 0.18, w: cardW - 0.4, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("Multi-Page PDF Generation", {
    x: 5.044, y: cardY + 0.68, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12.5, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Replaces 48-hour manual analyst delays. Completes full PDF OCR, reasoning, and rendering in under 2 minutes per report.", {
    x: 5.044, y: cardY + 1.02, w: cardW - 0.4, h: 0.9,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY, lineSpacing: 15, margin: 0
  });

  // Stat Card 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: cardY, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("Fixed Budget", {
    x: 9.088, y: cardY + 0.18, w: cardW - 0.4, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Zero Surprise Pricing", {
    x: 9.088, y: cardY + 0.68, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 12.5, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Predictable $950/mo flat rate. Fully managed end-to-end report generation, quality assurance, and automated multi-channel delivery.", {
    x: 9.088, y: cardY + 1.02, w: cardW - 0.4, h: 0.9,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_SECONDARY, lineSpacing: 15, margin: 0
  });

  // Operational Insight Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 3.65, w: 11.733, h: 2.6, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("THE COMMERCIAL STEP: ESTABLISHING REPORT BENCHMARKS BEFORE MODEL SELECTION", {
    x: 1.1, y: 3.85, w: 11.133, h: 0.28,
    fontFace: FONT.TITLE, fontSize: 10.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });

  slide.addText("1. Page Count Drives Token Volume: A 1–3 page summary uses ~15,000 tokens, while a 3–6 page review uses ~35,000 tokens.\n2. Why We Anchor on Tier 2 (Standard Review): Without exact sample PDFs, we establish Tier 2 (3–6 Pages @ $950/mo) as our baseline benchmark.\n3. Direct Email & WhatsApp Dispatch: Gemini Flash provides native OCR vision for scanned statements, with automatic delivery via Email & WhatsApp.", {
    x: 1.1, y: 4.20, w: 11.133, h: 1.5,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  // Footnote callout
  slide.addText("* Benchmark Footnote: Assumes an average workload of 35k input tokens and 3.5k output tokens per report (350M input / 35M output tokens across 10,000 monthly reports).", {
    x: 1.1, y: 5.85, w: 11.133, h: 0.3,
    fontFace: FONT.BODY, fontSize: 8.5, italic: true, color: COLOR.TEXT_MUTED, margin: 0
  });

  addSlideFooter(slide, "02", "Before evaluating AI models, we define the 3 Report Complexity Tiers.");
}

// =========================================================================
// SLIDE 3: LOCKED COMMERCIAL PRICING TIERS (UPDATED PAGE RANGES: 1-3, 3-6, 7-12)
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "PRICING OPTIONS", "3 Commercial Tiers for 10,000 Monthly Reports (Managed Package)");

  const cardW = 3.644;
  const cardH = 4.9;

  // Tier 1 Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("TIER 1: LITE BRIEF", {
    x: 1.0, y: 1.68, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.2, margin: 0
  });
  slide.addText("1 – 3 Pages", {
    x: 1.0, y: 1.95, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Short Monthly Summary", {
    x: 1.0, y: 2.38, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("• Powered by Gemini 3.5 Flash-Lite (Fast OCR).\n• Brief NAV & balance update statement.\n• Volume: 15k input / 1.5k output per report (150M in / 15M out for 10k reports).\n• Cost per Report: $0.035 (~4.5 KSh / ₹3.38)\n• 10k Monthly Total: $350 / month\n• Local Currency: ~45,100 KSh/mo (₹33.8k)", {
    x: 1.0, y: 2.75, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 10, color: COLOR.TEXT_BODY, lineSpacing: 19, margin: 0
  });

  // Tier 2 Card (LOCKED BENCHMARK $950/MO)
  slide.addShape(pres.ShapeType.roundRect, {
    x: 4.844, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("TIER 2: STANDARD REVIEW (RECOMMENDED)", {
    x: 5.044, y: 1.68, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("3 – 6 Pages", {
    x: 5.044, y: 1.95, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Detailed Portfolio Breakdown", {
    x: 5.044, y: 2.38, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("• Gemini OCR + DeepSeek Text + Kimi Brain.\n• Full holding list, yield notes & market updates.\n• Volume: 35k input / 3.5k output per report (350M in / 35M out for 10k reports).\n• Cost per Report: $0.095 (~12.2 KSh / ₹9.17)\n• 10k Monthly Total: $950 / month\n• Local Currency: ~122,500 KSh/mo (₹91,700)", {
    x: 5.044, y: 2.75, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 10, color: COLOR.TEXT_BODY, lineSpacing: 19, margin: 0
  });

  // Tier 3 Card
  slide.addShape(pres.ShapeType.roundRect, {
    x: 8.888, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("TIER 3: INSTITUTIONAL", {
    x: 9.088, y: 1.68, w: cardW - 0.4, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.2, margin: 0
  });
  slide.addText("7 – 12 Pages", {
    x: 9.088, y: 1.95, w: cardW - 0.4, h: 0.4,
    fontFace: FONT.TITLE, fontSize: 22, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Deep Institutional Analysis", {
    x: 9.088, y: 2.38, w: cardW - 0.4, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("• Gemini OCR + DeepSeek Text + Kimi K3 Brain.\n• Comprehensive asset allocation & tax breakdown.\n• Volume: 75k input / 8.0k output per report (750M in / 80M out for 10k reports).\n• Cost per Report: $0.195 (~25.1 KSh / ₹18.80)\n• 10k Monthly Total: $1,950 / month\n• Local Currency: ~251,500 KSh/mo (₹1.88 Lakhs)", {
    x: 9.088, y: 2.75, w: cardW - 0.4, h: 3.4,
    fontFace: FONT.BODY, fontSize: 10, color: COLOR.TEXT_BODY, lineSpacing: 19, margin: 0
  });

  addSlideFooter(slide, "03", "Let's inspect the visual structure of a Standard 3-6 Page Client Report.");
}

// =========================================================================
// SLIDE 4: REPORT WIREFRAME (3-6 PAGES)
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "REPORT TEMPLATE", "Anatomy of a Standard 3-6 Page Client Portfolio Report");

  const colW = 2.22;
  const colH = 4.9;

  // Page 1
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("PAGE 1 (OCR)", { x: 0.95, y: 1.68, w: colW - 0.3, h: 0.22, fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.0 });
  slide.addText("Portfolio Overview", { x: 0.95, y: 1.95, w: colW - 0.3, h: 0.45, fontFace: FONT.TITLE, fontSize: 15, bold: true, color: COLOR.BLACK });
  slide.addText("• Ingested via Gemini Flash OCR\n• Investor Name & Account ID\n• Total Portfolio Value (KSh)\n• Month-on-Month Growth (%)", { x: 0.95, y: 2.45, w: colW - 0.3, h: 3.6, fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20 });

  // Page 2
  slide.addShape(pres.ShapeType.roundRect, {
    x: 3.18, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("PAGE 2 (OCR)", { x: 3.33, y: 1.68, w: colW - 0.3, h: 0.22, fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.0 });
  slide.addText("Asset Holdings", { x: 3.33, y: 1.95, w: colW - 0.3, h: 0.45, fontFace: FONT.TITLE, fontSize: 15, bold: true, color: COLOR.BLACK });
  slide.addText("• Scanned Statement Parsing\n• Almasi Fixed Income Balance\n• Money Market Fund Balance\n• Asset Class Pie Chart Vision", { x: 3.33, y: 2.45, w: colW - 0.3, h: 3.6, fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20 });

  // Page 3
  slide.addShape(pres.ShapeType.roundRect, {
    x: 5.56, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("PAGE 3 (TEXT)", { x: 5.71, y: 1.68, w: colW - 0.3, h: 0.22, fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.0 });
  slide.addText("Yield & Returns", { x: 5.71, y: 1.95, w: colW - 0.3, h: 0.45, fontFace: FONT.TITLE, fontSize: 15, bold: true, color: COLOR.BLACK });
  slide.addText("• DeepSeek Heavy Text Lifting\n• Interest Yield Analysis\n• Benchmark Comparison\n• Distribution History", { x: 5.71, y: 2.45, w: colW - 0.3, h: 3.6, fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20 });

  // Page 4
  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.94, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("PAGE 4 (BRAIN)", { x: 8.09, y: 1.68, w: colW - 0.3, h: 0.22, fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.0 });
  slide.addText("Market Commentary", { x: 8.09, y: 1.95, w: colW - 0.3, h: 0.45, fontFace: FONT.TITLE, fontSize: 15, bold: true, color: COLOR.BLACK });
  slide.addText("• Kimi K3 Financial Logic\n• Kenyan Fixed Income Trends\n• Central Bank Rate Impacts\n• Risk & Outlook Brief", { x: 8.09, y: 2.45, w: colW - 0.3, h: 3.6, fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20 });

  // Page 5-6
  slide.addShape(pres.ShapeType.roundRect, {
    x: 10.32, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("PAGES 5–6 (CONTROL)", { x: 10.47, y: 1.68, w: colW - 0.3, h: 0.22, fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.0 });
  slide.addText("Advisor Actions", { x: 10.47, y: 1.95, w: colW - 0.3, h: 0.45, fontFace: FONT.TITLE, fontSize: 15, bold: true, color: COLOR.BLACK });
  slide.addText("• Rebalancing Suggestions\n• Recommended Next Steps\n• Assigned IFA Contact Details\n• Click-to-Approve Gate", { x: 10.47, y: 2.45, w: colW - 0.3, h: 3.6, fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20 });

  addSlideFooter(slide, "04", "Now let's compare 22 AI models side-by-side: Direct Uncached vs. SARVAX Managed Package.");
}

// =========================================================================
// SLIDE 5: 22 MODEL COMPARISON — PART 1
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "MODEL EVALUATION (1/3)", "High-Efficiency Context Readers (External Direct vs. SARVAX Package)");

  slide.addTable([
    [
      { text: "Model Name", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Role / Superpower", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Rates (In/Out per 1M)", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "External Direct 10k Cost", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Managed Package Price", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Savings", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } }
    ],
    [{ text: "DeepSeek V4 Pro", options: { bold: true } }, "★ Heavy Text Lifter ($0.0036 cached)", "$0.435 / $0.870", "$182.70 (~23.6k KSh)", { text: "$150.00 (~19.3k KSh)", options: { bold: true, color: COLOR.BLUE } }, { text: "17.9% ★ Text Lead", options: { bold: true, color: COLOR.GREEN } }],
    [{ text: "Gemini 3.5 Flash-Lite", options: { bold: true } }, "★ Primary OCR Reader (362 tps)", "$0.300 / $2.500", "$192.50 (~24.8k KSh)", { text: "$160.00 (~20.6k KSh)", options: { bold: true, color: COLOR.BLUE } }, { text: "16.9% ★ OCR Lead", options: { bold: true, color: COLOR.GREEN } }],
    ["Qwen 3.7 Plus", "Base Input Rate ($0.40) Table Extraction", "$0.400 / $1.600", "$196.00 (~25.3k KSh)", "$165.00 (~21.2k KSh)", "15.8%"],
    ["Cohere Command A", "Enterprise RAG & Source Citations", "$0.500 / $1.500", "$228.00 (~29.4k KSh)", "$190.00 (~24.5k KSh)", "16.7%"],
    ["Amazon Nova Pro", "AWS Bedrock Enterprise VPC Security", "$0.800 / $3.200", "$392.00 (~50.6k KSh)", "$310.00 (~40.0k KSh)", "20.9%"],
    ["Kimi K2.6", "Long Context Under $1.00 Input Rate", "$0.950 / $4.000", "$472.50 (~61.0k KSh)", "$370.00 (~47.7k KSh)", "21.7%"],
    ["GPT-5.6 Luna", "Sub-Second Low Latency Chat Copilot", "$1.000 / $6.000", "$560.00 (~72.2k KSh)", "$450.00 (~58.0k KSh)", "19.6%"]
  ], {
    x: 0.8, y: 1.45, w: 11.733, h: 4.8,
    fontFace: FONT.BODY, fontSize: 10,
    border: { pt: 1, color: COLOR.CARD_BORDER },
    align: 'center', valign: 'middle'
  });

  slide.addText("* Benchmark Volume Footnote: Calculated for Tier 2 Standard (35k input tokens + 3.5k output tokens per report = 350M input / 35M output tokens across 10,000 reports).", {
    x: 0.8, y: 6.32, w: 11.733, h: 0.25,
    fontFace: FONT.BODY, fontSize: 8, italic: true, color: COLOR.TEXT_MUTED, margin: 0
  });

  addSlideFooter(slide, "05", "Part 2 compares financial reasoning models and multimodal vision models.");
}

// =========================================================================
// SLIDE 6: 22 MODEL COMPARISON — PART 2
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "MODEL EVALUATION (2/3)", "Financial Reasoning & Vision Models (External Direct vs. SARVAX Package)");

  slide.addTable([
    [
      { text: "Model Name", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Role / Superpower", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Rates (In/Out per 1M)", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "External Direct 10k Cost", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Managed Package Price", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Savings", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } }
    ],
    [{ text: "Kimi K3 (Moonshot)", options: { bold: true } }, "★ #1 Global SOTA TAU Banking (0.3340)", "$3.000 / $15.000", "$1,575.00 (~203.2k KSh)", { text: "$950.00 (~122.5k KSh)", options: { bold: true, color: COLOR.BLUE } }, { text: "39.7% ★ Brain Lead", options: { bold: true, color: COLOR.GREEN } }],
    ["Gemini 3.5 Flash", "Fixed 258 Tokens/Page Scanned PDF Vision", "$1.500 / $9.000", "$840.00 (~108.4k KSh)", "$620.00 (~80.0k KSh)", "26.2%"],
    ["Gemini 3.6 Flash", "1M Native Context & OCR Speed", "$1.500 / $7.500", "$787.50 (~101.6k KSh)", "$550.00 (~70.9k KSh)", "30.2%"],
    ["Qwen 3.7 Max", "SOTA Multi-Sheet Excel Logic (0.3120 TAU)", "$2.500 / $7.500", "$1,137.50 (~146.7k KSh)", "$780.00 (~100.6k KSh)", "31.4%"],
    ["GLM-5.2", "Multi-Turn Dialogue Context Retention", "$1.400 / $4.400", "$644.00 (~83.1k KSh)", "$510.00 (~65.8k KSh)", "20.8%"],
    ["Grok 4.5 (xAI)", "Real-Time Market Search Integration", "$2.000 / $6.000", "$910.00 (~117.4k KSh)", "$690.00 (~89.0k KSh)", "24.2%"],
    ["Claude Sonnet 5", "Executive Writing Tone for UHNW Briefs", "$2.000 / $10.000", "$1,050.00 (~135.5k KSh)", "$750.00 (~96.7k KSh)", "28.6%"]
  ], {
    x: 0.8, y: 1.45, w: 11.733, h: 4.8,
    fontFace: FONT.BODY, fontSize: 10,
    border: { pt: 1, color: COLOR.CARD_BORDER },
    align: 'center', valign: 'middle'
  });

  slide.addText("* Benchmark Volume Footnote: Calculated for Tier 2 Standard (35k input tokens + 3.5k output tokens per report = 350M input / 35M output tokens across 10,000 reports).", {
    x: 0.8, y: 6.32, w: 11.733, h: 0.25,
    fontFace: FONT.BODY, fontSize: 8, italic: true, color: COLOR.TEXT_MUTED, margin: 0
  });

  addSlideFooter(slide, "06", "Part 3 compares heavy frontier flagship models.");
}

// =========================================================================
// SLIDE 7: 22 MODEL COMPARISON — PART 3
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "MODEL EVALUATION (3/3)", "Heavy Frontier & Enterprise Models (External Direct vs. SARVAX Package)");

  slide.addTable([
    [
      { text: "Model Name", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Role / Superpower", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "Rates (In/Out per 1M)", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "External Direct 10k Cost", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Managed Package Price", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } },
      { text: "SARVAX Savings", options: { bold: true, fill: COLOR.CARD_DARK, color: COLOR.WHITE } }
    ],
    ["Gemini 3.1 Pro Preview", "Deep Multimodal Code & Analysis", "$2.000 / $12.000", "$1,120.00 (~144.5k KSh)", "$820.00 (~105.8k KSh)", "26.8%"],
    ["GPT-5.4 (OpenAI)", "High Function-Calling Tool Reliability", "$2.500 / $15.000", "$1,400.00 (~180.6k KSh)", "$980.00 (~126.4k KSh)", "30.0%"],
    ["GPT-5.6 Terra", "High Concurrency Limits & Uptime SLA", "$2.500 / $15.000", "$1,400.00 (~180.6k KSh)", "$980.00 (~126.4k KSh)", "30.0%"],
    [{ text: "Claude Sonnet 4.6", options: { bold: true } }, "Flawless Document Formatting & Artifacts", "$3.000 / $15.000", "$1,575.00 (~203.2k KSh)", { text: "$980.00 (~126.4k KSh)", options: { bold: true, color: COLOR.BLUE } }, { text: "37.8%", options: { bold: true, color: COLOR.GREEN } }],
    ["Claude Opus 5", "Ultimate Frontier Reasoning Flagship", "$5.000 / $25.000", "$2,625.00 (~338.6k KSh)", "$1,750.00 (~225.8k KSh)", "33.3%"],
    ["GPT-5.5 (OpenAI)", "Heavy Frontier Code & Math Logic", "$5.000 / $30.000", "$2,800.00 (~361.2k KSh)", "$1,950.00 (~251.5k KSh)", "30.4%"],
    ["Claude Fable 5", "Specialized Long-Form Narrative Research", "$10.000 / $50.000", "$5,250.00 (~677.3k KSh)", "$3,500.00 (~451.5k KSh)", "33.3%"]
  ], {
    x: 0.8, y: 1.45, w: 11.733, h: 4.8,
    fontFace: FONT.BODY, fontSize: 10,
    border: { pt: 1, color: COLOR.CARD_BORDER },
    align: 'center', valign: 'middle'
  });

  slide.addText("* Benchmark Volume Footnote: Calculated for Tier 2 Standard (35k input tokens + 3.5k output tokens per report = 350M input / 35M output tokens across 10,000 reports).", {
    x: 0.8, y: 6.32, w: 11.733, h: 0.25,
    fontFace: FONT.BODY, fontSize: 8, italic: true, color: COLOR.TEXT_MUTED, margin: 0
  });

  addSlideFooter(slide, "07", "Rather than paying expensive standalone rates, SARVAX uses a Smart Multi-Model Cascade.");
}

// =========================================================================
// SLIDE 8: THE SMART MULTI-MODEL CASCADE ENGINE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "SMART AI ENGINE", "Smart Multi-Model Cascade: OCR Vision + Text Heavy Lifting");

  const colW = 2.708;
  const colH = 4.9;

  // Step 1: Gemini OCR
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("STEP 1: OCR VISION", {
    x: 0.95, y: 1.68, w: colW - 0.3, h: 0.22,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Gemini Flash (OCR)", {
    x: 0.95, y: 1.95, w: colW - 0.3, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Scanned PDF Vision Reader", {
    x: 0.95, y: 2.42, w: colW - 0.3, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });
  slide.addText("• Scans image PDFs, identity docs & charts.\n• Fixed 258 tokens per page.\n• Extracts structured text & numbers from scanned files.", {
    x: 0.95, y: 2.82, w: colW - 0.3, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  // Step 2: DeepSeek Text Engine
  slide.addShape(pres.ShapeType.roundRect, {
    x: 3.808, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("STEP 2: HEAVY TEXT LIFTING", {
    x: 3.958, y: 1.68, w: colW - 0.3, h: 0.22,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("DeepSeek V4 Pro", {
    x: 3.958, y: 1.95, w: colW - 0.3, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Text Context Ingestion", {
    x: 3.958, y: 2.42, w: colW - 0.3, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });
  slide.addText("• Ingests 50+ page CRM histories & fund disclosures.\n• 99.17% Caching discount ($0.0036/1M cached).\n• High-volume context processing at pennies.", {
    x: 3.958, y: 2.82, w: colW - 0.3, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  // Step 3: Kimi Brain
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.816, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("STEP 3: DEEP REASONING", {
    x: 6.966, y: 1.68, w: colW - 0.3, h: 0.22,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Kimi K3 Brain", {
    x: 6.966, y: 1.95, w: colW - 0.3, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("#1 SOTA Banking Reasoning", {
    x: 6.966, y: 2.42, w: colW - 0.3, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });
  slide.addText("• #1 TAU Banking benchmark leader (0.3340).\n• Writes clear, professional financial commentary.\n• Explains yield & market shifts clearly.", {
    x: 6.966, y: 2.82, w: colW - 0.3, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  // Step 4: Code Math Oracle & Advisor Control
  slide.addShape(pres.ShapeType.roundRect, {
    x: 9.824, y: 1.45, w: colW, h: colH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("STEP 4: EXACT MATH & CONTROL", {
    x: 9.974, y: 1.68, w: colW - 0.3, h: 0.22,
    fontFace: FONT.TITLE, fontSize: 10, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Exact Math Oracle", {
    x: 9.974, y: 1.95, w: colW - 0.3, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 18, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("100% Exact Math + Advisor Sign-Off", {
    x: 9.974, y: 2.42, w: colW - 0.3, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });
  slide.addText("• Python Decimal code handles 100% of NAVs & returns (Zero AI math error).\n• Human advisors review & approve drafts.\n• Full audit trail kept for internal records.", {
    x: 9.974, y: 2.82, w: colW - 0.3, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  addSlideFooter(slide, "08", "See how Smart Memory Caching slashes monthly API bills by another 65%.");
}

// =========================================================================
// SLIDE 9: ULTRA-PREMIUM BEAUTIFIED CACHING & PLATFORM ECONOMICS ($950/MO MATCH)
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "COST SAVINGS", "Smart Caching & Platform Economics: Direct Vendor vs. SARVAX Benchmark");

  const cardW = 5.666;
  const cardH = 4.9;

  // Left Card: Direct Standalone Vendor Uncached Cost
  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("DIRECT VENDOR UNCACHED RATE", {
    x: 1.1, y: 1.70, w: cardW - 0.6, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 9.5, bold: true, color: COLOR.TEXT_MUTED, charSpacing: 1.5, margin: 0
  });

  slide.addText("$1,575 / Month", {
    x: 1.1, y: 1.95, w: cardW - 0.6, h: 0.55,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.BLACK, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.1, y: 2.58, w: 4.2, h: 0.32, rectRadius: 0.06,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("~203,200 KSh / mo  ·  ₹1.52 Lakhs / mo", {
    x: 1.2, y: 2.62, w: 4.0, h: 0.25,
    fontFace: FONT.BODY, fontSize: 10, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });

  const rowY = 3.05;
  const itemH = 0.95;

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.1, y: rowY, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("Standalone Direct API Pricing", { x: 1.25, y: rowY + 0.12, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("$3.00/1M In ($0.105) + $15.00/1M Out ($0.0525) = $0.1575 / report.", { x: 1.25, y: rowY + 0.40, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_SECONDARY, margin: 0 });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.1, y: rowY + 1.1, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("Zero Ingestion Optimization", { x: 1.25, y: rowY + 1.22, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("Buying direct from vendor API charges full rate on every run.", { x: 1.25, y: rowY + 1.50, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_SECONDARY, margin: 0 });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.1, y: rowY + 2.2, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("10,000 Uncached Runs Total", { x: 1.25, y: rowY + 2.32, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("Assumes 350M input / 35M output tokens across 10,000 reports.", { x: 1.25, y: rowY + 2.60, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_SECONDARY, margin: 0 });


  // Right Card: SARVAX Managed Tier 2 Package ($950/mo)
  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 9.5, y: 1.65, w: 2.7, h: 0.3, rectRadius: 0.15,
    fill: { color: COLOR.BADGE_BG }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("39.7% CLIENT SAVINGS", {
    x: 9.5, y: 1.68, w: 2.7, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 9, bold: true, color: COLOR.BLUE, align: 'center', charSpacing: 1.0, margin: 0
  });

  slide.addText("SARVAX MANAGED TIER 2 PACKAGE", {
    x: 7.166, y: 1.70, w: 2.2, h: 0.25,
    fontFace: FONT.TITLE, fontSize: 9.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });

  slide.addText("$950 / Month", {
    x: 7.166, y: 1.95, w: cardW - 0.6, h: 0.55,
    fontFace: FONT.TITLE, fontSize: 32, bold: true, color: COLOR.GREEN, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.166, y: 2.58, w: 4.2, h: 0.32, rectRadius: 0.06,
    fill: { color: COLOR.BADGE_BG }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("~122,500 KSh / mo  ·  ₹91,700 / mo", {
    x: 7.266, y: 2.62, w: 4.0, h: 0.25,
    fontFace: FONT.BODY, fontSize: 10, bold: true, color: COLOR.BLUE, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.166, y: rowY, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("All-Inclusive Managed SaaS", { x: 7.316, y: rowY + 0.12, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("Fully managed report generation, quality checks, and investor distribution.", { x: 7.316, y: rowY + 0.40, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_BODY, lineSpacing: 14, margin: 0 });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.166, y: rowY + 1.1, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("Kimi K3 SOTA Banking Engine", { x: 7.316, y: rowY + 1.22, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("Includes #1 SOTA TAU Banking reasoning + Gemini OCR Vision reader.", { x: 7.316, y: rowY + 1.50, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_BODY, lineSpacing: 14, margin: 0 });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 7.166, y: rowY + 2.2, w: cardW - 0.6, h: itemH, rectRadius: 0.08,
    fill: { color: COLOR.WHITE }, line: { color: COLOR.BLUE, width: 1 }
  });
  slide.addText("Safe Flat-Rate Guarantee", { x: 7.316, y: rowY + 2.32, w: cardW - 0.9, h: 0.25, fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLACK, margin: 0 });
  slide.addText("Saves $625/mo vs direct vendor. Capped flat rate guarantees complete budget predictability.", { x: 7.316, y: rowY + 2.60, w: cardW - 0.9, h: 0.45, fontFace: FONT.BODY, fontSize: 9.5, color: COLOR.TEXT_BODY, lineSpacing: 14, margin: 0 });

  addSlideFooter(slide, "09", "How batch queueing ensures month-end reports dispatch reliably.");
}

// =========================================================================
// SLIDE 10: BATCH DISPATCH & ENCRYPTED PRIVACY
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "BATCH DISPATCH & PRIVACY", "Automated Monthly Dispatch & Encrypted Data Isolation");

  const rowH = 1.55;

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("01  AUTOMATED MONTH-END QUEUEING", {
    x: 1.1, y: 1.65, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Runs quietly in the background at month-end. System processes all 10,000 client reports in under 3.5 hours without requiring manual intervention from operations or IT.", {
    x: 1.1, y: 2.0, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 3.15, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("02  PRIMARY EMAIL & WHATSAPP API DISPATCH", {
    x: 1.1, y: 3.35, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Dispatches PDF reports directly to investor email inboxes and WhatsApp API messages. Zero integration dependencies on mobile app development.", {
    x: 1.1, y: 3.7, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 4.85, w: 11.733, h: rowH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("03  ENCRYPTED DATA PRIVACY & ZERO MODEL TRAINING", {
    x: 1.1, y: 5.05, w: 11.0, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11.5, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Strict Zero Data Retention agreements with LLM providers. Client financial data is encrypted in dedicated isolated storage and NEVER trained on by public AI models.", {
    x: 1.1, y: 5.4, w: 11.1, h: 0.8,
    fontFace: FONT.BODY, fontSize: 11, color: COLOR.TEXT_BODY, lineSpacing: 18, margin: 0
  });

  addSlideFooter(slide, "10", "The bottom-line financial ROI and recommended action items for today's call.");
}

// =========================================================================
// SLIDE 11: EXECUTIVE ROI & PILOT ACTION PLAN ($950/MO PACKAGE)
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  addSlideHeader(slide, "EXECUTIVE ROI & DECISION", "2,300+ Analyst Hours Recovered at <1% Cost & Pilot Plan");

  const cardW = 5.666;
  const cardH = 4.9;

  slide.addShape(pres.ShapeType.roundRect, {
    x: 0.8, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });
  slide.addText("QUANTIFIED FINANCIAL ROI", {
    x: 1.1, y: 1.68, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("2,340 Hours / Year", {
    x: 1.1, y: 2.0, w: cardW - 0.6, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLACK, margin: 0
  });
  slide.addText("Recovered Across Wealth Advisors & Operations", {
    x: 1.1, y: 2.5, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11.5, bold: true, color: COLOR.TEXT_SECONDARY, margin: 0
  });
  slide.addText("• Manual Alternative: Hiring 3 middle-office analysts = ~$45,000/yr (~5.8M KSh/yr).\n• SARVAX Standard Tier 2 Cost: ~$11,400 / year (~1.47M KSh/yr / $950/mo).\n• Direct Staffing Savings: >74.7% savings vs traditional analyst staffing.\n• 100% Investor Coverage: Guarantees every single client receives a statement.", {
    x: 1.1, y: 2.88, w: cardW - 0.6, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 6.866, y: 1.45, w: cardW, h: cardH, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.BLUE, width: 2 }
  });
  slide.addText("RECOMMENDED PACKAGE & NEXT STEPS FOR CALL", {
    x: 7.166, y: 1.68, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.TITLE, fontSize: 11, bold: true, color: COLOR.BLUE, charSpacing: 1.2, margin: 0
  });
  slide.addText("Tier 2: Standard Package (3–6 Pages)", {
    x: 7.166, y: 2.0, w: cardW - 0.6, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 24, bold: true, color: COLOR.GREEN, margin: 0
  });
  slide.addText("~$950 / Mo (~122,500 KSh / ₹91,700/mo) for 10k Reports", {
    x: 7.166, y: 2.5, w: cardW - 0.6, h: 0.3,
    fontFace: FONT.BODY, fontSize: 11.5, bold: true, color: COLOR.BLUE, margin: 0
  });
  slide.addText("1. Confirm Tier Selection: Select Tier 1 ($350/mo), Tier 2 ($950/mo), or Tier 3 ($1,950/mo).\n2. Share 1 Sample Report PDF: Allows C3A engineering to lock exact template bounds.\n3. Run 100-Report Free Test Batch: Verify Gemini Flash OCR & Email/WhatsApp dispatch.\n4. Kickoff Technical Setup: Connect BFF API endpoints with Arnold & Simar.", {
    x: 7.166, y: 2.88, w: cardW - 0.6, h: 3.3,
    fontFace: FONT.BODY, fontSize: 10.5, color: COLOR.TEXT_BODY, lineSpacing: 20, margin: 0
  });

  addSlideFooter(slide, "11", "Let's review C3aLabs platform overview and leadership contact details.");
}

// =========================================================================
// SLIDE 12: TAILORED C3ALABS CLIENT CLOSING SLIDE
// =========================================================================
{
  const slide = pres.addSlide();
  slide.background = { color: COLOR.CANVAS };

  if (fs.existsSync(LOGO_PATH)) {
    slide.addImage({ path: LOGO_PATH, x: 5.0, y: 0.45, w: 3.333, h: 1.0 });
  }

  slide.addText("C3aLabs, Inc.  ×  Arvocap Asset Managers", {
    x: 0.8, y: 1.55, w: 11.733, h: 0.5,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLACK, align: 'center', margin: 0
  });

  slide.addText("Autonomous Execution & Communication Engine for Wealth Advisory", {
    x: 0.8, y: 2.08, w: 11.733, h: 0.35,
    fontFace: FONT.BODY, fontSize: 14, color: COLOR.BLUE, align: 'center', margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.5, y: 2.55, w: 10.333, h: 2.7, rectRadius: 0.12,
    fill: { color: COLOR.CARD_BG }, line: { color: COLOR.CARD_BORDER, width: 1 }
  });

  slide.addText("SarvaX.ai", {
    x: 1.8, y: 2.78, w: 9.733, h: 0.45,
    fontFace: FONT.TITLE, fontSize: 28, bold: true, color: COLOR.BLACK, align: 'center', margin: 0
  });

  slide.addText("Agentic AI Platform for Regulated Wealth & Asset Management", {
    x: 1.8, y: 3.28, w: 9.733, h: 0.3,
    fontFace: FONT.BODY, fontSize: 12.5, bold: true, color: COLOR.TEXT_SECONDARY, align: 'center', margin: 0
  });

  slide.addText("Sai Casula — Founder & CEO\nsaicasula@c3alabs.com  ·  c3alabs.com  ·  New York, NY", {
    x: 1.8, y: 3.68, w: 9.733, h: 0.6,
    fontFace: FONT.BODY, fontSize: 11.5, bold: true, color: COLOR.BLACK, align: 'center', lineSpacing: 18, margin: 0
  });

  slide.addText("C3A Project Contacts: Satyam Singh Rajput (Product Lead) | Pratyush Malviya (Sales Manager)", {
    x: 1.8, y: 4.40, w: 9.733, h: 0.35,
    fontFace: FONT.BODY, fontSize: 10, color: COLOR.BLUE, align: 'center', margin: 0
  });

  slide.addShape(pres.ShapeType.roundRect, {
    x: 1.5, y: 5.4, w: 10.333, h: 0.9, rectRadius: 0.08,
    fill: { color: COLOR.CARD_DARK }
  });

  slide.addText("\"AI won't replace financial advisors. But advisors empowered by AI will serve 10x more investors with higher trust.\"", {
    x: 1.8, y: 5.55, w: 9.733, h: 0.6,
    fontFace: FONT.TITLE, fontSize: 13, italic: true, bold: true, color: COLOR.WHITE, align: 'center', margin: 0
  });

  slide.addText("SarvaX.ai — Powered by C3ALabs", {
    x: 0.8, y: 6.95, w: 11.733, h: 0.3,
    fontFace: FONT.BODY, fontSize: 9, bold: true, color: COLOR.TEXT_MUTED, align: 'center', margin: 0
  });
}

// Save Presentation directly to Arvocap_10k_Report_Pilot_Deck.pptx
const outputPath = path.join(__dirname, 'Arvocap_10k_Report_Pilot_Deck.pptx');
pres.writeFile({ fileName: outputPath })
  .then(fileName => {
    console.log(`\n✅ Presentation with updated page ranges (1-3, 3-6, 7-12) written directly to: ${fileName}`);
  })
  .catch(err => {
    console.error("❌ Error writing presentation:", err);
  });
