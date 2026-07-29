import os, importlib
import p_home, p_programs, p_qualify, p_faq, p_contact

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "build")
os.makedirs(OUT, exist_ok=True)

PAGES = {
    "index.html":    p_home.HTML,
    "programs.html": p_programs.HTML,
    "qualify.html":  p_qualify.HTML,
    "faq.html":      p_faq.HTML,
    "contact.html":  p_contact.HTML,
}

for name, html in PAGES.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{name:16s} {len(html)/1024:7.1f} KB")
print("\n-> " + OUT)
