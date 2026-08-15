#!/usr/bin/env python3
"""Parity Lending: V7 SET, built 2026-08-15 from Michael's 8/15 call verdicts.
Same 6 messages as v6 (M2B killed -> 23 ads), 1080x1350.
Global rules on top of v6:
  - NO dba line anywhere. Fine print = business-purpose line + "(c) 2026 Parity Lending".
  - NO blue text. Accents RED; body WHITE (dark) / NAVY (light). Blue only in the logo mark.
  - "DSCR HOME INVESTOR LOANS" at headline scale (red) at the top of EVERY ad;
    the old small label above the spec block is dropped (redundant).
  - No Equal Housing language, ever. No rates, no timing.
  - Specific reworks: M2D line swapped, M4A opener = SHOPPING DSCR QUOTES?, M5C + M6B filled.
Run in cloud container from /home/claude/parity_fb: python3 gen_fb_posts_v7.py [m1a m2 ...]"""
import gen_fb_posts_v6 as v6
from gen_fb_posts import *
from gen_fb_posts_v4 import pill_btn, corner_pill
from gen_fb_posts_v4ph import cover, paste_photo, vgrad_fast
from PIL import Image, ImageDraw

COPYRIGHT = "© 2026 Parity Lending"
LABEL = v6.LABEL
SPEC1, SPEC2, BAR = v6.SPEC1, v6.SPEC2, v6.BAR
hstack, cstack = v6.hstack, v6.cstack

def fine_print(d, dark, y1=None):
    y1 = y1 or H - 78
    f = F("Regular", 14)
    c = SLATEL if dark else SLATE
    ttext(d, W / 2, y1, DISCLAIMER, f, c, anchor="ma")
    ttext(d, W / 2, y1 + 24, COPYRIGHT, F("Medium", 14), WHITE if dark else NAVY, anchor="ma")

def big_label(d, x, y, size=46, center=False):
    ttext(d, x, y, LABEL, F("ExtraBold", size), RED, tr=2, anchor="ma" if center else "la")
    return y + int(size * 1.25)

def big_label2(d, x, y, size=34):
    """Two-line label for narrow panels."""
    f = F("ExtraBold", size)
    ttext(d, x, y, "DSCR HOME", f, RED, tr=2)
    ttext(d, x, y + int(size * 1.15), "INVESTOR LOANS", f, RED, tr=2)
    return y + int(size * 2.3)

def spec_block(d, y, dark, center=True):
    """v6 spec block minus the small label (big label lives at the top now)."""
    txt_c = WHITE if dark else NAVY
    ax = W / 2 if center else 84
    anc = "ma" if center else "la"
    ttext(d, ax, y + 40, SPEC1, F("SemiBold", 17.5), txt_c, tr=0.5, anchor=anc)
    ttext(d, ax, y + 72, SPEC2, F("SemiBold", 17.5), txt_c, tr=0.5, anchor=anc)
    rrect(d, (84, y + 116, W - 84, y + 172), 14, fill=NAVY2 if dark else NAVY)
    ttext(d, W / 2, y + 144, BAR, F("SemiBold", 17), WHITE, tr=1, anchor="mm")
    pf = F("Bold", 21)
    lab = "SEE IF YOU QUALIFY"
    bw = text_w(d, lab, pf, 2) + 96
    x0 = W / 2 - (bw + 24 + text_w(d, "DSCR Lending Nationwide.", F("SemiBold", 19))) / 2
    rrect(d, (x0, y + 196, x0 + bw, y + 264), 34, fill=RED)
    ttext(d, x0 + bw / 2, y + 230, lab, pf, WHITE, tr=2, anchor="mm")
    ttext(d, x0 + bw + 24, y + 230, "DSCR Lending Nationwide.", F("SemiBold", 19),
          txt_c, anchor="lm")

