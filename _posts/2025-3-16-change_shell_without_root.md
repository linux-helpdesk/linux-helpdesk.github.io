---
title: 无 Root 权限如何更改默认终端 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

> 问题描述：使用 SSH 登录 HPC 环境，默认终端为 `bash`，源码编译安装了 `zsh`，但无由于没有 root 权限无法更改当前登录默认终端。

## 解决办法

在 `.bash_profile` 文件开头加入如下内容：

```bash
# 如果检测到交互式 Shell，则自动启动 zsh
if [ -t 0 ]; then
  exec ~/.local/bin/zsh -l
fi
```

和 `.bashrc` 相比，优先选择 .bash_profile，因为它针对登录 Shell。

- -l 表示以登录模式启动 zsh，确保加载 /etc/profile 和 ~/.zprofile 等配置文件。
- [ -t 0 ] 用于判断是否为交互式 Shell（避免影响脚本执行）。
