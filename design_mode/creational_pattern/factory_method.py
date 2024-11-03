"""
工厂方法模式
"""
from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def render(self, a, b):
        pass

    def on_click(self, f):
        pass


class WindowsButton(Button):
    def render(self, a, b):
        print("Windows Button")

    def on_click(self, f):
        print("Windows Button Click")


class MacButton(Button):
    def render(self, a, b):
        print("Mac Button", a, b)

    def on_click(self, f):
        print("Mac Button Click")
        f()


class Dialog(metaclass=ABCMeta):
    def render(self):
        ok_button = self.create_button()
        ok_button.render(1, 2)
        ok_button.on_click(lambda: print("Button Click"))

    @abstractmethod
    def create_button(self):
        return Button()


class WindowsDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class MacDialog(Dialog):
    def create_button(self):
        return MacButton()


class Application(object):
    def __init__(self):
        self.dialog = None

    def initialize(self):
        config = "Mac"
        if config in "Windows":
            self.dialog = WindowsDialog()
        elif config in "Mac":
            self.dialog = MacDialog()
        else:
            raise ValueError("Unknown OS")


"""
工厂方法模式
将类的实例化推迟到子类
新增运算符，需要增加具体工厂类、具体运算符类
工厂方法把简单工厂的内部逻辑判断移到了客户端代码来进行
"""


class Operation(metaclass=ABCMeta):
    def __init__(self):
        self.__number_a = None
        self.__number_b = None

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


class OperationSub(Operation):
    def get_result(self):
        return self.get_number_a() - self.get_number_b()


class OperationMul(Operation):
    def get_result(self):
        return self.get_number_a() * self.get_number_b()


class OperationDiv(Operation):
    def get_result(self):
        if self.get_number_b() == 0:
            raise ValueError("除数不能为0")
        return self.get_number_a() / self.get_number_b()


class OperationFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_operation(self):
        pass


class AddFactory(OperationFactory):
    def create_operation(self):
        return OperationAdd()


class SubFactory(OperationFactory):
    def create_operation(self):
        return OperationSub()


class MulFactory(OperationFactory):
    def create_operation(self):
        return OperationMul()


class DivFactory(OperationFactory):
    def create_operation(self):
        return OperationDiv()


if __name__ == "__main__":
    # 按钮
    app = Application()
    app.initialize()
    app.dialog.render()

    """
    工厂方法模式
    客户端：根据 不同工厂类 的 同一接口和同一参数，创建不同的运算对象
    新增运算符：客户端更改工厂类
    """
    # 计算器
    factory = AddFactory()
    operation_factory = factory.create_operation()
    operation_factory.set_number_a(1)
    operation_factory.set_number_b(2)
    print(operation_factory.get_result())
