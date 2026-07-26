const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  try {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
    
    const filePath = pathToFileURL(path.resolve(__dirname, 'index.html')).href;
    console.log('Loading file:', filePath);
    await page.goto(filePath, { waitUntil: 'networkidle' });
    await page.waitForTimeout(1000);

    const audit = await page.evaluate(() => {
      const getMeta = (sel) => {
        const el = document.querySelector(sel);
        if (!el) return null;
        const r = el.getBoundingClientRect();
        const cs = window.getComputedStyle(el);
        return { 
          rect: { x: r.x, y: r.y, w: r.width, h: r.height, top: r.top, bottom: r.bottom, left: r.left, right: r.right }, 
          style: { bg: cs.backgroundColor, color: cs.color, flex: cs.flex, display: cs.display, padding: cs.padding, margin: cs.margin, gap: cs.gap, alignSelf: cs.alignSelf, justifyContent: cs.justifyContent } 
        };
      };

      // 1. Navigation
      const navMeta = getMeta('.nav');
      const navLinks = [...document.querySelectorAll('.nav a')].map(a => {
        const r = a.getBoundingClientRect();
        return { text: a.textContent.trim(), href: a.getAttribute('href'), x: r.x, right: r.right, width: r.width };
      });

      // 2. Sections inspection
      const sections = [...document.querySelectorAll('.section, .section-dark, .section-light')].map((el, i) => {
        const r = el.getBoundingClientRect();
        const h2 = el.querySelector('h2')?.textContent.trim();
        const label = el.querySelector('.section-label')?.textContent.trim();
        const cs = window.getComputedStyle(el);
        return { idx: i, id: el.id, label, h2, rect: { x: r.x, y: r.y, w: r.width, h: r.height }, padding: cs.padding, maxW: cs.maxWidth };
      });

      // 3. Uncanny / Architecture flow
      const routeFlow = getMeta('.uncanny-route-flow');
      const routeNodes = [...document.querySelectorAll('.route-node')].map((el, i) => {
        const r = el.getBoundingClientRect();
        const cs = window.getComputedStyle(el);
        return { i, title: el.querySelector('strong')?.textContent.trim(), rect: { x: r.x, y: r.y, w: r.width, h: r.height, right: r.right }, minW: cs.minWidth, flex: cs.flex };
      });

      // 4. Usecase cards alignment
      const usecaseCards = [...document.querySelectorAll('.usecase-card')].map((el, i) => {
        const r = el.getBoundingClientRect();
        const h3 = el.querySelector('h3')?.textContent.trim();
        const cs = window.getComputedStyle(el);
        const aside = el.querySelector('aside');
        const asideR = aside ? aside.getBoundingClientRect() : null;
        return { 
          i, h3, cardWidth: r.width, cardHeight: r.height, gridTemplate: cs.gridTemplateColumns, 
          asideWidth: asideR ? asideR.width : null, asideHeight: asideR ? asideR.height : null 
        };
      });

      // 5. Model cards grid alignment
      const modelCards = [...document.querySelectorAll('.model-card')].map((el, i) => {
        const r = el.getBoundingClientRect();
        const title = el.querySelector('h3')?.textContent.trim();
        const vendor = el.querySelector('.model-card-vendor')?.textContent.trim();
        return { i, title, vendor, width: r.width, height: r.height };
      });

      // 6. Check for horizontal scroll / overflow at 1440px
      const docW = document.documentElement.scrollWidth;
      const clientW = document.documentElement.clientWidth;
      const overflowElements = [];
      document.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.right > clientW + 2 && el.tagName !== 'HTML' && el.tagName !== 'BODY') {
          overflowElements.push({ tag: el.tagName, id: el.id, cls: el.className, right: r.right, width: r.width });
        }
      });

      // 7. Check tiny font sizes (<11px)
      const tinyElements = [];
      document.querySelectorAll('*').forEach(el => {
        if (el.children.length === 0 && el.textContent.trim().length > 0) {
          const fSize = parseFloat(window.getComputedStyle(el).fontSize);
          if (fSize < 11) {
            tinyElements.push({ tag: el.tagName, cls: el.className, text: el.textContent.trim().slice(0, 40), fSize });
          }
        }
      });

      return {
        docW, clientW,
        navMeta, navLinks,
        sections,
        routeFlow,
        routeNodes,
        usecaseCards,
        modelCardsCount: modelCards.length,
        modelCardHeights: modelCards.map(m => ({ title: m.title, h: m.height })),
        overflowElements: overflowElements.slice(0, 15),
        tinyElementsCount: tinyElements.length,
        tinyElementsSample: tinyElements.slice(0, 15)
      };
    });

    console.log(JSON.stringify(audit, null, 2));
    await browser.close();
  } catch (err) {
    console.error('ERROR:', err);
  }
})();
