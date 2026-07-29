from shell import *
from graphics import GFX_CSS

EXTRA_CSS = """
.wiz-shell{max-width:780px;margin:0 auto}
.numgrid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:620px){.numgrid{grid-template-columns:1fr}}
.res-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:22px 0}
@media(max-width:640px){.res-grid{grid-template-columns:1fr}}
.res-tile{border:1px solid var(--line);border-radius:13px;padding:18px;background:rgba(255,255,255,.03);text-align:center}
.res-tile .t{font-size:.71rem;letter-spacing:.12em;text-transform:uppercase;color:var(--dim);font-weight:700}
.res-tile .v{font-family:'Sora',sans-serif;font-size:1.75rem;font-weight:750;letter-spacing:-.03em;margin-top:6px;line-height:1}
.lever{display:flex;gap:13px;align-items:flex-start;padding:14px 0;border-bottom:1px dashed rgba(255,255,255,.07)}
.lever:last-child{border-bottom:none}
.lever .b{width:26px;height:26px;border-radius:7px;background:rgba(23,227,155,.12);color:var(--acc);display:grid;place-items:center;flex:none;font-weight:700;font-size:.78rem;margin-top:2px}
.lever div p{margin:0;font-size:.93rem}
.lever div b{display:block;font-size:.97rem;margin-bottom:2px}
.adjbox{border-radius:12px}
.adjbox summary{padding:14px 18px;font-size:.92rem;font-family:'Inter',sans-serif;font-weight:600}
.adjbox .body{padding:0 18px 8px}
.adjbox .field{margin-bottom:14px}
"""

