---
title: OpenWrt 低闪存机器：自动挂载内存 SSH 隧道方案
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

#### 阶段一：在外部 Linux 电脑上的准备工作

由于 OpenWrt 空间有限且工具链不全，必须先在另一台 Linux 机器（或 WSL、虚拟机）上生成密钥并获取指纹。

**1. 生成 ED25519 密钥对**

```bash
# 生成密钥，提示输入路径时建议直接回车，或者记下保存位置
ssh-keygen -t ed25519 -f ./id_ed25519 -N ""

```

**2. 将公钥上传至服务器**

```bash
# 将生成的 id_ed25519.pub 内容复制，并追加到服务器的授权文件中
ssh-copy-id -i ./id_ed25519.pub -p [服务器SSH端口] [用户名]@[服务器IP]

```

**3. 获取服务器指纹**

```bash
# 获取并记录输出结果，稍后需填入路由器
ssh-keyscan -t ed25519 -p [服务器SSH端口] [服务器IP]

```

---

#### 阶段二：在路由器上的基础配置

通过 `scp` 或手动粘贴方式，将密钥和指纹固化到路由器的 Flash 永久存储中。

```bash
# 1. 创建目录
mkdir -p /root/.ssh
chmod 700 /root/.ssh

# 2. 存放私钥 (将外部电脑生成的 id_ed25519 内容粘贴进去)
vi /root/.ssh/id_ed25519
chmod 600 /root/.ssh/id_ed25519

# 3. 存放指纹 (将 ssh-keyscan 的结果粘贴进去)
vi /root/.ssh/known_hosts

```

---

#### 阶段三：核心脚本 `/root/load_ssh.sh`

该脚本实现了：开机联网 -> 内存安装依赖 -> 软链接修复 -> 建立隧道。

```bash
#!/bin/sh

# --- 配置区 ---
SERVER_IP="服务器IP"
SERVER_USER="用户名"
REMOTE_PORT="22222"
# --------------

export RAM_PATH="/tmp"
export LD_LIBRARY_PATH="$RAM_PATH/usr/lib:$RAM_PATH/lib:/lib:/usr/lib"
export PATH="$RAM_PATH/usr/bin:$RAM_PATH/usr/sbin:$PATH"
export AUTOSSH_PATH="$RAM_PATH/usr/bin/openssh-ssh"
export AUTOSSH_GATETIME=30

# 等待网络就绪
while ! ping -c 1 -W 2 $SERVER_IP > /dev/null; do
    sleep 5
done
ntpd -q -p ntp.aliyun.com

# 内存动态安装
if [ ! -f "$AUTOSSH_PATH" ]; then
    opkg update
    opkg remove autossh openssh-client --force-removal
    opkg -d ram install openssh-client autossh
fi

# 修复 OpenWrt 默认指向错误路径的软链接（改为绝对路径指向 /tmp）
if [ -L "$RAM_PATH/usr/bin/ssh" ]; then
    rm "$RAM_PATH/usr/bin/ssh"
    ln -s "$RAM_PATH/usr/bin/openssh-ssh" "$RAM_PATH/usr/bin/ssh"
fi

# 启动 autossh (不带 -f，由 procd 守护进程管理)
"$RAM_PATH/usr/sbin/autossh" -M 0 -N \
    -i /root/.ssh/id_ed25519 \
    -o "UserKnownHostsFile=/root/.ssh/known_hosts" \
    -o "StrictHostKeyChecking=yes" \
    -o "ServerAliveInterval=30" \
    -o "ServerAliveCountMax=3" \
    -o "ExitOnForwardFailure=yes" \
    -R ${REMOTE_PORT}:localhost:22 \
    ${SERVER_USER}@${SERVER_IP}

```

*执行：* `chmod +x /root/load_ssh.sh`

---

#### 阶段四：Procd 守护进程配置

创建 `/etc/init.d/ssh_jump` 确保服务在后台稳定运行并具备崩溃自启功能。

```bash
#!/bin/sh /etc/rc.common

START=99
USE_PROCD=1

start_service() {
    procd_open_instance
    procd_set_param command /bin/sh /root/load_ssh.sh
    procd_set_param respawn 3600 10 0
    procd_set_param stdout 1
    procd_set_param stderr 1
    procd_close_instance
}

stop_service() {
    killall autossh openssh-ssh 2>/dev/null
}

```

---

#### 阶段五：激活与运维

**1. 开启服务**

```bash
/etc/init.d/ssh_jump enable
/etc/init.d/ssh_jump start

```

**2. 在服务器端反向连接路由器**

```bash
# 从服务器连接路由器（通过隧道）
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa -p 22222 root@localhost

# 在局域网直接连接路由器
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa root@192.168.1.1

```

**3. 查看实时日志**

```bash
# 如果连接不上，通过此命令查看安装或连接报错
logread -f

```

---

### ⚠️ 安全与维护提醒

* **防火墙**：如果服务器上无法连接，请确认服务器已在安全组/防火墙放行了该端口。
* **内存监测**：由于 720N 只有 32MB 内存，建议定期运行 `free -m`。若内存极度紧张，可考虑手动解压 `.ipk` 提取二进制文件到 `/root`，省去 `opkg update` 的内存开销。

Would you like me to help you create a version that uses pre-downloaded `.ipk` files to make the boot process even faster and offline-ready?
