import os.path
import subprocess
from typing import List
from Config import *

def check_logic(file_path: str) -> str:
    """
         Use the flake8 tool to check logical errors in the specified Python file and return an error message string.

         :param file_path: The path of the Python file to check.
         :return: A string containing error information, or an empty string if there is no error.
    """
    flake8_dir = FLAKE8_DIR
    # Call the flake8 command line tool and pass the file path to be checked
    # result = subprocess.run([flake8_dir, '--ignore=E501', file_path], capture_output=True, text=True)
    result = subprocess.run([flake8_dir, '--ignore=E501', file_path], capture_output=True, text=True,
                            encoding=TEST_FILE_ENCODING)
    return result.stdout

if __name__ == '__main__':
    file_to_check = INSECURE_CHECK_FILE_DIR
    errors = check_logic(file_to_check)
    if errors:
        print("Detected logic errors:")
        print(errors)
    else:
        print("No logic errors detected.")