---
title: 如何检查固态硬盘健康度
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

**Windows 系统下：**

使用 `CryptalDisk` 工具查看，重点查看 `03：可用备用空间` 及 `0E：媒体与数据完整性错误计数`。

`03` 最佳为 100，数值越低，代表健康度越差。

`0E` 最佳为 0，数值越高，代表健康读越差。

**Linux 系统下：**

使用 `scartctl` 工具查看。

安装方式

```bash
sudo apt install smartmontools
```

使用方式

```bash
sudo smartctl --all /dev/nvme0n1
```

`03` 和 `0E` 分别对应 `Available Spare` 和 `Media and Data Integrity Errors`。
