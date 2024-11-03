import asyncio


class AsyncContextManager:
    def __init__(self, conn=None):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return "do something"

    async def __aenter__(self):
        print("__aenter__")
        # 异步链接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("__aexit__")
        # 异步关闭数据库链接
        await asyncio.sleep(1)


async def func():
    # 异步上下文管理器
    # 自动执行 __aenter__ 方法，返回值赋值给 f
    async with AsyncContextManager("mysql") as f:
        result = await f.do_something()
        print(result)
    # 自动执行 __aexit__ 方法


asyncio.run(func())
