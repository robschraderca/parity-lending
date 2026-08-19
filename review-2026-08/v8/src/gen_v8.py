#!/usr/bin/env python3
"""Parity Lending v8 master template. ONE layout, controlled variables:
   - message (6)      -> headline copy only
   - state A/B         -> A = photo hero, B = flat navy hero (same geometry)
Everything else is pixel-identical. 1080x1350, rendered at 2x then downsampled.
Rules: DSCR HOME INVESTOR LOANS at hero scale; no blue text (red/navy/white/slate);
no rates, no timing; standard spec set; CTA SEE IF YOU QUALIFY; no dba; no EHL."""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = 2                      # supersample
W, H = 1080, 1350
NAVY  = (14, 27, 61)
NAVY2 = (22, 39, 82)
BLUE  = (27, 63, 160)      # logo only
BLUED = (59, 111, 212)     # logo only
RED   = (217, 59, 43)
SLATE = (90, 100, 132)
MIST  = (242, 243, 246)
WHITE = (255, 255, 255)
BORDER= (222, 225, 232)
FONT  = "/tmp/v8/fonts/Montserrat-VF.ttf"
_fc = {}
def F(weight, size):
    k = (weight, size)
    if k not in _fc:
        f = ImageFont.truetype(FONT, int(size * S))
        f.set_variation_by_name(weight)
        _fc[k] = f
    return _fc[k]
def sx(v): return int(round(v * S))

def ttext(d, x, y, s, f, fill, tr=0, anchor="la"):
    if tr == 0:
        d.text((sx(x), sx(y)), s, font=f, fill=fill, anchor=anchor); return
    # tracked text: manual layout
    widths = [d.textlength(ch, font=f) for ch in s]
    total = sum(widths) + tr * S * (len(s) - 1)
    if anchor[0] == "m": x0 = sx(x) - total / 2
    elif anchor[0] == "r": x0 = sx(x) - total
    else: x0 = sx(x)
    va = anchor[1]
    cx = x0
    for ch, w in zip(s, widths):
        d.text((cx, sx(y)), ch, font=f, fill=fill, anchor="l" + va)
        cx += w + tr * S
def text_w(d, s, f, tr=0):
    return (sum(d.textlength(ch, font=f) for ch in s) + tr * S * (len(s) - 1)) / S

def rrect(d, box, r, **kw):
    x0, y0, x1, y1 = box
    d.rounded_rectangle([sx(x0), sx(y0), sx(x1), sx(y1)], radius=sx(r), **kw)

def chevron(d, cx, cy, sc, blue=BLUED, red=RED):
    def P(pts): return [(sx(cx + x * sc), sx(cy + y * sc)) for x, y in pts]
    d.polygon(P([(0,0),(-31.5,31.5),(-20,43),(0,23)]), fill=blue)
    d.polygon(P([(0,0),( 31.5,31.5),( 20,43),(0,23)]), fill=red)

def lockup_h(d, x, y, mark_h=40, dark=False):
    sc = mark_h / 43.0
    chevron(d, x + 31.5 * sc, y, sc)
    tx = x + 63 * sc + 16
    c1 = WHITE if dark else NAVY
    ttext(d, tx, y + mark_h * 0.5, "PARITY", F("ExtraBold", mark_h * 0.62), c1, tr=1.5, anchor="lm")
    pw = text_w(d, "PARITY", F("ExtraBold", mark_h * 0.62), 1.5)
    ttext(d, tx + pw + 8, y + mark_h * 0.5, "LENDING", F("Regular", mark_h * 0.62), c1, tr=1.5, anchor="lm")

def cover(path, w, h, focal=(0.5, 0.5), target=(0.5, 0.5)):
    """Scale to cover w x h; place source focal point at target fraction of the box."""
    im = Image.open(path).convert("RGB")
    r = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * r * S) + 1, int(im.height * r * S) + 1), Image.LANCZOS)
    x0 = int(im.width * focal[0] - sx(w) * target[0]); y0 = int(im.height * focal[1] - sx(h) * target[1])
    x0 = max(0, min(im.width - sx(w), x0)); y0 = max(0, min(im.height - sx(h), y0))
    return im.crop((x0, y0, x0 + sx(w), y0 + sx(h)))

