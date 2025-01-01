---
title: SSH 终端播放视频 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---


```bash
ssh -C -Y ...
cvlc --vout x11 file.mp4
```

> `cvlc`：使用本机默认显示配置，否则会因云端与本机显示配置不同而卡顿
>
> `--vout x11`：不加会卡顿

