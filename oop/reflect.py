import sys


class Person:
    num = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.num += 1

    def walk(self):
        print("walking....")


def talk(self):
    print(self.name, "is speaking.....")


def num():
    return Person.num


class User:
    def login(self):
        print('欢迎来到登录页面')

    def register(self):
        print('欢迎来到注册页面')

    def save(self):
        print('欢迎来到存储页面')


print(__name__)  # __main__ 就代表模块本身

if __name__ == '__main__':
    p = Person("Alex", 22)
    # 反射、映射、自省
    # 判断属性是否存在
    if hasattr(p, "name"):
        # 获取属性
        print("name: ", getattr(p, "name"))
        print("age: ", getattr(p, "age"))

    # 增加实例属性
    setattr(p, "sex", "Female")
    print("sex: ", p.sex)

    # 实例方法
    setattr(p, "speak", talk)
    p.speak(p)
    # 类方法
    setattr(Person, "person_num", num)
    print("person_num: ", Person.person_num())

    # 删除属性
    delattr(p, "age")
    if hasattr(p, "age"):
        print("age: ", p.age)
    else:
        print("age is deleted")
    print(p.__dict__)

    for k, v in sys.modules.items():
        print(k, v)

    # print(sys.modules["__main__"])
    mod = sys.modules[__name__]
    if hasattr(mod, "p"):
        o = getattr(mod, "p")
        print(o)

    u = User()
    while True:
        user_cmd = input(">>:").strip()
        if hasattr(u, user_cmd):
            func = getattr(u, user_cmd)
            func()
