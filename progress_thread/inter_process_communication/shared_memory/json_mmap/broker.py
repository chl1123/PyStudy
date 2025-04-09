import mmap
import time

from progress_thread.inter_process_communication.shared_memory.json_mmap.jsonmmap import ObjectMmap
import random


def main():
    mm = ObjectMmap(-1, 1024 * 1024, access=mmap.ACCESS_WRITE, tagname='share_mmap')
    while True:
        task = {
            "operation": "jack",
            "length": random.randint(1, 100),
        }
        if mm.jsonwrite(task):
            print(f"{task=}")
            time.sleep(5)
        else:
            print("Failed to write object")

if __name__ == '__main__':
    main()