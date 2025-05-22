import unittest
import math
from calculator import add, subtract, multiply, divide, power, sqrt
from calculator import sin, cos, tan, log10, ln, abs_val, factorial, sci_notation

class TestCalculator(unittest.TestCase):
    
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(5, 0), "错误：除数不能为零")
        
    def test_power_and_sqrt(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(-1), "错误：不能对负数开平方")
        
    def test_trigonometric_functions(self):
        # 测试三角函数（使用近似值比较）
        self.assertAlmostEqual(sin(30), 0.5, places=2)
        self.assertAlmostEqual(cos(60), 0.5, places=2)
        self.assertAlmostEqual(tan(45), 1, places=2)
        
    def test_logarithmic_functions(self):
        self.assertEqual(log10(100), 2)
        self.assertEqual(log10(0), "错误：不能对非正数取对数")
        self.assertAlmostEqual(ln(math.e), 1, places=10)
        self.assertEqual(ln(-1), "错误：不能对非正数取对数")
        
    def test_other_functions(self):
        self.assertEqual(abs_val(-5), 5)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(-1), "错误：阶乘只适用于非负整数")
        self.assertEqual(factorial(0), 1)
        self.assertEqual(sci_notation(1234), "1.23e+03")
        
if __name__ == "__main__":
    unittest.main() 