# =============================================================================
# SITE CONFIG: edit these values, re-run build.py, done.
# =============================================================================

BRAND       = "Parity Lending"        # from the supplied logo
BRAND_SHORT = "Parity"
BRAND_MARK  = "PL"                    # fallback only; the real logo image is used
TAGLINE     = "DSCR Lending for Real Estate Investors"

PHONE_DISPLAY = "(888) 555-0123"      # <-- replace with the real number
PHONE_TEL     = "+18885550123"
EMAIL         = "loans@paritylending.com"     # <-- replace with the real inbox

CITY_STATE   = "Nationwide (excluding ND, SD, VT)"
LO_NAME      = "Michael McDermott"
LO_NMLS      = "1036304"
CO_NAME      = "Ameritrust Mortgage Corporation"
CO_NMLS      = "217229"

RATES_AS_OF  = "July 2026"

COMPLIANCE = (
    "Equal Housing Lender. " + CO_NAME + " NMLS " + CO_NMLS + ". "
    "This is not a commitment to lend. Programs, rates, terms, and conditions are "
    "subject to change without notice. All loans subject to credit approval."
)

RATE_DISCLAIMER = (
    "Rates shown are illustrative examples as of " + RATES_AS_OF + " for discussion purposes only. "
    "They are not an offer, quote, rate lock, or commitment to lend. Your actual rate depends on "
    "credit, LTV, DSCR, property type, occupancy, loan amount, state, and market conditions at "
    "the time of lock."
)

NAV = [
    ("index.html",    "Home"),
    ("programs.html", "Programs"),
    ("qualify.html",  "Check My Numbers"),
    ("faq.html",      "FAQ"),
    ("contact.html",  "Contact"),
]
