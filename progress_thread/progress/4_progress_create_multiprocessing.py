"""
进程的创建
"""
import multiprocessing
import os
import time


def watch():
    print("watch id: ", id(watch))
    for i in range(3):
        print("子进程....", os.getpid())
        time.sleep(1)


def multiprocessing_demo():
    # 进程操作对象 = multiprocessing.Process(target=任务）
    # 任务可以是一个函数，也可以是一个方法
    print("[Parent]|pid: ", os.getpid())
    print("watch id: ", id(watch))
    # 在windows中，不能放在全局中执行；因为windows通过import当前模块的方式创建子进程，放在全局中会循环调用
    # 相当于在此处 import 4_progress_create_multiprocessing
    process = multiprocessing.Process(target=watch)
    process.start()  # 创建进程


# windows下会调用两次
print("pid: ", os.getpid())

if __name__ == "__main__":
    multiprocessing_demo()

# linux: 通过fork创建子进程
"""
pid:  44781
[Parent]|pid:  44781
watch id:  140390422232800
watch id:  140390422232800
子进程.... 44787
子进程.... 44787
子进程.... 44787
"""

# windows: 通过import 当前模块的方式创建子进程，因此全局变量和函数会被调用2次
"""
pid:  92480
[Parent]|pid:  92480
watch id:  2652736526224
pid:  84268
watch id:  2376267424960
子进程.... 84268
子进程.... 84268
子进程.... 84268
"""

"""
linux和windows中watch id结果不一样
linux: 主进程和子进程watch id相同；因为linux通过fork创建子进程，子进程是父进程的拷贝
windows: 主进程和子进程watch id不同；因为windows通过import当前模块的方式创建子进程，相当于创建了一个新的进程
"""
