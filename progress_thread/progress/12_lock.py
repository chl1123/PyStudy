import json, time
from multiprocessing import Process, Lock

# 多进程同时打开操作同一个文件，就会出现资源冲突导致的报错问题。
# 这里体现的就是多进程并发/并行情况下会带来数据操作的过程中一致性问题。（表现在商品超卖，转账结果出错等情况）


def get_ticket(username):
    """查询余票"""
    time.sleep(0.01)
    data = json.load(open("ticket.txt"))
    print(f"{username}查询余票：{data['count']}")


def buy_ticket(username):
    """购买车票"""
    time.sleep(0.1)
    data = json.load(open("ticket.txt"))

    # 判断如果有票，则购买
    if data["count"] > 0:
        data["count"] -= 1  # 买票
        print(f"{username}购买车票成功!")
    else:
        print(f"{username}购买车票失败!")
    time.sleep(0.1)
    json.dump(data, open("ticket.txt", "w"))


def task(username, lock):
    """购票流程"""
    get_ticket(username)
    # 给需要加锁的代码设置加锁（拿钥匙）和解锁（换钥匙）操作
    # lock.acquire()  # 加锁
    # buy_ticket(username)  # acquire与release就属于被加锁的代码，它是基于同步阻塞方式运行的
    # lock.release()  # 解锁
    # 尽量采用with lock的方式对程序进行加锁，这样的话，即便被加锁的代码发生错误了，也可以自动解锁
    with lock:  # __enter__ 和 __exit__ -> finally -> 解锁
        buy_ticket(username)

if __name__ == '__main__':
    # 在进程中，创建锁
    lock = Lock()
    for i in range(10):
        # 把锁传递到需要加锁的每个子进程中
        p = Process(target=task, args=(f"user-{i}", lock))
        p.start()