---
title: Linux 系统时间无法自动更新
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

> 原因：**NTP 服务未安装或未运行**

- **检查服务状态**：

  ```bash
  timedatectl status | grep "NTP service"
  ```

  若输出为 `inactive` 或显示不支持，说明系统缺少 NTP 服务。

- **安装并启用 NTP 客户端**：

  - **对于 `systemd-timesyncd`**（多数 Linux 发行版默认）：

    ```bash
    sudo apt install systemd-timesyncd  # Debian/Ubuntu
    sudo systemctl enable --now systemd-timesyncd
    sudo timedatectl set-ntp 1
    ```

  - **其他 NTP 服务（如 `chrony` 或 `ntpd`）**：

    ```bash
    sudo apt install chrony  # Debian/Ubuntu
    sudo yum install chrony # CentOS/RHEL
    sudo systemctl enable --now chronyd
    ```
