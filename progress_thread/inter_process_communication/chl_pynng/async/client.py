import time

import pynng
import trio

async def send_and_recv(sender, message):
    await sender.asend(message)

with pynng.Pair0(listen='tcp://127.0.0.1:54321') as s1:
    trio.run(send_and_recv, s1, b'hello there old pal!')
    time.sleep(10)