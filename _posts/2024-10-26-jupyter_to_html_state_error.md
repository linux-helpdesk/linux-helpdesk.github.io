---
title: "Jupyter Notebook 导出 HTML 报错 KeyError: 'state'"
author: "Zhao Zilong"
date: 2024-10-26
category: AI
layout: post
---

当时用 Jupyter Notebook 导出 `.ipynb` 文件的 HTML 文件时会报如下错误：

```
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
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 597, in convert_notebooks
    self.convert_single_notebook(notebook_filename)
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 563, in convert_single_notebook
    output, resources = self.export_single_notebook(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/nbconvertapp.py", line 487, in export_single_notebook
    output, resources = self.exporter.from_filename(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/templateexporter.py", line 386, in from_filename
    return super().from_filename(filename, resources, **kw)  # type:ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/exporter.py", line 201, in from_filename
    return self.from_file(f, resources=resources, **kw)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/templateexporter.py", line 392, in from_file
    return super().from_file(file_stream, resources, **kw)  # type:ignore[return-value]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/exporter.py", line 220, in from_file
    return self.from_notebook_node(
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/html.py", line 268, in from_notebook_node
    html, resources = super().from_notebook_node(nb, resources, **kw)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/exporters/templateexporter.py", line 424, in from_notebook_node
    output = self.template.render(nb=nb_copy, resources=resources)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/jinja2/environment.py", line 1304, in render
    self.environment.handle_exception()
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/jinja2/environment.py", line 939, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/index.html.j2", line 4, in top-level template code
    {% from 'jupyter_widgets.html.j2' import jupyter_widgets %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 3, in top-level template code
    {% from 'cell_id_anchor.j2' import cell_id_anchor %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/display_priority.j2", line 1, in top-level template code
    {%- extends 'base/null.j2' -%}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 26, in top-level template code
    {%- block body -%}
    ^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 29, in block 'body'
    {%- block body_loop -%}
^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 31, in block 'body_loop'
    {%- block any_cell scoped -%}
^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 34, in block 'any_cell'
    {%- block codecell scoped -%}
^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 13, in block 'codecell'
    {{ super() }}
    ^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 44, in block 'codecell'
    {%- block output_group -%}
^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 39, in block 'output_group'
    {{ super() }}
    ^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 48, in block 'output_group'
    {%- block outputs scoped -%}

  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 45, in block 'outputs'
    {{ super() }}
    ^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 50, in block 'outputs'
    {%- block output scoped -%}

  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 92, in block 'output'
    {{ super() }}
    ^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/null.j2", line 52, in block 'output'
    {%- block execute_result scoped -%}{%- endblock execute_result -%}

  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 130, in block 'execute_result'
    {% block data_priority scoped %}
    ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/lab/base.html.j2", line 131, in block 'data_priority'
    {{ super() }}
    ^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/share/jupyter/nbconvert/templates/base/display_priority.j2", line 7, in block 'data_priority'
    {%- for type in output.data | filter_data_type -%}
^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/warren/miniconda3/envs/pytorch-gpu/lib/python3.12/site-packages/nbconvert/filters/widgetsdatatypefilter.py", line 58, in __call__
    metadata["widgets"][WIDGET_STATE_MIMETYPE]["state"]
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^
KeyError: 'state'

```

程序会出现上述错误的原因是 ipynb 文件中存在一些 widgets 控件，这些控件存在的目的是增加文件的可交互性。但有时即使开发者并没有添加这些控件，控件依然会被加入文件中。（如从 Google Colab 下载脚本文件时，会自动添加控件）

此时使用如下命令去除控件信息，然后再进行导出：

```
# 去除控件信息
jq -M 'del(.metadata.widgets)'  main.ipynb > main_rm.ipynb
# 转换导出
jupyter nbconvert --to html main_rm.ipynb
```

这里的 `main.ipynb` 和 `main_rm.ipynb` 需要你在使用时替换成自己的文件名。现在，在当前文件夹下就会有一个名叫 `main_rm.ipynb` 的新文件生成了。

> 参考链接：https://github.com/jupyter/nbconvert/issues/1731
