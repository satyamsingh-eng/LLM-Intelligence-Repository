const {chromium}=require('playwright');
const path=require('path');
const {pathToFileURL}=require('url');

const ROOT=path.resolve(__dirname,'..');
const FILE=pathToFileURL(path.join(ROOT,'index.html')).href;
let passed=0,failed=0;const failures=[];
function check(name,ok,detail=''){if(ok){passed++;console.log('PASS',name)}else{failed++;failures.push({name,detail});console.error('FAIL',name,detail)}}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));

(async()=>{
 const browser=await chromium.launch({headless:true});
 for(const [viewportName,viewport] of Object.entries({mobile:{width:390,height:844},tablet:{width:768,height:1024},desktop:{width:1440,height:1000}})){
  const page=await browser.newPage({viewport});const errors=[];
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(FILE,{waitUntil:'networkidle'});
  check(`${viewportName}: no JavaScript errors`,errors.length===0,errors.join(' | '));
  const layout=await page.evaluate(()=>({scroll:document.documentElement.scrollWidth,client:document.documentElement.clientWidth,section:!!document.querySelector('#workflows .workflow-shell'),calc:!!document.querySelector('#simulator #calcStatus')}));
  check(`${viewportName}: no horizontal overflow`,layout.scroll===layout.client,JSON.stringify(layout));
  check(`${viewportName}: Section 4 rendered`,layout.section);
  check(`${viewportName}: calculator rendered`,layout.calc);
  await page.close();
 }
 const page=await browser.newPage({viewport:{width:1440,height:1000}});const errors=[];
 page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});page.on('pageerror',e=>errors.push(String(e)));
 await page.goto(FILE,{waitUntil:'networkidle'});
 const text=await page.locator('body').innerText();
 for(const bad of ['₹4.487','26,200 tok','4.5 sec','₹9.038','35,000/mo','100% Zero-Defect Score','101 percent accuracy'])check(`removed unsupported value: ${bad}`,!text.includes(bad));
 check('Section 4 does not render repetitive telemetry tiles',await page.locator('#workflows .not-measured').count()===0);
 check('Section 4 states control-order purpose',text.includes('control order—not production execution quality'));
 check('Section 4 features accurate step and journey costing',text.includes('Verified Model Rates & Token Breakdown') || text.includes('Step Costing & Telemetry'));
 const options=await page.locator('#wfSelect option').allTextContents();
 check('includes core wealth-advisory journeys', options.includes('Client Relationship Intelligence') && options.includes('Portfolio & Market Intelligence') && options.includes('Compliance & Advisor Operations'));
 const expectedSteps={relationship:7,portfolio:8,operations:7};
 for(const [journey,count] of Object.entries(expectedSteps)){
  await page.selectOption('#wfSelect',journey);await page.evaluate(()=>resetSim());
  check(`${journey}: expected step count`,await page.locator('#dagContainer .dag-step').count()===count,String(await page.locator('#dagContainer .dag-step').count()));
  const facts=await page.evaluate(()=>['wfDecision','wfProductOwner','wfControlOwner','wfApprovalOwner','wfExitGate','wfReleaseGap'].map(id=>document.getElementById(id).textContent.trim()));
  check(`${journey}: decision rights are populated`,facts.every(Boolean),JSON.stringify(facts));
  check(`${journey}: reset is Ready`,await page.locator('#wfStatus').innerText()==='Ready');
  check(`${journey}: reset progress is zero`,await page.locator('#wfProgressTrack').getAttribute('aria-valuenow')==='0');
  check(`${journey}: reset stages are pending`,await page.locator('#dagContainer .dag-step[data-state="pending"]').count()===count);
  await page.selectOption('#simSpeed','400');await page.click('#btnPlay');
  await sleep((count+1)*430);
  check(`${journey}: scenario completes`,await page.locator('#wfStatus').innerText()==='Scenario complete',await page.locator('#wfStatus').innerText());
  check(`${journey}: progress is 100`,await page.locator('#wfProgressTrack').getAttribute('aria-valuenow')==='100');
  check(`${journey}: all gates are passed`,await page.locator('#dagContainer .dag-step.passed').count()===count);
  check(`${journey}: no active gate after completion`,await page.locator('#dagContainer .dag-step.active').count()===0);
  check(`${journey}: replay control appears`,await page.locator('#btnPlay').innerText()==='Replay scenario');
 }
 await page.selectOption('#wfSelect','relationship');await page.evaluate(()=>resetSim());await page.selectOption('#simSpeed','1500');await page.click('#btnPlay');await sleep(120);await page.click('#btnPause');
 check('pause changes state',await page.locator('#wfStatus').innerText()==='Paused');
 check('pause exposes Continue',await page.locator('#btnPlay').innerText()==='Continue');
 const pausedStep=await page.evaluate(()=>currentStep);await sleep(500);check('paused workflow does not advance',await page.evaluate(()=>currentStep)===pausedStep);
 await page.click('#btnPlay');check('Continue resumes one timer',await page.evaluate(()=>simInterval!==null));await page.evaluate(()=>resetSim());check('Reset clears interval',await page.evaluate(()=>simInterval===null));

 const presetCount=await page.locator('#simPreset option').count();check('calculator presets are runtime-driven',presetCount>=3,String(presetCount));
 async function setCalc(a,b,input,output,runs){await page.selectOption('#simModelA',a);await page.selectOption('#simModelB',b);await page.evaluate(({input,output,runs})=>{simInTok.value=input;simOutTok.value=output;simRuns.value=runs;updateLabels();runSim();},{input:String(input),output:String(output),runs:String(runs)});return page.evaluate(()=>({a:costA.textContent,b:costB.textContent,ma:lakhsA.textContent,mb:lakhsB.textContent,diff:savingsText.textContent,annual:annualSavings.textContent,status:calcStatus.textContent,error:calcStatus.classList.contains('error'),scopeA:rateScopeA.textContent,scopeB:rateScopeB.textContent}));}
 const defaults=await setCalc('gemini-3-5-flash-lite','kimi-k2-6',75000,8000,10000);
 check('default Gemini per-run cost is exact rounded output',defaults.a==='₹4.10',JSON.stringify(defaults));
 check('default Kimi per-run cost is exact rounded output',defaults.b==='₹9.97',JSON.stringify(defaults));
 check('default scenario is not blocked',!defaults.error,JSON.stringify(defaults));
 const qwenBase=await setCalc('qwen3-7-plus','deepseek-v4-pro',250000,5000,10000);check('Qwen ≤256K uses base pricing tier',qwenBase.scopeA.includes('≤ 256K'),qwenBase.scopeA);
 const qwenHigh=await setCalc('qwen3-7-plus','deepseek-v4-pro',260000,5000,10000);check('Qwen >256K uses higher pricing tier',qwenHigh.scopeA.includes('256K <'),qwenHigh.scopeA);
 const kimiBlocked=await setCalc('kimi-k2-6','deepseek-v4-pro',260000,5000,10000);check('Kimi over total context limit fails closed',kimiBlocked.error&&kimiBlocked.a==='Unavailable'&&kimiBlocked.status.includes('context tokens'),JSON.stringify(kimiBlocked));
 await page.evaluate(()=>{const o=document.createElement('option');o.value='unknown';o.textContent='Unknown';simModelA.appendChild(o);simModelA.value='unknown';runSim();});
 const unknown=await page.evaluate(()=>({a:costA.textContent,status:calcStatus.textContent,error:calcStatus.classList.contains('error')}));check('unknown model ID fails closed',unknown.a==='Unavailable'&&unknown.error&&unknown.status.includes('Unknown model identifier'),JSON.stringify(unknown));
 await page.evaluate(()=>{simModelA.value='gemini-3-5-flash-lite';simInTok.max='400000';simInTok.value='350000';runSim();simInTok.max='300000';});
 check('tampered out-of-range input fails closed',await page.locator('#calcStatus').evaluate(e=>e.classList.contains('error')&&e.textContent.includes('outside the validated')));
 check('calculator labels output as price difference, not savings',await page.locator('#simulator .section-label').filter({hasText:'Calculated price difference'}).count()===1);
 check('direct-file mode uses local Chart.js',await page.locator('script[src="./vendor/chart.umd.min.js"]').count()===1);
 check('direct-file mode uses local Decimal.js',await page.locator('script[src="./vendor/decimal.min.js"]').count()===1);
 check('no final JavaScript errors',errors.length===0,errors.join(' | '));
 await page.close();await browser.close();
 console.log(JSON.stringify({passed,failed,failures},null,2));if(failed)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
