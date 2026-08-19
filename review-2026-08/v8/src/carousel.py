import sys; sys.path.insert(0,'/tmp/v8')
from gen_v8 import *
from PIL import ImageChops

def card1(name, photo):
    img = Image.new("RGB", (sx(W), sx(H)), WHITE); d = ImageDraw.Draw(img)
    # header
    lockup_h(d, 72, 52, mark_h=40)
    pw = text_w(d, "DSCR LENDING NATIONWIDE", F("Bold", 14), 2.5) + 44
    rrect(d, (W-72-pw, 52, W-72, 92), 20, outline=NAVY, width=sx(1.6))
    ttext(d, W-72-pw/2, 72, "DSCR LENDING NATIONWIDE", F("Bold", 14), NAVY, tr=2.5, anchor="mm")
    # hero band, same geometry as the master
    band = cover(photo, W-144, HERO_Y1-HERO_Y0, focal=(0.5,0.5), target=(0.76,0.5))
    mask = Image.new("L", band.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,band.width-1,band.height-1], radius=sx(30), fill=255)
    img.paste(band, (sx(72), sx(HERO_Y0)), mask); d = ImageDraw.Draw(img)
    poly = [(72, HERO_Y0), (PANEL_TOP_X, HERO_Y0), (PANEL_BOT_X, HERO_Y1), (72, HERO_Y1)]
    layer = Image.new("RGB", img.size, WHITE); lm = Image.new("L", img.size, 0)
    ImageDraw.Draw(lm).polygon([(sx(x),sx(y)) for x,y in poly], fill=255)
    big = Image.new("L", img.size, 0)
    ImageDraw.Draw(big).rounded_rectangle([sx(72),sx(HERO_Y0),sx(W-72)-1,sx(HERO_Y1)-1], radius=sx(30), fill=255)
    img.paste(layer, (0,0), ImageChops.multiply(lm, big)); d = ImageDraw.Draw(img)
    d.line([sx(PANEL_TOP_X), sx(HERO_Y0), sx(PANEL_BOT_X), sx(HERO_Y1)], fill=RED, width=sx(7))
    # type: eyebrow, then the hook as the biggest thing on the card, then product line, then sub
    x = 112
    def avail(yy):
        edge = PANEL_TOP_X - (yy - HERO_Y0) / (HERO_Y1 - HERO_Y0) * (PANEL_TOP_X - PANEL_BOT_X)
        return edge - 34 - x
    def fit(txt, weight, size, yy, tr=0):
        f = F(weight, size)
        while text_w(d, txt, f, tr) > avail(yy) and size > 12:
            size -= 0.5; f = F(weight, size)
        return f
    y = HERO_Y0 + 60
    # product name FIRST and big, in the master's stack style
    lines=["DSCR HOME","INVESTOR","LOANS"]
    sz=min(fit(ln,"Black",68,y+i*72+60,tr=-0.5).size/2 for i,ln in enumerate(lines))
    for i,ln in enumerate(lines):
        ttext(d, x, y, ln, F("Black", sz), NAVY, tr=-0.5); y += int(sz*1.06)
    y += 18
    ttext(d, x, y, "HOW WE QUALIFY YOU", F("Bold", 16), RED, tr=3.5); y += 40
    for ln in ["The four things", "we look at."]:
        ttext(d, x, y, ln, fit(ln, "ExtraBold", 40, y+40), RED); y += 50
    y += 10
    for ln in ["No W-2s. No tax returns.", "No debt-to-income ratio."]:
        ttext(d, x, y, ln, fit(ln, "Medium", 21, y+26), SLATE); y += 31
    # below the hero: the four numbered rings as a preview strip, muted, with "swipe"
    sy = HERO_Y1 + 58
    cols = [("house","1","The property"),("pct","2","Your equity"),("gauge","3","Your credit"),("rent","4","The rent")]
    cw = (W-144)/4
    for i,(k,n,lab) in enumerate(cols):
        cx = 72 + cw*i + cw/2
        if k=="pct":
            R=30; d.ellipse([sx(cx-R),sx(sy+30-R),sx(cx+R),sx(sy+30+R)], outline=RED, width=sx(2.5))
            ttext(d, cx, sy+31, "%", F("Bold", 30), NAVY, anchor="mm")
        else:
            icon(d, cx, sy+30, k)
        # number badge
        d.ellipse([sx(cx+16),sx(sy-4),sx(cx+40),sx(sy+20)], fill=NAVY)
        ttext(d, cx+28, sy+8, n, F("Bold", 13), WHITE, anchor="mm")
        ttext(d, cx, sy+84, lab, F("Bold", 19), NAVY, anchor="ma")
    # swipe bar
    by0, by1 = sy+150, sy+262
    rrect(d, (72, by0, W-72, by1), 26, fill=NAVY)
    ttext(d, 112, (by0+by1)/2, "Tick all four and you're a fit. Swipe to check.", F("SemiBold", 24), WHITE, anchor="lm")
    # arrow chevron pill right
    rrect(d, (W-72-40-96, by0+28, W-72-40, by1-28), 28, fill=RED)
    ttext(d, W-72-40-48, (by0+by1)/2, "→", F("Bold", 30), WHITE, anchor="mm")
    # dots (5 cards)
    for i in range(6):
        cx = W/2 - 2.5*22 + i*22
        r = 5
        d.ellipse([sx(cx-r),sx(by1+34-r),sx(cx+r),sx(by1+34+r)], fill=NAVY if i==0 else (200,206,220))
    ttext(d, W/2, H-76, "Business-purpose loans for non-owner-occupied investment property only.", F("Regular", 13.5), SLATE, anchor="ma")
    ttext(d, W/2, H-52, "© 2026 Parity Lending  ·  DSCR Lending Nationwide", F("Regular", 13.5), SLATE, anchor="ma")
    img.resize((W,H), Image.LANCZOS).save(f"/tmp/v8/out/{name}", quality=95)

