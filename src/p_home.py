from shell import *
from graphics import (GFX_CSS, rent_vs_pitia, tier_meter, ltv_stack, doc_compare,
                      BRRRR_SVG, PROPERTY_ICONS, PROGRAM_ICONS)

BODY = f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="eyebrow rv"><span class="dot"></span>DSCR for Investment Property Only</div>
        <h1 class="rv">The property qualifies.<span class="br hl">Not your tax returns.</span></h1>
        <p class="hero-sub rv">DSCR loans underwrite the rent, not your W-2, your K-1s, or your
        debt-to-income ratio. If the lease covers the payment, you have a deal, whether it's
        your second door or your twenty-second.</p>
        <div class="btn-row rv">
          <a class="btn btn-primary btn-lg" href="qualify.html">Check my numbers &rarr;</a>
          <a class="btn btn-ghost btn-lg" href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
        </div>
        <div class="trust rv">
          <div>{CHECK} No tax returns or W-2s</div>
          <div>{CHECK} Close in an LLC</div>
          <div>{CHECK} No limit on properties owned</div>
          <div>{CHECK} 630+ FICO</div>
        </div>
      </div>

      <div class="panel rv" id="calc-panel">
        <div style="display:flex;align-items:center;justify-content:space-between;gap:14px;margin-bottom:20px">
          <div>
            <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.06rem">Does the deal pencil?</div>
            <div style="font-size:.83rem;color:var(--dim)">Move the numbers. Watch the ratio.</div>
          </div>
          <span class="tag tag-acc">Live</span>
        </div>

        <div class="field">
          <label for="h_rent">Monthly market rent</label>
          <input type="number" id="h_rent" value="2400" min="0" step="50">
        </div>
        <div class="grid g2" style="gap:14px">
          <div class="field">
            <label for="h_price">Price / value</label>
            <input type="number" id="h_price" value="320000" min="0" step="5000">
          </div>
          <div class="field">
            <label for="h_down">Down payment</label>
            <select id="h_down">
              <option value="20">20% down (80% LTV)</option>
              <option value="25" selected>25% down (75% LTV)</option>
              <option value="30">30% down (70% LTV)</option>
              <option value="35">35% down (65% LTV)</option>
            </select>
          </div>
        </div>

        <div class="readout" style="padding-top:10px;padding-bottom:14px;border-top:1px solid var(--line)">
          <div class="lbl">Estimated DSCR</div>
          <div class="val mono" id="h_dscr">-</div>
          <div class="verdict" id="h_verdict">&nbsp;</div>
        </div>
        <div class="rows">
          <div class="row"><span>Loan amount</span><b class="mono" id="h_loan">-</b></div>
          <div class="row"><span>Illustrative rate</span><b class="mono" id="h_rate">-</b></div>
          <div class="row"><span>Est. monthly PITIA</span><b class="mono" id="h_pitia">-</b></div>
          <div class="row"><span>Est. monthly cash flow</span><b class="mono" id="h_cf">-</b></div>
        </div>
        <div class="assump" id="h_assump"></div>
      </div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap"><div class="stats-in">
    <div class="stat rv"><b>630</b><span>Minimum qualifying FICO</span></div>
    <div class="stat rv"><b>80%</b><span>Max LTV on purchase</span></div>
    <div class="stat rv"><b>$150K-$2M</b><span>Loan amount range</span></div>
    <div class="stat rv"><b>0</b><span>Tax returns required</span></div>
  </div></div>
</section>

