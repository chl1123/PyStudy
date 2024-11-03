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


class Led:
    # 类属性
    DEFAULT_COLOR = True
    MAX_BRIGHTNESS = 255

    def __init__(self, brand, rgbw, comm=None):
        # 成员属性 实例属性
        self.brand = brand
        self.rgbw = rgbw
        # 关联：是一种拥有的关系，使Led类知道SerialComm类的属性和方法
        self.comm = comm

    def set_led_color(self, rgbw):
        self.rgbw = rgbw
        print(f"{self.brand} LED lights are set to {rgbw}")

    def turn_on_led(self):
        print(f"{self.brand} LED lights are turned on")
        print(f"rgbw: {self.rgbw}")
        self.comm.open()
        self.comm.send(self.rgbw)

    def turn_off_led(self):
        print(f"{self.brand} LED lights are turned off")
        self.rgbw = [0, 0, 0, 0]
        print(f"rgbw: {self.rgbw}")
        self.comm.send(self.rgbw)
        self.comm.close()

    def toggle_led(self):
        print(f"{self.brand} LED lights are toggled")
        if self.rgbw == [0, 0, 0, 0]:
            self.set_led_color([255, 255, 255, 255])
            self.turn_on_led()
        else:
            self.turn_off_led()

    def get_max_brightness(self):
        return self.MAX_BRIGHTNESS


if __name__ == "__main__":
    serial_comm = SerialComm("COM1", 9600)
    led = Led("WST", [255, 255, 255, 255], serial_comm)
    led.set_led_color([255, 255, 255, 255])
    led.turn_on_led()
    led.toggle_led()
