# example_with_more_issues.py
import math

# Bad module-level variable name
BadGlobalVar = "This is a global variable"  # 不符合命名规范的全局变量


class BadClassName(object):  # 类名应该使用CamelCase风格
    """A class with bad style."""

    # Bad constant name
    bad_constant = 10  # 常量应该全大写，用下划线分隔

    def __init__(self, first_name, LAST_name):  # 参数命名风格不一致
        self.first_name = first_name
        self.LAST_NAME = LAST_name  # 属性命名风格不一致
        self.some_list = []  # 变量名缺乏描述性

    def Bad_Method_Name(self, x, Y):  # 方法名不符合snake_case风格，参数命名风格不一致
        """A method with inconsistent naming."""
        temp = x + Y  # 局部变量命名不规范，且未使用下划线分隔
        self.some_list.append(temp)

        if temp > 100:  # 判断语句后应有空格
            print("Temp is greater than 100")  # 使用了括号，但内部缺少空格，且最好使用双引号

        # Redundant parenthesis
        z = (1 + 2) * (temp - 5)  # 冗余的括号，虽然不影响功能，但不符合简洁风格

        return z  # 返回变量名最好具有描述性


def function_with_long_name_and_redundant_comments(arg1, arg2):  # 函数名过长，应简洁明了
    # This is a redundant comment that doesn't add any value to the code
    result = arg1 * arg2  # 变量命名虽无错，但'result'过于通用，最好更具体
    return result


# Unused variable
unused_var = "This variable is not used anywhere in the code"  # 未使用的变量


# Inconsistent indentation
def inconsistently_indented_function():
    var1 = 10
    var2 = 20  # 缩进不一致，导致代码风格问题


var3 = 30

# Line too long
long_line = "This is a very long line that exceeds the recommended maximum line length for readability and maintainability of the code. It should be split into multiple lines for better readability."  # 行过长，应分行以提高可读性

# Multiple statements on one line
x = 1;
y = 2;
z = x + y  # 一行中有多个语句，应分开以提高可读性

# Unnecessary semicolon
print("Hello, world!");  # 不必要的分号，Python使用换行作为语句分隔