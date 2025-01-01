---
title: Linux TTY 纯终端修改字体大小 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在 Linux 纯终端（TTY，非图形界面）中，调整字体大小需要修改终端的字体配置。以下是几种常用的调整方法：

### 方法一：使用 `setfont` 命令

1. 在终端中输入 `setfont` 命令来更改字体：

   ```bash
   sudo setfont /usr/share/consolefonts/字体名称
   ```

   可以通过以下命令查看可用的字体列表：

   ```bash
   ls /usr/share/consolefonts
   ```

   例如，常见的字体文件有 `Lat15-TerminusBold20x10.psf.gz`，这个文件代表20x10的字体大小。

2. 选择适合你的字体大小后，使用 `setfont` 命令来加载字体。

### 方法二：通过 `console-setup` 配置

1. 使用以下命令来配置控制台字体：

   ```bash
   sudo dpkg-reconfigure console-setup
   ```

2. 按照提示选择合适的字符集、字体类型和字体大小。

3. 配置完成后，系统将应用新的字体设置。

通过这些方法，你可以在 Linux 纯终端中调整字体大小，以适应不同的屏幕分辨率或个人偏好。
