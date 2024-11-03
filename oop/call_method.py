class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def __call__(self, *args, **kwargs):
        print("call method")


if __name__ == "__main":
    s = School("apeland", "beijing")
    s()  # 实例名() 执行__call__方法
    School("fdsaf", "shanghai")()  # 类名()() 执行__call__方法
