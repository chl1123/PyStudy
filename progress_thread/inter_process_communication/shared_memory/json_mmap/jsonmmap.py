# -*- coding: utf-8 -*-
import mmap
import json
import os
import sys

class ObjectMmap(mmap.mmap):
    def __new__(cls, fileno=-1, length=1024, access=mmap.ACCESS_WRITE, tagname='share_mmap'):
        if sys.platform == 'win32':
            return super().__new__(cls, fileno, length, access=access, tagname=tagname)
        else:
            # 创建一个临时文件来共享内存映射
            fd = os.open(tagname, os.O_CREAT | os.O_RDWR)
            os.ftruncate(fd, length)
            return super().__new__(cls, fd, length, access=access)

    def __init__(self, fileno=-1, length=1024, access=mmap.ACCESS_WRITE, tagname='share_mmap'):
        # 初始化子类特有的属性，不调用父类的__init__
        self.length = length
        self.access = access
        self.contentbegin = 0  # 新增属性需在__init__中初始化
        self.contentend = 0
        self.contentlength = 0
        self.obj = None

    def jsonwrite(self, obj):
        try:
            self.obj = obj
            self.seek(0)
            obj_str = json.dumps(obj)
            obj_len = len(obj_str)
            content = f"{obj_len}:{obj_str}"
            self.write(content.encode('utf-8'))  # 确保写入字节数据
            self.contentbegin = len(str(obj_len)) + 1
            self.contentend = self.tell()
            self.contentlength = self.contentend - self.contentbegin
            return True
        except Exception as e:
            print(f"Error in jsonwrite: {e}")
            return False

    def jsonread_master(self):
        try:
            self.seek(self.contentbegin)
            content = self.read(self.contentlength).decode('utf-8')  # 解码字节数据
            obj = json.loads(content)
            self.obj = obj
            return obj
        except Exception as e:
            print(f"Error in jsonread_master: {e}")
            return self.obj if hasattr(self, 'obj') else None

    def jsonread_follower(self):
        try:
            self.seek(0)
            data = self.read().decode('utf-8')
            index = data.find(':')
            if index != -1:
                head = data[:index]
                contentlength = int(head)
                content = data[index+1:index+1+contentlength]
                obj = json.loads(content)
                self.obj = obj
                return obj
            else:
                return None
        except Exception as e:
            print(f"Error in jsonread_follower: {e}")
            return self.obj if hasattr(self, 'obj') else None