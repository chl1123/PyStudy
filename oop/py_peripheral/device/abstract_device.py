# abstract_device.py
from abc import ABC, abstractmethod

from utils.log_method import log_class_methods


@log_class_methods
class Device(ABC):
    def __init__(self, comm_interface):
        self.comm_interface = comm_interface

    def initialize(self):
        print(f"Initializing {self.__class__.__name__}")

    @abstractmethod
    def get_status(self):
        raise NotImplementedError("Subclasses must implement this method.")
