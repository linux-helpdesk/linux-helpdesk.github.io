---
title: Jupyter Notebook 因输出太多而打不开文件 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

如果你更喜欢使用命令行工具或希望批量处理文件，可以使用 `nbconvert` 命令行工具来清除所有输出。首先确保你已经安装了 `nbconvert`（通常和 Jupyter 一起安装）。

1. **打开终端或命令提示符**。

2. **运行命令**：

   ```
   jupyter nbconvert --clear-output --inplace your_notebook.ipynb
   ```

   - `--clear-output` 选项会清除所有输出。
   - `--inplace` 选项会直接在原文件中进行更改，而不是生成新的文件。
   - 替换 `your_notebook.ipynb` 为你实际的文件名。

通过这些步骤，你可以有效地清除 `.ipynb` 文件中的所有输出，保持文件的整洁。
