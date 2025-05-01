import time

import multiprocessing
from multiprocessing.managers import BaseManager


class RobotStatus:
    # 进程锁
    _instance_lock = multiprocessing.Lock()
    _initialized = False  # 是否初始化完成

    def __init__(self):
        self.state = {}  # 状态字典
        if not RobotStatus._initialized:
            print("RobotStatus init")
            RobotStatus._initialized = True

    def __new__(cls, *args, **kwargs):
        if not hasattr(RobotStatus, "_instance"):
            with RobotStatus._instance_lock:
                if not hasattr(RobotStatus, "_instance"):
                    RobotStatus._instance = object.__new__(cls)
        return RobotStatus._instance

    def set_state(self, key, value):
        """设置状态"""
        self.state[key] = value
        print(f"Set state: {key} -> {value}")

    def get_state(self):
        """返回状态字典"""
        print(f"Get state: {self.state}")
        return self.state


# 全局单例
shared_robot_status = RobotStatus()


class MyManager(BaseManager):
    pass


# 注册给客户端调用的方法:
MyManager.register('get_shared_state', callable=lambda: shared_robot_status)

if __name__ == '__main__':
    manager = MyManager(address=('localhost', 5017), authkey=b'abracadabra')
    manager.start()

    shared_state = manager.get_shared_state()

    print("Manager started.")
    # 键盘中断
    import signal

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    while True:
        time.sleep(1)
        print(f"Server state: {shared_state.get_state()}")
        shared_state.set_state("test", "test_value")
