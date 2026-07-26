const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1440, height: 1000 } });
  
  const filePath = pathToFileURL(path.resolve(__dirname, 'index.html')).href;
  await page.goto(filePath, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1000);

  const findings = await page.evaluate(() => {
    const list = [];

    // Helper to log finding
    const add = (severity, category, component, selector, description, details) => {
      list.push({ severity, category, component, selector, description, details });
    };

    // 1. Navigation Alignment & Spacing
    const nav = document.querySelector('.nav');
    if (nav) {
      const cs = window.getComputedStyle(nav);
      const links = [...nav.querySelectorAll('a')];
      // Check link height and alignment
      links.forEach((a, idx) => {
        const r = a.getBoundingClientRect();
        if (r.height < 15) {
          add('HIGH', 'Typography', 'Top Nav', `.nav a:nth-child(${idx+1})`, `Nav link height too small (${r.height}px)`, { text: a.textContent });
        }
      });
      // Check z-index conflict with scroll progress
      const pb = document.querySelector('#progressBar');
      if (pb) {
        const navZ = parseInt(cs.zIndex) || 0;
        const pbZ = parseInt(window.getComputedStyle(pb).zIndex) || 0;
        if (pbZ > navZ) {
          add('MEDIUM', 'Visual Layering', 'Progress Bar & Nav', '#progressBar', `Progress bar z-index (${pbZ}) sits on top of sticky nav border/content (${navZ})`, { navZ, pbZ });
        }
      }
    }

    // 2. Hero Section Alignment & Spacing
    const heroMeta = document.querySelector('.hero .meta');
    if (heroMeta) {
      const children = [...heroMeta.children];
      const ys = children.map(c => Math.round(c.getBoundingClientRect().y));
      const allSameY = ys.every(y => y === ys[0]);
      if (!allSameY) {
        add('HIGH', 'Alignment / Layout', 'Hero Metadata Strip', '.hero .meta', 'Hero metadata items wrap awkwardly onto multiple lines at 1440px viewport', { ys });
      }
    }

    // 3. Verdict Section Negative Margin & Padding Hierarchy
    const verdict = document.querySelector('.verdict');
    if (verdict) {
      const vCs = window.getComputedStyle(verdict);
      if (vCs.marginTop.includes('-')) {
        add('MEDIUM', 'Whitespace / Rhythm', 'Executive Verdict Card', '.verdict', `Uses raw negative margin (${vCs.marginTop}) creating fragile section overlap`, { margin: vCs.marginTop });
      }
    }

    // 4. Staggered Pipeline Heights in Architecture Flow
    const routeNodes = [...document.querySelectorAll('.route-node')];
    if (routeNodes.length > 0) {
      const heights = routeNodes.map(n => Math.round(n.getBoundingClientRect().height));
      const tops = routeNodes.map(n => Math.round(n.getBoundingClientRect().top));
      const minH = Math.min(...heights);
      const maxH = Math.max(...heights);
      if (maxH - minH > 15) {
        add('HIGH', 'Alignment & Visual Rhythm', 'Architecture Pipeline Flow', '.uncanny-route-flow .route-node', `Pipeline stage cards have severely uneven heights (${minH}px to ${maxH}px) causing jagged top/bottom borders across the flow`, { heights, tops });
      }
    }

    // 5. Product Journey Grid Layout Gap / Asymmetrical Padding
    const usecaseCards = [...document.querySelectorAll('.usecase-card')];
    usecaseCards.forEach((card, idx) => {
      const aside = card.querySelector('aside');
      if (aside) {
        const cardH = card.getBoundingClientRect().height;
        const asideH = aside.getBoundingClientRect().height;
        if (cardH - asideH > 40) {
          add('MEDIUM', 'Card Proportion & Whitespace', 'Wealth Advisory Usecase Card', `.usecase-card:nth-child(${idx+1})`, `Aside panel inside usecase card leaves empty dead space at the bottom (card height ${Math.round(cardH)}px vs aside ${Math.round(asideH)}px)`, { cardH, asideH });
        }
      }
    });

    // 6. Font Size Scale Inconsistencies (< 11px)
    const tinyElements = [];
    document.querySelectorAll('*').forEach(el => {
      if (el.children.length === 0 && el.textContent.trim().length > 0) {
        const fs = parseFloat(window.getComputedStyle(el).fontSize);
        if (fs < 11) {
          tinyElements.push({ selector: el.className ? `.${el.className.split(' ').join('.')}` : el.tagName.toLowerCase(), text: el.textContent.trim().slice(0, 30), fs });
        }
      }
    });
    if (tinyElements.length > 0) {
      add('HIGH', 'Typography', 'Microtext Scale', 'multiple (.proof-badge, .journey-tags span, .sim-results span, .model-price-note, etc.)', `${tinyElements.length} elements use sub-legible 9px-10px microtext violating standard 12px+ executive typography scale`, { count: tinyElements.length, sample: tinyElements.slice(0, 8) });
    }

    // 7. Color Palette & Border Color Fragmentation
    const borderColors = new Set();
    document.querySelectorAll('*').forEach(el => {
      const bc = window.getComputedStyle(el).borderColor;
      if (bc && bc !== 'rgba(0, 0, 0, 0)' && bc !== 'transparent') {
        borderColors.add(bc);
      }
    });
    if (borderColors.size > 8) {
      add('MEDIUM', 'Visual Polish & Consistency', 'Border Palette', 'CSS root / component rules', `Component borders use ${borderColors.size} different border color variations (#333336, #2c2c2e, #3a3a3c, rgba(255,255,255,0.1), #d2d2d7, #164f7d, #0071e3, etc.), breaking unified design system tokens`, { count: borderColors.size, colors: [...borderColors].slice(0, 10) });
    }

    // 8. Model Card Grid Heights & Metrics Box
    const modelCards = [...document.querySelectorAll('.model-card')];
    if (modelCards.length > 0) {
      for (let i = 0; i < modelCards.length; i += 2) {
        if (modelCards[i+1]) {
          const h1 = Math.round(modelCards[i].getBoundingClientRect().height);
          const h2 = Math.round(modelCards[i+1].getBoundingClientRect().height);
          if (Math.abs(h1 - h2) > 20) {
            add('HIGH', 'Card Alignment', 'Model Card Grid Row', `.model-cards-grid .model-card:nth-child(${i+1})`, `Paired model cards in grid row ${Math.floor(i/2)+1} have mismatched heights (${h1}px vs ${h2}px)`, { card1: h1, card2: h2 });
          }
        }
      }
    }

    // 9. Workflow Control-Flow DAG Steps Alignment
    const dagSteps = [...document.querySelectorAll('.dag-step')];
    dagSteps.forEach((step, idx) => {
      const badge = step.querySelector('span');
      const title = step.querySelector('strong');
      if (badge && title) {
        const bR = badge.getBoundingClientRect();
        const tR = title.getBoundingClientRect();
        if (Math.abs(bR.y - tR.y) > 4) {
          add('LOW', 'Alignment', 'DAG Step Header', `.dag-step:nth-child(${idx+1})`, `Step number badge and title text are vertically misaligned`, { badgeY: bR.y, titleY: tR.y });
        }
      }
    });

    // 10. Financial Simulator Input Controls & Select Styling
    const simSelects = [...document.querySelectorAll('#simulator select')];
    simSelects.forEach((sel, idx) => {
      const cs = window.getComputedStyle(sel);
      if (cs.backgroundColor === 'rgb(0, 0, 0)' || cs.backgroundColor === 'rgba(0, 0, 0, 0)') {
        add('MEDIUM', 'Visual Consistency', 'Simulator Select Boxes', `#simulator select:nth-child(${idx+1})`, `Simulator selects use pitch black background (#000) while other section inputs use dark gray (#1c1c1e)`, { bg: cs.backgroundColor });
      }
    });

    // 11. Public Proof Details Box Styling Inconsistency
    const proofDetails = [...document.querySelectorAll('.review-grid details')];
    proofDetails.forEach((dt, idx) => {
      const cs = window.getComputedStyle(dt);
      if (cs.backgroundColor === 'rgb(255, 255, 255)') {
        add('HIGH', 'Theme Inconsistency / Visual Rhythm', 'Public Proof Details Box', `.review-grid details:nth-child(${idx+1})`, `Proof detail cards abruptly render with stark white background (#fff) and dark border (#d2d2d7) in an otherwise dark-themed section`, { bg: cs.backgroundColor, border: cs.borderColor });
      }
    });

    return list;
  });

  console.log(JSON.stringify(findings, null, 2));
  await browser.close();
})();
