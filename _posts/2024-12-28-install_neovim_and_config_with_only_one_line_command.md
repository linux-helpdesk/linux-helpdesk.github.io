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

#### **特定语言开发环境配置**

上述命令会自动从源码编译安装最新版 Neovim 并自动配置 Lazyvim 到本地系统。安装及配置完成后会自动清理安装 过程中产生的文件。

安装并配置好 Lazyvim 后，可以根据需要通过内置工具安装特定语言的开发环境。例如，配置 Python 开发环境：

1. 在 Neovim 中输入 `:LazyExtras`。
2. 使用 `/` 搜索关键字 `python`，找到 `lang.python` 并按 `x` 键安装相关插件。
3. 退出 Neovim 后重新打开，Lazyvim 会自动完成插件的安装。

如果安装未完成，可以尝试多次或通过 `proxychains4 nvim test.py` 启动 Neovim 并触发安装。

**字体**

字体配置非必须，可选择性配置。如果想要像效果图中一样显示图标，则需要下载 [Nerd Fonts](https://www.nerdfonts.com/) 字体，并在本地终端中进行手动配置。