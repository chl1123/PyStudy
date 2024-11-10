from multiprocessing import Queue, Process


def queue_demo():
    """创建一个队列"""
    # q = Queue()  # 不定长的队列
    q = Queue(5)   # 定长的队列

    """添加数据到队列中"""
    q.put("a")  # 一次添加一个数据到队列中
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)
    print("~~~~")
    # q.put(6)
    # 对于定长队列，如果队列满了，再次使用put会进入阻塞状态，直到另一个进程从队列中提取数据项，让队列腾出空间
    print(q.qsize())  # 查看队列中的数据项数量

    """从队列提取数据"""
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.qsize())   # 队列中的数据项全部提取以后，qsize就为0
    print("继续提取数据...")
    # print(q.get())
    # 对于空队列，如果使用get提取数据项，因为没有数据，所以当前进程会进入阻塞状态，直到另一个进程添加数据项到队列中。


def ipc_queue():
    # 创建一个队列
    q = Queue()
    # 把队列对象作为参数传递给需要通信的子进程中
    p = Process(target=computing, args=("10+20+30", q)).start()
    # 从队列中提取数据
    print("队列中的结果：", q.get())


def computing(exp, queue):
    # 把传递进来的exp字符串当成python代码来运行，并把结果返回给主进程
    ret = eval(exp)
    print("eval的计算结果：", ret)
    # 把结果保存到队列queue中
    queue.put(ret)


if __name__ == '__main__':
    queue_demo()

    ipc_queue()
