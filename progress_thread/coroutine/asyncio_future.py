"""
Future使用的不多，一般使用Task对象，Task对象是Future的子类

Task和Future的区别：
    Task包装协程对象，将协程对象加入到事件循环中
    Task对象绑定的方法执行完毕后，会自动调用set_result方法，设置Future对象的结果
    Future需要手动设置调用set_result方法，设置Future对象的结果
"""

import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")


async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象），没绑定任何行为，则这个任务永远不知道什么时候结束。
    fut = loop.create_future()

    # 创建一个任务（Task对象），绑定set_after函数，函数内部在2s之后，会给fut赋值
    # 即手动设置future任务的最终结果，那么fut就可以结束了
    await loop.create_task(set_after(fut))

    # 等待 Future对象获取 最终结果，否则一直等下去
    data = await fut
    print(data)


asyncio.run(main())
