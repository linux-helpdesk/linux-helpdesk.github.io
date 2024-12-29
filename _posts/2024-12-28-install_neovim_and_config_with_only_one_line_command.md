---
title: 一行命令实现 Neovim 安装及配置
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

直接上代码：
```bash
curl https://install-neovim.github.io | bash 
```
Over! ~

效果图：

![image](/assets/images/lazyvim.png)

____

### 注意事项：

**代理**

国内用户部分地区请自备代理，使用 `proxychains4` 工具配合上述命令：

```bash
proxychains4 curl https://install-neovim.github.io | bash 
```

如果依然因“防火墙”拦截导致安装过程出现中断，可以先使用以下命令将脚本保存到本地，然后配合 `proxychains4` 手动逐行运行：

```bash
proxychains4 curl https://install-neovim.github.io > install.sh
```

**特定语言开发环境配置**

上述命令会自动从源码编译安装最新版 Neovim 并自动配置 Lazyvim 到本地系统。安装及配置完成后会自动清理安装 过程中产生的文件。

Lazyvim 会在 Neovim 打开后自动安装必要的组件，此时如果需要特定语言的开发环境，即可使用 Lazyvim 中内置的工具进行配置了。比如这里以配置 Python 开发环境举例：

首先在 Neovim 界面打开 `:LazyExtras`，使用 `/` 命令搜索关键字 `python`，回车导航到 `lang.python` 后按 `x` 安装 `python` 相关插件，完全退出 `nvim` 后重新打开开始自动化安装流程。

如果重新启动 `nvim` 后依然没有安装完成，那就多试几次或使用 `proxychains4 nvim test.py` 挂代理并触发安装。 

**字体**

字体配置非必须，可选择性配置。如果想要像效果图中一样显示图标，则需要下载 [Nerd Fonts](https://www.nerdfonts.com/) 字体，并在本地终端中进行手动配置。