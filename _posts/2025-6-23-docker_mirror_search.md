---
title: 大陆地区 Docker 使用指南
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

随着 Docker 的普及，容器化已经成为开发与运维的重要组成部分。然而在中国大陆，由于网络防火墙（GFW）的存在，访问 Docker Hub 或其它国外镜像仓库时，常常会遇到搜索、拉取镜像速度极慢甚至超时的问题。本文将介绍两种简单实用的技巧，帮助你在大陆地区加速 Docker 镜像的搜索与拉取。

---

### 方法一：`docker search` 指定镜像仓库

默认情况下，`docker search` 命令会在 Docker Hub 公共镜像仓库中进行查询，但在网络受限环境中，访问 Docker Hub 的速度可能非常缓慢。我们可以通过在命令中指定其他镜像仓库地址来绕过这一限制：

```bash
# 在 quay.io 镜像仓库中搜索 redis 镜像
docker search quay.io/redis
```

其中：

- `<registry-url>`：目标镜像仓库域名（如 `quay.io`、`ghcr.io`、私有仓库地址等）。
- `<image-name>`：你要查询的镜像名称（如 `redis`、`nginx`、`mysql` 等）。

> **提示**：部分仓库支持在镜像后追加 `:<tag>`，实现更精确的检索。例如：
>
> ```
> docker search quay.io/redis:6.2
> ```

> **注意**：不同仓库的 `search` 功能可能存在差异，具体选项与返回字段请参考对应仓库官方文档。

**可选镜像仓库地址示例（来源：GitHub 仓库 [https://github.com/dongyubin/DockerHub）：](https://github.com/dongyubin/DockerHub）：)**

- docker.1ms.run
- dytt.online
- lispy.org
- docker.xiaogenban1993.com
- docker.yomansunter.com
- 666860.xyz
- hub.rat.dev

---

### 方法二：配置加速器与代理脚本（Source on GitHub）

针对镜像拉取缓慢的问题，我们可以通过配置 `registry-mirrors` 或者网络代理，将官方镜像请求重定向至速度更快的国内加速源。下面提供两组脚本，托管于作者的 GitHub Pages：

#### 1. 一键切换镜像加速器

```bash
# 安装并运行脚本
curl -fsSL https://install-neovim.github.io/docker-mirror | bash
```

该脚本会生成或覆盖 `/etc/docker/daemon.json`，内容示例：

```json
{
  "registry-mirrors": [
    "https://docker.unsee.tech",
    "https://dockerpull.org",
    "https://docker.1panel.live",
    "https://dockerhub.icu"
  ]
}
```

脚本执行完成后，会自动重载并重启 Docker 服务：

```bash
sudo systemctl daemon-reload && sudo systemctl restart docker
```

通过镜像加速器列表，Docker 在拉取镜像时会优先从这些国内源获取，极大提升下载速度。

#### 2. 配置 Docker 服务的 HTTP/HTTPS 代理

对于无法直接访问外部网络的环境（如公司内网，或使用自建代理时），可以为 Docker 服务配置代理：

```bash
# 安装并运行脚本，替换为你的代理地址与端口
curl -fsSL https://install-neovim.github.io/docker-proxy | bash -s "proxy.example.com:3128"
```

脚本原理：

1. 在 `/etc/systemd/system/docker.service.d/proxy.conf` 中写入如下内容：

   ```ini
   [Service]
   Environment="HTTP_PROXY=http://proxy.example.com:3128/"
   Environment="HTTPS_PROXY=http://proxy.example.com:3128/"
   Environment="NO_PROXY=localhost,127.0.0.1"
   ```

2. 重载 systemd 配置并重启 Docker：

   ```bash
   sudo systemctl daemon-reload && sudo systemctl restart docker
   ```

配置代理后，Docker 在拉取镜像和构建时，所有外部 HTTP/HTTPS 请求都会通过指定代理通道进行。

---

### 拓展：手动修改 `daemon.json`

如果你更偏好手动操作，也可以按照以下步骤：

```bash
sudo mkdir -p /etc/docker
cat <<-'EOF' | sudo tee /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://docker.unsee.tech",
    "https://dockerpull.org"
  ],
  "insecure-registries": [
    "my-private-registry.local:5000"
  ]
}
EOF

sudo systemctl daemon-reload && sudo systemctl restart docker
```

- `registry-mirrors`：列出所有镜像加速地址。
- `insecure-registries`：如果你的私有仓库使用 HTTP 或者自签名证书，可通过此字段允许访问。

---

## 总结

在中国大陆环境下使用 Docker 时：

1. **搜索**：通过 `docker search <registry>/<image>` 直接查询国内或镜像托管平台中的镜像。
2. **拉取加速**：使用一键脚本配置 `registry-mirrors`，加速公共镜像下载。
3. **网络代理**：在无法直接访问外网时，为 Docker 服务配置 HTTP/HTTPS 代理。

通过上述方法，你可以在大部分场景中显著提升 Docker 镜像拉取与搜索的稳定性与速度。欢迎在评论区分享你的经验与更多镜像源，也可关注 GitHub 仓库获取脚本更新。
