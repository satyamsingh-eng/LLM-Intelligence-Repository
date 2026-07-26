const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    
    const filePath = pathToFileURL(path.resolve(__dirname, 'index.html')).href;
    await page.goto(filePath, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    const audit = await page.evaluate(() => {
      const issues = [];

      // Helper to check alignment & box props
      const checkEl = (sel, name) => {
        const els = [...document.querySelectorAll(sel)];
        if (!els.length) return { name, count: 0 };
        return {
          name,
          count: els.length,
          items: els.map((el, idx) => {
            const r = el.getBoundingClientRect();
            const cs = window.getComputedStyle(el);
            return {
              idx,
              tag: el.tagName,
              cls: el.className,
              id: el.id,
              x: Math.round(r.x),
              y: Math.round(r.y),
              w: Math.round(r.width),
              h: Math.round(r.height),
              fontSize: cs.fontSize,
              fontWeight: cs.fontWeight,
              lineHeight: cs.lineHeight,
              padding: cs.padding,
              margin: cs.margin,
              display: cs.display,
              flexDirection: cs.flexDirection,
              alignItems: cs.alignItems,
              justifyContent: cs.justifyContent,
              bg: cs.backgroundColor,
              color: cs.color,
              border: cs.border,
              borderRadius: cs.borderRadius
            };
          })
        };
      };

      // 1. Sticky Nav + Progress bar
      const nav = checkEl('.nav', 'Sticky Nav');
      const progressBar = checkEl('#progressBar', 'Scroll Progress Bar');

      // 2. Verdict Box & KPI Strip
      const verdict = checkEl('.verdict', 'Executive Verdict Box');
      const kpis = checkEl('.kpi', 'KPI Items');

      // 3. Uncanny Valley / Route Flow
      const routeFlow = checkEl('.uncanny-route-flow', 'Route Flow Box');
      const routeNodes = checkEl('.route-node', 'Route Nodes');
      const routeArrows = checkEl('.route-arrow', 'Route Arrows');

      // 4. Product Journey Map
      const journeyMap = checkEl('.product-journey-map', 'Product Journey Map');
      const journeyMapArticles = checkEl('.journey-map-grid article', 'Journey Map Articles');

      // 5. Uncanny Role Cards
      const roleCards = checkEl('.uncanny-role-card', 'Uncanny Role Cards');

      // 6. Wealth Usecase Cards
      const usecaseCards = checkEl('.usecase-card', 'Wealth Usecase Cards');

      // 7. Simulator
      const simControls = checkEl('#simulator select, #simulator input', 'Simulator Inputs');
      const simResults = checkEl('.sim-results article', 'Simulator Results Cards');

      // 8. Workflows
      const wfLayout = checkEl('.workflow-layout', 'Workflow Layout');
      const dagSteps = checkEl('.dag-step', 'DAG Steps');

      // 9. Charts
      const chartBoxes = checkEl('.chart-box', 'Chart Boxes');
      const chartCanvases = checkEl('#charts canvas', 'Chart Canvases');

      // 10. Proof Cards
      const proofCards = checkEl('.evidence-summary details, .review-grid details', 'Proof Cards');

      // 11. Model Cards
      const modelCards = checkEl('.model-card', 'Model Cards');
      const modelMetrics = checkEl('.model-metric', 'Model Metrics');

      // 12. Compliance
      const govCards = checkEl('.governance-card', 'Governance Cards');

      return {
        nav,
        progressBar,
        verdict,
        kpis,
        routeFlow,
        routeNodes,
        routeArrows,
        journeyMap,
        journeyMapArticles,
        roleCards,
        usecaseCards,
        simControls,
        simResults,
        wfLayout,
        dagSteps,
        chartBoxes,
        chartCanvases,
        proofCards,
        modelCards,
        modelMetrics,
        govCards
      };
    });

    console.log(JSON.stringify(audit, null, 2));
    await browser.close();
  } catch (err) {
    console.error('ERROR:', err);
  }
})();
