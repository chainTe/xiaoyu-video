import math, os
from PIL import Image
FPS=30; N=300
whale=Image.open("/root/work/xiaoyu-video/assets/whale.png").convert("RGBA")
for i in range(N):
    t=i/FPS
    base=Image.open(f"/root/work/xiaoyu-video/frames/f{i:04d}.png").convert("RGBA")
    W,H=base.size
    if t<3.6:      # 镜头一：从下面弹出来
        k=min(1,max(0,(t-0.15)/0.9)); e=1-(1-k)**3
        s=0.62*e**0.5
        x=W/2-360*s; y=560+520*(1-e)+24*math.sin(t*2.2)
        a=255*min(1,k*1.4)
    elif t<7.2:    # 镜头二：右下角小头像
        s=0.34; x=W-330*s-40; y=H-360*s-40+10*math.sin(t*2.6); a=235
    else:          # 镜头三：居中大头像
        k=min(1,max(0,(t-7.2)/0.7)); e=1-(1-k)**3
        s=0.72*e; x=W/2-360*s; y=190-340*(1-e)+18*math.sin(t*2.0); a=255
    if s<=0.01: 
        base.convert("RGB").save(f"/root/work/xiaoyu-video/composed/f{i:04d}.png"); continue
    w=max(1,int(whale.width*s)); h=max(1,int(whale.height*s))
    im=whale.resize((w,h), Image.LANCZOS)
    if a<255:
        al=im.split()[3].point(lambda v: int(v*a/255)); im.putalpha(al)
    base.alpha_composite(im,(int(x),int(y)))
    base.convert("RGB").save(f"/root/work/xiaoyu-video/composed/f{i:04d}.png")
print("composed")
