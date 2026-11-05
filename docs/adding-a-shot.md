# 加一个分镜

分镜都在 `src/render.mjs` 里的 `scene(t)`：给一个时间（秒），返回这一帧的样式树。

```js
if (t >= 5 && t < 10) {
  const k = ease(clamp((t - 5) / 0.6))   // 入场进度 0→1
  kids.push({
    type: "div",
    props: {
      style: {
        position: "absolute", left: 0, right: 0, top: "300px",
        display: "flex", flexDirection: "column", alignItems: "center",
        opacity: String(k)                 // 淡入
      },
      children: [/* 文本或色块 */]
    }
  })
}
```

几条经验：

- 每帧都要给**确定的样式**，不要依赖浏览器默认值（satori 不是浏览器）
- 想要「弹一下」就自己算缓动，satori 不跑 CSS animation
- 中文一定要在 `fonts` 里传字体，不然是方框
- 时间轴用 `t` 算，别用 `Math.random()`，不然每帧都不一样
