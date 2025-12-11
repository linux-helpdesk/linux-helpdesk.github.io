---
title: 查看 Windows 远程桌面服务指纹信息
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

## SHA1 版本

在 `PowerShell` 中运行如下命令：

```powershell
wmic /namespace:\\root\cimv2\TerminalServices path Win32_TSGeneralSetting get SSLCertificateSHA1Hash               
```

## SHA256 版本

```powershell
# 连接本机 RDP 端口
$tcp = [Net.Sockets.TcpClient]::new("localhost", 56688)
$sslStream = New-Object System.Net.Security.SslStream($tcp.GetStream(), $false, ({$true}))
$sslStream.AuthenticateAsClient("localhost")
$cert = New-Object System.Security.Cryptography.X509Certificates.X509Certificate2 $sslStream.RemoteCertificate

# 导出到文件
$cert | Export-Certificate -FilePath C:\rdp.cer

# 查看 SHA-256 指纹
certutil -hashfile C:\rdp.cer SHA256
```
