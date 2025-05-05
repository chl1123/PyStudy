"""
使用 python-can 内置的虚拟总线来模拟发送和接收。
无需任何 CAN 硬件。
发送线程每0.5s在虚拟总线上发送ID为0x7E0的随机数据，接收通知器会将接收到的消息打印到控制台，并使用内置的 can.Logger 通知器将其写入 asc 日志文件。
"""
import can
import threading
import time
import random
import queue


def print_message(msg: can.Message):
    # 将数据转换为整数列表
    data_ints = list(msg.data)
    print(f"ID={hex(msg.arbitration_id)}, Data={data_ints}")


class tx_thread_cl:

    def __init__(self, bus):
        self.bus = bus
        self.running = True
        self.thread = threading.Thread(target=self.tx_callback, args=(self.bus,), daemon=True, name="send")
        self.finished = False

    def start(self):
        self.thread.start()

    def tx_callback(self, bus):
        while self.running:
            data = [random.randint(0, 255) for _ in range(8)]  # 生成0-255更真实的CAN数据
            print(f"Send={data}")
            # 发送CAN帧: 发送一条包含随机数据的CAN消息（ID为 0x7E0，数据长度8字节）
            msg = can.Message(is_extended_id=False, arbitration_id=0x7E0, data=data)
            bus.send(msg)
            time.sleep(0.00001)
        self.finished = True

    def stop(self):
        self.running = False
        self.thread.join()

def sender_simulator():
    # 发送部分 (TX)
    # 创建另一个虚拟CAN通道（与接收使用相同通道）
    bus_tx = can.interface.Bus('virtual_ch', interface='virtual')
    tx_service = tx_thread_cl(bus_tx)
    tx_service.start()

def receiver_simulator():
    # 接收部分 (RX)
    bus_rx = can.interface.Bus('virtual_ch', interface='virtual')
    while True:
        msg = bus_rx.recv(timeout=0.1)  # 非阻塞读取
        if msg is not None:
            print(f"recv={list(msg.data)}")
    bus_rx.shutdown()

def notifier_receiver_simulator():
    # 接收部分 (RX)
    # 创建一个虚拟CAN通道 virtual_ch，用于接收消息

    # channel: 指定通信通道（如 'virtual_ch'），int或str。若为 None，则自动从默认配置中解析。
    # interface: 指定使用的 CAN 接口名称（如 'virtual', 'socketcan', 'pcan' 等）。若为 None，则从配置中自动获取。
    # config_context: 配置上下文，用于选择配置文件中的特定 section（例如 'test_mode'）。
    # ignore_config: 若为 True，忽略所有配置文件，仅使用传入的参数初始化总线。
    bus_rx = can.interface.Bus('virtual_ch', interface='virtual')
    logger = can.Logger("logfile.asc")  # save log to asc file
    # 设置两个监听器
    listeners = [
        print_message,  # Callback function, 打印接收到的消息
        logger,  # 消息记录到文件 logfile.asc 中
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


def method_receiver_simulator():
    bus_rx = can.interface.Bus('virtual_ch', interface='virtual')

    while True:
        latest_msg = None
        # 快速清空缓冲区并保留最后一条消息
        while True:
            msg = bus_rx.recv(timeout=0.1)  # 非阻塞读取
            print(f"{msg=}")
            if msg is None:
                break
            latest_msg = msg  # 持续覆盖直到获取最新消息

        if latest_msg:
            print(f"recv={list(latest_msg.data)}")

        time.sleep(5)  # 保持低CPU占用

    bus_rx.shutdown()


# ---------------------- 队列接收 ----------------------
class AsyncReceiver:
    def __init__(self, bus):
        self.msg_queue = queue.Queue()
        self.notifier = can.Notifier(bus, [self._handler])

    def _handler(self, msg):
        """异步消息处理（在接收线程中执行）"""
        self.msg_queue.put(msg)

    def get_latest(self):
        """获取最新消息（非阻塞）"""
        latest = None
        while not self.msg_queue.empty():
            latest = self.msg_queue.get_nowait()
        return latest


class OptimizedAsyncReceiver:
    def __init__(self, bus):
        self.notifier = can.Notifier(bus, [self._handler])
        self._latest_msg = None  # 直接存储最新消息，避免队列

    def _handler(self, msg):
        self._latest_msg = msg  # 原子操作，无需锁

    def get_latest(self):
        latest = self._latest_msg
        self._latest_msg = None  # 清空
        return latest

def queue_receiver_simulator():
    bus = can.interface.Bus('virtual_ch', interface='virtual')
    # 获取队列最后一个消息
    # receiver = AsyncReceiver(bus)
    # 直接获取最新消息
    receiver = OptimizedAsyncReceiver(bus)
    logger = can.Logger("logfile.asc")  # 日志记录器

    try:
        while True:
            # 获取最新消息（非阻塞）
            latest = receiver.get_latest()
            if latest:
                print(f"recv: {list(latest.data)}")
                logger(latest)  # 记录到日志文件

            time.sleep(5)  # 保持低CPU占用

    except KeyboardInterrupt:
        pass
    finally:
        receiver.notifier.stop()
        bus.shutdown()

def main():
    sender_simulator()

    # 循环接收
    # receiver_simulator()

    # 快速清空缓冲区并保留最后一条消息
    # method_receiver_simulator()

    # 通知+回调
    # notifier_receiver_simulator()

    # 通知+获取最新消息
    queue_receiver_simulator()

if __name__ == "__main__":
    main()