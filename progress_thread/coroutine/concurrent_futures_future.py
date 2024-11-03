import asyncio
import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor

import requests


def func(value):
    time.sleep(1)
    print("value", value)
    return value


def thread_pool():
    pool = ThreadPoolExecutor(max_workers=5)
    for i in range(10):
        fut = pool.submit(func, i)
        print("fut: ", fut)


def process_pool():
    pool = ProcessPoolExecutor(max_workers=5)
    for i in range(10):
        fut = pool.submit(func, i)
        print("fut: ", fut)


async def main():
    loop = asyncio.get_running_loop()

    # 1. Run in the default loop's executor ( 默认ThreadPoolExecutor )
    # 第一步：内部会先调用 ThreadPoolExecutor 的 submit 方法去线程池中申请一个线程去执行func函数，并返回一个concurrent.futures.Future对象
    # 第二步：调用asyncio.wrap_future将concurrent.futures.Future对象包装为asycio.Future对象。
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装为 asycio.Future对象 才能使用。
    fut = loop.run_in_executor(None, func, 1)
    result = await fut
    print('default thread pool', result)

    # 2. Run in a custom thread pool:
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, func, 2)
        print('custom thread pool', result)

    # 3. Run in a custom process pool:
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, func, 3)
        print('custom process pool', result)


"""
不支持异步操作的第三方库，使用线程池来配合
"""


async def download_image(url):
    # 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
    print("开始下载:", url)

    loop = asyncio.get_event_loop()
    # requests模块默认不支持异步操作，使用线程池来配合
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')
    # 图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)


def coroutine_and_third_sync():
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]
    tasks = [download_image(url) for url in url_list]
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete( asyncio.wait(tasks) )
    asyncio.run(asyncio.wait(tasks))


if __name__ == "__main__":
    print("-------------------thread_pool-------------------")
    thread_pool()
    print("-------------------process_pool-------------------")
    process_pool()
    print("-------------------asyncio-------------------")
    asyncio.run(main())

    print("-------------------coroutine_and_third_sync-------------------")
    coroutine_and_third_sync()
