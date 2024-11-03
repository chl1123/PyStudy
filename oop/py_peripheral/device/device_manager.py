# device_manager.py
from utils.log_method import log_class_methods


@log_class_methods
class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device added: {device.__class__.__name__}")

    def initialize_all(self):
        for device in self.devices:
            device.initialize()