def narrow_spec(d, x, y, dark, pill_w=380):
    c_txt = WHITE if dark else SLATE
    yy = y + 6
    for item in ["Investment properties only", "20%+ down / equity", "620+ credit",
                 "Qualify using rental income", "No tax returns required"]:
        check_circle(d, x + 14, yy + 13, 13, RED)
        ttext(d, x + 42, yy, item, F("Medium", 22), c_txt)
        yy += 46
    yy += 10
    ttext(d, x, yy, "PURCHASE · REFINANCE · CASH OUT", F("Bold", 16.5),
          WHITE if dark else NAVY, tr=1)
    ttext(d, x, yy + 34, "SFR · CONDOS · 2-4 UNITS", F("SemiBold", 15.5),
          SLATEL if dark else SLATE, tr=1)
    rrect(d, (x, yy + 78, x + pill_w, yy + 146), 34, fill=RED)
    ttext(d, x + pill_w / 2, yy + 112, "SEE IF YOU QUALIFY", F("Bold", 19), WHITE, tr=2, anchor="mm")

# =====================================================================
# TEMPLATES (all carry the big red DSCR label at the top)
# =====================================================================
SPEC_Y = 976

def t_navy_left(name, eyebrow, headline, subs=(), label_size=46, hl_y=None):
    img, d = canvas(NAVY)
    chevron(d, 965, 900, 8.5, blue=NAVY2, red=NAVY2)
    lockup_h(d, 84, 84, mark_h=40, dark=True)
    corner_pill(d, col=WHITE)
    y = big_label(d, 84, 214, size=label_size)
    if eyebrow:
        ttext(d, 84, y + 10, eyebrow, F("SemiBold", 19), WHITE, tr=4)
        y += 52
    else:
        y += 18
    y = hstack(d, 84, hl_y or y, headline)
    y += 14
    for s, c in subs:
        ttext(d, 84, y, s, F("Medium", 26), c)
        y += 44
    spec_block(d, SPEC_Y, dark=True, center=False)
    fine_print(d, dark=True)
    save(img, name)

def t_mist_center(name, eyebrow, headline, subs=(), label_size=46, sub_size=25):
    img, d = canvas(MIST)
    lockup_stack(d, W / 2, 74, mark_h=50, tagline=True)
    y = big_label(d, W / 2, 252, size=label_size, center=True)
    if eyebrow:
        ttext(d, W / 2, y + 8, eyebrow, F("SemiBold", 18), NAVY, tr=4, anchor="ma")
        y += 50
    else:
        y += 16
    y = cstack(d, y, headline)
    y += 12
    for s, c in subs:
        ttext(d, W / 2, y, s, F("Medium", sub_size), c, anchor="ma")
        y += int(sub_size * 1.7)
    spec_block(d, SPEC_Y, dark=False, center=True)
    fine_print(d, dark=False)
    save(img, name)

def t_photo_split(name, photo, dark, eyebrow, headline, panel_w=560):
    img, d = canvas(NAVY if dark else MIST)
    ph = cover(photo, W - panel_w + 40, 1216)
    paste_photo(img, ph, panel_w - 40, 0)
    d = ImageDraw.Draw(img)
    d.rectangle([0, sx(1216), sx(W), sx(H)], fill=NAVY)
    lockup_h(d, 84, 78, mark_h=36, dark=dark)
    y = big_label2(d, 84, 176, size=34)
    if eyebrow:
        ttext(d, 84, y + 8, eyebrow, F("SemiBold", 15.5), WHITE if dark else NAVY, tr=2.5)
        y += 46
    else:
        y += 14
    y = hstack(d, 84, y, headline)
    narrow_spec(d, 84, y + 18, dark)
    fine_print(d, dark=True)
    save(img, name)

