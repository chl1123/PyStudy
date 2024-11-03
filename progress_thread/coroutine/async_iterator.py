"""
使用迭代器的好处
1. 节省内存：
    好处：迭代器一次只生成一个元素，而不是一次性将所有元素加载到内存中。这对于处理大数据集或无限数据流非常有用，可以显著减少内存占用。
    例子：读取大文件时，使用迭代器逐行读取，而不是一次性读取整个文件。
2. 延迟计算：
    好处：迭代器在需要时才生成下一个元素，这称为延迟计算。这种特性使得可以在生成数据的过程中进行复杂的计算，而不会提前消耗资源。
    例子：生成斐波那契数列时，使用迭代器可以按需生成下一个数，而不是预先计算所有数。
3. 代码简洁：
    好处：使用迭代器可以使代码更加简洁和易读。Python 的 for 循环可以直接遍历迭代器，无需手动管理索引或状态。
    例子：
    for item in my_iterator:
        print(item)
"""
import asyncio


class Reader(object):
    """ 自定义异步迭代器（同时也是异步可迭代对象） """

    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    # 返回异步迭代器对象本身
    def __aiter__(self):
        return self

    # 返回容器中的下一个元素的协程对象，如果容器中没有更多元素，则抛出 StopAsyncIteration 异常
    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    # 创建异步可迭代对象
    async_iter = Reader()
    # async for 必须要放在async def函数内，否则语法错误。
    async for item in async_iter:
        print(item)


asyncio.run(func())
