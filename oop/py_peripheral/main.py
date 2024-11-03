from oop.py_peripheral.device.battery_device import BatteryDevice
from oop.py_peripheral.communicate.serial_comm import SerialComm
from oop.py_peripheral.pyperipheral import PyPeripheral
from utils.log_method import log_class_methods


@log_class_methods
class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file

    def load(self):
        return {"device": "BatteryDevice", "port": "/dev/ttyS0", "baudrate": 9600}


if __name__ == "__main__":
    sdk = PyPeripheral()

    # 加载配置
    config_loader = ConfigLoader(config_file="config.json")
    sdk.load_configuration(config_loader)

    # 通信方法
    serial_comm = SerialComm(port="/dev/ttyS0", baudrate=9600)
    sdk.configure_communication(serial_comm)

    # 创建设备并添加
    battery_device = BatteryDevice(comm_interface=serial_comm)
    sdk.add_device(battery_device)

    # 初始化系统
    sdk.initialize_system()

    # 获取电池数据
    battery_device.get_status()
