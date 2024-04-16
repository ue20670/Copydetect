import subprocess
import os
from Config import *

# 检测语法错误
def check_python_syntax(file_path):
    # 提取文件名和基本名（不带扩展名）
    file_name = os.path.basename(file_path)
    base_name = os.path.splitext(file_name)[0]

    # 运行pylint并捕获输出
    try:
        pylint_path = PYLINT_DIR
        result = subprocess.run(
            [pylint_path, " --output-format=text", " --reports=no", " --score=no ", file_path],
            capture_output=True,
            text=True,
            encoding=TEST_FILE_ENCODING
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running pylint: {e}")
        return

    print(result.stdout)
    return result.stdout

if __name__ == '__main__':
    # 使用示例
    input_file_path = SYNTAX_CHECK_FILE_DIR
    check_python_syntax(input_file_path)