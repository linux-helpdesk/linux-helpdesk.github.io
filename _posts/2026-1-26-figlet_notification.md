---
title: TTY 中显示大号文字提示：FIGlet 使用全攻略
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在纯 TTY 模式下，默认的字符字体通常很小。如果你在机房远程操作时，想要给物理机前的同事留下醒目的提示（例如：“SYSTEM UPDATING” 或 “DO NOT TOUCH”），或者只是想让你的终端欢迎界面更酷，**FIGlet** 是你的不二之选。

---

## 1. 什么是 FIGlet？

**FIGlet** 是一款能将普通的 ASCII 字符转换成由字符组成的“大号字”的工具。它基于 ASCII Art，不需要任何图形环境支持，非常适合在 Ubuntu Server 的 TTY 终端中使用。

---

## 2. 安装方法

在 Ubuntu 中，你可以通过简单的 `apt` 命令完成安装：

```bash
sudo apt update
sudo apt install figlet

```

---

## 3. 基础使用技巧

### A. 最简单的生成

直接在命令后加上你想说的文字：

```bash
figlet "SYSTEM READY"

```

### B. 配合重定向输出到物理屏幕

结合我们上一篇笔记的技巧，你可以直接让文字显示在 TTY1 屏幕上：

```bash
figlet "DANGER - DO NOT POWER OFF" > /dev/tty1

```

### C. 调整文字对齐方式

如果你想让文字在屏幕上居中（`-c`）或靠右（`-r`）：

```bash
figlet -c -w 80 "LOGGING IN..."

```

*注：`-w 80` 是指定屏幕宽度，确保居中效果准确。*

---

## 4. 进阶：更换字体样式

FIGlet 内置了多种字体样式，通过 `-f` 参数可以切换。

* **常用字体展示：**
* `standard` (默认)
* `slant` (斜体)
* `shadow` (带阴影)
* `banner` (超大超粗)



**尝试命令：**

```bash
figlet -f slant "Hello Ubuntu"

```

### 如何查看所有可用字体？

你可以查看 `/usr/share/figlet` 目录下的 `.flf` 文件：

```bash
ls /usr/share/figlet/*.flf

```

---

## 5. 趣味联动：搭配回显颜色

虽然 FIGlet 本身不带颜色，但你可以利用 Linux 的转义字符为它“上色”，让 TTY 提示更具震撼力。例如，显示一个红色的警告：

```bash
# \e[31m 代表红色
echo -e "\e[31m$(figlet -f standard 'STOP')\e[0m"

```

---

## 6. 实战建议：制作 TTY 公告牌

结合上一篇关于 `conspy` 和 `tmux` 的内容，你可以在物理屏幕上专门挂一个 `tmux` 窗口，然后循环显示动态时间或警告：

```bash
# 简单的 TTY 时钟提示
watch -n 1 "date '+%H:%M:%S' | figlet -c"

```

通过这种方式，即使是一台落满灰尘的服务器屏幕，也能瞬间变成一个充满科技感的系统监视器。

