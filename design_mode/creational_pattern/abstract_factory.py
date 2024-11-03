"""
抽象工厂模式
"""
from abc import ABCMeta, abstractmethod


class Button(metaclass=ABCMeta):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, f):
        pass


class WindowsButton(Button):
    def render(self):
        print("Windows Button")

    def on_click(self, f):
        print("Windows Button Click")
        f()


class MacButton(Button):
    def render(self):
        print("Mac Button")

    def on_click(self, f):
        print("Mac Button Click")
        f()


class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def render(self):
        pass

    def on_check(self, f):
        pass


class WindowsCheckbox(Checkbox):
    def render(self):
        print("Windows Checkbox")

    def on_check(self, f):
        print("Windows Checkbox Check")
        f()


class MacCheckbox(Checkbox):
    def render(self):
        print("Mac Checkbox")

    def on_check(self, f):
        print("Mac Checkbox Check")
        f()


class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:
    def __init__(self):
        self.factory = None

    def initialize(self):
        config = "Windows"
        if config in "Windows":
            self.factory = WindowsFactory()
        elif config in "Mac":
            self.factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

    def create_ui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()
        button.render()
        checkbox.render()
        button.on_click(lambda: print("Button Click"))
        checkbox.on_check(lambda: print("Checkbox Check"))


if __name__ == '__main__':
    app = Application()
    app.initialize()
    app.create_ui()
