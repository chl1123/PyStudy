class Student(object):
    role = "Stu"

    def __init__(self, name):
        self.name = name

    # 静态方法：和类和实例无关
    @staticmethod
    def walk():
        print("student walking...")

    # self可以作为参数，调用者显示传递
    @staticmethod
    def fly(self):
        print(self.name, "is flying...")


s = Student("Jack")
# s.walk()  # 和下面等价
Student.walk()

s.fly(s)  # s.fly(s)
