import time, random
from multiprocessing import Process


def send_sms(i):
    """模拟发送邮件的方法"""
    # 使用随机数进行程序睡眠，random.random()随机生成0-1之间的小数
    time.sleep(random.random())
    print(f"成功发送第{i}份邮件！")


if __name__ == '__main__':
    t1 = time.time()
    process_list = []
    for i in range(10):
        p = Process(target=send_sms, args=(i,))
        p.start()
        # p.join()  # 同步阻塞，所以会导致整主进程的所有代码，都处于同步阻塞了，使用多进程就变得没有意义了
        process_list.append(p)
    t2 = time.time()
    print(f"创建并启动所有子进程——>所有子进程启动后：{t2-t1}")
    # 先让主进程把所有子进程创建并启动起来，后续才进行阻塞等待所有子进程执行结束
    for p in process_list:
        p.join()
    t3 = time.time()
    print(f"所以子进程启动后——>所有子进程完成（成功发送邮寄）：{t3-t2}")
    print(f"整个发送邮件的过程：{t3-t1}")
    print("所有邮件已经发送成功了！")