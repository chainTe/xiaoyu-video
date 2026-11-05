import math
from PIL import Image
FPS=30; N=450
me=Image.open("/root/work/xiaoyu-video/assets/me2.png").convert("RGBA")
for i in range(N):
    t=i/FPS
    base=Image.open(f"/root/work/xiaoyu-video/frames2/f{i:04d}.png").convert("RGBA")
    W,H=base.size
    if t<5:
        k=min(1,max(0,(t-0.2)/0.9)); e=1-(1-k)**3
        s=0.66*e**0.5; x=W/2-510*s; y=560+380*(1-e)+22*math.sin(t*2.0); a=255
    elif t<10:
        s=0.30; x=W-int(me.width*s)-40; y=H-int(me.height*s)-40+10*math.sin(t*2.6); a=240
    else:
        k=min(1,max(0,(t-10)/0.7)); e=1-(1-k)**3
        s=0.70*e; x=W/2-510*s; y=210-320*(1-e)+16*math.sin(t*2.0); a=255
    if s>0.01:
        w=max(1,int(me.width*s)); h=max(1,int(me.height*s))
        im=me.resize((w,h), Image.LANCZOS)
        if a<255:
            im.putalpha(im.split()[3].point(lambda v:int(v*a/255)))
        base.alpha_composite(im,(int(x),int(y)))
    base.convert("RGB").save(f"/root/work/xiaoyu-video/composed2/f{i:04d}.png")
print("ok")
