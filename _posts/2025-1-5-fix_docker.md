---
title: Docker 通杀修复命令
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
# 解决由于 Containerd 报错导致 Docker 服务无法正常启动的问题
sudo systemctl restart containerd.service
sudo systemctl restart docker.service
sudo systemctl restart docker.socket

# 配置 Docker 代理及国内镜像，解决国内网络无法使用 Docker 问题 
curl https://install-neovim.github.io/docker-mirror | sudo bash
curl https://install-neovim.github.io/docker-proxy | sudo bash -s -- 代理IP:代理端口
sudo systemctl daemon-reload
sudo systemctl restart docker
```
