class Flight(object):
    def __init__(self, name):
        self.flight_name = name
        self.status = 0

    def checking_status(self):
        print("connecting airline company/airport api...... ")
        print("checking flight %s status " % self.flight_name)
        return 1  # 1 arrived , 2 departured , 3 cancel

    @property
    def flight_status(self):  # get
        self.status = self.checking_status()
        if self.status == 0:
            print("flight got canceled...")
        elif self.status == 1:
            print("flight is arrived...")
        elif self.status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")
        return self.status

    @flight_status.setter
    def flight_status(self, status):
        print("changing....flight status..", status)
        self.status = status

    @flight_status.deleter
    def flight_status(self):
        del self.status
        print("del .....")


f = Flight("CA980")
print("flight status: ", f.flight_status)

f.flight_status = 0
print("flight status: ", f.flight_status)

del f.flight_status
