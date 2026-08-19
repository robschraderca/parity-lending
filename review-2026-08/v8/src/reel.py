#!/usr/bin/env python3
"""Reel concept 1 animatic: 'The Build'. 1080x1920, 24fps, ~15s. No voice.
Motion = photo slow pan, eyebrow fade, DSCR stack builds line by line, red message lines
type on, four spec ticks land, CTA end card holds. Same zones/type as the v8 master."""
import os, math, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageChops
W, H, FPS = 1080, 1920, 24
NAVY=(14,27,61); NAVY2=(22,39,82); BLUED=(59,111,212); RED=(217,59,43)
SLATE=(90,100,132); WHITE=(255,255,255); MIST=(242,243,246)
FONT="/tmp/v8/fonts/Montserrat-VF.ttf"
_fc={}
def F(w,s):
    k=(w,int(s))
    if k not in _fc:
        f=ImageFont.truetype(FONT,int(s)); f.set_variation_by_name(w); _fc[k]=f
    return _fc[k]
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3           # ease-out cubic
def seg(t,a,b): return ease((t-a)/(b-a)) if b>a else 1.0
def tracked(d,x,y,s,f,fill,tr=0,anchor="la"):
    if tr==0: d.text((x,y),s,font=f,fill=fill,anchor=anchor); return
    ws=[d.textlength(c,font=f) for c in s]; tot=sum(ws)+tr*(len(s)-1)
    x0 = x-tot/2 if anchor[0]=="m" else x
    for c,w in zip(s,ws): d.text((x0,y),c,font=f,fill=fill,anchor="l"+anchor[1]); x0+=w+tr
def chevron(d,cx,cy,sc):
    P=lambda pts:[(cx+x*sc,cy+y*sc) for x,y in pts]
    d.polygon(P([(0,0),(-31.5,31.5),(-20,43),(0,23)]),fill=BLUED)
    d.polygon(P([(0,0),(31.5,31.5),(20,43),(0,23)]),fill=RED)
def lockup(d,x,y,mh=44):
    sc=mh/43; chevron(d,x+31.5*sc,y,sc); tx=x+63*sc+16
    tracked(d,tx,y+mh/2,"PARITY",F("ExtraBold",mh*.62),NAVY,1.5,"lm")
    pw=sum(d.textlength(c,font=F("ExtraBold",mh*.62)) for c in "PARITY")+1.5*5
    tracked(d,tx+pw+8,y+mh/2,"LENDING",F("Regular",mh*.62),NAVY,1.5,"lm")
def icon(d,cx,cy,kind,alpha=1.0):
    R=30; d.ellipse([cx-R,cy-R,cx+R,cy+R],outline=RED,width=3); lw=3
    if kind=="house":
        d.polygon([(cx,cy-16),(cx+17,cy-1),(cx+17,cy+15),(cx-17,cy+15),(cx-17,cy-1)],outline=NAVY,width=lw)
        d.line([cx-22,cy+1,cx,cy-18,cx+22,cy+1],fill=NAVY,width=lw,joint="curve")
    elif kind=="gauge":
        d.arc([cx-18,cy-13,cx+18,cy+23],180,360,fill=NAVY,width=lw); d.line([cx,cy+5,cx+10,cy-6],fill=RED,width=lw)
    elif kind=="rent":
        d.rectangle([cx-16,cy-18,cx+7,cy+18],outline=NAVY,width=lw)
        for yy in (-10,-2,6): d.line([cx-10,cy+yy,cx+1,cy+yy],fill=NAVY,width=lw)
        d.ellipse([cx+7,cy+2,cx+23,cy+18],outline=RED,width=lw)
    elif kind=="nodoc":
        d.rectangle([cx-12,cy-18,cx+12,cy+18],outline=NAVY,width=lw)
        for yy in (-9,-2,5): d.line([cx-7,cy+yy,cx+7,cy+yy],fill=NAVY,width=lw)
        d.line([cx-20,cy+20,cx+20,cy-20],fill=RED,width=4)

PHOTO=Image.open("/tmp/v8/photos/p11.jpg").convert("RGB")
def photo_frame(t):
    """slow push-in + drift over the full duration"""
    zoom=1.08+0.10*t/15; bw,bh=W,H
    r=max(bw/PHOTO.width,bh/PHOTO.height)*zoom
    im=PHOTO.resize((int(PHOTO.width*r),int(PHOTO.height*r)),Image.BILINEAR)
    x0=int((im.width-bw)*(0.55-0.08*t/15)); y0=int((im.height-bh)*0.45)
    return im.crop((x0,y0,x0+bw,y0+bh))

MSG=dict(eyebrow="SHOPPING DSCR QUOTES?", h2=["You're a borrower.","Not a lead."],
         sub="One lender. No call lists. Your information is never resold.")
SPECS=[("house","20%+ down","or equity"),("gauge","620+ credit","score"),
       ("rent","Qualify on","rental income"),("nodoc","No tax returns","required")]

def avail(yy, top_x=700, bot_x=560):
    edge = top_x - (yy/H)*(top_x-bot_x); return edge - 40 - 64
