---
title: 如何让 zsh 的终端补全大小写敏感 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在 `.zshrc` 结尾加上如下内容：

```text
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' '+m:{A-Z}={a-z}'
```

重新载入 `.zshrc`：

```bash
$ source ~/.zshrc
```

