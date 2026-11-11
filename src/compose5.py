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
    base=Image.open(f"/root/work/xiaoyu-video/frames5/f{i:04d}.png").convert("RGBA")
    W,H=base.size
    s,dy = 0.26, 8
    cw,ch=int(card.width*s),int(card.height*s)
    c=card.resize((cw,ch),Image.LANCZOS)
    sh=shadow.resize((int(shadow.width*s),int(shadow.height*s)),Image.LANCZOS)
    e=min(1,max(0,t/0.8)); e=1-(1-e)**3
    x=W-cw-56-int(260*(1-e)); y=int(300+dy*math.sin(t*2.2))
    base.alpha_composite(sh,(int(x-30*s),int(y-40*s)))
    base.alpha_composite(c,(int(x),int(y)))
    base.convert("RGB").save(f"/root/work/xiaoyu-video/composed5/f{i:04d}.png")
print("ok")
