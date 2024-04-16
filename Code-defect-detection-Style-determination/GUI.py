import sys
from os.path import dirname, abspath
from Config import *

# 添加Check目录的父目录（即主工程目录）到sys.path  
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from Check.CompatibilityCheck import check_compatibility
from Check.LogicCheck import check_logic
from Check.PerformanceAnalysis import check_performance_issues
from Check.SecurityCheck import check_security_issues
from Check.SyntaxCheck import check_python_syntax
from Check.StyleCheck import check_style
from Check.TypeCheck import check_types
import os
import time
from datetime import datetime


def check_all_files_in_directory(directory_path: str):
    # 获取当前时间戳并格式化为字符串，用于文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"code_check_{timestamp}.txt"

    # 用于存储所有检查信息的列表
    all_check_info = []

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):  # 只处理.py文件
                file_path = os.path.join(root, file)
                # 对每个文件执行所有检查，并收集检查信息
                check_info = [f"File: {file_path}\n"]
                checks = [
                    check_compatibility,
                    check_logic,
                    check_performance_issues,
                    check_security_issues,
                    check_python_syntax,
                    check_style,
                    check_types
                ]
                for check in checks:
                    try:
                        result = check(file_path)  # 执行检查方法并获取结果
                        check_info.append(f"{check.__name__}:\n{result}\n=====\n")  # 添加分隔符和检查结果到列表中
                    except Exception as e:
                        pass
                all_check_info.append("\n".join(check_info))  # 将当前文件的检查信息合并为一个字符串，并添加到总列表中
                all_check_info.append("------------------------\n")  # 在文件之间添加分隔符

    # 将所有检查信息写入txt文件
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.writelines(all_check_info)

    print(f"Check information has been saved to {output_filename}")



check_all_files_in_directory(test_file_dir)  # 替换为你的文件夹路径


