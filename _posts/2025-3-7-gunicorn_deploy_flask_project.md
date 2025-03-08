---
title: 使用 Gunicorn 部署 Flask 项目
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在开发完一个 Flask 项目后，将其部署到生产环境是确保应用可用性和性能的关键步骤。本文将介绍如何使用 Gunicorn 部署已开发好的 Flask 项目，并探讨在 `app.py` 文件中预先配置端口的影响，以及 `app:app` 中两个 `app` 的含义。此外，我们还将讨论如何更改应用实例的名称。

### 什么是 Gunicorn？

Gunicorn，全称 **Green Unicorn**，是一个用于 UNIX 系统的 Python WSGI（Web 服务器网关接口）HTTP 服务器。它能够将应用程序与 Web 服务器连接起来，处理并发请求，提高应用的性能和稳定性。

### 部署步骤

1. **安装 Gunicorn：**

   首先，确保您的环境中已安装 Flask。然后，使用以下命令安装 Gunicorn：

   ```bash
   pip install gunicorn
   ```

2. **创建 Flask 应用：**

   假设您已经有一个名为 `app.py` 的 Flask 应用，其内容如下：

   ```python
   from flask import Flask

   app = Flask(__name__)

   @app.route('/')
   def hello():
       return 'Hello, World!'

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=5000)
   ```

   在上述代码中，`app` 是 Flask 应用实例，`app.run()` 用于在开发环境中启动内置服务器，监听 `0.0.0.0:5000`。

3. **使用 Gunicorn 启动 Flask 应用：**

   在生产环境中，推荐使用 Gunicorn 等 WSGI 服务器来托管应用。使用以下命令启动应用：

   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

   其中，`-w 4` 指定使用 4 个工作进程，`-b 0.0.0.0:8000` 指定绑定地址和端口，`app:app` 表示从 `app.py` 模块中导入名为 `app` 的 Flask 应用实例。

### 关于 `app:app` 的含义

在 `gunicorn -w 4 -b 0.0.0.0:8000 app:app` 命令中，`app:app` 的含义如下：

- **第一个 `app`：** 指模块名称，即 `app.py` 文件（不包含 `.py` 后缀）。

- **第二个 `app`：** 指模块中定义的 Flask 应用实例名称。

因此，`app:app` 告诉 Gunicorn 从 `app.py` 文件中导入名为 `app` 的 Flask 应用实例。

### 更改应用实例名称

如果您希望将应用实例名称从默认的 `app` 更改为其他名称，例如 `my_application`，可以按照以下步骤进行：

1. **修改应用实例名称：**

   在您的 `app.py` 文件中，将 Flask 应用实例从默认的 `app` 更改为其他名称，例如 `my_application`：

   ```python
   from flask import Flask

   my_application = Flask(__name__)

   @my_application.route('/')
   def hello():
       return 'Hello, World!'

   if __name__ == '__main__':
       my_application.run(host='0.0.0.0', port=5000)
   ```

2. **使用 Gunicorn 部署应用：**

   在终端中，使用以下命令启动 Gunicorn，并指定新的应用实例名称：

   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:my_application
   ```

   在此命令中：

   - `-w 4`：指定使用 4 个工作进程。

   - `-b 0.0.0.0:8000`：指定绑定地址和端口。

   - `app:my_application`：`app` 是模块名（即 `app.py`），`my_application` 是在模块中定义的 Flask 应用实例名称。

通过上述步骤，您可以将 Flask 应用实例名称更改为其他名称，并使用 Gunicorn 部署应用。请确保在启动 Gunicorn 时，使用正确的模块名和应用实例名称，以确保应用正常运行。

### 关于在 `app.py` 中预先配置端口

在开发环境中，通常使用 `app.run()` 方法启动 Flask 内置服务器，并指定主机和端口，如上例中的 `app.run(host='0.0.0.0', port=5000)`。然而，在生产环境中，使用 Gunicorn 等 WSGI 服务器时，**无需**在 `app.py` 中调用 `app.run()`。这是因为 Gunicorn 会自行管理服务器的启动和端口绑定。使用 Gunicorn 启动网页后，`app.py` 中对端口的配置会被直接覆盖。

因此，当使用 Gunicorn 部署时，您只需确保在 `app.py` 中定义了 Flask 应用实例，而不需要调用 `app.run()`。然后，通过命令行指定 Gunicorn 的绑定地址和端口，例如：

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

在此命令中，`-b 0.0.0.0:8000` 指定了 Gunicorn 监听的地址和端口。这样，Gunicorn 将在指定的端口上启动服务器，而无需在 `app.py` 中额外指定端口。

### 总结

通过上述步骤，您可以使用 Gunicorn 将已开发好的 Flask 项目部署到生产环境。在生产环境中，建议避免在 `app.py` 中调用 `app.run()`，而是通过 Gunicorn 的命令行参数来管理服务器的启动和端口绑定。此外，理解 `app:app` 中两个 `app` 的含义，有助于正确配置和启动您的 Flask 应用。
