"""
守护进程（Daemon Process）也叫精灵进程，是一种特殊的进程，一般在后台运行，不与任何控制终端相关联，
并且周期性地执行某种任务或等待处理某些发生的事件（一般用于处理一些系统级的任务）
基本特点：
1. 生存周期长[非必须]，一般启动了以后就会一直驻留在操作系统中，直到主进程结束。
2. 主进程创建了守护进程以后，守护进程作为一个特殊的子进程会随着主进程的代码结束而自动结束。
3. 守护进程内不允许再开子进程（孙子进程）。
4. 守护进程是在后台运行，和终端无关联，不会占着终端，终端可以执行其他命令或操作，终端退出，也不会导致守护进程退出，也因此守护进程中所有关于IO的操作都不能通过终端来完成。
"""
import time
from multiprocessing import Process


def mydaemon():
    while True:
        print("daemon is alive!")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=mydaemon)
    # 如果不设置为守护进程，主进程结束后，子进程还会继续执行
    p.daemon = True  # 设置当前子进程为守护进程，必须写在start()方法之前
    p.start()
    time.sleep(5)