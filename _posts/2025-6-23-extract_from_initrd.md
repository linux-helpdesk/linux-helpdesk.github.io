---
title: 从 initrd 中提取文件
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

On Debian and related distributions, you can use the unmkinitramfs script, which is designed to handle different initrd formats.

1. Install initramfs-tools:

```bash
sudo apt-get install initramfs-tools
```

2. Extract the initrd:

```bash
sudo unmkinitramfs /boot/initrd.img-$(uname -r) .
```

This will extract the contents into the current directory.

3. Repack the initrd (using mkinitramfs):

```bash
sudo mkinitramfs -o new_initrd.img .
```
