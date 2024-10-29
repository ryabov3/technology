import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(10, 2), 10)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 2), 8)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(10, 2), 20)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(16, 8), 2)

if __name__ == "__main__":
    unittest.main()