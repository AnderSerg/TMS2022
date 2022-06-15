import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_add_float(self):
        self.assertEqual(self.calculator.add(2.0, 2), 4.0)

    @unittest.expectedFailure
    def test_add_efail(self):
        self.assertEqual(self.calculator.add(1, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_subtract_float(self):
        self.assertEqual(self.calculator.subtract(10.0, 5), 5.0)

    @unittest.expectedFailure
    def test_subtract_efail(self):
        self.assertEqual(self.calculator.subtract(15, 3), 10)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 7), 21)

    def test_multiply_float(self):
        self.assertEqual(self.calculator.multiply(3.0, 7), 21.0)

    @unittest.expectedFailure
    def test_multiply_efail(self):
        self.assertEqual(self.calculator.multiply(3, 6), 20)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)

    def test_divide_float(self):
        self.assertEqual(self.calculator.divide(10.0, 2), 5.0)

    @unittest.expectedFailure
    def test_divide_efail(self):
        self.assertEqual(self.calculator.divide(10, 3), 5)


if __name__ == "__main__":
    unittest.main()
