import sys; sys.path.insert(0,'/tmp/v8')
from reel import *          # W,H=1080x1920, F, tracked, lockup, icon, chevron, colours
from PIL import Image, ImageDraw
SAFE_T, SAFE_B = 250, 340   # IG story safe zones
def base_photo(path, focal_x=0.5):
    im=Image.open(path).convert("RGB"); r=max(W/im.width,H/im.height)*1.02
    im=im.resize((int(im.width*r),int(im.height*r)),Image.LANCZOS)
    x0=int((im.width-W)*focal_x); y0=int((im.height-H)*0.45); return im.crop((x0,y0,x0+W,y0+H))
def panel(img, top_x=700, bot_x=560):
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    od.polygon([(0,0),(top_x,0),(bot_x,H),(0,H)],fill=(255,255,255,255))
    img=Image.alpha_composite(img.convert("RGBA"),ov); d=ImageDraw.Draw(img)
    d.line([top_x,0,bot_x,H],fill=RED,width=10); return img.convert("RGB")
def flat():
    img=Image.new("RGB",(W,H),NAVY); d=ImageDraw.Draw(img)
    chevron(d, W-250, 1420, 5.2); return img
def header(d, dark=False):
    if dark:
        sc=44/43; chevron(d,64+31.5*sc,SAFE_T-30,sc)
        tracked(d,64+63*sc+16,SAFE_T-30+22,"PARITY",F("ExtraBold",27),WHITE,1.5,"lm")
        pw=sum(d.textlength(c,font=F("ExtraBold",27)) for c in "PARITY")+7
        tracked(d,64+63*sc+16+pw+8,SAFE_T-30+22,"LENDING",F("Regular",27),WHITE,1.5,"lm")
    else:
        lockup(d,64,SAFE_T-30)
def foot(d, dark=False, n=1, total=5):
    c=(196,204,226) if dark else SLATE
    d.text((64,H-SAFE_B+60),"Business-purpose loans for",font=F("Regular",18),fill=c)
    d.text((64,H-SAFE_B+84),"non-owner-occupied investment property only.",font=F("Regular",18),fill=c)
    for i in range(total):
        cx=64+6+i*22
        d.ellipse([cx-5,H-SAFE_B+134-5,cx+5,H-SAFE_B+134+5],fill=(WHITE if dark else NAVY) if i==n-1 else ((60,80,130) if dark else (200,206,220)))
def sticker_zone(d, box, label, dark):
    x0,y0,x1,y1=box
    d.rounded_rectangle([x0,y0,x1,y1],radius=28,outline=(RED),width=4)
    # dashed feel: overlay short gaps
    for xx in range(x0+30,x1-30,44): d.line([xx,y0,xx+22,y0],fill=(WHITE if not dark else NAVY),width=4); d.line([xx,y1,xx+22,y1],fill=(WHITE if not dark else NAVY),width=4)
    for yy in range(y0+30,y1-30,44): d.line([x0,yy,x0,yy+22],fill=(WHITE if not dark else NAVY),width=4); d.line([x1,yy,x1,yy+22],fill=(WHITE if not dark else NAVY),width=4)
    d.text(((x0+x1)/2,(y0+y1)/2),label,font=F("Bold",22),fill=RED,anchor="mm")

def f1_hook():
    img=panel(base_photo("/tmp/v8/photos/p11.jpg",0.55)); d=ImageDraw.Draw(img); header(d)
    y=440
    for ln in ["SHOPPING","DSCR","QUOTES?"]:
        tracked(d,64,y,ln,F("Black",72),RED,2); y+=80
    y+=26
    for ln in ["You're a","borrower.","Not a lead."]:
        d.text((64,y),ln,font=F("Black",92),fill=NAVY if ln!="Not a lead." else RED); y+=104
    y+=30
    d.text((64,y),"One lender. No call lists.",font=F("Medium",32),fill=SLATE); y+=44
    d.text((64,y),"Your info is never resold.",font=F("Medium",32),fill=SLATE)
    d.text((64,H-SAFE_B-40),"Tap through  →",font=F("Bold",26),fill=NAVY)
    foot(d,n=1); return img
def f2_product():
    img=flat(); d=ImageDraw.Draw(img); header(d,dark=True)
    y=560; tracked(d,64,y,"SHOPPING DSCR QUOTES?",F("Bold",24),(255,120,105),4); y+=64
    for ln in ["DSCR HOME","INVESTOR","LOANS"]:
        d.text((64,y),ln,font=F("Black",118),fill=WHITE); y+=126
    y+=30
    d.text((64,y),"Qualified on the rent,",font=F("ExtraBold",44),fill=(255,120,105)); y+=54
    d.text((64,y),"not your paperwork.",font=F("ExtraBold",44),fill=(255,120,105)); y+=80
    d.text((64,y),"DSCR Lending Nationwide.",font=F("Medium",30),fill=(196,204,226))
    foot(d,dark=True,n=2); return img
