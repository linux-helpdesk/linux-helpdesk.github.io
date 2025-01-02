---
title: Micro 总是产生 log.txt 文件 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

Micro 总是在当前路径下生成 `log.txt` 文件是因为 Linux 开发人员在编译时开启了 debug 模式，解决方法是卸载官方源内的 Micro，安装 GitHub 版本。

```bash
curl https://getmic.ro | bash
sudo mv micro /usr/bin
```

