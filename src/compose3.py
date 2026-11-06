import math
from PIL import Image, ImageDraw, ImageFilter
FPS=30; N=450
src=Image.open("/sdcard/Download/DSHA/xiaoyu-final.png").convert("RGBA")
w,h=src.size
src=src.crop((70,0,w-100,h-30)); w,h=src.size
r=int(min(w,h)*0.06)
mask=Image.new("L",(w,h),0); ImageDraw.Draw(mask).rounded_rectangle([0,0,w-1,h-1],r,fill=255)
card=src.copy(); card.putalpha(mask)
shadow=Image.new("RGBA",(w+60,h+60),(0,0,0,0))
ImageDraw.Draw(shadow).rounded_rectangle([30,40,w+30,h+40],r,fill=(0,0,0,110))
shadow=shadow.filter(ImageFilter.GaussianBlur(22))
for i in range(N):
    t=i/FPS
    base=Image.open(f"/root/work/xiaoyu-video/frames3/f{i:04d}.png").convert("RGBA")
    W,H=base.size
    if t<5:    s,dy = 0.52, 8
    elif t<10: s,dy = 0.30, 6
    else:      s,dy = 0.60, 10
    cw,ch=int(card.width*s),int(card.height*s)
    c=card.resize((cw,ch),Image.LANCZOS)
    sh=shadow.resize((int(shadow.width*s),int(shadow.height*s)),Image.LANCZOS)
    if t<5:
        e=min(1,max(0,(t-0.2)/0.9)); e=1-(1-e)**3
        x=W//2-cw//2; y=int(560+380*(1-e)+dy*math.sin(t*2.0))
    elif t<10:
        x=W-cw-60; y=H-ch-50+dy*math.sin(t*2.6)
    else:
        e=min(1,max(0,(t-10)/0.7)); e=1-(1-e)**3
        x=W//2-cw//2; y=int(170-240*(1-e)+dy*math.sin(t*2.0))
    base.alpha_composite(sh,(int(x-30*s),int(y-40*s)))
    base.alpha_composite(c,(int(x),int(y)))
    base.convert("RGB").save(f"/root/work/xiaoyu-video/composed3/f{i:04d}.png")
print("ok")
