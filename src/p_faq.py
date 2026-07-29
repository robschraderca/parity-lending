from shell import *
from graphics import GFX_CSS

GROUPS = [
    ("Basics", "tag-acc", [
        ("What exactly is a DSCR loan?",
         "<p>A mortgage on investment property that qualifies on the property's rental income instead of "
         "your personal income. The lender divides gross monthly rent by the monthly PITIA payment "
         "(principal, interest, taxes, insurance, and HOA). That quotient is the DSCR. If it clears the "
         "program threshold and the credit and equity requirements are met, the loan works.</p>"
         "<p>It is a business-purpose loan. It cannot be used for a property you intend to live in.</p>"),
        ("How is DSCR actually calculated?",
         "<p>Gross monthly rent divided by monthly PITIA. Rent is the gross lease amount or the appraiser's "
         "market rent estimate, not net of vacancy, management, or maintenance. PITIA is the full "
         "housing payment including escrows and HOA dues.</p>"
         "<p>Example: $2,400 rent against a $1,920 PITIA gives a DSCR of 1.25. Short-term rentals are the "
         "exception. Gross receipts are typically multiplied by about 0.80 before the division to "
         "account for higher operating costs.</p>"),
        ("What DSCR do I need to qualify?",
         "<p>1.00 is the standard floor and means rent exactly covers the payment. At 1.25 and above you "
         "reach the best pricing tier. Between 0.80 and 0.99 you can still close, but expect a lower LTV "
         "cap, a 660+ credit requirement, and a rate add-on. Below 0.80 the conversation usually shifts to "
         "a no-ratio program or a larger down payment.</p>"),
        ("Is a DSCR loan the same as a hard money loan?",
         "<p>No, and the difference matters. Hard money is short-term, interest-only, typically 10-13%, "
         "and priced for speed and risk during a rehab. A DSCR loan is permanent financing: 30-year "
         "amortization, conventional-adjacent pricing, and built to be held. Investors often use one to "
         "exit the other.</p>"),
        ("Why is it called a non-QM loan? Is that risky?",
         "<p>Non-QM means the loan doesn't meet the Consumer Financial Protection Bureau's Qualified "
         "Mortgage definition, largely because QM requires a documented ability-to-repay analysis "
         "based on personal income, which DSCR deliberately skips. It is a classification, not a quality "
         "judgment. These are fully amortizing, fully underwritten loans made by regulated institutional "
         "lenders.</p>"),
    ]),
    ("Qualifying", "tag-blue", [
        ("What credit score do I need?",
         "<p>630 is the general minimum. Pricing improves at 700, again at 720, and again at 740+. "
         "The spread between a 660 and a 740 borrower at the same LTV can be more than half a point. "
         "Sub-1.00 DSCR tiers usually require 660 or better.</p>"),
        ("Do you check my debt-to-income ratio?",
         "<p>No. DTI is not calculated on a DSCR loan. Your car payment, student loans, personal mortgage, "
         "and other rental mortgages are not counted against you.</p>"),
        ("How much money do I need for a down payment?",
         "<p>Plan on 20-25% for a purchase. Twenty percent is achievable with strong credit and a "
         "healthy ratio. A weaker DSCR, a lower score, a short-term rental, a smaller loan, or a rural "
         "property can push that to 25-30%. Foreign nationals generally need 30-35%.</p>"),
        ("What reserves do I need after closing?",
         "<p>Two months of PITIA on the subject property is the standard requirement. That climbs to six "
         "months on loans above $1.5 million. Reserves can sit in "
         "personal or business accounts and can include seasoned retirement funds at a discount.</p>"),
        ("Can I use gift funds?",
         "<p>Generally not for the down payment on a business-purpose investment loan. Some programs will "
         "allow gifted funds toward reserves or closing costs with documentation. Assume your own seasoned "
         "funds unless we confirm otherwise on your specific file.</p>"),
        ("What if I've had a bankruptcy or foreclosure?",
         "<p>Credit events are typically expected to be 36 months seasoned for full program eligibility. "
         "At 24 months you can often still close, capped around 75% LTV on a purchase. Forbearance, "
         "modification, or deferral generally needs more than 12 months of seasoning.</p>"),
        ("Do I need landlord experience?",
         "<p>Not on most programs. First-time investors qualify. A few investors price first-timers slightly "
         "differently or trim the maximum LTV by a tier, but lack of experience is not a disqualifier.</p>"),
    ]),
    ("The property", "tag-acc", [
        ("What property types are eligible?",
         "<p>Single-family detached and attached, 2-4 unit residential, warrantable condominiums, and "
         "townhomes. Up to 5 acres is standard. Condotels, rural properties, and larger parcels are often "
         "possible at reduced leverage. Raw land, commercial, and 5+ unit multifamily fall outside DSCR "
         "programs.</p>"),
        ("The property is vacant. Can I still qualify?",
         "<p>Yes. The appraiser completes a comparable rent schedule (Form 1007 on a single unit, "
         "Form 1025 on 2-4 units) and we qualify off that market rent figure. An executed lease "
         "is cleaner and occasionally prices better, but vacancy is not a blocker.</p>"),
        ("What if the current lease is below market?",
         "<p>Most programs use the lower of the actual lease or the appraiser's market rent, which means a "
         "deeply below-market lease can drag your ratio down. If a tenant is well under market and the lease "
         "expires soon, tell us up front. Timing the refinance after the lease turns can materially "
         "change the outcome.</p>"),
        ("Can I finance a property that needs work?",
         "<p>DSCR programs finance stabilized, rent-ready property. Habitability issues, missing systems, or "
         "an active construction site will fail appraisal condition standards. The common path is short-term "
         "or hard-money financing for the rehab, then a DSCR refinance once the property is complete and "
         "leased.</p>"),
        ("Do you lend on short-term rentals?",
         "<p>Yes, on programs that permit them. Underwriting uses documented platform revenue or a short-term "
         "rent schedule with roughly a 20% expense factor applied, plus a rate premium. Local ordinances and "
         "permit status are reviewed. Markets that have banned or heavily restricted STRs are a "
         "problem regardless of the revenue.</p>"),
    ]),
    ("Structure and costs", "tag-gold", [
        ("Can I close in an LLC?",
         "<p>Yes, and most investors do. LLC, LP, and corporate vesting are standard. You will typically sign "
         "a personal guarantee. Documentation needed: operating agreement, articles of organization, EIN "
         "letter, and a certificate of good standing.</p>"),
        ("Is there a limit on the number of properties I can own or finance?",
         "<p>No. This is the primary structural advantage over agency financing, which caps financed "
         "properties and stacks reserve requirements across your whole portfolio.</p>"),
        ("What loan terms are available?",
         "<p>30-year fixed is the most common. Adjustable-rate structures, interest-only periods, and 40-year "
         "terms with a 10-year interest-only front end are widely available. Interest-only is a common tool "
         "for making a tight DSCR clear the threshold, since it lowers the payment in the denominator.</p>"),
        ("Explain the prepayment penalty.",
         "<p>Most DSCR loans carry a prepay period of one to five years. It is a fee, typically 3% to 5% of "
         "the balance, if you pay off or refinance during that window. A longer prepay buys a lower rate; a "
         "zero-prepay option is available at a higher rate. If you expect to sell or refinance within a "
         "couple of years, structure for it deliberately. Prepays are prohibited in Alaska, Kansas, Michigan, "
         "Minnesota, New Mexico, and Rhode Island, and restricted in Illinois, New Jersey, Ohio, and "
         "Pennsylvania.</p>"),
        ("What are the closing costs?",
         "<p>Expect origination points, an appraisal with a rent schedule addendum, title and escrow, "
         "recording, and standard prepaids for taxes and insurance. DSCR closing costs generally run somewhat "
         "higher than a comparable agency loan. You will see every line item on a written term sheet before "
         "you spend money on third-party reports.</p>"),
        ("How long does closing take?",
         "<p>Two to four weeks is typical. The appraisal is usually the constraint. Because there are no tax "
         "transcripts, employment verifications, or income conditions to chase, DSCR files tend to stall "
         "less than full-doc loans.</p>"),
    ]),
    ("Getting started", "tag-blue", [
        ("What do you need from me to start?",
         "<p>To give you an indicative rate and structure: the property address, the purchase price or your "
         "estimate of value, the monthly rent (actual or expected), your approximate credit score, and "
         "whether it's a purchase, rate-and-term, or cash-out. That's a five-minute conversation.</p>"),
        ("Will you pull my credit right away?",
         "<p>No. We can give you indicative terms from a soft conversation. A credit pull happens when you've "
         "seen the numbers in writing and want to move forward.</p>"),
        ("Is there an application fee?",
         "<p>No fee to review a scenario or receive a term sheet. Third-party costs, principally the "
         "appraisal, come later, once you've decided to proceed.</p>"),
        ("What states do you lend in?",
         f"<p>{CITY_STATE}. Not every program is available in every state, and prepayment penalty rules vary "
         "considerably by jurisdiction. Ask about your specific state on the first call.</p>"),
        ("My deal is unusual. Should I still call?",
         "<p>Yes. Mixed portfolios, tight ratios, recent credit events, entity complications, and unusual "
         "property characteristics are routine here. The worst outcome of a five-minute call is a clear no "
         "and a specific reason, which is more useful than a maybe.</p>"),
    ]),
]


