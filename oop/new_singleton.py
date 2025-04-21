import threading


class Singleton(object):
    _instance_lock = threading.Lock()
    _initialized = False  # 是否初始化完成

    def __new__(cls, *args, **kwargs):
        # 创建类的实例: 分配内存, 返回新对象
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

    def __init__(self):
        # 对象的初始化: 对__new__返回的对象进行初始化, 设置属性、执行逻辑
        if not Singleton._initialized:
            print("Singleton init")
            Singleton._initialized = True

class MutilSingleton:
    _instances = {}
    _instance_lock = threading.Lock()

    def __new__(cls, id_, *args, **kwargs):
        if id_ not in MutilSingleton._instances:
            with MutilSingleton._instance_lock:
                if id_ not in MutilSingleton._instances:
                    instance = object.__new__(cls)
                    MutilSingleton._instances[id_] = {"instance": instance, "init": False}
        return MutilSingleton._instances[id_]["instance"]

    def __init__(self, id_):
        if self._instances[id_]["init"] is False:
            print(id_ + " init")
            self._instances[id_]["init"] = True
            self.client = "client_" + id_

    def get_client(self):
        return self.client

def singleton_example():
    # 类() 先执行__new__方法，再执行__init__方法
    obj1 = Singleton()
    obj2 = Singleton()
    print(obj1, obj2)

    def task(arg):
        obj = Singleton()
        print(obj)

    for i in range(10):
        t = threading.Thread(target=task, args=[i, ])
        t.start()

def mutil_singleton_example():
    obj1 = MutilSingleton("1")
    obj2 = MutilSingleton("1")
    obj3 = MutilSingleton("2")
    print(obj1, obj2, obj3)
    print(obj1.get_client(), obj2.get_client(), obj3.get_client())

if __name__ == '__main__':
    mutil_singleton_example()