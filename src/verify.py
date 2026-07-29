import asyncio, os, re, glob
from playwright.async_api import async_playwright

B = "/root/dscr-site/build"
SHOTS = "/root/dscr-site/shots"
os.makedirs(SHOTS, exist_ok=True)
PAGES = ["index.html", "programs.html", "qualify.html", "faq.html", "contact.html"]


async def main():
    problems = []
    async with async_playwright() as p:
        br = await p.chromium.launch()

        # ---------- link integrity ----------
        have = set(PAGES)
        for f in PAGES:
            html = open(os.path.join(B, f), encoding="utf-8").read()
            for href in re.findall(r'href="([^"]+)"', html):
                if href.startswith(("http", "mailto:", "tel:", "#", "data:")):
                    continue
                target = href.split("#")[0]
                if target and target not in have:
                    problems.append(f"[{f}] broken link -> {href}")
            # anchor targets
            for href in re.findall(r'href="(\w[\w.]*\.html)#([\w-]+)"', html):
                tgt_html = open(os.path.join(B, href[0]), encoding="utf-8").read()
                if f'id="{href[1]}"' not in tgt_html:
                    problems.append(f"[{f}] missing anchor #{href[1]} in {href[0]}")
            for tag in ["NMLS 217229", "Equal Housing Lender", "not a commitment to lend"]:
                if tag not in html:
                    problems.append(f"[{f}] MISSING compliance text: {tag}")

        # ---------- render + console ----------
        for f in PAGES:
            for label, w, h in [("desktop", 1440, 1000), ("mobile", 390, 844)]:
                pg = await br.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
                errs = []
                pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
                pg.on("pageerror", lambda e: errs.append(str(e)))
                await pg.goto("file://" + os.path.join(B, f))
                await pg.wait_for_timeout(1200)
                await pg.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await pg.wait_for_timeout(900)
                await pg.evaluate("window.scrollTo(0,0)")
                await pg.wait_for_timeout(500)
                await pg.screenshot(path=f"{SHOTS}/{f.replace('.html','')}-{label}.png",
                                    full_page=(label == "desktop"), timeout=90000)
                # horizontal overflow check
                ow = await pg.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth+2")
                if ow:
                    problems.append(f"[{f}/{label}] horizontal overflow")
                for e in errs:
                    problems.append(f"[{f}/{label}] console: {e}")
                await pg.close()

        # ---------- home calculator math ----------
        pg = await br.new_page(viewport={"width": 1440, "height": 1000})
        await pg.goto("file://" + os.path.join(B, "index.html"))
        await pg.wait_for_timeout(600)
        vals = await pg.evaluate("""() => ({
            dscr: document.getElementById('h_dscr').textContent,
            loan: document.getElementById('h_loan').textContent,
            rate: document.getElementById('h_rate').textContent,
            pitia: document.getElementById('h_pitia').textContent,
            cf: document.getElementById('h_cf').textContent })""")
        print("HOME CALC (2400 rent / 320k / 25% down):", vals)
        if vals["dscr"] in ("—", "NaN", ""):
            problems.append("home calculator did not compute")
        # change rent, confirm reactive
        await pg.fill("#h_rent", "1500")
        await pg.wait_for_timeout(300)
        v2 = await pg.evaluate("document.getElementById('h_dscr').textContent")
        print("HOME CALC (1500 rent):", v2)
        if v2 == vals["dscr"]:
            problems.append("home calculator not reactive")
        await pg.close()

        # ---------- wizard end-to-end ----------
        pg = await br.new_page(viewport={"width": 1440, "height": 1100})
        werr = []
        pg.on("pageerror", lambda e: werr.append(str(e)))
        await pg.goto("file://" + os.path.join(B, "qualify.html"))
        await pg.wait_for_timeout(500)
        await pg.click('.stepq[data-s="1"] .opt:nth-child(1)')      # Purchase
        await pg.wait_for_timeout(500)
        await pg.click('.stepq[data-s="2"] .opt:nth-child(1)')      # SFR
        await pg.wait_for_timeout(500)
        await pg.fill("#w_price", "320000")
        await pg.fill("#w_rent", "2400")
        await pg.select_option("#w_down", "25")
        await pg.click("#btnNext")
        await pg.wait_for_timeout(500)
        await pg.click('.stepq[data-s="4"] .opt:nth-child(2)')      # 740-759
        await pg.wait_for_timeout(500)
        await pg.click('.stepq[data-s="5"] .opt:nth-child(2)')      # 30-60 days
        await pg.wait_for_timeout(500)
        await pg.click('.stepq[data-s="6"] .opt:nth-child(1)')      # LLC
        await pg.wait_for_timeout(900)
        res = await pg.evaluate("""() => ({
            visible: !!document.querySelector('.stepq[data-s="7"].on'),
            dscr: document.getElementById('rDscr').textContent,
            loan: document.getElementById('rLoan').textContent,
            ltv:  document.getElementById('rLtv').textContent,
            rate: document.getElementById('rRate').textContent,
            pitia:document.getElementById('rPitia').textContent,
            cf:   document.getElementById('rCf').textContent,
            down: document.getElementById('rDown').textContent,
            res:  document.getElementById('rRes').textContent,
            pill: document.getElementById('rPill').textContent,
            levers: document.querySelectorAll('#levers .lever').length,
            mail: document.getElementById('mailBtn').getAttribute('href').slice(0,90) })""")
        print("WIZARD RESULT:", res)
        if not res["visible"]:
            problems.append("wizard did not reach results")
        if res["dscr"] in ("—", "NaN", ""):
            problems.append("wizard DSCR not computed")
        if res["levers"] == 0:
            problems.append("wizard levers empty")
        if not res["mail"].startswith("mailto:"):
            problems.append("wizard mailto not built")
        for e in werr:
            problems.append(f"[wizard] pageerror: {e}")
        await pg.screenshot(path=f"{SHOTS}/qualify-results.png", full_page=True)

        # tight-ratio path
        await pg.click("#adjBox summary")
        await pg.fill("#r_price", "525000")
        await pg.fill("#r_rent", "3300")
        await pg.select_option("#r_down", "20")
        await pg.wait_for_timeout(400)
        tight = await pg.evaluate("""() => ({dscr:document.getElementById('rDscr').textContent,
            pill:document.getElementById('rPill').textContent,
            levers:document.querySelectorAll('#levers .lever').length})""")
        print("WIZARD TIGHT (525k/3300/20%):", tight)
        await pg.close()
        await br.close()

    print("\n" + "=" * 60)
    if problems:
        print(f"{len(problems)} ISSUE(S):")
        for x in problems:
            print("  •", x)
    else:
        print("ALL CHECKS PASSED")


asyncio.run(main())