def group(title, cls, items):
    d = "".join(
        f'<details><summary>{q}</summary><div class="body">{a}</div></details>' for q, a in items
    )
    return f"""<div class="rv" style="margin-bottom:44px">
  <span class="tag {cls}">{title}</span>
  <div class="acc" style="margin-top:16px">{d}</div>
</div>"""


BODY = f"""
<section class="hero" style="padding:88px 0 66px">
  <div class="wrap">
    <div class="eyebrow rv"><span class="dot"></span>Frequently Asked</div>
    <h1 class="rv" style="max-width:16ch">Everything investors ask, answered plainly.</h1>
    <p class="hero-sub rv" style="max-width:60ch">No hedging and no sales language. If something here doesn't
    match your situation, call and ask. The specific answer is usually more useful than the general one.</p>
    <div class="btn-row rv">
      <a class="btn btn-primary btn-lg" href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
      <a class="btn btn-ghost btn-lg" href="mailto:{EMAIL}">{MAIL_ICO}Email a question</a>
    </div>
  </div>
</section>

<div class="hr"></div>

<section class="sec">
  <div class="wrap" style="max-width:900px">
    {"".join(group(t, c, i) for t, c, i in GROUPS)}
    <p class="disc">{COMPLIANCE}</p>
  </div>
</section>

{CTA_BAND}
"""

HTML = page(
    f"DSCR Loan FAQ: Requirements, Rates, Down Payment, LLC | {BRAND}",
    "Answers to the most common DSCR loan questions: minimum credit score, DSCR calculation, down "
    "payment, LLC vesting, prepayment penalties, short-term rentals, closing timelines, and more.",
    "faq.html", BODY, "", GFX_CSS,
)
