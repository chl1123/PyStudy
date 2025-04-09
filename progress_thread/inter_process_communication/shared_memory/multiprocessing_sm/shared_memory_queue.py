# shared_memory_queue.py
import json
import logging
import time
import struct
import os
import random
from multiprocessing import Manager, shared_memory
from typing import Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class SharedMemoryQueue:
    """
    使用共享内存实现的进程间通信队列
    内存布局:
    - 0-3字节: 数据长度标记
    - 4-7字节: 消息ID (用于确认消息是否为新消息)
    - 8-11字节: 状态标志 (0=空闲, 1=写入中, 2=可读取, 3=读取中)
    - 12+字节: 实际数据内容
    """

    HEADER_SIZE = 12  # 头部大小：4字节长度 + 4字节消息ID + 4字节状态
    STATUS_IDLE = 0  # 空闲状态
    STATUS_WRITING = 1  # 写入中
    STATUS_READABLE = 2  # 可读取
    STATUS_READING = 3  # 读取中

    def __init__(self, name: str, max_size: int = 4096):
        self.name = name
        # 确保有足够空间存储头部和数据
        self.max_size = max(max_size + self.HEADER_SIZE, 100)
        self.shm = None
        self.message_id = random.randint(1, 1000000)  # 初始消息ID
        self._initialize_shm()

        self.manager = Manager()
        self.cond = self.manager.Condition()  # 跨进程条件变量

    def _initialize_shm(self):
        """初始化共享内存"""
        try:
            # 尝试连接到已存在的共享内存
            try:
                self.shm = shared_memory.SharedMemory(name=self.name)
                logger.info(f"连接到已存在的共享内存: {self.name}")
            except FileNotFoundError:
                # 创建新的共享内存
                self.shm = shared_memory.SharedMemory(
                    name=self.name, create=True, size=self.max_size
                )
                # 初始化头部
                self._set_data_length(0)
                self._set_message_id(0)
                self._set_status(self.STATUS_IDLE)
                logger.info(f"创建新的共享内存: {self.name}")
        except Exception as e:
            logger.error(f"初始化共享内存失败: {e}")
            raise

    def _set_data_length(self, length):
        """设置数据长度"""
        struct.pack_into('!I', self.shm.buf, 0, length)

    def _get_data_length(self):
        """获取数据长度"""
        return struct.unpack_from('!I', self.shm.buf, 0)[0]

    def _set_message_id(self, msg_id):
        """设置消息ID"""
        struct.pack_into('!I', self.shm.buf, 4, msg_id)

    def _get_message_id(self):
        """获取消息ID"""
        return struct.unpack_from('!I', self.shm.buf, 4)[0]

    def _set_status(self, status):
        struct.pack_into('!I', self.shm.buf, 8, status)
        if hasattr(self.shm, '_fd'):  # 仅限Linux/Unix
            os.fsync(self.shm._fd)  # 强制刷写物理内存

    def _get_status(self):
        """获取状态标志"""
        return struct.unpack_from('!I', self.shm.buf, 8)[0]

    def put(self, data: dict, timeout: float = 5.0) -> bool:
        """写入数据到共享内存"""
        start_time = time.time()

        # 序列化数据
        serialized = json.dumps(data).encode('utf-8')

        # 检查数据大小
        if len(serialized) > self.max_size - self.HEADER_SIZE:
            logger.error(f"数据过大: {len(serialized)} 字节, 超过最大限制: {self.max_size - self.HEADER_SIZE} 字节")
            return False

        # 等待队列空闲
        while True:
            status = self._get_status()
            if status == self.STATUS_IDLE or status == self.STATUS_READABLE:
                # 标记为写入中
                self._set_status(self.STATUS_WRITING)
                break

            # 检查超时
            if time.time() - start_time > timeout:
                logger.warning(f"等待写入超时: {self.name}")
                return False
            logger.info(f"等待队列空闲: {self.name}")
            time.sleep(0.01)

        with self.cond:  # 使用条件变量同步
            try:
                # 递增消息ID
                self.message_id += 1

                # 写入数据长度
                self._set_data_length(len(serialized))

                # 写入消息ID
                self._set_message_id(self.message_id)

                # 写入实际数据
                self.shm.buf[self.HEADER_SIZE:self.HEADER_SIZE + len(serialized)] = serialized

                # 标记为可读取
                self._set_status(self.STATUS_READABLE)

                logger.info(f"成功写入数据: {data}, 消息ID: {self.message_id}")
                # 写入完成后通知所有等待者
                self.cond.notify_all()
                return True
            except Exception as e:
                logger.error(f"写入数据失败: {e}")
                # 恢复为空闲状态
                self._set_status(self.STATUS_IDLE)
                return False

    def _check_available(self, last_msg_id: int) -> bool:
        status = self._get_status()
        current_msg_id = self._get_message_id()
        return status == self.STATUS_READABLE and current_msg_id != last_msg_id

    def _process_data(self, last_msg_id: int) -> Optional[dict]:
        try:
            self._set_status(self.STATUS_READING)
            data_len = self._get_data_length()

            if 0 < data_len <= self.max_size - self.HEADER_SIZE:
                data_bytes = bytes(self.shm.buf[self.HEADER_SIZE:self.HEADER_SIZE + data_len])
                data = json.loads(data_bytes.decode('utf-8'))
                self._set_status(self.STATUS_IDLE)
                return data
        except Exception as e:
            logger.error(f"处理数据失败: {e}")
            self._set_status(self.STATUS_IDLE)
        return None

    def get(self, timeout: float = 5.0) -> Optional[dict]:
        """从共享内存读取数据"""
        start_time = time.time()
        last_msg_id = self._get_message_id()
        print(f"get")
        with self.cond:  # 使用条件变量同步
            # 首次检查后立即等待（不要跳过初次等待）
            # self.cond.wait(timeout=0)  # 立即触发一次状态检查

            while True:
                # 第一重检查（快速路径）
                if self._check_available(last_msg_id):
                    return self._process_data(last_msg_id)

                print(f"等待数据: {self.name}")
                remaining = timeout - (time.time() - start_time)
                if remaining <= 0:
                    logger.debug(f"读取超时: {self.name}")
                    return None

                # 延长等待时间并移除print
                self.cond.wait(timeout=min(0.5, remaining))
                # 唤醒后再次检查
                if self._check_available(last_msg_id):
                    return self._process_data(last_msg_id)

    def close(self):
        """关闭共享内存"""
        if self.shm:
            self.shm.close()
            logger.info(f"关闭共享内存: {self.name}")

    def unlink(self):
        """删除共享内存(只有创建者应该调用此方法)"""
        if self.shm:
            try:
                self.shm.unlink()
                logger.info(f"删除共享内存: {self.name}")
            except FileNotFoundError:
                pass


# 使用示例
if __name__ == "__main__":
    # 测试代码
    queue_name = f"test_queue_{os.getpid()}"

    # Broker端
    broker_queue = SharedMemoryQueue(name=queue_name)
    broker_queue.put({"task": "test_data"})

    # Worker端
    worker_queue = SharedMemoryQueue(name=queue_name)
    data = worker_queue.get(timeout=5)
    print(f"接收到数据: {data}")

    # 清理资源
    worker_queue.close()
    broker_queue.close()
    broker_queue.unlink()  # 只有创建者需要unlink