"""
代理
需求：在第三方腾讯视频程序库中添加延迟初始化和缓存
"""
from abc import ABCMeta, abstractmethod


# 服务连接器的抽象类
class ThirdPartyTVLib(meta=ABCMeta):
    @abstractmethod
    def list_videos(self):
        pass

    @abstractmethod
    def get_video_info(self, id):
        pass

    @abstractmethod
    def download_video(self, id):
        pass


# 服务连接器的具体实现
class ThirdPartyTVClass(ThirdPartyTVLib):
    def list_videos(self):
        # 向腾讯视频发送获取视频列表API请求
        return '视频列表'

    def get_video_info(self, id):
        # 向腾讯视频发送获取视频信息API请求
        return f'视频信息{id}'

    def download_video(self, id):
        # 向腾讯视频发送下载视频API请求
        return f'下载视频{id}'


# 为了节省带宽，添加一个代理类，缓存之前的请求的结果
class CachedTVClass(ThirdPartyTVLib):
    def __init__(self, service: ThirdPartyTVLib):
        self.service = service
        self.list_cache = None
        self.video_cache = None
        self.need_reset = False

    def list_videos(self):
        if self.list_cache is None or self.need_reset:
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, id):
        if self.video_cache is None or self.need_reset:
            self.video_cache = self.service.get_video_info(id)
        return self.video_cache

    def download_exists(self, id):
        return False

    def download_video(self, id):
        if not self.download_exists(id) or self.need_reset:
            self.service.download_video(id)


# 客户端
class TVManager:
    def __init__(self, service: ThirdPartyTVLib):
        self.service = service

    def render_list_panel(self):
        list = self.service.list_videos()
        print(list)
        # 渲染视频缩略图列表

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        print(info)
        # 渲染视频页面

    def react_on_user_input(self, id):
        self.render_list_panel()
        self.render_video_page(id)


if __name__ == '__main__':
    service = CachedTVClass(ThirdPartyTVClass())
    manager = TVManager(service)
    manager.react_on_user_input(1)
