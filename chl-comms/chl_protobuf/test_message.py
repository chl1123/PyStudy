import sys

sys.path.append("proto")
import proto.message_odometer_pb2 as message_odometer

"""
标准的Message方法：
    IsInitialized(): checks if all the required fields have been set.
    __str__(): returns a human-readable representation of the message, particularly useful for debugging. (Usually invoked as or .)str(message)print message
    CopyFrom(other_msg): overwrites the message with the given message’s values.
    Clear(): clears all the elements back to the empty state.
"""

"""
如果分配一个未在.proto文件中定义的字段，则会引发AttributeError
如果将字段分配给错误类型的值，则会引发TypeError
在设置字段之前读取字段的值将返回默认值
"""


def init_odometer():
    odo = message_odometer.Message_Odometer()
    odo.cycle = 1000
    odo.x = 0.25
    odo.y = 0.01
    odo.angle = 0.1
    # odo.is_stop = False
    odo.vel_x = 0.1
    odo.vel_y = 0.2
    odo.vel_rotate = 0.3
    # odo.no_such_field = 1  # AttributeError: 'Message_Odometer' object has no attribute 'no_such_field'
    # odo.vel_rotate = "0.3"  # TypeError: '0.3' has type <class 'str'>, but expected one of: ((<class 'numbers.Real'>,),)
    return odo.IsInitialized(), odo


def print_odometer(odo):
    print(f"cycle: {odo.cycle}")
    print(f"x: {odo.x}")
    print(f"y: {odo.y}")
    print(f"angle: {odo.angle}")
    print(f"is_stop: {odo.is_stop}")
    print(f"vel_x: {odo.vel_x}")
    print(f"vel_y: {odo.vel_y}")
    print(f"vel_rotate: {odo.vel_rotate}")


"""
序列化和解析
    SerializeToString()： 序列化消息并将其作为字符串返回。 请注意，字节是二进制的，而不是文本;我们只将类型用作 方便的容器。str
    ParseFromString(data)：从给定的字符串中解析消息
"""


def serialize_odometer(odo):
    return odo.SerializeToString()


def parse_odometer(data):
    odo = message_odometer.Message_Odometer()
    odo.ParseFromString(data)
    return odo


if __name__ == "__main__":
    is_init, odo = init_odometer()
    if is_init:
        print("Odometer is initialized")
        print(odo)

    put_data = serialize_odometer(odo)
    print("put:\n", put_data)

    get_data = parse_odometer(put_data)
    print("get:\n", get_data)
    print("is_stop: ", get_data.is_stop)
    # odo_copy.CopyFrom(odo)
    # odo.Clear()
