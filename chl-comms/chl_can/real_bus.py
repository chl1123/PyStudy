import can
import threading
import time
import random


def print_message(msg):
    # 将数据转换为整数列表
    data_ints = list(msg.data)
    print(f"ID={hex(msg.arbitration_id)}, Data={data_ints}")


class tx_thread_cl:

    def __init__(self, bus):
        self.bus = bus
        self.running = True
        self.thread = threading.Thread(target=self.tx_callback, args=(self.bus,), daemon=True)
        self.finished = False

    def start(self):
        self.thread.start()

    def tx_callback(self, bus):
        while self.running:
            data = [random.randint(0, 15) for i in range(0, 8)]
            print(f"Send={data}")
            msg = can.Message(is_extended_id=False, arbitration_id=0x7E0, data=data)
            bus.send(msg)
            time.sleep(0.5)
        self.finished = True

    def stop(self):
        self.running = False

def sender_simulator():
    # 发送部分 (TX)
    # 创建另一个虚拟CAN通道（与接收使用相同通道）
    bus_tx = can.interface.Bus(channel='can0', interface='socketcan', bitrate=500000)
    tx_service = tx_thread_cl(bus_tx)
    tx_service.start()

def receiver_simulator():
    bus_rx = can.interface.Bus(channel='can0', interface='socketcan', bitrate=500000)
    logger = can.Logger("logfile.asc")  # save log to asc file
    listeners = [
        print_message,  # Callback function, print the received messages
        logger,  # save received messages to asc file
    ]
    # 监听CAN总线并触发监听器
    notifier = can.Notifier(bus_rx, listeners)

    # 等待用户输入（按回车键），然后退出循环
    running = True
    while running:
        input()
        running = False
    # It's important to stop the notifier in order to finish the writting of asc file
    notifier.stop()
    # stops the bus
    bus_rx.shutdown()


def main():
    sender_simulator()
    receiver_simulator()


if __name__ == "__main__":
    main()
