---
title: Debian 蓝牙连接 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

当出现蓝牙设备断开后无法在再显示在列表中的情况

```bash
(base) ..[warren@debian] - [~] - [Sun Jul 28, 11:45]
..[$] <()> bluetoothctl scan on
Discovery started
[CHG] Controller D8:F2:CA:51:86:27 Discovering: yes
[NEW] Device 55:D5:3B:0B:26:DE 55-D5-3B-0B-26-DE
[NEW] Device 90:CC:DF:F7:35:F4 LAPTOP-NBFQM5ML
[NEW] Device AC:72:DD:08:08:DB net
[NEW] Device 44:D6:88:70:DF:EE 联想thinkplus-K30
[NEW] Device 49:6B:F3:C3:EB:DD 49-6B-F3-C3-EB-DD
^C%                                                                                            (base) ..[warren@debian] - [~] - [Sun Jul 28, 11:45]
..[$] <()> bluetoothctl pair 44:D6:88:70:DF:EE
Attempting to pair with 44:D6:88:70:DF:EE
[CHG] Device 44:D6:88:70:DF:EE Connected: yes
[CHG] Device 44:D6:88:70:DF:EE UUIDs: 0000110b-0000-1000-8000-00805f9b34fb
[CHG] Device 44:D6:88:70:DF:EE UUIDs: 0000110c-0000-1000-8000-00805f9b34fb
[CHG] Device 44:D6:88:70:DF:EE UUIDs: 0000110e-0000-1000-8000-00805f9b34fb
[CHG] Device 44:D6:88:70:DF:EE UUIDs: 0000111e-0000-1000-8000-00805f9b34fb
[CHG] Device 44:D6:88:70:DF:EE ServicesResolved: yes
[CHG] Device 44:D6:88:70:DF:EE Paired: yes
Pairing successful
```