def icon(d, cx, cy, kind):
    """Simple line icons inside a red ring. cx,cy center in 1x coords."""
    R = 30
    d.ellipse([sx(cx-R), sx(cy-R), sx(cx+R), sx(cy+R)], outline=RED, width=sx(2.5))
    lw = sx(2.6)
    if kind == "house":
        pts = [(cx, cy-14),(cx+15, cy-1),(cx+15, cy+13),(cx-15, cy+13),(cx-15, cy-1)]
        d.polygon([(sx(x),sx(y)) for x,y in pts], outline=NAVY, width=lw)
        d.line([sx(cx-19),sx(cy+1),sx(cx),sx(cy-16),sx(cx+19),sx(cy+1)], fill=NAVY, width=lw, joint="curve")
    elif kind == "gauge":
        d.arc([sx(cx-16),sx(cy-12),sx(cx+16),sx(cy+20)], 180, 360, fill=NAVY, width=lw)
        d.line([sx(cx),sx(cy+4),sx(cx+9),sx(cy-6)], fill=RED, width=lw)
        d.ellipse([sx(cx-3),sx(cy+1),sx(cx+3),sx(cy+7)], fill=NAVY)
    elif kind == "rent":
        # building + key rows
        d.rectangle([sx(cx-14),sx(cy-16),sx(cx+6),sx(cy+16)], outline=NAVY, width=lw)
        for yy in (-9,-2,5):
            d.line([sx(cx-9),sx(cy+yy),sx(cx+1),sx(cy+yy)], fill=NAVY, width=lw)
        d.ellipse([sx(cx+6),sx(cy+2),sx(cx+20),sx(cy+16)], outline=RED, width=lw)
        d.text((sx(cx+13),sx(cy+9)), "$", font=F("Bold", 11), fill=RED, anchor="mm")
    elif kind == "nodoc":
        d.rectangle([sx(cx-11),sx(cy-16),sx(cx+11),sx(cy+16)], outline=NAVY, width=lw)
        for yy in (-8,-2,4):
            d.line([sx(cx-6),sx(cy+yy),sx(cx+6),sx(cy+yy)], fill=NAVY, width=lw)
        d.line([sx(cx-18),sx(cy+18),sx(cx+18),sx(cy-18)], fill=RED, width=sx(3.2))
    elif kind == "check":
        d.line([sx(cx-11),sx(cy+1),sx(cx-3),sx(cy+9),sx(cx+12),sx(cy-9)], fill=NAVY, width=sx(3.2), joint="curve")

# ---------------------------------------------------------------- MASTER
HERO_Y0, HERO_Y1 = 132, 828
PANEL_TOP_X, PANEL_BOT_X = 616, 500     # angled white panel right edge

