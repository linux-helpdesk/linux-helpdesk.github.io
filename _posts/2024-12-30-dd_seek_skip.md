---
title: DD 命令指定位置读取写入
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## `seek` 指定被写入对象的起始位置

要将 `sda.dd` 文件写入 `/dev/sda`，并从分区的 2MB 位置开始写入，可以使用以下 `dd` 命令：

```bash
sudo dd if=sda.dd of=/dev/sda bs=1M seek=2
```

### 解释：

- `if=sda.dd`：指定输入文件为 `sda.dd`。
- `of=/dev/sda`：指定输出目标为 `/dev/sda`。
- `bs=1M`：指定块大小为 1MB，这样 `seek=2` 就是从 2MB 位置开始写入。
- `seek=2`：跳过输出文件（即 `/dev/sda`）的前 2 个 1MB 块（即 2MB 位置），开始写入数据。

这个命令会在 `/dev/sda` 的 2MB 位置开始写入 `sda.dd` 文件的内容。

## `skip` 指定读取对象的起始位置

如果你想从 `sda.dd` 文件的 2MB 位置开始读取数据并写入到 `/dev/sda`，可以使用 `dd` 命令的 `skip` 参数。以下是命令：

```bash
sudo dd if=sda.dd of=/dev/sda bs=1M skip=2
```

### 解释：

- `if=sda.dd`：指定输入文件为 `sda.dd`。
- `of=/dev/sda`：指定输出目标为 `/dev/sda`。
- `bs=1M`：指定块大小为 1MB，这样 `skip=2` 就会跳过 2MB 数据。
- `skip=2`：跳过输入文件（即 `sda.dd`）的前 2 个 1MB 块（即 2MB 位置），从 2MB 开始读取数据。

这个命令会从 `sda.dd` 文件的 2MB 位置开始读取，并写入到 `/dev/sda`。

> 如果不指定 `bs` 大小，则默认 512。
>
> 同 `fdisk -l` 命令输出结果中的 `sector` 数值。

