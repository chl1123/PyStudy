"""
组合关系也是关联关系的特例，属于强聚合，本身也表示整体与部分的关系，但是组合关系中的整体和部分是不可分离的，整体生命周期的结束时也是部分的生命周期到头时。如人和大脑。
聚合和组合其实都是关联的特例，都是整体与部分的关系。它们的区别在于整体和部分是否可分离，聚合的两个对象之间是可分离的，且具有各自的生命周期，而组合的两个对象往往表现为一种同命相连的关系。
"""


class Person(object):
    def __init__(self):
        print("Person Iinitialization Start")
        # 组合关系在代码上体现为在整体类的构造方法中直接实例化成员类，因为类组合关系中整体与部分是共生的
        self.__brain = Brain()
        print("Person Iinitialization End")

    def run(self):
        print("Running...")


class Brain(object):
    def __init__(self):
        print("Brain Initialization Start")
        print("Brain Initialization End")


if __name__ == "__main__":
    person = Person()
    person.run()
