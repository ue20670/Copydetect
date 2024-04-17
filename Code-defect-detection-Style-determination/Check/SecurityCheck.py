import os
import re
import subprocess
from typing import List, Tuple

from Config import *

# Define some possible security problem patterns
UNSAFE_CRYPTO_METHODS = ['md5', 'sha1']
UNSAFE_EVAL_METHODS = ['eval', 'exec']
POTENTIAL_INJECTION_PATTERNS = [
    r'(\W+)sql\W+\=',  # Potential SQL injection
    r'(\W+)query\W+\(\W+\+',  # Another potential SQL injection
    r'(\W+)html\W+\+',  # Potential HTML injection/XSS
]


def find_potential_issues(file_content: str) -> List[Tuple[str, List[str]]]:
    issues = []

    # Detect insecure encryption methods
    for method in UNSAFE_CRYPTO_METHODS:
        if re.search(rf'\b{method}\b', file_content):
            issues.append(('Unsafe crypto method', [method]))

            # Detect unsafe eval/exec usage
    for method in UNSAFE_EVAL_METHODS:
        if re.search(rf'\b{method}\(', file_content):
            issues.append(('Unsafe eval/exec usage', [method]))

            # Detect potential injection attacks
    for pattern in POTENTIAL_INJECTION_PATTERNS:
        matches = re.findall(pattern, file_content)
        if matches:
            issues.append(('Potential injection attack', matches))

    return issues


def run_bandit_analysis(file_path: str) -> str:

    # Run Bandit analysis
    completed_process = subprocess.run([BANDIT_DIR, '-r', file_path], capture_output=True, text=True,
                                       encoding= TEST_FILE_ENCODING)
    return completed_process.stdout



def check_security_issues(file_path: str) -> str:
    if not os.path.isfile(file_path):
        return "File not found."

    with open(file_path, 'r', encoding=TEST_FILE_ENCODING) as file:
        content = file.read()

        # Use custom regular expressions to detect potential security issues
        custom_issues = find_potential_issues(content)
        custom_issues_str = "\n".join([f"{issue[0]}: {issue[1]}" for issue in custom_issues])

        # Use Bandit for deeper security analysis
        bandit_output = run_bandit_analysis(file_path)

        # Combine custom and Bandit analysis results
        if custom_issues_str:
            return f"Custom security issues detected:\n{custom_issues_str}\n\nBandit analysis output:\n{bandit_output}"
        else:
            return f"Bandit analysis output:\n{bandit_output}"


if __name__ == '__main__':
    file_to_check = INSECURE_CHECK_FILE_DIR
    security_report = check_security_issues(file_to_check)
    print(security_report)