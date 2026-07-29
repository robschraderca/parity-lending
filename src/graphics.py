# Custom brand SVG / CSS graphics, Ameritrust palette only.
# Red #D43426  Navy #101A35  Silver #AEB1BD  Rose #E08A80  LGray #EBECEF
# Peri #7C8AC4  Sage #8DAE9B  Steel #758C9C  Off #F9F9F9

GFX_CSS = r"""
/* --- bar comparison --- */
.barcmp{display:grid;gap:20px}
.barcmp .blab{display:flex;justify-content:space-between;align-items:baseline;font-size:.86rem;margin-bottom:9px}
.barcmp .blab span{color:var(--muted);font-weight:550}
.barcmp .blab b{font-family:'Sora',sans-serif;font-size:1.02rem;color:var(--navy);font-variant-numeric:tabular-nums}
.barcmp .btrack{height:32px;background:var(--lgray);border-radius:6px;overflow:hidden}
.barcmp .bfill{height:100%;width:0;border-radius:6px;transition:width 1.2s cubic-bezier(.22,1,.36,1)}
.bf-navy{background:linear-gradient(90deg,#101A35,#2E4BB0)}
.bf-red{background:linear-gradient(90deg,#D43426,#E8564A)}
.bf-silver{background:linear-gradient(90deg,#7C8AC4,#AEB1BD)}
.bf-steel{background:linear-gradient(90deg,#5F7585,#758C9C)}

/* --- ratio meter --- */
.meter{margin-top:6px}
.meter .mtrack{position:relative;height:16px;border-radius:8px;overflow:hidden;display:flex}
.meter .mseg{height:100%}
.meter .mticks{display:flex;margin-top:9px;font-size:.7rem;color:var(--dim);letter-spacing:.04em;font-weight:600}
.meter .mticks div{text-align:center}
.meter .mpoint{position:absolute;top:-7px;width:3px;height:30px;background:var(--navy);border-radius:2px;
  transform:translateX(-50%);transition:left 1.2s cubic-bezier(.22,1,.36,1)}

/* --- LTV stack --- */
.ltvstack{display:grid;gap:16px}
.ltvrow .lhead{display:flex;justify-content:space-between;font-size:.84rem;margin-bottom:8px;color:var(--muted);font-weight:550}
.ltvrow .lhead b{color:var(--navy);font-family:'Sora',sans-serif}
.ltvrow .ltrack{display:flex;height:30px;border-radius:6px;overflow:hidden;border:1px solid var(--line)}
.ltvrow .lloan{background:linear-gradient(90deg,#101A35,#2E4BB0);display:grid;place-items:center;
  color:#fff;font-size:.73rem;font-weight:700;letter-spacing:.05em;transition:width 1.2s cubic-bezier(.22,1,.36,1);width:0}
.ltvrow .ldown{background:var(--lgray);flex:1;display:grid;place-items:center;color:var(--navy);
  font-size:.73rem;font-weight:700;letter-spacing:.05em}

/* --- doc compare --- */
.doccmp{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:700px){.doccmp{grid-template-columns:1fr}}
.doccol{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;box-shadow:var(--sh)}
.doccol .dh{padding:16px 20px;font-family:'Sora',sans-serif;font-weight:700;font-size:.98rem;
  display:flex;align-items:center;justify-content:space-between;gap:12px}
.doccol.a .dh{background:var(--lgray);color:var(--navy)}
.doccol.b .dh{background:var(--navy);color:#fff}
.doccol ul{list-style:none;margin:0;padding:14px 20px 18px}
.doccol li{display:flex;gap:10px;align-items:flex-start;margin:9px 0;font-size:.9rem;color:var(--muted)}
.doccol li svg{flex:none;margin-top:3px}
.doccnt{font-size:.72rem;font-weight:700;letter-spacing:.08em;padding:3px 9px;border-radius:100px}
.doccol.a .doccnt{background:#fff;color:var(--red);border:1px solid rgba(212,52,38,.3)}
.doccol.b .doccnt{background:rgba(255,255,255,.16);color:#fff}

/* --- icon tiles --- */
.icogrid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:760px){.icogrid{grid-template-columns:repeat(2,1fr)}}
.icotile{border:1px solid var(--line);border-radius:13px;padding:22px 16px;text-align:center;background:#fff;
  box-shadow:var(--sh);transition:.2s}
.icotile:hover{transform:translateY(-3px);box-shadow:var(--sh-l);border-color:var(--line2)}
.icotile svg{margin:0 auto 12px;display:block}
.icotile b{display:block;font-family:'Sora',sans-serif;font-size:.95rem;color:var(--navy);font-weight:650}
.icotile span{display:block;font-size:.79rem;color:var(--dim);margin-top:4px}

/* --- cycle flow --- */
.cycle{width:100%;height:auto}
"""

