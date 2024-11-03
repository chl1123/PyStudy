def func1():
    yield 1  # step 1
    yield from func2()  # step 4
    yield 2  # step 5


def func2():
    yield 3  # step 2
    yield 4  # step 3


f1 = func1()

for item in f1:
    print(item)
