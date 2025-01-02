---
title: 去除 Linux 微信窗口阴影
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

**详细教程链接：**

[https://forum.ubuntu.org.cn/viewtopic.php?f=73&t=491709](http://link.zhihu.com/?target=https%3A//forum.ubuntu.org.cn/viewtopic.php%3Ff%3D73%26t%3D491709)

**补充：**

终端输入 `xwininfo`，用鼠标点击微信边框的阴影处，具体位置是边框线靠外一点点。





![](/assets/images/linux_wechat_shadow.webp)

![](/assets/images/xwininfo_4_wechat.webp)

终端输入 `xdotool windowunmap [id]` 即可去除阴影。这里的 ID 是 `0x7800014`，和主窗口 ID `0x0780000c` 差 8。
