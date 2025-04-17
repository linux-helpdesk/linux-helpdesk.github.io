---
title: LazyVim PyRight 报错
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```text
Client pyright quit with exit code 1 and signal 0. Check log for errors: /root/.local/state/nvim/lsp.log
```

首先，所有 `LazyVim` 项目相关的日志都在 `~/.local/state/nvim/` 这一目录下。在文件 `lsp.log` 中查看到如下报错：

```log
'/root/.local/share/nvim/mason/packages/pyright/node_modules/pyright/dist/vendor.js:2\nexports.id=121,exports.ids=[121],exports.modules=...this.pat\n\nSyntaxError: Unexpected token =\n ... at Promise.all.Object.keys.reduce (/root/.local/share/nvim/mason/packages/pyright/node_modules/pyright/dist/pyright-langserver.js:1:1713)\n    at Array.reduce (<anonymous>)\n'
```

这通常是因为系统中安装的 Node 版本过旧，不支持该语法。接下来，我们会讲解具体原因，并给出升级 Node.js 的操作建议。

## 问题原因

1. **现代 JS 语法不被旧版 Node 支持**  
   Pyright 的 `vendor.js` 文件大量使用了 ES2015+ 特性（包括参数解构赋默认值、类字段等），而在旧版 Node.js 中，这些语法会直接导致 `Unexpected token =` 错误。citeturn0search2
2. **常见案例**  
   多个社区反馈均指向同一问题：在 Linux 发行版自带的旧版 Node（如 APT 源安装的 v8/v10）上运行 Pyright，就会出现类似错误。citeturn0search1

## 解决方案

1. **升级 Node.js 到 LTS 或最新版本**
   - 推荐安装 Node.js v18 或以上（Pyright 最低支持 v14）。
   - 可以使用官方安装包（[nodejs.org](https://nodejs.org)）或 nvm（Node Version Manager）来管理和切换版本。
   - 安装完成后，执行 `node -v` 确认版本 ≥ v14。citeturn0search0
2. **重装 Pyright**
   - 升级 Node 之后，先在 mason 中卸载再安装 Pyright：
     ```bash
     :MasonUninstall pyright
     :MasonInstall pyright
     ```
   - 或者全局通过 npm 安装并确保可执行路径在 Neovim 的 `PATH` 中：
     ```bash
     npm install -g pyright
     ```
3. **验证**
   - 在终端中运行 `pyright-langserver --version`，应能正常输出版本号。
   - 重启 Neovim，打开 Python 文件，应不再出现 `Unexpected token =` 错误。

## 小结

该错误并非 Pyright 本身的 Bug，而是 Node.js 运行环境过旧导致无法解析现代 JS 语法。升级 Node.js（推荐 v18+），并重新安装 Pyright，即可彻底消除此类启动报错。

若仍有问题，可检查 Neovim 内部使用的 Node 路径（`echo $PATH` / `:echo $PATH`），确保新版 Node 优先被加载。

---

**参考资料**

- Pyright 官方文档：如果没有较新的 Node，请先从 nodejs.org 安装最新版本 citeturn0search0
- 社区反馈（StackOverflow）：APT 安装的 Node 过旧，手动安装最新版后问题解决 citeturn0search1
- GitHub Issue：在古老 Node 版本上会因不识别现代 JS 特性而报 Unexpected token \* citeturn0search2
