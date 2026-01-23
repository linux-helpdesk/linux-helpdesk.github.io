---
title: 小容量设备 OpenWrt 19.07 系统编译与刷入全指南
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

本指南包含两种方案：**Image Builder (快速固件生成)** 与 **SDK (软件包编译)**。

### 一、 编译环境准备 (Ubuntu/Debian)

无论是使用 Image Builder 还是 SDK，都需要在宿主机安装基础构建工具，并确保 Python 版本为 2.x。

```bash
# 更新并安装必要依赖
apt update
apt install build-essential libncurses5-dev libncursesw5-dev zlib1g-dev gawk git gettext libssl-dev xsltproc wget unzip python file sync

```

---

### 二、 方案 A：使用 Image Builder 快速生成精简固件

这是将系统塞进 4MB Flash 的最有效方法，通过剔除不必要的组件来极限压缩体积。

**1. 下载并解压 Image Builder**

```bash
wget https://downloads.openwrt.org/releases/19.07.9/targets/ar71xx/tiny/openwrt-imagebuilder-19.07.9-ar71xx-tiny.Linux-x86_64.tar.xz
tar xavf openwrt-imagebuilder-19.07.9-ar71xx-tiny.Linux-x86_64.tar.xz
cd openwrt-imagebuilder-19.07.9-ar71xx-tiny.Linux-x86_64

```

**2. 查找并生成镜像**

```bash
# 查找设备对应的 PROFILE 名称（TL-WR720N v4 对应 tl-wr720n-v4）
make info | less 

# 执行编译：剔除 LuCI 界面、IPv6 和 PPPoE 拨号相关包以压缩固件体积
make image PROFILE=tl-wr720n-v4 PACKAGES="-luci -luci-proto-ppp -ppp -ppp-mod-pppoe -ip6tables -odhcp6c -kmod-ipv6"

```

**3. 获取固件**
编译结果位于 `bin/targets/ar71xx/tiny/`，通常体积在 3.2MB 左右，适合 4MB 设备。

---

### 三、 方案 B：使用 SDK 编译特定软件包 (.ipk)

当系统 Flash 空间不足以内置 `autossh` 等软件时，需用 SDK 编译出安装包，以便后续动态加载到内存中。

**1. 下载并解压 SDK**

```bash
wget https://downloads.openwrt.org/releases/19.07.9/targets/ar71xx/generic/openwrt-sdk-19.07.9-ar71xx-generic_gcc-7.5.0_musl.Linux-x86_64.tar.xz
tar xavf openwrt-sdk-19.07.9-ar71xx-generic_gcc-7.5.0_musl.Linux-x86_64.tar.xz
cd openwrt-sdk-19.07.9-ar71xx-generic_gcc-7.5.0_musl.Linux-x86_64

# 更新并安装 feeds 插件
./scripts/feeds update -a
./scripts/feeds install -a

```

**2. 配置并编译**

```bash
# 进入配置界面选择需要编译的包（如 Network -> SSH -> autossh），设为 <M>
make menuconfig 

# 执行编译命令 (核心步骤)
# V=s 显示详细日志，-j 指定使用的 CPU 核心数
make package/network/services/autossh/compile V=s -j$(nproc)

```

**3. 导出安装包**
编译出的 `.ipk` 文件位于 `bin/packages/` 下的子目录中。

---

### 四、 系统安装与刷机

**1. 上传固件**
务必将固件上传至路由器的 **/tmp** 路径，以防存储溢出。

**2. 升级系统**

```bash
# -n: 不保留配置（跨版本必须执行此项）
# -v: 详细模式
sysupgrade -n -v /tmp/openwrt-19.07.9-ar71xx-tiny-tl-wr720n-v4-squashfs-sysupgrade.bin

```

**3. 强制刷写 (MTD 方式)**
若 `sysupgrade` 因校验失败无法使用，可采用底层 MTD 命令（危险操作，确认分区名无误后再执行）：

```bash
# 查看分区名，TL-WR720N 通常是 "firmware"
cat /proc/mtd

# 强制刷写并自动重启 (-r)
mtd -r write /tmp/upgrade.bin firmware

```

---

### 五、 登录兼容性说明

由于 19.07 版本系统的 Dropbear 算法较旧，现代电脑连接时必须手动指定加密算法：

```bash
# 连接路由器或反向隧道时的兼容命令
ssh -o HostKeyAlgorithms=+ssh-rsa -o PubkeyAcceptedAlgorithms=+ssh-rsa root@192.168.1.1

```

后续可配合此前编写的 `load_ssh.sh` 脚本，将 SDK 编译出的插件在开机时自动加载到 RAM 运行。
