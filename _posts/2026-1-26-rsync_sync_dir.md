---
title: 使用 `rsync` 高效同步文件与目录：实用指南
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在日常的系统管理、数据备份或迁移工作中，文件和目录的同步是一个常见需求。Linux 提供了多种工具来完成这项任务，而 `rsync` 凭借其高效性、灵活性和丰富的功能选项，成为其中最受欢迎的选择之一。本文将详细介绍如何使用 `rsync` 来同步文件与目录，并解决一些常见的误解和问题。

------

#### 🔍 1. 基础用法：同步两个目录

假设我们有两个目录 `gradless` 和 `gradless.bak`，想要将前者的内容同步到后者中。

##### 错误示例：

```bash
rsync --progress -av gradless gradless.bak
```

执行上述命令后，你可能会发现 `gradless.bak` 目录下多了一个名为 `gradless` 的子目录，而不是直接将内容复制进去。这是因为源路径没有以斜杠 `/` 结尾。

##### 正确做法：

要确保 `gradless` 目录内的所有文件直接被复制到 `gradless.bak` 中，应使用带斜杠的路径：

```bash
rsync --progress -av gradless/ gradless.bak/
```

这里的关键是 **源路径末尾加上斜杠** (`/`)，这告诉 `rsync` 同步的是目录内容而非整个目录结构。

------

#### ➕ 2. 创建目标目录（如果不存在）

如果你的目标目录 `gradless.bak` 不存在，不用担心——`rsync` 会自动为你创建它。例如：

```bash
rsync --progress -av gradless/ gradless.bak/
```

即使 `gradless.bak` 目录原先并不存在，`rsync` 也会在同步过程中自动创建它，并将 `gradless` 目录中的内容放入其中。

> ⚠️ 注意：若目标路径的父目录不可写，则会报错。

------

#### 🔄 3. 设置同步行为

除了基本的文件复制，`rsync` 还提供了许多选项来控制同步行为：

- **保留权限、时间戳等元数据**：

  ```bash
  rsync -av source/ destination/
  ```

  `-a`（archive）模式会递归同步，并尽可能保留文件属性。

- **显示进度条**：

  ```bash
  rsync --progress -av source/ destination/
  ```

- **删除目标目录中多余的文件**（保持镜像一致）：

  ```bash
  rsync -av --delete source/ destination/
  ```

  这个选项非常有用，尤其是当你希望目标目录完全反映源目录的状态时。

- **模拟运行**（dry-run），查看即将发生的变化而不实际执行：

  ```bash
  rsync -avn source/ destination/
  ```

------

#### 🗑️ 4. 删除旧的或不必要的文件

有时候，你的目标目录可能包含了不再存在于源目录中的文件。为了保持目标目录与源目录的一致性，可以使用 `--delete` 选项来删除这些多余的文件。

```bash
rsync -av --delete gradless/ gradless.bak/
```

这样，任何在 `gradless.bak` 中但不在 `gradless` 中的文件都会被删除，确保两个目录严格同步。

------

#### 💡 小技巧

- **排除特定文件或目录**：如果你想同步大部分内容但排除某些文件或目录，可以使用 `--exclude` 选项：

  ```bash
  rsync -av --exclude='*.tmp' source/ destination/
  ```

- **跨网络同步**：`rsync` 也支持通过 SSH 进行远程同步，只需指定远程主机地址：

  ```bash
  rsync -avz /local/path user@remote:/path
  ```

  其中 `-z` 表示压缩传输的数据。

------

### 总结

`rsync` 是一个强大且灵活的工具，适用于各种文件同步场景。无论你是需要简单的本地文件复制，还是复杂的远程备份和镜像操作，掌握以下几点将大大提高效率：

1. **正确使用斜杠**：源路径是否带斜杠决定了是同步目录本身还是其内容。
2. **自动创建目标目录**：无需手动创建目标目录，`rsync` 会自动处理。
3. **精细控制同步行为**：利用 `-a`, `--delete`, `--exclude` 等选项实现更精准的同步需求。
4. **模拟运行**：在执行大规模同步前，先用 `-n` 模拟运行，确认无误后再正式操作。

通过这篇文章，希望你能更好地理解并应用 `rsync`，让文件同步工作更加轻松高效！
