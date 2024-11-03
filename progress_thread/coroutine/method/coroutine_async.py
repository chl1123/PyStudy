import asyncio


async def func1():
    # time.sleep(10)  # 阻塞操作，会导致其他协程无法执行
    print(1)
    await asyncio.sleep(2)  # await + 阻塞操作，会自动切换到其他协程执行
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(3)  # 遇到阻塞操作时，会自动切换到其他协程执行
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(tasks))
