---
title: ls 中文显示乱码 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

如果终端出现以下情况，ls 显示中文乱码，而 du 和 find 显示中文正常：

```bash
user@host:~$ mkdir tmp
user@host:~$ cd tmp
user@host:~/tmp$ touch 测试
user@host:~/tmp$ ls 
''$'\346\265\213\350\257\225'
user@host:~/tmp$ du -ha -d 1 .
0       ./测试4.0K    .
user@host:~/tmp$ zsh -c "ls"
''$'\346\265\213\350\257\225'
user@host:~/tmp$ zsh -c "du -ha -d 1 ."
0       ./测试4.0K    .
user@host:~/tmp$ export LC_CTYPE="zh_CN.UTF-8"
user@host:~/tmp$ export LANG="zh_CN.UTF-8"
user@host:~/tmp$ ls 
''$'\346\265\213\350\257\225'
user@host:~/tmp$ du -ha -d 1 .
0       ./测试4.0K    .
```

最简单方便的解决办法：

```bash
user@host:~/tmp$ ls |cat
测试
user@host:~/tmp$ ls -lh | cat
total 0
-rw-r--r-- 1 warren warren 0 Dec 14 00:51 测试
```
