"""
原型、克隆
原型是一种创建型设计模式，使你能够复制已有对象，而又无需使代码依赖它们所属的类
"""

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):
    def __init__(self, shape=None):
        if shape:
            self.x = shape.x
            self.y = shape.y
            self.color = shape.color
        else:
            self.x = 0
            self.y = 0
            self.color = 'white'

    @abstractmethod
    def clone(self):
        pass


class Rectangle(Shape):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.width = source.width
            self.height = source.height
        else:
            self.width = 0
            self.height = 0

    def clone(self):
        return Rectangle(self)


class Circle(Shape):
    def __init__(self, source=None):
        super().__init__(source)
        if source:
            self.radius = source.radius
        else:
            self.radius = 0

    def clone(self):
        return Circle(self)


class Client:
    def __init__(self):
        self.shapes = []
        self.load_cache()

    def load_cache(self):
        circle = Circle()
        circle.x = 10
        circle.y = 10
        circle.color = 'red'
        circle.radius = 20
        self.shapes.append(circle)

        rectangle = Rectangle()
        rectangle.x = 20
        rectangle.y = 20
        rectangle.color = 'blue'
        rectangle.width = 10
        rectangle.height = 20
        self.shapes.append(rectangle)

    def clone(self):
        for i in range(len(self.shapes)):
            self.shapes.append(self.shapes[i].clone())

    def show(self):
        for shape in self.shapes:
            print(shape.__class__.__name__, shape.x, shape.y, shape.color)


if __name__ == '__main__':
    client = Client()
    client.clone()
    client.show()
