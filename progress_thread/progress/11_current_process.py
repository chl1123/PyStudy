import os
import time
from multiprocessing import Process, current_process


def watch():
    p = current_process()
    print(f"当前进程名：{p.name}")
    print(f"当前进程名：{p.pid}")
    os.kill(os.getpid(), 9)  # 强制杀死进程
    # 不要直接在子进程中，使用exit()关闭当前进程，容易导致出现僵尸进程
    for i in range(3):
        print(f"进程{p.name}在看电视....", os.getpid())


if __name__ == '__main__':
    print("主进程", os.getpid())
    # 创建子进程
    # name 声明进程名
    p = Process(target=watch, name="watch")
    p.start()
    time.sleep(5)