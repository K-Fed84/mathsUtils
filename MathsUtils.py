# MathUtils - A program that can factorial or square a given value


class Calculator:

    global num, calc
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
    calc = (input("Enter 'factorial' or 'square':"))


if calc == 'factorial':
    def factorial_calc(num):
        n = 1
        while num > 1:
            n *= num
            num -= 1
        return n

    print(factorial_calc(num))

elif calc == 'square':
    def square_calc(num):
        squared = num ** 2
        return squared

    print(square_calc(num))

else:
    print("Invalid operator")