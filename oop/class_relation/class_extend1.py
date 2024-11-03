"""
继承：
继承指的是子类继承父类、或子接口继承父接口的功能并增加自己新功能的过程，是两个类之间耦合度最大的关系之一。父类称为基类或超类，子类也称为派生类。子类可以继承自抽象类或普通类。
"""

# 子类继承自抽象类，必须实现父类中@abstractmethod修饰的抽象方法
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def __init__(self):
        self.name = "Animal"

    # 动物都会移动，但移动方式不同，定义为抽象方法，子类必须实现
    @abstractmethod
    def move(self):
        print("Animal is running.")

    # 动物不一定会叫，且叫的方式不同，定义为普通方法，子类可以不实现
    def cry(self):
        pass


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Dog"

    def move(self):
        print("Dog is running.")

    def cry(self):
        print("Dog wang wang.")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = "Cat"

    def move(self):
        print("Animal is running.")

    def cry(self):
        print("Cat miao miao.")

    def __jump(self):
        print("Cat is jumping.")


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    dog.move()
    cat.move()

    dog.cry()
    cat.cry()
