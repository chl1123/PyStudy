"""
下载图片使用第三方模块requests，请提前安装：pip3 install requests
"""
import requests
import time
import aiohttp
import asyncio


def download_image(url):
    print("开始下载：", url)
    # 发送网络请求，下载图片
    response = requests.get(url)
    # 图片保存到本地文件
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)
        time.sleep(2)  # 休眠2秒，模拟网络延迟
        print("下载完成")


def download_images(url_list):
    for url in url_list:
        download_image(url)


async def download_image_async(session, url):
    print("开始下载：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            await asyncio.sleep(2)  # 休眠2秒，模拟网络延迟
            file_object.write(content)
            print("下载完成")


async def download_images_async(url_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in url_list:
            task = asyncio.create_task(download_image_async(session, url))
            tasks.append(task)
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # 下载1张图片需要2秒
    url_list = [
        'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
        'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
        'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
    ]
    # 3张图片，同步下载，总共需要6秒
    # download_images(url_list)

    # 3张图片，协程异步下载图片，总共需要2秒
    asyncio.run(download_images_async(url_list))