def t_photo_top(name, photo, eyebrow, headline, subs=(), ph_h=440, label_size=44, sub_size=24):
    img, d = canvas(NAVY)
    ph = cover(photo, W, ph_h)
    paste_photo(img, ph, 0, 0)
    vgrad_fast(img, 0, ph_h - 160, W, 160, NAVY, 0, 255)
    vgrad_fast(img, 0, 0, W, 120, NAVY, 140, 0)
    d = ImageDraw.Draw(img)
    lockup_h(d, 84, 58, mark_h=36, dark=True)
    y = big_label(d, 84, ph_h + 10, size=label_size)
    if eyebrow:
        ttext(d, 84, y + 8, eyebrow, F("SemiBold", 17), WHITE, tr=4)
        y += 48
    else:
        y += 14
    y = hstack(d, 84, y, headline)
    yy = y + 6
    for s, c in subs:
        ttext(d, 84, yy, s, F("Medium", sub_size), c)
        yy += int(sub_size * 1.7)
    spec_block(d, SPEC_Y, dark=True, center=False)
    fine_print(d, dark=True)
    save(img, name)

# =====================================================================
# MESSAGE 1 — Negation stack
# =====================================================================
def m1a():
    img, d = canvas(NAVY)
    chevron(d, 965, 900, 8.5, blue=NAVY2, red=NAVY2)
    lockup_h(d, 84, 84, mark_h=40, dark=True)
    corner_pill(d, col=WHITE)
    y = big_label(d, 84, 226, size=46)
    y += 30
    y = hstack(d, 84, y, [
        ("No tax returns.", "ExtraBold", 80, WHITE),
        ("No W2s.", "ExtraBold", 80, WHITE),
        ("No DTI.", "ExtraBold", 80, WHITE),
        ("The property", "ExtraBold", 80, RED),
        ("qualifies.", "ExtraBold", 80, RED)])
    spec_block(d, SPEC_Y, dark=True, center=False)
    fine_print(d, dark=True)
    save(img, "parity-fb-v7-01a-negation.png")

def m1():
    m1a()
    t_mist_center("parity-fb-v7-01b-negation.png", None,
        [("The property", "ExtraBold", 76, NAVY),
         ("qualifies.", "ExtraBold", 76, NAVY),
         ("Not your paperwork.", "ExtraBold", 76, RED)],
        subs=[("No tax returns. No W2s. No DTI.", SLATE)])
    t_photo_split("parity-fb-v7-01c-negation.png", "p2.jpg", True, None,
        [("No tax", "ExtraBold", 62, WHITE),
         ("returns.", "ExtraBold", 62, WHITE),
         ("No W2s. No DTI.", "ExtraBold", 40, WHITE),
         ("The property", "ExtraBold", 46, RED),
         ("qualifies.", "ExtraBold", 46, RED)])
    t_photo_top("parity-fb-v7-01d-negation.png", "p7.jpg", None,
        [("No tax returns. No W2s. No DTI.", "ExtraBold", 46, WHITE),
         ("The property qualifies.", "ExtraBold", 46, RED)],
        subs=[("If the rent covers the payment, you have a deal.", SLATEL)])

