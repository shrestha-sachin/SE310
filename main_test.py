import unittest as ut

from main import addition, subtraction, multiplication, integer_division, division, SQRT

class testCalculator(ut.TestCase):

    def test_addition(self):

        self.assertEqual(addition(5, 3), 8, "Addition test failed")

    def test_addition(self):

        self.assertEqual(addition(-5, -3), -8, "Addition test failed")

    def test_subtraction(self):

        self.assertEqual(subtraction(5, 3), 2, "Subtraction test failed")

    def test_subtraction(self):

        self.assertEqual(subtraction(-5, -3), -2, "Subtraction test failed")

    def test_multiplication(self):

        self.assertEqual(multiplication(5, 3), 15, "Multiplication test failed")

    def test_integer_division(self):

        self.assertEqual(integer_division(5, 3), 1, "Integer Division test failed")

    def test_division(self):

        self.assertEqual(division(5, 2), 2.5, "Division test failed")

    def test_SQRT(self):

        self.assertEqual(SQRT(16), 4, "Square Root test failed")

if __name__=="__main__":

    ut.main()