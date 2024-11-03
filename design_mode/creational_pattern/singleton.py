"""
单例
"""
import threading
import time


class Singleton0(object):
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    @staticmethod
    def instance():
        with Singleton0.__lock:
            if Singleton0.__instance is None:
                Singleton0.__instance = Singleton0()
        return Singleton0.__instance


class Singleton1(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(2)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton1, "_instance"):
            with Singleton1._instance_lock:
                if not hasattr(Singleton1, "_instance"):
                    Singleton1._instance = object.__new__(cls)
        return Singleton1._instance


def task():
    obj = Singleton0.instance()
    print(obj)
    obj1 = Singleton1()
    print(obj1)


for i in range(10):
    t = threading.Thread(target=task)
    t.start()
