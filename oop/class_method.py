class Student(object):
    __stu_num = 0

    def __new__(cls, *args, **kwargs):
        print("__new__")
        return super(Student, cls).__new__(cls)

    def __init__(self, name):
        print("__init__")
        self.name = name
        # Student.__stu_num += 1  # 和下面等效
        self.__add_stu()

    def set_name(self, name):
        self.name = name

    # 类方法不能访问实例属性/方法，只能访问类属性
    @classmethod
    def get_stu_num(cls):
        return cls.__stu_num

    # 私有类方法
    @classmethod
    def __add_stu(cls):
        cls.__stu_num += 1
        print("add student, student num: ", cls.__stu_num)


s1 = Student("crx")
s2 = Student("gsx")
s3 = Student("oen")

# 不会调用__new__和__init__, Student("XXX")时才调用
print("student num: ", Student.get_stu_num())
