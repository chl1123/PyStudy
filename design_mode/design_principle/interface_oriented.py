"""
面向接口开发，而不是面向实现开发
"""

from abc import abstractmethod, ABCMeta

"""
design mode before:
"""


class Sausage0:
    def get_nutrition(self):
        return 10

    def get_color(self):
        return 'red'

    def get_expiration(self):
        return '2022-12-31'


class Cat0:
    def __init__(self, energy):
        self.__energy = energy

    def eat(self, s: Sausage0):
        self.__energy += 10


"""
design mode after:
"""


class Food(metaclass=ABCMeta):
    """食物接口类"""

    @abstractmethod
    def get_nutrition(self):
        pass


class Sausage(Food):
    def get_nutrition(self):
        return 10

    def get_color(self):
        return 'red'

    def get_expiration(self):
        return '2022-12-31'


class Cat:
    def __init__(self, energy):
        self.__energy = energy

    def eat(self, s: Food):
        self.__energy += s.get_nutrition()


"""
组合优于继承
"""

"""
需求：为汽车制造商创建一个目录程序。 
该公司同时生产：
汽车 Car 和 卡车 Truck
车辆可能是 电动车 Electric 或 汽油车 Combustion
所有车型都配备了手动控制 manual control 或 自动驾驶 Autopilot 功能。

继承问题：在多个维度上扩展一个类（汽车类型 × 引擎类型 × 驾驶类型）可能会导致子类组合的数量爆炸
"""


class Transport:
    pass


class Truck(Transport):
    pass


class Car(Transport):
    pass


class ElectricTruck(Car):
    pass


class CombustionEngineTruck(Truck):
    pass


class AutopilotElectricTruck(ElectricTruck):
    pass


class AutopilotCombustionEngineTruck(CombustionEngineTruck):
    pass


class ElectricCar(Car):
    pass


class CombustionEngineCar(Car):
    pass


class AutopilotElectricCar(ElectricCar):
    pass


class AutopilotCombustionEngineCar(CombustionEngineCar):
    pass


"""
组合：将不同“维度”的功能抽取到各自的类层次结构中
"""


class Transport:
    def __init__(self, engine, driver):
        self.__engine = engine
        self.__driver = driver

    def deliver(self, destination, cargo):
        self.__engine.move()
        self.__driver.navigate()


class Engine(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass


class Drive(metaclass=ABCMeta):
    @abstractmethod
    def navigate(self):
        pass


class ElectricEngine(Engine):
    def move(self):
        print("Electric engine moves")


class CombustionEngine(Engine):
    def move(self):
        print("Combustion engine moves")


class Robot(Drive):
    def navigate(self):
        print("Autopilot drive")


class Human(Drive):
    def navigate(self):
        print("Manual drive")


if __name__ == "__main__":
    # design mode before:
    sausage0 = Sausage0()
    cat0 = Cat0(10)
    cat0.eat(sausage0)
    print(cat0.__dict__)

    # design mode after:
    sausage = Sausage()
    cat = Cat(10)
    cat.eat(sausage)
    print(cat.__dict__)
