import asyncio
import time


async def read_file(file_name):
    print("coroutine name: ", asyncio.current_task().get_name())
    print("file: ", file_name, "1")
    # 会阻塞，直到遇到await关键字，才会挂起当前协程，切换执行其他协程
    time.sleep(2)
    print("file: ", file_name, "2")
    await asyncio.sleep(2)
    print("coroutine name: ", asyncio.current_task().get_name())
    print("file: ", file_name, "3")
    return True, (file_name, "ok")


async def coroutine_task():
    task = asyncio.create_task(read_file("navigation.wav"), name="read1")
    print("coroutine object: ", task)
    done, pending = await asyncio.wait([task], timeout=3)
    # 判断任务的状态是否完成
    if task.done():
        # 完成时的处理
        print("task is done")
        result = task.result()
    else:
        # 未完成时的处理
        print("task is not done, wait ...")
        result = await task

    print("task.result(): ", result)


async def coroutine_tasks():
    # 通过asyncio.create_task()创建的任务，会自动添加到事件循环的任务列表中，等待事件循环去执行（默认是就绪状态）。
    # 不会立即执行，而是等待事件循环调度执行。
    task_list = [
        asyncio.create_task(read_file("background.wav"), name="readBackground"),
        asyncio.create_task(read_file("Foreground.wav"), name="readForeground")
    ]

    # 先执行第一个协程任务n1，直到n1内部执行await asyncio.sleep(2)时，挂起当前协程任务n1，切换执行其他协程任务n2
    # 当n2执行到await asyncio.sleep(2)时，挂起当前协程任务n2，切换执行其他协程任务n1
    # 此处的await是等待所有协程执行完毕，并将所有协程的返回值保存到done
    # 如果设置了timeout值，则意味着此处最多等待的秒，完成的协程返回值写入到done中，未完成则写到pending中
    done, pending = await asyncio.wait(task_list, timeout=5)
    # 判断这两个任务的状态是否完成，按照任务名分别处理各自的状态
    for task in task_list:
        # 获取任务的名称
        task_name = task.get_name()
        print("----------task_name: ", task_name)
        result = None
        # 判断任务的状态是否完成
        if task_name == "readBackground":
            if task.done():
                # 完成时的处理
                print("task is done: ", task_name)
                result = task.result()
            else:
                # 未完成时的处理
                print("task is not done, wait ...: ", task_name)
                result = await task
        elif task_name == "readForeground":
            if task.done():
                # 完成时的处理
                print("task is done: ", task_name)
                result = task.result()
            else:
                # 未完成时的处理
                print("task is not done, wait ...: ", task_name)
                result = await task
        print("task.result(): ", result)


if __name__ == '__main__':
    print("-----------------single coroutine task---------------")
    asyncio.run(coroutine_task())

    print("--------------------multiple tasks---------------")
    asyncio.run(coroutine_tasks())

    print("------------run external use task list---------------")
    task_list = [read_file("background.wav"), read_file("Foreground.wav")]
    # 错误：task_list = [asyncio.create_task(ead_file("background.wav")), asyncio.create_task(read_file("Foreground.wav"))]
    # 此处不能直接 asyncio.create_task，因为将Task立即加入到事件循环的任务列表，但此时事件循环还未创建，所以会报错。

    # 使用asyncio.wait将列表封装为一个协程，并调用asyncio.run实现执行两个协程
    # asyncio.wait内部会对列表中的每个协程执行ensure_future，封装为Task对象
    done, pending = asyncio.run(asyncio.wait(task_list))
    if done:
        for task in done:
            print("task.result(): ", task.result())
    if pending:
        for task in pending:
            print("task.result(): ", task.result())
