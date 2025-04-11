---
title: Linux 下麦克风严重杂音 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

### **1. 降低 ALSA/PulseAudio 输入增益**

杂音可能是由 **过高的麦克风或音频增益** 引起：

```bash
alsamixer
```

- 按 **F6** 选择 `HDA Intel PCH` 声卡
- 找到以下通道并调整：
  - `Master` 或 `Speaker`：降低至 70-80%
  - `Mic Boost` 或 `Capture`：设置为 0%（或禁用）
  - `Auto-Mute Mode`：设置为 `Disabled`
- 按 `Esc` 保存退出
- 可使用命令 `sudo alsactl store` 命令来保存当前配置。
- 下次开机后使用 `sudo alsactl restore` 重新加载已保存的配置。

------

### **2. 强制指定 ALC256 的降噪参数**

编辑 ALSA 配置以启用噪音抑制：

```bash
sudo nvim /etc/modprobe.d/alsa-base.conf
```

添加以下参数（尝试不同组合）：

```bash
# 启用噪音抑制（常见于笔记本）
options snd-hda-intel model=alc256-dac
# 或
options snd-hda-intel model=alc256-asus-headset
# 或禁用电源管理（防止电流干扰）
options snd-hda-intel power_save=0
```

保存后更新并重启：

```bash
sudo update-initramfs -u
sudo reboot
```
