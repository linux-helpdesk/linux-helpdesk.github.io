---
title: 查看硬盘上安装的系统名称 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

查看目标硬盘上的 `etc/issue` 文件：
```bash
sudo mount /dev/sdxy /mnt
cat /mnt/etc/issue
```
