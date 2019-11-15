import unittest
# import calculator as cl
import MathsUtils


class TestCalc(unittest.TestCase):

    def test_factorial(self):
        result = MathsUtils.factorial_calc(2)
        self.assertEqual(result, 2)

        if __name__ == "__main__":
            unittest.main()