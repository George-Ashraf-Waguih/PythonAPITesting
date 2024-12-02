class Calculator:
    num = 100

    #default constructor
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am a method in class")


    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2,3)
obj.getData()
print(obj.num)
print(obj.summation())

obj = Calculator(4,5)
obj.getData()
print(obj.num)
print(obj.summation())