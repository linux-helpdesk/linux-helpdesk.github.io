---
title: 小内存设备如何安装 OpenWRT (4 M 以下内存） 手动编译加安装扩容教程（无需硬改，小内存设备，挂载 U 盘，USB 启动） 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## ——TL-WR720N V4 手动编译加安装 Openwrt 教程（无需硬改）

对于许多小内存设备，尤其是 4 M 及以下容量的设备，我们在 Openwrt 刷机时经常能看到官方给出的以下提示：

![4 M 及以下警告](assets/images/openwrt_below_4m_warning.jpg)

上文大意是不建议在闪存容量为 4 M 及以下的设备中刷入 `Openwrt`，这是因为由于极小的容量会导致刷入系统本体加 `luci` 可视化控制台后系统容量所剩无几，无法再安装其他软件，与普通路由相差无几，发挥不出 `Openwrt` 系统的特点与优势。（有时甚至会导致直接无法刷入标准系统）

所以，今天给大家分享一下，如何在编译阶段去掉 `luci` 可视化控制台以及其他不必要功能，编译定制自己的个性化刷机包，腾出空间安装挂载 USB 设备所需的软件，最后在挂载并成功扩容闪存后再将 `luci` 安装至设备中。

（教程制作不易，如果成功的帮到了您，还请您动动您发财的小手，给 UP 主点个赞，谢谢了！）

首先保证环境与本教程一致，选用 CentOS 7，下载 [DVD 版镜像](http://link.zhihu.com/?target=https%3A//mirrors.tuna.tsinghua.edu.cn/centos/7.9.2009/isos/x86_64/CentOS-7-x86_64-DVD-2009.iso) 并在 VMWare 中完成安装。

进入并更新系统，然后下载编译所需文件：[imagebuilder-for-tl-wr720n-v4](http://link.zhihu.com/?target=https%3A//downloads.openwrt.org/releases/17.01.5/targets/ar71xx/generic/lede-imagebuilder-17.01.5-ar71xx-generic.Linux-x86_64.tar.xz)

（以下有部分借鉴该[链接](http://link.zhihu.com/?target=https%3A//blog.csdn.net/c5113620/article/details/84368644)）

```bash
# 解压
$ tar -xvJf lede-imagebuilder-17.01.5-ar71xx-generic.Linux-x86_64.tar.xz
# 进入项目目录
$ cd lede-imagebuilder-17.01.5-ar71xx-generic.Linux-x86_64
# 查看所有PROFILE参数，包括packages
$ make info
# 看profile
$ make info |grep 720  
tl-wr720n-v3:
    TP-LINK TL-WR720N v3
tl-wr720n-v4:
    TP-LINK TL-WR720N v4
# 由于make image会下载需要的交叉编译环境，可以设置终端代理（根据自己的情况填入 host 和 port）
$ export http_proxy=http://[host]:[port]
$ export https_proxy=http://[host]:[port]
# 使用以下命令编译
$ make image PROFILE="tl-wr720n-v4" PACKAGES="kmod-usb-storage kmod-fs-ext4 e2fsprogs block-mount -firewall -ip6tables -iptables -kmod-ipt-nathelper -odhcp6c"
```

在编译过程中，大概率会报错，如果报错，根据以下对照安装相应的包解决：

（以下有部分借鉴该[链接](http://link.zhihu.com/?target=https%3A//imdouba.com/archives/openwrt-centos7-%E7%BC%96%E8%AF%91%E7%8E%AF%E5%A2%83%E6%90%AD%E5%BB%BA.html)）

```bash
Build dependency: Please install the GNU C Compiler (gcc)
yum -y install gcc

Build dependency: Please reinstall the GNU C Compiler - it appears to be broken
Build dependency: Please install the GNU C++ Compiler (g++)
Build dependency: Please reinstall the GNU C++ Compiler - it appears to be broken
yum -y install gcc-c++

Build dependency: Please install ncurses. (Missing libncurses.so or ncurses.h)
yum -y install ncurses-devel

Build dependency: Please install a static zlib. (Missing libz.a or zlib.h)
yum -y install zlib-static

Build dependency: Please install the openssl library (with development headers)
yum -y install openssl-devel

Build dependency: Please install the Perl Thread::Queue module
yum -y install perl-Thread-Queue

Build dependency: Please install GNU 'patch'
yum -y install patch

Build dependency: Please install 'unzip'
yum -y install unzip

Build dependency: Please install 'bzip2'
yum -y install bzip2

Build dependency: Please install GNU 'wget'
yum -y install wget

Build dependency: Please install the Subversion client
yum -y install svn
```

编译完成后会在 `./bin/targets/ar71xx/generic/` 路径下获得几个编译后的文件，其中：

> 刷新固件：`lede-17.01.5-ar71xx-generic-tl-wr720n-v4-squashfs-factory.bin`
> 升级已有的 Openwrt 固件：`lede-17.01.5-ar71xx-generic-tl-wr720n-v4-squashfs-sysupgrade.bin`

根据自己情况上传刷机包刷机。

刷机成功后我们会获得一个无 Web 管理界面（`Luci`）但能挂载 U 盘的 `Openwrt` 路由器，以下操作均通过终端命令行 `ssh` 远程链接操作。

首先，将路由器调至 3G 模式并开机，插入优盘至 USB 口。

使用网线链接 `Openwrt` 路由器 `Lan` 口至电脑，`ssh` 远程登录 `192.168.1.1`，用户名为 `root`：

```bash
ssh root@192.168.1.1
```

成功登录后使用 `vi` 编辑 `/etc/config/fstab` 文件，删除 `config global` 以外所有其他项目。（`vi` 编辑器具体使用方法请自行百度，这里就不啰嗦了）

```bash
vi /etc/config/fstab
```

![Vi 编辑器](https://picx.zhimg.com/80/v2-b9bdebe03c6f7052deccee8a01a0740b_1440w.webp?source=d16d100b)

保存退出后，逐行输入以下代码（一路无脑复制粘贴就好）：

```bash
cd
DEVICE="$(sed -n -e "/\s\/overlay\s.*$/s///p" /etc/mtab)"
uci -q delete fstab.rwm
uci set fstab.rwm="mount"
uci set fstab.rwm.device="${DEVICE}"
uci set fstab.rwm.target="/rwm"
uci commit fstab
DEVICE="/dev/sda1"
mkfs.ext4 ${DEVICE}
eval $(block info ${DEVICE} | grep -o -e "UUID=\S*")
uci -q delete fstab.overlay
uci set fstab.overlay="mount"
uci set fstab.overlay.uuid="${UUID}"
uci set fstab.overlay.target="/overlay"
uci commit fstab
mkdir -p /tmp/cproot
mount --bind /overlay /tmp/cproot
mount ${DEVICE} /mnt
tar -C /tmp/cproot -cvf - . | tar -C /mnt -xf - 
umount /tmp/cproot /mnt
reboot
```

重启后 `ssh` 登录路由器，输入以下命令你会发现 `flash` 已扩容成功：

```bash
$ df -h
Filesystem                Size      Used Available Use% Mounted on
/dev/root                 2.3M      2.3M         0 100% /rom
tmpfs                    13.7M     68.0K     13.7M   0% /tmp
/dev/sda1               456.8M      2.3M    426.5M   1% /overlay 
overlayfs:/overlay      456.8M      2.3M    426.5M   1% /  # 扩容前为 400 多 K
tmpfs                   512.0K         0    512.0K   0% /dev
/dev/mtdblock3          384.0K    228.0K    156.0K  59% /rwm
```

最后，输入以下命令安装 Web 控制台 `Luci`：

```bash
opkg update
opkg install luci
```

安装后浏览器输入 `192.168.1.1` 即可打开登录界面。

![Openwrt 登录界面](https://pic1.zhimg.com/80/v2-90c5a0f80c58bd838f07dce206f589a2_1440w.webp?source=d16d100b)

至此，我们的安装任务就大功告成啦！

**（教程制作不易，如果成功的帮到了您，还请您动动您发财的小手，给 UP 主点个赞，谢谢了！（：**
