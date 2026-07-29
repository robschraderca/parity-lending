from config import *
from assets_data import *

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">"""

# ---------------------------------------------------------------------------
# Parity Lending palette, sampled straight out of the supplied logo file:
#   #D43426  chevron red      primary accent, CTAs, rules
#   #1A3796  chevron blue     secondary accent, bars, gradients
#   #101A35  wordmark navy    headings and dark type
#   #16224A  dark surface     footer, CTA band, stat band
#   #505979  wordmark grey    body copy
# Neutrals: #EBECEF lgray  #AEB1BD silver  #F9F9F9 offwhite
# ---------------------------------------------------------------------------

CSS = r"""
:root{
  --red:#D43426; --red-d:#B32A1E; --red-l:#E8564A;
  --navy:#101A35; --navy-d:#0A1128; --navy-l:#1A3796; --navy-bg:#16224A;
  --silver:#AEB1BD; --rose:#E08A80; --lgray:#EBECEF;
  --peri:#7C8AC4; --sage:#8DAE9B; --steel:#758C9C; --off:#F9F9F9;

  --bg:#FFFFFF; --bg2:var(--off); --surface:#FFFFFF;
  --line:#E6E8EE; --line2:#D3D7E1;
  --text:var(--navy); --body:#505979; --muted:#5A6485; --dim:#8A93A8;
  --acc:var(--red);
  --ok:#2E7A55; --warn:#B0740F; --bad:var(--red);

  --r:14px; --max:1180px;
  --sh:0 1px 2px rgba(16,26,53,.05), 0 8px 24px -12px rgba(16,26,53,.14);
  --sh-l:0 4px 10px rgba(16,26,53,.07), 0 20px 44px -18px rgba(16,26,53,.22);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth; -webkit-text-size-adjust:100%}
body{
  margin:0; background:var(--bg); color:var(--body);
  font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;
  font-size:16.5px; line-height:1.65; letter-spacing:-.004em;
  -webkit-font-smoothing:antialiased; overflow-x:hidden;
}
h1,h2,h3,h4,.dspl{font-family:'Sora',-apple-system,'Segoe UI',Helvetica,Arial,sans-serif;
  letter-spacing:-.03em; line-height:1.1; margin:0 0 .5em; color:var(--navy)}
h1{font-size:clamp(2.35rem,5.4vw,4.15rem); font-weight:800}
h2{font-size:clamp(1.8rem,3.5vw,2.8rem); font-weight:700}
h3{font-size:clamp(1.12rem,1.8vw,1.38rem); font-weight:650}
p{margin:0 0 1.05em}
a{color:var(--red); text-decoration:none}
a:hover{text-decoration:underline}
img,svg{max-width:100%}
ul{margin:0 0 1em; padding-left:1.15em}
li{margin:.3em 0}
strong{color:var(--navy); font-weight:650}
.wrap{max-width:var(--max); margin:0 auto; padding:0 24px}
.sec{padding:100px 0; position:relative}
.sec-tight{padding:66px 0}
.sec-alt{background:var(--bg2); border-top:1px solid var(--line); border-bottom:1px solid var(--line)}
.center{text-align:center}
.lead{font-size:1.13rem; color:var(--muted); max-width:64ch}
.center .lead{margin-left:auto;margin-right:auto}
.mono{font-variant-numeric:tabular-nums; font-feature-settings:"tnum"}
.hl{color:var(--red)}
.hl-n{color:var(--navy)}

/* ---------- eyebrow / chips ---------- */
.eyebrow{
  display:inline-flex; align-items:center; gap:9px; padding:6px 15px 6px 11px;
  border:1px solid var(--line2); border-radius:100px; background:#fff;
  font-size:.73rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase;
  color:var(--navy); margin-bottom:26px; box-shadow:var(--sh);
}
.eyebrow .dot{width:6px;height:6px;border-radius:50%;background:var(--red);box-shadow:0 0 0 4px rgba(212,52,38,.14)}
.tag{display:inline-block;padding:5px 12px;border-radius:100px;font-size:.69rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase}
.tag-acc{background:rgba(212,52,38,.08); color:var(--red); border:1px solid rgba(212,52,38,.22)}
.tag-blue{background:rgba(16,26,53,.06); color:var(--navy); border:1px solid rgba(16,26,53,.18)}
.tag-gold{background:rgba(117,140,156,.12); color:#4C5F6D; border:1px solid rgba(117,140,156,.3)}

/* ---------- buttons ---------- */
.btn{
  display:inline-flex; align-items:center; justify-content:center; gap:10px;
  padding:15px 26px; border-radius:9px; font-weight:650; font-size:.97rem;
  border:1px solid transparent; cursor:pointer; transition:.18s ease; text-decoration:none!important;
  font-family:'Inter',sans-serif; white-space:nowrap;
}
.btn-primary{background:var(--red); color:#fff!important; box-shadow:0 6px 18px -6px rgba(212,52,38,.5)}
.btn-primary:hover{background:var(--red-d); transform:translateY(-2px); box-shadow:0 12px 26px -8px rgba(212,52,38,.55)}
.btn-ghost{background:#fff; color:var(--navy)!important; border-color:var(--line2); box-shadow:var(--sh)}
.btn-ghost:hover{border-color:var(--navy); transform:translateY(-2px)}
.btn-navy{background:var(--navy); color:#fff!important}
.btn-navy:hover{background:var(--navy-l); transform:translateY(-2px)}
.btn-white{background:#fff; color:var(--navy)!important}
.btn-white:hover{background:var(--lgray); transform:translateY(-2px)}
.btn-outline-w{background:transparent; color:#fff!important; border-color:rgba(255,255,255,.42)}
.btn-outline-w:hover{background:rgba(255,255,255,.12); border-color:#fff; transform:translateY(-2px)}
.btn-sm{padding:11px 18px; font-size:.88rem}
.btn-lg{padding:18px 32px; font-size:1.04rem}
.btn-row{display:flex; gap:14px; flex-wrap:wrap}
.center .btn-row{justify-content:center}
@media(max-width:520px){
  .btn{white-space:normal; text-align:center; max-width:100%}
  .btn-lg{padding:16px 20px; font-size:.99rem}
  .btn-row>.btn{flex:1 1 100%}
  .contact-line a{font-size:1.02rem}
}

/* ---------- nav ---------- */
.nav{position:sticky; top:0; z-index:80; background:rgba(255,255,255,.9);
  backdrop-filter:blur(16px) saturate(160%); border-bottom:1px solid var(--line)}
.nav-in{max-width:var(--max); margin:0 auto; padding:0 24px; height:72px; display:flex; align-items:center; gap:26px}
.logo{display:flex; align-items:center; text-decoration:none!important; flex:none}
.logo img{height:34px; width:auto; display:block}
@media(max-width:420px){.logo img{height:29px}}
footer .logo img{height:36px}
.nav-links{display:flex; gap:2px; margin-left:auto; align-items:center}
.nav-links a{padding:9px 13px; border-radius:7px; color:var(--muted)!important; font-size:.92rem;
  font-weight:550; text-decoration:none!important; transition:.15s}
.nav-links a:hover{color:var(--navy)!important; background:var(--off)}
.nav-links a.on{color:var(--navy)!important; background:var(--lgray)}
.nav-cta{display:flex; gap:10px; align-items:center}
.burger{display:none; margin-left:auto; background:#fff;border:1px solid var(--line2);border-radius:8px;padding:9px 11px;cursor:pointer}
.burger span{display:block;width:18px;height:2px;background:var(--navy);margin:3px 0;border-radius:2px}
@media(max-width:940px){
  .nav-in{flex-wrap:wrap; height:auto; min-height:72px; gap:0}
  .logo{min-height:72px}
  .nav-links,.nav-cta{display:none}
  .burger{display:block; margin-left:auto; align-self:center}
  .nav.open .nav-links{display:flex; flex:1 0 100%; flex-direction:column; align-items:stretch;
    gap:2px; margin:0; padding:8px 0 12px; border-top:1px solid var(--line)}
  .nav.open .nav-links a{padding:13px 12px; font-size:1rem}
  .nav.open .nav-cta{display:flex; flex:1 0 100%; flex-direction:column; gap:10px; padding:0 0 20px}
  .nav.open .nav-cta .btn{width:100%}
}

/* ---------- hero ---------- */
.hero{position:relative; padding:112px 0 92px; overflow:hidden; background:var(--off);
  border-bottom:1px solid var(--line)}
.hero:before{
  content:''; position:absolute; inset:-40% -15% auto -15%; height:900px; pointer-events:none;
  background:
    radial-gradient(40% 46% at 18% 34%, rgba(212,52,38,.10), transparent 68%),
    radial-gradient(44% 50% at 82% 24%, rgba(16,26,53,.10), transparent 66%);
}
.hero:after{
  content:''; position:absolute; inset:0; pointer-events:none; opacity:.65;
  background-image:linear-gradient(rgba(16,26,53,.055) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(16,26,53,.055) 1px,transparent 1px);
  background-size:58px 58px;
  mask-image:radial-gradient(76% 62% at 50% 32%,#000,transparent 78%);
  -webkit-mask-image:radial-gradient(76% 62% at 50% 32%,#000,transparent 78%);
}
.hero .wrap{position:relative; z-index:2}
.hero-grid{display:grid; grid-template-columns:1.05fr .95fr; gap:56px; align-items:center}
@media(max-width:980px){.hero-grid{grid-template-columns:1fr; gap:44px} .hero{padding:72px 0 64px}}
.hero h1 span.br{display:block}
.hero-sub{font-size:1.18rem; max-width:56ch; color:var(--muted); margin-bottom:30px}
.trust{display:flex; flex-wrap:wrap; gap:10px 26px; margin-top:32px; padding-top:24px; border-top:1px solid var(--line2)}
.trust div{display:flex; align-items:center; gap:8px; font-size:.87rem; color:var(--muted); font-weight:550}
.trust svg{flex:none}

/* ---------- panel / cards ---------- */
.panel{background:#fff; border:1px solid var(--line); border-radius:16px; padding:28px; box-shadow:var(--sh-l)}
.panel-navy{background:var(--navy); border-color:var(--navy); color:#fff}
.panel-navy h2,.panel-navy h3{color:#fff}
.card{background:#fff; border:1px solid var(--line); border-radius:var(--r); padding:26px;
  transition:.2s ease; position:relative; overflow:hidden; box-shadow:var(--sh)}
.card:hover{border-color:var(--line2); transform:translateY(-3px); box-shadow:var(--sh-l)}
.card:before{content:''; position:absolute; left:0; top:0; bottom:0; width:3px; background:var(--red);
  opacity:0; transition:.2s}
.card:hover:before{opacity:1}
.card h3{margin-bottom:.45em}
.card p:last-child{margin-bottom:0}
.card-ico{width:46px;height:46px;border-radius:10px;display:grid;place-items:center;margin-bottom:18px;
  background:rgba(212,52,38,.07);border:1px solid rgba(212,52,38,.16)}
.card-ico.b{background:rgba(16,26,53,.05);border-color:rgba(16,26,53,.14)}
.card-ico.g{background:rgba(117,140,156,.11);border-color:rgba(117,140,156,.26)}
.grid{display:grid; gap:20px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:900px){.g3,.g4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:620px){.g2,.g3,.g4{grid-template-columns:1fr}}

/* ---------- stat band ---------- */
.stats{background:var(--navy-bg); color:#fff}
.stats-in{display:grid; grid-template-columns:repeat(4,1fr)}
.stat{padding:36px 26px; border-right:1px solid rgba(255,255,255,.13); position:relative}
.stat:last-child{border-right:none}
.stat b{display:block; font-family:'Sora',sans-serif; font-size:clamp(1.7rem,3vw,2.4rem);
  font-weight:750; letter-spacing:-.035em; color:#fff; line-height:1}
.stat span{display:block; margin-top:10px; font-size:.83rem; color:rgba(255,255,255,.66); letter-spacing:.02em}
.stat:after{content:''; position:absolute; left:26px; top:26px; width:22px; height:3px; background:var(--red); border-radius:2px}
@media(max-width:820px){.stats-in{grid-template-columns:repeat(2,1fr)}
  .stat:nth-child(2){border-right:none} .stat:nth-child(-n+2){border-bottom:1px solid rgba(255,255,255,.13)}}

/* ---------- section head ---------- */
.shead{max-width:70ch; margin-bottom:50px}
.shead.center{margin-left:auto;margin-right:auto}
.shead h2{margin-bottom:.35em}
.shead p{font-size:1.09rem; margin-bottom:0; color:var(--muted)}

/* ---------- table ---------- */
.tbl-wrap{overflow-x:auto; border:1px solid var(--line); border-radius:var(--r); background:#fff; box-shadow:var(--sh)}
table{width:100%; border-collapse:collapse; min-width:560px; font-size:.94rem}
th,td{padding:15px 20px; text-align:left; border-bottom:1px solid var(--line)}
th{font-size:.7rem; letter-spacing:.11em; text-transform:uppercase; color:#fff; font-weight:700; background:var(--navy-bg)}
td{color:var(--muted)}
td:first-child{color:var(--navy); font-weight:600}
tr:last-child td{border-bottom:none}
tbody tr:nth-child(even) td{background:#FBFBFD}
tbody tr:hover td{background:rgba(212,52,38,.035)}

/* ---------- steps ---------- */
.steps{display:grid; grid-template-columns:repeat(4,1fr); gap:0; position:relative}
.steps:before{content:''; position:absolute; top:23px; left:9%; right:9%; height:2px;
  background:linear-gradient(90deg,transparent,var(--line2),var(--line2),transparent)}
.step{padding:0 18px; position:relative}
.step .n{width:48px;height:48px;border-radius:50%;display:grid;place-items:center;background:#fff;
  border:2px solid var(--navy); font-family:'Sora',sans-serif;font-weight:700;color:var(--navy);
  margin-bottom:20px;position:relative;z-index:2;font-size:.95rem}
.step h3{font-size:1.05rem;margin-bottom:.4em}
.step p{font-size:.93rem;margin:0}
@media(max-width:900px){.steps{grid-template-columns:1fr;gap:30px}.steps:before{display:none}.step{padding:0}}

/* ---------- calculator ---------- */
.field{margin-bottom:19px}
.field label{display:block; font-size:.77rem; font-weight:700; letter-spacing:.08em;
  text-transform:uppercase; color:var(--dim); margin-bottom:8px}
.field .hint{font-size:.78rem;color:var(--dim);margin-top:6px;text-transform:none;letter-spacing:0;font-weight:400}
input[type=text],input[type=number],input[type=email],input[type=tel],select,textarea{
  width:100%; padding:13px 15px; border-radius:8px; border:1px solid var(--line2);
  background:#fff; color:var(--navy); font-size:1rem; font-family:'Inter',sans-serif;
  font-weight:550; transition:.15s; font-variant-numeric:tabular-nums;
}
input:focus,select:focus,textarea:focus{outline:none; border-color:var(--red);
  box-shadow:0 0 0 3px rgba(212,52,38,.12)}
select{appearance:none; background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'><path d='M1 1l5 5 5-5' stroke='%23001F60' stroke-width='1.7' fill='none' stroke-linecap='round'/></svg>");
  background-repeat:no-repeat; background-position:right 15px center; padding-right:40px}
.readout{text-align:center; padding:16px 0 20px}
.readout .lbl{font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--dim);font-weight:700}
.readout .val{font-family:'Sora',sans-serif; font-size:3.9rem; font-weight:800; letter-spacing:-.045em;
  line-height:1.05; margin:6px 0 4px; color:var(--navy)}
.readout .verdict{font-size:.95rem; font-weight:600}
.ok{color:var(--ok)} .warn{color:var(--warn)} .bad{color:var(--bad)}
.rows{border-top:1px solid var(--line); padding-top:14px}
.row{display:flex; justify-content:space-between; align-items:baseline; padding:9px 0; font-size:.93rem;
  border-bottom:1px dashed var(--line)}
.row:last-child{border-bottom:none}
.row span{color:var(--muted)}
.row b{font-weight:650; font-variant-numeric:tabular-nums; color:var(--navy)}
.assump{font-size:.76rem; color:var(--dim); line-height:1.55; margin-top:16px; padding-top:14px; border-top:1px solid var(--line)}

/* ---------- accordion ---------- */
.acc{border:1px solid var(--line); border-radius:var(--r); overflow:hidden; background:#fff; box-shadow:var(--sh)}
.acc details{border-bottom:1px solid var(--line)}
.acc details:last-child{border-bottom:none}
.acc summary{padding:20px 24px; cursor:pointer; font-weight:600; font-size:1.01rem; list-style:none;
  display:flex; justify-content:space-between; align-items:center; gap:20px; transition:.15s;
  font-family:'Sora',sans-serif; letter-spacing:-.015em; color:var(--navy)}
.acc summary::-webkit-details-marker{display:none}
.acc summary:hover{background:var(--off)}
.acc summary:after{content:'+'; font-size:1.45rem; color:var(--red); font-weight:400; flex:none; line-height:1; transition:.2s}
.acc details[open] summary:after{transform:rotate(45deg)}
.acc details[open] summary{color:var(--red)}
.acc .body{padding:0 24px 22px; color:var(--muted); font-size:.96rem; max-width:78ch}
.acc .body p:last-child{margin-bottom:0}

/* ---------- cta band ---------- */
.cta-band{position:relative; overflow:hidden; background:var(--navy-bg); color:#fff}
.cta-band h2{color:#fff}
.cta-band .lead{color:rgba(255,255,255,.78)}
.cta-band:before{content:'';position:absolute;inset:0;
  background:radial-gradient(50% 70% at 50% 0%, rgba(212,52,38,.30), transparent 70%)}
.cta-band:after{content:'';position:absolute;inset:0;opacity:.5;
  background-image:linear-gradient(rgba(255,255,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.06) 1px,transparent 1px);
  background-size:54px 54px;
  mask-image:radial-gradient(70% 90% at 50% 50%,#000,transparent);-webkit-mask-image:radial-gradient(70% 90% at 50% 50%,#000,transparent)}
.cta-band .wrap{position:relative;z-index:2}
.contact-line{display:flex;gap:14px 34px;flex-wrap:wrap;justify-content:center;margin-top:28px}
.contact-line a{display:flex;align-items:center;gap:10px;font-family:'Sora',sans-serif;font-weight:650;
  font-size:1.15rem;color:#fff!important;text-decoration:none!important}
.contact-line a:hover{color:#FFD9E0!important}

/* ---------- footer ---------- */
footer{padding:62px 0 38px; background:var(--navy-bg); color:rgba(255,255,255,.72); font-size:.9rem}
.f-grid{display:grid; grid-template-columns:1.6fr 1fr 1fr 1fr; gap:40px; margin-bottom:42px}
@media(max-width:820px){.f-grid{grid-template-columns:1fr 1fr; gap:32px}}
footer h4{font-size:.72rem; letter-spacing:.13em; text-transform:uppercase; color:rgba(255,255,255,.5);
  margin-bottom:16px; font-weight:700}
footer ul{list-style:none; padding:0; margin:0}
footer li{margin:9px 0}
footer li a{color:rgba(255,255,255,.72)!important; text-decoration:none!important}
footer li a:hover{color:#fff!important}
footer p{color:rgba(255,255,255,.62)}
.legal{border-top:1px solid rgba(255,255,255,.15); padding-top:24px; color:rgba(255,255,255,.5); font-size:.78rem; line-height:1.7}
.legal p{color:rgba(255,255,255,.5); font-size:.78rem}
.legal a{color:rgba(255,255,255,.7)!important}
.ehl{display:inline-flex;align-items:center;gap:9px;margin-bottom:14px;color:#fff;font-weight:600;font-size:.8rem}

/* ---------- wizard ---------- */
.wiz-bar{height:4px;background:var(--lgray);border-radius:100px;overflow:hidden;margin-bottom:12px}
.wiz-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,var(--navy),var(--red));transition:width .35s cubic-bezier(.4,0,.2,1)}
.wiz-meta{display:flex;justify-content:space-between;font-size:.8rem;color:var(--dim);margin-bottom:24px;letter-spacing:.03em}
.stepq{display:none;animation:fade .35s ease}
.stepq.on{display:block}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.stepq h2{font-size:clamp(1.45rem,3vw,2rem);margin-bottom:.3em}
.stepq .qsub{color:var(--muted);margin-bottom:24px;font-size:1rem}
.opts{display:grid;gap:10px;margin-bottom:8px}
.opts.two{grid-template-columns:1fr 1fr}
@media(max-width:620px){.opts.two{grid-template-columns:1fr}}
.opt{display:flex;align-items:center;gap:14px;padding:16px 18px;border:1px solid var(--line2);border-radius:10px;
  background:#fff;cursor:pointer;transition:.15s;font-weight:550;text-align:left;color:var(--navy);
  font-family:'Inter',sans-serif;font-size:.97rem;width:100%}
.opt:hover{border-color:var(--red);background:rgba(212,52,38,.035);transform:translateX(3px)}
.opt.sel{border-color:var(--red);background:rgba(212,52,38,.06);box-shadow:0 0 0 3px rgba(212,52,38,.1)}
.opt .oi{width:30px;height:30px;border-radius:7px;background:var(--off);display:grid;place-items:center;
  flex:none;font-size:.82rem;color:var(--red);font-weight:700;border:1px solid var(--line)}
.opt small{display:block;color:var(--dim);font-weight:400;font-size:.83rem;margin-top:2px}
.wiz-nav{display:flex;justify-content:space-between;gap:12px;margin-top:26px;padding-top:20px;border-top:1px solid var(--line)}
.result-hero{text-align:center;padding:10px 0 24px;border-bottom:1px solid var(--line);margin-bottom:24px}
.pill-big{display:inline-block;padding:8px 20px;border-radius:100px;font-weight:700;font-size:.85rem;
  letter-spacing:.06em;text-transform:uppercase;margin-bottom:16px}

/* ---------- reveal ---------- */
.rv{opacity:0; transform:translateY(20px); transition:opacity .7s cubic-bezier(.22,1,.36,1), transform .7s cubic-bezier(.22,1,.36,1)}
.rv.in{opacity:1; transform:none}
@media(prefers-reduced-motion:reduce){.rv{opacity:1;transform:none;transition:none} html{scroll-behavior:auto}
  .bar-fill,.ring-arc{transition:none!important}}

/* ---------- graphics ---------- */
.fig{width:100%; height:auto; display:block}
.fig-cap{font-size:.79rem;color:var(--dim);margin-top:12px;text-align:center}
.bar-fill{transition:width 1.1s cubic-bezier(.22,1,.36,1)}
.gfx-card{background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;box-shadow:var(--sh-l)}

/* ---------- misc ---------- */
.note{border-left:3px solid var(--red); padding:6px 0 6px 18px; color:var(--muted); font-size:.94rem; margin:24px 0}
.disc{font-size:.78rem; color:var(--dim); line-height:1.6; margin-top:20px}
.kv{display:flex;gap:10px;align-items:flex-start;margin:10px 0;color:var(--muted);font-size:.95rem}
.kv .ck{color:var(--red);flex:none;margin-top:3px}
.split{display:grid;grid-template-columns:1fr 1fr;gap:54px;align-items:center}
@media(max-width:900px){.split{grid-template-columns:1fr;gap:36px}}
.quote{font-family:'Sora',sans-serif;font-size:1.26rem;line-height:1.5;letter-spacing:-.02em;color:var(--navy);font-weight:500}
.who{margin-top:16px;font-size:.86rem;color:var(--dim)}
.hr{height:1px;background:var(--line);margin:0}
"""

