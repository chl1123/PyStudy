from oop.py_peripheral.communicate.abstract_communicate import Communication
from utils.log_method import log_class_methods


@log_class_methods
class CANComm(Communication):
    def __init__(self, channel, bitrate):
        self.channel = channel
        self.bitrate = bitrate

    def configure(self, bitrate=None, **kwargs):
        if bitrate:
            self.bitrate = bitrate
        print(f"CANComm bitrate {self.bitrate}")

    def send(self, data):
        print(f"Sending CAN message: {data}")

    def receive(self):
        print("Receive CAN message")
        return "can_message"
