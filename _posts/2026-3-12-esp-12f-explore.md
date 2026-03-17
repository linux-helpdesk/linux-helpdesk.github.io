---
title: 硬件逆向：深度探索基于 ESP-12F 的红外开发板与 REZO 风扇破解
author: "Zhao Zilong"
date: 2024-10-28
category: Linux
layout: post
---

在本篇博文中，我们将记录一次完整的硬件逆向与协议破解过程。目标是使用一块基于 **ESP-12F (ESP8266)** 的红外开发板，通过固件烧录、引脚探测、信号捕获，最终实现对马来西亚 **REZO** 品牌风扇的红外控制破解。

------

## 一、 硬件信息查看及固件刷入

在进行任何软件层面的操作前，首先需要确认硬件状态并刷入支持 Python 交互的 MicroPython 固件。

### 1. 硬件准备与连接

首先拿到板子，样子如下：

![ESP8266 with IR RX](https://linux-helpdesk.github.io/assets/images/ESP-12F.jpeg)

**进入刷机模式：**

1. 使用跳线短接左下角的 **IO0** 和 **GND**。
2. 使用 **USB 转 TTL** 模块（如 CH340 或 CP2102）连接电脑与开发板。

### 2. 读取 Flash 信息

安装 `esptool` 工具并运行以下命令查看设备容量，确保连通性：

```
# 安装 esptool
$ pip install esptool
...
# 查看 Flash ID
$ python3 -m esptool --port /dev/ttyUSB0 flash_id
Warning: Deprecated: Command 'flash_id' is deprecated. Use 'flash-id' instead.
esptool v5.2.0
Connected to ESP8266 on /dev/ttyUSB0:
Chip type:          ESP8266EX
Features:           Wi-Fi, 160MHz
Crystal frequency:  26MHz
MAC:                48:3f:da:c4:70:02

Stub flasher running.

Flash Memory Information:
=========================
Manufacturer: c4
Device: 6016
Detected flash size: 4MB

Hard resetting via RTS pin...
```

**输出参考：**

> Chip type: ESP8266EX
>
> Detected flash size: **4MB**

### 3. 固件烧录

根据获取到的 4MB 容量数据，我们选择刷入 [v1.22.2](https://micropython.org/resources/firmware/ESP8266_GENERIC-20240222-v1.22.2.bin) 版本的 MicroPython 固件。

```bash
$ python3 -m esptool --port /dev/ttyUSB0 --chip esp8266 --baud 115200 write-flash --flash-mode dout --flash-size 4MB 0x0 ESP8266_GENERIC-20240222-v1.22.2.bin
esptool v5.2.0
Connected to ESP8266 on /dev/ttyUSB0:
Chip type:          ESP8266EX
Features:           Wi-Fi, 160MHz
Crystal frequency:  26MHz
MAC:                48:3f:da:c4:70:02

Stub flasher is already running. No upload is necessary.

Configuring flash size...
Flash parameters set to 0x0340.
Flash will be erased from 0x00000000 to 0x0009cfff...
Wrote 642080 bytes (426777 compressed) at 0x00000000 in 38.1 seconds (135.0 kbit/s).
Hash of data verified.

Hard resetting via RTS pin...
```

### 4. 交互式命令行测试

使用 `picocom` 进入交互式终端（REPL），测试固件是否运行正常：

```bash
# 安装 picocom
$ sudo apt install picocom
...
# 连接串口
$ picocom /dev/ttyUSB0 -b 115200

port is        : /dev/ttyUSB0
flowcontrol    : none
baudrate is    : 115200
parity is      : none
databits are   : 8
stopbits are   : 1
escape is      : C-a
local echo is  : no
noinit is      : no
noreset is     : no
hangup is      : no
nolock is      : no
send_cmd is    : sz -vv
receive_cmd is : rz -vv -E
imap is        :
omap is        :
emap is        : crcrlf,delbs,
logfile is     : none
initstring     : none
exit_after is  : not set
exit is        : no

Type [C-a] [C-h] to see available commands
Terminal ready

# 此时按下回车进入命令行
>>> print("Hello")
Hello
```

------

## 二、 进一步探索端口功能

由于是通用开发板，我们需要通过逻辑探测确定红外发射、接收以及 LED 灯所对应的 GPIO 引脚。

### 1. 红外发送端口和指示灯端口

运行以下扫描脚本，通过循环控制电平变化来观察硬件反应。

**注意：** 红外光肉眼不可见，需通过手机摄像头观察发光二极管是否有闪烁。

```python
from machine import Pin
import time

# 常见的 ESP8266 GPIO 引脚列表
pins = [0, 2, 4, 5, 12, 13, 14, 15]

for p in pins:
    print("正在测试引脚: GPIO", p)
    test_pin = Pin(p, Pin.OUT)
    # 快速交替产生高低电平
    for _ in range(10):
        test_pin.value(1)
        time.sleep(0.5)
        test_pin.value(0)
        time.sleep(0.05)
    time.sleep(0.5)
```

**测试结论：**

- **GPIO 2**：板载蓝色指示灯。
- **GPIO 4**：红外发射二极管。

### 2. 信号接收端口探测

红外接收头在没有信号时通常保持高电平，接收到信号时会产生跳变。我们重点怀疑 GPIO 5 或 14。

```python
from machine import Pin
import time

# 排除掉发射引脚 4 和蓝灯引脚 2，尝试最可能的 GPIO 14
target_pin = 14 

rx = Pin(target_pin, Pin.IN, Pin.PULL_UP)

print(f"验证 GPIO {target_pin} ... 当前状态: {rx.value()}")

if rx.value() == 0:
    print(f"警告：GPIO {target_pin} 当前就是低电平，可能不是接收头，或者有干扰。")

print("请按遥控器测试...")

count = 0
while count < 20:
    if rx.value() == 0:
        print("检测到电平跳变！")
        count += 1
        time.sleep(0.05) # 避开单次脉冲的多次触发
```

**测试结论：**

- **GPIO 14**：红外接收装置。

------

## 三、 捕获与破解信号

确定引脚后，我们需要捕获遥控器发出的原始脉冲数据。

### 1. 基础信号捕获

通过记录电平翻转的时间间隔（微秒），获取原始脉冲序列。

```python
import machine
import time

# 设置接收引脚
rx_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

def capture_ir():
    print("等待红外信号...（按下遥控器）")

    # 等待信号开始（平时是1，收到信号变0）
    while rx_pin.value() == 1:
        pass

    # 记录时间轴
    timestamps = []
    last_val = 0
    start_time = time.ticks_us()

    # 持续捕获一段时间的电平变化
    for _ in range(200):
        # 等待电平翻转
        while rx_pin.value() == last_val:
            # 如果太久没变化，说明信号结束了
            if time.ticks_diff(time.ticks_us(), start_time) > 100000:
                break

        curr_time = time.ticks_us()
        duration = time.ticks_diff(curr_time, start_time)
        timestamps.append(duration)

        start_time = curr_time
        last_val = rx_pin.value()

        if duration > 50000: # 信号超时退出
            break

    print("捕获完成！原始脉冲数据（微秒）:")
    print(timestamps)

# 执行捕获
capture_ir()
```

### 2. 发送信号与暴力尝试 (REZO 风扇)

针对马来西亚 **REZO** 风扇，由于其协议可能存在特殊的载波频率（33kHz 或 38kHz）和逻辑极性，我们编写了一个自动化脚本进行暴力破解尝试。

```python
import machine
import time
import gc

# 硬件配置
TX_PIN_OBJ = machine.Pin(4, machine.Pin.OUT, value=0)
RX_PIN_OBJ = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
machine.freq(160000000) # 必须保持最高速运行

def record_signal():
    """高采样率录制"""
    print("\n[等待录制] 请按遥控器...")
    while RX_PIN_OBJ.value() == 1: pass
    
    state = machine.disable_irq()
    data = []
    start = time.ticks_us()
    level = 0
    # 扩大采样深度到 300，应对长协议
    for _ in range(300):
        ps = time.ticks_us()
        while RX_PIN_OBJ.value() == level:
            if time.ticks_diff(time.ticks_us(), ps) > 100000: break
        now = time.ticks_us()
        data.append(time.ticks_diff(now, start))
        start = now
        level = 1 - level
        if data[-1] > 50000: break
    machine.enable_irq(state)
    return data

def precise_manual_send(pulses, freq_hz):
    """
    极致优化版手动载波发送
    通过局部变量减少对象查找耗时
    """
    pin_v = TX_PIN_OBJ.value
    t_us = time.ticks_us
    t_diff = time.ticks_diff
    # 计算半周期：例如 38kHz 对应约 13us
    half_period = 500000 // freq_hz 
    
    state = machine.disable_irq()
    try:
        # 连发 3 次
        for _ in range(3):
            for i, duration in enumerate(pulses):
                if i % 2 == 0: # 信号位：手动产生震荡
                    p_start = t_us()
                    while t_diff(t_us(), p_start) < duration:
                        pin_v(1)
                        # 这里微调延时补偿 Python 执行开销
                        time.sleep_us(half_period - 2) 
                        pin_v(0)
                        time.sleep_us(half_period - 2)
                else: # 间隔位：静默
                    pin_v(0)
                    time.sleep_us(duration)
            
            # 帧间隔 40ms
            pin_v(0)
            machine.enable_irq(state)
            time.sleep_ms(40)
            state = machine.disable_irq()
    finally:
        pin_v(0)
        machine.enable_irq(state)

def start_brute_force(data):
    # 频率列表：REZO 可能是 33k 或 38k
    # 极性列表：同时测试采集到的原始逻辑和反转逻辑
    for f in [33000, 38000]:
        print(f"--- 尝试频率: {f/1000}kHz ---")
        
        # 模式1：原始极性
        print("模式: 原始极性发送")
        precise_manual_send(data, f)
        time.sleep(1.5)
        
        # 模式2：反转极性 (将第一个脉冲当做间隔)
        if len(data) > 1:
            print("模式: 反转极性发送")
            precise_manual_send(data[1:], f)
            time.sleep(1.5)

# --- 主程序 ---
print("="*30)
print("REZO 风扇手动控制终端已就绪")
print("="*30)

while True:
    raw_pulses = record_signal()
    if len(raw_pulses) > 30:
        print(f"录制成功！脉冲数: {len(raw_pulses)}")
        print(f"特征前8位: {raw_pulses[:8]}")
        
        print("3秒后开始重放破解...")
        time.sleep(3)
        start_brute_force(raw_pulses)
        print("\n[破解结束] 请观察风扇反应。")
    else:
        print("录制数据太短，请靠近接收头重试。")
    time.sleep(1)
```

**测试结果：**

经测试，在 **33K 和 38K** 频率下使用**原始极性**都可以成功触发风扇响应。

------

## 四、 整理：REZO 风扇专用发送程序

基于上述实验，我们将成功触发“关闭”指令的原始脉冲数据进行固化，编写了一个精简的控制程序。

```python
import machine
import time

# --- 硬件固定配置 ---
TX_PIN_OBJ = machine.Pin(4, machine.Pin.OUT, value=0)
machine.freq(160000000)

# --- REZO 风扇关闭指令原始脉冲数据 ---
REZO_POWER_OFF = [8920, 4470, 658, 543, 658, 479, 673, 493, 601, 548, 658, 493, 601, 543, 658, 494, 600, 1720, 600, 1670, 601, 1670, 658, 1688, 551] 

def send_command(pulses, freq_hz=38000):
    """极致精简的专用发送函数"""
    pin_v = TX_PIN_OBJ.value
    t_us = time.ticks_us
    t_diff = time.ticks_diff
    half_period = 500000 // freq_hz - 2 # 补偿 Python 执行开销
    
    state = machine.disable_irq()
    try:
        # 连发 3 次以确保 100% 成功率
        for _ in range(3):
            start_frame = t_us()
            for i, duration in enumerate(pulses):
                if i % 2 == 0: # 发光位
                    p_start = t_us()
                    while t_diff(t_us(), p_start) < duration:
                        pin_v(1)
                        time.sleep_us(half_period)
                        pin_v(0)
                        time.sleep_us(half_period)
                else: # 间隔位
                    pin_v(0)
                    time.sleep_us(duration)
            
            pin_v(0)
            # 允许中断短暂恢复，处理系统后台任务
            machine.enable_irq(state)
            time.sleep_ms(40) 
            state = machine.disable_irq()
    finally:
        pin_v(0)
        machine.enable_irq(state)

# --- 测试调用 ---
print("正在执行 REZO 风扇关闭指令...")
send_command(REZO_POWER_OFF, 38000)
print("指令已发送。")
```

通过这一流程，我们成功实现了从零开始的硬件分析与红外协议重放。