X_MARK = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none">'
          '<path d="M4 4l8 8M12 4l-8 8" stroke="#D43426" stroke-width="2.1" stroke-linecap="round"/></svg>')
CK_NAVY = ('<svg width="15" height="15" viewBox="0 0 16 16" fill="none">'
           '<path d="M13.5 4.5L6.2 11.8 2.5 8.1" stroke="#101A35" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')


# ---------------------------------------------------------------- rent vs pitia
def rent_vs_pitia(rent="$2,400", pitia="$1,920", rent_w="100%", pitia_w="80%",
                  ratio="1.25", verdict="Standard tier, qualifies"):
    return f"""<div class="gfx-card">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;margin-bottom:22px">
    <div>
      <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.04rem;color:var(--navy)">Rent against payment</div>
      <div style="font-size:.83rem;color:var(--dim)">The only comparison that decides the loan</div>
    </div>
    <div style="text-align:right">
      <div style="font-family:'Sora',sans-serif;font-size:2rem;font-weight:800;color:var(--navy);line-height:1">{ratio}</div>
      <div style="font-size:.68rem;letter-spacing:.13em;text-transform:uppercase;color:var(--dim);font-weight:700">DSCR</div>
    </div>
  </div>
  <div class="barcmp">
    <div class="brow">
      <div class="blab"><span>Gross monthly rent</span><b>{rent}</b></div>
      <div class="btrack"><div class="bfill bf-navy" data-w="{rent_w}"></div></div>
    </div>
    <div class="brow">
      <div class="blab"><span>Monthly PITIA</span><b>{pitia}</b></div>
      <div class="btrack"><div class="bfill bf-red" data-w="{pitia_w}"></div></div>
    </div>
  </div>
  <div style="margin-top:20px;padding-top:16px;border-top:1px solid var(--line);font-size:.86rem;color:var(--muted)">
    Rent covers the payment <strong>{ratio} times over</strong>. {verdict}
  </div>
</div>"""


# ---------------------------------------------------------------- tier meter
def tier_meter(pointer="72%"):
    return f"""<div class="gfx-card">
  <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.04rem;color:var(--navy);margin-bottom:4px">
    How lenders read the number</div>
  <div style="font-size:.83rem;color:var(--dim);margin-bottom:22px">Four bands, four different conversations</div>
  <div class="meter">
    <div class="mtrack">
      <div class="mseg" style="width:24%;background:#D43426"></div>
      <div class="mseg" style="width:24%;background:#E08A80"></div>
      <div class="mseg" style="width:26%;background:#7C8AC4"></div>
      <div class="mseg" style="width:26%;background:#101A35"></div>
      <div class="mpoint" style="left:{pointer}"></div>
    </div>
    <div class="mticks">
      <div style="width:24%">&lt;0.80</div><div style="width:24%">0.80-0.99</div>
      <div style="width:26%">1.00-1.24</div><div style="width:26%">1.25+</div>
    </div>
  </div>
  <div style="margin-top:24px">
    <div class="row"><span><b class="bad" style="font-size:1rem;font-family:'Sora',sans-serif">&lt;0.80</b> &nbsp;Restructure</span><b style="color:var(--muted);font-weight:500;font-size:.86rem">More down, or no-ratio</b></div>
    <div class="row"><span><b class="warn" style="font-size:1rem;font-family:'Sora',sans-serif">0.80-0.99</b> &nbsp;Workable</span><b style="color:var(--muted);font-weight:500;font-size:.86rem">Reduced LTV, 660+ FICO</b></div>
    <div class="row"><span><b style="font-size:1rem;font-family:'Sora',sans-serif;color:var(--navy)">1.00-1.24</b> &nbsp;Qualifies</span><b style="color:var(--muted);font-weight:500;font-size:.86rem">Standard tier</b></div>
    <div class="row"><span><b class="ok" style="font-size:1rem;font-family:'Sora',sans-serif">1.25+</b> &nbsp;Strong</span><b style="color:var(--muted);font-weight:500;font-size:.86rem">Best pricing tier</b></div>
  </div>
</div>"""


