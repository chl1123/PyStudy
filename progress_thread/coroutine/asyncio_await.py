import asyncio


async def read_file(file_name):
    await asyncio.sleep(2)
    return file_name


async def func2():
    # 遇到IO操作挂起当前协程（任务），等IO操作完成之后再继续往下执行。当前协程挂起时，事件循环可以去执行其他协程（任务）。
    # await 后面的代码不会立即执行，而是等待当前协程挂起，切换到其他协程执行，直到IO操作完成之后，再切换回来继续执行。
    response1 = await read_file("navigation.wav")
    print("read file: ", response1)

    response2 = await read_file("error.wav")
    print("read file: ", response2)


if __name__ == '__main__':
    # result = func1()
    result = func2()

    asyncio.run(result)