card1("parity-v8-carousel-c1-card1.png", "/tmp/v8/photos/p6.jpg")
print("ok")

def glyph(d, cx, cy, kind, k=3.2):
    lw = sx(2.6*k*0.9)
    if kind == "house":
        pts=[(0,-14),(15,-1),(15,13),(-15,13),(-15,-1)]
        d.polygon([(sx(cx+x*k),sx(cy+y*k)) for x,y in pts], outline=NAVY, width=lw)
        d.line([sx(cx-19*k),sx(cy+1*k),sx(cx),sx(cy-16*k),sx(cx+19*k),sx(cy+1*k)], fill=NAVY, width=lw, joint="curve")
    elif kind == "gauge":
        d.arc([sx(cx-16*k),sx(cy-12*k),sx(cx+16*k),sx(cy+20*k)],180,360,fill=NAVY,width=lw)
        d.line([sx(cx),sx(cy+4*k),sx(cx+9*k),sx(cy-6*k)],fill=RED,width=lw)
        d.ellipse([sx(cx-3*k),sx(cy+1*k),sx(cx+3*k),sx(cy+7*k)],fill=NAVY)
    elif kind == "rent":
        d.rectangle([sx(cx-14*k),sx(cy-16*k),sx(cx+6*k),sx(cy+16*k)],outline=NAVY,width=lw)
        for yy in (-9,-2,5): d.line([sx(cx-9*k),sx(cy+yy*k),sx(cx+1*k),sx(cy+yy*k)],fill=NAVY,width=lw)
        d.ellipse([sx(cx+6*k),sx(cy+2*k),sx(cx+20*k),sx(cy+16*k)],outline=RED,width=lw)
        ttext(d, cx+13*k, cy+9*k, "$", F("Bold", 11*k), RED, anchor="mm")

