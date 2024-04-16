import ast
import os
import re
from subprocess import run, PIPE
from Config import *

def check_compatibility(file_path, requirements_path=None):
    """  
    检查Python文件的兼容性问题。  
    :param file_path: Python文件的路径。  
    :param requirements_path: requirements.txt文件的路径（可选）。  
    :return: 包含错误信息的字符串。  
    """
    errors = []
    warnings = []

    # 静态代码分析  
    static_analysis_result = run([FLAKE8_DIR, '--ignore=E501,W503', file_path], stdout=PIPE, stderr=PIPE, text=True
                                 , encoding=TEST_FILE_ENCODING)
    if static_analysis_result.stderr:
        errors.append(f"静态代码分析错误：\n{static_analysis_result.stderr}")
    if static_analysis_result.stdout:
        warnings.extend(static_analysis_result.stdout.splitlines())

        # 依赖检查  
    if requirements_path:
        try:
            with open(requirements_path, 'r', encoding=TEST_FILE_ENCODING) as f:
                dependencies = f.read().splitlines()
            for dep in dependencies:
                if '==' in dep:
                    library, version = dep.split('==')
                    warnings.append(f"库 {library} 被固定到了版本 {version}，这可能导致兼容性问题。")
        except Exception as e:
            errors.append(f"无法读取requirements.txt文件：{e}")

            # 特定于平台的代码检查  
    try:
        with open(file_path, 'r', encoding=TEST_FILE_ENCODING) as file:
            content = file.read()

            # 检查Windows特定代码  
            # if re.search(r'\bwin32\b|\bctypes\b|\bpywin32\b', content):
            #     warnings.append("检测到可能特定于Windows的代码。")

            lines = content.split('\n')  # 将内容按行分割

            for line_number, line in enumerate(lines, start=1):
                # 检查Linux特定代码（如使用os.system调用shell命令）
                if re.search(r'\bos\.system\b|\bsubprocess\.call\b', line):
                    warnings.append(f"第{line_number}行: 检测到可能特定于Linux的代码。问题代码: {line.strip()}")

                    # 检查macOS特定代码（如使用AppKit或Objective-C桥接）
                if re.search(r'\bAppKit\b|\bobjc\b', line):
                    warnings.append(f"第{line_number}行: 检测到可能特定于macOS的代码。问题代码: {line.strip()}")

    except Exception as e:
            errors.append(f"无法读取文件 {file_path}：{e}")

    # 返回错误信息字符串
    output = []
    if errors:
        output.append("错误：")
        output.extend(errors)
    if warnings:
        # output.append("\n警告：")
        output.extend(warnings)
    return "\n".join(output) if output else "未检测到潜在的兼容性问题。"

if __name__ == '__main__':
    print(check_compatibility(COMPATALITY_CHECK_FILE_DIR))