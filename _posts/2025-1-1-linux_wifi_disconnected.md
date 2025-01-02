---
title: Linux WIFI 突然断网，显示问号 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

今天 Ubuntu 突然断网，右上角 WIFI 始终显示问号，开关 WIFI 重新连接也不管用，执行以下命令解决：

```bash
sudo systemctl restart NetworkManager
```
现在 WIFI 应该就能恢复正常了。

亦或者你是别的 Linux 发行版，使用的不是 `NetworkManager`，那么你可以执行以下命令：

```bash
nmcli device down wlo1
nmcli device up wlo1
```
wlo1 替换成你的设备名称，设备名称可以通过以下命令查看：

```bash
nmcli device show
```
