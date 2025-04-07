class Student:
    __stu_num = 0

    @classmethod
    def __add_stu(cls):
        cls.__stu_num += 1

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.__add_stu()
        print("student num: ", Student.__stu_num)

    def get_stu_num(cls):
        return cls.__stu_num

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score