# ---------------------------------------------------------------- LTV stack
def ltv_stack():
    rows = [
        ("Purchase", "80% LTV", "80%", "20% down"),
        ("Rate and term refinance", "75% LTV", "75%", "25% equity"),
        ("Cash-out refinance", "70-75% LTV", "72%", "28% equity"),
        ("Foreign national", "65-70% LTV", "68%", "32% down"),
    ]
    body = "".join(f"""<div class="ltvrow">
      <div class="lhead"><span>{a}</span><b>{b}</b></div>
      <div class="ltrack"><div class="lloan" data-w="{w}">Loan</div><div class="ldown">{d}</div></div>
    </div>""" for a, b, w, d in rows)
    return f"""<div class="gfx-card">
  <div style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.04rem;color:var(--navy);margin-bottom:4px">
    Maximum leverage by program</div>
  <div style="font-size:.83rem;color:var(--dim);margin-bottom:22px">Navy is borrowed. Grey is your capital.</div>
  <div class="ltvstack">{body}</div>
  <div style="margin-top:18px;font-size:.76rem;color:var(--dim)">Ceilings, not entitlements. Credit, ratio,
  loan size, and property type all move these.</div>
</div>"""


# ---------------------------------------------------------------- doc compare
def doc_compare():
    full = ["Two years of personal tax returns", "All K-1s and business returns",
            "Two years of W-2s", "30 days of pay stubs", "Verification of employment",
            "IRS transcript order (4506-C)", "Debt-to-income worksheet",
            "Letters of explanation", "Financed-property count schedule",
            "Reserves against every property owned"]
    dscr = ["Credit report", "Appraisal with rent schedule", "Lease or market rent estimate",
            "Entity documents and EIN letter", "Insurance binder", "Two months of reserves"]
    a = "".join(f"<li>{X_MARK}<span>{x}</span></li>" for x in full)
    b = "".join(f"<li>{CK_NAVY}<span>{x}</span></li>" for x in dscr)
    return f"""<div class="doccmp">
  <div class="doccol a">
    <div class="dh">Conventional full-doc file <span class="doccnt">10 items</span></div>
    <ul>{a}</ul>
  </div>
  <div class="doccol b">
    <div class="dh">DSCR file <span class="doccnt">6 items</span></div>
    <ul>{b}</ul>
  </div>
</div>"""


# ---------------------------------------------------------------- BRRRR cycle
BRRRR = """<svg class="cycle" viewBox="0 0 760 230" fill="none" xmlns="http://www.w3.org/2000/svg" role="img"
  aria-label="Buy, rehab, rent, refinance, repeat cycle">
  <defs>
    <marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
      <path d="M0 0.8L8 4.5L0 8.2z" fill="#AEB1BD"/>
    </marker>
    <marker id="arR" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
      <path d="M0 0.8L8 4.5L0 8.2z" fill="#D43426"/>
    </marker>
  </defs>
  %BOXES%
  %ARROWS%
  <path d="M683 126 C 683 186, 660 196, 380 196 C 100 196, 75 186, 75 126"
        stroke="#D43426" stroke-width="1.8" stroke-dasharray="5 5" fill="none" marker-end="url(#arR)"/>
  <rect x="330" y="182" width="100" height="28" rx="14" fill="#D43426"/>
  <text x="380" y="200" text-anchor="middle" font-family="Sora,sans-serif" font-size="12.5"
        font-weight="700" fill="#FFFFFF" letter-spacing="1">REPEAT</text>
</svg>"""


def _brrrr():
    labels = [("01", "Buy", "Cash or hard money"),
              ("02", "Rehab", "Force appreciation"),
              ("03", "Rent", "Sign a lease"),
              ("04", "Refinance", "DSCR cash-out"),
              ("05", "Recycle", "Capital back out")]
    boxes, arrows = [], []
    x = 10
    for i, (n, t, s) in enumerate(labels):
        boxes.append(
            f'<rect x="{x}" y="34" width="130" height="88" rx="11" fill="#FFFFFF" stroke="#E6E8EE" stroke-width="1.5"/>'
            f'<rect x="{x}" y="34" width="130" height="3.5" rx="2" fill="{"#D43426" if i in (0,3) else "#101A35"}"/>'
            f'<text x="{x+16}" y="62" font-family="Sora,sans-serif" font-size="11" font-weight="700" '
            f'fill="#8A93A8" letter-spacing="1.4">{n}</text>'
            f'<text x="{x+16}" y="88" font-family="Sora,sans-serif" font-size="17" font-weight="700" fill="#101A35">{t}</text>'
            f'<text x="{x+16}" y="108" font-family="Inter,sans-serif" font-size="11.5" fill="#5A6485">{s}</text>')
        if i < 4:
            arrows.append(f'<path d="M{x+136} 78 L{x+145} 78" stroke="#AEB1BD" stroke-width="1.8" marker-end="url(#ar)"/>')
        x += 152
    return BRRRR.replace("%BOXES%", "".join(boxes)).replace("%ARROWS%", "".join(arrows))


