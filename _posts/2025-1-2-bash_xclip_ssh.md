---
title: 在 bash 文件中操作剪切板（将 ssh 登录密码自动发送到剪切板） 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

终端中：

```bash
echo xxxxx | xclip -i
或
echo xxxxx | xclip -selection clipboard
```

bash 文件中：

```bash
echo xxxxx | xclip -selection clipboard
```

> echo 不换行输出：`echo -n xxxx`
