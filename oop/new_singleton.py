import threading


class Singleton(object):
    _instance_lock = threading.Lock()
    _initialized = False  # 是否初始化完成

    def __init__(self):
        # 对象的初始化: 对__new__返回的对象进行初始化, 设置属性、执行逻辑
        if not Singleton._initialized:
            print("Singleton init")
            Singleton._initialized = True

    def __new__(cls, *args, **kwargs):
        # 创建类的实例: 分配内存, 返回新对象
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):

                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


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
