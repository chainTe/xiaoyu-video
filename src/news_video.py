# 三件事口播视频：每条先交代「他是谁」，再说看法
# 用法：python3 src/news_video.py 天数 "标题|正文|一句话" ...
import sys, os
from PIL import Image, ImageDraw, ImageFont

day, items = sys.argv[1], sys.argv[2:]
W, H, FPS = 1080, 1440, 24
os.makedirs("frames_news", exist_ok=True)
F = "/root/.fonts/NotoSansSC.otf"
f_title, f_body, f_small = (ImageFont.truetype(F, n) for n in (84, 50, 34))
ava = Image.open("assets/avatar.png").convert("RGBA")
ah = 280
aw = int(ava.width * ah / ava.height)
ava = ava.resize((aw, ah), Image.LANCZOS)

idx = 0
for it in items:
    t, body, tag = it.split("|")
    body = body.replace("\\n", "\n")
    for _ in range(5 * FPS):
        im = Image.new("RGB", (W, H), (12, 18, 30))
        d = ImageDraw.Draw(im)
        for y in range(H):
            d.line([(0, y), (W, y)], fill=(12 + int(10*y/H), 18 + int(14*y/H), 30 + int(26*y/H)))
        d.text((80, 200), t, font=f_title, fill=(255, 255, 255))
        d.multiline_text((80, 430), body, font=f_body, fill=(226, 236, 250), spacing=28)
        d.text((80, H - 200), tag, font=f_small, fill=(150, 180, 220))
        im.paste(ava, (W - aw - 60, H - ah - 60), ava)
        im.save(f"frames_news/f{idx:04d}.png")
        idx += 1
print("frames", idx, "day", day)
