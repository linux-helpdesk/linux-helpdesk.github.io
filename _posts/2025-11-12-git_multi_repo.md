---
title: Git 常用命令及多仓库管理
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 一、项目初始化与版本控制

### 1. 创建与初始化项目

```bash
mkdir test-proj
cd test-proj

# 初始化 Git 仓库
git init

# 新建文件
touch readme.md
```

### 2. 添加文件并提交版本

```bash
# 添加文件到暂存区
git add .

# 提交到版本库
git commit -m "Added readme.md"
```

### 3. 查看提交历史

```bash
git log
```

示例输出：

```bash
commit 6fbe10d285b4572d6803ec7a3b823334b5c39465 (HEAD -> master)
Author: Warren <zilong.zhao@monash.edu>
Date:   Thu Nov 13 03:39:01 2025 +0800

    Added readme.md
```

------

## 二、配置远程仓库

### 1. `git remote add` 与 `git remote set-url` 的区别

| 命令                 | 作用                                                         |
| -------------------- | ------------------------------------------------------------ |
| `git remote add`     | **首次添加**远程仓库地址（项目初始化阶段）                   |
| `git remote set-url` | 修改已存在的远程仓库地址或添加多个地址（包括 push/fetch 分离） |

------

### 2. 添加远程仓库地址

假设远程仓库地址为：

```bash
admin@localhost:/home/admin/test-remote
```

执行：

```bash
git remote add origin admin@localhost:/home/admin/test-remote
git remote get-url origin
```

输出：

```bash
admin@localhost:/home/admin/test-remote
```

`origin` 是 Git 中远程仓库的默认别名（即简写名），远程仓库名称也可以随意自定义。当执行首次添加时，这个名称还不存在。

------

### 3. 首次推送（设置上游分支）

直接执行 `git push` 会失败：

```bash
git push
# Or 
# git push origin master 
```

错误提示：

```
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master
```

按照提示执行：

```bash
git push --set-upstream origin master
```

示例输出：

```
The authenticity of host 'localhost (::1)' can't be established.
ED25519 key fingerprint is SHA256:...
...
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'localhost' (ED25519) to the list of known hosts.
admin@localhost's password:
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 214 bytes | 214.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To localhost:/home/admin/test-remote
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```

之后推送可直接使用：

```bash
git push
```

输出：

```
admin@localhost's password:
Everything up-to-date
```

------

## 三、配置多个远程仓库（多地备份）

目标：
 使 `git push` 自动向多个远程服务器推送备份。

假设第二个远程仓库地址为：

```
admin@localhost:/home/admin/test-remote-2
```

### 1. 添加第二个远程地址（push-only）

```bash
git remote set-url --add --push origin admin@localhost:/home/admin/test-remote-2
```

此时查看状态：

```bash
git remote get-url origin
```

输出：

```
admin@localhost:/home/admin/test-remote
git remote get-url origin --all
```

输出：

```
admin@localhost:/home/admin/test-remote
git remote get-url origin --push
```

输出：

```
admin@localhost:/home/admin/test-remote-2
```

> ⚠️ 说明：
>  添加新 push 地址后会覆盖原先的 push 地址，因此还需重新添加第一个仓库为 push 地址。

------

### 2. 添加第一个远程地址为第二个 push 目标

```bash
git remote set-url --add --push origin admin@localhost:/home/admin/test-remote
```

查看 `.git/config`：

```bash
cat .git/config
```

输出示例：

```
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = admin@localhost:/home/admin/test-remote
        fetch = +refs/heads/*:refs/remotes/origin/*
        pushurl = admin@localhost:/home/admin/test-remote-2
        pushurl = admin@localhost:/home/admin/test-remote
[branch "master"]
        remote = origin
        merge = refs/heads/master
```

------

### 3. 推送至多个远程仓库

```bash
git push
```

输出示例：

```
admin@localhost's password:
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 214 bytes | 214.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To localhost:/home/admin/test-remote-2
 * [new branch]      master -> master
admin@localhost's password:
Everything up-to-date
```

> 💡 注意：
>  Git 会按 `.git/config` 文件中 `pushurl` 的顺序依次推送。
>  若希望调整推送优先顺序，可手动编辑文件中两行 `pushurl` 的顺序。

------

### 4. 常用状态与历史查看命令

以下命令可帮助查看版本状态与分支结构：

#### 查看当前工作区与暂存区状态

```bash
git status
```

#### 从暂存区恢复文件（取消已暂存的更改）

```bash
git restore --staged <file>
```

#### 查看所有分支的树形提交历史（包含引用日志）

```bash
git log --graph --oneline --reflog
```

该命令以图形方式展示所有分支的提交树结构，包含 `HEAD` 的移动记录，非常适合排查历史分支变动。

------

## 四、创建远程仓库（SSH）

与普通客户端项目初始化不同，**远程仓库**初始化时需加上 `--bare` 参数：

```bash
mkdir test-remote && cd test-remote
git init --bare
```

查看结构：

```bash
ls
```

输出：

```
HEAD  config  description  hooks  info  objects  refs
```

查看路径：

```bash
pwd
```

输出：

```
/home/admin/test-remote
```

因此远程仓库地址为：

```
admin@localhost:/home/admin/test-remote
```

------

✅ **总结**

| 操作               | 命令                                           | 说明                         |
| ------------------ | ---------------------------------------------- | ---------------------------- |
| 初始化项目         | `git init`                                     | 创建本地仓库                 |
| 提交更改           | `git add . && git commit -m "msg"`             | 保存修改                     |
| 添加远程仓库       | `git remote add origin <url>`                  | 绑定远程仓库                 |
| 修改远程地址       | `git remote set-url origin <url>`              | 更换远程仓库                 |
| 添加多个 push 地址 | `git remote set-url --add --push origin <url>` | 配置多地备份                 |
| 查看远程地址       | `git remote get-url origin --all`              | 查看所有 URL                 |
| 推送初始分支       | `git push --set-upstream origin master`        | 建立 tracking 分支           |
| 后续推送           | `git push`                                     | 自动同步所有配置的 push 目标 |
| 查看状态           | `git status`                                   | 显示暂存与修改状态           |
| 取消暂存           | `git restore --staged <file>`                  | 从暂存区移除文件             |
| 查看提交树         | `git log --graph --oneline --reflog`           | 图形方式展示所有分支历史     |

------