<!-- PROBLEM ---------------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead rv">
      <span class="tag tag-gold">The wall every investor hits</span>
      <h2 style="margin-top:18px">Conventional lending punishes you for doing this well.</h2>
      <p>Agency guidelines were written for people who buy one house and live in it. The better your
      portfolio performs, the worse you look on a Fannie Mae worksheet.</p>
    </div>
    <div class="grid g3">
      <div class="card rv">
        <div class="card-ico g"><svg width="21" height="21" viewBox="0 0 24 24" fill="none"><path d="M4 19V5a1 1 0 011-1h9l6 6v9a1 1 0 01-1 1H5a1 1 0 01-1-1z" stroke="#1A3796" stroke-width="1.7" stroke-linejoin="round"/><path d="M14 4v6h6M8 14h8M8 17h5" stroke="#1A3796" stroke-width="1.7" stroke-linecap="round"/></svg></div>
        <h3>Your write-offs work against you</h3>
        <p>Depreciation, repairs, mileage, cost segregation. Every deduction that saves you tax
        money shrinks the income a conventional underwriter is allowed to count. You get penalized
        twice for good accounting.</p>
      </div>
      <div class="card rv">
        <div class="card-ico b"><svg width="21" height="21" viewBox="0 0 24 24" fill="none"><path d="M3 21V9l6-4 6 4v12M9 21v-5h4v5" stroke="#5B93FF" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path d="M15 21V11l6 3v7" stroke="#5B93FF" stroke-width="1.7" stroke-linejoin="round"/></svg></div>
        <h3>The 10-property ceiling</h3>
        <p>Agency programs cap the number of financed properties, then stack reserve requirements on
        every single one. Investors routinely get told "no" not because a deal is weak, but because
        they already own too many good ones.</p>
      </div>
      <div class="card rv">
        <div class="card-ico"><svg width="21" height="21" viewBox="0 0 24 24" fill="none"><circle cx="12" cy="12" r="8.5" stroke="#17E39B" stroke-width="1.7"/><path d="M12 7v5.5l3.5 2" stroke="#17E39B" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <h3>Forty-five days you don't have</h3>
        <p>Full doc means two years of returns, all schedules, VOEs, transcript orders, letters of
        explanation, then a second condition list. Sellers with three offers don't wait for it, and
        hard-money bridges don't pause their clock for it.</p>
      </div>
    </div>
  </div>
</section>

<div class="hr"></div>

<!-- WHAT IS DSCR ----------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="tag tag-acc">The mechanic</span>
        <h2 style="margin-top:18px">One ratio decides it.</h2>
        <p>DSCR stands for <strong>Debt Service Coverage Ratio</strong>. It's a single number that asks
        one question: does the property's rent cover the property's payment?</p>
        <div class="panel" style="margin:26px 0;padding:26px;text-align:center;background:var(--off);box-shadow:none;border-left:3px solid var(--red)">
          <div style="font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);font-weight:700;margin-bottom:14px">The whole formula</div>
          <div class="dspl" style="font-size:1.32rem;font-weight:650">
            DSCR &nbsp;=&nbsp; <span class="hl">Gross monthly rent</span>
            <span style="color:var(--dim)"> &divide; </span>
            <span class="hl-n">Monthly PITIA</span>
          </div>
          <div style="font-size:.83rem;color:var(--dim);margin-top:14px">PITIA = principal, interest, taxes, insurance, and HOA dues</div>
        </div>
        <p>A <strong>1.25 DSCR</strong> means the rent covers the payment 1.25 times over, or $1.25 of
        rent for every $1.00 of debt service. Most programs price best at 1.00 and above, and options
        exist below 1.00 with a larger down payment.</p>
        <p style="margin-bottom:0">Your personal income never enters the calculation. Neither does your
        job, your DTI, or how many other doors you own.</p>
      </div>

      <div class="rv">
        {rent_vs_pitia()}
        <div class="note" style="margin-top:24px">A property that misses on DSCR isn't automatically dead.
        More often it's a structure problem: a bigger down payment, an interest-only period, or a
        no-ratio program moves it back into range.</div>
      </div>
    </div>

    <div class="grid g2 rv" style="margin-top:44px">
      {tier_meter()}
      {ltv_stack()}
    </div>
  </div>
</section>

<div class="hr"></div>

<!-- DOC COMPARE ------------------------------------------------------------>
<section class="sec sec-alt">
  <div class="wrap">
    <div class="shead center rv">
      <span class="tag tag-blue">Documentation</span>
      <h2 style="margin-top:18px">Ten items versus six</h2>
      <p>The difference is not a shortcut. It is a different question being asked.</p>
    </div>
    <div class="rv">{doc_compare()}</div>
    <p class="disc center rv" style="max-width:70ch;margin-left:auto;margin-right:auto">Representative
    document lists. Individual files vary by lender, property, and borrower profile.</p>
  </div>
</section>

<div class="hr"></div>

