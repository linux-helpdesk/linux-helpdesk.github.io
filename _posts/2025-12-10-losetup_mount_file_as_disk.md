---
title: 将文件作为磁盘驱动器挂载
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

将普通文件挂载为可通过 `fdisk` 访问的驱动器，其核心是利用 Linux 的 **“循环设备”（loop device）** 功能。这个功能允许你将一个文件（如 `.img` 文件）虚拟成一块块设备（就像一块物理硬盘），从而可以使用 `fdisk` 进行分区、格式化等所有磁盘操作。

整个过程可以概括为：**创建文件 → 关联到循环设备 → 使用 `fdisk` 分区 → 格式化分区 → 挂载使用**。

### 📝 完整操作步骤

**第1步：创建一个指定大小的空文件**
使用 `dd` 命令创建一个全零文件。这里创建一个 1GB 的文件作为示例：
```bash
dd if=/dev/zero of=./virtual_disk.img bs=1M count=1024
```
*   `if=/dev/zero`：输入源，一个无限输出零的字符设备。
*   `of=./virtual_disk.img`：输出文件，即你要创建的虚拟磁盘文件。
*   `bs=1M`：每次读写的块大小为 1MB。
*   `count=1024`：读写 1024 个块，总计 1024MB (1GB)。

**第2步：将文件关联到一个可用的循环设备**
使用 `losetup` 命令将该文件“伪装”成一块硬盘：
```bash
sudo losetup -fP ./virtual_disk.img
```
*   `-f`：自动查找下一个空闲的循环设备（例如 `/dev/loop0`）。
*   `-P`：**关键参数**。它会让内核在关联后立即扫描该设备，以便识别可能的分区表，为后续分区操作做准备。
*   执行后，你可以用 `losetup -a` 查看关联情况，虚拟磁盘文件通常会绑定到类似 `/dev/loop0` 的设备上。

**第3步：使用 `fdisk` 对虚拟磁盘进行分区**
现在，你可以像操作一块新硬盘一样操作这个循环设备。假设上一步找到的设备是 `/dev/loop0`：
```bash
sudo fdisk /dev/loop0
```
进入 `fdisk` 交互界面后，常用按键序列如下：
1.  输入 `n` 创建一个新分区。
2.  选择分区类型（`p` 主分区 / `e` 扩展分区）。
3.  设置分区号、起始扇区和结束扇区（通常直接按回车使用默认值即可使用全部空间）。
4.  分区完成后，输入 `w` **将分区表写入磁盘并退出**。

> 注：完成此步后，由于之前使用了 `-P` 参数，系统会自动创建代表分区的设备文件，例如第一个分区会是 `/dev/loop0p1`。如果没有，可以运行 `partprobe /dev/loop0` 或重启系统来让内核重读分区表。

**第4步：格式化分区**
假设你创建了分区 `/dev/loop0p1`，并将其格式化为 ext4 文件系统：
```bash
sudo mkfs.ext4 /dev/loop0p1
```

**第5步：挂载分区使用**
创建一个挂载点，然后将分区挂载上去，就可以像普通硬盘一样访问了：
```bash
sudo mkdir -p /mnt/virtual_disk
sudo mount /dev/loop0p1 /mnt/virtual_disk
```
现在，你可以通过 `/mnt/virtual_disk` 目录访问这个虚拟驱动器了。

### 💡 操作要点与提示
*   **整个过程的核心**：`losetup -fP` 命令是创建“可分区”虚拟驱动器的关键。
*   **查看关联状态**：任何时候都可以使用 `losetup -a` 查看所有关联的循环设备，使用 `lsblk /dev/loop0` 查看该虚拟磁盘的分区结构。
*   **如何安全卸载**：先卸载分区 `sudo umount /mnt/virtual_disk`，再解除循环设备关联 `sudo losetup -d /dev/loop0`。
*   **文件是固定的**：请注意，这种方式创建的虚拟磁盘大小是固定的（上面示例是1GB）。如果需要动态扩容，可以考虑使用 `qcow2` 格式，但这需要QEMU等虚拟化工具支持，`fdisk` 无法直接操作 `qcow2` 文件。
*   **确保文件路径正确**：在关联和挂载时，请确保使用的是正确的**分区设备路径**（如 `/dev/loop0p1`），而不是整个循环设备路径（如 `/dev/loop0`）。

### 📖 进阶场景：如何处理已存在的磁盘映像
如果你有一个现成的磁盘映像文件（例如从虚拟机中导出的 `.img` 文件），并想查看或修改其分区内容，可以直接从第2步开始：
```bash
# 将现有的映像文件关联到循环设备
sudo losetup -fP /path/to/your/existing_disk.img
# 查看其分区结构
lsblk /dev/loop0
# 直接挂载其中的某个分区
sudo mount /dev/loop0p1 /mnt/some_mount_point
```

如果要卸载设备：
```bash
sudo umount /dev/loop0p1
sudo losetup -d /dev/loop0
```

这种方法非常实用，常用于检查、修复或修改系统镜像、恢复数据等场景。


