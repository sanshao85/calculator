import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "错误：除数不能为零"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "错误：不能对负数开平方"
    return math.sqrt(x)

# 新增函数：三角函数
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# 新增函数：对数
def log10(x):
    if x <= 0:
        return "错误：不能对非正数取对数"
    return math.log10(x)

def ln(x):
    if x <= 0:
        return "错误：不能对非正数取对数"
    return math.log(x)

# 新增函数：绝对值
def abs_val(x):
    return abs(x)

# 新增函数：阶乘
def factorial(x):
    if x < 0 or int(x) != x:
        return "错误：阶乘只适用于非负整数"
    if x == 0:
        return 1
    return math.factorial(int(x))

# 新增函数：科学计数法转换
def sci_notation(x):
    return f"{x:.2e}"

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("输入无效，请输入一个数字。")

def get_operation_choice(operations):
    while True:
        choice = input("请选择操作：").strip().lower()
        if choice in operations:
            return choice
        else:
            print(f"无效的操作。请输入以下任一操作：{', '.join(operations.keys())}")

def calculator():
    print("欢迎使用命令行计算器！")
    print("您可以执行以下操作：")

    # 内存功能
    memory = 0
    
    operations = {
        # 基本运算
        'add': {'func': add, 'args': 2, 'desc': '加法 (例如: add)'},
        'subtract': {'func': subtract, 'args': 2, 'desc': '减法 (例如: subtract)'},
        'multiply': {'func': multiply, 'args': 2, 'desc': '乘法 (例如: multiply)'},
        'divide': {'func': divide, 'args': 2, 'desc': '除法 (例如: divide)'},
        'power': {'func': power, 'args': 2, 'desc': '幂运算 (例如: power)'},
        'sqrt': {'func': sqrt, 'args': 1, 'desc': '平方根 (例如: sqrt)'},
        
        # 三角函数
        'sin': {'func': sin, 'args': 1, 'desc': '正弦函数，输入角度 (例如: sin)'},
        'cos': {'func': cos, 'args': 1, 'desc': '余弦函数，输入角度 (例如: cos)'},
        'tan': {'func': tan, 'args': 1, 'desc': '正切函数，输入角度 (例如: tan)'},
        
        # 对数函数
        'log10': {'func': log10, 'args': 1, 'desc': '以10为底的对数 (例如: log10)'},
        'ln': {'func': ln, 'args': 1, 'desc': '自然对数 (例如: ln)'},
        
        # 其他数学函数
        'abs': {'func': abs_val, 'args': 1, 'desc': '绝对值 (例如: abs)'},
        'factorial': {'func': factorial, 'args': 1, 'desc': '阶乘 (例如: factorial)'},
        'sci': {'func': sci_notation, 'args': 1, 'desc': '转换为科学计数法 (例如: sci)'},
        
        # 内存操作
        'ms': {'func': lambda x: x, 'args': 1, 'desc': '保存数值到内存 (例如: ms)'},
        'mr': {'func': lambda: memory, 'args': 0, 'desc': '读取内存中的数值 (例如: mr)'},
        'mc': {'func': lambda: 0, 'args': 0, 'desc': '清除内存 (例如: mc)'},
        'm+': {'func': lambda x: memory + x, 'args': 1, 'desc': '将数值加到内存中 (例如: m+)'},
        'm-': {'func': lambda x: memory - x, 'args': 1, 'desc': '从内存中减去数值 (例如: m-)'},
        
        # 退出
        'quit': {'func': None, 'args': 0, 'desc': '退出计算器 (例如: quit)'},
        'help': {'func': None, 'args': 0, 'desc': '显示帮助信息 (例如: help)'}
    }

    # 按类别显示操作
    categories = {
        "基本运算": ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt'],
        "三角函数": ['sin', 'cos', 'tan'],
        "对数函数": ['log10', 'ln'],
        "其他数学函数": ['abs', 'factorial', 'sci'],
        "内存操作": ['ms', 'mr', 'mc', 'm+', 'm-'],
        "系统命令": ['quit', 'help']
    }
    
    def display_help():
        print("\n=== 帮助信息 ===")
        for category, ops in categories.items():
            print(f"\n{category}:")
            for op in ops:
                print(f"- {operations[op]['desc']}")
        print("\n=================")
    
    # 显示帮助信息
    display_help()

    history = []

    while True:
        print("\n-------------------------")
        print(f"内存中的值: {memory}")
        choice = get_operation_choice(operations)

        if choice == 'quit':
            print("感谢使用计算器！再见。")
            break
            
        if choice == 'help':
            display_help()
            continue

        selected_op = operations[choice]
        op_func = selected_op['func']
        num_args = selected_op['args']

        # 处理内存操作
        if choice == 'mr':
            result = memory
            print(f"从内存读取的值: {result}")
            continue
        elif choice == 'mc':
            memory = 0
            print("内存已清除")
            continue

        args_values = []
        if num_args == 1:
            args_values.append(get_number_input(f"请输入进行 {choice} 操作的数字: "))
        elif num_args == 2:
            args_values.append(get_number_input("请输入第一个数字: "))
            args_values.append(get_number_input("请输入第二个数字: "))
        
        result = op_func(*args_values)
        
        # 处理特殊的内存操作
        if choice == 'ms':
            memory = result
            print(f"已将 {result} 保存到内存")
        elif choice == 'm+':
            memory += args_values[0]
            print(f"已将 {args_values[0]} 加到内存，新的内存值: {memory}")
            result = memory
        elif choice == 'm-':
            memory -= args_values[0]
            print(f"已从内存减去 {args_values[0]}，新的内存值: {memory}")
            result = memory
        else:
            print(f"结果: {result}")
            
        # 添加到历史记录
        if isinstance(result, (int, float, str)):
            history.append(f"{choice}({', '.join(map(str, args_values))}) = {result}")
        
        show_history = input("是否查看历史记录? (yes/no): ").strip().lower()
        if show_history == 'yes':
            print("\n--- 历史记录 ---")
            for item in history:
                print(item)
            print("------------------")

if __name__ == "__main__":
    calculator() 