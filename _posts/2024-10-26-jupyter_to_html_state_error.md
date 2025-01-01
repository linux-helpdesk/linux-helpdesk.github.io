---
title: "Jupyter Notebook 导出 HTML 报错 KeyError: 'state'"
author: "Zhao Zilong"
date: 2024-10-26
category: AI
layout: post
---

当时用 Jupyter Notebook 导出 `.ipynb` 文件的 HTML 文件时会报如下错误：

{% raw %}

```plaintext
(pytorch-gpu) ..[warren@localhost] - [~/Downloads/dl] - [五 10月 25, 04:24]
..[$] <()> jupyter nbconvert --to html main.ipynb
[NbConvertApp] Converting notebook main.ipynb to html
Traceback (most recent call last):
  File "/home/warren/miniconda3/envs/pytorch-gpu/bin/jupyter-nbconvert", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/jupyter_core/application.py", line 283, in launch_instance
    super().launch_instance(argv=argv, **kwargs)
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/traitlets/config/application.py", line 1075, in launch_instance
    app.start()
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 420, in start
    self.convert_notebooks()
   ^^^^^^^^^^^^^^
...

  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/display_priority.j2", line 7, in block 'data_priority'
    {%- for type in output.data | filter_data_type -%}
^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/filters/widgetsdatatypefilter.py", line 58, in __call__
    metadata["widgets"][WIDGET_STATE_MIMETYPE]["state"]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
KeyError: 'state'

```

{% endraw %}

程序会出现上述错误的原因是 ipynb 文件中存在一些 widgets 控件，这些控件存在的目的是增加文件的可交互性。但有时即使开发者并没有添加这些控件，控件依然会被加入文件中。（如从 Google Colab 下载脚本文件时，会自动添加控件）

此时使用如下命令去除控件信息，然后再进行导出：

```bash
# 去除控件信息
jq -M 'del(.metadata.widgets)'  main.ipynb > main_rm.ipynb
# 转换导出
jupyter nbconvert --to html main_rm.ipynb
```

这里的 `main.ipynb` 和 `main_rm.ipynb` 需要你在使用时替换成自己的文件名。现在，在当前文件夹下就会有一个名叫 `main_rm.ipynb` 的新文件生成了。

> 参考链接：<https://github.com/jupyter/nbconvert/issues/1731>
