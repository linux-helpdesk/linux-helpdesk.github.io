---
title: 系统盘爆满？三步将 Python 开发环境完美迁移到大容量磁盘
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 引言

许多开发者在本地搭建 Python 环境时会遇到这样的尴尬：系统分区（通常是 `/`）容量有限，而 `conda` 和 `pip` 在安装大量包（尤其是涉及编译的科学计算库如 numpy、pandas）时，会无情地消耗宝贵的根分区空间。即便你已经通过 `ln -s` 或 `mount --bind` 将 `~/.cache/pip` 指向了其他磁盘，根分区的可用空间依然在不断缩小，这究竟是为什么？

答案在于：**pip 安装过程不仅使用缓存目录，还会在临时目录（如 `/tmp`）中解压、编译包**。即使下载的包文件（缓存）已重定向，临时文件仍然可能写在根分区。本文将手把手教你如何将整个 Python 开发环境（包括 Miniconda 安装、pip 缓存和临时目录）完整地迁移到大容量磁盘，彻底解决空间不足的烦恼。

---

## 一、准备工作：确认目标磁盘已正确挂载

在动手之前，请确保你有一个独立分区（例如 `/dev/sdb1`）已经挂载到某个目录（如 `/mnt`），并且该分区有足够的剩余空间。执行以下命令确认：

```bash
df -h /mnt
```

如果输出显示 `/dev/root` 或 `/dev/sda1` 等与根分区相同的设备，说明 `/mnt` 只是根目录下的一个普通文件夹，并非独立磁盘。这种情况下，你需要先挂载一块新磁盘到 `/mnt`（编辑 `/etc/fstab` 实现开机自动挂载），否则后续所有操作都只是在根分区内“搬家”，无法真正释放空间。

假设 `/mnt` 已正确挂载独立分区，我们开始迁移工作。

---

## 二、将 Miniconda 本体及数据安置到大容量磁盘

### 场景一：全新安装 Miniconda（最简单）

在安装时，直接指定安装路径到目标磁盘（例如 `/mnt/miniconda3`）。安装程序会自动将 Miniconda 的所有文件（包括可执行文件、包缓存 `pkgs`、虚拟环境 `envs`）都放在该目录下，从此与根分区绝缘。

```bash
# 以官方安装脚本为例
bash Miniconda3-latest-Linux-x86_64.sh -b -p /mnt/miniconda3
```

之后将 Miniconda 的 `bin` 目录添加到 `PATH` 即可正常使用。

### 场景二：已安装 Miniconda，需要迁移现有环境

如果你已经将 Miniconda 安装在根分区（如 `~/miniconda3`），希望将后续的包缓存和虚拟环境移到新磁盘，同时保留原有的 `base` 环境，可以通过修改 Conda 配置来实现。

#### 1. 创建目标文件夹

```bash
mkdir -p /mnt/conda/pkgs
mkdir -p /mnt/conda/envs
```

#### 2. 修改 Conda 配置

使用 `conda config` 命令添加新的路径：

```bash
conda config --add pkgs_dirs /mnt/conda/pkgs
conda config --add envs_dirs /mnt/conda/envs
```

#### 3. 验证配置是否生效

```bash
conda config --show pkgs_dirs envs_dirs
```

输出应显示 `/mnt/conda/` 下的两个目录位于列表最前面，表示优先级最高。

#### 4. （可选）迁移现有数据

如果你之前已经安装了许多包或创建了多个环境，可以手动将原有数据复制过来：

```bash
# 复制包缓存
cp -r ~/miniconda3/pkgs/* /mnt/conda/pkgs/

# 克隆虚拟环境（以 myenv 为例）
conda create -p /mnt/conda/envs/myenv --clone ~/miniconda3/envs/myenv
```

复制完成后，可以使用 `conda clean --all` 清理旧缓存，并手动删除原 `~/miniconda3/envs` 目录（谨慎操作）。

> **注意**：`base` 环境仍保留在原位置，但新安装的包和环境都会进入新目录，旧空间不会继续膨胀。

---

## 三、将 pip 缓存目录重定向到新磁盘

