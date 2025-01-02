---
title: Linux 下文件解压缩中文乱码问题的解决 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

将带中文文件名的压缩文件上传到服务器，使用 `unzip` 解压后，文件名乱码：

**临时解决方法：**

通过 `unzip` 行命令解压，指定字符集 `unzip -O CP936 xxx.zip` （或 GBK, GB18030，想了解更多可以通过 `man unzip` 查看该选项的说明。）

**永久生效方法：**

在环境变量中，指定 `unzip` 参数，总是以指定的字符集显示和解压文件 `/etc/environment` 中加入2行

```bash
UNZIP="-O CP936"
ZIPINFO="-O CP936"
```