<!-- PROGRAMS --------------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead center rv">
      <span class="tag tag-blue">Programs</span>
      <h2 style="margin-top:18px">Six ways investors use this</h2>
      <p>Same underwriting logic, different jobs to be done.</p>
    </div>
    <div class="rv" style="margin-bottom:44px">{PROPERTY_ICONS}</div>
    <div class="grid g3">
      <a class="card rv" href="programs.html#purchase" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["purchase"]}</div>
        <span class="tag tag-acc">Purchase</span>
        <h3 style="margin-top:16px">Buy the next door</h3>
        <p>Up to 80% LTV on 1-4 unit residential. Close in an LLC, use the lease or a market-rent
        appraisal addendum, and skip the income documentation entirely.</p>
      </a>
      <a class="card rv" href="programs.html#rateterm" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["rateterm"]}</div>
        <span class="tag tag-acc">Rate &amp; term</span>
        <h3 style="margin-top:16px">Get off the bridge</h3>
        <p>Refinance out of hard money, a maturing balloon, or a private note into 30-year fixed
        permanent debt before the rate resets or the term runs out.</p>
      </a>
      <a class="card rv" href="programs.html#cashout" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["cashout"]}</div>
        <span class="tag tag-acc">Cash-out</span>
        <h3 style="margin-top:16px">Pull equity, keep the asset</h3>
        <p>Convert trapped appreciation into the down payment on the next two deals without selling
        and without a taxable event today.</p>
      </a>
      <a class="card rv" href="programs.html#str" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["str"]}</div>
        <span class="tag tag-blue">Short-term rental</span>
        <h3 style="margin-top:16px">Airbnb &amp; mid-term</h3>
        <p>Qualify on documented short-term revenue rather than a 12-month lease. Expect a modest
        rate premium and an expense haircut on gross receipts.</p>
      </a>
      <a class="card rv" href="programs.html#portfolio" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["portfolio"]}</div>
        <span class="tag tag-blue">Portfolio</span>
        <h3 style="margin-top:16px">Blanket several doors</h3>
        <p>Roll multiple rentals into one loan, one payment, one closing. Useful when you're
        consolidating scattered private notes or seasoned free-and-clear stock.</p>
      </a>
      <a class="card rv" href="programs.html#foreign" style="color:inherit;text-decoration:none">
        <div style="margin-bottom:16px">{PROGRAM_ICONS["foreign"]}</div>
        <span class="tag tag-gold">Foreign national</span>
        <h3 style="margin-top:16px">No U.S. credit history</h3>
        <p>Non-resident investors can finance U.S. rental property without a FICO score, using
        passport, visa status, and international credit references instead.</p>
      </a>
    </div>
    <div class="center" style="margin-top:38px">
      <a class="btn btn-ghost" href="programs.html">Full program details and eligibility matrix &rarr;</a>
    </div>
  </div>
</section>

<div class="hr"></div>

<!-- TERMS TABLE ------------------------------------------------------------>
<section class="sec">
  <div class="wrap">
    <div class="shead rv">
      <h2>Terms at a glance</h2>
      <p>General program parameters as of {RATES_AS_OF}. Individual files vary. These are the guardrails,
      not a quote.</p>
    </div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>Parameter</th><th>Typical range</th><th>Notes</th></tr></thead>
        <tbody>
          <tr><td>Minimum FICO</td><td>630</td><td>660 for sub-1.00 DSCR tiers; better pricing at 700, 720, 740+</td></tr>
          <tr><td>Max LTV, purchase</td><td>80%</td><td>Driven by FICO, DSCR, and loan size</td></tr>
          <tr><td>Max LTV, rate &amp; term</td><td>75%</td><td>Straight payoff of existing lien plus limited costs</td></tr>
          <tr><td>Max LTV, cash-out</td><td>70-75%</td><td>Small rate add-on typical</td></tr>
          <tr><td>Minimum DSCR</td><td>1.00</td><td>Sub-1.00 and no-ratio available at reduced LTV</td></tr>
          <tr><td>Loan amount</td><td>$150,000-$2,000,000</td><td>$150,000 floor; larger files reviewed case by case</td></tr>
          <tr><td>Property types</td><td>SFR, 2-4 unit, condo, townhome</td><td>Up to 5 acres; condotels and rural see reduced LTV</td></tr>
          <tr><td>Reserves</td><td>2 months PITIA</td><td>6 months on loans over $1.5M</td></tr>
          <tr><td>Vesting</td><td>LLC, LP, or corporation</td><td>Personal name also permitted</td></tr>
          <tr><td>Terms offered</td><td>30-yr fixed, ARMs, interest-only</td><td>40-year I/O available on many programs</td></tr>
          <tr><td>Prepayment penalty</td><td>0-5 years</td><td>Shorter or zero prepay trades for a higher rate; prohibited in some states</td></tr>
          <tr><td>Occupancy</td><td>Non-owner occupied only</td><td>Business-purpose loan, no primary residences</td></tr>
        </tbody>
      </table>
    </div>
    <p class="disc rv">{RATE_DISCLAIMER}</p>
  </div>
