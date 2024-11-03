"""
解决问题2：不会随环境改变的数据是享元对象的内部状态，随环境改变的数据是享元对象的外部状态
内部状态：存储在ConcreteFlyweight对象中；外部状态：由客户端对象存储或计算
这里外部状态是用户账号，内部状态是网站类别
"""

from abc import ABCMeta, abstractmethod


# 用户类：网站的外部状态
class User:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


# 抽象网站类
class WebSite(metaclass=ABCMeta):
    @abstractmethod
    def use(self, user: User):
        pass


# 具体网站类
class ConcreteWebSite(WebSite):
    def __init__(self, name):
        self.name = name

    def use(self, user):
        print(f'网站分类：{self.name}，用户：{user.get_name()}')


# 网站工厂类
class WebSiteFactory:
    def __init__(self):
        self.web_sites = {}

    def get_web_site(self, name):
        if name not in self.web_sites:
            self.web_sites[name] = ConcreteWebSite(name)
        return self.web_sites[name]

    def get_web_site_count(self):
        return len(self.web_sites)


if __name__ == '__main__':
    factory = WebSiteFactory()
    fx = factory.get_web_site('产品展示')
    fx.use(User('小菜'))

    fy = factory.get_web_site('产品展示')
    fy.use(User('大鸟'))

    fz = factory.get_web_site('产品展示')
    fz.use(User('娇娇'))

    fl = factory.get_web_site('博客')
    fl.use(User('老顽童'))

    fm = factory.get_web_site('博客')
    fm.use(User('桃谷六仙'))

    fn = factory.get_web_site('博客')
    fn.use(User('南海鳄神'))

    # 6个客户，只有两个网站类别/实例
    print("网站分类总数：", factory.get_web_site_count())
