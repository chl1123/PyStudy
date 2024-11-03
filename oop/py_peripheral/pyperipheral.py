# pyperipheral.py
from oop.py_peripheral.configuration import Configuration
from oop.py_peripheral.device.device_manager import DeviceManager
from utils.log_method import log_class_methods


@log_class_methods
class PyPeripheral:
    def __init__(self):
        self.communication = None
        self.configuration = None
        self.device_manager = DeviceManager()

    def configure_communication(self, comm_interface):
        self.communication = comm_interface
        print(f"Communication configured with {comm_interface.__class__.__name__}")

    def load_configuration(self, config_loader):
        self.configuration = Configuration(config_loader)
        self.configuration.load_configuration()

    def add_device(self, device):
        self.device_manager.add_device(device)

    def initialize_system(self):
        self.device_manager.initialize_all()
        print("System initialized")
