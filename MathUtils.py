# MathUtils - A program that can factorial or square a given value
class Cal:
    def __init__(self, a):
        self.a = a

    def factor(self):
        return self.a+self.a

    def square(self):
        return self.a*self.a

    a = int(input("Enter number: "))
    obj = Cal(a)


# print ("Math Utils program")
# print ("Select Operation:")
# print ("1. Factorial")
# print ("2. Square")
