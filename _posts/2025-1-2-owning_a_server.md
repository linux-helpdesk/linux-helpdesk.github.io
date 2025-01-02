---
title: 自己拥有一台服务器可以做哪些很酷的事情？ 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 挂照片

有了服务器以后第一件事当然是搭网站咯，在腾讯云买了台服务器，十年期的，搭了个网站，等以后有女朋友了用来上传和展示女朋友的照片。访问当然是需要密码的，域名就是女朋友的名字。。。嗯。。期待她以后无意间搜索自己网站的瞬间，看到我们俩一路走来的样子，能让她感动哭了。。

![](/assets/images/server-001.webp)

## DIY 坚果云 & 有道云笔记

给大家推荐一个好用的全平台文件同步工具：`Syncthing`

![](/assets/images/server-002.webp)

安装步骤非常简单：

```bash
sudo apt install syncthing
```

`Syncthing` 是一款开源免费跨平台的文件同步工具，是基于 P2P 技术实现设备间的文件同步，并且如果你恰巧拥有一台公网服务器(或者一台24小时开机的设备也可)，那么你就能将其变为一款免费的**云**同步工具。

当然，云同步工具都有了，云笔记自然不在话下。在你的共享文件夹下新建一个 `notespace` 文件夹，这样你的笔记就可以实现多端同步啦。如果你和我一样还是个命令行爱好者，就又同时获得了个命令行版有道云啦～

![](/assets/images/server-003.webp)

项目的 [Github链接](https://github.com/syncthing/syncthing) 在此，详情可自行查阅

## 跑量化交易

![](/assets/images/server-004.webp)

在服务器上部署了几个量化交易策略，每天24h实时运行实时出结果，最后将结果通过微信或短信发送到手机上

## 挂爬虫

利用量化交易平台提供的API接口让爬虫每天在服务器更新当天行情数据，服务器稳定运行两年，已经为我省下了上万的数据费

![](/assets/images/server-005.webp)

## 科学的上网

我一般使用的就是 `Python` 自带的 `sha***socks`, 当然这里就不详细叙述教程了，有需要的直接阅读[官方文档](https://pypi.org/project/shadowsocks/)就好了

## 下崽

你没有听错，不是下载，是下崽。但到底如何让服务器下崽呢，这里就要拿出我们最熟悉的 `ssh` 了。通过 `ssh` 将局域网 Linux 主机端口映射到公网服务器上，俗称反向代理，也叫做内网穿透。

在本地输入以下命令

```bash
ssh -CR \[RemotePort]:localhost:22 \[RemoteUser]@[RemoteIp]
```

在服务端输入以下命令即可随时随地操控家里的设备啦

```bash
ssh \[LocalUser]@localhost -p \[RemotePort]
```

这样你现在就拥有两台服务器了

当然，`ssh` 在稳定性方面有些不足，所以这里我们可以在本地使用 `autossh` 来增加下稳定性

```bash
autossh -M \[ListenPort] -CR \[RemotePort]:localhost:22 \[RemoteUser]@[RemoteIp]
```

如果你觉得还不够过瘾，服务器几万个端口，想开多少个你随意 /手动滑稽
