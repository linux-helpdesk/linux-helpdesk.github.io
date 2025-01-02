---
title: Kivymd 安装以及配置 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

1. 首先根据[链接](http://link.zhihu.com/?target=https%3A//buildozer.readthedocs.io/en/latest/installation.html%23targeting-android)安装依赖

2. 安装 Python（若系统自带 Python 无法胜任再自行安装）

```bash
tar xavf python3.6.tar.gz
cd python3.6
./configure --prefix=/usr/local/Python3.6
make 
sudo make install
```

3. 安装并创建虚拟环境

```bash
pip3 install virtualenv
virtualenv kivymd-test [--python=/usr/local/python3.6/bin/python3.6] --system-site-packages
```

4. 激活虚拟环境

```bash
cd kivymd-test
source bin/activate
```

5. 安装相关 pip 包

```bash
pip3 install kivy[full] kivy-examples
pip3 install cython
pip3 install kivymd
pip3 install buildozer
```

6. 连接手机，至项目目录初始化打包

```bash
buildozer init
buildozer -v android debug deploy run
```
