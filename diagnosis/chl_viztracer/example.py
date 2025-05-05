from viztracer import VizTracer

def func():
    for i in range(1000):
        print(i)

def main():
    with VizTracer():
        func()

if __name__ == '__main__':
    main()