from oop.py_peripheral.communicate.abstract_communicate import Communication
from utils.log_method import log_class_methods


@log_class_methods
class SerialComm(Communication):
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def configure(self, baudrate=None, **kwargs):
        if baudrate:
            self.baudrate = baudrate
        print(f"SerialComm baudrate {self.baudrate}")

    def send(self, data):
        print(f"Sending data over serial: {data}")

    def receive(self):
        print("Receive data over serial")
        return "data"
