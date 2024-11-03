"""
解决问题1：不管多少个网站，每一个网站类别只需要一个实例
问题2：每家企业的数据不一样，至少账号不一样
"""
from abc import ABCMeta, abstractmethod


# 抽象网站类
class WebSite(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def use(self):
        pass


# 具体网站类
class ConcreteWebSite(WebSite):
    def __init__(self, name):
        super().__init__(name)

    def use(self):
        print(f'网站分类：{self.name}')


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
    fx.use()

    fy = factory.get_web_site('产品展示')
    fy.use()

    fz = factory.get_web_site('产品展示')
    fz.use()

    fl = factory.get_web_site('博客')
    fl.use()

    fm = factory.get_web_site('博客')
    fm.use()

    fn = factory.get_web_site('博客')
    fn.use()

    print("网站分类总数：", factory.get_web_site_count())
