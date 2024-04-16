import os.path
import subprocess
from typing import List
from Config import *

def check_types(file_path: str) -> str:
    """
    使用mypy工具检查指定Python文件的类型错误，并返回错误信息字符串。

    :param file_path: 要检查的Python文件的路径。
    :return: 包含错误信息的字符串，如果没有错误则返回空字符串。
    """

    mypy_dir = MYPY_DIR
    # 调用mypy命令行工具并传递要检查的文件路径
    result = subprocess.run([mypy_dir, file_path], capture_output=True, text=True,
                            encoding=TEST_FILE_ENCODING)
    return result.stdout

if __name__ == '__main__':
    file_to_check = TYPE_CHECK_FILE_DIR
    errors = check_types(file_to_check)
    print(errors)