即使 Conda 管理了包缓存，在 Conda 环境中使用 `pip` 安装包时，pip 依然会使用自己的缓存目录（通常为 `~/.cache/pip`）。我们需要将它也指向 `/mnt`。

有两种常用方法：符号链接或绑定挂载。这里以符号链接为例：

### 1. 删除原有的缓存目录（如果存在）

```bash
rm -rf ~/.cache/pip   # 注意：这会删除所有旧的 pip 缓存，释放根分区空间
```

### 2. 创建新缓存目录并建立符号链接

```bash
mkdir -p /mnt/pip
ln -s /mnt/pip ~/.cache/pip
```

检查链接是否生效：

```bash
ls -l ~/.cache/pip
# 应显示 -> /mnt/pip
```

---

## 四、将 pip 临时目录也指向新磁盘——关键一步

前面两步只解决了“下载的包文件”存放位置，但 pip 安装过程中的**解压、编译临时文件**默认仍会写入系统临时目录（通常是 `/tmp`）。这正是根分区空间依然不断缩小的元凶。我们需要通过设置环境变量 `TMPDIR` 来改变这一行为。

### 1. 创建新的临时目录

```bash
mkdir -p /mnt/tmp
chmod 1777 /mnt/tmp   # 临时目录标准权限
```

### 2. 设置 TMPDIR 环境变量

**临时生效**（仅当前终端）：

```bash
export TMPDIR=/mnt/tmp
```

**永久生效**（推荐）：将上述命令添加到 shell 配置文件（如 `~/.bashrc`）：

```bash
echo 'export TMPDIR=/mnt/tmp' >> ~/.bashrc
source ~/.bashrc
```

### 3. 验证临时目录更改

```bash
python -c "import tempfile; print(tempfile.gettempdir())"
```

应输出 `/mnt/tmp`。

现在，任何 pip 安装操作都会在 `/mnt/tmp` 中解压和编译，安装完成后自动清理临时文件，不再占用根分区。

---

## 五、验证迁移效果

进行一次完整的安装测试，观察根分区空间变化：

```bash
# 创建一个测试环境
conda create -n test_env python=3.9 -y
conda activate test_env

# 安装一个较大的包（如 numpy）
pip install numpy

# 检查缓存和临时文件位置
ls -la /mnt/pip          # 应有 numpy 的缓存
ls -la /mnt/conda/pkgs   # 应有 numpy 的 conda 包缓存（如果用 conda 安装）
df -h /                   # 根分区空间应稳定，不再持续下降
```

同时，你可以用 `df -h /mnt` 观察新分区的使用量增长，确保所有写操作都发生在目标磁盘。

---

## 六、常见问题与注意事项

1. **挂载点重启后失效**：如果使用 `mount --bind` 而非符号链接，请确保将挂载信息写入 `/etc/fstab` 以实现持久化。
2. **权限问题**：确保你的用户对新目录（`/mnt/pip`、`/mnt/tmp`、`/mnt/conda`）有读写权限。必要时使用 `chown` 调整所有者。
3. **Conda 环境克隆**：`conda create -p /绝对路径 --clone 旧环境` 是迁移虚拟环境的推荐方式，避免直接复制文件夹导致路径硬编码问题。
4. **多用户环境**：如果服务器有多位用户，建议为每个用户单独创建缓存和临时目录，或使用共享目录并合理设置权限。
5. **其他临时文件**：某些包在编译过程中可能还会使用 `/var/tmp` 或其他目录，但设置 `TMPDIR` 通常能覆盖大部分情况。如有特殊需求，可进一步研究具体包的构建行为。

---

## 总结

通过上述三步，我们将 Python 开发环境的核心数据（conda 本体、包缓存、虚拟环境、pip 缓存、pip 临时目录）全部迁移到了大容量磁盘 `/mnt`。这一组合策略彻底解决了系统盘空间不足的问题，让你可以放心地安装成百上千个 Python 包，而无需担心根分区被撑爆。

无论你是全新安装还是已有环境需要迁移，都能找到对应的解决方案。如果你在操作中遇到任何困难，欢迎在评论区留言交流。希望这篇博客能帮助到你，让你的开发环境不再受磁盘容量的束缚！


