---
title: Kivy 调试（打包后软件闪崩） 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

首先，根据[这个链接](http://link.zhihu.com/?target=https%3A//www.codenong.com/cs106517353/)并未在软件目录下找到 `.kivy` 文件夹。

故根据[第二条链接](http://link.zhihu.com/?target=https%3A//kev-dev.medium.com/testing-your-application-using-kivy-launcher-15601aacb764)使用 `Kivy Launcher` 调试，不要忘记在 `kivy/myapp` 目录下创建 `android.txt` 文件，否则不会显示。

在软件内启动工程，根据[这条链接](http://link.zhihu.com/?target=https%3A//stackoverflow.com/questions/22733951/logs-generated-when-launching-an-app-in-kivy-launcher-on-android)使用 `adb logcat` 或者 `buildozer android logcat` 实时打印日志，最好在运行软件之前提前清理手机后台。

```text
11-22 01:54:12.133 31985 32065 I libSDL  : Physical screen resolution is 1080x2300
11-22 01:54:12.134 31985 32065 I python  : Initialize Python for Android
11-22 01:54:12.154 31985 32065 I python  : ['/data/user/0/org.kivy.pygame/files/lib/python2.7/site-packages', '/data/user/0/org.kivy.pygame/files/lib/site-python']
11-22 01:54:12.155 31985 32065 I python  : Android path ['/data/user/0/org.kivy.pygame/files/lib/python27.zip', '/data/user/0/org.kivy.pygame/files/lib/python2.7', '/data/user/0/org.kivy.pygame/files/lib/python2.7/lib-dynload', '/data/user/0/org.kivy.pygame/files/lib/python2.7/site-packages', '/storage/emulated/0/kivy/myapp', '/data/user/0/org.kivy.pygame/files/lib/python2.7/site-packages/PIL']
11-22 01:54:12.155 31985 32065 I python  : Android kivy bootstrap done. __name__ is __main__
11-22 01:54:12.155 31985 32065 I python  : Run user program, change dir and execute main.py
11-22 01:54:12.156 31985 32065 I python  : Traceback (most recent call last):
11-22 01:54:12.156 31985 32065 I python  :   File "main.py", line 1, in <module>
11-22 01:54:12.156 31985 32065 I python  :     from kivymd.app import MDApp
11-22 01:54:12.156 31985 32065 I python  : ImportError: No module named kivymd.app
11-22 01:54:12.158 31985 32065 I python  : Python for android ended.
11-22 01:54:12.158 31985 32065 I y.pygame:pytho: System.exit called, status: 0
```

其中，`ImportError: No module named kivymd.app` 是关键。

进入项目目录查看 `buildozer.spec` 文件内 `requirments` 选项，加入 `kivymd` 后重新编译。（加入所有非自定义的系统包，如果是使用 `kivymd` 编写的，还需要加入 `pillow` 包或者 `PIL` 包，输入 Ipython 看哪个能 import，否则会报 `no module named PIL`）
