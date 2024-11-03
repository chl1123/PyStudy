"""
桥接模式
"""
from abc import ABCMeta, abstractmethod


class PhoneSoftware(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class PhoneGame(PhoneSoftware):
    def run(self):
        print('Phone Game Running')


class PhoneAddressList(PhoneSoftware):
    def run(self):
        print('Phone Address List Running')


class PhoneBrand(metaclass=ABCMeta):
    def __init__(self, software: PhoneSoftware = None):
        self.software = software

    def set_software(self, software: PhoneSoftware):
        self.software = software

    @abstractmethod
    def run(self):
        pass


class PhoneBrandHW(PhoneBrand):
    def run(self):
        self.software.run()
        print('HW Phone Running')


class PhoneBrandXM(PhoneBrand):
    def run(self):
        self.software.run()
        print('XM Phone Running')


if __name__ == '__main__':
    hw = PhoneBrandHW()
    hw.set_software(PhoneGame())
    hw.run()
    hw.set_software(PhoneAddressList())
    hw.run()

    xm = PhoneBrandXM()
    xm.set_software(PhoneAddressList())
    xm.run()
    xm.set_software(PhoneGame())
    xm.run()
