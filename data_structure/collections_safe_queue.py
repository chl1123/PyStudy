import threading
from collections import deque

class SafeQueue:
    def __init__(self, maxlen=None):
        self._queue = deque(maxlen=maxlen)
        self._lock = threading.Lock()

    def append(self, item):
        """向队列添加一个元素"""
        with self._lock:
            self._queue.append(item)

    def popleft(self):
        """从队列移除并返回最左侧的元素"""
        with self._lock:
            if not self._queue:
                raise IndexError("get from an empty queue")
            return self._queue.popleft()

    def peek(self):
        """查看队列中最左侧的元素但不移除它"""
        with self._lock:
            if not self._queue:
                raise IndexError("peek from an empty queue")
            return self._queue[0]

    def is_empty(self):
        """如果队列为空则返回True"""
        with self._lock:
            return len(self._queue) == 0

    def size(self):
        """返回队列中的元素数量"""
        with self._lock:
            return len(self._queue)

    def clear(self):
        """清空队列"""
        with self._lock:
            self._queue.clear()

    def __bool__(self):
        """返回队列是否为空"""
        with self._lock:
            return bool(self._queue)

    def __str__(self):
        """返回队列的字符串表示"""
        with self._lock:
            return str(self._queue)


if __name__ == '__main__':
    queue = SafeQueue(maxlen=3)
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print("queue.size()", queue.size())
    print(queue)
    # 队列已满，添加元素会覆盖旧数据
    queue.append(4)
    print(queue)
    print("queue.size()", queue.size())
    print("pop left: ", queue.popleft())
    print(queue)