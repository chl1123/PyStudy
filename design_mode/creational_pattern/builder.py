"""
生成器
生成器是一种创建型设计模式，使你能够分步骤创建复杂对象。
该模式允许你使用相同的代码创建生成不同类型和形式的对象。
"""
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def reset(self):
        pass

    def set_seats(self, seats):
        pass

    def set_engine(self, engine):
        pass

    def set_trip_computer(self, trip_computer):
        pass

    def set_gps(self, gps):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.__car = Car()

    def reset(self):
        self.__car = Car()

    def set_seats(self, seats):
        self.__car.add('seats', seats)

    def set_engine(self, engine):
        self.__car.add('engine', engine)

    def set_trip_computer(self, trip_computer):
        self.__car.add('trip computer', trip_computer)

    def set_gps(self, gps):
        self.__car.add('gps', gps)

    def get_result(self):
        return self.__car


class Car:
    def __init__(self):
        self.__parts = {}

    def add(self, key, value):
        self.__parts[key] = value

    def list_parts(self):
        print(f'Car parts: {", ".join(self.__parts.keys())}')


class CarManualBuilder(Builder):
    def __init__(self):
        self.__manual = Manual()

    def reset(self):
        self.__manual = Manual()

    def set_seats(self, seats):
        self.__manual.add('seats', seats)

    def set_engine(self, engine):
        self.__manual.add('engine', engine)

    def set_trip_computer(self, trip_computer):
        self.__manual.add('trip computer', trip_computer)

    def set_gps(self, gps):
        self.__manual.add('gps', gps)

    def get_result(self):
        return self.__manual


class Manual:
    def __init__(self):
        self.__parts = {}

    def add(self, key, value):
        self.__parts[key] = value

    def print(self):
        print(f'Manual: {", ".join(self.__parts.keys())}')


class Director:
    def __init__(self):
        self.__builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def construct_sports_car(self):
        self.__builder.reset()
        self.__builder.set_seats(2)
        self.__builder.set_engine('Sport Engine')
        self.__builder.set_trip_computer('Sport Trip Computer')
        self.__builder.set_gps('Sport GPS')

    def construct_city_car(self):
        self.__builder.reset()
        self.__builder.set_seats(4)
        self.__builder.set_engine('City Engine')
        self.__builder.set_trip_computer('City Trip Computer')
        self.__builder.set_gps('City GPS')


if __name__ == "__main__":
    director = Director()
    car_builder = CarBuilder()
    director.set_builder(car_builder)
    director.construct_sports_car()
    car = car_builder.get_result()
    car.list_parts()

    manual_builder = CarManualBuilder()
    director.set_builder(manual_builder)
    director.construct_sports_car()
    manual = manual_builder.get_result()
    manual.print()

    director.construct_city_car()
    car = car_builder.get_result()
    car.list_parts()

    director.construct_city_car()
    manual = manual_builder.get_result()
    manual.print()
