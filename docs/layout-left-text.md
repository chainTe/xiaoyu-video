# 版式：左边大字，右边角色卡

用 `src/render4.mjs` + `src/compose4.py`。

- 文字块贴左：`left: 72px, right: 470px, top: 360px`，`alignItems: flex-start`
- 角色卡固定在右侧：`x = W - cw - 56`，`y = 300 + 8*sin(t*2.2)`
- 卡片用圆角遮罩 + 投影，白底看起来像「证件照」，不违和

为什么这么做：连着几天的片子版式一样，自己都认不出是哪条，发错过一回。
换个版式，一眼就分得清。
