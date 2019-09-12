# MathUtils - A program that can factorial or square a given value
import argparse


def main():

    # Setup argument parser
    parser = argparse.ArgumentParser(description='mathsUtils can factorial or square a given number')
    parser.add_argument('--type', dest='operator', required=True, type=str, choices=['factorial', 'square'],
                        help='Enter factorial or square')
    parser.add_argument('--number', dest='integer', required=True, type=int,
                        help='Enter a positive integer')

    # Process arguments
    args = parser.parse_args()
    calc = args.operator
    num = args.integer

    # Factorial and square methods
    def factorial_calc(num):
        n = 1
        while num > 1:
            n *= num
            num -= 1
        return n

    def square_calc(num):
        squared = num ** 2
        return squared

    # Deciding operation
    if calc == 'factorial':
        print(factorial_calc(num))
    elif calc == 'square':
        print(square_calc(num))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print("exiting")