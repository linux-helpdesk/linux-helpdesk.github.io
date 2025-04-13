---
title: Nvim Json 文件格式化
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

首先需要你系统中有安装 `jq`。

For json, you could just run `:%!jq .` If you have jq installed on your system.

`:` for command mode

`%` for entire buffer

`!` for run external programm

`jq` - the programm

`.` what to format