</section>

<div class="hr"></div>

<!-- PROCESS ---------------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead center rv">
      <span class="tag tag-acc">Process</span>
      <h2 style="margin-top:18px">Four steps, not forty</h2>
      <p>Most files clear in two to four weeks. Nobody asks you for a tax transcript.</p>
    </div>
    <div class="steps">
      <div class="step rv"><div class="n">01</div><h3>Scenario</h3>
        <p>Address, purchase price or value, and the rent. Five minutes on the phone or one email is
        enough to get an indicative rate and structure.</p></div>
      <div class="step rv"><div class="n">02</div><h3>Term sheet</h3>
        <p>You get the rate, the LTV, the payment, the prepay options, and the total cash to close in
        writing, before you spend a dollar on third-party reports.</p></div>
      <div class="step rv"><div class="n">03</div><h3>Appraisal &amp; docs</h3>
        <p>Appraisal with a rent schedule, entity documents, insurance binder, and two months of
        reserves. That's the file. No returns, no VOE, no DTI worksheet.</p></div>
      <div class="step rv"><div class="n">04</div><h3>Close</h3>
        <p>Underwriting, clear conditions, sign in your LLC. Then start the next one. The count
        of doors you own doesn't cap you here.</p></div>
    </div>
  </div>
</section>

<div class="hr"></div>

<!-- WHO IT'S FOR ----------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead rv">
      <h2>Who this is built for</h2>
      <p>If you recognize yourself in one of these, the conversation is short.</p>
    </div>
    <div class="grid g2">
      <div class="card rv">
        <h3>The investor agency turned down</h3>
        <p>You own eight, twelve, twenty doors. Your returns show a paper loss. Your last lender said
        "too many financed properties." Nothing about your portfolio is actually weak. It just
        doesn't fit a form built for homeowners.</p>
      </div>
      <div class="card rv">
        <h3>The BRRRR operator on a clock</h3>
        <p>You bought with hard money at 11-12%, rehabbed, tenanted. Now the bridge is maturing and
        the takeout has to happen. Cash-out DSCR at 70-75% is how you recycle the capital and start
        the next one.</p>
      </div>
      <div class="card rv">
        <h3>The self-employed buyer</h3>
        <p>1099, business owner, commission, or recently-changed structure. Your income is real and
        your bank statements prove it, but the last two years of returns don't tell a clean
        agency story. The property doesn't care.</p>
      </div>
      <div class="card rv">
        <h3>The first rental buyer</h3>
        <p>You've never done this before and you want to start without handing over your entire
        financial life. One door, 20-25% down, a lease that covers the payment, and a straight
        30-year fixed. It's a legitimate on-ramp, not an advanced play.</p>
      </div>
    </div>
  </div>
</section>

<div class="hr"></div>

<!-- BRRRR CYCLE ------------------------------------------------------------>
<section class="sec sec-alt">
  <div class="wrap">
    <div class="shead center rv">
      <span class="tag tag-acc">The loop</span>
      <h2 style="margin-top:18px">Where DSCR sits in the strategy</h2>
      <p>Most investors do not use this once. They use it as step four of a cycle they run again
      and again, because the refinance is what frees the capital for the next acquisition.</p>
    </div>
    <div class="gfx-card rv" style="padding:20px">{BRRRR_SVG}</div>
    <p class="disc center rv" style="max-width:66ch;margin-left:auto;margin-right:auto">Buy and rehab
    are typically financed with cash or short-term debt. Steps four and five are where permanent
    rental-income financing does the work.</p>
  </div>
</section>

<div class="hr"></div>

