# shared_memory_broker.py
from shared_memory_queue import SharedMemoryQueue

workers = ["worker1", "worker2", "jack"]

def main():
    i = 0
    while True:
        # 输入发送任务
        task = input("Enter a task: ")
        if task == "q":
            break
        elif task == "jack":
            i += 1
            task = {"task_id": i, "data": f"payload_{i}"}
            if SharedMemoryQueue(name="jack").put(task):
                print(f"Sent task to {workers[i % len(workers)]}: {task}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBroker shutdown gracefully.")