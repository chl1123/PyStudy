import time

import pynng
import trio

async def send_and_recv(receiver):
    return await receiver.arecv()

with pynng.Pair0(dial='tcp://127.0.0.1:54321') as s2:
    received = trio.run(send_and_recv, s2)
    print(received)
    time.sleep(10)
    assert received == b'hello there old pal!'