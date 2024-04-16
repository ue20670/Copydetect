import subprocess
import sys
from Config import *

def check_style(file_path):
    """
    使用pylint检查Python文件的代码风格，并返回错误信息字符串。

    :param file_path: 要检查的Python文件的路径。
    :return: 错误信息字符串，如果没有错误则返回空字符串。
    """
    # try:
    # 使用pylint检查代码风格，并通过stdout获取输出
    result = subprocess.run(
        [PYLINT_DIR, '--msg-template="{line}:{column}: {msg} ({symbol})"', file_path],
        capture_output=True, text=True, encoding=TEST_FILE_ENCODING)

    return result.stdout
    # except subprocess.CalledProcessError as e:
    #     # 如果pylint命令执行失败，返回错误信息
    #     return str(e)
    # except FileNotFoundError:
    #     # 如果找不到pylint，返回错误信息
    #     return "pylint not found. Please make sure pylint is installed and available in your PATH."
    # except Exception as e:
    #     # 返回其他异常信息
    #     return str(e)

    # 使用示例：检查test.py文件的代码风格

if __name__ == '__main__':
    file_path = STYLE_CHECK_FILE_DIR
    error_messages = check_style(file_path)
    if error_messages:
        print("Code style errors found:")
        print(error_messages)
    else:
        print("No code style errors found.")