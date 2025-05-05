---
title: Linux 下我的世界服务器搭建及客户端下载及配置
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 服务端搭建

环境准备

```bash
sudo apt update
sudo apt install openjdk-21-jre-headless
sudo ufw allow 25565 # Optional
```

在[此链接](https://www.minecraft.net/download/server)下载服务端文件，下载后使用如下命令运行服务端

```bash
java -Xmx1024M -Xms1024M -jar minecraft_server.1.21.5.jar nogui
```

初次运行后会产生 `eual.txt` 文件，将文件中的 `false` 更改为 `true` 后再使用上述命令重新运行服务端，即可完成服务端搭建。

## 客户端下载

[GitHub 项目地址](https://github.com/HMCL-dev/HMCL/releases)
