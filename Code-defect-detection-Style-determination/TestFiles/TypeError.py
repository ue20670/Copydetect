# ========================类型错误检测代码==================================
def greet(name: str) -> int:  # 错误的返回类型注解，应该是str而不是int
    return f"Hello, {name}!"


def add_numbers(a: int, b: int) -> int:
    return a + b


result = add_numbers(10, '20')  # 错误的参数类型，'20'是字符串而不是整数

x: int = 'this is not an integer'  # 错误的变量类型注解，字符串赋值给了整型变量
print(greet('World'))
print(result)
print(x)
# =======================================================================