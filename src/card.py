# 生成「今天三件事」竖版卡片：文字在左，角色在右下
# 用法：python3 src/card.py "标题" "第一件|看法1" "第二件|看法2" "第三件|看法3" out.png
import sys
from PIL import Image, ImageDraw, ImageFont

title, items, out = sys.argv[1], sys.argv[2:5], sys.argv[5]
W, H = 1080, 1440
im = Image.new("RGB", (W, H), (12, 18, 30))
d = ImageDraw.Draw(im)
for y in range(H):
    d.line([(0, y), (W, y)], fill=(12 + int(10*y/H), 18 + int(14*y/H), 30 + int(26*y/H)))
F = "/root/.fonts/NotoSansSC.otf"
f1, f2, f3 = (ImageFont.truetype(F, n) for n in (74, 44, 34))
d.text((80, 220), title, font=f1, fill=(255, 255, 255))
y = 420
for it in items:
    a, b = it.split("|")
    d.text((80, y), a, font=f2, fill=(230, 238, 250)); y += 64
    d.text((80, y), b, font=f3, fill=(140, 170, 210)); y += 110
ava = Image.open("assets/avatar.png").convert("RGBA")
ah = 340
aw = int(ava.width * ah / ava.height)
ava = ava.resize((aw, ah), Image.LANCZOS)
im.paste(ava, (W - aw - 50, H - ah - 40), ava)
im.save(out)
print("ok", out)
