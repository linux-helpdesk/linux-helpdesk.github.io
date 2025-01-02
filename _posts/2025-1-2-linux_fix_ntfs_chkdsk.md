---
title: 在 Linux 上直接修复 NTFS 系统 —— CHKDSK.exe 替代品 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

```bash
ntfsfix /dev/sda4
```

例如：

```bash
$ sudo mount /dev/sda4 /mnt
$MFTMirr does not match $MFT (record 0).
Failed to mount '/dev/sda4': Input/output error
NTFS is either inconsistent, or there is a hardware fault, or it's a
SoftRAID/FakeRAID hardware. In the first case run chkdsk /f on Windows
then reboot into Windows twice. The usage of the /f parameter is very
important! If the device is a SoftRAID/FakeRAID then first activate
it and mount a different device under the /dev/mapper/ directory, (e.g.
/dev/mapper/nvidia_eahaabcc1). Please see the 'dmraid' documentation
for more details.
$ sudo ntfsfix /dev/sda4
Mounting volume... $MFTMirr does not match $MFT (record 0).
FAILED
Attempting to correct errors... 
Processing $MFT and $MFTMirr...
Reading $MFT... OK
Reading $MFTMirr... OK
Comparing $MFTMirr to $MFT... FAILED
Correcting differences in $MFTMirr record 0...OK
Processing of $MFT and $MFTMirr completed successfully.
Setting required flags on partition... OK
Going to empty the journal ($LogFile)... OK
Checking the alternate boot sector... OK
NTFS volume version is 3.1.
NTFS partition /dev/sda4 was processed successfully.
```
