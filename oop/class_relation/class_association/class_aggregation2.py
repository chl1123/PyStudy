class DeviceManager:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device added: {device.__class__.__name__}")

    def initialize_all(self):
        for device in self.devices:
            device.initialize()


class SerialComm:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate

    def open(self):
        print(f"Serial port {self.port} is opened with baudrate {self.baudrate}")

    def close(self):
        print(f"Serial port {self.port} is closed")

    def send(self, data):
        print(f"Data sent: {data}")

    def receive(self):
        data = "Data received"
        print(f"{data}")
        return data


class RGBW:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 0

    def set_led_color(self, rgbw):
        self.r = rgbw[0]
        self.g = rgbw[1]
        self.b = rgbw[2]
        self.w = rgbw[3]
        print(f"LED lights are set to {rgbw}")

    def get_led_color(self):
        return [self.r, self.g, self.b, self.w]


class Led:
    # 类属性
    DEFAULT_COLOR = True
    MAX_BRIGHTNESS = 255

    def __init__(self, brand, comm=None):
        # 成员属性 实例属性
        self.brand = brand
        # 关联：是一种拥有的关系，使Led类知道SerialComm类的属性和方法
        self.comm = comm
        # 组合：关联的特例。是整体(Led)与部分(RGBW)的关系，但部分(RGBW)不能离开整体(Led)而单独存在
        self.rgbw = RGBW()

    def initialize(self):
        print(f"{self.brand} LED lights are initialized")
        self.rgbw.set_led_color([0, 0, 0, 0])

    def turn_on_led(self):
        print(f"{self.brand} LED lights are turned on")
        print(f"rgbw: {self.rgbw.get_led_color()}")
        self.comm.open()
        self.comm.send(self.rgbw.get_led_color())

    def turn_off_led(self):
        print(f"{self.brand} LED lights are turned off")
        self.rgbw.set_led_color([0, 0, 0, 0])
        print(f"rgbw: {self.rgbw.get_led_color()}")
        self.comm.send(self.rgbw.get_led_color())
        self.comm.close()

    def toggle_led(self):
        print(f"{self.brand} LED lights are toggled")
        if self.rgbw.get_led_color() == [0, 0, 0, 0]:
            self.rgbw.set_led_color([255, 255, 255, 255])
            self.turn_on_led()
        else:
            self.turn_off_led()

    def get_max_brightness(self):
        return self.MAX_BRIGHTNESS


if __name__ == "__main__":
    serial_comm = SerialComm("COM1", 9600)

    led = Led("WST", serial_comm)

    device_manager = DeviceManager()
    # 聚合：关联的特例。是整体(Led)与部分(RGBW)的关系，部分(Led)可以离开整体(DeviceManager)而单独存在，led可以在device_manager不管理时创建和使用
    device_manager.add_device(led)
    device_manager.initialize_all()

    led.rgbw.set_led_color([255, 255, 255, 255])
    led.turn_on_led()
    led.toggle_led()
