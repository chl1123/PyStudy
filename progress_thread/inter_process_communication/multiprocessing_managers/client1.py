from progress_thread.inter_process_communication.multiprocessing_managers.server import MyManager
import time


class Client:
    def __init__(self, address, authkey):
        self.manager = MyManager(address=address, authkey=authkey)
        self.manager.connect()
        self.shared_state = self.manager.get_shared_state()
        print(f"Connected to shared state: {self.shared_state}")

    def update_state(self, key, value):
        self.shared_state.set_state(key, value)
        print(f"Updated state: {key} -> {value}")

    def get_state(self):
        return self.shared_state.get_state()


client = Client(('localhost', 5017), b'abracadabra')

if __name__ == '__main__':
    # 使用客户
    client.update_state('chl', 'chl')
    print(client.get_state())
    while True:
        time.sleep(1)
        print(client.get_state())
