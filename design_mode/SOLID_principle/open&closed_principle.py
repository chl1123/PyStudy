"""
开闭原则
对于扩展，类应该是开放的，对于修改，类应该是封闭的
"""
from abc import abstractmethod, ABCMeta

"""
design mode before: 
添加新的运输方式时，必须修改Order类
"""


class Order0:
    def __init__(self):
        self.__line_items = []
        self.shipping = 0

    def get_total(self):
        total = 0
        for item in self.__line_items:
            total += item["price"] * item["quantity"]
        return total + self.shipping

    def get_total_weight(self):
        total = 0
        for item in self.__line_items:
            total += item["weight"] * item["quantity"]
        return total

    def set_shipping_type(self, shipping_type):
        # 陆运
        if shipping_type == "ground":
            # 大额订单免陆运费
            if self.get_total() > 100:
                self.shipping = 0
            else:
                # 每公斤1.5元, 最少10元
                self.shipping = max(10.0, self.get_total_weight() * 1.5)
        # 空运
        elif shipping_type == "air":
            # 每公斤3元, 最少20元
            self.shipping = max(20, self.get_total_weight() * 3)

    def get_shipping_cost(self):
        return self.shipping

    def get_shipping_date(self):
        pass


"""
design mode after:
通过策略模式，将运输方式的计算逻辑封装到独立的类中
添加新的运输方式时，只需添加新的类，而不需要修改Order类
"""


class Order:
    def __init__(self):
        self.__line_items = []
        self.shipping = 0

    def add_item(self, item):
        self.__line_items.append(item)

    def get_total(self):
        total = 0
        for item in self.__line_items:
            total += item["price"] * item["quantity"]
        return total + self.shipping

    def get_total_weight(self):
        total = 0
        for item in self.__line_items:
            total += item["weight"] * item["quantity"]
        return total

    def set_shipping_type(self, shipping_type):
        self.shipping = shipping_type.get_cost(self)

    def get_shipping_cost(self):
        return self.shipping

    def get_shipping_date(self):
        pass


class Shipping(metaclass=ABCMeta):
    @abstractmethod
    def get_cost(self, order):
        pass

    @abstractmethod
    def get_date(self, order):
        pass


class GroundShipping(Shipping):
    def get_cost(self, order):
        if order.get_total() > 100:
            return 0
        return max(10.0, order.get_total_weight() * 1.5)

    def get_date(self, order):
        pass


class AirShipping(Shipping):
    def get_cost(self, order):
        return max(20, order.get_total_weight() * 3)

    def get_date(self, order):
        pass


if __name__ == "__main__":
    order1 = Order()
    order1.add_item({"price": 100, "quantity": 1, "weight": 1})
    order1.set_shipping_type(GroundShipping())
    print(order1.get_shipping_cost())

    order2 = Order()
    order2.add_item({"price": 50, "quantity": 2, "weight": 10})
    order2.set_shipping_type(AirShipping())
    print(order2.get_shipping_cost())
