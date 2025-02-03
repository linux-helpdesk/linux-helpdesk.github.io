---
title: 设置 FRP 开机自启动
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

要让系统在启动时自动运行命令 `/home/warren/frp/frpc -c /home/warren/frp/frpc.toml`，并且确保在网络连接后启动，你需要编写一个 systemd 服务单元文件。以下是步骤和示例配置：

### 步骤：
1. 创建一个新的 systemd 服务单元文件。
2. 设置 `After=network.target` 来确保网络连接后启动。
3. 设置合适的权限和执行命令。

### 示例配置文件：`/etc/systemd/system/frpc.service`

```ini
[Unit]
Description=FRP Client (frpc)
After=network.target

[Service]
ExecStart=/home/warren/frp/frpc -c /home/warren/frp/frpc.toml
WorkingDirectory=/home/warren/frp
User=warren
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 解释：
- `[Unit]` 部分：
  - `Description`：服务的描述，通常是简单的说明。
  - `After=network.target`：确保该服务在网络连接后启动。
  
- `[Service]` 部分：
  - `ExecStart`：定义启动该服务的命令，这里就是你需要运行的 `/home/warren/frp/frpc -c /home/warren/frp/frpc.toml`。
  - `WorkingDirectory`：指定工作目录，这里是 `/home/warren/frp`。
  - `User=warren`：以 `warren` 用户身份运行该命令（你可以根据需要调整）。
  - `Restart=always`：如果该服务崩溃，systemd 会自动重启服务。
  - `RestartSec=5`：重启前等待 5 秒，防止快速重复重启。
  
- `[Install]` 部分：
  - `WantedBy=multi-user.target`：这意味着该服务将在系统达到 `multi-user` 级别时启动，通常是系统正常运行时。

### 步骤 2：启动并启用服务

1. 保存并关闭该文件。
2. 运行以下命令来重新加载 systemd 配置并启动服务：

```bash
sudo systemctl daemon-reload
sudo systemctl enable frpc.service
sudo systemctl start frpc.service
```

- `daemon-reload`：重新加载 systemd 配置文件。
- `enable`：设置服务开机自启。
- `start`：立即启动该服务。

你可以使用以下命令检查服务状态：

```bash
sudo systemctl status frpc.service
```

如果一切正常，你应该能看到 FRP 客户端程序已经启动并在网络连接后自动运行。
