# ABCMeta是Python的特殊的元类，用来生成抽象类
from abc import ABCMeta, abstractmethod


# 动物类，定义say方法，但不实现
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


# 狗类，继承动物，重写say方法
class Dog(Animal):
    def say(self):
        print('i am dog')


# 猫类，继承动物，重写say方法
class Cat(Animal):
    def say(self):
        print('i am cat')


# 工厂类
class ForestFactory(object):
    # say方法的统一接口，传入子类对象，调用他们的say方法
    def say_something(self, object_type):
        return eval(object_type)().say()


"""
简单运算
新增运算符，需要修改OperationFactory类、增加运算符类
违反开闭原则
"""


class OperationFactory(object):
    @staticmethod
    def create_operation(operation):
        if operation == '+':
            return OperationAdd()
        elif operation == '-':
            return OperationSub()
        elif operation == '*':
            return OperationMul()
        elif operation == '/':
            return OperationDiv()
        else:
            raise Exception('error operation')


class Operation:
    def __init__(self):
        self.__number_a = 0
        self.__number_b = 0

    def get_number_a(self):
        return self.__number_a

    def get_number_b(self):
        return self.__number_b

    def set_number_a(self, number_a):
        self.__number_a = number_a

    def set_number_b(self, number_b):
        self.__number_b = number_b

    @abstractmethod
    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        return self.get_number_a() + self.get_number_b()

    def __str__(self):
        return '+'


class OperationSub(Operation):
    def get_result(self):
        return self.get_number_a() - self.get_number_b()

    def __str__(self):
        return '-'


class OperationMul(Operation):
    def get_result(self):
        return self.get_number_a() * self.get_number_b()

    def __str__(self):
        return '*'


class OperationDiv(Operation):
    def get_result(self):
        if self.get_number_b() == 0:
            raise Exception('divisor cannot be zero')
        return self.get_number_a() / self.get_number_b()

    def __str__(self):
        return '/'


"""
按钮
"""


class Button(metaclass=ABCMeta):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, f):
        pass


class WindowsButton(Button):
    def render(self):
        print("show Windows Button")

    def on_click(self, f):
        print("Click Windows Button")
        f()


class MacButton(Button):
    def render(self):
        print("show Mac Button")

    def on_click(self, f):
        print("Click Mac Button")
        f()


class ButtonFactory(object):
    @staticmethod
    def create_button(button_type):
        if button_type == 'Windows':
            return WindowsButton()
        elif button_type == 'Mac':
            return MacButton()
        else:
            raise Exception('error button type')


if __name__ == '__main__':
    # 动物工厂
    ff = ForestFactory()
    ff.say_something('Cat')

    # 按钮
    windows_button = ButtonFactory().create_button('Windows')
    windows_button.render()
    windows_button.on_click(lambda: print('Button Click'))
    mac_button = ButtonFactory().create_button('Mac')
    mac_button.render()
    mac_button.on_click(lambda: print('Button Click'))

    """
    工厂方法模式
    客户端通过调用统一的接口，由工厂类创建具体的操作对象
    客户端：根据 同一工厂类 同一接口 的不同的参数，创建不同的运算对象
    新增运算符：客户端更改参数
    """
    # 简单运算
    op = OperationFactory().create_operation('+')
    op.set_number_a(1)
    op.set_number_b(2)
    print(op.get_result())

    op = OperationFactory().create_operation('-')
    op.set_number_a(1)
    op.set_number_b(2)
    print(op.get_result())
