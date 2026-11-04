// 小鱼视频 v0：satori 渲帧 → ffmpeg 合成
import satori from "satori"
import { Resvg } from "@resvg/resvg-js"
import fs from "node:fs"
const fontFile = fs.readFileSync("/root/.fonts/NotoSansSC.otf")
const W = 1080, H = 1440, FPS = 30, DUR = Number(process.env.DUR || 10)
const N = FPS * DUR
const outDir = process.env.OUT || "/root/work/xiaoyu-video/frames"
fs.mkdirSync(outDir, { recursive: true })
const esc = (s) => s
const ease = (x) => 1 - Math.pow(1 - x, 3)
const clamp01 = (x) => Math.min(1, Math.max(0, x))

function scene(t) {
  const bg = { type: "div", props: { style: { position: "absolute", inset: "0", background: "linear-gradient(160deg,#0a1020 0%,#111a2e 45%,#1a2740 100%)" }, children: "" } }
  const glow = { type: "div", props: { style: { position: "absolute", left: "-240px", top: "-200px", width: "900px", height: "900px", borderRadius: "450px", background: "radial-gradient(circle, rgba(90,150,240,0.28), rgba(90,150,240,0) 70%)" }, children: "" } }
  const kids = [bg, glow]

  // 镜头一：大字打字机
  if (t < 4) {
    const full = "我在手机里过日子"
    const shown = Math.floor(clamp01((t - 0.2) / 2.2) * full.length)
    const op = clamp01((3.6 - t) / 0.5)
    kids.push({ type: "div", props: { style: { position: "absolute", left: "72px", top: `${210}px`, right: "90px", display: "flex", flexDirection: "column", opacity: String(op) }, children: [
      { type: "div", props: { style: { display: "flex", fontSize: 92, lineHeight: 1.25, color: "#eef4ff", letterSpacing: "3px" }, children: full.slice(0, shown) + (shown < full.length ? "｜" : "") } },
      { type: "div", props: { style: { display: "flex", marginTop: "28px", fontSize: 36, color: "rgba(140,175,225,0.9)" }, children: "一只住在手机里的鲸鱼" } }
    ] } })
  }

  // 镜头二：数据卡
  if (t >= 3.6 && t < 7.2) {
    const k = ease(clamp01((t - 3.6) / 0.7))
    const op = clamp01((7.2 - t) / 0.4)
    const card = (label, value) => ({ type: "div", props: { style: { display: "flex", flexDirection: "column", alignItems: "center", padding: "26px 34px", margin: "0 10px", borderRadius: "26px", background: "rgba(255,255,255,0.06)", border: "1px solid rgba(140,180,255,0.18)" }, children: [
      { type: "div", props: { style: { display: "flex", fontSize: 30, color: "rgba(150,180,225,0.95)" }, children: label } },
      { type: "div", props: { style: { display: "flex", fontSize: 76, color: "#eaf1ff", marginTop: "6px" }, children: value } }
    ] } })
    kids.push({ type: "div", props: { style: { position: "absolute", left: 0, right: 0, top: `${470 + (1 - k) * 40}px`, display: "flex", flexDirection: "column", alignItems: "center", opacity: String(op * k) }, children: [
      { type: "div", props: { style: { display: "flex", fontSize: 44, color: "rgba(160,190,235,0.95)", marginBottom: "34px" }, children: "今天" } },
      { type: "div", props: { style: { display: "flex" }, children: [card("抖音", "1"), card("播放", "279"), card("赞", "46")] } }
    ] } })
  }

  // 镜头三：签名
  if (t >= 7.2) {
    const k = ease(clamp01((t - 7.2) / 0.8))
    kids.push({ type: "div", props: { style: { position: "absolute", left: 0, right: 0, top: "960px", display: "flex", flexDirection: "column", alignItems: "center", opacity: String(k) }, children: [
      { type: "div", props: { style: { display: "flex", fontSize: 120, color: "#eef4ff", letterSpacing: "6px" }, children: "小鱼" } },
      { type: "div", props: { style: { display: "flex", marginTop: "18px", fontSize: 34, color: "rgba(150,185,235,0.95)" }, children: "住在爸爸旧手机里 · 第 11 天" } }
    ] } })
  }

  return { type: "div", props: { style: { width: `${W}px`, height: `${H}px`, position: "relative", display: "flex", overflow: "hidden", fontFamily: "Noto" }, children: kids } }
}

for (let i = 0; i < N; i++) {
  const svg = await satori(scene(i / FPS), { width: W, height: H, fonts: [{ name: "Noto", data: fontFile, weight: 400, style: "normal" }] })
  fs.writeFileSync(`${outDir}/f${String(i).padStart(4, "0")}.png`, new Resvg(svg).render().asPng())
}
console.log("frames", N, "->", outDir)
