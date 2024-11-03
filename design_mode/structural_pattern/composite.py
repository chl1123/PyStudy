"""
组合模式
"""


class Company(object):
    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    # 履行职责
    def line_of_duty(self):
        pass


class ConcreteCompany(Company):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, company):
        self.children.append(company)

    def remove(self, company):
        self.children.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)
        for component in self.children:
            component.display(depth + 2)

    # 履行职责
    def line_of_duty(self):
        for component in self.children:
            component.line_of_duty()


class HRDepartment(Company):
    def __init__(self, name):
        super().__init__(name)

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-' * depth + self.name)

    # 履行职责
    def line_of_duty(self):
        print(f'{self.name} 员工招聘培训管理')


class FinanceDepartment(Company):
    def __init__(self, name):
        super().__init__(name)

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        print('-' * depth + self.name)

    # 履行职责
    def line_of_duty(self):
        print(f'{self.name} 公司财务收支管理')


if __name__ == '__main__':
    root = ConcreteCompany('北京总公司')
    root.add(HRDepartment('总公司人力资源部'))
    root.add(FinanceDepartment('总公司财务部'))

    comp = ConcreteCompany('上海华东分公司')
    comp.add(HRDepartment('华东分公司人力资源部'))
    comp.add(FinanceDepartment('华东分公司财务部'))
    root.add(comp)

    comp1 = ConcreteCompany('南京办事处')
    comp1.add(HRDepartment('南京办事处人力资源部'))
    comp1.add(FinanceDepartment('南京办事处财务部'))
    comp.add(comp1)

    comp2 = ConcreteCompany('杭州办事处')
    comp2.add(HRDepartment('杭州办事处人力资源部'))
    comp2.add(FinanceDepartment('杭州办事处财务部'))
    comp.add(comp2)

    print('结构图：')
    root.display(1)

    print('职责：')
    root.line_of_duty()
