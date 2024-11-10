"""
在当前程序中，基于pycharm来运行代码的时候，实际的运行流程：
1. pycharm调用了python解释器，实际上pycharm通过创建进程的方式来调用了python解释器的。
2. python解释器执行了python模块代码

在当前程序中，基于cmd命令来运行代码的时候，实际上的运行流程：
1. cmd终端调用了python解释器，实际上cmd终端通过创建进程的方式来调用了python解释器的。
2. python解释器执行了python模块代码
"""

import os
import time


if __name__ == '__main__':
    for i in range(60):
        time.sleep(1)  # 让程序睡1秒，也就是停顿1秒
        # os.getpid()  # 获取当前进程的PID
        # os.getppid() # 获取当前进程的父级（parent process）进程的PID
        print(i, os.getpid(), os.getppid())