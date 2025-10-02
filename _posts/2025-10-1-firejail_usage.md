---
title: Firejail 使用笔记
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## 1. `--private` 参数的区别

### 不带 `--private` 参数
```bash
firejail konsole
```
- **文件系统可见性**：可以看见并访问宿主系统的完整家目录
- **持久化**：在终端中创建的文件会保存在实际的家目录中
- **权限限制**：仍然受到 Firejail 的基本权限限制（如无法使用 sudo、su）

### 带 `--private` 参数
```bash
firejail --private konsole
```
- **文件系统隔离**：创建一个临时的、空的虚拟家目录
- **非持久化**：退出后所有在沙盒中创建的文件都会消失
- **完全隔离**：无法访问宿主系统的实际文件（除了一些必要的系统文件）

## 2. `--private` 后跟路径的区别

### 不指定路径（临时空目录）
```bash
firejail --private konsole
```
- 每次启动都创建一个全新的空临时目录
- 退出后所有更改丢失
- 适合需要完全隔离的临时任务

### 指定路径（持久化私有目录）
```bash
firejail --private=/home/admin/Firejail/Konsole konsole
```
- 使用指定目录作为私有家目录
- **持久化**：在沙盒中创建的文件会保存在该目录中
- **隔离但持久**：既与主系统隔离，又能保留工作成果
- 适合需要保存工作但又希望与主系统隔离的场景

## 3. Konsole 测试结果总结

| 启动方式                           | 文件可见性       | 文件持久化           | sudo/su 权限 |
| ---------------------------------- | ---------------- | -------------------- | ------------ |
| `firejail konsole`                 | 可见完整家目录   | ✅ 持久化             | ❌ 被阻止     |
| `firejail --private konsole`       | 空目录           | ❌ 临时性             | ❌ 被阻止     |
| `firejail --private=/path konsole` | 仅见指定目录内容 | ✅ 在指定路径中持久化 | ❌ 被阻止     |

**关键发现**：
- 所有 Firejail 环境都阻止了特权命令（sudo、su）
- `--private` 不指定路径时创建临时沙盒
- `--private=/path` 使用指定目录作为持久化沙盒环境

## 4. 网络访问控制

### 完全禁用网络
```bash
# 方法1：使用 --net=none
firejail --net=none konsole

# 方法2：使用 --nosound（同时禁用声音）
firejail --net=none --nosound konsole
```

### 限制网络访问
```bash
# 只允许本地回环网络
firejail --net=lo konsole

# 使用特定的网络配置
firejail --net=eth0 --dns=8.8.8.8 konsole
```

### 验证网络状态
在沙盒中测试网络连接：
```bash
# 测试网络连通性
ping google.com

# 检查网络接口
ip addr show

# 测试 HTTP 访问
curl http://example.com
```

## 5. `--appimage` 参数

### 专门用于运行 AppImage
```bash
# 基本用法
firejail --appimage /path/to/program.AppImage

# 结合其他参数
firejail --appimage --private /path/to/program.AppImage
firejail --appimage --net=none /path/to/program.AppImage
```

### `--appimage` 参数的特点
1. **自动配置**：为 AppImage 自动设置合适的沙盒规则
2. **文件访问**：允许访问当前目录和临时目录
3. **图形支持**：确保 X11 或 Wayland 图形界面正常工作
4. **简化使用**：无需手动配置复杂的文件系统规则

### 实际应用示例
```bash
# 运行 LibreWolf AppImage 并禁用网络
firejail --appimage --net=none ./LibreWolf.AppImage

# 在私有沙盒中运行 AppImage
firejail --appimage --private=/home/admin/AppImageSandbox ./MyApp.AppImage
```

## 实用技巧与最佳实践

### 配置文件管理
```bash
# 查看当前配置
firejail --list

# 查看可用配置
ls /etc/firejail/

# 创建用户级配置
mkdir -p ~/.config/firejail
cp /etc/firejail/firejail.config ~/.config/firejail/
```

### 常用组合命令
```bash
# 安全浏览：无网络 + 私有目录
firejail --net=none --private firefox

# 开发测试：持久化私有目录
firejail --private=/home/user/dev-sandbox --net=none code

# AppImage 完全隔离
firejail --appimage --net=none --private /path/to/app.AppImage
```

### 验证沙盒效果
在沙盒环境中检查：
```bash
# 检查当前进程的沙盒状态
firejail --tree

# 查看网络隔离
ip route show

# 检查文件系统隔离
ls -la ~/
mount | grep firejail
```

这份笔记涵盖了 Firejail 的核心用法，特别强调了 `--private` 参数的不同行为模式，以及如何有效运行 AppImage 应用程序。
