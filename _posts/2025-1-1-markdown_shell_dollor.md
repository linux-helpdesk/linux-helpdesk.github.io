---
title: Markdown Shell 命令代码块美元符号意义 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

*不要* 在 shell 代码前加 `$` 符号，除非你想要展示命令的输出。

如果目的是表明确切的语言，那么直接在代码前标明。

解释: 复制粘贴比较困难，不利于阅读。

建议使用:

```bash
echo a
echo a > file
```

不建议：

```bash
$ echo a
$ echo a > file
```

建议, 展示输出:

```bash
$ echo a
a
$ echo a > file
```

建议, 在代码前标明代码语言:

```bash
Use the following Bash code:

echo a
echo a > file
```


