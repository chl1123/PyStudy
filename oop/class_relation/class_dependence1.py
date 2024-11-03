"""
依赖：类A仅使用到了另一个类B，类B本身并不属于类A，或者说类A并不拥有类B
"""


class Person(object):
    # 依赖：Plane类作为Person类flying1方法的形参，将plane对象作为参数传入，依赖plane对象的fly1()方法
    def flying1(self, plane):
        plane.fly1()

    # 依赖：Plane类作为Person类flying2方法的局部变量，依赖Plane类的fly1()方法
    def flying2(self):
        plane = Plane()
        plane.fly1()

    # 依赖：Person类调用Plane类的静态方法，依赖Plane类的fly2()方法
    def flying3(self):
        Plane.fly2()


class Plane(object):
    def fly1(self):
        print("The plane is flying.")

    @staticmethod
    def fly2():
        print("The plane is flying.")


if __name__ == "__main__":
    person = Person()
    plane = Plane()
    person.flying1(plane)
    person.flying2()
