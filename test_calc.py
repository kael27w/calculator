import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc()

    def test_add(self):
        
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0) # Edge Case: Negative numbers
        self.assertEqual(self.calc.add(-5, -5), -10) # Edge Case: Two negative numbers

    def test_sub(self):
       
        self.assertEqual(self.calc.sub(3, 2), 1)
        self.assertEqual(self.calc.sub(-1, 1), -2) # Edge Case: Negative numbers
        self.assertEqual(self.calc.sub(-5, -2), -3) # Edge Case: Two negative numbers

    def test_mul(self):
        
        self.assertEqual(self.calc.mul(2, 3), 6)
        self.assertEqual(self.calc.mul(5, 0), 0) # Edge Case: Multiplication by zero
        self.assertEqual(self.calc.mul(-2, 5), -10) # Edge Case: Negative numbers

    def test_div(self):
       
        self.assertEqual(self.calc.div(8, 4), 2)
        self.assertEqual(self.calc.div(5, 2), 2.5) # Edge Case: Floating point division
        # Edge Case: Test for division by zero, which should raise an error
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(10, 0)

    def test_pow(self):
        
        self.assertEqual(self.calc.pow(2, 3), 8)
        self.assertEqual(self.calc.pow(5, 0), 1) # Edge Case: Power of zero is 1

    def test_sqrt(self):
        
        self.assertEqual(self.calc.sqrt(9), 3)
        self.assertEqual(self.calc.sqrt(0), 0) # Edge Case: Square root of zero
        self.assertAlmostEqual(self.calc.sqrt(2), 1.41421356) # Edge Case: Floating point result