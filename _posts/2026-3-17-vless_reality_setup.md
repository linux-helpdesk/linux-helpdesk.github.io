---
title: 🚀 深度指南：搭建最稳健的 Xray VLESS + Reality 代理服务器
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在当前的网络环境下，**Reality** 协议凭借其“借用”主流网站（如 Apple, Microsoft）TLS 证书的特性，实现了极高的隐蔽性。它无需购买域名，且有效规避了传统 TLS 代理指纹特征。

本教程将手把手教你如何手动配置一套高性能、高隐蔽性的代理系统。

------

### 一、 核心优势

- **无需域名**：直接使用服务器 IP，省去域名备案和证书申请的麻烦。
- **消除指纹**：利用目标网站的真实证书，完美伪装成正常的 HTTPS 请求。
- **高性能**：配合 `xtls-rprx-vision` 流控，极大地降低了延迟。

------

### 二、 环境准备

- **服务器**：一台干净的 Ubuntu/Debian 系统的 VPS。

- **基础操作**：更新系统并重启。

  ```bash
  sudo apt update && sudo apt upgrade -y
  sudo reboot
  ```

------

### 三、 安装与生成关键参数

#### 1. 安装 Xray 核心

执行官方安装脚本：

```bash
bash <(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh) install
```

#### 2. 生成 Reality 密钥对

Reality 依赖于 **x25519** 算法生成的密钥对。

```bash
/usr/local/bin/xray x25519
```

**输出示例：**

- `PrivateKey`: `0BIphNQCXk...` (**用于服务端配置，严禁外泄**)
- `Password`: `cGGPtCrpqO...` (**即公钥，用于客户端配置**)

#### 3. 生成用户 UUID

```bash
cat /proc/sys/kernel/random/uuid
```

记下这个生成的字符串，它是你连接服务器的唯一凭证。

------

### 四、 服务端配置详解

编辑配置文件：`sudo nano /usr/local/etc/xray/config.json`

将以下内容填入，请务必替换 `UUID` 和 `PrivateKey`：

```json
{
  "log": { "loglevel": "warning" },
  "inbounds": [
    {
      "port": 443,
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "id": "你的_UUID",
            "flow": "xtls-rprx-vision"
          }
        ],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "dest": "www.apple.com:443", // 伪装目标地址
          "serverNames": ["www.apple.com"],
          "privateKey": "你的_PrivateKey", // 填入刚才生成的私钥
          "shortIds": [""]
        }
      }
    }
  ],
  "outbounds": [
    { "protocol": "freedom", "tag": "direct" },
    { "protocol": "blackhole", "tag": "block" }
  ],
  "routing": {
    "rules": [
      { "type": "field", "ip": ["geoip:private", "geoip:cn"], "outboundTag": "block" }
    ]
  }
}
```

------

### 五、 启动与维护

1. **检查配置语法**：

   `xray run -test -config /usr/local/etc/xray/config.json`

2. **启动服务**：

   Bash

   ```
   sudo systemctl enable xray
   sudo systemctl restart xray
   ```

3. **开放防火墙**：

   确保服务器控制台和系统内部防火墙（如 UFW）已放行 **443** 端口。

------

### 六、 客户端配置要点

无论你使用哪个平台（V2RayN, Shadowrocket, Stash），请确保以下关键点一致：

- **协议 (Protocol)**: `VLESS`
- **地址 (Address)**: `你的服务器IP`
- **端口 (Port)**: `443`
- **UUID**: `你生成的UUID`
- **流控 (Flow)**: `xtls-rprx-vision`
- **传输层安全 (TLS)**: `Reality`
- **SNI / ServerName**: `www.apple.com`
- **PublicKey**: `你生成的公钥(Password)`
- **指纹 (Fingerprint)**: `chrome` 或 `safari`

------

### 七、 客户端配置文件详解 (JSON)

如果你使用的是支持 Xray 核心的 PC 客户端（如 v2rayN 的自定义配置或 Linux 客户端），其 `config.json` 的 `outbounds` 部分应如下配置。

**请特别注意：客户端填写的 `publicKey` 是服务端生成时显示的 `Password` 字段。**

```json
{
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "vless",
      "settings": {
        "vnext": [
          {
            "address": "你的服务器_IP", // 替换为真实 IP
            "port": 443,
            "users": [
              {
                "id": "你的_UUID",      // 必须与服务端一致
                "flow": "xtls-rprx-vision",
                "encryption": "none"
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "serverName": "www.apple.com", // 必须在服务端的 serverNames 列表中
          "publicKey": "你的_公钥",       // 对应生成时的 Password 字段
          "shortId": "",                 // 需与服务端一致（若服务端为空则此处也为空）
          "spiderX": "/"
        },
        "tcpSettings": {
          "header": {
            "type": "none"
          }
        }
      }
    },
    {
      "tag": "direct",
      "protocol": "freedom"
    }
  ],
  "routing": {
    "domainStrategy": "AsIs",
    "rules": [
      { "type": "field", "ip": ["geoip:cn", "geoip:private"], "outboundTag": "direct" },
      { "type": "field", "domain": ["geosite:cn"], "outboundTag": "direct" }
    ]
  }
}
```

------

### 八、 参数对照表（避坑指南）

很多新手在手动配置时容易填错位置，请参照下表核对：

| **功能模块** | **参数名称**         | **来源 / 备注**                                    |
| ------------ | -------------------- | -------------------------------------------------- |
| **基础连接** | 地址 (Address)       | 你的服务器公网 IP                                  |
| **基础连接** | 端口 (Port)          | 服务端 `inbound` 监听的端口 (默认 443)             |
| **用户识别** | UUID                 | 服务端 `clients` 中的 `id`                         |
| **传输协议** | 流控 (Flow)          | 必须填 `xtls-rprx-vision` 才能发挥最佳性能         |
| **安全传输** | 安全 (Security)      | 选择 `REALITY`                                     |
| **REALITY**  | SNI (ServerName)     | 伪装域名，如 `www.apple.com`                       |
| **REALITY**  | **公钥 (PublicKey)** | **重要：** 填写 `x25519` 生成结果中的 **Password** |
| **REALITY**  | Fingerprint          | 建议选 `chrome` (模拟浏览器指纹)                   |

------

### 九、 常见问题排查 (FAQ)

1. **连接超时 (Timeout)**：检查服务器防火墙是否放行了 443 端口（`sudo ufw status`）。
2. **非法指令 (Illegal Instruction)**：如果你的 VPS CPU 太老，可能不支持某些指令集，尝试更新 Xray 到最新版。
3. **密钥不匹配**：请反复确认，服务端填的是 `PrivateKey`，客户端填的是 `Password` (即公钥)。

------


