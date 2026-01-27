---
title: `brightnessctl` 与 `ddcutil` 简明使用指南
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

#### 🔹 1. 调节笔记本屏幕亮度（用 `brightnessctl`）

```bash
# 安装（如未安装）
sudo apt install brightnessctl    # Debian/Ubuntu
sudo dnf install brightnessctl    # Fedora

# 查看当前亮度
brightnessctl

# 设置亮度（百分比或绝对值）
brightnessctl set 50%     # 设为 50%
brightnessctl set +10%    # 增加 10%
brightnessctl set -10%    # 减少 10%
```

> ✅ 仅适用于笔记本内置屏幕，对外接显示器无效。

------

#### 🔹 2. 调节外接显示器亮度（用 `ddcutil`）

> ⚠️ 前提：显示器需在 OSD 菜单中 **开启 DDC/CI**（通常在“设置”→“系统”里）。

```bash
# 安装
sudo apt install ddcutil    # Debian/Ubuntu
sudo dnf install ddcutil    # Fedora

# 检测显示器
sudo ddcutil detect

# 查看当前亮度
sudo ddcutil getvcp 10

# 设置亮度（0–100）
sudo ddcutil setvcp 10 60
```

> ✅ 适用于 HDMI / DisplayPort 外接显示器。
> 💡 亮度值范围通常是 0–100，具体以 `getvcp 10` 输出为准。

------

#### 🔸 小贴士

- 若不想每次输 `sudo`，可将用户加入 `i2c` 组并配置 udev 规则（略）。
- `ddcutil` 还能调对比度（`setvcp 12`）、切换输入源等，但亮度最常用。

------

✅ 记住：

- **内屏 → `brightnessctl`**
- **外屏 → `ddcutil`（需开启 DDC/CI）**