CHECK = '<svg class="ck" width="15" height="15" viewBox="0 0 16 16" fill="none"><path d="M13.5 4.5L6.2 11.8 2.5 8.1" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PHONE_ICO = '<svg width="17" height="17" viewBox="0 0 20 20" fill="none"><path d="M18 14.1v2.5a1.7 1.7 0 01-1.8 1.7 16.6 16.6 0 01-7.2-2.6 16.3 16.3 0 01-5-5A16.6 16.6 0 011.4 3.5 1.7 1.7 0 013.1 1.7h2.5a1.7 1.7 0 011.7 1.5c.1.8.3 1.6.6 2.4a1.7 1.7 0 01-.4 1.8L6.4 8.5a13.3 13.3 0 005 5l1.1-1.1a1.7 1.7 0 011.8-.4c.8.3 1.6.5 2.4.6a1.7 1.7 0 011.4 1.5z" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
MAIL_ICO  = '<svg width="17" height="17" viewBox="0 0 20 20" fill="none"><rect x="1.7" y="3.7" width="16.7" height="12.5" rx="2" stroke="currentColor" stroke-width="1.6"/><path d="M2.2 5l7.8 5.4L17.8 5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'
EHL_ICO   = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M3 10.5L12 4l9 6.5" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path d="M5.5 12v7.5h13V12" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/><path d="M9.5 19.5v-4h5v4" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def nav(active):
    links = "".join(
        f'<a href="{h}" class="{"on" if h==active else ""}">{t}</a>' for h, t in NAV
    )
    return f"""<nav class="nav" id="nav">
  <div class="nav-in">
    <a class="logo" href="index.html"><img src="{LOGO_DATA}" alt="{BRAND}"></a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
    <div class="nav-links">{links}</div>
    <div class="nav-cta">
      <a class="btn btn-ghost btn-sm" href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
      <a class="btn btn-primary btn-sm" href="qualify.html">Check my numbers</a>
    </div>
  </div>
</nav>"""


