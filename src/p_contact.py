from shell import *
from graphics import GFX_CSS

BODY = f"""
<section class="hero" style="padding:92px 0 72px">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <div class="eyebrow rv"><span class="dot"></span>Talk to a human</div>
        <h1 class="rv" style="max-width:14ch">Call. Or write. Both get answered.</h1>
        <p class="hero-sub rv">No contact form that disappears into a CRM, no chatbot, no "a specialist will
        reach out within 48 hours." A phone number and an inbox, both monitored by the person who will
        actually underwrite your scenario.</p>
        <div class="btn-row rv">
          <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
          <a class="btn btn-ghost btn-lg" href="mailto:{EMAIL}">{MAIL_ICO}{EMAIL}</a>
        </div>
      </div>

      <div class="panel rv">
        <h3 style="margin-bottom:20px">What to have ready</h3>
        <p style="font-size:.95rem">Five details turn a vague call into an indicative rate and structure:</p>
        <div class="kv">{CHECK}<div><strong>Property address</strong>, or at minimum the city and state</div></div>
        <div class="kv">{CHECK}<div><strong>Purchase price or estimated value</strong></div></div>
        <div class="kv">{CHECK}<div><strong>Monthly rent</strong>, actual lease or your expectation</div></div>
        <div class="kv">{CHECK}<div><strong>Approximate credit score</strong>, a range is fine</div></div>
        <div class="kv">{CHECK}<div><strong>Purchase, rate-and-term, or cash-out</strong></div></div>
        <div class="note" style="margin-top:24px;margin-bottom:0">Don't have all five? Call anyway. We can
        work from an address and a rough number.</div>
      </div>
    </div>
  </div>
</section>

<div class="hr"></div>

<section class="sec">
  <div class="wrap">
    <div class="grid g3">
      <div class="card rv">
        <div class="card-ico">{PHONE_ICO}</div>
        <h3>Phone</h3>
        <p style="margin-bottom:14px">Fastest path to an answer. Most scenario calls run five to ten minutes.</p>
        <a class="btn btn-primary btn-sm" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
        <p style="margin-top:16px;font-size:.86rem;color:var(--dim)">Monday-Friday, 8:00a-7:00p ET</p>
      </div>
      <div class="card rv">
        <div class="card-ico b">{MAIL_ICO}</div>
        <h3>Email</h3>
        <p style="margin-bottom:14px">Best for complex scenarios, multiple properties, or attaching a rent roll.</p>
        <a class="btn btn-ghost btn-sm" href="mailto:{EMAIL}?subject=DSCR%20scenario">{EMAIL}</a>
        <p style="margin-top:16px;font-size:.86rem;color:var(--dim)">Same-day reply on business days</p>
      </div>
      <div class="card rv">
        <div class="card-ico g"><svg width="21" height="21" viewBox="0 0 24 24" fill="none"><path d="M4 6.5A2.5 2.5 0 016.5 4h11A2.5 2.5 0 0120 6.5v11a2.5 2.5 0 01-2.5 2.5h-11A2.5 2.5 0 014 17.5v-11z" stroke="#1A3796" stroke-width="1.7"/><path d="M8 10h8M8 14h5" stroke="#1A3796" stroke-width="1.7" stroke-linecap="round"/></svg></div>
        <h3>Run it yourself first</h3>
        <p style="margin-bottom:14px">Answer six questions and see an estimated ratio, LTV, and indicative rate before you call.</p>
        <a class="btn btn-ghost btn-sm" href="qualify.html">Check my numbers &rarr;</a>
        <p style="margin-top:16px;font-size:.86rem;color:var(--dim)">No credit pull, no signup</p>
      </div>
    </div>
  </div>
</section>

<div class="hr"></div>

<section class="sec">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <span class="tag tag-acc">About</span>
        <h2 style="margin-top:18px">Built for one borrower type.</h2>
        <p>{BRAND} does one thing: rental-income qualified financing on 1-4 unit residential
        investment property. No primary residences, no commercial, no consumer refinances.</p>
        <p>That narrowness is the point. An investor calling a generalist shop spends the first twenty
        minutes explaining what a DSCR loan is and the next two weeks watching an underwriter ask for
        tax returns the program doesn't require. Here, the first question is the rent.</p>
        <p style="margin-bottom:0">Loans are originated through {CO_NAME}, NMLS {CO_NMLS}, a licensed
        residential mortgage lender.</p>
      </div>
      <div class="rv">
        <div class="panel">
          <div class="quote">"Tell me the address and the rent. I'll tell you in five minutes whether it
          works, and if it doesn't, exactly what would have to change."</div>
          <div class="who">{LO_NAME}, Loan Officer, NMLS {LO_NMLS}</div>
          <div style="border-top:1px solid var(--line);margin-top:24px;padding-top:22px">
            <div class="row"><span>Focus</span><b>DSCR / non-QM investor lending</b></div>
            <div class="row"><span>Property types</span><b>1-4 unit residential</b></div>
            <div class="row"><span>Coverage</span><b>{CITY_STATE}</b></div>
            <div class="row"><span>Typical close</span><b>2-4 weeks</b></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="hr"></div>

<section class="sec-tight sec">
  <div class="wrap">
    <div class="shead center rv"><h2>Common reasons people call</h2></div>
    <div class="grid g4">
      <div class="card rv"><h3 style="font-size:1.02rem">"My bridge matures in 45 days"</h3>
        <p style="font-size:.91rem;margin:0">Takeout financing before the hard money balloon comes due.</p></div>
      <div class="card rv"><h3 style="font-size:1.02rem">"They said too many properties"</h3>
        <p style="font-size:.91rem;margin:0">Agency counted your doors. We don't.</p></div>
      <div class="card rv"><h3 style="font-size:1.02rem">"My returns show a loss"</h3>
        <p style="font-size:.91rem;margin:0">Good accounting shouldn't cost you a loan.</p></div>
      <div class="card rv"><h3 style="font-size:1.02rem">"Is 0.95 DSCR dead?"</h3>
        <p style="font-size:.91rem;margin:0">Usually not. It's a structure question.</p></div>
    </div>
  </div>
</section>

{CTA_BAND}
"""

HTML = page(
    f"Contact: DSCR Loan Scenarios | {BRAND}",
    f"Call {PHONE_DISPLAY} or email {EMAIL} for a DSCR loan scenario review. No application fee, "
    "no credit pull to get indicative terms. Investment property financing only.",
    "contact.html", BODY, "", GFX_CSS,
)
