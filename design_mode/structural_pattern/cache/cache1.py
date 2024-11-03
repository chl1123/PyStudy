"""
有多个客户都需要自己的网站，网站形式有产品展示、博客等，功能类似
方法1：每个网站一个实例
问题1：多个实例相同，浪费计算机资源
"""


class WebSite(object):
    def __init__(self, name):
        self.name = name

    def use(self):
        print(f'网站分类：{self.name}')


if __name__ == '__main__':
    fx = WebSite('产品展示')
    fx.use()

    fy = WebSite('产品展示')
    fy.use()

    fz = WebSite('产品展示')
    fz.use()

    fl = WebSite('博客')
    fl.use()

    fm = WebSite('博客')
    fm.use()

    fn = WebSite('博客')
    fn.use()
