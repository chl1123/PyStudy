# worker.py
from shared_memory_queue import SharedMemoryQueue
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)



def main(worker_name: str):
    queue = SharedMemoryQueue(name=worker_name)
    logger.info(f"工作进程 {worker_name} 已启动，等待任务...")

    try:
        while True:
            task = queue.get(timeout=10.0)  # 阻塞等待，最多10秒超时
            if task:
                logger.info(f"工作进程 {worker_name} 正在处理: {task}")
            else:
                logger.info("超时，重试...")
    finally:
        # 确保资源清理（Worker只需要close，不需要unlink）
        queue.close()
        logger.info(f"工作进程 {worker_name} 已关闭队列")


if __name__ == "__main__":
    worker_name = "jack"
    try:
        main(worker_name)
    except KeyboardInterrupt:
        logger.info(f"工作进程 {worker_name} 正在退出")