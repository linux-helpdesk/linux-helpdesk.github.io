---
title: 运行 AppImage 缺少 FUSE
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 概要

当看到如下错误时，说明系统缺少 FUSE 2.x 运行时库：

```
dlopen(): error loading libfuse.so.2
AppImages require FUSE to run.
You might still be able to extract the contents of this AppImage
if you run it with the --appimage-extract option.
```

此时，最常见的解决方案是**安装对应的 libfuse2**软件包；如果无法安装，则可以使用`--appimage-extract`将 AppImage 解包后运行。 ([20.04 - Etcher appimage not working in Ubuntu20.04 - Ask Ubuntu](https://askubuntu.com/questions/1357194/etcher-appimage-not-working-in-ubuntu20-04?utm_source=chatgpt.com))

---

## 在各发行版上安装 FUSE2

下面按常见发行版分别列出安装命令。

### Debian / Ubuntu

- **Ubuntu < 22.04**

  ```bash
  sudo apt-get update
  sudo apt-get install fuse libfuse2
  ```

  ([fuse - Can't run an AppImage on Ubuntu 20.04](https://askubuntu.com/questions/1363783/cant-run-an-appimage-on-ubuntu-20-04?utm_source=chatgpt.com))

- **Ubuntu ≥ 22.04**

  ```bash
  sudo apt update
  sudo apt install libfuse2
  ```

  ([fuse - Can't run an AppImage on Ubuntu 20.04](https://askubuntu.com/questions/1363783/cant-run-an-appimage-on-ubuntu-20-04?utm_source=chatgpt.com))

- **Ubuntu 24.04 及以后**
  由于包名更改，需要先启用 universe 仓库：

  ```bash
  sudo add-apt-repository universe
  sudo apt update
  sudo apt install libfuse2t64
  ```

  ([FUSE · AppImage/AppImageKit Wiki - GitHub](https://github.com/appimage/appimagekit/wiki/fuse?utm_source=chatgpt.com))

- **针对 32 位或其他架构**
  如果要运行 i386、armhf 等格式的 AppImage，需要安装对应架构的库：

  ```bash
  sudo apt-get install libfuse2:i386
  sudo apt-get install libfuse2:armhf
  ```

  ([I get some errors related to something called “FUSE”](https://docs.appimage.org/user-guide/troubleshooting/fuse.html?utm_source=chatgpt.com))

---

## 无法或不想安装 FUSE 时的替代方案

如果因权限、环境隔离（如容器）或其它原因无法安装 FUSE，可以**解包** AppImage 并直接运行其中程序：

```bash
./YourAppImage.AppImage --appimage-extract
cd squashfs-root
./AppRun
```

这样绕过 FUSE 挂载，直接使用解压后的文件系统。 ([20.04 - Etcher appimage not working in Ubuntu20.04 - Ask Ubuntu](https://askubuntu.com/questions/1357194/etcher-appimage-not-working-in-ubuntu20-04?utm_source=chatgpt.com))
