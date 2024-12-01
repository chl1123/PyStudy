from pynng import Pair0

s2 = Pair0()
s2.dial('tcp://127.0.0.1:54321')
print(s2.recv())
s2.close()