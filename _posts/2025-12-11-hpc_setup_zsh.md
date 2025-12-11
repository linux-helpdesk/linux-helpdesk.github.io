---
title: 无 ROOT 权限为当前用户安装 ZSH 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 编译安装 ZSH 

```bash 
wget https://downloads.sourceforge.net/project/zsh/zsh/5.9/zsh-5.9.tar.xz
tar xf zsh-5.9.tar.xz
cd zsh-5.9

./configure --prefix=$HOME/.local \
            --bindir=$HOME/.local/bin \
            --libdir=$HOME/.local/lib \
            --datarootdir=$HOME/.local/share \
            --enable-multibyte
make -j$(nproc)
make install
```

## 设置 ZSH 登录自启动

在 `.bash_profile` 文件结尾添加如下内容：

```bash 
cat .bash_profile        
# .bash_profile

...

# User specific environment and startup programs

# 如果检测到交互式 Shell，则自动启动 zsh
if [ -t 0 ]; then
  exec ~/.local/bin/zsh -l
fi
```
