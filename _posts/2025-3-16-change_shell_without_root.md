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

## 其他

如有 `conda` 环境，还需要对其进行配置，将如下内容加入 `.zshrc` 文件中：

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/susi0001/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/susi0001/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/susi0001/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/susi0001/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

这里 `bash` 和 `zsh` 环境中 `conda` 初始化脚本唯一的区别就是 `shell.bash` 和 `shell.bash`。