def glyph(d,cx,cy,kind,k=1.9):
    lw=int(3*k)
    if kind=="house":
        d.polygon([(cx+x*k,cy+y*k) for x,y in [(0,-16),(17,-1),(17,15),(-17,15),(-17,-1)]],outline=NAVY,width=lw)
        d.line([cx-22*k,cy+1*k,cx,cy-18*k,cx+22*k,cy+1*k],fill=NAVY,width=lw,joint="curve")
    elif kind=="gauge":
        d.arc([cx-18*k,cy-13*k,cx+18*k,cy+23*k],180,360,fill=NAVY,width=lw); d.line([cx,cy+5*k,cx+10*k,cy-6*k],fill=RED,width=lw)
    elif kind=="rent":
        d.rectangle([cx-16*k,cy-18*k,cx+7*k,cy+18*k],outline=NAVY,width=lw)
        for yy in (-10,-2,6): d.line([cx-10*k,cy+yy*k,cx+1*k,cy+yy*k],fill=NAVY,width=lw)
        d.ellipse([cx+7*k,cy+2*k,cx+23*k,cy+18*k],outline=RED,width=lw)
    elif kind=="pct":
        d.text((cx,cy+2),"%",font=F("Bold",int(44*k)),fill=NAVY,anchor="mm")
def f3_spec():
    img=Image.new("RGB",(W,H),WHITE); d=ImageDraw.Draw(img); header(d)
    y=470
    for ln in ["DSCR HOME","INVESTOR LOANS"]:
        d.text((64,y),ln,font=F("Black",78),fill=NAVY); y+=86
    tracked(d,64,y+16,"THE FOUR THINGS WE LOOK AT",F("Bold",24),RED,4)
    specs=[("house","The property is a rental","SFR · condo · 2 to 4 units"),
           ("gauge","Your credit is 620 or better","We look at the score, not your income"),
           ("rent","The rent covers the payment","Rent in, PITIA out. That is the test"),
           ("pct","20% down or equity","No W-2s. No tax returns. No DTI")]
    y=780
    for i,(k,l1,l2) in enumerate(specs):
        cy=y+i*180
        R=54; d.ellipse([64+60-R,cy-R,64+60+R,cy+R],outline=RED,width=5)
        # bigger glyphs via reel icon at scale: draw small then it's fine (simple)
        glyph(d,64+60,cy,k)
        d.text((64+150,cy-34),l1,font=F("Bold",38),fill=NAVY)
        d.text((64+150,cy+16),l2,font=F("Medium",26),fill=SLATE)
    d.text((64,H-SAFE_B-40),"Tick all four?  →",font=F("Bold",26),fill=NAVY)
    foot(d,n=3); return img
def f4_poll():
    img=flat(); d=ImageDraw.Draw(img); header(d,dark=True)
    tracked(d,64,540,"QUICK ONE",F("Bold",24),(255,120,105),4)
    y=610
    for ln in ["Ever had a bank","say no to a","rental purchase?"]:
        d.text((64,y),ln,font=F("Black",78),fill=WHITE); y+=88
    sticker_zone(d,(120,1000,W-120,1180),"POLL STICKER: Yes / No  (added in the app)",True)
    d.text((64,1240),"Tap an answer. Next frame shows why the property, not you, gets qualified.",font=F("Medium",26),fill=(196,204,226))
    foot(d,dark=True,n=4); return img
def f5_cta():
    img=panel(base_photo("/tmp/v8/photos/p6.jpg",0.5),720,600); d=ImageDraw.Draw(img); header(d)
    y=520
    for ln in ["DSCR HOME","INVESTOR","LOANS"]:
        d.text((64,y),ln,font=F("Black",92),fill=NAVY); y+=100
    y+=20; tracked(d,64,y,"SEE IF YOU QUALIFY",F("Bold",24),RED,4); y+=50
    d.text((64,y),"Six quick questions.",font=F("ExtraBold",40),fill=RED); y+=50
    d.text((64,y),"No credit pull.",font=F("ExtraBold",40),fill=RED); y+=70
    d.text((64,y),"paritylending.com/dscr",font=F("Bold",34),fill=NAVY)
    # link sticker zone
    sticker_zone(d,(64,1290,600,1410),"LINK STICKER (added in app)",False)
    # CTA card
    y0=1440; d.rounded_rectangle([64,y0,W-64,y0+120],radius=30,fill=NAVY)
    d.text((104,y0+42),"A real person follows up. Your info stays put.",font=F("SemiBold",26),fill=WHITE)
    foot(d,n=5); return img

frames=[f1_hook(),f2_product(),f3_spec(),f4_poll(),f5_cta()]
for i,fr in enumerate(frames,1): fr.save(f"/tmp/v8/out/parity-v8-story-M4-f{i}.png",quality=95)
tw,th=324,576
s=Image.new("RGB",(tw*5+6*14,th+28),"#e9ebf0")
for i,fr in enumerate(frames): s.paste(fr.resize((tw,th),Image.LANCZOS),(14+i*(tw+14),14))
s.save("/tmp/v8/story-M4-set.jpg",quality=88); print("ok")
