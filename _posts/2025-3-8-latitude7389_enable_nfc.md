---
title: Dell Latitude 7389 Ubuntu 使用 NFC 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 环境检查

当前系统环境为 Ubuntu 22.04。首先执行 `lsusb` 得到以下结果：

```bash
warren@localhost:~$ lsusb
Bus 002 Device 002: ID 0bda:0328 Realtek Semiconductor Corp. USB3.0-CRW
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 002: ID 0bda:5650 Realtek Semiconductor Corp. Integrated Webcam_HD
Bus 001 Device 004: ID 0a5c:5834 Broadcom Corp. 5880
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
```

其中 `Broadcom Corp. 5880` 就是我们的 NFC 设备，该设备同时负责 NFC 模块及指纹模块。下面我们主要进行两部分操作：启用 NFC 和进行 NFC 卡片的读取。

## 启用 NFC

使用[这个项目](https://github.com/jacekkow/controlvault2-nfc-enable)启用 NFC。

```bash
git clone https://github.com/jacekkow/controlvault2-nfc-enable.git
sudo apt install python3 python3-usb 
cd controlvault2-nfc-enable/
sudo ./nfc.py on
```

## 读取 NFC 卡片

```bash
sudo apt-get update
sudo apt-get install pcscd pcsc-tools
sudo systemctl start pcscd
sudo systemctl status pcscd
pcsc_scan
```

此命令会自动扫描并显示系统中检测到的智能卡阅读器及相关信息，例如设备名称、ATR（复位应答）、卡片状态等。如果没有检测到阅读器，它会显示类似 “Waiting for the first reader...” 的提示。

当你将智能卡或 NFC 卡放到阅读器上时，pcsc_scan 会实时更新显示卡片的详细信息。如果卡片被移除，状态也会相应改变。要停止扫描，可使用 Ctrl+C 退出程序。

以上工具只会显示大致的卡片信息，且不会将卡片信息 dump 到本地，先面进行进一步环境搭建来 dump 卡片信息。

普通 `nfc-mfcclassic` 工具无法使用我们这台电脑的 NFC 硬件，所以我们需要找到基于 PCSC 的 NFC 卡片读取项目。比如 PySCard 或 [nfc-pcsc](https://github.com/pokusew/nfc-pcsc)。
