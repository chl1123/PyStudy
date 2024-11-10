"""
fork创建进程
    1. fork()函数调用一次，返回两次，操作系统会把当前进程（父进程）复制一份（子进程），然后分别在父进程和子进程中返回
    2. 因此fork也是分叉的意思
    3. 即使fork在方法内执行，但是fork后父进程和子进程将会继续执行fork后的代码（不只是调用fork的方法），而是直到进程结束
"""
import os


def fork_demo():
    # 通过fork创建一个子进程
    w = 100
    pid = os.fork()  # 此处子进程中pid=0，而在父进程中pid > 0；因为父进程中执行了fork，得到子进程的pid作为返回值
    print(f'1. 当前进程PID: {os.getpid()}')
    if pid == 0:
        print(f'2. [Child]|w={w}, 子进程PID={os.getpid()}，当前子进程的父进程PID={os.getppid()}')
    else:
        print(f'2. [Parent]|父进程PID：{os.getpid()}，创建的子进程，PID={pid}')


if __name__ == '__main__':
    print("---------------fork create process-----------------")
    fork_demo()
    print("--------------process: " + str(os.getpid()) + " end----------------------")
    print()

"""
---------------fork create process-----------------
1. 当前进程PID: 41848
2. [Parent]|父进程PID：41848，创建的子进程，PID=41854
--------------process: 41848 end----------------------

1. 当前进程PID: 41854
2. [Child]|w=100, 子进程PID=41854，当前子进程的父进程PID=41848
--------------process: 41854 end----------------------

"""
