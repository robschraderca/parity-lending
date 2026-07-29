from shell import *
from graphics import GFX_CSS, PROGRAM_ICONS, ltv_stack


def prog(pid, tag, tagcls, title, lede, bullets, table_rows, best_for):
    b = "".join(f'<div class="kv">{CHECK}<div>{x}</div></div>' for x in bullets)
    rows = "".join(f"<tr><td>{a}</td><td>{c}</td></tr>" for a, c in table_rows)
    return f"""<section class="sec" id="{pid}">
  <div class="wrap">
    <div class="split">
      <div class="rv">
        <div style="margin-bottom:14px">{PROGRAM_ICONS.get(pid,'')}</div>
        <span class="tag {tagcls}">{tag}</span>
        <h2 style="margin-top:18px">{title}</h2>
        <p class="lead">{lede}</p>
        <div style="margin:26px 0">{b}</div>
        <div class="note"><strong>Best for:</strong> {best_for}</div>
      </div>
      <div class="rv">
        <div class="tbl-wrap">
          <table style="min-width:auto">
            <thead><tr><th>Parameter</th><th>Typical</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>
        <div class="btn-row" style="margin-top:22px">
          <a class="btn btn-primary" href="qualify.html">Check this scenario &rarr;</a>
          <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{PHONE_ICO}Call</a>
        </div>
      </div>
    </div>
  </div>
</section>
<div class="hr"></div>"""


