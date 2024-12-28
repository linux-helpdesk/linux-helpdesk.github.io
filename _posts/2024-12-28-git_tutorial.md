---
title: GitHub 密钥生成及配置
author: "Zhao Zilong"
date: 2024-12-28
category: Linux
layout: post
---

本文主要分为以下三个部分：
  - 开发者密钥生成
  - 密钥的使用方法
  - 本地项目配置方法

## 开发者密钥生成

依次完成如下步骤：
  - 登录 GitHub 后点击右上角头像
  - 点击 `Settings`
  - 在新页面左侧菜单栏点击 `Developer settings`
  - 点击 `Personal access tokens`
  - 选择 `Tokens (classic)`
  - 右上角点击 `Generate new token`
  - 按照提示选择密钥权限并保存好密钥

## 密钥的使用方法

在将项目 `git pull` 到本地并完成修改后使用 `git push` 命令时，按照要求输入用户名和密钥即可。

## 本地项目配置方法

为实现每次 `git push` 后自动提交不用每次输入密码的功能，我们需要使用 `set-url` 命令。
首先查看当前项目对应的 GitHub Url：
```bash
git remote -v 
```
然后将密钥加入原 Url 并使用 `set-url` 命令更改 Url：
```bash
git remote set-url origin https://[key]@[原 URL]
```
现在再次使用 `git push` 功能就会自动提交无需输入密码了。
