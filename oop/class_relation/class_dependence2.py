class Battery:
    def __init__(self, brand):
        self.__brand = brand
        self.__charge_voltage = 0
        self.__charge_current = 0
        self.__percentage = 20
        self.__cycle = 0
        self.__temperature = 0

    def get_percentage(self):
        return self.__percentage


class Led:
    # 类属性
    DEFAULT_COLOR = True
    MAX_BRIGHTNESS = 255

    def __init__(self, brand, rgbw):
        # 成员属性 实例属性
        self.brand = brand
        self.rgbw = rgbw

    def set_led_color(self, rgbw):
        self.rgbw = rgbw
        print(f"{self.brand} LED lights are set to {rgbw}")

    def set_color_by_battery(self, battery):
        # 依赖：Led对象中的方法不能获取电量，将Battery对象作为参数传入，依赖Battery对象的get_percentage()方法
        percentage = battery.get_percentage()
        if percentage > 80:
            self.set_led_color([255, 0, 0, 255])
        elif percentage > 60:
            self.set_led_color([255, 255, 0, 255])
        elif percentage > 40:
            self.set_led_color([0, 255, 0, 255])
        elif percentage > 20:
            self.set_led_color([0, 0, 255, 255])
        else:
            self.set_led_color([255, 0, 255, 255])
        print(f"rgbw: {self.rgbw}")

    def turn_on_led(self):
        print(f"{self.brand} LED lights are turned on")
        print(f"rgbw: {self.rgbw}")

    def turn_off_led(self):
        print(f"{self.brand} LED lights are turned off")
        self.rgbw = [0, 0, 0, 0]
        print(f"rgbw: {self.rgbw}")

    def toggle_led(self):
        print(f"{self.brand} LED lights are toggled")
        if self.rgbw == [0, 0, 0, 0]:
            self.turn_on_led()
        else:
            self.turn_off_led()

    def get_max_brightness(self):
        return self.MAX_BRIGHTNESS


if __name__ == "__main__":
    top_band_battery = Battery("WST")
    wst_led = Led("WST", [255, 255, 255, 255])
    wst_led.turn_on_led()
    wst_led.set_color_by_battery(top_band_battery)
