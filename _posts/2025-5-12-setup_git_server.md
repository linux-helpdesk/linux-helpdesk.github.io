---
title: Git 服务器搭建
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

On Server:

```bash
$ sudo useradd -m git -s /bin/bash
$ passwd git
```

On Client:

```bash
$ ssh-keygen -t rsa -b 4096
$ ssh-copy-id git@[gitserver]
```

On Server:

```bash
$ su git
$ mkdir /home/git/project # Choose whatever path you like
$ cd /home/git/project
$ git init --bare
```

On Client:

```bash
$ cd myproject
$ git init
$ git add .
$ git commit -m 'initial commit'
$ git remote add origin git@gitserver:/home/git/project.git
$ git push origin master
```

If you wanna multiple developers, run the same `ssh-keygen` and `ssh-copy-id` as well, and then clone the project:

```bash
$ ssh-keygen -t rsa -b 4096
$ ssh-copy-id git@[gitserver]
$ git clone git@gitserver:/home/git/project.git
$ cd project
$ vim README
$ git commit -am 'fix for the README file'
$ git push origin master
```

To limit the operation of the git

```bash
chsh git -s $(which git-shell)
```
