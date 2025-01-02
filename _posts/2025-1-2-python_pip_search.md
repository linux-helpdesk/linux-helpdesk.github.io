---
title: pip search 用不了了怎么办？？？ 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

由于某些说来很气的原因，Python 的包管理器 `pip search` 功能用不了了。这可是 Python 语言的一大亮点啊，怎么能缺！！！

今天给大家介绍两个小工具来替代 `pip search` 功能：`pip_search` 和 `pipq`。

两款工具安装都非常简单，Python 仓库就可以拉取到。

### 1. pip_search

安装：

```bash
$ pip3 install pip_search
```

使用:

```bash
$ pip_search [package_name]
```

后面的 `[package_name]` 即为你要搜索的相关信息。这里我们以搜索 `pipsearch` 来举例，执行 `pip_search pipsearch` 得到以下结果：

![](/assets/images/pip_search_001.webp)

结果会以表格的形式反馈，而且比原来的还要好看！！！

这里大家能看到表格里的第二个选项就是我今天要给大家介绍的第二款工具：`pipq`。



### 2. pipq

安装：

```bash
$ pip3 install pipq
```

使用：

```bash
$ pipq search [package_name]
```

![](/assets/images/pip_search_002.webp)

这里的结果同样是以表格的形式展示的，且相较于第一款工具 `pipq` 具有更多的功能，但由于都不是本人平时常用的功能，故不做一一介绍了。感兴趣的可以 `pipq --help` 自行查看帮助页。

![](/assets/images/pip_search_003.webp)
