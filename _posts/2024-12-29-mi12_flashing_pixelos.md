---
title: 小米 12 安装 Pixel OS 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 重点注意事项

1. 安装方式

小米 12 安装 Pixel OS 分两种方式：TWRP 刷写和 Pixel OS 原生 Recovery 刷写。
这里由于大多数情况下我们刷写 Pixel OS 的底包并非官方要求的系统版本，原生 Recovery 功能太少无法对某些分区进行格式化，会导致刷写系统包后无法进入系统。
**所以这里我们统一采用 TWRP 刷写方式。**

2. 文件日期

刷写小米 12 的 Pixel OS 主要涉及五个文件：

- PixelOS_cupid-14.0-xxx.zip
- dtbo-cupid-xxx.img
- boot-cupid-xxx.img
- vendor_boot-cupid-xxx.img
- twrp-3.7.1_12-v8.6_A14-cupid-skkk.img
**下载前四个文件的时候注意文件名中的日期，应选相同或相近的日期，否则在系统安装那一步会签名校验出错。**

## 刷入系统

解锁 BL 的环节请自行解决，这里不再赘述，直接开始刷写步骤。

- 手机关机后按 `电源键 + 音量下` 进入 Fastboot 模式
- 依次执行以下几条命令：
  ```bash
  fastboot flash vendor_boot <path/to/vendor_boot-xxx.img>
  fastboot flash dtbo <path/to/dtbo-xxx.img>
  fastboot flash boot <path/to/boot-xxx.img>
  fastboot flash recovery <path/to/twrp-xxx.img>
  ```

将上述文件名替换为自己的文件对应的文件名，然后再次输入以下命令进入 Recovery 模式：

```bash
fastboot reboot recovery
```

在 Recovery 中选择 ADB Sideload 更新，然后在电脑端使用一下命令开始系统的刷入：

```bash
adb sideload PixelOS_cupid-14-xxx.zip
```

刷入后返回主界面，进入清除，勾选所有可以勾选的分区然后全部格式化。完成后重启即可进入系统了。
