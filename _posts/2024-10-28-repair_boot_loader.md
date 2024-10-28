---
title: "Linux 修复引导万能方法"
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

当 Linux 出现引导异常，无法正常启动系统时，可以参考本教程修复大多数问题：

首先，您需要准备一个 U 盘，并刷入对应系统发行版的 LiveCD 系统（即安装系统时用于从 U 盘启动的那个系统）。

- 如果待修复系统是 Arch 系，则选择 Arch 系的发行版 LiveCD。
- 如果是 Debian 系，则选择 Debian 系的 LiveCD。

将 U 盘插入需要修复的电脑并从 LiveCD 系统启动。

## 确认引导类型

在修复之前，需要确认系统的引导类型，分为 UEFI 和非 UEFI 两种。可以通过以下命令查看分区列表，以确认是否有 EFI 分区：

```shell
sudo fdisk -l
```

如果分区表中有一个分区标记为 `EFI System`（通常是 `/dev/sda1`），则系统很可能是 UEFI 引导；否则可能是非 UEFI。

## UEFI 引导修复：

假设您的 EFI 分区在 `/dev/sda1` 上，根分区在 `/dev/sda2` 上。

1. **修复文件系统（可选，但推荐）**：在挂载之前，建议先检查分区的一致性，以确保文件系统没有损坏。可以使用 `fsck` 命令来修复分区：

   ```shell
   sudo fsck /dev/sda2  # 检查并修复根分区
   sudo fsck /dev/sda1  # 检查并修复 EFI 分区
   ```

2. **挂载根分区和 EFI 分区**：

   ```shell
   sudo mount /dev/sda2 /mnt
   sudo mount /dev/sda1 /mnt/boot/efi
   ```

3. **挂载系统文件目录**：

   ```shell
   for i in /dev /dev/pts /proc /sys /run; do sudo mount -B $i /mnt$i; done
   ```

4. **进入 chroot 环境**：

   ```shell
   sudo chroot /mnt
   ```

5. **更新 initramfs 并重新安装 GRUB**：

   ```shell
   update-initramfs -u
   grub-install /dev/sda
   update-grub
   ```

## 非 UEFI 引导修复：

假设您的 boot 分区在 `/dev/sda1`，根分区在 `/dev/sda2`。

1. **修复文件系统（可选，但推荐）**：

   ```shell
   sudo fsck /dev/sda2  # 检查并修复根分区
   sudo fsck /dev/sda1  # 检查并修复 boot 分区
   ```

2. **挂载根分区和 boot 分区**：

   ```shell
   sudo mount /dev/sda2 /mnt
   sudo mount /dev/sda1 /mnt/boot
   ```

3. **挂载系统文件目录到 `/mnt`**：

   ```shell
   sudo mount --bind /dev /mnt/dev
   sudo mount --bind /dev/pts /mnt/dev/pts
   sudo mount --bind /proc /mnt/proc
   sudo mount --bind /sys /mnt/sys
   ```

4. **进入 chroot 环境**：

   ```shell
   sudo chroot /mnt
   ```

5. **更新 initramfs 并重新安装 GRUB**：

   ```shell
   update-initramfs -u
   grub-install /dev/sda
   grub-install --recheck /dev/sda
   update-grub
   ```

完成以上步骤重启电脑即可。

> 本文的主要修复步骤基于 Debian 系列的命令，若您使用的是 Arch 系，请注意以下命令差异：
>
> 1. **更新 initramfs**  
>
>    - 在 Debian 系中，使用 `update-initramfs`。
>
>    - 在 Arch 系中，使用 `mkinitcpio` 生成 initramfs：
>
>      ```shell
>      mkinitcpio -P
>      ```
>
> 2. **重新安装 GRUB**  
>
>    - 在 Debian 系中，使用 `update-grub` 来更新 GRUB 配置。
>
>    - 在 Arch 系中，没有 `update-grub`，需要手动生成 GRUB 配置文件：
>
>      ```bash
>      grub-mkconfig -o /boot/grub/grub.cfg
>      ```
