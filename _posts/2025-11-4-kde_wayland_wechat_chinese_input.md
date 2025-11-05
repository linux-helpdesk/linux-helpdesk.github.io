---
title: Linux 下微信无法切换中文输入法（KDE + Wayland）
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

### 对于 **原生 Linux 微信 (com.tencent.weixin)**

微信启动时 Wayland 默认不会继承输入法变量。
 可以强制使用 XWayland + fcitx：

#### ✅ 解决命令（推荐）

```bash
env QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx GTK_IM_MODULE=fcitx QT_QPA_PLATFORM=xcb wechat
```

⚙️ 解释：

- `QT_QPA_PLATFORM=xcb` → 强制微信用 X11 模式（避免 Wayland 键盘抓取问题）
- 其他三个环境变量 → 确保输入法正确连接

你可以把这命令做成桌面启动器修改版。

#### 🔧 修改桌面图标方式

编辑文件：

```bash
sudo nano /usr/share/applications/wechat.desktop
```

找到：

```
Exec=/opt/apps/com.tencent.weixin/files/run.sh
```

改成：

```
Exec=env QT_IM_MODULE=fcitx XMODIFIERS=@im=fcitx GTK_IM_MODULE=fcitx QT_QPA_PLATFORM=xcb /opt/apps/com.tencent.weixin/files/run.sh
```

保存 → 重新从启动器启动微信 → 就能中文输入了 ✅
