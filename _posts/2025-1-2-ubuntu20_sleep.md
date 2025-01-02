---
title: Ubuntu 20.04 设置休眠 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

> 目前只分区 swap 实现了休眠，文件形式的 swap 分区未成功休眠。

Ubuntu 默认竟然默认没有开启休眠，令人无语，记录一下开启休眠的方法，

执行命令测试：

```bash
sudo systemctl hibernate
```

命令运行后关机了，但重新开机后发现休眠没有起作用，还是关机。

检查 swap 类型及大小

要实现休眠，要求 swap 空间要大于等于系统内存。

查看内存及 swap 大小：

```bash
free -m
```

如果swap小于内存，需要先调整swap空间大小。

查看swap类型：

```bash
swapon -s
```

查找swap的UUID：

```bash
grep swap /etc/fstab
```

修改grub配置

```bash
sudo vi /etc/default/grub
```

找到 GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" 一行，在 quiet splash 后添加：resume=UUID=××××，这里可以添加分区名也可以添加 UUID。但经本机实践，在 Ubuntu 18要用 UUID才能成功。

最后结果为：

```text
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash resume=UUID=××××××"
```

执行命令生效修改：

```bash
sudo update-grub
```

执行休眠命令

```bash
sudo systemctl hibernate
```

开机后发现休眠成功。

注意事项：swap 一定要大于等于内存容量，如果太少，要调整 swap 空间，用 UUID 指定 swap 位置。

添加休眠按扭

```bash
sudo gedit /etc/polkit-1/localauthority/50-local.d/com.ubuntu.enable-hibernate.pkla
```

添加以下内容并保存

```text
[Re-enable hibernate by default in upower]
Identity=unix-user:*
Action=org.freedesktop.upower.hibernate
ResultActive=yes

[Re-enable hibernate by default in logind]
Identity=unix-user:*
Action=org.freedesktop.login1.hibernate;org.freedesktop.login1.handle-hibernate-key;org.freedesktop.login1;org.freedesktop.login1.hibernate-multiple-sessions;org.freedesktop.login1.hibernate-ignore-inhibit
ResultActive=yes
```

![](/assets/images/ubuntu_sleep.webp)

其中，swap 分区 /etc/fstab 文件挂载设置如下：

```text
...
UUID=3f990628-373a-4ff5-879c-d4bfcb8ea1a6 swap    swap    defaults    0  0
...
```
