
const { chromium } = require('playwright');
const fs = require('fs');

async function testModals() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:8923/index.html', { waitUntil: 'networkidle' });

  const modalResults = {};

  // 1. Test Evidence Modal
  console.log('--- Testing Evidence Modal ---');
  // Trigger evidence modal
  const evTrigger = await page.$('.model-detail-btn');
  if (evTrigger) {
    await evTrigger.focus();
    const triggerIdBefore = await page.evaluate(() => document.activeElement ? (document.activeElement.outerHTML) : null);
    await evTrigger.click();
    await page.waitForTimeout(300);

    const evModalState = await page.evaluate(() => {
      const modal = document.getElementById('evidenceModal');
      const dialog = modal ? modal.querySelector('.evidence-dialog') : null;
      return {
        modalHidden: modal ? modal.hidden : null,
        modalRole: modal ? modal.getAttribute('role') : null,
        dialogRole: dialog ? dialog.getAttribute('role') : null,
        ariaModal: modal ? modal.getAttribute('aria-modal') : null,
        ariaLabelledBy: dialog ? dialog.getAttribute('aria-labelledby') : null,
        activeElement: document.activeElement ? document.activeElement.outerHTML : null
      };
    });

    // Test Tabbing inside Evidence Modal
    const tabHistory = [];
    for (let i = 0; i < 15; i++) {
      await page.keyboard.press('Tab');
      const active = await page.evaluate(() => {
        const modal = document.getElementById('evidenceModal');
        const activeEl = document.activeElement;
        return {
          insideModal: modal ? modal.contains(activeEl) : false,
          tag: activeEl.tagName,
          id: activeEl.id,
          class: activeEl.className,
          text: activeEl.innerText ? activeEl.innerText.substring(0, 20) : ''
        };
      });
      tabHistory.push(active);
    }

    const leakedToBackground = tabHistory.some(t => !t.insideModal);

    // Test Escape Key
    await page.keyboard.press('Escape');
    await page.waitForTimeout(300);

    const afterEscapeState = await page.evaluate(() => {
      const modal = document.getElementById('evidenceModal');
      return {
        modalHidden: modal ? modal.hidden : null,
        activeElement: document.activeElement ? document.activeElement.outerHTML : null
      };
    });

    modalResults.evidenceModal = {
      evModalState,
      leakedToBackground,
      afterEscapeState,
      triggerIdBefore
    };
  }

  // 2. Test Term Modal
  console.log('--- Testing Term Modal ---');
  const termTrigger = await page.$('.term-link');
  if (termTrigger) {
    // Note: termTrigger might not be focusable if no tabindex!
    await page.evaluate(() => {
      const link = document.querySelector('.term-link');
      if (link) link.click();
    });
    await page.waitForTimeout(300);

    const termModalState = await page.evaluate(() => {
      const modal = document.getElementById('termModal');
      return {
        classList: modal ? Array.from(modal.classList) : [],
        modalRole: modal ? modal.getAttribute('role') : null,
        ariaModal: modal ? modal.getAttribute('aria-modal') : null,
        activeElement: document.activeElement ? document.activeElement.outerHTML : null
      };
    });

    // Test Tabbing inside Term Modal
    const tabHistory = [];
    for (let i = 0; i < 15; i++) {
      await page.keyboard.press('Tab');
      const active = await page.evaluate(() => {
        const modal = document.getElementById('termModal');
        const activeEl = document.activeElement;
        return {
          insideModal: modal ? modal.contains(activeEl) : false,
          tag: activeEl.tagName,
          id: activeEl.id,
          class: activeEl.className,
          text: activeEl.innerText ? activeEl.innerText.substring(0, 20) : ''
        };
      });
      tabHistory.push(active);
    }

    const leakedToBackground = tabHistory.some(t => !t.insideModal);

    // Test Escape Key
    await page.keyboard.press('Escape');
    await page.waitForTimeout(300);

    const afterEscapeState = await page.evaluate(() => {
      const modal = document.getElementById('termModal');
      return {
        classList: modal ? Array.from(modal.classList) : [],
        activeElement: document.activeElement ? document.activeElement.outerHTML : null
      };
    });

    modalResults.termModal = {
      termModalState,
      leakedToBackground,
      afterEscapeState
    };
  }

  await browser.close();

  fs.writeFileSync('modal_test_results.json', JSON.stringify(modalResults, null, 2));
  console.log('Done modal tests');
}

testModals().catch(console.error);
