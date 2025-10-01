---
title: Tmux 创建会话并直接运行命令
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 最佳解决方案

```
tmux new-session -s 会话名称 -d "要执行的命令"
```

> **重要注意事项**：
>
> 如果使用 `-d`参数创建会话并运行命令：
>
> - **当命令是常驻进程**（如 `top`, `npm start`, `python app.py`）时，会话会持续存在
> - **当命令是短暂命令**（如 `ls`, `echo`, `date`）时，命令执行完毕后会话会自动销毁
>
> **解决方案**：如果希望执行后窗口不关闭，在命令末尾添加交互式 shell：
>
> ```
> tmux new-session -s 会话名称 -d "要执行的命令; exec $SHELL"
> # 或
> tmux new-session -s 会话名称 -d "要执行的命令; bash"
> ```

## 完整命令详解

### 基本语法

```
tmux new-session -s 会话名称 [选项] ["命令"]
```

### 常用选项

| 选项          | 说明                           |
| ------------- | ------------------------------ |
| `-s`          | 指定会话名称（必需）           |
| `-d`          | 在后台创建会话（不自动附加）   |
| `-c 目录路径` | 指定工作目录                   |
| `-n 窗口名称` | 指定初始窗口名称（默认为bash） |
| `-x 宽度`     | 设置窗口宽度                   |
| `-y 高度`     | 设置窗口高度                   |

### 不同场景下的命令格式

| 场景             | 命令格式                                             | 示例                                                         |
| ---------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| **常驻进程**     | `tmux new-session -s name -d "command"`              | `tmux new-session -s server -d "npm start"`                  |
| **短暂命令**     | `tmux new-session -s name -d "command; bash"`        | `tmux new-session -s logs -d "cat error.log; bash"`          |
| **多命令序列**   | `tmux new-session -s name -d "cmd1; cmd2; bash"`     | `tmux new-session -s setup -d "apt update; apt upgrade; bash"` |
| **条件执行**     | `tmux new-session -s name -d "cmd1 && cmd2 && bash"` | `tmux new-session -s build -d "make && make test && bash"`   |
| **指定工作目录** | `tmux new-session -s name -c path -d "command"`      | `tmux new-session -s project -c ~/code -d "ls -la"`          |
| **复杂命令**     | `tmux new-session -s name -d "复合命令"`             | `tmux new-session -s monitor -d "watch -n 1 'date; echo; free -h'"` |

## 完整工作流程示例

### 1. 创建并管理会话

```
# 创建后台会话运行Python脚本
tmux new-session -s data_processing -d "python3 analysis.py; bash"

# 查看会话列表
tmux list-sessions

# 附加到会话
tmux attach -t data_processing

# 从会话分离 (在会话中按 Ctrl+b d)

# 结束会话
tmux kill-session -t data_processing
```

### 2. 创建带多个窗口的会话

```
# 创建主会话
tmux new-session -s project -d "vim"

# 添加新窗口
tmux new-window -t project:1 -n "server" "npm start"
tmux new-window -t project:2 -n "tests" "npm test"
tmux new-window -t project:3 -n "logs" "tail -f debug.log; bash"

# 附加到会话
tmux attach -t project
```

## 常见问题解决

### 问题1：会话创建后立即退出

**原因**：执行的命令不是常驻进程

**解决**：在命令末尾添加 `; bash`或 `; $SHELL`

### 问题2：命令中包含特殊字符

**解决**：使用单引号或转义特殊字符

```
tmux new-session -s test -d 'echo "Hello $USER"; bash'
```

### 问题3：需要传递环境变量

**解决**：在命令前设置变量

```
tmux new-session -s env_test -d "API_KEY=12345 python app.py; bash"
```

### 问题4：命令执行需要用户输入

**解决**：使用 `expect`或创建会话后附加交互

```
tmux new-session -s interactive -d "bash -c 'some_command; bash'"
```

## 高级技巧

### 1. 创建会话并立即附加

```
tmux new-session -s 会话名称 "命令"
```

### 2. 在现有会话中创建新窗口

```
tmux new-window -t 会话名称 -n 窗口名称 "命令"
```

### 3. 发送命令到现有会话

```
tmux send-keys -t 会话名称:窗口编号 "命令" Enter
```

### 4. 创建带特定布局的会话

```
tmux new-session -s dev -d
tmux split-window -v -t dev:0 "npm run watch"
tmux split-window -h -t dev:0.1 "jest --watch"
tmux attach -t dev
```

## 总结备忘表

| 任务             | 命令                                |
| ---------------- | ----------------------------------- |
| **创建新会话**   | `tmux new-session -s name -d "cmd"` |
| **保持窗口打开** | 在命令后添加 `; bash`               |
| **附加到会话**   | `tmux attach -t name`               |
| **列出会话**     | `tmux list-sessions`                |
| **结束会话**     | `tmux kill-session -t name`         |
| **创建新窗口**   | `tmux new-window -n name "cmd"`     |
| **发送按键**     | `tmux send-keys -t target "keys"`   |

通过掌握这些命令和技巧，您可以高效地使用 tmux 管理多个会话和窗口，特别适合服务器管理、开发调试和长时间任务监控等场景。