# =====================================================================
# MESSAGE 2 — Spec sheet (M2B killed by Michael 8/15)
# =====================================================================
def m2a():
    img, d = canvas(MIST)
    lockup_stack(d, W / 2, 70, mark_h=48, tagline=True)
    ttext(d, W / 2, 268, "BUYING OR REFINANCING A RENTAL PROPERTY?", F("SemiBold", 19), RED, tr=3, anchor="ma")
    ttext(d, W / 2, 314, "DSCR HOME", F("Black", 84), NAVY, tr=1, anchor="ma")
    ttext(d, W / 2, 418, "INVESTOR LOANS", F("Black", 84), NAVY, tr=1, anchor="ma")
    cy0, cy1 = 556, 776
    gap = 24
    cw = (W - 168 - gap) / 2
    for i, (num, lab) in enumerate([("20%+", "DOWN / EQUITY"), ("620+", "CREDIT SCORE")]):
        x0 = 84 + i * (cw + gap)
        rrect(d, (x0, cy0, x0 + cw, cy1), 22, fill=WHITE, outline=BORDER, width=sx(1.2))
        cx = x0 + cw / 2
        ttext(d, cx, cy0 + 34, num, F("Black", 92), NAVY, anchor="ma")
        ttext(d, cx, cy1 - 56, lab, F("SemiBold", 18), RED, tr=4, anchor="ma")
    ttext(d, W / 2, 812, "Qualify using rental income. No tax returns required.",
          F("SemiBold", 24), SLATE, anchor="ma")
    rrect(d, (84, 880, W - 84, 936), 14, fill=NAVY)
    ttext(d, W / 2, 908, BAR, F("SemiBold", 17), WHITE, tr=1, anchor="mm")
    pill_btn(d, 986, "SEE IF YOU QUALIFY")
    ttext(d, W / 2, 1096, "80% MAX LTV ACROSS THE BOARD  ·  DSCR Lending Nationwide.",
          F("SemiBold", 19), NAVY, anchor="ma")
    ttext(d, W / 2, 1146, "Options to close in an LLC or your personal name.",
          F("Medium", 19), SLATE, anchor="ma")
    fine_print(d, dark=False)
    save(img, "parity-fb-v7-02a-specsheet.png")

def m2():
    m2a()
    t_photo_split("parity-fb-v7-02c-specsheet.png", "p9.jpg", False, None,
        [("Buying or", "ExtraBold", 60, NAVY),
         ("refinancing", "ExtraBold", 60, NAVY),
         ("a rental", "ExtraBold", 60, NAVY),
         ("property?", "ExtraBold", 60, RED)])
    # M2D reworked: Michael disliked "The application is the property, not your paperwork."
    t_photo_top("parity-fb-v7-02d-specsheet.png", "p11.jpg",
        "BUYING OR REFINANCING A RENTAL PROPERTY?",
        [("Qualified on the rent.", "ExtraBold", 56, WHITE),
         ("No W-2s. No tax returns.", "ExtraBold", 48, RED)],
        subs=[("Purchase, refinance or cash out on SFR, condos and 2-4 units.", WHITE),
              ("20%+ down or equity. 620+ credit.", SLATEL)])

# =====================================================================
# MESSAGE 3 — The rehab is done
# =====================================================================
def m3():
    t_navy_left("parity-fb-v7-03a-rehab.png",
        "FOR FLIPPERS & BRRRR INVESTORS",
        [("THE REHAB", "Black", 84, WHITE),
         ("IS DONE.", "Black", 84, WHITE),
         ("NOW LOCK IN THE", "Black", 52, RED),
         ("LONG-TERM HOME LOAN.", "Black", 52, RED)],
        subs=[("Refi into 30-year money on the rent it earns.", SLATEL)])
    t_mist_center("parity-fb-v7-03b-rehab.png",
        "FOR FLIPPERS & BRRRR INVESTORS",
        [("The rehab is done.", "ExtraBold", 70, NAVY),
         ("Now lock in the", "ExtraBold", 70, NAVY),
         ("long-term home loan.", "ExtraBold", 70, RED)],
        subs=[("Your capital comes back out for the next one.", SLATE)])
    t_photo_top("parity-fb-v7-03c-rehab.png", "p11.jpg",
        "FOR FLIPPERS & BRRRR INVESTORS",
        [("THE REHAB IS DONE.", "Black", 52, WHITE),
         ("NOW LOCK IN THE LONG-TERM", "Black", 40, RED),
         ("HOME LOAN.", "Black", 40, RED)])
    t_photo_split("parity-fb-v7-03d-rehab.png", "p3.jpg", True,
        "FLIPPERS & BRRRR INVESTORS",
        [("The rehab", "ExtraBold", 58, WHITE),
         ("is done.", "ExtraBold", 58, WHITE),
         ("Lock in the", "ExtraBold", 44, RED),
         ("long-term", "ExtraBold", 44, RED),
         ("home loan.", "ExtraBold", 44, RED)])

