from utils.log_method import log_class_methods


# configuration.py
@log_class_methods
class Configuration:
    def __init__(self, config_loader):
        self.config_loader = config_loader

    def load_configuration(self):
        config = self.config_loader.load()
        print(f"Loaded configuration: {config}")
