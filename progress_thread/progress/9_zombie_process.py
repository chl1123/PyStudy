"""
僵尸进程：子进程结束后，父进程没有回收子进程的资源，导致子进程成为僵尸进程
"""

import time
import multiprocessing


def func():
    print("子进程执行了")
    exit()


if __name__ == '__main__':
    process = multiprocessing.Process(target=func)
    process.start()  # 创建进程
    time.sleep(30)
