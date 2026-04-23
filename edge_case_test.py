import unittest

from main import division, integer_division, SQRT

class TestCalculatorEdgeCases(unittest.TestCase):

    
    def test_division_by_zero(self):
        """Test that division by zero raises ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            division(10, 0, "Division by zero should raise an error")

    def test_integer_division_by_zero(self):
        """Test that integer division by zero raises ZeroDivisionError"""
        with self.assertRaises(ZeroDivisionError):
            integer_division(10, 0, "Integer division by zero should raise an error")

    
    def test_float_precision_addition(self):
        """Test floating point precision with problematic floats"""
        result = 0.1 + 0.2
        self.assertAlmostEqual(result, 0.3, places=7, msg="Float precision test failed")

    def test_float_precision_division(self):
        """Test division precision"""
        result = division(1, 3) * 3
        self.assertAlmostEqual(result, 1.0, places=7, msg="Division precision test failed")

    
    def test_sqrt_negative_number(self):
        """Test that sqrt of negative number raises ValueError"""
        with self.assertRaises(ValueError):
            
            SQRT(-9, "Square root of negative number should raise an error")  

    def test_sqrt_zero(self):
        """Test square root of zero"""
        result = SQRT(0)
        self.assertEqual(result, 0, "Square root of zero should be zero")

    def test_sqrt_positive_perfect_square(self):
        """Test square root of perfect square"""
        result = SQRT(16)
        self.assertEqual(result, 4.0, "Square root of 16 should be 4.0")

    def test_sqrt_large_number(self):
        """Test square root of large number"""
        result = SQRT(1000000)
        self.assertEqual(result, 1000.0, "Square root of 1000000 should be 1000.0")

if __name__ == '__main__':
    unittest.main()