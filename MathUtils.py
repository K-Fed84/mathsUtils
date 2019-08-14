# MathUtils - A program that can factorial or square a given value

# def factorial(x):
#    n = 1
#    while x > 1:
#        n *= x
#        x -= 1
#    return n
#
# print (factorial(3))




class Calculator:

    num = int(input("Enter a number: "))

    def factorial(num):
        n = 1
        while num > 1:
            n *= num
            num -= 1
        return n

    print(factorial(num))




    # def square(num):
    #     squared = num ** 2
    #     return squared
    #
    # print(square(num))




# print ("Math Utils program")
# print ("Select Operation:")
# print ("1. Factorial")
# print ("2. Square")
