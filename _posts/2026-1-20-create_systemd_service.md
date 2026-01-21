---
title: Systemd 服务创建教程
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

创建一个 systemd `service` 其实就像是在写一份“员工入职登记表”。你告诉系统：这个程序是谁、怎么运行、什么时候该重启。

一个完整的 `.service` 文件通常存放在 `/etc/systemd/system/` 目录下，主要由三个部分（Section）组成：`[Unit]`、`[Service]` 和 `[Install]`。

---

### 1. [Unit]：服务的元数据

这部分不涉及具体的启动命令，而是描述服务本身以及它与其他服务、Target 之间的关系。

* **Description**: 服务的简短描述（会在 `systemctl status` 中显示）。
* **After**: 规定**启动顺序**。比如 `After=network.target` 表示等网络启动后再启动此服务。
* **Requires / Wants**: 规定**依赖关系**。`Requires` 是强依赖（如果依赖项挂了，我也挂）；`Wants` 是弱依赖（最好有，没有我也能启动）。

### 2. [Service]：核心运行配置

这是最关键的部分，定义了程序具体怎么跑。

* **Type**: 告诉 systemd 如何判断服务已经启动成功。
* `simple`（默认）：程序一运行，systemd 就认为启动成功。
* `forking`：程序启动后会派生子进程，主进程退出（常见于传统后台守护进程）。
* `oneshot`：执行一次就结束，后面不常驻内存（适合备份、清理任务）。


* **ExecStart**: **启动命令**。必须使用**绝对路径**（例如 `/usr/bin/python3` 而不是 `python3`）。
* **User / Group**: 以哪个用户运行。为了安全，尽量不要用 `root`。
* **Restart**: 失败后是否自动重启。常用 `on-failure`（仅在非正常退出时重启）。
* **WorkingDirectory**: 程序运行时的当前目录。

### 3. [Install]：安装配置

定义如何“激活”这个服务。

* **WantedBy**: 指定该服务属于哪个 `target`。最常见的是 `multi-user.target`。

---

### 4. 动手写一个：极简的 Python Web 服务

假设你有一个 Python 脚本 `/home/pi/web_server.py`。

**第一步：编写配置文件**
在 `/etc/systemd/system/myweb.service` 写入：

```ini
[Unit]
Description=My Python Web Server
After=network.target

[Service]
# 指定运行用户
User=www-data
# 指定工作目录，脚本里的相对路径会以此为准
WorkingDirectory=/home/pi
# 启动命令（必须是绝对路径）
ExecStart=/usr/bin/python3 /home/pi/web_server.py
# 如果程序崩溃，5秒后自动重启
Restart=on-failure
RestartSec=5s

[Install]
# 绑定到多用户模式
WantedBy=multi-user.target

```

**第二步：让配置生效**

```bash
# 1. 告诉 systemd 配置文件有变动，请重新扫描
systemctl daemon-reload

# 2. 启动服务
systemctl start myweb

# 3. 设置开机自动启动（就是在 target 的 .wants 目录下建软链接）
systemctl enable myweb

# 4. 查看运行状态
systemctl status myweb

```

---

### 5. 服务的“生命周期”图

### 进阶技巧：环境变量与保护

如果你不希望把数据库密码写在脚本里，可以在 `[Service]` 里使用：

* `Environment="DB_PASSWORD=secret123"`
* 或者指向一个文件：`EnvironmentFile=/etc/default/myweb`

**你想了解如何通过 `journalctl` 命令来精准地给你的新 Service 排查错误（看日志）吗？**
