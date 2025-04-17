---
title: Mitmproxy 设置代理类型及代理认证信息
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
mitmproxy --mode socks5 --listen-host=0.0.0.0 --listen-port=8082 --proxyauth user:pwd
```

`mode` 参数支持多种代理（Socks5/HTTP/...），输入 `mitmproxy --help | less` 在 `--mode` 一栏查看详情。