def crit_card(name, num, kind, title_lines, body_lines, not_lines, photo, total=6, idx=1, not_label="WHAT WE DON'T ASK FOR"):
    """Criterion card: big numbered ring icon + one plain sentence + what it does NOT require.
    Thin photo strip keeps the Parity look without repeating the hero."""
    img = Image.new("RGB", (sx(W), sx(H)), WHITE); d = ImageDraw.Draw(img)
    lockup_h(d, 72, 52, mark_h=40)
    pw = text_w(d, "DSCR LENDING NATIONWIDE", F("Bold", 14), 2.5) + 44
    rrect(d, (W-72-pw, 52, W-72, 92), 20, outline=NAVY, width=sx(1.6))
    ttext(d, W-72-pw/2, 72, "DSCR LENDING NATIONWIDE", F("Bold", 14), NAVY, tr=2.5, anchor="mm")
    # thin photo strip top with the red diagonal cutting its left end
    ST0, ST1 = 132, 372
    band = cover(photo, W-144, ST1-ST0, focal=(0.5,0.5), target=(0.7,0.5))
    mask = Image.new("L", band.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,band.width-1,band.height-1], radius=sx(30), fill=255)
    img.paste(band, (sx(72), sx(ST0)), mask); d = ImageDraw.Draw(img)
    # angled white wedge on left holding the step label
    poly = [(72, ST0), (392, ST0), (352, ST1), (72, ST1)]
    layer = Image.new("RGB", img.size, WHITE); lm = Image.new("L", img.size, 0)
    ImageDraw.Draw(lm).polygon([(sx(x),sx(y)) for x,y in poly], fill=255)
    big = Image.new("L", img.size, 0)
    ImageDraw.Draw(big).rounded_rectangle([sx(72),sx(ST0),sx(W-72)-1,sx(ST1)-1], radius=sx(30), fill=255)
    img.paste(layer, (0,0), ImageChops.multiply(lm, big)); d = ImageDraw.Draw(img)
    d.line([sx(392), sx(ST0), sx(352), sx(ST1)], fill=RED, width=sx(7))
    # wedge type: fit every line under the wedge's diagonal (edge 392 at top -> 352 at bottom)
    def wavail(yy):
        edge = 392 - (yy-ST0)/(ST1-ST0)*(392-352); return edge - 30 - 108
    def wfit(txt, weight, size, yy, tr=0):
        f=F(weight,size)
        while text_w(d, txt, f, tr) > wavail(yy) and size > 8: size -= 0.5; f=F(weight,size)
        return f
    ttext(d, 108, ST0+50, "HOW WE", wfit("HOW WE","ExtraBold",24,ST0+74,tr=2.5), RED, tr=2.5)
    ttext(d, 108, ST0+82, "QUALIFY YOU", wfit("QUALIFY YOU","ExtraBold",24,ST0+106,tr=2.5), RED, tr=2.5)
    ttext(d, 108, ST0+122, f"{num} of 4", wfit(f"{num} of 4","Black",50,ST0+172,tr=-0.5), NAVY, tr=-0.5)
    ttext(d, 108, ST0+188, "DSCR HOME INVESTOR LOANS", wfit("DSCR HOME INVESTOR LOANS","Bold",12,ST0+202,tr=2), SLATE, tr=2)
    # big ring icon left, text right
    cx, cy = 72+150, 620
    R = 118
    d.ellipse([sx(cx-R),sx(cy-R),sx(cx+R),sx(cy+R)], outline=RED, width=sx(6))
    if kind == "pct":
        ttext(d, cx, cy+4, "%", F("Bold", 120), NAVY, anchor="mm")
    else:
        # scale the small icon up by drawing at 3.5x via a temp layer
        glyph(d, cx, cy+4, kind, k=3.2)
    # number badge on the ring
    d.ellipse([sx(cx+62),sx(cy-118),sx(cx+118),sx(cy-62)], fill=NAVY)
    ttext(d, cx+90, cy-90, str(num), F("Bold", 28), WHITE, anchor="mm")
    tx = 72+330
    y = 470
    for ln in title_lines:
        ttext(d, tx, y, ln, F("Black", 60), NAVY, tr=-0.5); y += 66
    y += 14
    for ln in body_lines:
        ttext(d, tx, y, ln, F("Medium", 24), SLATE); y += 34
    # "does not require" block, full width below
    by = 800
    rrect(d, (72, by, W-72, by+150), 22, fill=MIST)
    ttext(d, 108, by+34, not_label, F("Bold", 14), RED, tr=3)
    yy = by+66
    xx = 108
    for ln in not_lines:
        # red slash mark then text, laid out in a row
        d.line([sx(xx), sx(yy+22), sx(xx+16), sx(yy+2)], fill=RED, width=sx(3))
        ttext(d, xx+26, yy, ln, F("SemiBold", 20.5), NAVY)
        xx += text_w(d, ln, F("SemiBold", 20.5)) + 26 + 36
    # nav bar
    by0, by1 = 1010, 1122
    rrect(d, (72, by0, W-72, by1), 26, fill=NAVY)
    ttext(d, 112, (by0+by1)/2, f"Next: {['the property','your equity','your credit','the rent','see if you qualify'][idx]}", F("SemiBold", 24), WHITE, anchor="lm")
    rrect(d, (W-72-40-96, by0+28, W-72-40, by1-28), 28, fill=RED)
    ttext(d, W-72-40-48, (by0+by1)/2, "→", F("Bold", 30), WHITE, anchor="mm")
    for i in range(total):
        cxd = W/2 - (total-1)/2*22 + i*22
        d.ellipse([sx(cxd-5),sx(by1+34-5),sx(cxd+5),sx(by1+34+5)], fill=NAVY if i==idx else (200,206,220))
    ttext(d, W/2, H-76, "Business-purpose loans for non-owner-occupied investment property only.", F("Regular", 13.5), SLATE, anchor="ma")
    ttext(d, W/2, H-52, "© 2026 Parity Lending  ·  DSCR Lending Nationwide", F("Regular", 13.5), SLATE, anchor="ma")
    img.resize((W,H), Image.LANCZOS).save(f"/tmp/v8/out/{name}", quality=95)

