import os
import time
from multiprocessing import Process
from threading import Thread


def thread_func(name, i):
    time.sleep(2)
    print(f'{name}.{i}号子线程运行了!')


def process_func(name):
    time.sleep(2)
    print(f'{name}号子进程运行了!')
    # 在子进程中，开启多线程
    for i in range(3):
        t = Thread(target=thread_func, args=(name, f'{i}',))
        t.start()


class Human(object):
    def watch(self):
        for i in range(3):
            print("看电视....", os.getpid())
            time.sleep(1)

    def drink(self, food):
        for i in range(3):
            print(f"喝{food}....",os.getpid())
            time.sleep(1)

    def eat(self, food):
        for i in range(3):
            print(f"吃{food}....", os.getpid())
            time.sleep(1)


def human_action():
    xiaoming = Human()
    watch_thread = Thread(target=xiaoming.watch)
    drink_thread = Thread(target=xiaoming.drink, kwargs={"food": "羊汤"})
    eat_thread = Thread(target=xiaoming.eat, args=("米饭", ))

    watch_thread.start()
    drink_thread.start()
    eat_thread.start()


if __name__ == '__main__':
    # 先开启多进程
    for i in range(3):
        t = Process(target=process_func, args=(f'{i}',))
        t.start()

    # 面向对象的方式开启多线程
    human_action()
