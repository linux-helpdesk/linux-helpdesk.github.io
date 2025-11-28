---
title: Python 调试技巧：在循环中暂停并进入 IPython 交互环境
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

# ✅ **方法 1：使用 `IPython.embed()`（最推荐）**

在循环中插入：

```
from IPython import embed

for i in range(10):
    x = i * 2
    embed()   # 程序会在这一行自动进入 IPython
```

运行后，每次循环到 `embed()` 时会自动进入 IPython，可以查看所有当前作用域变量：

```
In [1]: i
In [2]: x
```

输入 `exit` 或 `Ctrl-D` 可以继续执行后续循环。

⚠️ 注意
 如果你不想每次循环都进入，加入条件即可：

```
if i == 5:
    embed()
```

或者如果已经调试完成不想再进行后续的进入，可以设置一个控制变量：

```Python
from IPython import embed

loop = True
for i in range(5):
    if loop:
        embed(header="Exit Test")
```

当想结束调试让程序自动进行后续循环时，只需要在调试环境内赋值 `False` 给 `loop` 变量然后退出即可。

------

# ✅ **方法 2：使用 `IPython.core.debugger.set_trace()` 像 pdb 一样断点**

类似 pdb，但自动进入 IPython：

```
from IPython.core.debugger import set_trace

for i in range(10):
    x = i + 1
    if i == 3:
        set_trace()   # 自动进入 IPython 的调试环境
```

`set_trace()` 会让你进入增强版 pdb，可以查看变量、执行语句、继续运行等。

------

# ✅ **方法 3：用 `breakpoint()` + IPython breakpointhook（更现代）**

如果你希望直接使用 Python 内置的 `breakpoint()`：

先设置环境变量：

```
export PYTHONBREAKPOINT=IPython.core.debugger.set_trace
```

然后在代码里写：

```
for i in range(10):
    x = i + 1
    breakpoint()
```

运行到 `breakpoint()` 就会自动进入 IPython 风格的调试环境。

------

# 📌 推荐总结

| 方法                          | IPython 交互？ | 适用场景                               |
| ----------------------------- | -------------- | -------------------------------------- |
| `IPython.embed()`             | ⭐⭐⭐⭐⭐          | 最强大，直接在当前作用域启动交互 shell |
| `set_trace()`                 | ⭐⭐⭐⭐           | 类似 pdb，但增强版                     |
| `breakpoint()` + ipython hook | ⭐⭐⭐            | 想用 Python 官方推荐方式               |