crit_card("parity-v8-carousel-c1-card2.png", 1, "house",
    ["The property", "is a rental."],
    ["Single-family, condo, or 2 to 4 units.", "Purchase, refinance, or cash out.", "Close in an LLC or your own name."],
    ["Not a primary residence", "Not a second home", "Not owner-occupied"],
    "/tmp/v8/photos/p11.jpg", idx=1, not_label="WHAT IT CAN'T BE")
print("ok")

crit_card("parity-v8-carousel-c1-card3.png", 2, "pct",
    ["You have 20%", "in it."],
    ["20% down on a purchase, or", "20% equity on a refinance or cash out.", "Gift funds allowed toward the down."],
    ["No W-2s", "No tax returns", "No debt-to-income ratio"],
    "/tmp/v8/photos/p6.jpg", idx=2)
print("card3 ok")

crit_card("parity-v8-carousel-c1-card4.png", 3, "gauge",
    ["Your credit is", "620 or better."],
    ["We look at the score, not your income.", "Stronger credit opens better terms,", "but 620 gets you in the door."],
    ["No income verification", "No employment letter", "No pay stubs"],
    "/tmp/v8/photos/p4.jpg", idx=3)
print("card4 ok")

crit_card("parity-v8-carousel-c1-card5.png", 4, "rent",
    ["The rent covers", "the payment."],
    ["That is the whole test. Rent in; principal,", "interest, taxes, insurance and HOA out.", "If the property pays for itself, the loan works."],
    ["No personal income", "No employment history", "No DTI"],
    "/tmp/v8/photos/p11.jpg", idx=4)
print("card5 ok")

