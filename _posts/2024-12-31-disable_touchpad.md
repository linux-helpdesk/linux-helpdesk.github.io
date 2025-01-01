---
title: Linux 打字时禁用触摸板 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
sudo apt install libinput-tools xinput
libinput list-devices
```

自动化并设置开机启动 `vim /etc/profile.d/disable_touchpad.sh`

> #!/bin/bash
>
> xinput set-prop “ELAN1204:00 04F3:30B2 Touchpad” “libinput Disable While Typing Enabled” 1
