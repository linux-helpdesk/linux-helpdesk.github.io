---
title: Linux UFW 防火墙必备操作 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

1.安装

```bash
sudo apt-get install ufw
```

2.启用

```bash
sudo ufw enable
sudo ufw default deny
```

运行以上两条命令后，开启了防火墙，并在系统启动时自动开启。关闭所有外部对本机的访问，但本机访问外部正常。 3.开启/禁用

```bash
sudo ufw allow|deny [service]
```

打开或关闭某个端口，例如：

```bash
sudo ufw allow smtp　允许所有的外部IP访问本机的25/tcp (smtp)端口
sudo ufw allow 22/tcp 允许所有的外部IP访问本机的22/tcp (ssh)端口
sudo ufw allow 53 允许外部访问53端口(tcp/udp)
sudo ufw allow from 192.168.1.100 允许此IP访问所有的本机端口
```

4.查看防火墙状态

```bash
sudo ufw status
```

5.根据端口删除规则 先查询规则号：

```bash
sudo ufw status numbered
```

然后再根据号来删除

```bash
sudo ufw delete 2
```
