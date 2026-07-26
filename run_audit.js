
const { chromium } = require('playwright');
const fs = require('fs');

async function runAudit() {
  const browser = await chromium.launch({ headless: true });
  const results = {
    consoleErrors: [],
    overflow390: [],
    overflow768: [],
    keyboardIssues: [],
    dialogIssues: [],
    chartIssues: [],
    printIssues: [],
    a11ySummary: {}
  };

  const context = await browser.newContext();
  const page = await context.newPage();

  page.on('console', msg => {
    if (msg.type() === 'error') {
      results.consoleErrors.push(msg.text());
    }
  });

  page.on('pageerror', err => {
    results.consoleErrors.push(err.message);
  });

  console.log('--- Navigating to page ---');
  await page.goto('http://localhost:8923/index.html', { waitUntil: 'networkidle' });

  // ==========================================
  // 1. OVERFLOW CHECKS (390px & 768px)
  // ==========================================
  console.log('--- Testing 390x844 Viewport ---');
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(500);

  const overflow390 = await page.evaluate(() => {
    const docWidth = document.documentElement.clientWidth;
    const bodyScrollWidth = document.documentElement.scrollWidth;
    const overflowingElements = [];

    const all = document.querySelectorAll('*');
    for (const el of all) {
      const rect = el.getBoundingClientRect();
      if (rect.right > docWidth + 1) { // 1px threshold for rounding
        // Find a selector / description
        let idStr = el.id ? '#' + el.id : '';
        let classStr = el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).join('.') : '';
        let tag = el.tagName.toLowerCase();
        let textExcerpt = el.innerText ? el.innerText.substring(0, 30).replace(/\n/g, ' ') : '';
        
        // Only record parent-most overflowing block or unique elements
        overflowingElements.push({
          tag,
          id: el.id,
          className: el.className,
          rectRight: Math.round(rect.right),
          rectWidth: Math.round(rect.width),
          textExcerpt
        });
      }
    }
    return {
      docWidth,
      bodyScrollWidth,
      hasHorizontalScroll: bodyScrollWidth > docWidth,
      overflowingElements: overflowingElements.slice(0, 20) // top 20
    };
  });
  results.overflow390 = overflow390;

  console.log('--- Testing 768x1024 Viewport ---');
  await page.setViewportSize({ width: 768, height: 1024 });
  await page.waitForTimeout(500);

  const overflow768 = await page.evaluate(() => {
    const docWidth = document.documentElement.clientWidth;
    const bodyScrollWidth = document.documentElement.scrollWidth;
    const overflowingElements = [];

    const all = document.querySelectorAll('*');
    for (const el of all) {
      const rect = el.getBoundingClientRect();
      if (rect.right > docWidth + 1) {
        overflowingElements.push({
          tag: el.tagName.toLowerCase(),
          id: el.id,
          className: el.className,
          rectRight: Math.round(rect.right),
          rectWidth: Math.round(rect.width),
          textExcerpt: el.innerText ? el.innerText.substring(0, 30).replace(/\n/g, ' ') : ''
        });
      }
    }
    return {
      docWidth,
      bodyScrollWidth,
      hasHorizontalScroll: bodyScrollWidth > docWidth,
      overflowingElements: overflowingElements.slice(0, 20)
    };
  });
  results.overflow768 = overflow768;

  // Reset viewport to desktop for keyboard & dialog tests
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.waitForTimeout(500);

  // ==========================================
  // 2. KEYBOARD & ACCESSIBILITY AUDIT
  // ==========================================
  console.log('--- Testing Keyboard & Interactive Elements ---');
  const keyboardAudit = await page.evaluate(() => {
    const issues = [];
    
    // Check all clickable elements
    const elementsWithOnClick = document.querySelectorAll('[onclick], [data-action]');
    elementsWithOnClick.forEach((el, index) => {
      const tag = el.tagName.toLowerCase();
      const tabIndex = el.getAttribute('tabindex');
      const role = el.getAttribute('role');
      const isNativeFocusable = ['a', 'button', 'input', 'select', 'textarea'].includes(tag);

      if (!isNativeFocusable && tabIndex === null) {
        issues.push({
          type: 'CLICKABLE_NOT_FOCUSABLE',
          tag,
          id: el.id,
          className: typeof el.className === 'string' ? el.className : '',
          text: el.innerText ? el.innerText.trim().substring(0, 40) : '',
          detail: 'Element has onclick/action handler but no tabindex attribute'
        });
      }

      if (!isNativeFocusable && !role) {
        issues.push({
          type: 'CLICKABLE_MISSING_ROLE',
          tag,
          id: el.id,
          className: typeof el.className === 'string' ? el.className : '',
          text: el.innerText ? el.innerText.trim().substring(0, 40) : '',
          detail: 'Interactive non-native element lacks role="button" or appropriate ARIA role'
        });
      }
    });

    // Check focus indicators on focusable elements
    const focusableElements = Array.from(document.querySelectorAll('a, button, input, select, textarea, [tabindex]:not([tabindex="-1"])'));
    const missingFocusStyles = [];

    focusableElements.forEach(el => {
      // Check computed outline / ring styles
      const style = window.getComputedStyle(el);
      const outlineStyle = style.outlineStyle;
      const outlineWidth = style.outlineWidth;
      const boxShadow = style.boxShadow;

      // Note: pseudo-classes like :focus cannot be read directly via getComputedStyle without focus,
      // but we can check if outline is explicitly hidden without replacement.
    });

    // Check inputs for labels
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
      const id = input.id;
      const hasLabel = id && document.querySelector(`label[for="${id}"]`);
      const ariaLabel = input.getAttribute('aria-label');
      const ariaLabelledBy = input.getAttribute('aria-labelledby');
      const title = input.getAttribute('title');

      if (!hasLabel && !ariaLabel && !ariaLabelledBy && !title) {
        issues.push({
          type: 'INPUT_MISSING_LABEL',
          tag: input.tagName.toLowerCase(),
          id: input.id,
          name: input.getAttribute('name'),
          placeholder: input.getAttribute('placeholder'),
          detail: 'Input element lacks an associated <label>, aria-label, or aria-labelledby'
        });
      }
    });

    return {
      totalClickable: elementsWithOnClick.length,
      totalFocusable: focusableElements.length,
      issues
    };
  });
  results.keyboardIssues = keyboardAudit;

  // ==========================================
  // 3. DIALOGS, ESCAPE KEY & FOCUS RESTORATION
  // ==========================================
  console.log('--- Testing Dialogs & Modals ---');
  const dialogAudit = await page.evaluate(async () => {
    const dialogIssues = [];

    // Find all modal overlays / elements
    const modals = document.querySelectorAll('[id*="modal"], [id*="Modal"], [class*="modal"], [class*="Modal"]');
    
    // Check structural ARIA on modals
    modals.forEach(modal => {
      if (modal.children.length === 0) return; // skip empty or helper tags
      const role = modal.getAttribute('role');
      const ariaModal = modal.getAttribute('aria-modal');
      const ariaLabel = modal.getAttribute('aria-label');
      const ariaLabelledBy = modal.getAttribute('aria-labelledby');

      if (role !== 'dialog' && role !== 'alertdialog') {
        dialogIssues.push({
          modalId: modal.id,
          modalClass: modal.className,
          issue: 'MISSING_ROLE_DIALOG',
          detail: `Modal container #${modal.id || modal.className} lacks role="dialog" or role="alertdialog"`
        });
      }

      if (ariaModal !== 'true') {
        dialogIssues.push({
          modalId: modal.id,
          modalClass: modal.className,
          issue: 'MISSING_ARIA_MODAL',
          detail: `Modal container #${modal.id || modal.className} lacks aria-modal="true"`
        });
      }

      if (!ariaLabel && !ariaLabelledBy) {
        dialogIssues.push({
          modalId: modal.id,
          modalClass: modal.className,
          issue: 'MISSING_ARIA_LABEL',
          detail: `Modal container #${modal.id || modal.className} lacks aria-label or aria-labelledby`
        });
      }
    });

    return dialogIssues;
  });
  results.dialogIssues.push(...dialogAudit);

  // Live interaction test on dialogs
  console.log('--- Interacting with Modals live via Playwright ---');
  // Find modal trigger buttons/cards
  const triggers = await page.$$('[onclick*="modal"], [onclick*="Modal"], [data-modal], [onclick*="open"], [onclick*="show"]');
  console.log(`Found ${triggers.length} potential modal trigger elements.`);

  for (let i = 0; i < Math.min(triggers.length, 5); i++) {
    const trigger = triggers[i];
    const triggerText = await trigger.innerText();
    const triggerInfo = await trigger.evaluate(el => ({
      id: el.id,
      tag: el.tagName,
      onclick: el.getAttribute('onclick')
    }));

    try {
      // Focus trigger before clicking
      await trigger.focus();
      const activeBefore = await page.evaluate(() => document.activeElement ? (document.activeElement.id || document.activeElement.tagName) : null);

      await trigger.click();
      await page.waitForTimeout(300);

      // Check if modal is visible
      const modalVisibleState = await page.evaluate(() => {
        const visibleModals = Array.from(document.querySelectorAll('[id*="modal"], [id*="Modal"], [class*="modal"]'))
          .filter(m => {
            const style = window.getComputedStyle(m);
            return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0';
          });
        return visibleModals.map(m => ({
          id: m.id,
          role: m.getAttribute('role'),
          ariaModal: m.getAttribute('aria-modal'),
          activeElementInside: m.contains(document.activeElement)
        }));
      });

      console.log(`Trigger [${triggerInfo.onclick}] opened ${modalVisibleState.length} modal(s):`, modalVisibleState);

      if (modalVisibleState.length > 0) {
        // Test Escape Key
        await page.keyboard.press('Escape');
        await page.waitForTimeout(300);

        const isClosed = await page.evaluate((modalId) => {
          const m = document.getElementById(modalId);
          if (!m) return true;
          const style = window.getComputedStyle(m);
          return style.display === 'none' || style.visibility === 'hidden' || style.opacity === '0' || m.classList.contains('hidden');
        }, modalVisibleState[0].id);

        const activeAfter = await page.evaluate(() => document.activeElement ? (document.activeElement.id || document.activeElement.tagName) : null);

        if (!isClosed) {
          results.dialogIssues.push({
            trigger: triggerInfo.onclick,
            issue: 'ESCAPE_KEY_FAILED',
            detail: `Pressing Escape did not close modal #${modalVisibleState[0].id}`
          });
        }

        // Focus restoration check
        // If it closed, check activeElement
        if (isClosed && activeAfter !== activeBefore) {
          results.dialogIssues.push({
            trigger: triggerInfo.onclick,
            issue: 'FOCUS_NOT_RESTORED',
            detail: `Closing modal did not restore focus to trigger. Focus before: ${activeBefore}, Focus after: ${activeAfter}`
          });
        }
      }
    } catch (e) {
      console.log(`Error testing trigger ${i}:`, e.message);
    }
  }

  // ==========================================
  // 4. CHART LEGIBILITY & ACCESSIBILITY AUDIT
  // ==========================================
  console.log('--- Testing Charts ---');
  const chartAudit = await page.evaluate(() => {
    const charts = document.querySelectorAll('canvas, svg.chart, .chart-container');
    const issues = [];

    charts.forEach(chart => {
      const id = chart.id || chart.className;
      const tag = chart.tagName.toLowerCase();
      const role = chart.getAttribute('role');
      const ariaLabel = chart.getAttribute('aria-label');
      const title = chart.getAttribute('title');
      const rect = chart.getBoundingClientRect();

      if (tag === 'canvas') {
        if (role !== 'img') {
          issues.push({
            chartId: id,
            issue: 'CANVAS_MISSING_ROLE_IMG',
            detail: `<canvas id="${id}"> lacks role="img"`
          });
        }
        if (!ariaLabel && !title) {
          issues.push({
            chartId: id,
            issue: 'CANVAS_MISSING_ARIA_LABEL',
            detail: `<canvas id="${id}"> lacks aria-label or accessible description`
          });
        }

        // Check if there is accessible fallback text or table in DOM
        const parent = chart.parentElement;
        const fallbackText = parent ? parent.innerText : '';
        if (!ariaLabel && fallbackText.replace(chart.innerText || '', '').trim().length < 10) {
          issues.push({
            chartId: id,
            issue: 'CANVAS_MISSING_FALLBACK_DATA',
            detail: `<canvas id="${id}"> has no accessible fallback text or table for screen readers`
          });
        }
      }

      // Check sizing
      if (rect.width < 100 || rect.height < 100) {
        issues.push({
          chartId: id,
          issue: 'CHART_COLLAPSED_OR_TINY',
          detail: `Chart element rendering box is unusually small (${Math.round(rect.width)}x${Math.round(rect.height)})`
        });
      }
    });

    return issues;
  });
  results.chartIssues = chartAudit;

  // Check chart responsiveness on 390px
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(500);

  const mobileChartSizes = await page.evaluate(() => {
    const canvases = document.querySelectorAll('canvas');
    return Array.from(canvases).map(c => {
      const rect = c.getBoundingClientRect();
      const style = window.getComputedStyle(c);
      return {
        id: c.id,
        displayWidth: Math.round(rect.width),
        displayHeight: Math.round(rect.height),
        canvasWidthAttr: c.width,
        canvasHeightAttr: c.height,
        parentWidth: c.parentElement ? Math.round(c.parentElement.getBoundingClientRect().width) : null
      };
    });
  });
  results.mobileChartSizes = mobileChartSizes;

  // ==========================================
  // 5. PRINT STYLESHEET AUDIT (@media print)
  // ==========================================
  console.log('--- Testing Print Styles ---');
  await page.emulateMedia({ media: 'print' });
  await page.waitForTimeout(500);

  const printAudit = await page.evaluate(() => {
    const issues = [];
    
    // Body background check in print mode
    const bodyStyle = window.getComputedStyle(document.body);
    const bodyBg = bodyStyle.backgroundColor;

    // Interactive controls visibility
    const buttons = document.querySelectorAll('button, input, select, nav, .navbar, .header-nav, .filter-bar, .controls');
    let visibleControls = 0;
    buttons.forEach(btn => {
      const style = window.getComputedStyle(btn);
      if (style.display !== 'none' && style.visibility !== 'hidden') {
        visibleControls++;
      }
    });

    if (visibleControls > 5) {
      issues.push({
        issue: 'INTERACTIVE_CONTROLS_VISIBLE_IN_PRINT',
        detail: `${visibleControls} interactive buttons/controls/inputs are visible in print mode. They should typically be hidden via @media print { display: none; }`
      });
    }

    // Check contrast / dark background in print
    // If background is rgb(15, 23, 42) or dark slate in print, it consumes massive ink and fails print standards
    const isDarkBg = bodyBg.includes('15, 23, 42') || bodyBg.includes('0, 0, 0') || bodyBg.includes('17, 24, 39') || bodyBg.includes('30, 41, 59');
    if (isDarkBg) {
      issues.push({
        issue: 'PRINT_DARK_BACKGROUND',
        detail: `Body background remains dark (${bodyBg}) in print mode instead of converting to white background for paper printing.`
      });
    }

    // Page break rules
    const cards = document.querySelectorAll('.card, .section, .panel, table, tr');
    let cardsWithoutBreakAvoid = 0;
    cards.forEach(card => {
      const style = window.getComputedStyle(card);
      const breakInside = style.breakInside || style.pageBreakInside;
      if (breakInside !== 'avoid' && breakInside !== 'avoid-page') {
        cardsWithoutBreakAvoid++;
      }
    });

    if (cardsWithoutBreakAvoid > 0) {
      issues.push({
        issue: 'CARDS_MISSING_PAGE_BREAK_AVOID',
        detail: `${cardsWithoutBreakAvoid} card/section elements do not have break-inside: avoid in print mode, risking awkward mid-card page splits.`
      });
    }

    return issues;
  });
  results.printIssues = printAudit;

  await browser.close();

  fs.writeFileSync('audit_results.json', JSON.stringify(results, null, 2));
  console.log('Audit completed! Saved to audit_results.json');
}

runAudit().catch(err => {
  console.error('Audit Script Error:', err);
  process.exit(1);
});