BRRRR_SVG = _brrrr()


# ---------------------------------------------------------------- property icons
def _ico(paths, size=44):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 48 48" fill="none" '
            f'xmlns="http://www.w3.org/2000/svg">{paths}</svg>')


N = 'stroke="#101A35" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
R = 'stroke="#D43426" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'

ICO_SFR = _ico(f'<path d="M8 22L24 9l16 13" {N}/><path d="M12 25v14h24V25" {N}/>'
               f'<path d="M20 39v-9h8v9" {R}/>')
ICO_DUPLEX = _ico(f'<path d="M6 21l9-9 9 9" {N}/><path d="M24 21l9-9 9 9" {N}/>'
                  f'<path d="M9 23v16h30V23" {N}/><path d="M17 39v-8h5v8M26 39v-8h5v8" {R}/>')
ICO_CONDO = _ico(f'<rect x="12" y="7" width="24" height="34" rx="2.5" {N}/>'
                 f'<path d="M18 14h4M26 14h4M18 21h4M26 21h4M18 28h4M26 28h4" {N}/>'
                 f'<path d="M21 41v-6h6v6" {R}/>')
ICO_STR = _ico(f'<path d="M8 22L24 9l16 13" {N}/><path d="M12 25v14h24V25" {N}/>'
               f'<path d="M24 27.5l1.9 3.9 4.3.6-3.1 3 .7 4.3-3.8-2-3.8 2 .7-4.3-3.1-3 4.3-.6z" {R}/>')

PROPERTY_ICONS = f"""<div class="icogrid">
  <div class="icotile">{ICO_SFR}<b>Single-family</b><span>Detached or attached</span></div>
  <div class="icotile">{ICO_DUPLEX}<b>2-4 unit</b><span>Duplex to fourplex</span></div>
  <div class="icotile">{ICO_CONDO}<b>Condo / townhome</b><span>Warrantable</span></div>
  <div class="icotile">{ICO_STR}<b>Short-term rental</b><span>Airbnb and mid-term</span></div>
</div>"""


# ---------------------------------------------------------------- program icons
P_PURCHASE = _ico(f'<path d="M7 21L23 8l16 13" {N}/><path d="M11 24v15h18V24" {N}/>'
                  f'<path d="M36 29v10M31 34h10" {R}/>', 40)
P_RATETERM = _ico(f'<path d="M9 17h27l-6-6" {N}/><path d="M39 31H12l6 6" {R}/>', 40)
P_CASHOUT = _ico(f'<path d="M7 21L23 8l16 13" {N}/><path d="M11 24v15h18V24" {N}/>'
                 f'<circle cx="36" cy="34" r="7" {R}/><path d="M36 30.5v7M34 33h4" {R}/>', 40)
P_STR = _ico(f'<rect x="8" y="11" width="32" height="29" rx="3" {N}/>'
             f'<path d="M8 20h32M16 8v6M32 8v6" {N}/>'
             f'<path d="M24 26l1.6 3.3 3.6.5-2.6 2.5.6 3.6-3.2-1.7-3.2 1.7.6-3.6-2.6-2.5 3.6-.5z" {R}/>', 40)
P_PORTFOLIO = _ico(f'<rect x="6" y="18" width="14" height="22" rx="2" {N}/>'
                   f'<rect x="22" y="10" width="14" height="30" rx="2" {N}/>'
                   f'<path d="M10 24h6M10 30h6M26 16h6M26 22h6M26 28h6" {R}/>', 40)
P_FOREIGN = _ico(f'<circle cx="24" cy="24" r="16" {N}/><path d="M8 24h32" {N}/>'
                 f'<path d="M24 8c4.5 5 6.5 10.5 6.5 16S28.5 35 24 40c-4.5-5-6.5-10.5-6.5-16S19.5 13 24 8z" {R}/>', 40)

PROGRAM_ICONS = {
    "purchase": P_PURCHASE, "rateterm": P_RATETERM, "cashout": P_CASHOUT,
    "str": P_STR, "portfolio": P_PORTFOLIO, "foreign": P_FOREIGN,
}
