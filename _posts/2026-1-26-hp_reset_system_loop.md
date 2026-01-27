---
title: 惠普（HP）电脑安装 Ubuntu 后卡在 “Reset System” 无限重启

author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

> **TL;DR**：
> 别折腾 BIOS 启动顺序了——**直接删除 `\EFI\Boot\fbx64.efi` 才是真正有效的解决方案**。
> 这个文件是 Ubuntu 安装时写入的 fallback EFI 程序，它与 HP 固件互相修改 `BootOrder`，导致死循环。

------

#### 🌀 问题现象

- 在 HP 笔记本（如 EliteBook、ProBook、Pavilion 等）安装 Ubuntu；
- 开机黑屏，反复显示 **“Reset System”** 并自动重启；
- 但通过 `ESC → F9` 手动选择 **“Ubuntu”** 可正常进入系统；
- 一旦你从 Live USB 或 BIOS 中选择“USB Drive”或“Hard Disk”设备启动（而非明确选“Ubuntu”），循环立刻重现。

这不是驱动问题，也不是安装失败——而是一个 **UEFI 启动机制冲突**。

------

#### 🔍 真正原因

Ubuntu 安装时会在 EFI 分区写入一个名为 `fbx64.efi` 的程序（全称 `fallback.efi`），位于：

```
\EFI\Boot\fbx64.efi
```

它的设计初衷是：**当系统找不到已注册的启动项时，自动扫描并创建一个新的**。

但在 HP 电脑上，问题来了：

1. HP BIOS 默认（或用户设置）优先从 **“设备”**（如整个硬盘或 USB 盘）启动；
2. 此时 UEFI 会加载默认路径 `\EFI\Boot\bootx64.efi`，后者调用 `fbx64.efi`；
3. `fbx64.efi` 发现 `\EFI\ubuntu\` 存在，于是：
   - 自动创建或提升 `ubuntu` 启动项；
   - **强制修改 `BootOrder`**；
   - **立即重启系统**；
4. 重启后，HP BIOS 又检测到“设备”优先级更高，再次从 `\EFI\Boot\` 启动……
   → **死循环开始**。

> ⚠️ 即使你在 BIOS 里把 “ubuntu” 设为第一，只要某次误选了“Hard Disk”启动，`fbx64.efi` 就会被触发，一切重来。

------

#### ✅ 唯一可靠解决方案：删除 `fbx64.efi`

要彻底打破这个循环，**必须移除自动篡改启动顺序的源头**：

```bash
# 1. 确保 EFI 系统分区已挂载（通常为 /boot/efi）
ls /boot/efi/EFI/Boot/fbx64.efi  # 先确认文件存在

# 2. 删除 fbx64.efi（即 fallback.efi）
sudo rm /boot/efi/EFI/Boot/fbx64.efi
```

> 💡 注意：
>
> - **不要删除 `bootx64.efi`** —— 它是标准通用启动入口，安全且必要；
> - 只删 `fbx64.efi` 即可，Ubuntu 的正常启动完全不受影响；
> - 删除后，即使从“USB Drive”启动，也不会再触发自动重启。

------

#### 🛠️ 补充建议（可选）

如果你担心未来重装系统又写回该文件，可以：

- **备份后删除**：

  ```bash
  sudo cp /boot/efi/EFI/Boot/fbx64.efi ~/fbx64.efi.bak
  sudo rm /boot/efi/EFI/Boot/fbx64.efi
  ```

- **或直接重命名**（更安全）：

  ```bash
  sudo mv /boot/efi/EFI/Boot/fbx64.efi /boot/efi/EFI/Boot/fbx64.efi.disabled
  ```

------

#### ✅ 验证修复

重启系统，不再按 `F9`，让其默认启动——
如果不再出现 “Reset System”，而是直接进入 GRUB 或 Ubuntu，说明问题已解决！

------

### 总结

| 方法                           | 是否有效             | 说明                                 |
| ------------------------------ | -------------------- | ------------------------------------ |
| 调整 BIOS 启动顺序             | ❌ 临时有效，极易复发 | HP 固件会因设备启动再次触发 fallback |
| **删除 `\EFI\Boot\fbx64.efi`** | ✅ **永久有效**       | 切断死循环根源，一劳永逸             |

> 这不是 Ubuntu 的 bug，也不是 HP 的错——只是两者在 UEFI fallback 行为上的不兼容。
> 而删除 `fbx64.efi`，是最简单、最干净、最可靠的解决方式。

