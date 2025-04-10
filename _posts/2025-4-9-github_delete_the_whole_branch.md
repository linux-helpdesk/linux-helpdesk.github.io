---
title: GitHub 删除整条分枝
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

首先新建新的分枝：

```bash
git checkout --orphan new-root
# Here new-root will be the name of the new branch
```

现在环境将自动切换到新的分枝，下面删除原分枝：

```bash
git add . && git commit -m "first submit" # 这一步可选
git branch -D main # 删除 main 分枝 
git branch -m main # 将当前分枝切换为 main 分枝 
```
