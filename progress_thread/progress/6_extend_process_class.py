"""
p.start()
    在父进程中开启子进程，并执行子进程的run方法
"""
import os
from multiprocessing import Process


class MyProcess(Process):
    """自定义进程类"""

    def __init__(self, target, name, *args, **kwargs):
        # 父类初始化
        super().__init__(target=target, *args, **kwargs)
        # 自定义参数
        self.name = name

    def run(self):
        """run必须有，但是run中的代码可以根据自己的需要来编写"""
        print(f"process: {self.name}, id: {os.getpid()}, run", )
        super().run()


def func():
    print("child process func() ...")


if __name__ == '__main__':
    p1 = MyProcess(target=func, name='1号')
    p2 = MyProcess(target=func, name='2号')
    p3 = MyProcess(target=func, name='3号')

    p1.start()  # 启动进程，会自动调用run方法
    # p1.run() 也可以启动进程，但是工作中，我们一定要使用start()
    p2.start()
    p3.start()

    print("main process end")