def master(name, msg, photo=None):
    """msg = dict(eyebrow, h1 (list of lines), h2 (list of lines), sub)"""
    img = Image.new("RGB", (sx(W), sx(H)), WHITE)
    d = ImageDraw.Draw(img)

    # ---- header
    lockup_h(d, 72, 52, mark_h=40)
    pw = text_w(d, "DSCR LENDING NATIONWIDE", F("Bold", 14), 2.5) + 44
    rrect(d, (W-72-pw, 52, W-72, 92), 20, outline=NAVY, width=sx(1.6))
    ttext(d, W-72-pw/2, 72, "DSCR LENDING NATIONWIDE", F("Bold", 14), NAVY, tr=2.5, anchor="mm")

    # ---- hero band (rounded), photo or navy
    band = Image.new("RGB", (sx(W-144), sx(HERO_Y1-HERO_Y0)), NAVY)
    if photo:
        band = cover(photo, W-144, HERO_Y1-HERO_Y0, focal=FOCAL.get(os.path.basename(photo),(0.5,0.5)), target=(0.76,0.5))
    else:
        bd = ImageDraw.Draw(band)
        # full-colour brand chevron with a white keyline so it pops on navy
        cx, cy = (W-144) - 236, (HERO_Y1-HERO_Y0)/2 - 160
        sc = 6.8
        L = [(0,0),(-31.5,31.5),(-20,43),(0,23)]; Rr = [(0,0),(31.5,31.5),(20,43),(0,23)]
        def P(pts, o=0):  # o = outset in 1x px for the keyline
            return [(sx(cx + x*sc), sx(cy + y*sc)) for x,y in pts]
        # keyline: draw the union outline slightly larger by stroking
        outline = [(0,-0.0),(-31.5,31.5),(-20,43),(0,23),(20,43),(31.5,31.5)]
        bd.polygon(P(L), fill=BLUED)
        bd.polygon(P(Rr), fill=RED)
    mask = Image.new("L", band.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,band.width-1,band.height-1], radius=sx(30), fill=255)
    img.paste(band, (sx(72), sx(HERO_Y0)), mask)
    d = ImageDraw.Draw(img)

    # ---- angled white panel over left of hero (carries the type)
    poly = [(72, HERO_Y0), (PANEL_TOP_X, HERO_Y0), (PANEL_BOT_X, HERO_Y1), (72, HERO_Y1)]
    # re-round the left corners by clipping with same mask: draw panel onto a layer then paste with mask
    layer = Image.new("RGB", img.size, WHITE)
    lm = Image.new("L", img.size, 0)
    ImageDraw.Draw(lm).polygon([(sx(x),sx(y)) for x,y in poly], fill=255)
    big = Image.new("L", img.size, 0)
    ImageDraw.Draw(big).rounded_rectangle([sx(72),sx(HERO_Y0),sx(W-72)-1,sx(HERO_Y1)-1], radius=sx(30), fill=255)
    from PIL import ImageChops
    lm = ImageChops.multiply(lm, big)
    img.paste(layer, (0,0), lm)
    d = ImageDraw.Draw(img)
    # red accent stripe along the angle
    d.line([sx(PANEL_TOP_X), sx(HERO_Y0), sx(PANEL_BOT_X), sx(HERO_Y1)], fill=RED, width=sx(7))

    # ---- hero type (constant hierarchy); every line auto-fits under the diagonal
    x = 112
    def avail(yy):   # usable width at row yy (panel edge minus safe gap)
        edge = PANEL_TOP_X - (yy - HERO_Y0) / (HERO_Y1 - HERO_Y0) * (PANEL_TOP_X - PANEL_BOT_X)
        return edge - 34 - x
    def fit(txt, weight, size, yy, tr=0):
        f = F(weight, size)
        while text_w(d, txt, f, tr) > avail(yy) and size > 12:
            size -= 0.5; f = F(weight, size)
        return f, size
    block_h = 44 + 3*72 + 14 + 43*len(msg["h2"]) + 10 + 29*len(msg["sub"]) - 12
    y = HERO_Y0 + (HERO_Y1 - HERO_Y0 - block_h) / 2 - 24
    ttext(d, x, y, msg["eyebrow"], F("Bold", 16), RED, tr=3.5)
    y += 44
    for ln in ["DSCR HOME", "INVESTOR", "LOANS"]:
        f, _ = fit(ln, "Black", 68, y + 60, tr=-0.5)
        ttext(d, x, y, ln, f, NAVY, tr=-0.5)
        y += 72
    y += 14
    for ln in msg["h2"]:
        f, _ = fit(ln, "ExtraBold", 33, y + 36)
        ttext(d, x, y, ln, f, RED)
        y += 43
    y += 10
    for ln in msg["sub"]:
        f, _ = fit(ln, "Medium", 19.5, y + 24)
        ttext(d, x, y, ln, f, SLATE)
        y += 29

    # ---- spec strip (4 icons)
    sy = HERO_Y1 + 52
    cols = [("house", "20%+ down", "or equity"),
            ("gauge", "620+ credit", "score"),
            ("rent",  "Qualify on", "rental income"),
            ("nodoc", "No tax returns", "required")]
    cw = (W - 144) / 4
    for i, (k, l1, l2) in enumerate(cols):
        cx = 72 + cw * i + cw / 2
        icon(d, cx, sy + 30, k)
        ttext(d, cx, sy + 84, l1, F("Bold", 20), NAVY, anchor="ma")
        ttext(d, cx, sy + 110, l2, F("Medium", 18), SLATE, anchor="ma")
    ttext(d, W/2, sy + 162, "INVESTMENT PROPERTIES ONLY   ·   PURCHASE · REFINANCE · CASH OUT   ·   SFR · CONDOS · 2-4 UNITS",
          F("SemiBold", 14.5), NAVY, tr=1.2, anchor="ma")

    # ---- CTA bar
    by0, by1 = sy + 208, sy + 340
    rrect(d, (72, by0, W-72, by1), 26, fill=NAVY)
    ttext(d, 112, by0 + 44, "See if you qualify in six quick questions.", F("SemiBold", 23), WHITE)
    ttext(d, 112, by0 + 80, "No credit pull.  paritylending.com/dscr", F("Medium", 19), (196, 204, 226))
    lab = "SEE IF YOU QUALIFY"
    bw = text_w(d, lab, F("Bold", 18), 2) + 72
    rrect(d, (W-72-40-bw, by0 + 34, W-72-40, by1 - 34), 32, fill=RED)
    ttext(d, W-72-40-bw/2, (by0+by1)/2, lab, F("Bold", 18), WHITE, tr=2, anchor="mm")

    # ---- fine print
    ttext(d, W/2, H - 76, "Business-purpose loans for non-owner-occupied investment property only.", F("Regular", 13.5), SLATE, anchor="ma")
    ttext(d, W/2, H - 52, "© 2026 Parity Lending  ·  DSCR Lending Nationwide", F("Regular", 13.5), SLATE, anchor="ma")

    out = img.resize((W, H), Image.LANCZOS)
    os.makedirs("/tmp/v8/out", exist_ok=True)
    out.save(f"/tmp/v8/out/{name}", quality=95)
    return out

