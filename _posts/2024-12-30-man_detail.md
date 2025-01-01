---
title:  Man 说明跳转到详情页
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

比如我们使用如下命令查看了 `cryptsetup` 的说明页：

```bash
man cryptsetup
```

中有这么一部分：

```
   RESIZE
       resize <name>

       Resizes an active mapping <name>.
       See cryptsetup-resize(8).
```

想查看这里的 `cryptsetup-resize(8)` 我们可以退出当前说明，然后输入如下命令：

```bash
man 8 cryptsetup-resize
```

