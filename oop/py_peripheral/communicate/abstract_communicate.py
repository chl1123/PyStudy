from abc import abstractmethod, ABC
from utils.log_method import log_class_methods


@log_class_methods
class Communication(ABC):
    @abstractmethod
    def configure(self, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def send(self, data):
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def receive(self):
        raise NotImplementedError("Subclasses must implement this method.")
