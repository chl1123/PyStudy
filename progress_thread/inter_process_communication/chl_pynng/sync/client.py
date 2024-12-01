import time

from pynng import Pair0

s1 = Pair0()
s1.listen('tcp://127.0.0.1:54321')
s1.send(b'Well hello there')
time.sleep(10)
s1.close()
