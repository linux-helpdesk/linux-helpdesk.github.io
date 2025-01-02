---
title: Git 基础 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

### 一. Git 安装

**1. Windows:**

点击[下载页面]([Git - Downloading Package](http://link.zhihu.com/?target=https%3A//git-scm.com/download/win))根据自己电脑版本选择 32 位或 64 位，下载后双击安装即可。

**2. MacOS:**

在 Mac 上安装 Git 有多种方式。 最简单的方法是安装 Xcode Command Line Tools。 Mavericks （10.9） 或更高版本的系统中，在 Terminal 里尝试首次运行 *git* 命令即可。

```text
git --version
```

如果没有安装过命令行开发者工具，将会提示你安装。

如果你想安装更新的版本，可以使用二进制安装程序。 官方维护的 macOS Git 安装程序可以在 Git 官方网站下载，网址为 [https://git-scm.com/download/mac](http://link.zhihu.com/?target=https%3A//git-scm.com/download/mac)。

**3. Linux:**

打开命令行输入以下指令（以 Debian 系为例）：

```bash
sudo apt install git
```



**二. 本地版本管理**

导航至项目文件夹下，并新建用于测试的项目文件，此处以 `Project` 文件夹举例：

```bash
$ pwd                  # 显示当前路径
/home/warren/Project

$ echo "print('Hello World\!')" > helloworld.py
$ ls -a                # Git 初始化之前只有一个 helloworld.py 文件
.  ..  helloworld.py 
```

Git 初始化：

```bash
$ git init
Initialized empty Git repository in /home/warren/Project/.git/

$ ls -a                # 项目初始化后可以看到多出了一个 .git 隐藏文件夹
.  ..  .git  helloworld.py  
```

Git 在对项目存档前需要使用 `add` 将待存档文件加入缓冲区，这里我们将该目录下所有文件加入缓冲区：

```bash
$ git add .
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   helloworld.py
```

加入缓冲区后我们可以使用 `git status` 命令查看当前缓冲区状态，可以看到当前有一个文件被标记为 `stage` 状态。使用 `commit` 命令完成最终存档，`-m` 参数可以加入注释方便后期回滚辨认：

```bash
$ git commit -m "First submit"
[master (root-commit) a54c5bd] First submit
 1 file changed, 1 insertion(+)
 create mode 100644 helloworld.py
```

提交过后可以通过 `log` 和 `branch` 命令查看提交记录以及项目分支状态：

```bash
$ git log
commit a54c5bd30d7a794ce6aef4ba38517c6dbb0e8fb2 (HEAD -> master)
Author: Warren-Zhao-Zilong <nobody010101010101010101@gmail.com>
Date:   Sat Apr 23 23:39:36 2022 +0800

    First submit

$ git branch 
* master

$ git branch -av
* master a54c5bd First submit
```

**三. 远程仓库与本地仓库同步**

1. 若远程仓库不是新建仓库，可以先使用 `pull` 命令将远程仓库内容拉取至本地：

\2. 若远程仓库为新建仓库：

首先新建仓库（仓库平台为 Gitee）

![](/assets/images/git_creat_repo.webp)
新建后会显示入门教程

![](/assets/images/git_startup_tutorial.webp)

由于之前我们的项目已新建完毕并完成了本地仓库相关操作，这里我们可以直接从 `git remote` 命令开始：

```bash
$ git remote add origin https://username:password@gitee.com/warreningitee/project.git
```

但这里有一点不同请注意，与新手教程命令中的链接不同，这里加入了 `username:password@`，否则在后续每次上传时需要手动输入账号密码 。

现在，我们可以上传本地项目至远程仓库了：

```bash
$ git push -u origin master
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 252 bytes | 252.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
remote: Powered by GITEE.COM [GNK-6.3]
To https://gitee.com/warreningitee/project.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

当然你也可以选择通过令牌实现免密上传（Github 现已不支持账号密码模式，必须通过令牌方式实现免密上传），具体配置方法：

登录 Github 后依次点击 `头像` --> `Settings`--> `Developer settings` --> `Personal access tokens` 新建 `token`，并勾选赋予该 `token` 的权限。

接下来在后续的上传过程中即可通过带入 `token` 实现免密上传：

```bash
$ git remote add origin https://token@gitee.com/warreningitee/project.git
...
$ git push
```
