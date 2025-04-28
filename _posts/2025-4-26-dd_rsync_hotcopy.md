---
title: DD 热拷贝乱码解决
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

当我们在开机状态使用 `dd` 命令热拷贝备份当前系统分区时，得到的备份分区内的文件一定会出现乱码文件。这是由于 `dd` 命令并不会检查文件一致性，而系统运行过程中很多文件在时刻变动。

解决思路是，首先使用 `dd` 命令克隆分区以保持分区属性一致（文件系统 UUID 及 加密分区的 UUID 等）。然后再删除拷贝出的备份分区内的所有文件，使用 `rsync` 同步数据。

大致命令如下：

```bash
dd if=/dev/sda1 of=/dev/sdb1 status=progress
dd if=/dev/sda2 of=/dev/sdb2 status=progress
dd if=/dev/sda3 of=/dev/sdb3 status=progress
```

修复根目录所在分区：

```bash
cryptsetup open /dev/sdb3 sdb3_crypt
e2fsck -f /dev/mapper/sdb3_crypt -y
```

挂载根分区并使用 `rsync` 进行系统备份：

```bash
mount /dev/mapper/sdb3_crypt /mnt
rm -rf /mnt/*
rsync --progress -av /* /mnt/ --exclude=/mnt --exclude=/proc --exclude=/sys --exclude=/media --exclude=/dev
mkdir /proc /sys /media/ /dev /mnt
```
