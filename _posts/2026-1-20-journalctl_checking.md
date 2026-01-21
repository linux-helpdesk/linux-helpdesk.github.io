---
title: Linux 日志排查教程
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

排查 `service` 报错是每个 Linux 用户的必修课。由于 `systemd` 接管了所有进程，它会把程序的 **标准输出 (stdout)** 和 **标准错误 (stderr)** 全部收集起来，统一存放在二进制日志中。

要看这些日志，唯一的工具就是 `journalctl`。

---

### 1. 基础排错三板斧

当你发现服务启动失败（红色报错）时，按顺序执行以下命令：

#### 第一步：查看实时滚动日志

这类似于 `tail -f`，适合你一边启动服务，一边观察它报什么错。

```bash
journalctl -u myweb.service -f

```

* `-u`: 指定单元（Unit）。
* `-f`: 追踪（follow）实时输出。

#### 第二步：查看本次开机以来的所有日志

如果服务半夜挂了，你想翻看之前的记录：

```bash
journalctl -u myweb.service -b
journalctl -u myweb.service -b -1 

```

* `-b`: 本次启动（boot）以来的日志。
* `0`: 代表本次启动（默认值）。
* `-1`: 代表上一次启动。
* `-2`: 代表上上一次启动，以此类推。

如果你维护服务器时间长了，可能有很多次开关机记录。你可以用这个命令列出所有历史批次：

```bash 
journalctl --list-boots

```

输出示例：

```plaintext
IDX  BOOT ID                          FIRST ENTRY                 LAST ENTRY
 -2  4f2a...  Wed 2026-01-19 10:00:01 CST  Wed 2026-01-19 22:00:00 CST
 -1  8d3b...  Thu 2026-01-20 09:00:00 CST  Thu 2026-01-20 23:00:00 CST
  0  a1b2...  Fri 2026-01-21 07:00:00 CST  Fri 2026-01-21 07:30:00 CST
```

#### 第三步：查看特定时间段

如果你知道服务是昨天下午两点挂的：

```bash
journalctl -u myweb.service --since "2026-01-20 14:00:00" --until "2026-01-20 15:00:00"

```

---

### 2. 进阶：排查“启动不起来”的玄学问题

有时候 `systemctl status` 只告诉你 `Result: exit-code`，没写原因。这时候你可以用 **“-xe”** 组合拳：

```bash
systemctl status myweb.service -l
# 或者
journalctl -xeu myweb.service

```

* `-x`: (Catalog) 提供错误的详细解释（如果系统库里有的话）。
* `-e`: (End) 直接跳到日志末尾。

---

### 3. 日志管理的“潜规则”

由于 `journalctl` 的日志默认存在内存或 `/var/log/journal`，如果不加限制，它会吃掉大量磁盘空间。

* **查看日志占了多少空间**：
`journalctl --disk-usage`
* **清理日志**（例如只保留最近 2 天的）：
`journalctl --vacuum-time=2d`
* **只保留 500MB**：
`journalctl --vacuum-size=500M`

如果你要在上一次的日志里搜某个关键词（比如 "Error"），可以配合 grep，或者直接用 journalctl 内置的搜索：

```bash 
# 方法 A：配合 grep (搜索特定关键词)
journalctl -b -1 | grep -i "error"

# 方法 B：查看上一次启动中所有优先级为 "err" 及以上的日志
journalctl -b -1 -p err

```

* `-p err` 会过滤出 Emergency, Alert, Critical, 和 Error 级别的日志，自动过滤掉普通的 Info 信息。

---

### 4. 综合演示：从创建到排错的闭环

1. **修改文件**：你改了 `/etc/systemd/system/myweb.service`。
2. **重载**：`systemctl daemon-reload`（**必须做**，否则 systemd 还在运行旧配置）。
3. **启动**：`systemctl restart myweb`。
4. **观察**：如果失败，立刻执行 `journalctl -u myweb -n 50`（查看最后 50 行）。

**一个小提醒**：在编写 `ExecStart` 脚本时，如果你的程序需要**环境变量**，记得在 `.service` 文件里用 `Environment=` 定义，或者在脚本里写绝对路径。因为 systemd 运行环境非常“干净”，它拿不到你 `.bashrc` 里的那些别名和路径。