<!-- SCENARIOS -------------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead center rv">
      <span class="tag tag-blue">Worked examples</span>
      <h2 style="margin-top:18px">What the math actually looks like</h2>
      <p>Illustrative scenarios built from typical {RATES_AS_OF} parameters. Not offers, not quotes,
      just the shape of the arithmetic.</p>
    </div>
    <div class="grid g3">
      <div class="card rv">
        <span class="tag tag-acc">Purchase</span>
        <h3 style="margin-top:16px">$320K SFR, $2,400 rent</h3>
        <div class="row"><span>Down payment</span><b>25% ($80,000)</b></div>
        <div class="row"><span>Loan amount</span><b>$240,000</b></div>
        <div class="row"><span>Est. PITIA</span><b>~$1,920/mo</b></div>
        <div class="row"><span>DSCR</span><b class="ok">~1.25</b></div>
        <p style="margin-top:16px;font-size:.9rem">Comfortably in the standard tier. No income docs
        requested at any point in the file.</p>
      </div>
      <div class="card rv">
        <span class="tag tag-acc">Cash-out</span>
        <h3 style="margin-top:16px">BRRRR takeout, $410K ARV</h3>
        <div class="row"><span>Hard money payoff</span><b>$248,000</b></div>
        <div class="row"><span>New loan at 72% LTV</span><b>$295,000</b></div>
        <div class="row"><span>Cash to borrower</span><b class="ok">~$40,000</b></div>
        <div class="row"><span>Rate drop</span><b>11.5% &rarr; ~6.9%</b></div>
        <p style="margin-top:16px;font-size:.9rem">Payment falls by roughly half and the equity funds
        the down payment on deal number two.</p>
      </div>
      <div class="card rv">
        <span class="tag tag-gold">Tight ratio</span>
        <h3 style="margin-top:16px">$525K duplex, $3,300 rent</h3>
        <div class="row"><span>At 20% down</span><b class="warn">DSCR ~0.94</b></div>
        <div class="row"><span>At 30% down</span><b class="ok">DSCR ~1.07</b></div>
        <div class="row"><span>Or: interest-only</span><b class="ok">DSCR ~1.10</b></div>
        <p style="margin-top:16px;font-size:.9rem">Same property, three different answers. Structure is
        usually the lever, not the deal itself.</p>
      </div>
    </div>
    <p class="disc center rv">Scenarios are hypothetical illustrations using assumed taxes at 1.1% and
    insurance at 0.55% of value annually. Your figures will differ.</p>
  </div>
</section>

<div class="hr"></div>

<!-- FAQ -------------------------------------------------------------------->
<section class="sec">
  <div class="wrap">
    <div class="shead center rv"><h2>Straight answers</h2>
    <p>The questions that come up on nearly every first call.</p></div>
    <div class="acc rv" style="max-width:860px;margin:0 auto">
      <details open><summary>Do you really not look at my income?</summary><div class="body">
        <p>Correct. There's no tax return, no W-2, no pay stub, no employment verification, and no
        debt-to-income calculation. We verify identity, credit, assets for down payment and reserves,
        and the property's rental income. Your personal earnings are not part of the qualification.</p></div></details>
      <details><summary>What credit score do I need?</summary><div class="body">
        <p>630 is the general floor. Pricing improves meaningfully at 700, again at 720, and again at
        740+. Sub-1.00 DSCR tiers typically want 660 or better. Foreign nationals without U.S. credit
        can qualify through an alternate documentation path.</p></div></details>
      <details><summary>How much do I have to put down?</summary><div class="body">
        <p>Usually 20-25% on a purchase. Twenty percent down is possible with strong credit and a
        healthy ratio; a weaker ratio, a lower score, a short-term rental, or a smaller loan amount
        can push the requirement to 25-30%.</p></div></details>
      <details><summary>Can I close in my LLC?</summary><div class="body">
        <p>Yes, and most investors do. LLC, LP, and corporate vesting are all standard on DSCR
        programs. You'll typically sign a personal guarantee, and we'll need the operating agreement,
        articles, EIN letter, and a certificate of good standing.</p></div></details>
      <details><summary>Is there a limit on how many properties I can own?</summary><div class="body">
        <p>No. This is the single biggest reason investors move off agency financing. There's no
        financed-property count ceiling and no requirement to hold reserves against every unrelated
        door in your portfolio.</p></div></details>
      <details><summary>What if the property is vacant right now?</summary><div class="body">
        <p>Still workable. The appraiser completes a rent schedule (Form 1007) estimating market rent,
        and we can qualify off that figure. An executed lease is cleaner and sometimes prices better,
        but it is not a hard requirement on most programs.</p></div></details>
      <details><summary>How long does closing take?</summary><div class="body">
        <p>Two to four weeks is typical, with the appraisal usually the long pole. Because there's no
        income documentation to chase, files tend to move faster and stall less than comparable
        full-doc loans.</p></div></details>
      <details><summary>What's a prepayment penalty and can I avoid it?</summary><div class="body">
        <p>Most DSCR programs carry a prepay of one to five years. It is a fee if you pay off or
        refinance early. Shorter or zero prepay is available and is priced into the rate. If you plan
        to sell or refinance within a couple of years, say so up front so we structure for it. Prepays
        are prohibited outright in several states.</p></div></details>
      <details><summary>Do short-term rentals count?</summary><div class="body">
        <p>Yes, on programs that allow them. Qualification generally uses documented platform revenue
        or a short-term rent schedule, with roughly a 20% expense haircut applied to gross receipts,
        plus a rate premium versus a long-term lease.</p></div></details>
      <details><summary>What does it cost to find out where I stand?</summary><div class="body">
        <p>Nothing. A scenario review is a conversation, with no application fee and no credit pull
        until you've seen indicative terms in writing and want to move forward.</p></div></details>
    </div>
    <div class="center" style="margin-top:34px"><a class="btn btn-ghost" href="faq.html">Read the full FAQ &rarr;</a></div>
  </div>
