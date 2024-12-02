from OOPDemo import Calculator


class Child (Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 1, 2)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()


obj1 = Child()
print(obj1.getCompleteData())