"""
单一职责原则：
每个类只负责软件中的一个功能，并将该功能完全封装（隐藏）在该类中
减少复杂度，提高可维护性
"""

"""
design mode before: Employee0类中包含多个不同的行为
雇员表打印的格式可能会随着时间而改变，从而需要对类中的代码进行修改
"""


class Employee0:
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

    def get_name(self):
        return self.name

    def print_employee_sheet(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")


"""
design mode before: Employee类和EmployeeSheet类分别负责不同的功能
打印需求发生变化时，只需修改EmployeeSheet类
"""


class Employee:
    def __init__(self, emp_id: int, name: str):
        self.emp_id = emp_id
        self.name = name

    def get_name(self):
        return self.name


class EmployeeSheet:
    def __init__(self, employee: Employee):
        self.employee = employee

    def print_employee_sheet(self):
        print(f"Employee Name: {self.employee.get_name()}")
        print(f"Employee ID: {self.employee.emp_id}")


if __name__ == "__main__":
    emp2 = Employee0(2, "Bob")
    emp2.print_employee_sheet()

    emp = Employee(1, "Alice")
    emp_sheet = EmployeeSheet(emp)
    emp_sheet.print_employee_sheet()
    # emp.print_employee_sheet()
