---
title: XRDP 在 Ubuntu 20 和 22 上没有声音 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
sudo apt install build-essential dpkg-dev libpulse-dev git autoconf libtool
cd ~
git clone https://github.com/neutrinolabs/pulseaudio-module-xrdp.git
cd ~/pulseaudio-module-xrdp
scripts/install_pulseaudio_sources_apt_wrapper.sh
# This process will take a very long period of time, to check the process, use the following commands:
# tail -f /var/tmp/pa-build-root-debootstrap.log
# and 
# tail -f /var/tmp/pa-build-root-schroot.log
./bootstrap && ./configure PULSE_DIR=~/pulseaudio.src
make 
make install
ls $(pkg-config --variable=modlibexecdir libpulse) | grep xrdp
```