def fit(d, txt, w, size, yy):
    f=F(w,size)
    while d.textlength(txt,font=f) > avail(yy) and size>20: size-=1; f=F(w,size)
    return f
def frame(t):
    img=photo_frame(t)
    # white angled panel slides in from left (0-0.8s), covers left ~62% at top, ~48% at bottom
    px=seg(t,0.0,0.8)
    ov=Image.new("RGBA",(W,H),(0,0,0,0)); od=ImageDraw.Draw(ov)
    top_x=int(700*px); bot_x=int(560*px)
    od.polygon([(0,0),(top_x,0),(bot_x,H),(0,H)],fill=(255,255,255,255))
    img=Image.alpha_composite(img.convert("RGBA"),ov)
    d=ImageDraw.Draw(img)
    if px>0.05: d.line([top_x,0,bot_x,H],fill=RED,width=10)
    # header lockup + pill (fade 0.6-1.2)
    a=seg(t,0.6,1.2)
    if a>0:
        lockup(d,64,120)
    # BEAT 1 (0.9-1.6s): eyebrow + product name + message arrive together, one move
    a=seg(t,0.9,1.6)
    if a>0:
        dx=int((1-a)*-36)
        tracked(d,64+dx,430,MSG["eyebrow"],F("Bold",22),RED,4)
        y=500
        lines=["DSCR HOME","INVESTOR","LOANS"]
        sz=min(fit(d,ln,"Black",100,y+i*112+100).size for i,ln in enumerate(lines))
        f=F("Black",sz)
        for i,ln in enumerate(lines):
            d.text((64+dx,y+i*int(sz*1.12)),ln,font=f,fill=NAVY)
        y=880
        for i,ln in enumerate(MSG["h2"]):
            f=fit(d,ln,"ExtraBold",52,y+i*66+52)
            d.text((64+dx,y+i*66),ln,font=f,fill=RED)
        d.text((64+dx,1030),"One lender. No call lists.",font=F("Medium",30),fill=SLATE)
        d.text((64+dx,1072),"Your information is never resold.",font=F("Medium",30),fill=SLATE)
    # BEAT 2 (3.0-3.9s): the four specs land as one group, tight stagger
    for i,(k,l1,l2) in enumerate(SPECS):
        s0=3.0+0.18*i; a=seg(t,s0,s0+0.35)
        if a>0:
            cy=1175+i*102; dy=int((1-a)*24)
            icon(d,64+40,cy+dy,k)
            d.text((64+100,cy-22+dy),l1,font=F("Bold",30),fill=NAVY)
            d.text((64+100,cy+12+dy),l2,font=F("Medium",24),fill=SLATE)
    # BEAT 3 (6.0s): CTA card rises, holds to end
    a=seg(t,6.0,6.6)
    if a>0:
        y0=1590+int((1-a)*400)
        d.rounded_rectangle([64,y0,W-64,y0+220],radius=30,fill=NAVY)
        d.text((104,y0+44),"See if you qualify in six quick questions.",font=F("SemiBold",30),fill=WHITE)
        d.text((104,y0+90),"No credit pull.",font=F("Medium",26),fill=(196,204,226))
        d.text((104,y0+140),"paritylending.com/dscr",font=F("Bold",34),fill=WHITE)
        lab="SEE IF YOU QUALIFY"; f=F("Bold",22)
        bw=sum(d.textlength(c,font=f) for c in lab)+2*len(lab)+64
        d.rounded_rectangle([W-64-40-bw,y0+150,W-64-40,y0+150+60],radius=30,fill=RED)
        tracked(d,W-64-40-bw/2,y0+180,lab,f,WHITE,2,"mm")
    # fine print always
    d.text((W/2,H-70),"Business-purpose loans for non-owner-occupied investment property only.",font=F("Regular",18),fill=SLATE,anchor="ma")
    return img.convert("RGB")

if __name__=="__main__":
    out="/tmp/v8/reel_frames"; import shutil; shutil.rmtree(out, ignore_errors=True); os.makedirs(out,exist_ok=True)
    DUR=12.0; n=int(DUR*FPS)
    for i in range(n):
        frame(i/FPS).save(f"{out}/f{i:04d}.jpg",quality=90)
    subprocess.run(["ffmpeg","-y","-loglevel","error","-r",str(FPS),"-i",f"{out}/f%04d.jpg",
                    "-c:v","libx264","-pix_fmt","yuv420p","-crf","22","/tmp/v8/parity-reel-concept1b-threebeat.mp4"],check=True)
    # storyboard sheet
    keys=[0.3,1.0,1.8,3.2,4.0,6.3,8.0,11.5]
    ims=[Image.open(f"{out}/f{int(k*FPS):04d}.jpg").resize((270,480)) for k in keys]
    sheet=Image.new("RGB",(len(ims)*280+10,540),"white"); dd=ImageDraw.Draw(sheet)
    for j,(im,k) in enumerate(zip(ims,keys)):
        sheet.paste(im,(10+j*280,40)); dd.text((10+j*280,12),f"t={k}s",fill=(14,27,61),font=F("Bold",18))
    sheet.save("/tmp/v8/parity-reel-concept1-storyboard.jpg",quality=85)
    print("done",n,"frames")
