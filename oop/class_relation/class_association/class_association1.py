"""
关联：
关联关系一般长期性的、拥有性的关系，而且双方的关系一般是平等的，如老师与学生之间。
被关联类B以类的属性形式出现在关联类A中，关联可以是单向的，也可以是双向的。
依赖关系与关联关系的区别有动静之分，依赖关系的偶然性和临时性说明了动态性，关联关系的长期性、拥有性静态地展示了对被关联类的引用。
"""


class Computer(object):

    def run(self):
        print("running...")


class Student(object):
    def __init__(self, teacher=None):
        # Student和Teacher双向关联
        self.teacher = teacher
        # Student和Computer单向关联，Student拥有Computer的属性和方法，Computer不拥有Student的属性和方法
        self.computer = Computer()

    def listen(self):
        print("listening...")

    def study(self):
        print("studying...")

    def ask(self):
        print("asking...")

    def code(self):
        print("coding...")
        self.computer.run()


class Teacher(object):
    def __init__(self, student=None):
        # 双向关联
        self.student = student

    def teach(self):
        print("Teaching...")
        self.student.listen()


class Node(object):
    def __init__(self):
        self.data = None
        # 自关联
        self.next = None
        # 自关联
        self.prev = None

    def __str__(self):
        return str(self.data)


if __name__ == "__main__":
    s = Student()
    s.study()

    t = Teacher()
    s.teacher = t
    t.student = s
    t.teach()
    s.ask()
    t.teach()

    s.code()

    # 自关联
    n = Node()
    n.data = 1
    n.next = Node()
    n.next.data = 2
    n.next.prev = n
    print(n)
    print(n.next)
    print(n.next.prev)
