---
title: 最新版 Typora 激活方法
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

> 次方法全平台通用，在此仅以 Linux 平台作为实验展示

## 第一步：安装  

下载最新版 Typora 并安装：

```bash 
sudo dpkg -i typora-xxx.deb
```

## 第二步：寻找 Lincense 文件

寻找 Licence 文件，找到 Typora 安装目录并进入 `resources/page-dist/static/js` 路径下：

```bash 
$ whereis typora
typora: /usr/bin/typora /usr/share/typora
$ cd /usr/share/typora/resources/page-dist/static/js
$ ls | grep License
LicenseIndex.180dd4c7.54684560.chunk.js
runtime-LicenseIndex.180dd4c7.f7c007dd.js
```

## 第三步：替换 

打开 LicenseIndex 文件，并替换 `hasActivated="true"==e.hasActivated` 为 `hasActivated="true"=="true"`。
