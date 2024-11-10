from threading import Thread


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None):
        super().__init__(group, target, name,
                         args, kwargs)
        self.name = name

    def run(self):
        """run里面编写线程运行时要执行的任务代码"""
        print(f"{self.name}线程运行前!")
        super().run()
        print(f"{self.name}线程运行后!")


def func():
    print("子线程要执行的任务代码")


def extend_thread_class():
    t = MyThread(name="1号", target=func)
    t.start()


if __name__ == '__main__':

    # 继承Thread类开启多线程
    extend_thread_class()