BODY = f"""
<section class="hero" style="padding:92px 0 76px">
  <div class="wrap">
    <div class="eyebrow rv"><span class="dot"></span>Loan Programs</div>
    <h1 class="rv" style="max-width:17ch">Six programs. One underwriting question.</h1>
    <p class="hero-sub rv" style="max-width:62ch">Every product below qualifies on the property's rental
    income rather than your personal income. What changes between them is the job you're hiring the
    loan to do, and the leverage and pricing that come with it.</p>
    <div class="btn-row rv">
      <a class="btn btn-primary btn-lg" href="qualify.html">Check my numbers &rarr;</a>
      <a class="btn btn-ghost btn-lg" href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
    </div>
  </div>
</section>

<div class="hr"></div>

{prog("purchase", "Program 01: Purchase", "tag-acc",
     "Acquisition financing on 1-4 unit rentals",
     "The core product. Buy a rental with 20-25% down, qualify on the lease or an appraiser's market "
     "rent estimate, and close in your entity. No returns, no DTI, no ceiling on how many you already own.",
     ["Up to 80% LTV with strong credit and a healthy ratio",
      "Vacant properties qualify off a Form 1007 rent schedule",
      "30-year fixed, ARM, and interest-only structures available",
      "LLC, LP, or corporate vesting with a personal guarantee",
      "Two months of PITIA in reserves is the standard requirement"],
     [("Max LTV", "80%"), ("Min FICO", "630"), ("Min DSCR", "1.00"),
      ("Loan amount", "$150K-$2M"), ("Reserves", "2 months PITIA"),
      ("Property types", "SFR, 2-4 unit, condo, townhome"), ("Occupancy", "Non-owner occupied")],
     "buy-and-hold investors adding doors, and first-time rental buyers who don't want to hand over "
     "two years of tax returns.")}

{prog("rateterm", "Program 02: Rate &amp; Term Refinance", "tag-acc",
     "Move off short-term debt before it moves you",
     "A straight payoff of your existing lien plus limited closing costs. Most commonly used to exit "
     "hard money, a maturing balloon, a private note, or an ARM that's about to reset.",
     ["Up to 75% LTV on rate and term",
      "Pays off the existing lien plus reasonable costs and prepaids",
      "No cash to the borrower beyond a small incidental amount",
      "Prices slightly better than a cash-out at the same LTV",
      "Seasoning requirements are generally light on stabilized property"],
     [("Max LTV", "75%"), ("Min FICO", "630"), ("Min DSCR", "1.00"),
      ("Cash to borrower", "Incidental only"), ("Term", "30-yr fixed, ARM, I/O"),
      ("Prepay options", "0-5 years")],
     "BRRRR operators whose bridge is maturing, and anyone sitting on a note that reprices soon.")}

{prog("cashout", "Program 03: Cash-Out Refinance", "tag-acc",
     "Turn dead equity into the next down payment",
     "Pull capital out of a stabilized rental without selling it. The proceeds are loan proceeds, not "
     "a sale, so the asset keeps appreciating and keeps producing while the money goes to work "
     "somewhere else.",
     ["Typically 70-75% LTV depending on credit and ratio",
      "No restriction on the use of proceeds for business purposes",
      "Commonly funds down payments, rehab budgets, or debt consolidation",
      "Expect a modest rate add-on versus a rate-and-term at the same leverage",
      "Appraised value governs, so recent renovation work is captured"],
     [("Max LTV", "70-75%"), ("Min FICO", "630 (higher tiers price better)"),
      ("Min DSCR", "1.00"), ("Rate add-on", "~0.25% typical"),
      ("Seasoning", "Varies by program"), ("Use of proceeds", "Business purpose")],
     "investors who bought right, rehabbed, and now want the capital back out to repeat the process.")}

{prog("str", "Program 04: Short-Term Rental", "tag-blue",
     "Qualify on nightly revenue, not a 12-month lease",
     "For Airbnb, VRBO, and mid-term furnished rentals. Instead of a lease, underwriting uses documented "
     "platform revenue or a short-term rent schedule, with an expense factor applied to gross receipts.",
     ["Documented platform revenue or an STR-specific rent schedule",
      "Roughly a 20% expense haircut applied to gross receipts",
      "Rate premium of approximately 0.20-0.50% versus long-term rental",
      "LTV is often capped a tier below the comparable long-term product",
      "Local ordinance and permitting are reviewed as part of the file"],
     [("Max LTV", "75% typical"), ("Min FICO", "660 typical"), ("Income basis", "Gross receipts &times; 0.80"),
      ("Rate premium", "+0.20% to +0.50%"), ("Documentation", "Platform statements or STR 1007"),
      ("Restrictions", "Subject to local STR rules")],
     "operators in markets where nightly rates materially beat long-term lease comps, and where "
     "the city hasn't legislated against it.")}

{prog("portfolio", "Program 05: Portfolio / Blanket", "tag-blue",
     "Several doors, one loan, one payment",
     "Roll multiple rental properties into a single facility. Useful for consolidating scattered private "
     "notes, financing free-and-clear stock in bulk, or simplifying the servicing of a growing portfolio.",
     ["Multiple properties cross-collateralized under one note",
      "One closing, one set of costs, one monthly payment",
      "DSCR is computed on the aggregate portfolio, so strong doors carry weaker ones",
      "Release provisions can be negotiated so individual assets can be sold",
      "Entity vesting is effectively required"],
     [("Properties", "Typically 5+"), ("Max LTV", "70-75%"),
      ("DSCR basis", "Portfolio aggregate"), ("Min loan", "Higher than single-asset"),
      ("Release clause", "Negotiable"), ("Vesting", "Entity")],
     "investors with a stack of small notes, or anyone who wants to stop managing eight separate "
     "escrow accounts.")}

{prog("foreign", "Program 06: Foreign National", "tag-gold",
     "U.S. rental property without U.S. credit",
     "Non-resident investors can finance American rental real estate without a FICO score or domestic "
     "credit history. Identity, immigration status, and international references replace the traditional "
     "credit file.",
     ["No U.S. credit score or Social Security number required",
      "Passport plus visa or equivalent documentation",
      "International credit references or bank letters in place of a FICO file",
      "Larger down payment, generally 30-35%",
      "Rates run roughly 0.75-1.00% above the comparable domestic program"],
     [("Max LTV", "65-70%"), ("Credit", "No U.S. FICO required"),
      ("Rate", "~+0.75% to +1.00% vs. domestic"), ("Vesting", "U.S. entity typically required"),
      ("Reserves", "Often 6+ months"), ("Documentation", "Passport, visa, intl. references")],
     "overseas buyers acquiring U.S. cash-flow property who have been told by banks that they need "
     "domestic credit first.")}

<section class="sec">
  <div class="wrap">
    <div class="shead rv">
      <h2>Full eligibility matrix</h2>
      <p>Consolidated guardrails across programs as of {RATES_AS_OF}. Individual investor guidelines vary; treat
      this as the shape of the box, not the final word on your file.</p>
    </div>
    <div class="rv" style="margin-bottom:36px">{ltv_stack()}</div>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th>Parameter</th><th>Standard tier</th><th>Reduced / specialty tier</th></tr></thead>
        <tbody>
          <tr><td>Minimum FICO</td><td>630</td><td>660 for sub-1.00 DSCR; none for foreign national</td></tr>
          <tr><td>DSCR</td><td>1.00 and above</td><td>0.80-0.99 at reduced LTV; no-ratio available</td></tr>
          <tr><td>Purchase LTV</td><td>Up to 80%</td><td>60-75% depending on FICO and loan size</td></tr>
          <tr><td>Rate &amp; term LTV</td><td>Up to 75%</td><td>65-70%</td></tr>
          <tr><td>Cash-out LTV</td><td>70-75%</td><td>60-70%</td></tr>
          <tr><td>Loan amount</td><td>$150,000-$2,000,000</td><td>Above $2,000,000 reviewed case by case</td></tr>
          <tr><td>Reserves</td><td>2 months PITIA</td><td>6 months on loans over $1.5M</td></tr>
          <tr><td>Eligible property</td><td>SFR detached &amp; attached, 2-4 unit, warrantable condo, townhome</td><td>Condotel, rural, and 5-acre-plus at reduced LTV</td></tr>
          <tr><td>Acreage</td><td>Up to 5 acres</td><td>Case by case above 5</td></tr>
          <tr><td>Credit events</td><td>36 months seasoned</td><td>24 months at 75% max on purchase</td></tr>
          <tr><td>Housing history</td><td>No 30-day lates in past 12 months</td><td>Exceptions case by case</td></tr>
          <tr><td>Forbearance / modification</td><td>Over 12 months seasoned</td><td>-</td></tr>
          <tr><td>Prepayment penalty</td><td>1-5 years, 3%-5%</td><td>0-year available with rate add-on</td></tr>
          <tr><td>Prepay prohibited in</td><td colspan="2">AK, KS, MI, MN, NM, RI. Restricted in IL, NJ, OH, PA</td></tr>
          <tr><td>Vesting</td><td>LLC, LP, corporation, or individual</td><td>Entity typically required on portfolio and foreign national</td></tr>
          <tr><td>Financed property limit</td><td colspan="2">None</td></tr>
          <tr><td>Occupancy</td><td colspan="2">Non-owner occupied, business purpose only</td></tr>
        </tbody>
      </table>
    </div>
    <p class="disc rv">{RATE_DISCLAIMER} Program parameters are subject to investor guideline changes and
    state-level restrictions. Not all products are available in all states.</p>
  </div>
</section>

{CTA_BAND}
"""

HTML = page(
    f"DSCR Loan Programs: Purchase, Refinance, Cash-Out, STR | {BRAND}",
    "Six DSCR loan programs for investors: purchase to 80% LTV, rate-and-term, cash-out, short-term "
    "rental, portfolio blanket, and foreign national. Full eligibility matrix and terms.",
    "programs.html", BODY, "", GFX_CSS,
)
