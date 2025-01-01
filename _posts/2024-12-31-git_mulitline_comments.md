---
title: Git commit 多行注释 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

如果要输入多行注释，则在 `git commit` 提交时不要输入 `-m`，而直接输入：

```bash
git commit
```

这会打开一个文本编辑器（Vi 或者 Nano），输入然后保存即可。

或者使用多个 `-m` 输入多行注释：

```bash
git commit -m 'Comment 1' -m 
```

