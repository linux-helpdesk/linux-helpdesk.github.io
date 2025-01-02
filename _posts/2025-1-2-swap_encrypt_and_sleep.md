---
title: 加密 Swap 分区并实现休眠 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---


```bash
# 创建 「加密分区」 和 「swap 分区」 前的准备工作
sudo swapon --summary # Check the detail of the swap partitions
sudo swapoff /dev/sdXY

# 创建 「加密分区」 和 「swap 分区」
sudo cryptsetup luksFormat /dev/sdXY
sudo cryptsetup open /dev/sdXY swap_partition
sudo mkswap /dev/mapper/swap_partition
sudo blkid | grep /dev/mapper/swap_partition # 查看映射后的 「swap 分区」 的 UUID

# 写入 /etc/crypttab 和 /etc/fstab 配置文件
## /etc/crypttab
swap UUID=01c5a946-8327-4fb1-ac77-276445c5edab none 
## /etc/fstab
UUID=43b69911-5435-4aa2-bcab-1aabc39a3e5b swap    swap    defaults    0  0 # 在 / 分区挂载前后都可

# 编辑 /etc/default/grub 文件
## 在 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" 后加入 resume=UUID=XXXX
## /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash resume=UUID=43b69911-5435-4aa2-bcab-1aabc39a3e5b"

# 更新 initramfs，这一步很关键 ！！！！！！！！！
sudo update-grub
sudo update-initramfs -u
sudo update-grub
```

最后一步很关键！！！！！！！！！！！！

（但如果你的 swap 分区是安装全盘加密系统时自动生成的，这一步就不需要）

猜测，若不更新 initramfs，新建的加密分区不会写入内核，而是会在加载根分区后通过 /etc/crypttab 文件加载，故无法在加载根分区之前从 swap 分区加载内存文件。这也是为什么不加密分区和出厂加密分区无需执行此命令即可被 grub 识别并加载。

