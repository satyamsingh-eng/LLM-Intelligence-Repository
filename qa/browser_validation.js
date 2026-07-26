const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const root = path.resolve(__dirname, '..');
const outDir = path.join(root, 'audit', 'screenshots');
fs.mkdirSync(outDir, { recursive: true });
const url = process.env.REPORT_URL || 'http://127.0.0.1:8899/Documents/R%26D%20-%20C3ALABS/LLM-Intelligence-Repository/index.html';
const tests = [];
function record(name, ok, detail='') { tests.push({name, status: ok ? 'PASS' : 'FAIL', detail}); }
function assert(name, condition, detail='') { record(name, Boolean(condition), detail); if (!condition) throw new Error(`${name}: ${detail}`); }

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' });
  let fatal = null;
  try {
    const desktop = await browser.newPage({ viewport: { width: 1440, height: 900 } });
    const consoleErrors = [];
    desktop.on('console', m => { if (m.type() === 'error') consoleErrors.push(m.text()); });
    desktop.on('pageerror', e => consoleErrors.push(e.message));
    const response = await desktop.goto(url, { waitUntil: 'networkidle' });
    assert('HTTP document load', response && response.ok(), `status=${response && response.status()}`);
    assert('Structured dataset rendered', await desktop.locator('#claimRows tr').count() === 22, `rows=${await desktop.locator('#claimRows tr').count()}`);
    assert('Executive decision visible', (await desktop.locator('#decisionText').innerText()).startsWith('NO-GO'), await desktop.locator('#decisionText').innerText());
    assert('No external runtime scripts', await desktop.locator('script[src]').count() === 0, `external=${await desktop.locator('script[src]').count()}`);
    assert('No load error banner', await desktop.locator('#loadError').evaluate(el => getComputedStyle(el).display === 'none'));

    await desktop.locator('#claimFilters [data-filter="verified"]').click();
    assert('Claim filter interaction', await desktop.locator('#claimRows tr').count() === 1, `filtered=${await desktop.locator('#claimRows tr').count()}`);
    await desktop.locator('[data-claim="C-018"]').first().click();
    assert('Evidence dialog opens', await desktop.locator('#claimDialog').evaluate(el => el.open));
    assert('Evidence dialog has eight fields', await desktop.locator('#dialogGrid > div').count() === 8, `fields=${await desktop.locator('#dialogGrid > div').count()}`);
    assert('Dialog close receives focus', await desktop.locator('#closeDialog').evaluate(el => document.activeElement === el));
    await desktop.keyboard.press('Escape');
    assert('Escape closes evidence dialog', !(await desktop.locator('#claimDialog').evaluate(el => el.open)));
    await desktop.locator('#claimFilters [data-filter="all"]').click();

    await desktop.locator('#workflowSelect').selectOption('wf-daily-summary');
    assert('Workflow selection', (await desktop.locator('#workflowName').innerText()) === 'Daily operations summary');
    await desktop.locator('#runWorkflow').click();
    await desktop.waitForTimeout(3100);
    assert('Workflow player completes', (await desktop.locator('#workflowProgress').getAttribute('style')).includes('100%'), await desktop.locator('#workflowProgress').getAttribute('style'));
    assert('Workflow keeps unmeasured telemetry honest', (await desktop.locator('.m-value').allInnerTexts()).every(x => x === 'Not measured'));
    assert('Workflow timer stops', await desktop.evaluate(() => timer === null));

    await desktop.locator('#termSearch').fill('OCR');
    const matched = await desktop.locator('.term').count();
    assert('Glossary search interaction', matched >= 1 && matched < 25, `matched=${matched}`);
    await desktop.locator('.term > button').first().click();
    assert('Glossary accordion interaction', await desktop.locator('.term > button').first().getAttribute('aria-expanded') === 'true');
    await desktop.locator('#termSearch').fill('');

    await desktop.emulateMedia({ media: 'print' });
    assert('Print mode hides navigation', await desktop.locator('.nav').evaluate(el => getComputedStyle(el).display === 'none'));
    await desktop.emulateMedia({ media: 'screen' });
    await desktop.screenshot({ path: path.join(outDir, 'desktop-full.png'), fullPage: true });
    assert('Desktop screenshot generated', fs.existsSync(path.join(outDir, 'desktop-full.png')));
    assert('Desktop console clean', consoleErrors.length === 0, JSON.stringify(consoleErrors));
    await desktop.close();

    const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
    const mobileErrors = [];
    mobile.on('console', m => { if (m.type() === 'error') mobileErrors.push(m.text()); });
    mobile.on('pageerror', e => mobileErrors.push(e.message));
    await mobile.goto(url, { waitUntil: 'networkidle' });
    const geometry = await mobile.evaluate(() => ({
      innerWidth,
      rootWidth: document.documentElement.scrollWidth,
      bodyWidth: document.body.scrollWidth,
      containers: [...document.querySelectorAll('.container')].map(x => ({ id: x.id, left: x.getBoundingClientRect().left, right: x.getBoundingClientRect().right, scroll: x.scrollWidth, client: x.clientWidth })),
      allowedOverflow: [...document.querySelectorAll('.nav,.nav-inner,.table-wrap')].map(x => ({ cls: x.className, scroll: x.scrollWidth, client: x.clientWidth }))
    }));
    assert('Mobile document has no horizontal overflow', geometry.rootWidth === 390 && geometry.bodyWidth === 390, JSON.stringify(geometry));
    assert('Mobile content containers stay inside viewport', geometry.containers.every(x => x.left >= 0 && x.right <= 390 && x.scroll <= x.client + 1), JSON.stringify(geometry.containers));
    assert('Mobile decision remains visible', await mobile.locator('#decisionText').isVisible());
    assert('Mobile decision text remains complete', (await mobile.locator('#decisionText').innerText()).includes('production routing'));
    await mobile.screenshot({ path: path.join(outDir, 'mobile-390x844.png'), fullPage: false });
    assert('Mobile screenshot generated', fs.existsSync(path.join(outDir, 'mobile-390x844.png')));
    assert('Mobile console clean', mobileErrors.length === 0, JSON.stringify(mobileErrors));
    await mobile.close();
  } catch (e) {
    fatal = e.stack || String(e);
  } finally {
    await browser.close();
  }
  const failed = tests.filter(t => t.status === 'FAIL');
  const sha256 = p => crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
  const result = { executed_at: new Date().toISOString(), url, html_sha256: sha256(path.join(root, 'index.html')), dataset_sha256: sha256(path.join(root, 'models', 'report_data.json')), passed: tests.length - failed.length, total: tests.length, overall: fatal || failed.length ? 'FAIL' : 'PASS', fatal, tests };
  fs.writeFileSync(path.join(root, '10-Validation-Logs', 'browser_validation_results.json'), JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ overall: result.overall, passed: result.passed, total: result.total, fatal }, null, 2));
  process.exit(result.overall === 'PASS' ? 0 : 1);
})();
