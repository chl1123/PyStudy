#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio
import uvicorn
import aioredis
from fastapi import FastAPI

app = FastAPI()

REDIS_POOL = None


async def init_redis_pool():
    global REDIS_POOL
    REDIS_POOL = await aioredis.Redis.from_url(
        'redis://47.193.14.198:6379',
        password="root123",
        minsize=1,
        maxsize=10
    )


@app.on_event("startup")
async def startup():
    await init_redis_pool()


@app.on_event("shutdown")
async def shutdown():
    if REDIS_POOL:
        await REDIS_POOL.close()


@app.get("/")
def index():
    """ 普通操作接口 """
    return {"message": "Hello World"}


@app.get("/red")
async def red():
    """ 异步操作接口 """
    print("请求来了")

    await asyncio.sleep(3)

    if not REDIS_POOL:
        return {"error": "Redis pool not initialized"}

    # 从连接池获取一个连接
    conn = await REDIS_POOL.acquire()
    try:
        # 设置值
        await conn.hset('car', mapping={'key1': 1, 'key2': 2, 'key3': 3})

        # 读取值
        result = await conn.hgetall('car', encoding='utf-8')
        print(result)
    finally:
        # 归还连接
        REDIS_POOL.release(conn)

    return result


if __name__ == '__main__':
    uvicorn.run("aio_fastapi:app", host="127.0.0.1", port=5000, log_level="info")
