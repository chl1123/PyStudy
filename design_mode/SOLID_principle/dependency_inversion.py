"""
依赖倒置原则
高层次的类不应该依赖于低层次的类。两者都应该依赖于抽象接口。
抽象接口不应依赖于具体实现。具体实现应该依赖于抽象接口
• 低层次的类实现基础操作（例如磁盘操作、传输网络数据和连接数据库等）。
• 高层次类包含复杂业务逻辑以指导低层次类执行特定操作。
"""
from abc import ABCMeta, abstractmethod

"""
before:
高层次的预算报告类（BudgetReport）使用低层次的数据库类（MySQLDatabase）来读取和保存其数据
低层次类中的任何改变（例如当数据库服务器发布新版本时）都可能会影响到高层次的类，但高层次的类不应关注数据存储的细节
"""


class BudgetReport0:
    def __init__(self):
        self.__database = None

    def open(self, database):
        self.__database = database
        print('BudgetReport: open database')

    def save(self):
        print('BudgetReport: save data')


class MySQLDatabase0:
    def __init__(self):
        print('MySQLDatabase: init')

    def insert(self):
        print('MySQLDatabase: insert data')

    def update(self):
        print('MySQLDatabase: update data')

    def delete(self):
        print('MySQLDatabase: delete data')


"""
after:
高层次的预算报告类（BudgetReport）使用接口（Database）来读取和保存其数据
低层次的类依赖于高层次的抽象
"""


class Database(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class BudgetReport:
    def __init__(self):
        self.__database = None

    def open(self, database: Database):
        self.__database = database
        print('BudgetReport: open database')

    def save(self):
        print('BudgetReport: save data')


class MySQLDatabase(Database):
    def __init__(self):
        print('MySQLDatabase: init')

    def connect(self):
        print('MySQLDatabase: connect')

    def insert(self):
        print('MySQLDatabase: insert data')

    def update(self):
        print('MySQLDatabase: update data')

    def delete(self):
        print('MySQLDatabase: delete data')


class OracleDatabase(Database):
    def __init__(self):
        print('OracleDatabase: init')

    def connect(self):
        print('OracleDatabase: connect')

    def insert(self):
        print('OracleDatabase: insert data')

    def update(self):
        print('OracleDatabase: update data')

    def delete(self):
        print('OracleDatabase: delete data')


if __name__ == '__main__':
    report1 = BudgetReport()
    report1.open(OracleDatabase())
    report1.save()

    report2 = BudgetReport()
    report2.open(MySQLDatabase())
    report2.save()
