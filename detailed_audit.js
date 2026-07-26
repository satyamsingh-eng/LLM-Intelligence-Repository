
const { chromium } = require('playwright');
const fs = require('fs');

async function detailedAudit() {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  await page.goto('http://localhost:8923/index.html', { waitUntil: 'networkidle' });

  // 1. Mobile Touch Targets & Specific Overflow Elements at 390x844
  await page.setViewportSize({ width: 390, height: 844 });
  await page.waitForTimeout(500);

  const mobileDetails = await page.evaluate(() => {
    // Check elements exceeding 390px
    const overflowing = [];
    const all = document.querySelectorAll('body *');
    all.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.right > 391) { // 391 to avoid 1px border
        overflowing.push({
          tagName: el.tagName.toLowerCase(),
          id: el.id,
          className: el.className,
          rectLeft: Math.round(rect.left),
          rectRight: Math.round(rect.right),
          rectWidth: Math.round(rect.width),
          textSnippet: el.innerText ? el.innerText.substring(0, 40).replace(/\n/g, ' ') : ''
        });
      }
    });

    // Filter to top-level containers causing overflow
    const topContainers = overflowing.filter(item => {
      // Find parent items
      return ['nav', 'header', 'div', 'section', 'canvas', 'table', 'ul'].includes(item.tagName);
    });

    // Check touch target sizes for interactive elements (< 24px height or width)
    const smallTargets = [];
    const interactives = document.querySelectorAll('button, a, input, select, textarea, [onclick], [role="button"]');
    interactives.forEach(el => {
      const rect = el.getBoundingClientRect();
      if ((rect.width > 0 || rect.height > 0) && (rect.width < 24 || rect.height < 24)) {
        smallTargets.push({
          tag: el.tagName.toLowerCase(),
          id: el.id,
          class: el.className,
          text: el.innerText ? el.innerText.trim().substring(0, 30) : '',
          width: Math.round(rect.width),
          height: Math.round(rect.height)
        });
      }
    });

    return {
      totalOverflowingElements: overflowing.length,
      topContainers: topContainers.slice(0, 15),
      smallTargetsCount: smallTargets.length,
      smallTargets: smallTargets.slice(0, 15)
    };
  });

  // 2. Focus Visible Styles Test
  await page.setViewportSize({ width: 1280, height: 800 });
  await page.waitForTimeout(300);

  const focusStylesTest = await page.evaluate(async () => {
    const focusables = Array.from(document.querySelectorAll('a, button, input, select, textarea, [tabindex="0"]'));
    const results = [];

    for (let i = 0; i < Math.min(focusables.length, 30); i++) {
      const el = focusables[i];
      el.focus();
      const style = window.getComputedStyle(el);
      const outlineStyle = style.outlineStyle;
      const outlineColor = style.outlineColor;
      const outlineWidth = style.outlineWidth;
      const boxShadow = style.boxShadow;
      const borderColor = style.borderColor;

      const hasVisibleFocus = outlineStyle !== 'none' && outlineWidth !== '0px' ||
                              (boxShadow && boxShadow !== 'none') ||
                              style.outline !== '0px none rgb(255, 255, 255)';

      results.push({
        tag: el.tagName.toLowerCase(),
        id: el.id,
        class: typeof el.className === 'string' ? el.className.substring(0, 30) : '',
        text: el.innerText ? el.innerText.trim().substring(0, 25) : '',
        outlineStyle,
        outlineWidth,
        boxShadow,
        hasVisibleFocus
      });
    }
    return results;
  });

  // 3. Contrast Ratios Sample Check
  const contrastCheck = await page.evaluate(() => {
    // Helper to calculate luminance & contrast ratio
    function getRGB(colorStr) {
      const match = colorStr.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
      if (!match) return null;
      return [parseInt(match[1]), parseInt(match[2]), parseInt(match[3])];
    }

    function getLuminance([r, g, b]) {
      const a = [r, g, b].map(v => {
        v /= 255;
        return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
      });
      return a[0] * 0.2126 + a[1] * 0.7152 + a[2] * 0.0722;
    }

    function getContrastRatio(rgb1, rgb2) {
      const l1 = getLuminance(rgb1) + 0.05;
      const l2 = getLuminance(rgb2) + 0.05;
      return l1 > l2 ? l1 / l2 : l2 / l1;
    }

    const textElements = document.querySelectorAll('p, span, h1, h2, h3, h4, th, td, label, button, a');
    const lowContrastElements = [];

    textElements.forEach(el => {
      const text = el.innerText ? el.innerText.trim() : '';
      if (!text || text.length < 2) return;

      const style = window.getComputedStyle(el);
      const fgColor = style.color;
      let parent = el.parentElement;
      let bgColor = style.backgroundColor;

      // Trace back for background if transparent
      while (parent && (bgColor === 'rgba(0, 0, 0, 0)' || bgColor === 'transparent')) {
        bgColor = window.getComputedStyle(parent).backgroundColor;
        parent = parent.parentElement;
      }

      const fgRGB = getRGB(fgColor);
      const bgRGB = getRGB(bgColor);

      if (fgRGB && bgRGB) {
        const ratio = getContrastRatio(fgRGB, bgRGB);
        const fontSize = parseFloat(style.fontSize);
        const isBold = style.fontWeight === '700' || style.fontWeight === 'bold';
        const minRatio = (fontSize >= 18 || (fontSize >= 14 && isBold)) ? 3.0 : 4.5;

        if (ratio < minRatio) {
          lowContrastElements.push({
            tag: el.tagName.toLowerCase(),
            class: typeof el.className === 'string' ? el.className.substring(0, 30) : '',
            text: text.substring(0, 30),
            fgColor,
            bgColor,
            ratio: ratio.toFixed(2),
            minRatio,
            fontSize
          });
        }
      }
    });

    return lowContrastElements;
  });

  await browser.close();

  const output = {
    mobileDetails,
    focusStylesTest,
    lowContrastElementsCount: contrastCheck.length,
    lowContrastSamples: contrastCheck.slice(0, 20)
  };

  fs.writeFileSync('detailed_audit.json', JSON.stringify(output, null, 2));
  console.log('Detailed audit completed!');
}

detailedAudit().catch(console.error);
