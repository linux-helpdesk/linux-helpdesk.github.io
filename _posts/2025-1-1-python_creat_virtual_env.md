---
title: Python 创建虚拟环境 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

安装 `virtualenv`

```bash
pip3 install virtualenv
```

创建运行环境

```bash
virtualenv [env_name]
# 如果想使用系统的包，加上 --system-site-packages，默认是不加的
```

激活环境

```bash
cd venv 
source bin/activate
```

进入环境后，一切操作和正常使用 Python 一样，安装包使用 `pip install [package]`

退出环境

```bash
deactivate
```

删除环境直接删除该文件夹即可。
