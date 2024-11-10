"""
孤儿进程：父进程退出，子进程还在运行，子进程会被操作系统托管给init进程，init进程会负责回收子进程的资源

ps aux | grep 10_orphan_process
kill -9 主进程PID
# 子进程变成一个还在运行的孤儿进程
ps aux | grep 10_orphan_process
"""
import os
import time
from multiprocessing import Process


def func():
    print(f"子进程的pid={os.getpid()}")
    time.sleep(60)
    print("hello")


if __name__ == '__main__':
    print(f"主进程的pid={os.getpid()}")
    p = Process(target=func)
    p.daemon = True
    p.start()
    time.sleep(15)
