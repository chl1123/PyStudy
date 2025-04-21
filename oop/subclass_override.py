
class TaskModule:
    def __init__(self):
        self.has_period_run = self.__is_overridden(self, '_period_run')

    def _period_run(self):
        pass

    @staticmethod
    def __is_overridden(instance, method_name):
        # 检查子类是否重写了指定方法
        return getattr(instance.__class__, method_name) != getattr(TaskModule, method_name)

    def main(self):
        while True:
            if self.has_period_run:
                self._period_run()
            else:
                break

class Jack(TaskModule):
    pass


class WaterTank(TaskModule):
    def _period_run(self):
        print("Jack is running")

if __name__ == '__main__':
    jack = Jack()
    jack.main()

    jack = WaterTank()
    jack.main()