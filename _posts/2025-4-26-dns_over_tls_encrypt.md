---
title: 使用加密 DNS 解析
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

##### **使用加密 DNS（DoH/DoT）**

- **通过 `systemd-resolved` 配置 DoT**：

```bash
sudo nano /etc/systemd/resolved.conf
```

修改为：

```ini
[Resolve]
DNS=8.8.8.8 1.1.1.1   # 指定自定义 DNS
DNSOverTLS=yes        # 启用 DNS-over-TLS
```

重启服务：

```bash
sudo systemctl restart systemd-resolved
```

**验证加密 DNS**：

```bash
resolvectl query google.com
```

观察结果是否正常，且流量通过 TLS 加密（端口 853）。
