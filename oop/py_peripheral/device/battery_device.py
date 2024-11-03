from utils.log_method import log_class_methods
from oop.py_peripheral.device.abstract_device import Device


@log_class_methods
class BatteryDevice(Device):
    def __init__(self, comm_interface):
        super().__init__(comm_interface)

    def get_status(self):
        self.comm_interface.send("Request battery status")
        status = self.comm_interface.receive()
        print(f"Battery status: {status}")
        return status
