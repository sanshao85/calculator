"""
计算器功能示例脚本
此脚本展示了如何以编程方式使用计算器的各种功能
"""

from calculator import (
    add, subtract, multiply, divide, power, sqrt,
    sin, cos, tan, log10, ln, abs_val, factorial, sci_notation
)

def run_examples():
    print("计算器功能示例:")
    print("-" * 40)
    
    # 基本运算示例
    print("基本运算:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")
    print("-" * 40)
    
    # 幂运算和平方根
    print("幂运算和平方根:")
    print(f"2^3 = {power(2, 3)}")
    print(f"√16 = {sqrt(16)}")
    print("-" * 40)
    
    # 三角函数
    print("三角函数 (角度制):")
    print(f"sin(30°) = {sin(30)}")
    print(f"cos(60°) = {cos(60)}")
    print(f"tan(45°) = {tan(45)}")
    print("-" * 40)
    
    # 对数函数
    print("对数函数:")
    print(f"log10(100) = {log10(100)}")
    print(f"ln(2.718) = {ln(2.718)}")
    print("-" * 40)
    
    # 其他函数
    print("其他数学函数:")
    print(f"abs(-5) = {abs_val(-5)}")
    print(f"5! = {factorial(5)}")
    print(f"1234 (科学计数法) = {sci_notation(1234)}")
    print("-" * 40)
    
    # 链式计算示例
    print("链式计算示例:")
    result = add(2, 3)
    result = multiply(result, 4)
    result = sqrt(result)
    print(f"√((2 + 3) * 4) = {result}")
    print("-" * 40)

if __name__ == "__main__":
    run_examples() 