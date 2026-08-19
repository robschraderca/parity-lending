# Parity v8 creative toolchain (session 2026-08-18)

Run in a cloud sandbox with Python 3 + Pillow + ffmpeg. Everything renders from these four scripts.

## Bootstrap (copy-paste)
    mkdir -p /tmp/v8/fonts /tmp/v8/photos /tmp/v8/out && cd /tmp/v8
    curl -sL -o fonts/Montserrat-VF.ttf "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/Montserrat%5Bwght%5D.ttf"
    # photos: images.unsplash.com is reachable. p<N>.jpg = photo-<id>?w=1600&q=80&fm=jpg&fit=crop
    # p2 1570129477492-45c003edd2be   p4 1512917774080-9991f1c4c750   p6 1600585154340-be6161a56a0c
    # p7 1605276374104-dee2a0ed3cd6   p10 1576941089067-2de3c901e126  p11 1600047509807-ba8f99d2cdde
    # p12 1449844908441-8829872d2607  p14 1613977257363-707ba9348227  p15 1592595896551-12b371d546d5
    # p16 1625602812206-5ec545ca1231
    for kv in "2 1570129477492-45c003edd2be" "4 1512917774080-9991f1c4c750" "6 1600585154340-be6161a56a0c" "7 1605276374104-dee2a0ed3cd6" "10 1576941089067-2de3c901e126" "11 1600047509807-ba8f99d2cdde" "12 1449844908441-8829872d2607" "14 1613977257363-707ba9348227" "15 1592595896551-12b371d546d5" "16 1625602812206-5ec545ca1231"; do set -- $kv; curl -sL -o photos/p$1.jpg "https://images.unsplash.com/photo-$2?w=1600&q=80&fm=jpg&fit=crop"; done
    # then drop gen_v8.py reel.py carousel.py story.py into /tmp/v8 (fetch raw from this repo folder)
    python3 gen_v8.py            # 12 master PNGs -> /tmp/v8/out
    python3 carousel.py          # 6 carousel cards -> /tmp/v8/out
    python3 story.py             # 5 story frames + sheet
    python3 reel.py              # 12s Reel mp4 (concept 1b) + storyboard

## Files
- gen_v8.py    master template (1080x1350, 2x supersample). MSGS dict = the six messages. PHOTOS/FOCAL maps.
- carousel.py  imports gen_v8; card1 (hook), crit_card (cards 2-5), cta_card (card 6).
- story.py     imports reel; 5 frames 1080x1920 with safe zones; sticker placeholder zones.
- reel.py      concept 1b three-beat animatic; frames -> ffmpeg; wipes /tmp/v8/reel_frames each run.
- Parity/gen_fb_posts_v8.py on Rob's Mac is the env-var version of gen_v8.py (same output).

## Rules baked in (do not undo)
DSCR HOME INVESTOR LOANS at hero scale; no blue text (blue only in the mark); no rates; no timing claims;
no dba line; no Equal Housing; CTA "SEE IF YOU QUALIFY"; every URL = paritylending.com/dscr; fine print =
business-purpose line + "© 2026 Parity Lending · DSCR Lending Nationwide"; every text line auto-fits under
the red diagonal; the three DSCR lines share one size; flat state uses the full-colour chevron, no keyline.
