import os
import re
import subprocess
from typing import List, Tuple

from Config import *

# 定义一些可能的安全问题模式
UNSAFE_CRYPTO_METHODS = ['md5', 'sha1']
UNSAFE_EVAL_METHODS = ['eval', 'exec']
POTENTIAL_INJECTION_PATTERNS = [
    r'(\W+)sql\W+\=',  # 潜在的SQL注入
    r'(\W+)query\W+\(\W+\+',  # 另一个潜在的SQL注入
    r'(\W+)html\W+\+',  # 潜在的HTML注入/XSS
]


def find_potential_issues(file_content: str) -> List[Tuple[str, List[str]]]:
    issues = []

    # 检测不安全的加密方法
    for method in UNSAFE_CRYPTO_METHODS:
        if re.search(rf'\b{method}\b', file_content):
            issues.append(('Unsafe crypto method', [method]))

            # 检测不安全的eval/exec使用
    for method in UNSAFE_EVAL_METHODS:
        if re.search(rf'\b{method}\(', file_content):
            issues.append(('Unsafe eval/exec usage', [method]))

            # 检测潜在的注入攻击
    for pattern in POTENTIAL_INJECTION_PATTERNS:
        matches = re.findall(pattern, file_content)
        if matches:
            issues.append(('Potential injection attack', matches))

    return issues


def run_bandit_analysis(file_path: str) -> str:

    # 运行Bandit分析
    completed_process = subprocess.run([BANDIT_DIR, '-r', file_path], capture_output=True, text=True,
                                       encoding= TEST_FILE_ENCODING)
    return completed_process.stdout



def check_security_issues(file_path: str) -> str:
    if not os.path.isfile(file_path):
        return "File not found."

    with open(file_path, 'r', encoding=TEST_FILE_ENCODING) as file:
        content = file.read()

        # 使用自定义的正则表达式来检测潜在的安全问题
        custom_issues = find_potential_issues(content)
        custom_issues_str = "\n".join([f"{issue[0]}: {issue[1]}" for issue in custom_issues])

        # 使用Bandit进行更深入的安全分析
        bandit_output = run_bandit_analysis(file_path)

        # 组合自定义和Bandit的分析结果
        if custom_issues_str:
            return f"Custom security issues detected:\n{custom_issues_str}\n\nBandit analysis output:\n{bandit_output}"
        else:
            return f"Bandit analysis output:\n{bandit_output}"


if __name__ == '__main__':
    file_to_check = INSECURE_CHECK_FILE_DIR
    security_report = check_security_issues(file_to_check)
    print(security_report)