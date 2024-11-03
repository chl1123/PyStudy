"""
实现关系是指一个类实现一个或多个接口功能的过程，这里的接口更多的是一种契约或规范。
实现是两个类之间或类与接口之间耦合度最大的关系之一，在这种关系中，类实现了接口或接口类中所声明的操作
类具体实现接口类中所声明的操作：python中无原生interface，这里的接口类是逻辑上的契约或规范
"""


class Car(object):
    def engine(self):
        raise NotImplementedError


class Benz(Car):
    # Banz必须实现engine方法
    def engine(self):
        print("Benz is running.")


class BMW(Car):
    # BMW必须实现engine方法
    def engine(self):
        print("BMW is running.")


if __name__ == "__main__":
    benz = Benz()
    bmw = BMW()
    benz.engine()
    bmw.engine()