BODY = f"""
<section class="sec" style="padding:66px 0 40px">
  <div class="wrap">
    <div class="wiz-shell">
      <div class="center rv" style="margin-bottom:36px">
        <div class="eyebrow"><span class="dot"></span>Scenario Check, 6 questions, no credit pull</div>
        <h1 style="font-size:clamp(2rem,4.4vw,3.1rem);margin-bottom:.3em">Does your deal pencil?</h1>
        <p class="lead center" style="margin:0 auto">Answer six questions and see your estimated DSCR, LTV, and an
        illustrative rate. Nothing is submitted anywhere. The math runs in your browser.</p>
      </div>

      <div class="panel" id="wizPanel">
        <div class="wiz-bar"><i id="bar"></i></div>
        <div class="wiz-meta"><span id="stepLbl">Step 1 of 6</span><span id="stepName">Your goal</span></div>

        <!-- 1 -->
        <div class="stepq on" data-s="1">
          <h2>What are you trying to do?</h2>
          <p class="qsub">This sets the leverage cap and the pricing tier.</p>
          <div class="opts">
            <button class="opt" data-k="goal" data-v="Purchase"><span class="oi">01</span><span>Buy a rental property<small>Acquisition, up to 80% LTV</small></span></button>
            <button class="opt" data-k="goal" data-v="Rate &amp; term refinance"><span class="oi">02</span><span>Refinance an existing loan<small>Rate and term, up to 75% LTV</small></span></button>
            <button class="opt" data-k="goal" data-v="Cash-out refinance"><span class="oi">03</span><span>Pull cash out of a property I own<small>Cash-out, 70-75% LTV</small></span></button>
          </div>
        </div>

        <!-- 2 -->
        <div class="stepq" data-s="2">
          <h2>What kind of property?</h2>
          <p class="qsub">Property type affects both the maximum LTV and the rate.</p>
          <div class="opts two">
            <button class="opt" data-k="ptype" data-v="Single-family rental"><span class="oi">&#9679;</span><span>Single-family<small>Detached or attached</small></span></button>
            <button class="opt" data-k="ptype" data-v="2-4 unit"><span class="oi">&#9679;</span><span>2-4 unit<small>Duplex, triplex, fourplex</small></span></button>
            <button class="opt" data-k="ptype" data-v="Condo / townhome"><span class="oi">&#9679;</span><span>Condo / townhome<small>Warrantable</small></span></button>
            <button class="opt" data-k="ptype" data-v="Short-term rental"><span class="oi">&#9679;</span><span>Short-term rental<small>Airbnb / VRBO / mid-term</small></span></button>
          </div>
        </div>

        <!-- 3 -->
        <div class="stepq" data-s="3">
          <h2>The numbers</h2>
          <p class="qsub">Estimates are fine. You can change them on the results screen.</p>
          <div class="numgrid">
            <div class="field">
              <label for="w_price">Purchase price or current value</label>
              <input type="number" id="w_price" value="320000" min="0" step="5000">
            </div>
            <div class="field">
              <label for="w_rent">Gross monthly rent</label>
              <input type="number" id="w_rent" value="2400" min="0" step="50">
              <div class="hint" id="rentHint">Actual lease, or expected market rent if vacant</div>
            </div>
          </div>
          <div class="field">
            <label for="w_down" id="downLbl">Down payment</label>
            <select id="w_down">
              <option value="20">20% down (80% LTV)</option>
              <option value="25" selected>25% down (75% LTV)</option>
              <option value="30">30% down (70% LTV)</option>
              <option value="35">35% down (65% LTV)</option>
              <option value="40">40% down (60% LTV)</option>
            </select>
          </div>
          <div class="field">
            <label for="w_hoa">Monthly HOA dues <span style="text-transform:none;letter-spacing:0;font-weight:400;color:var(--dim)">(optional)</span></label>
            <input type="number" id="w_hoa" value="0" min="0" step="10">
          </div>
        </div>

        <!-- 4 -->
        <div class="stepq" data-s="4">
          <h2>Roughly where is your credit?</h2>
          <p class="qsub">An estimate is fine. Nothing here pulls your credit.</p>
          <div class="opts two">
            <button class="opt" data-k="fico" data-v="760+" data-n="770"><span class="oi">A+</span><span>760 or higher<small>Best pricing tier</small></span></button>
            <button class="opt" data-k="fico" data-v="740-759" data-n="748"><span class="oi">A</span><span>740-759<small>Strong</small></span></button>
            <button class="opt" data-k="fico" data-v="720-739" data-n="728"><span class="oi">B+</span><span>720-739<small>Good</small></span></button>
            <button class="opt" data-k="fico" data-v="700-719" data-n="708"><span class="oi">B</span><span>700-719<small>Solid</small></span></button>
            <button class="opt" data-k="fico" data-v="680-699" data-n="688"><span class="oi">C+</span><span>680-699<small>Workable</small></span></button>
            <button class="opt" data-k="fico" data-v="660-679" data-n="668"><span class="oi">C</span><span>660-679<small>Qualifies</small></span></button>
            <button class="opt" data-k="fico" data-v="630-659" data-n="644"><span class="oi">D</span><span>630-659<small>Program floor</small></span></button>
            <button class="opt" data-k="fico" data-v="Below 630 / unsure" data-n="610"><span class="oi">?</span><span>Below 630 or not sure<small>Let's talk through options</small></span></button>
          </div>
        </div>

        <!-- 5 -->
        <div class="stepq" data-s="5">
          <h2>How soon do you need to close?</h2>
          <p class="qsub">Timeline changes what we prioritize on the file.</p>
          <div class="opts">
            <button class="opt" data-k="time" data-v="ASAP - under contract or bridge maturing"><span class="oi">&#9889;</span><span>As fast as possible<small>Under contract, or a bridge loan is maturing</small></span></button>
            <button class="opt" data-k="time" data-v="30-60 days"><span class="oi">&#128197;</span><span>Next 30-60 days<small>Actively working on it</small></span></button>
            <button class="opt" data-k="time" data-v="60-90 days"><span class="oi">&#128197;</span><span>60-90 days<small>Planning ahead</small></span></button>
            <button class="opt" data-k="time" data-v="Just researching"><span class="oi">&#128269;</span><span>Just researching<small>Learning how the numbers work</small></span></button>
          </div>
        </div>

        <!-- 6 -->
        <div class="stepq" data-s="6">
          <h2>How will you take title?</h2>
          <p class="qsub">Last question. Then you get your numbers.</p>
          <div class="opts">
            <button class="opt" data-k="vest" data-v="LLC or entity"><span class="oi">&#127970;</span><span>In an LLC or other entity<small>Standard for DSCR, personal guarantee applies</small></span></button>
            <button class="opt" data-k="vest" data-v="Personal name"><span class="oi">&#128100;</span><span>In my personal name<small>Also permitted</small></span></button>
            <button class="opt" data-k="vest" data-v="Not sure yet"><span class="oi">?</span><span>Haven't decided<small>We can walk through the trade-offs</small></span></button>
          </div>
        </div>

        <!-- RESULTS -->
        <div class="stepq" data-s="7">
          <div class="result-hero">
            <div class="pill-big" id="rPill">-</div>
            <div style="font-size:.75rem;letter-spacing:.13em;text-transform:uppercase;color:var(--dim);font-weight:650">Estimated DSCR</div>
            <div class="val mono" id="rDscr" style="font-family:'Sora',sans-serif;font-size:4.2rem;font-weight:800;letter-spacing:-.04em;line-height:1.05;margin:6px 0 6px">-</div>
            <div id="rVerdict" style="font-size:1.02rem;font-weight:600">&nbsp;</div>
          </div>

          <details class="acc adjbox" id="adjBox" style="margin-bottom:6px">
            <summary>Adjust the numbers</summary>
            <div class="body" style="padding-top:6px">
              <div class="numgrid">
                <div class="field"><label for="r_price">Price / value</label>
                  <input type="number" id="r_price" min="0" step="5000"></div>
                <div class="field"><label for="r_rent">Gross monthly rent</label>
                  <input type="number" id="r_rent" min="0" step="50"></div>
                <div class="field"><label for="r_down">Down payment / equity</label>
                  <select id="r_down">
                    <option value="20">20% (80% LTV)</option>
                    <option value="25">25% (75% LTV)</option>
                    <option value="30">30% (70% LTV)</option>
                    <option value="35">35% (65% LTV)</option>
                    <option value="40">40% (60% LTV)</option>
                  </select></div>
                <div class="field"><label for="r_hoa">Monthly HOA</label>
                  <input type="number" id="r_hoa" min="0" step="10"></div>
              </div>
            </div>
          </details>

          <div class="res-grid">
            <div class="res-tile"><div class="t">Loan amount</div><div class="v mono" id="rLoan">-</div></div>
            <div class="res-tile"><div class="t">LTV</div><div class="v mono" id="rLtv">-</div></div>
            <div class="res-tile"><div class="t">Illustrative rate</div><div class="v mono" id="rRate">-</div></div>
          </div>

          <div class="rows">
            <div class="row"><span>Estimated monthly PITIA</span><b class="mono" id="rPitia">-</b></div>
            <div class="row"><span>Estimated monthly cash flow</span><b class="mono" id="rCf">-</b></div>
            <div class="row"><span>Estimated cash to close (down payment)</span><b class="mono" id="rDown">-</b></div>
            <div class="row"><span>Reserves required (est.)</span><b class="mono" id="rRes">-</b></div>
          </div>

          <div style="margin-top:28px;padding-top:22px;border-top:1px solid var(--line)">
            <h3 style="font-size:1.08rem;margin-bottom:14px" id="leverTitle">What could move this</h3>
            <div id="levers"></div>
          </div>

          <div style="margin-top:28px;padding:22px;border-radius:14px;background:linear-gradient(155deg,rgba(23,227,155,.1),rgba(91,147,255,.07));border:1px solid var(--line2)">
            <h3 style="font-size:1.12rem;margin-bottom:8px">Get a real answer on this scenario</h3>
            <p style="font-size:.94rem;margin-bottom:18px">The number above is an estimate from public program
            parameters. A five-minute call turns it into an actual structure, with a written term sheet, no
            application fee, and no credit pull until you say go.</p>
            <div class="btn-row">
              <a class="btn btn-primary" href="tel:{PHONE_TEL}">{PHONE_ICO}Call {PHONE_DISPLAY}</a>
              <a class="btn btn-ghost" id="mailBtn" href="#">{MAIL_ICO}Email me this scenario</a>
            </div>
            <p style="font-size:.79rem;color:var(--dim);margin:16px 0 0">The email button opens your own mail app
            with the scenario details filled in. Nothing is sent or stored until you press send.</p>
          </div>

          <div class="assump" id="rAssump"></div>

          <div class="wiz-nav">
            <button class="btn btn-ghost btn-sm" id="btnEdit">&larr; Change my answers</button>
            <button class="btn btn-ghost btn-sm" id="btnRestart">Start over</button>
          </div>
        </div>

        <div class="wiz-nav" id="navRow">
          <button class="btn btn-ghost btn-sm" id="btnBack">&larr; Back</button>
          <button class="btn btn-primary btn-sm" id="btnNext">Continue &rarr;</button>
        </div>
      </div>

      <p class="disc center" style="max-width:70ch;margin:26px auto 0">{RATE_DISCLAIMER} This tool is an
      educational estimator, not an application, a pre-approval, or an underwriting decision.</p>
    </div>
  </div>
</section>

{CTA_BAND}
"""

