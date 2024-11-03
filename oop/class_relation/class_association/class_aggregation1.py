"""
聚合关系是也是关联关系的特例。
普通关联关系的两个类一般处于同一平等层次上，而聚合关系的两个类处于不同的层次，是整体与部分的关系。
聚合关系中的整体和部分是可以分离的，生命周期也是相互独立的，如公司与员工之间。
"""


class Company:
    def __init__(self, name='Company', address='China'):
        self.employees = []
        self.name = name
        self.address = address

    def add_employee(self, employee):
        # Company类由Employee类聚合而成。Company类包含有Employee类的全局对象，但Employee类的对象可以不在Company类创建的时刻创建
        self.employees.append(employee)
        print('{} add {}'.format(self.name, employee.name))


class Employee:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    employee = Employee('John')
    company = Company("Google", "USA")
    company.add_employee(employee)