# =====================================================================
# MESSAGE 4 — You're a borrower, not a lead
# =====================================================================
def m4a():
    """Reworked per Michael: opener leads with SHOPPING DSCR QUOTES?, DSCR label big."""
    img, d = canvas(NAVY)
    chevron(d, 965, 880, 8.5, blue=NAVY2, red=NAVY2)
    lockup_h(d, 84, 84, mark_h=40, dark=True)
    corner_pill(d, col=WHITE)
    y = big_label(d, 84, 214, size=46)
    ttext(d, 84, y + 16, "SHOPPING DSCR QUOTES?", F("Black", 46), WHITE, tr=1)
    y = hstack(d, 84, y + 84, [("You're a borrower.", "ExtraBold", 76, WHITE),
                               ("Not a lead.", "Black", 108, RED)])
    y += 10
    rrect(d, (84, y, W - 84, y + 72), 16, fill=NAVY2)
    ttext(d, W / 2, y + 36, "ONE LENDER   ·   NO CALL LISTS   ·   NEVER RESOLD",
          F("SemiBold", 20), WHITE, tr=1, anchor="mm")
    ttext(d, 84, y + 104, "Quote sites sell your number to five call lists.", F("Medium", 25), WHITE)
    ttext(d, 84, y + 146, "Here you talk to the lender. Your info stays put.", F("Medium", 25), SLATEL)
    spec_block(d, SPEC_Y, dark=True, center=False)
    fine_print(d, dark=True)
    save(img, "parity-fb-v7-04a-notalead.png")

def m4():
    m4a()
    t_mist_center("parity-fb-v7-04b-notalead.png",
        "SHOPPING DSCR QUOTES?",
        [("One lender.", "ExtraBold", 78, NAVY),
         ("Zero call lists.", "ExtraBold", 78, NAVY),
         ("Never resold.", "ExtraBold", 78, RED)],
        subs=[("Your information never leaves the building.", SLATE)])
    t_photo_split("parity-fb-v7-04c-notalead.png", "p2.jpg", True,
        "SHOPPING DSCR QUOTES?",
        [("You're a", "ExtraBold", 62, WHITE),
         ("borrower.", "ExtraBold", 62, WHITE),
         ("Not a lead.", "Black", 66, RED)])
    t_photo_top("parity-fb-v7-04d-notalead.png", "p9.jpg",
        "SHOPPING DSCR QUOTES?",
        [("You're a borrower.", "ExtraBold", 54, WHITE),
         ("Not a lead.", "Black", 60, RED)],
        subs=[("One lender. No call lists. Your info is never resold.", SLATEL)])

# =====================================================================
# MESSAGE 5 — Serious investor checklist
# =====================================================================
def m5a():
    img, d = canvas(MIST)
    rrect(d, (56, 56, W - 56, H - 56), 28, fill=WHITE)
    rrect(d, (56, 56, W - 56, 400), 28, fill=NAVY)
    d.rectangle([sx(56), sx(340), sx(W - 56), sx(400)], fill=NAVY)
    lockup_stack(d, W / 2, 126, mark_h=76, dark=True, tagline=True)
    px = 128
    ttext(d, px, 440, LABEL, F("ExtraBold", 36), RED, tr=2)
    ttext(d, px, 504, "Built for the", F("Bold", 52), NAVY)
    ttext(d, px, 570, "serious investor.", F("Bold", 52), NAVY)
    y = 676
    for item in ["Investment properties only", "20%+ down or equity", "620+ credit",
                 "Qualify using rental income, not tax returns",
                 "Close in your LLC or personal name"]:
        check_circle(d, px + 16, y + 14, 15, RED)
        ttext(d, px + 50, y, item, F("Medium", 25), SLATE)
        y += 54
    rrect(d, (px, y + 30, W - px, y + 84), 14, fill=NAVY)
    ttext(d, W / 2, y + 57, BAR, F("SemiBold", 16.5), WHITE, tr=0.5, anchor="mm")
    bw = 340
    rrect(d, (px, y + 112, px + bw, y + 178), 33, fill=RED)
    ttext(d, px + bw / 2, y + 145, "SEE IF YOU QUALIFY", F("Bold", 19), WHITE, tr=2, anchor="mm")
    ttext(d, px + bw + 28, y + 145, "DSCR Lending Nationwide.", F("SemiBold", 18), NAVY, anchor="lm")
    fine_print(d, dark=False, y1=H - 118)
    save(img, "parity-fb-v7-05a-checklist.png")