CTA_BAND = f"""<section class="cta-band sec-tight">
  <div class="wrap center">
    <h2 style="max-width:20ch;margin:0 auto .4em">Tell us the address and the rent. We'll tell you the number.</h2>
    <p class="lead" style="margin-bottom:0">No application fee, no credit pull, no obligation. A real conversation with a
    licensed loan officer. Usually five minutes is all it takes to know whether the deal pencils.</p>
    <div class="contact-line">
      <a href="tel:{PHONE_TEL}">{PHONE_ICO}{PHONE_DISPLAY}</a>
      <a href="mailto:{EMAIL}">{MAIL_ICO}{EMAIL}</a>
    </div>
    <div class="btn-row" style="margin-top:28px">
      <a class="btn btn-primary btn-lg" href="qualify.html">Run my scenario &rarr;</a>
      <a class="btn btn-outline-w btn-lg" href="programs.html">See loan programs</a>
    </div>
  </div>
</section>"""


def footer():
    ln = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""<footer>
  <div class="wrap">
    <div class="f-grid">
      <div>
        <a class="logo" href="index.html" style="margin-bottom:18px"><img src="{LOGO_WHITE_DATA}" alt="{BRAND}"></a>
        <p style="max-width:34ch;font-size:.9rem">{TAGLINE}. Rental-income qualified financing for
        1-4 unit residential investment property.</p>
        <div class="ehl">{EHL_ICO} Equal Housing Lender</div>
      </div>
      <div><h4>Site</h4><ul>{ln}</ul></div>
      <div><h4>Programs</h4><ul>
        <li><a href="programs.html#purchase">Purchase</a></li>
        <li><a href="programs.html#rateterm">Rate and term refinance</a></li>
        <li><a href="programs.html#cashout">Cash-out refinance</a></li>
        <li><a href="programs.html#str">Short-term rental</a></li>
        <li><a href="programs.html#portfolio">Portfolio / blanket</a></li>
        <li><a href="programs.html#foreign">Foreign national</a></li>
      </ul></div>
      <div><h4>Talk to us</h4><ul>
        <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li style="color:rgba(255,255,255,.5)">Mon-Fri, 8a-7p ET</li>
      </ul></div>
    </div>
    <div class="legal">
      <p>{COMPLIANCE} {CO_NAME} is licensed to originate residential mortgage loans in the states where it holds
      the required authority; not all products are available in all states. Loan approval is subject to underwriting
      review of the property, the borrower, and supporting documentation.</p>
      <p>{RATE_DISCLAIMER}</p>
      <p>Calculators and eligibility indicators on this site are educational estimates. They do not price a loan,
      do not constitute underwriting, and do not guarantee eligibility or terms. Nothing on this site is legal,
      tax, accounting, or investment advice. Consult your own professionals before acquiring or financing
      investment property.</p>
      <p style="margin-top:18px">&copy; 2026 {BRAND}. All rights reserved. |
      NMLS Consumer Access: <a href="https://www.nmlsconsumeraccess.org">nmlsconsumeraccess.org</a></p>
    </div>
  </div>
</footer>"""


JS_BASE = """
(function(){
  var b=document.getElementById('burger'), n=document.getElementById('nav');
  if(b) b.addEventListener('click',function(){n.classList.toggle('open')});
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){
      e.target.classList.add('in');
      e.target.querySelectorAll('[data-w]').forEach(function(el){el.style.width=el.getAttribute('data-w')});
      io.unobserve(e.target)}})},{threshold:.08,rootMargin:'0px 0px -40px'});
  document.querySelectorAll('.rv').forEach(function(el,i){el.style.transitionDelay=(Math.min(i%4,3)*70)+'ms';io.observe(el)});
})();
"""


def page(title, desc, active, body, extra_js="", extra_css=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#16224A">
<link rel="icon" type="image/png" href="{FAVICON_DATA}">
<meta name="robots" content="index,follow">
{FONTS}
<style>{CSS}{extra_css}</style>
</head>
<body>
{nav(active)}
{body}
{footer()}
<script>{JS_BASE}{extra_js}</script>
</body>
</html>"""
