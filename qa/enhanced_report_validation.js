const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const results = [];
  const errors = [];
  const check = (name, ok, detail) => results.push([name, !!ok, detail]);

  async function run(viewport, label) {
    const page = await browser.newPage({ viewport });
    page.on('pageerror', e => errors.push(`${label}: ${e.message}`));
    page.on('console', m => { if (m.type() === 'error') errors.push(`${label}: console ${m.text()}`); });
    await page.goto('http://127.0.0.1:8899/index.html?v=sarvax-product-map', { waitUntil: 'networkidle' });

    const buttons = page.locator('.route-mode');
    check(`${label}: three advisory journey controls`, await buttons.count() === 3, await buttons.allTextContents());
    check(`${label}: file-type controls removed`, !(await page.locator('.route-mode').allTextContents()).some(x => /Text PDF|Scanned|Structured Tax Data/i.test(x)), await buttons.allTextContents());
    check(`${label}: four bounded model roles`, await page.locator('.uncanny-role-card').count() === 4, await page.locator('.uncanny-role-card').count());

    const expected = [
      { id: 'relationship', label: 'Client Relationship Intelligence', stages: 6, agents: 3, must: 'Meeting Assistant' },
      { id: 'portfolio', label: 'Portfolio & Market Intelligence', stages: 8, agents: 2, must: 'Portfolio Analyst' },
      { id: 'operations', label: 'Compliance & Advisor Operations', stages: 8, agents: 7, must: 'KYC/CDD QA Auditor' },
    ];
    for (const j of expected) {
      await page.locator(`[data-route-mode="${j.id}"]`).click();
      check(`${label}: ${j.id} selected`, await page.locator(`[data-route-mode="${j.id}"]`).getAttribute('aria-pressed') === 'true', await page.locator(`[data-route-mode="${j.id}"]`).getAttribute('aria-pressed'));
      check(`${label}: ${j.id} stage count`, await page.locator('#uncannyRouteFlow .route-node').count() === j.stages, await page.locator('#uncannyRouteFlow .route-node').count());
      check(`${label}: ${j.id} journey label`, (await page.locator('.journey-map-head strong').textContent()).trim() === j.label, await page.locator('.journey-map-head strong').textContent());
      check(`${label}: ${j.id} agent count`, await page.locator('#productJourneyMap article').nth(1).locator('.journey-tags span').count() === j.agents, await page.locator('#productJourneyMap article').nth(1).locator('.journey-tags span').count());
      check(`${label}: ${j.id} product mapping visible`, (await page.locator('#productJourneyMap').textContent()).includes(j.must), j.must);
      check(`${label}: ${j.id} has control boundary`, /approv|advisor owns/i.test(await page.locator('.journey-guardrail').textContent()), await page.locator('.journey-guardrail').textContent());
    }

    const state = await page.evaluate(() => ({
      journeys: routingArchitecture.journeys.length,
      mappedAgents: new Set(routingArchitecture.journeys.flatMap(j => j.agents)).size,
      configs: models.reduce((n, m) => n + m.configurationCount, 0),
      claude: models.filter(m => m.name === 'Claude Opus 5').length,
      productEvidence: routingArchitecture.product_mapping.evidence_status,
    }));
    check(`${label}: all 12 SARVAX agents mapped`, state.mappedAgents === 12, state.mappedAgents);
    check(`${label}: codebase evidence boundary explicit`, /frontend contracts/.test(state.productEvidence), state.productEvidence);

    const sectionText = await page.locator('.uncanny-shell').textContent();
    check(`${label}: product-not-model message visible`, sectionText.includes('Models underneath the product'), sectionText.slice(0, 120));
    check(`${label}: broad channels visible`, /meetings, CRM history, email, WhatsApp, holdings, market data, KYC/.test(sectionText), 'channels');
    check(`${label}: deterministic and human controls visible`, /deterministic calculations, policy enforcement, authorization and human approval/i.test(sectionText), 'controls');
    check(`${label}: old PDF-first route copy absent`, !/Choose an example document route|Text PDF|Scanned \/ Image PDF|Structured Tax Data/.test(sectionText), 'old labels scan');
    check(`${label}: no undefined architecture fields`, !/undefined/i.test(sectionText), sectionText.match(/.{0,30}undefined.{0,30}/i));

    const shell = await page.locator('.uncanny-shell').boundingBox();
    check(`${label}: architecture shell fits viewport`, shell.x >= -1 && shell.x + shell.width <= viewport.width + 1, shell);
    const routeGeometry = await page.locator('#uncannyRouteFlow').evaluate(el => ({ scrollWidth: el.scrollWidth, clientWidth: el.clientWidth, direction: getComputedStyle(el).flexDirection }));
    check(`${label}: selected route has no horizontal clipping`, routeGeometry.scrollWidth <= routeGeometry.clientWidth + 1, routeGeometry);
    if (label === 'mobile') {
      await page.locator('[data-route-mode="operations"]').click();
      const geometry = await page.locator('#uncannyRouteFlow').evaluate(el => ({ scrollWidth: el.scrollWidth, clientWidth: el.clientWidth, direction: getComputedStyle(el).flexDirection }));
      check(`${label}: route is vertical`, geometry.direction === 'column', geometry);
      check(`${label}: route has no horizontal clipping`, geometry.scrollWidth <= geometry.clientWidth + 1, geometry);
    }

    await page.locator('#models').scrollIntoViewIfNeeded();
    check(`${label}: Section 7 retains 24 unique cards`, await page.locator('.model-card').count() === 24, await page.locator('.model-card').count());
    check(`${label}: 40 benchmark configurations retained`, state.configs === 40, state.configs);
    check(`${label}: Claude Opus 5 remains one card`, state.claude === 1, state.claude);

    await page.locator('.uncanny-shell').screenshot({ path: `/Users/satyyy/Documents/R&D - C3ALABS/LLM-Intelligence-Repository/qa/sarvax-product-map-${label}.png` });
    await page.close();
  }

  await run({ width: 1440, height: 1000 }, 'desktop');
  await run({ width: 390, height: 844 }, 'mobile');
  await browser.close();
  const pass = results.filter(x => x[1]).length;
  const out = { pass, total: results.length, errors, results };
  fs.writeFileSync('/Users/satyyy/Documents/R&D - C3ALABS/LLM-Intelligence-Repository/qa/enhanced_report_validation.json', JSON.stringify(out, null, 2));
  console.log(JSON.stringify({ pass, total: results.length, errors }, null, 2));
  process.exit(pass === results.length && !errors.length ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
