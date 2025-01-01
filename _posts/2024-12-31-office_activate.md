---
title: Office 激活 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
546,575 views  Jul 29, 2023
1.官网下载 Office Deployment Tool 
https://www.microsoft.com/en-us/download/details.aspx?id=49117
2.配置config文件
https://config.office.com/deploymentsettings
导出 xml
3.安装
cd c:\office（文件夹目录）
setup.exe /download config.xml
setup.exe /configure config.xml
4.激活
cd C:\Program Files(x86)\Microsoft Office\Office16 
或者 cd C:\Program Files\Microsoft Office\Office16
cscript ospp.vbs /sethst:kms.03k.org 
cscript ospp.vbs /act
5.备选的KMS
kms.03k.org
kms.chinancce.com
kms.luody.info
kms.lotro.cc
kms.luochenzhimu.com
kms8.MSGuides.com
kms9.MSGuides.com
```

