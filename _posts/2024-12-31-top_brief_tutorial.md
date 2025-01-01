---
title: Top 命令使用方法 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

输入 `top` 命令进入界面后：

**`Space`**：立刻刷新屏幕。

**`h`**：显示帮助。

**`k`**：杀死进程。输入 `k` 后会提示输入 PID，然后输入信号（默认是 15）。

**`M`**：**按内存使用排序。**

**`P`**：**按 CPU 使用排序。**

**`N`**：按 PID 排序。

**`T`**：按运行时间排序。

<font color='red'>**`t`**：**切换显示进程和 CPU 状态行。**</font>

<font color=red>**`m`**：**切换显示内存信息。**</font>

<font color=red>**`1`**：**切换显示每个 CPU 的状态。**</font>

启动时的选项：

- **`top -d <seconds>`**：设置刷新间隔时间，例如 `top -d 2` 每2秒刷新一次。