</section>

{CTA_BAND}
"""

HOME_JS = r"""
(function(){
  var f=function(id){return document.getElementById(id)};
  var rent=f('h_rent'),price=f('h_price'),down=f('h_down');
  if(!rent) return;
  var money=function(n){return '$'+Math.round(n).toLocaleString('en-US')};

  function rateFor(ltv,dscr){
    var r = ltv<=70?6.125 : ltv<=75?6.25 : 6.49;      // base by LTV
    if(dscr>=1.5) r+=0; else if(dscr>=1.25) r+=0.10;
    else if(dscr>=1.0) r+=0.30; else if(dscr>=0.80) r+=0.60; else r+=1.00;
    return r;
  }
  function pmt(P,annual,yrs){
    var i=annual/100/12,n=yrs*12;
    if(i===0) return P/n;
    return P*i/(1-Math.pow(1+i,-n));
  }
  function calc(){
    var R=+rent.value||0, V=+price.value||0, d=+down.value;
    var ltv=100-d, L=V*ltv/100;
    var tax=V*0.011/12, ins=V*0.0055/12;
    // rate depends on dscr, dscr depends on rate -> two passes converge fine
    var r=rateFor(ltv,1.15), pitia=0, dscr=0;
    for(var k=0;k<4;k++){
      pitia=pmt(L,r,30)+tax+ins;
      dscr= pitia>0 ? R/pitia : 0;
      r=rateFor(ltv,dscr);
    }
    f('h_loan').textContent=money(L);
    f('h_rate').textContent=r.toFixed(3)+'%';
    f('h_pitia').textContent=money(pitia)+'/mo';
    var cf=R-pitia;
    var cfEl=f('h_cf');
    cfEl.textContent=(cf<0?'-':'')+money(Math.abs(cf))+'/mo';
    cfEl.className='mono '+(cf>=0?'ok':'bad');

    var dEl=f('h_dscr'), vEl=f('h_verdict');
    dEl.textContent=dscr.toFixed(2);
    if(dscr>=1.25){dEl.className='val mono ok';vEl.className='verdict ok';vEl.textContent='Strong, best pricing tier';}
    else if(dscr>=1.0){dEl.className='val mono ok';vEl.className='verdict ok';vEl.textContent='Qualifies, standard tier';}
    else if(dscr>=0.80){dEl.className='val mono warn';vEl.className='verdict warn';vEl.textContent='Workable, reduced LTV tier';}
    else {dEl.className='val mono bad';vEl.className='verdict bad';vEl.textContent='Needs restructuring: more down or no-ratio';}

    f('h_assump').textContent='Assumes 30-year fixed, taxes at 1.1% and insurance at 0.55% of value per year, '
      +'no HOA. Rate is an illustrative example as of """ + RATES_AS_OF + r""", not a quote or commitment to lend.';
  }
  [rent,price,down].forEach(function(el){el.addEventListener('input',calc);el.addEventListener('change',calc)});
  calc();
})();
"""

HTML = page(
    f"{BRAND} | DSCR Loans for Real Estate Investors, No Tax Returns",
    "DSCR rental property loans that qualify on the rent, not your tax returns. Up to 80% LTV, "
    "630+ FICO, LLC vesting, no limit on financed properties. Purchase, refinance, cash-out and STR.",
    "index.html", BODY, HOME_JS, GFX_CSS,
)
