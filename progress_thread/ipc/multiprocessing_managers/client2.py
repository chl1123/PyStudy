from progress_thread.ipc.multiprocessing_managers.client1 import client
import time

if __name__ == '__main__':
    # 使用客户端
    print(client.get_state())
    while True:
        time.sleep(1)
        print(client.get_state())
