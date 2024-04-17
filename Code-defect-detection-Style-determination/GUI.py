import sys
from os.path import dirname, abspath
from Config import *

# Add the parent directory of the Check directory (i.e. the main project directory) to sys.path
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
    # Get the current timestamp and format it as a string for file name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"code_check_{timestamp}.txt"

    # List used to store all inspection information
    all_check_info = []

    # Iterate through all files in the folder
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):  # Only process .py files
                file_path = os.path.join(root, file)
                # Perform all checks on each file and collect check information
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
                        result = check(file_path)  #Execute the check method and get the results
                        check_info.append(f"{check.__name__}:\n{result}\n=====\n")  # Add separators and check results to the list
                    except Exception as e:
                        pass
                all_check_info.append("\n".join(check_info))  # Combine the check information of the current file into a string and add it to the total list
                all_check_info.append("------------------------\n")  # Add separators between files

    #Write all inspection information to txt file
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.writelines(all_check_info)

    print(f"Check information has been saved to {output_filename}")



check_all_files_in_directory(test_file_dir)  # Replace with your folder path


