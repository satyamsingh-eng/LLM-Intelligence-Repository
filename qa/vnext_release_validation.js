const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const {pathToFileURL}=require('url');
const ROOT=path.resolve(__dirname,'..');
const BASE='http://127.0.0.1:8920/index.html?v=release-vnext';
const out={generated_at:new Date().toISOString(),pass:0,total:0,errors:[],results:[]};
function check(name,ok,detail=null){out.total++;if(ok)out.pass++;else out.errors.push(name+(detail?`: ${JSON.stringify(detail)}`:''));out.results.push([name,!!ok,detail]);}
async function suite(browser,label,viewport,url=BASE,blockNetwork=false){
 const page=await browser.newPage({viewport});const consoleErrors=[];const pageErrors=[];page.on('console',m=>{if(m.type()==='error')consoleErrors.push(m.text())});page.on('pageerror',e=>pageErrors.push(e.message));
 if(blockNetwork)await page.route(/^https?:\/\//,route=>route.abort());
 await page.goto(url,{waitUntil:'networkidle',timeout:60000});
 await page.waitForSelector('.model-card',{timeout:30000});
 check(`${label}: runtime loaded`,await page.locator('#runtimeError').isHidden());
 const runtime=JSON.parse(fs.readFileSync(path.join(ROOT,'models','executive_report_runtime.json'),'utf8'));
 const journeyCount=runtime.routing.journeys.length;
 const agentCount=new Set(runtime.routing.journeys.flatMap(j=>j.agents||[])).size;
 check(`${label}: wealth-journey KPI is data-driven`,await page.locator('#journeyKpi').innerText()===String(journeyCount));
 check(`${label}: domain-agent KPI is data-driven`,await page.locator('#agentKpi').innerText()===String(agentCount));
 check(`${label}: no console errors`,consoleErrors.length===0,consoleErrors);
 check(`${label}: no page errors`,pageErrors.length===0,pageErrors);
 const labels=await page.locator('.section-label').allTextContents();for(let i=1;i<=8;i++)check(`${label}: Section ${i} present`,labels.some(x=>x.trim()===`Section ${i}`),labels);
 check(`${label}: Section 9 absent`,!labels.some(x=>x.trim()==='Section 9'));
 check(`${label}: old PDF taxonomy absent`,!(await page.locator('body').innerText()).includes('Scanned / Image PDF'));
 check(`${label}: verified client accounts present`,await page.locator('#wealth-use-cases table tbody tr').count()>=6);
 check(`${label}: sales enablement playbook present`,(await page.locator('#wealth-use-cases').innerText()).includes('SALES ENABLEMENT & CLIENT PITCH GUIDE'));
 check(`${label}: 3 architecture journey controls`,await page.locator('[data-route-mode]').count()===3);
 check(`${label}: 4 architecture roles`,await page.locator('.uncanny-role-card').count()===4);
 check(`${label}: deterministic controls visible`,(await page.locator('#routing-capability').innerText()).includes('Deterministic'));
 check(`${label}: advisor approval visible`,/advisor approval/i.test(await page.locator('#routing-capability').innerText()));
 check(`${label}: 24 unique model cards`,await page.locator('.model-card').count()===24);
 const runtimeState=await page.evaluate(()=>({configs:models.reduce((n,m)=>n+m.configurationCount,0)}));check(`${label}: 40 benchmark configurations`,runtimeState.configs===40,runtimeState);
 check(`${label}: 4 charts`,await page.locator('#charts canvas').count()===4);
 check(`${label}: 4 accessible chart tables`,await page.locator('#charts .chart-table-wrap table').count()===4);
 const canvasSizes=await page.locator('#charts canvas').evaluateAll(xs=>xs.map(x=>({w:x.clientWidth,h:x.clientHeight})));check(`${label}: chart canvases have dimensions`,canvasSizes.every(x=>x.w>100&&x.h>200),canvasSizes);
 const chartTables=await page.locator('#charts .chart-table-wrap tbody').evaluateAll(xs=>xs.map(x=>x.querySelectorAll('tr').length));check(`${label}: chart tables populated`,chartTables.every(x=>x>0),chartTables);
 check(`${label}: chart boundaries disclosed`,await page.locator('#charts .chart-boundary').count()===4 && (await page.locator('#charts .chart-boundary').allTextContents()).every(x=>x.trim().length>40));
 check(`${label}: price chart table populated`,await page.locator('#priceTable tbody tr').count()===25);
 check(`${label}: workflow choices >= 3`,await page.locator('#wfSelect option').count()>=3);
 for(const [key,count] of [['relationship',7],['portfolio',8],['operations',7]]){await page.selectOption('#wfSelect',key);check(`${label}: ${key} control-flow stage count`,await page.locator('#dagContainer .dag-step').count()===count);}
 const wfText=await page.locator('#workflows').innerText();check(`${label}: workflow telemetry labelled with step costing`,wfText.includes('Verified Model Rates & Token Breakdown') || wfText.includes('Step Costing & Telemetry'));
 await page.selectOption('#wfSelect','relationship');await page.selectOption('#simSpeed','400');await page.click('#btnPlay');await page.waitForFunction(()=>document.getElementById('wfStatus').textContent==='Scenario complete',{timeout:8000});check(`${label}: workflow playback completes`,await page.locator('#wfStatus').innerText()==='Scenario complete');
 check(`${label}: calculator has 25 catalog models`,await page.locator('#simModelA option').count()===25&&await page.locator('#simModelB option').count()===25);
 check(`${label}: calculator formula boundary`,(await page.locator('#simulator').innerText()).includes('Model-specific context and pricing tiers are enforced'));
 await page.selectOption('#simModelA','gemini-3-5-flash-lite');await page.selectOption('#simModelB','kimi-k2-6');await page.locator('#simInTok').evaluate((e)=>{e.value='75000'});await page.locator('#simOutTok').evaluate((e)=>{e.value='8000'});await page.locator('#simRuns').evaluate((e)=>{e.value='10000'});await page.evaluate(()=>{updateLabels();runSim()});check(`${label}: calculator known Model A per-run display`,await page.locator('#costA').innerText()==='₹4.10',await page.locator('#costA').innerText());check(`${label}: calculator known Model B per-run display`,await page.locator('#costB').innerText()==='₹9.97',await page.locator('#costB').innerText());
 check(`${label}: FX basis visible`,/ECB 2026-07-24/.test(await page.locator('#fxBasis').innerText()));
 const body=await page.locator('body').innerText();check(`${label}: no Live telemetry label`,!/(^|\n)Live(\n|$)/.test(body));check(`${label}: no unsupported 100% Zero-Defect`,!body.includes('100% Zero-Defect'));check(`${label}: no fabricated margin recovery`,!body.includes('Margin Recovery'));
 const overflow=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth}));check(`${label}: no page horizontal overflow`,overflow.scroll<=overflow.client+1,overflow);
 const brokenAnchors=await page.evaluate(()=>[...document.querySelectorAll('a[href^="#"]')].map(a=>a.getAttribute('href')).filter(h=>h!=='#'&&!document.querySelector(h)));check(`${label}: no broken internal anchors`,brokenAnchors.length===0,brokenAnchors);
 const badExternal=await page.evaluate(()=>[...document.querySelectorAll('a[href^="http"]')].filter(a=>a.target!=='_blank'||!a.rel.split(/\s+/).includes('noopener')).map(a=>a.href));check(`${label}: external links use noopener`,badExternal.length===0,badExternal);
 const unnamed=await page.evaluate(()=>[...document.querySelectorAll('button,select,input')].filter(e=>{if(e.tagName==='INPUT'&&e.type==='hidden')return false;const id=e.id;const labelled=id&&document.querySelector(`label[for="${id}"]`);return !(e.getAttribute('aria-label')||e.getAttribute('aria-labelledby')||labelled||e.closest('label')||e.textContent.trim())}).map(e=>e.outerHTML.slice(0,120)));check(`${label}: controls have accessible names`,unnamed.length===0,unnamed);
 if(label==='desktop'){
  await page.screenshot({path:path.join(ROOT,'qa','vnext-release-desktop.png'),fullPage:true});
  await page.click('.model-detail-btn');check('desktop: evidence modal opens',await page.locator('#evidenceModal').isVisible());await page.keyboard.press('Escape');check('desktop: Escape closes evidence modal',!(await page.locator('#evidenceModal').isVisible()));
 }
 if(label==='mobile')await page.screenshot({path:path.join(ROOT,'qa','vnext-release-mobile-390x844.png'),fullPage:true});
 if(label==='tablet')await page.screenshot({path:path.join(ROOT,'qa','vnext-release-tablet-768x1024.png'),fullPage:true});
 if(label==='file-direct')await page.screenshot({path:path.join(ROOT,'qa','file-mode-direct-open.png'),fullPage:true});
 if(label==='offline-file')await page.screenshot({path:path.join(ROOT,'qa','offline-file-mode.png'),fullPage:true});
 await page.close();
}
(async()=>{const browser=await chromium.launch({headless:true});try{await suite(browser,'desktop',{width:1440,height:1000});await suite(browser,'mobile',{width:390,height:844});await suite(browser,'tablet',{width:768,height:1024});const fileUrl=pathToFileURL(path.join(ROOT,'index.html')).href;await suite(browser,'file-direct',{width:1440,height:1000},fileUrl);await suite(browser,'offline-file',{width:1440,height:1000},fileUrl,true);const page=await browser.newPage();await page.goto(BASE,{waitUntil:'networkidle'});await page.emulateMedia({media:'print'});check('print: nav hidden',await page.locator('.nav').evaluate(e=>getComputedStyle(e).display)==='none');check('print: charts remain visible',await page.locator('#charts').isVisible());await page.pdf({path:path.join(ROOT,'qa','vnext-release-print.pdf'),format:'A4',printBackground:true});await page.close();}catch(e){out.errors.push(e.stack||String(e));}finally{await browser.close();out.pass=out.results.filter(x=>x[1]).length;fs.writeFileSync(path.join(ROOT,'qa','vnext_release_validation.json'),JSON.stringify(out,null,2));console.log(JSON.stringify({pass:out.pass,total:out.total,errors:out.errors},null,2));process.exit(out.errors.length?1:0);}})();
