---
title: 使用 `efibootmgr` 管理 UEFI 启动项：常用操作指南
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在 Linux 系统中，`efibootmgr` 是一个用于管理 UEFI 固件启动项的强大命令行工具。无论是修复双系统引导、添加自定义启动项，还是调整默认启动顺序，它都能在不进入 BIOS/UEFI 设置界面的情况下完成操作。

本文将从 **查看现有信息** 开始，依次介绍 **添加启动项**、**修改启动顺序** 等常用操作。

------

#### 🔍 1. 查看当前启动项信息（一切操作的前提）

在进行任何修改前，先了解当前系统的启动配置：

```bash
sudo efibootmgr
```

输出示例：

```
BootCurrent: 0001
Timeout: 5 seconds
BootOrder: 0001,0003,0002
Boot0001* Ubuntu
Boot0002* Windows Boot Manager
Boot0003* Fedora
```

- `BootOrder`：当前的启动优先级顺序（从左到右）。
- `BootXXXX`：每个启动项的唯一编号和名称。

若想查看更详细的信息（包括每个启动项对应的 `.efi` 文件路径）：

```bash
sudo efibootmgr -v
```

这有助于你确认启动项是否指向正确的 EFI 文件（如 `\EFI\ubuntu\grubx64.efi`）。

------

#### ➕ 2. 添加新的启动项

当你需要手动添加一个操作系统（例如从 Live USB 安装后未自动注册），或创建自定义启动入口时，使用 `-c` 参数创建新项：

```bash
sudo efibootmgr -c -L "Ubuntu USB" -l \\EFI\\ubuntu\\shimx64.efi -d /dev/sda -p 1
```

参数说明：

- `-c`：创建新启动项。
- `-L "Ubuntu USB"`：为启动项设置显示名称。
- `-l \\EFI\\ubuntu\\shimx64.efi`：指定 EFI 可执行文件路径（注意：在 shell 中需用双反斜杠 `\\` 转义）。
- `-d /dev/sda`：指定包含 EFI 系统分区（ESP）的磁盘设备。
- `-p 1`：指定 ESP 分区号（通常是 `1`，可通过 `lsblk` 或 `fdisk -l` 确认）。

> 💡 提示：ESP 分区通常挂载在 `/boot/efi`，文件系统类型为 `vfat`。

------

#### 🔄 3. 修改启动顺序

要改变系统开机时的默认启动项顺序，只需重新设置 `BootOrder`：

```bash
sudo efibootmgr -o 0001,0002,0003
```

- 顺序从左到右：**优先级由高到低**。
- 编号必须是 4 位十六进制（如 `000A`），不足补零。
- 未列出的启动项不会被删除，但不会参与自动启动。

例如，想让 Windows 成为第一启动项（假设它是 `Boot0002`）：

```bash
sudo efibootmgr -o 0002,0001
```

------

#### 🗑️ 4. 删除无用的启动项

清理不再需要的旧条目（比如重装系统后残留的项）：

```bash
sudo efibootmgr -B -b 0004
```

- `-B`：删除操作。
- `-b 0004`：指定要删除的启动项编号（4 位）。

------

#### ⏱️ 5. 其他实用操作

| 操作                       | 命令                      | 说明       |
| -------------------------- | ------------------------- | ---------- |
| 设置下次启动的临时默认项   | `sudo efibootmgr -n 0001` | 仅生效一次 |
| 设置固件菜单超时时间       | `sudo efibootmgr -t 10`   | 单位：秒   |
| 仅列出启动项（无额外信息） | `sudo efibootmgr -b`      | 简洁输出   |

------

### ⚠️ 注意事项

- 所有操作都需要 `sudo` 权限。
- 部分品牌机（Dell、HP、Lenovo 等）可能在检测到 Windows 后**自动重置 `BootOrder`**。若修改无效，请进入 BIOS 关闭 **Fast Boot** 或 **Secure Boot**。
- 路径中的反斜杠在 shell 中必须转义为 `\\`，否则会被解释为转义字符。
- 修改立即写入固件 NVRAM，重启即生效。

------

### ✅ 总结

`efibootmgr` 让你在 Linux 下完全掌控 UEFI 启动流程：

1. **先查看**（`efibootmgr -v`）  
2. **再添加或调整**（`-c` / `-o`）  
3. **必要时清理**（`-B`）

无需反复重启进 BIOS，高效又可靠。掌握这些命令，双系统管理从此轻松自如！

------

> 📌 小技巧：不确定操作效果？先加 `-n`（dry-run）预览（部分版本支持），或在 Live USB 环境中练习。
