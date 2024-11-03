"""
装饰器
"""


class Person:
    def __init__(self, name=None):
        self.name = name

    def show(self):
        print(f'装扮的{self.name}')


class Finery(Person):
    def __init__(self):
        super().__init__()
        self.component = None

    def decorate(self, component):
        self.component = component

    def show(self):
        if self.component is not None:
            self.component.show()


class TShirts(Finery):
    def show(self):
        print('大T恤')
        super().show()


class BigTrouser(Finery):
    def show(self):
        print('垮裤')
        super().show()


class Sneakers(Finery):
    def show(self):
        print('破球鞋')
        super().show()


class Suit(Finery):
    def show(self):
        print('西装')
        super().show()


class Tie(Finery):
    def show(self):
        print('领带')
        super().show()


class LeatherShoes(Finery):
    def show(self):
        print('皮鞋')
        super().show()


if __name__ == '__main__':
    person = Person('小菜')
    print('第一种装扮：')
    tshirts = TShirts()
    big_trouser = BigTrouser()
    sneakers = Sneakers()

    tshirts.decorate(person)
    big_trouser.decorate(tshirts)
    sneakers.decorate(big_trouser)
    sneakers.show()

    print('第二种装扮：')
    suit = Suit()
    tie = Tie()
    leather_shoes = LeatherShoes()
    suit.decorate(person)
    tie.decorate(suit)
    leather_shoes.decorate(tie)
    leather_shoes.show()
