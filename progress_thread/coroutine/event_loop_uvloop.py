"""
uvloop是一个高性能的事件循环，它是asyncio的替代品，可以提高asyncio的性能
asgi uvicorn内部就是使用的uvloop的事件循环
windows下安装uvloop会报错，因为uvloop是基于libuv的，而libuv是一个跨平台的异步I/O库，它是Node.js的事件循环和异步I/O模型的跨平台实现
"""
import asyncio
import uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


# 编写asyncio的代码，与之前写的代码一致。
async def func():
    print("coroutine start")


# 调用协程函数，返回一个协程对象。
result = func()

# 内部的事件循环自动化会变为uvloop
asyncio.run(result)
