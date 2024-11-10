import queue
import time
import threading
import inspect
import ctypes

# 同步方法
def sync_method():
    for i in range(5):
        print('sync_method:', i)
        time.sleep(1)
    return True


# 异步方法
def async_method():
    t = threading.Thread(target=sync_method)
    t.start()
    return t

# 其他任务
def other():
    print('other start')
    time.sleep(2)
    print('other end')


# 1. 同步阻塞
def sync_block():
    sync_method()
    other()


class MyThread(object):
    '''
    手动终止线程的方法
    '''

    def __init__(self, func, argsTup=()):
        self.myThread = threading.Thread(target=func, args=argsTup)

    def start(self):
        print('线程启动')
        self.myThread.start()

    def state(self):
        status = self.myThread.is_alive()
        print('线程状态: {0}'.format(status))
        return status

    def stop(self):
        print('线程终止')
        try:
            for i in range(5):

                self._async_raise(self.myThread.ident, SystemExit)
                time.sleep(1)

        except Exception as e:
            print(e)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")


class Polling:
    def __init__(self):
        self.result = {}
        self.__queue = queue.Queue()
        self.__thread = threading.Thread(target=self.__run)
        self.__thread.start()

    def add(self, id):
        self.__queue.put(id)
        print("self.__thread.is_alive():", self.__thread.is_alive())

    def __run(self):
        while True:
            try:
                id = self.__queue.get(timeout=3)  # 使用超时机制来检查队列是否为空
                print("id: ", id)
                self.result[id] = sync_method()
                self.__queue.task_done()
            except queue.Empty:
                print("queue is empty")
                break

    def get(self, id):
        # 判断id是否在result中
        return self.result.get(id, None)


# 2. 同步非阻塞
def sync_nblock():
    poll = Polling()
    poll.add(1)
    while True:
        result = poll.get(1)
        other()
        print("sync_nblock result:", result)
        if result:
            print("sync_nblock end")
            break
        time.sleep(1)

# 3. 异步(非阻塞)
def async_nblock():
    t = async_method()
    other()
    t.join()
    return True


if __name__ == '__main__':
    print('-----------------sync block-----------------')
    # 同步阻塞
    sync_block()

    print('-----------------sync non-block-----------------')
    # 同步非阻塞
    sync_nblock()

    print('-----------------async non-block-----------------')
    # 异步非阻塞
    async_nblock()
    print('end')