import os
import time
from multiprocessing import Process

print("pid: ", os.getpid())
num = 100


def func():
    global num
    num -= 1


if __name__ == '__main__':
    process_list = []
    for i in range(10):
        p = Process(target=func)
        p.start()
        process_list.append(p)
    t2 = time.time()
    for p in process_list:
        p.join()

    print(num)  # 100
