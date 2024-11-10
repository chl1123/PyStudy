import multiprocessing
import os
import time


class Human(object):
    def watch(self):
        for i in range(3):
            print("看电视....", os.getpid())
            time.sleep(1)

    def drink(self, food):
        for i in range(3):
            print(f"喝{food}....", os.getpid())
            time.sleep(1)

    def eat(self, food):
        for i in range(3):
            print(f"吃{food}....", os.getpid())
            time.sleep(1)


if __name__ == '__main__':
    xiaoming = Human()
    print("主进程", os.getpid())
    watch_process = multiprocessing.Process(target=xiaoming.watch)
    drink_process = multiprocessing.Process(target=xiaoming.drink, kwargs={"food": "羊汤"})
    eat_process = multiprocessing.Process(target=xiaoming.eat, args=("米饭",))

    watch_process.start()
    drink_process.start()
    eat_process.start()