def cta_card(name, photo, total=6, idx=5):
    img = Image.new("RGB", (sx(W), sx(H)), WHITE); d = ImageDraw.Draw(img)
    lockup_h(d, 72, 52, mark_h=40)
    pw = text_w(d, "DSCR LENDING NATIONWIDE", F("Bold", 14), 2.5) + 44
    rrect(d, (W-72-pw, 52, W-72, 92), 20, outline=NAVY, width=sx(1.6))
    ttext(d, W-72-pw/2, 72, "DSCR LENDING NATIONWIDE", F("Bold", 14), NAVY, tr=2.5, anchor="mm")
    # hero band: photo with the angled panel, same as the master, but the panel carries the recap
    band = cover(photo, W-144, HERO_Y1-HERO_Y0, focal=(0.5,0.5), target=(0.76,0.5))
    mask = Image.new("L", band.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0,0,band.width-1,band.height-1], radius=sx(30), fill=255)
    img.paste(band, (sx(72), sx(HERO_Y0)), mask); d = ImageDraw.Draw(img)
    poly = [(72, HERO_Y0), (PANEL_TOP_X, HERO_Y0), (PANEL_BOT_X, HERO_Y1), (72, HERO_Y1)]
    layer = Image.new("RGB", img.size, WHITE); lm = Image.new("L", img.size, 0)
    ImageDraw.Draw(lm).polygon([(sx(x),sx(y)) for x,y in poly], fill=255)
    big = Image.new("L", img.size, 0)
    ImageDraw.Draw(big).rounded_rectangle([sx(72),sx(HERO_Y0),sx(W-72)-1,sx(HERO_Y1)-1], radius=sx(30), fill=255)
    img.paste(layer, (0,0), ImageChops.multiply(lm, big)); d = ImageDraw.Draw(img)
    d.line([sx(PANEL_TOP_X), sx(HERO_Y0), sx(PANEL_BOT_X), sx(HERO_Y1)], fill=RED, width=sx(7))
    x = 112
    def avail(yy):
        edge = PANEL_TOP_X - (yy - HERO_Y0) / (HERO_Y1 - HERO_Y0) * (PANEL_TOP_X - PANEL_BOT_X)
        return edge - 34 - x
    def fit(txt, weight, size, yy, tr=0):
        f = F(weight, size)
        while text_w(d, txt, f, tr) > avail(yy) and size > 12:
            size -= 0.5; f = F(weight, size)
        return f
    y = HERO_Y0 + 60
    lines=["DSCR HOME","INVESTOR","LOANS"]
    sz=min(fit(ln,"Black",68,y+i*72+60,tr=-0.5).size/2 for i,ln in enumerate(lines))
    for i,ln in enumerate(lines):
        ttext(d, x, y, ln, F("Black", sz), NAVY, tr=-0.5); y += int(sz*1.06)
    y += 18
    ttext(d, x, y, "TICKED ALL FOUR?", F("Bold", 16), RED, tr=3.5); y += 40
    for ln in ["See if you", "qualify."]:
        ttext(d, x, y, fit(ln, "ExtraBold", 40, y+40) and ln, fit(ln, "ExtraBold", 40, y+40), RED); y += 50
    y += 10
    for ln in ["Six quick questions.", "No credit pull. No obligation."]:
        ttext(d, x, y, ln, fit(ln, "Medium", 21, y+26), SLATE); y += 31
    # recap row: the four rings with checks
    sy = HERO_Y1 + 58
    cols = [("house","The property"),("pct","Your equity"),("gauge","Your credit"),("rent","The rent")]
    cw = (W-144)/4
    for i,(k,lab) in enumerate(cols):
        cx = 72 + cw*i + cw/2
        if k=="pct":
            R=30; d.ellipse([sx(cx-R),sx(sy+30-R),sx(cx+R),sx(sy+30+R)], outline=RED, width=sx(2.5))
            ttext(d, cx, sy+31, "%", F("Bold", 30), NAVY, anchor="mm")
        else:
            icon(d, cx, sy+30, k)
        # check badge
        d.ellipse([sx(cx+16),sx(sy-4),sx(cx+40),sx(sy+20)], fill=NAVY)
        d.line([sx(cx+22),sx(sy+8),sx(cx+26),sx(sy+12),sx(cx+34),sx(sy+3)], fill=WHITE, width=sx(2.2), joint="curve")
        ttext(d, cx, sy+84, lab, F("Bold", 19), NAVY, anchor="ma")
    # CTA bar, URL large
    by0, by1 = sy+150, sy+296
    rrect(d, (72, by0, W-72, by1), 26, fill=NAVY)
    ttext(d, 112, by0+40, "paritylending.com/dscr", F("Bold", 34), WHITE)
    ttext(d, 112, by0+92, "A real person follows up. Your info stays put.", F("Medium", 18), (196,204,226))
    lab = "SEE IF YOU QUALIFY"; f = F("Bold", 18)
    bw = text_w(d, lab, f, 2) + 72
    rrect(d, (W-72-40-bw, by0+40, W-72-40, by1-40), 33, fill=RED)
    ttext(d, W-72-40-bw/2, (by0+by1)/2, lab, f, WHITE, tr=2, anchor="mm")
    for i in range(total):
        cxd = W/2 - (total-1)/2*22 + i*22
        d.ellipse([sx(cxd-5),sx(by1+34-5),sx(cxd+5),sx(by1+34+5)], fill=NAVY if i==idx else (200,206,220))
    ttext(d, W/2, H-76, "Business-purpose loans for non-owner-occupied investment property only.", F("Regular", 13.5), SLATE, anchor="ma")
    ttext(d, W/2, H-52, "© 2026 Parity Lending  ·  DSCR Lending Nationwide", F("Regular", 13.5), SLATE, anchor="ma")
    img.resize((W,H), Image.LANCZOS).save(f"/tmp/v8/out/{name}", quality=95)

cta_card("parity-v8-carousel-c1-card6.png", "/tmp/v8/photos/p14.jpg")
print("card6 ok")
