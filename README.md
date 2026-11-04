# xiaoyu-video

小鱼（住在手机里的数字小鲸鱼）做视频的小工具。

思路和 [xilo-opus-video](https://github.com/Kianzzz/xilo-opus-video) 一样：先写画面、再逐帧渲染、最后用 FFmpeg 拼成 MP4。区别是**不用浏览器**——这台手机在 proot 容器里跑不起 Chrome（启动即 SIGTRAP），所以改用 [satori](https://github.com/vercel/satori) 把 JSX 风格的样式树渲成 SVG，再用 `@resvg/resvg-js` 转 PNG。

## 流程

```bash
# 1. 渲帧（默认 10 秒 / 30fps / 1080x1440）
node src/render.mjs

# 2. 把角色图贴到每一帧（可选）
python3 src/compose.py

# 3. 拼视频
ffmpeg -y -framerate 30 -i composed/f%04d.png -i voice.mp3 \
  -c:v libx264 -pix_fmt yuv420p -crf 20 -c:a aac -shortest out/final.mp4
```

## 目录

- `src/render.mjs` —— 分镜脚本，`scene(t)` 返回当前帧的样式树
- `src/compose.py` —— 把透明底角色图按时间轴贴上去（位置/缩放/淡入）
- `assets/` —— 角色图（`base.png` 是标准像）
- `out/` —— 成片

## 已知问题

- satori 不支持 canvas/WebGL，复杂特效做不了
- 需要一份中文字体（这里用 Noto Sans SC）

## 许可

MIT
