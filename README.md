PARITY LENDING — DSCR SITE
==========================

FILES
  index.html      Home / landing page (live DSCR calculator)
  programs.html   Six loan programs + full eligibility matrix
  qualify.html    Six-question scenario checker
  faq.html        Full FAQ
  contact.html    Phone, email, about
  assets/         Logo files extracted from the supplied artwork

Every page is self-contained. The logo and favicon are embedded as data URIs,
so the HTML files work on their own even without the assets folder.

BEFORE GOING LIVE — replace these placeholders
  Phone   (888) 555-0123
  Email   loans@paritylending.com
Both live in config.py in the source project. In the built HTML they appear
in tel:, mailto:, and visible text.

BRAND COLORS (sampled from the logo artwork)
  #D43426  chevron red      CTAs, accents, rules
  #1A3796  chevron blue     secondary accents, bars
  #101A35  wordmark navy    headings, dark type
  #16224A  dark surface     footer, CTA band, stat band
  #505979  wordmark grey    body copy

assets/
  logo.png            transparent, for light backgrounds
  logo-white.png      transparent, for dark backgrounds
  logo@2x.png         full-resolution transparent original
  logo-white@2x.png   full-resolution white variant
  mark.png            chevron only
  favicon.png         64px favicon

The mouse cursor that was baked into the supplied screenshot has been removed
and the white background converted to transparency.

COMPLIANCE
  Every page carries Equal Housing Lender, Ameritrust Mortgage Corporation
  NMLS 217229, the not-a-commitment-to-lend language, and a rate disclaimer.
  All rates shown are labeled illustrative examples, not quotes.
