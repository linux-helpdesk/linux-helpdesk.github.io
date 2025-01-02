---
title: Linux 硬盘测速 
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

![硬盘测速](/assets/images/linux_disk_speedtest.png)

1. 在待测硬盘（或优盘）路径下新建 [testDiskSpeed.py](http://link.zhihu.com/?target=http%3A//testdiskspeed.py/) 文件
2. 复制粘贴以下代码
3. 命令行终端切换至硬盘路径下并运行 `sudo python3 testDiskSpeed.py`

```python
#!/usr/bin/env python3

import os

bs_list_K = ['1', '2', '4', '8', '16', '32', '64', '128', '256', '512']

bs_list_M = ['1', '2', '4', '8', '12', '16', '24', '32', '48', '64']

print("\n传输大小：1KB 到 512KB")
print("文件大小：5MB")
print("测试中，请耐心等待...")
sum = 5
for bs in bs_list_K:
    count = int(sum*1024/int(bs))
    in_result = os.popen("dd if=/dev/zero of=test.dd oflag=direct bs="+str(bs)+"K count="+str(count)+" 2>&1").read()
    in_result = in_result.split("\n")[-2].split(",")[-1]
    out_result = os.popen("dd if=test.dd of=/dev/null iflag=direct bs="+str(bs)+"K count="+str(count)+" 2>&1").read()
    out_result = out_result.split("\n")[-2].split(",")[-1]
    print(bs+" KB\t"+"写入: "+in_result+"\t读取: "+out_result)
        
print("\n传输大小：1MB 到 64MB")
print("文件大小：128MB")
print("测试中，请耐心等待...")
sum = 128
for bs in bs_list_M:
    count = int(sum/int(bs))
    in_result = os.popen("dd if=/dev/zero of=test.dd oflag=direct bs="+str(bs)+"M count="+str(count)+" 2>&1").read()
    in_result = in_result.split("\n")[-2].split(",")[-1]
    out_result = os.popen("dd if=test.dd of=/dev/null iflag=direct bs="+str(bs)+"M count="+str(count)+" 2>&1").read()
    out_result = out_result.split("\n")[-2].split(",")[-1]
    print(bs+" MB\t"+"写入: "+in_result+"\t读取: "+out_result)

os.system("rm test.dd")
```
