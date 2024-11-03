"""
接口隔离原则
客户端不应被强迫依赖于其不使用的方法
与其他原则一样，可能会过度使用这条原则。不要进一步划分已经非常具体的接口。
创建的接口越多，代码就越复杂。因此要保持平衡。
"""
from abc import ABC, abstractmethod

"""
before:
不是所有客户端能满足复杂接口的要求，比如CDN地址
"""


class CloudProvider0(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def store_file(self, name):
        pass

    @abstractmethod
    def get_file(self, name):
        pass

    @abstractmethod
    def create_server(self, region):
        pass

    @abstractmethod
    def list_servers(self, region):
        pass

    @abstractmethod
    def get_CDN_address(self):
        pass


class AlibabaCloud0(CloudProvider0):
    def store_file(self, name):
        print(f'{self.name}存储文件{name}')

    def get_file(self, name):
        print(f'{self.name}获取文件{name}')

    def create_server(self, region):
        print(f'{self.name}创建服务器{region}')

    def list_servers(self, region):
        print(f'{self.name}列出服务器{region}')

    def get_CDN_address(self):
        print(f'{self.name}获取CDN地址')


class TencentCloud0(CloudProvider0):
    def store_file(self, name):
        print(f'{self.name}存储文件{name}')

    def get_file(self, name):
        print(f'{self.name}获取文件{name}')

    def create_server(self, region):
        print(f'{self.name}创建服务器{region}')

    def list_servers(self, region):
        print(f'{self.name}列出服务器{region}')

    # 假设腾讯云没有CDN地址，但是接口中有这个方法，此处必须实现。pass不是最好的解决方案
    def get_CDN_address(self):
        pass


"""
after:
一个复杂的接口被拆分为一组颗粒度更小的接口
"""


class CloudHostingProvider(ABC):
    @abstractmethod
    def create_server(self, region):
        pass

    @abstractmethod
    def list_servers(self, region):
        pass


class CloudStorageProvider(ABC):
    @abstractmethod
    def store_file(self, name):
        pass

    @abstractmethod
    def get_file(self, name):
        pass


class CDNProvider(ABC):
    @abstractmethod
    def get_CDN_address(self):
        pass


class AlibabaCloud(CloudHostingProvider, CloudStorageProvider, CDNProvider):
    def __init__(self, name):
        self.name = name

    def store_file(self, name):
        print(f'{self.name}存储文件{name}')

    def get_file(self, name):
        print(f'{self.name}获取文件{name}')

    def create_server(self, region):
        print(f'{self.name}创建服务器{region}')

    def list_servers(self, region):
        print(f'{self.name}列出服务器{region}')

    def get_CDN_address(self):
        print(f'{self.name}获取CDN地址')


class TencentCloud(CloudHostingProvider, CloudStorageProvider):
    def __init__(self, name):
        self.name = name

    def store_file(self, name):
        print(f'{self.name}存储文件{name}')

    def get_file(self, name):
        print(f'{self.name}获取文件{name}')

    def create_server(self, region):
        print(f'{self.name}创建服务器{region}')

    def list_servers(self, region):
        print(f'{self.name}列出服务器{region}')


if __name__ == "__main__":
    alibaba = AlibabaCloud('阿里云')
    alibaba.store_file('test')
    alibaba.get_file('test')
    alibaba.create_server('shanghai')
    alibaba.list_servers('shanghai')
    alibaba.get_CDN_address()

    tencent = TencentCloud('腾讯云')
    tencent.store_file('test')
    tencent.get_file('test')
    tencent.create_server('shanghai')
    tencent.list_servers('shanghai')
