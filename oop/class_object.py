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

    def turn_on_led(self):
        print(f"{self.brand} LED lights are turned on")
        print(f"{self.rgbw}")

    def turn_off_led(self):
        print(f"{self.brand} LED lights are turned off")
        self.rgbw = [0, 0, 0, 0]
        print(f"{self.rgbw}")

    def toggle_led(self):
        print(f"{self.brand} LED lights are toggled")
        if self.rgbw == [0, 0, 0, 0]:
            self.turn_on_led()
        else:
            self.turn_off_led()

    def get_max_brightness(self):
        return self.MAX_BRIGHTNESS


# 实例方法
def instance_method(led_obj):
    print(f"\ninstance_method()")
    # 实例出wst_led对象
    led_obj.turn_on_led()
    led_obj.turn_off_led()
    led_obj.toggle_led()
    print(f"instant_method() finished.\n")


# 类属性
def class_property():
    print("\nclass_property()")
    print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}")  # 64
    Led.MAX_BRIGHTNESS = 128  # 类属性可以被修改
    print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}")  # 128
    print("class_property() finished.\n")


# 实例属性
def instance_property():
    print("\ninstance_property()")
    """同名实例属性不会影响类属性"""
    # 1.同名实例属性修改，类属性不会改变
    print("update instance property:")
    wtp_led.MAX_BRIGHTNESS = 64
    print(f"wtp_led.get_max_brightness(): {wtp_led.get_max_brightness()}")  # 64
    print(f"wst_led.MAX_BRIGHTNESS: {wst_led.MAX_BRIGHTNESS}")  # 255
    print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}\n")  # 255

    print("delete instance property:")
    del wtp_led.MAX_BRIGHTNESS
    # 2.删除同名实例属性，类属性不会改变
    # 再次访问同名实例属性，会再次创建一个新的实例属性，默认值为类属性的值
    print(f"wtp_led.get_max_brightness(): {wtp_led.get_max_brightness()}")  # 255
    print(f"wst_led.MAX_BRIGHTNESS: {wst_led.MAX_BRIGHTNESS}")  # 128
    print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}\n")  # 128

    """同名类属性会影响实例属性"""
    # 1.类属性改变，同名实例属性也会改变
    print("update class property:")
    Led.MAX_BRIGHTNESS = 64  # 创建一个新的实例属性，和类属性不属于一个区域
    print(f"wtp_led.get_max_brightness(): {wtp_led.get_max_brightness()}")  # 64
    print(f"wst_led.MAX_BRIGHTNESS: {wst_led.MAX_BRIGHTNESS}")  # 128
    print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}")  # 128

    # 2.删除类属性，同名实例属性也会被删除
    # del Led.MAX_BRIGHTNESS
    # print(f"wtp_led.get_max_brightness(): {wtp_led.get_max_brightness()}") # 64
    # print(f"wst_led.MAX_BRIGHTNESS: {wst_led.MAX_BRIGHTNESS}") # 128
    # print(f"Led.MAX_BRIGHTNESS: {Led.MAX_BRIGHTNESS}") # 128
    print("instance_property() finished.\n")


if __name__ == "__main__":
    wst_led = Led("WST", [255, 255, 255, 255])
    wtp_led = Led("WTP", [255, 255, 255, 255])

    instance_method(wst_led)
    instance_property()
    class_property()
