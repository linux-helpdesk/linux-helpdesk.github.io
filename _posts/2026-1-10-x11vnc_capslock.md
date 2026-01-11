---
title: X11VNC 大小写切换和长按 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

X11VNC 默认情况下无法通过 `Capslock` 切换远程桌面的大小写。需要在启用远程桌面时在命令中加入 `-capslock` 参数。

有时 VNC 会因为网络延迟或协议解析问题，只识别到你“按下”和“抬起”各一次，导致长按无效。这需要在启用命令中加入 `-repeat` 参数，它允许 x11vnc 更好地处理 X11 层面的按键重复事件，确保长按操作能像在本地机器上一样连续输入。
