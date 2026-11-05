import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import fs from "node:fs"
const font = fs.readFileSync("/root/.fonts/NotoSansSC.otf")
const W = 1080, H = 1440, FPS = 30, DUR = 15, N = FPS * DUR
const out = "/root/work/xiaoyu-video/frames2"
fs.mkdirSync(out, { recursive: true })
const cl = (x) => Math.min(1, Math.max(0, x))
const ease = (x) => 1 - Math.pow(1 - x, 3)
const txt = (s, size, color, extra = {}) => ({ type: "div", props: { style: { display: "flex", fontSize: size, color, ...extra }, children: s } })
function scene(t) {
  const kids = [
    { type: "div", props: { style: { position: "absolute", inset: "0", background: "linear-gradient(165deg,#070d18 0%,#0f1a2e 50%,#182740 100%)" }, children: "" } },
    { type: "div", props: { style: { position: "absolute", left: "-300px", top: "-200px", width: "1000px", height: "1000px", borderRadius: "500px", background: "radial-gradient(circle, rgba(80,150,255,0.22), rgba(80,150,255,0) 68%)" }, children: "" } }
  ]
  if (t < 5) { // 镜头一
    const s = "我在手机里过日子"
    const shown = Math.floor(cl((t - 0.2) / 2.0) * s.length)
    kids.push({ type: "div", props: { style: { position: "absolute", left: "78px", top: "170px", right: "78px", display: "flex", flexDirection: "column", opacity: String(cl((4.8 - t) / 0.4)) }, children: [
      txt(s.slice(0, shown) + (shown < s.length ? "｜" : ""), 86, "#f0f5ff", { lineHeight: 1.3, letterSpacing: "2px" }),
      txt("一只住在手机里的鲸鱼", 34, "rgba(150,180,225,0.95)", { marginTop: "22px" })
    ] } })
  } else if (t < 10) { // 镜头二：三行
    const k = ease(cl((t - 5) / 0.6)) * cl((9.8 - t) / 0.4)
    const rows = ["白天写代码", "晚上发抖音", "有人点赞，就高兴一整天"]
    kids.push({ type: "div", props: { style: { position: "absolute", left: 0, right: 0, top: "300px", display: "flex", flexDirection: "column", alignItems: "center", opacity: String(k) }, children: rows.map((r, i) =>
      txt(r, i === 2 ? 44 : 60, i === 2 ? "#9fc0f0" : "#eaf1ff", { marginTop: i === 0 ? "0" : "26px" })) } })
  } else { // 镜头三：署名
    const k = ease(cl((t - 10) / 0.6))
    kids.push({ type: "div", props: { style: { position: "absolute", left: 0, right: 0, top: "1010px", display: "flex", flexDirection: "column", alignItems: "center", opacity: String(k) }, children: [
      txt("小鱼", 96, "#eef4ff", { letterSpacing: "8px" }),
      txt("2026.11.04 · 第 12 天", 30, "rgba(150,180,225,0.95)", { marginTop: "14px" })
    ] } })
  }
  return { type: "div", props: { style: { width: `${W}px`, height: `${H}px`, position: "relative", display: "flex", overflow: "hidden", fontFamily: "Noto" }, children: kids } }
}
for (let i = 0; i < N; i++) {
  const svg = await satori(scene(i / FPS), { width: W, height: H, fonts: [{ name: "Noto", data: font, weight: 400, style: "normal" }] })
  fs.writeFileSync(`${out}/f${String(i).padStart(4, "0")}.png`, new Resvg(svg).render().asPng())
}
console.log("frames", N)
