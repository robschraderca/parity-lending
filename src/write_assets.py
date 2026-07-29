"""Regenerate the PNG logo assets from the data URIs in assets_data.py.
Run this after cloning so assets/ exists without committing binaries.
    python3 write_assets.py
"""
import base64, os
from assets_data import LOGO_DATA, LOGO_WHITE_DATA, MARK_DATA, FAVICON_DATA

os.makedirs("assets", exist_ok=True)
for name, uri in [("logo.png", LOGO_DATA), ("logo-white.png", LOGO_WHITE_DATA),
                  ("mark.png", MARK_DATA), ("favicon.png", FAVICON_DATA)]:
    open(os.path.join("assets", name), "wb").write(base64.b64decode(uri.split(",", 1)[1]))
    print("wrote assets/" + name)
