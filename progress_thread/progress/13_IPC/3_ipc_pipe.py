from multiprocessing import Process, Queue, Pipe


def ipc_pipe():
    # 创建一个管道，返回值是一个元组，对应的就是管道的两端（可以用于进行输入输出）
    con1, con2 = Pipe()
    p = Process(target=computing, args=("10+20+30", con1)).start()
    # 接受来自管道的另一端发送过来的数据
    print("队列中的结果：", con2.recv())


def computing(exp, con1):
    ret = eval(exp)
    print("eval的计算结果：", ret)
    # 往管道的另一端发送数据
    con1.send(ret)


if __name__ == '__main__':
    ipc_pipe()