const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  
  const filePath = pathToFileURL(path.resolve(__dirname, 'index.html')).href;
  await page.goto(filePath, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  const audit = await page.evaluate(() => {
    const list = [];

    // Helper
    const add = (id, comp, sel, desc, details) => list.push({ id, comp, sel, desc, details });

    // 1. Model Card Toolbar Alignment
    const toolbar = document.querySelector('.model-card-toolbar');
    if (toolbar) {
      const select = toolbar.querySelector('select');
      const span = toolbar.querySelector('span');
      if (select && span) {
        const sR = select.getBoundingClientRect();
        const spR = span.getBoundingClientRect();
        add('TOOL_ALIGN', 'Model Cards Toolbar', '.model-card-toolbar', `Filter select box (${Math.round(sR.height)}px h) and card counter text (${Math.round(spR.height)}px h) align to flex-end without vertical baseline centering`, { selectY: sR.y, spanY: spR.y });
      }
    }

    // 2. Model Cards Metric Grid Item Padding / Alignment
    const modelMetrics = [...document.querySelectorAll('.model-metrics')];
    modelMetrics.forEach((grid, idx) => {
      const metrics = [...grid.querySelectorAll('.model-metric')];
      if (metrics.length >= 2) {
        const r1 = metrics[0].getBoundingClientRect();
        const r2 = metrics[1].getBoundingClientRect();
        if (Math.abs(r1.height - r2.height) > 2) {
          add('METRIC_HEIGHT', 'Model Metric Box', `.model-cards-grid .model-card:nth-child(${idx+1}) .model-metrics`, `Side-by-side metric boxes have unequal heights (${Math.round(r1.height)}px vs ${Math.round(r2.height)}px)`, { h1: r1.height, h2: r2.height });
        }
      }
    });

    // 3. Workflow Control-Flow Progress Bar
    const wfProgress = document.querySelector('.workflow-progress');
    if (wfProgress) {
      const cs = window.getComputedStyle(wfProgress);
      const textSpan = wfProgress.querySelector('span') || wfProgress;
      const bar = wfProgress.querySelector('div');
      if (bar) {
        const bR = bar.getBoundingClientRect();
        add('WF_PROGRESS', 'Workflow Progress Bar', '.workflow-progress > div', `Progress bar container height is only 6px with pitch black background (#000) and dark border, making progress hard to discern`, { height: bR.height });
      }
    }

    // 4. Chart Boxes Max Width / Overflow Wrapping
    const chartBoxes = [...document.querySelectorAll('.chart-box')];
    chartBoxes.forEach((cb, idx) => {
      const h4 = cb.querySelector('h4');
      const canvas = cb.querySelector('canvas');
      const boundary = cb.querySelector('.chart-boundary');
      const cs = window.getComputedStyle(cb);
      if (cs.padding !== '24px') {
        add('CHART_PAD', 'Chart Box Padding', `#charts .chart-box:nth-child(${idx+1})`, `Chart box padding uses custom inline style overriding theme standards`, { padding: cs.padding });
      }
    });

    // 5. Governance Cards Grid Gap & Button Margins
    const govCards = [...document.querySelectorAll('.governance-card')];
    govCards.forEach((card, idx) => {
      const a = card.querySelector('a');
      if (a) {
        const aCs = window.getComputedStyle(a);
        if (aCs.marginTop === '14px') {
          add('GOV_LINK', 'Governance Card Action Link', `.governance-card:nth-child(${idx+1}) a`, `Inline action link uses top margin instead of standard button pill container`, { margin: aCs.marginTop });
        }
      }
    });

    // 6. Section Labels Letter-Spacing / Font-Weight
    const labels = [...document.querySelectorAll('.section-label')];
    labels.forEach((lbl, idx) => {
      const cs = window.getComputedStyle(lbl);
      if (cs.letterSpacing === '2px') {
        // Check letter spacing inconsistency with architecture eyebrow (0.14em = ~1.54px)
      }
    });

    return list;
  });

  console.log(JSON.stringify(audit, null, 2));
  await browser.close();
})();