def m5():
    m5a()
    t_navy_left("parity-fb-v7-05b-checklist.png", None,
        [("Built for the", "ExtraBold", 82, WHITE),
         ("serious", "ExtraBold", 82, WHITE),
         ("investor.", "ExtraBold", 82, RED)],
        subs=[("Scaling a portfolio? This is the loan that doesn't", WHITE),
              ("care what your tax returns say.", WHITE)])
    # M5C filled per Michael: bigger headline, more copy
    t_photo_top("parity-fb-v7-05c-checklist.png", "p7.jpg", None,
        [("Built for the", "ExtraBold", 64, WHITE),
         ("serious investor.", "ExtraBold", 64, RED)],
        subs=[("Qualify on the rent, not your tax returns.", WHITE),
              ("Close in your LLC or personal name.", WHITE),
              ("Scale the portfolio without the paperwork.", SLATEL)],
        sub_size=25)
    t_photo_split("parity-fb-v7-05d-checklist.png", "p6.jpg", False, None,
        [("Built for", "ExtraBold", 62, NAVY),
         ("the serious", "ExtraBold", 62, NAVY),
         ("investor.", "ExtraBold", 62, RED)])

# =====================================================================
# MESSAGE 6 — Hard money STOP
# =====================================================================
def m6():
    t_navy_left("parity-fb-v7-06a-stop.png",
        "ATTENTION: INVESTMENT PROPERTY OWNERS",
        [("Still paying hard", "ExtraBold", 64, WHITE),
         ("money rates on an", "ExtraBold", 64, WHITE),
         ("investment property?", "ExtraBold", 64, WHITE),
         ("STOP.", "Black", 104, RED)],
        subs=[("A DSCR home loan can work for you.", WHITE)])
    # M6B filled per Michael: DSCR much larger, more copy
    t_mist_center("parity-fb-v7-06b-stop.png",
        "ATTENTION: INVESTMENT PROPERTY OWNERS",
        [("Hard money was", "ExtraBold", 84, NAVY),
         ("the bridge.", "ExtraBold", 84, NAVY),
         ("This is the exit.", "ExtraBold", 84, RED)],
        subs=[("Move to a long-term DSCR home loan, qualified on the rent.", NAVY),
              ("No tax returns. 20%+ equity. 620+ credit. Cash out available.", SLATE)],
        label_size=52, sub_size=25)
    t_photo_top("parity-fb-v7-06c-stop.png", "p11.jpg",
        "ATTENTION: INVESTMENT PROPERTY OWNERS",
        [("Still paying hard money rates?", "ExtraBold", 44, WHITE),
         ("STOP.", "Black", 72, RED)],
        subs=[("A DSCR home loan can work for you.", SLATEL)])
    t_photo_split("parity-fb-v7-06d-stop.png", "p3.jpg", True,
        "INVESTMENT PROPERTY OWNERS",
        [("Still paying", "ExtraBold", 54, WHITE),
         ("hard money", "ExtraBold", 54, WHITE),
         ("rates?", "ExtraBold", 54, WHITE),
         ("STOP.", "Black", 80, RED)])

if __name__ == "__main__":
    import sys, os
    os.makedirs("out", exist_ok=True)
    which = sys.argv[1:] or ["m1", "m2", "m3", "m4", "m5", "m6"]
    for w in which:
        globals()[w]()
