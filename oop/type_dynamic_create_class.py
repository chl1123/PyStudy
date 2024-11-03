class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("Alex", 22)

print(type(p))
print(type(Person))


# 定义Dog类的__init__方法
def __init__(self, name, age):
    self.name = name
    self.age = age


# 使用type函数动态创建Dog类
# role是类属性，值为"dog"
# __init__是类初始化方法，值为上面定义的__init__方法
Dog = type("Dog", (object,), {"role": "dog", "__init__": __init__})

print(Dog)

# 创建Dog类的实例
d = Dog("jhs", 2)
print(d.role, d.name, d.age)
print(Dog)
