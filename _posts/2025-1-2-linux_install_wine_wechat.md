---
title: 如何在 Linux 上安装微信（非 Deepin-WeChat） 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

1. 安装 `wine`
   $ sudo apt update && sudo apt install wine

   

2. 在系统中安装中文字符集（若系统已为中文环境可忽略这步）
   $ sudo dpkg-reconfigure locales
   选中 `zh_CN.UTF-8` 并按提示完成配置。

   

3. 进入[官网](http://link.zhihu.com/?target=https%3A//windows.weixin.qq.com/)下载[安装包](http://link.zhihu.com/?target=https%3A//dldir1.qq.com/weixin/Windows/WeChatSetup.exe)并使用 `wine` 安装
   $ env LANG=zh_CN.UTF-8 wine WeChatSetup.exe
   （这里注意将 `WeChatSetup.exe` 替换成你下载到的安装包文件名。）

   

4. 配置 `wine-wechat`

  - 安装 `wine` 配置工具 `winetricks`
    $ sudo apt install winetricks
  - 安装 `wine` 中文字体
    $ winetricks fakechinese
  - 安装 `riched20` 组件（解决输入窗口不显示文字问题）
    $ winetricks riched20
  - 修改 `.desktop` 快捷方式以解决中文乱码问题（若系统已为中文环境可忽略这步）
    在 `桌面` 或者 `~/.local/share/applications/wine/Programs/WeChat/` 路径下找到 `WeChat.desktop` 文件，并使用任意文本编辑器打开。
    找到第三行（`Exec=env...` 所在行），在 `env` 后插入 `LANG=zh_CN.UTF-8` 并注意前后空格，退出保存。