WIZ_JS = r"""
(function(){
  var S={goal:'',ptype:'',fico:'',ficoN:0,time:'',vest:''};
  var cur=1, TOT=6;
  var NAMES={1:'Your goal',2:'Property type',3:'The numbers',4:'Credit',5:'Timeline',6:'Vesting',7:'Your results'};
  var $=function(id){return document.getElementById(id)};
  var qq=function(s){return document.querySelectorAll(s)};
  var money=function(n){return '$'+Math.round(n).toLocaleString('en-US')};

  function show(n){
    cur=n;
    qq('.stepq').forEach(function(el){el.classList.toggle('on', +el.dataset.s===n)});
    $('bar').style.width=(Math.min(n,TOT)/TOT*100)+'%';
    $('stepLbl').textContent = n>TOT ? 'Complete' : 'Step '+n+' of '+TOT;
    $('stepName').textContent=NAMES[n];
    $('navRow').style.display = n>TOT ? 'none' : 'flex';
    $('btnBack').style.visibility = n===1 ? 'hidden' : 'visible';
    $('btnNext').textContent = n===TOT ? 'See my numbers →' : 'Continue →';
    $('btnNext').style.display = (n===3) ? 'inline-flex' : (needsPick(n)&&!picked(n) ? 'inline-flex' : 'inline-flex');
    window.scrollTo({top:$('wizPanel').offsetTop-90,behavior:'smooth'});
    if(n>TOT){ pull(); render(); }
  }
  function needsPick(n){return n!==3}
  function picked(n){
    if(n===1)return !!S.goal; if(n===2)return !!S.ptype; if(n===4)return !!S.fico;
    if(n===5)return !!S.time; if(n===6)return !!S.vest; return true;
  }

  qq('.opt').forEach(function(b){
    b.addEventListener('click',function(){
      var k=b.dataset.k;
      b.parentNode.querySelectorAll('.opt').forEach(function(o){o.classList.remove('sel')});
      b.classList.add('sel');
      S[k]=b.dataset.v.replace(/&amp;/g,'&');
      if(k==='fico') S.ficoN=+b.dataset.n;
      if(k==='goal'){
        var isP = S.goal==='Purchase';
        $('downLbl').textContent = isP ? 'Down payment' : 'Equity position / target LTV';
      }
      if(k==='ptype'){
        $('rentHint').textContent = S.ptype==='Short-term rental'
          ? 'Average gross monthly revenue, we apply a 20% expense factor'
          : 'Actual lease, or expected market rent if vacant';
      }
      setTimeout(function(){ show(Math.min(cur+1, TOT+1)); }, 220);
    });
  });

  $('btnNext').addEventListener('click',function(){
    if(needsPick(cur)&&!picked(cur)){
      var box=document.querySelector('.stepq.on .opts');
      if(box){box.style.animation='none';box.offsetHeight;box.style.animation='fade .35s ease'}
      return;
    }
    show(Math.min(cur+1,TOT+1));
  });
  $('btnBack').addEventListener('click',function(){show(Math.max(cur-1,1))});
  $('btnEdit').addEventListener('click',function(){show(1)});
  $('btnRestart').addEventListener('click',function(){
    S={goal:'',ptype:'',fico:'',ficoN:0,time:'',vest:''};
    qq('.opt').forEach(function(o){o.classList.remove('sel')});
    show(1);
  });

  function ficoAdj(f){
    if(f>=760)return -0.125; if(f>=740)return 0; if(f>=720)return 0.125; if(f>=700)return 0.25;
    if(f>=680)return 0.45; if(f>=660)return 0.70; if(f>=630)return 1.00; return 1.40;
  }
  function dscrAdj(d){
    if(d>=1.5)return 0; if(d>=1.25)return 0.10; if(d>=1.0)return 0.30; if(d>=0.80)return 0.60; return 1.00;
  }
  function baseByLtv(l){ return l<=65?6.05 : l<=70?6.125 : l<=75?6.25 : 6.49; }
  function pmt(P,a,y){var i=a/100/12,n=y*12; return i===0?P/n:P*i/(1-Math.pow(1+i,-n));}

  function render(){
    var V=+$('w_price').value||0, R0=+$('w_rent').value||0, d=+$('w_down').value, hoa=+$('w_hoa').value||0;
    var isSTR = S.ptype==='Short-term rental';
    var R = isSTR ? R0*0.80 : R0;
    var ltv=100-d, L=V*ltv/100;
    var tax=V*0.011/12, ins=V*0.0055/12;

    var r=baseByLtv(ltv)+ficoAdj(S.ficoN||700)+0.30, pitia=0, dscr=0;
    for(var k=0;k<5;k++){
      pitia=pmt(L,r,30)+tax+ins+hoa;
      dscr= pitia>0 ? R/pitia : 0;
      r=baseByLtv(ltv)+ficoAdj(S.ficoN||700)+dscrAdj(dscr)
        + (isSTR?0.35:0) + (S.goal==='Cash-out refinance'?0.25:0);
    }
    var cf=R0-pitia;
    var resMonths = L>1500000 ? 6 : 2;

    $('rDscr').textContent=dscr.toFixed(2);
    $('rLoan').textContent=money(L);
    $('rLtv').textContent=ltv+'%';
    $('rRate').textContent=r.toFixed(3)+'%';
    $('rPitia').textContent=money(pitia)+'/mo';
    var cfEl=$('rCf'); cfEl.textContent=(cf<0?'-':'')+money(Math.abs(cf))+'/mo';
    cfEl.className='mono '+(cf>=0?'ok':'bad');
    $('rDown').textContent=money(V-L);
    $('rRes').textContent=money(pitia*resMonths)+' ('+resMonths+' mo)';

    // verdict
    var pill=$('rPill'), vd=$('rVerdict'), dEl=$('rDscr');
    var lowFico = (S.ficoN&&S.ficoN<630);
    var cls,txt,pl,pbg;
    if(lowFico){cls='bad';txt='Credit is the constraint here, not the property. Worth a call, there are paths.';pl='Needs a conversation';}
    else if(dscr>=1.25){cls='ok';txt='Strong. This lands in the best pricing tier available.';pl='Looks strong';}
    else if(dscr>=1.0){cls='ok';txt='Qualifies. This clears the standard 1.00 threshold.';pl='Likely qualifies';}
    else if(dscr>=0.80){cls='warn';txt='Close. Workable at reduced LTV with 660+ credit, or restructure to lift the ratio.';pl='Workable with adjustments';}
    else {cls='bad';txt='Below program thresholds as structured. More equity or a no-ratio program is the usual fix.';pl='Needs restructuring';}
    dEl.className='val mono '+cls; vd.className=cls; vd.textContent=txt;
    pill.textContent=pl; pill.className='pill-big';
    var col = cls==='ok'?['rgba(23,227,155,.14)','#17E39B']:cls==='warn'?['rgba(245,193,91,.14)','#1A3796']:['rgba(255,107,138,.14)','#FF6B8A'];
    pill.style.background=col[0]; pill.style.color=col[1]; pill.style.border='1px solid '+col[0].replace('.14','.35');

    // levers
    var lv=[];
    if(dscr<1.25){
      var need=1.0, needP=R/need;
      var pi=pmt(L,r,30);
      var targetPI=needP-tax-ins-hoa;
      if(dscr<1.0 && targetPI>0){
        var lo=0,hi=L,mid;
        for(var j=0;j<40;j++){mid=(lo+hi)/2; if(pmt(mid,r,30)>targetPI) hi=mid; else lo=mid;}
        var newLtv=Math.max(0,Math.floor(mid/V*100));
        lv.push(['1','Put more down','Roughly '+newLtv+'% LTV ('+money(V-mid)+' down) brings the ratio to about 1.00 at this rate.']);
      }
      var ioPitia=L*(r/100/12)+tax+ins+hoa;
      var ioD= ioPitia>0? R/ioPitia : 0;
      lv.push(['2','Interest-only structure','An I/O period drops the payment to about '+money(ioPitia)+'/mo, lifting DSCR to roughly '+ioD.toFixed(2)+'.']);
    }
    if(isSTR) lv.push(['3','Compare the long-term number','Short-term revenue takes a 20% expense haircut and a rate premium. Sometimes a 12-month lease qualifies better even at lower gross rent.']);
    if(S.ficoN&&S.ficoN<720) lv.push(['4','Credit tier','Moving up one FICO bracket is typically worth 0.10-0.25% on rate, which feeds straight back into the ratio.']);
    if(S.goal==='Cash-out refinance') lv.push(['5','Rate and term instead','If you don\'t need the cash, a straight rate-and-term refinance prices roughly 0.25% better and allows higher LTV.']);
    if(dscr>=1.25) lv.push(['1','Consider more leverage','With this much coverage you may be able to take a higher LTV and keep the ratio above 1.00, leaving more capital for the next deal.']);
    if(L<150000) lv.push(['x','Loan size is under the program floor','This program starts at $150,000 and your loan comes to '
      +money(L)+'. A smaller down payment, a higher-priced property, or a different product would be the fix. Worth a call either way.']);
    if(L>2000000) lv.push(['x','Above the standard ceiling','The standard band tops out at $2,000,000 and your loan comes to '
      +money(L)+'. Larger files are reviewed case by case, usually with more reserves and a tighter LTV.']);
    lv.push([String(lv.length+1),'Shorter prepay','If you plan to sell or refinance within two years, ask for a reduced prepayment period. It costs rate but can save far more at exit.']);

    $('levers').innerHTML=lv.map(function(x,i){
      return '<div class="lever"><div class="b">'+(i+1)+'</div><div><b>'+x[1]+'</b><p>'+x[2]+'</p></div></div>';
    }).join('');

    $('rAssump').textContent='Assumes a 30-year fixed amortization, property taxes at 1.1% and insurance at 0.55% '
      +'of value per year, HOA as entered'+(isSTR?', and a 20% expense factor applied to short-term rental revenue':'')
      +'. Illustrative rate built from published program parameters as of """ + RATES_AS_OF + r"""; it is not a quote, '
      +'a lock, or a commitment to lend.';

    // mailto
    var body=
      'Hi, I ran a scenario on your site and would like a real quote.\n\n'+
      'GOAL: '+(S.goal||'n/a')+'\n'+
      'PROPERTY TYPE: '+(S.ptype||'n/a')+'\n'+
      'PRICE / VALUE: '+money(V)+'\n'+
      'GROSS MONTHLY RENT: '+money(R0)+(isSTR?' (short-term gross)':'')+'\n'+
      'DOWN PAYMENT / EQUITY: '+d+'%  (LTV '+ltv+'%)\n'+
      'MONTHLY HOA: '+money(hoa)+'\n'+
      'CREDIT BAND: '+(S.fico||'n/a')+'\n'+
      'TIMELINE: '+(S.time||'n/a')+'\n'+
      'VESTING: '+(S.vest||'n/a')+'\n\n'+
      '--- ESTIMATE FROM YOUR CALCULATOR ---\n'+
      'Loan amount: '+money(L)+'\n'+
      'Estimated DSCR: '+dscr.toFixed(2)+'\n'+
      'Illustrative rate: '+r.toFixed(3)+'%\n'+
      'Estimated PITIA: '+money(pitia)+'/mo\n'+
      'Estimated cash flow: '+(cf<0?'-':'')+money(Math.abs(cf))+'/mo\n\n'+
      'Property address: \nBest time to reach me: \nMy name: \nMy phone: \n';
    $('mailBtn').href='mailto:__EMAIL__?subject='+encodeURIComponent('DSCR scenario: '+(S.goal||'inquiry')+', '+money(V))
      +'&body='+encodeURIComponent(body);
  }

  // two-way sync between the step-3 inputs and the results-screen adjuster
  var PAIRS=[['w_price','r_price'],['w_rent','r_rent'],['w_down','r_down'],['w_hoa','r_hoa']];
  function pull(){ PAIRS.forEach(function(p){ $(p[1]).value=$(p[0]).value }); }
  PAIRS.forEach(function(p){
    $(p[1]).addEventListener('input',function(){ $(p[0]).value=$(p[1]).value; render(); });
    $(p[1]).addEventListener('change',function(){ $(p[0]).value=$(p[1]).value; render(); });
  });
  show(1);
})();
""".replace("__EMAIL__", EMAIL)

HTML = page(
    f"Check My DSCR Numbers: Free Scenario Calculator | {BRAND}",
    "Answer six questions and see your estimated DSCR, LTV, illustrative rate, monthly PITIA, and cash "
    "flow. No credit pull, no signup, nothing submitted. Runs entirely in your browser.",
    "qualify.html", BODY, WIZ_JS, EXTRA_CSS + GFX_CSS,
)