MSGS = {
 "01-negation": dict(eyebrow="FOR REAL ESTATE INVESTORS",
     h2=["No tax returns. No W-2s.", "The property qualifies."],
     sub=["If the rent covers the payment,", "you have a deal."]),
 "02-specsheet": dict(eyebrow="BUYING OR REFINANCING A RENTAL?",
     h2=["Qualified on the rent,", "not your paperwork."],
     sub=["80% max LTV. Close in an LLC", "or your personal name."]),
 "03-rehab": dict(eyebrow="FOR FLIPPERS & BRRRR INVESTORS",
     h2=["The rehab is done.", "Lock in the long-term loan."],
     sub=["Refi into 30-year money on the", "rent it earns. Capital comes back out."]),
 "04-notalead": dict(eyebrow="SHOPPING DSCR QUOTES?",
     h2=["You're a borrower.", "Not a lead."],
     sub=["One lender. No call lists.", "Your information is never resold."]),
 "05-serious": dict(eyebrow="BUILT FOR THE SERIOUS INVESTOR",
     h2=["Scaling a portfolio?", "This is the loan for it."],
     sub=["Qualify on rental income.", "Purchase, refinance or cash out."]),
 "06-stop": dict(eyebrow="STILL PAYING HARD MONEY RATES?",
     h2=["Hard money was the bridge.", "This is the exit."],
     sub=["Move to long-term DSCR financing", "qualified on the rent."]),
}
FOCAL = {"p11.jpg":(0.5,0.5),"p16.jpg":(0.5,0.5),"p10.jpg":(0.5,0.5),"p15.jpg":(0.62,0.5),"p6.jpg":(0.5,0.5),"p4.jpg":(0.42,0.5),"p14.jpg":(0.5,0.5)}
PHOTOS = {"01-negation":"p11.jpg","02-specsheet":"p16.jpg","03-rehab":"p10.jpg",
          "04-notalead":"p15.jpg","05-serious":"p6.jpg","06-stop":"p4.jpg"}

if __name__ == "__main__":
    import sys
    keys = sys.argv[1:] or list(MSGS)
    for k in keys:
        master(f"parity-v8-{k}-A.png", MSGS[k], photo="/tmp/v8/photos/"+PHOTOS[k])
        master(f"parity-v8-{k}-B.png", MSGS[k], photo=None)
        print("ok", k)
