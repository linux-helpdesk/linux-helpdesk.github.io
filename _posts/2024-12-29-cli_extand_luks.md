---
title: 使用命令扩展 LUKS 分区 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

### 扩展 LUKS 加密分区的步骤说明

1. **调整底层物理分区大小**：
   使用 `parted` 工具调整分区大小。假设你要调整 `/dev/sda` 的第二个分区：

   ```bash
   sudo parted /dev/sda
   resizepart 2 90%
   quit
   ```

   - 这里，`resizepart 2 90%` 将第二个分区扩展到磁盘的 90% 大小。

   - 你也可以设置为 `100%`，工具会自行检索所有剩余可用空间，不会影响其他分区。

     > 但这里建议留出一些空余空间，一遍后期有移植需求的时候避免两盘之间 `Sectors` 之间微小的差别导致文件系统损坏

2. **扩展 LUKS 容器**：
   在调整物理分区后，使用 `cryptsetup` 工具扩展 LUKS 加密容器以利用分区新增的空间：

   ```bash
   sudo cryptsetup resize /dev/mapper/sda2_crypt
   ```

   - `/dev/mapper/sda2_crypt` 是加密分区的名称，`resize` 命令扩展 LUKS 容器到分配的分区空间。

   - 这里你还可以通过 `--size` 和 `--device-size` 命令指定想要扩容的可用空间，不加即是默认所有可用空间：

     >     --size, -b <number of 512 byte sectors>
     >        Set the size of the device in sectors of 512 bytes.
     >
     >     --device-size size[units]
     >        Sets new size of the device. If unset real device size is used.
     >
     >        If no unit suffix is specified, the size is in bytes.
     >
     >        Unit suffix can be S for 512 byte sectors, K/M/G/T (or
     >        KiB,MiB,GiB,TiB) for units with 1024 base or KB/MB/GB/TB for 1000
     >        base (SI scale).

3. **扩展文件系统**：
   最后，扩展加密卷中的文件系统（假设是 `ext4` 文件系统）：

   ```bash
   sudo resize2fs /dev/mapper/sda2_crypt
   ```

   - `resize2fs` 扩展文件系统以匹配扩展后的 LUKS 容器。

这三个步骤将底层分区、LUKS 容器和文件系统都扩展到合适的大小。

