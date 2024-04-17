import os.path
import subprocess
from typing import List
from Config import *

def check_types(file_path: str) -> str:
    """
         Use the mypy tool to check for type errors in the specified Python file and return an error message string.

         :param file_path: The path of the Python file to check.
         :return: A string containing error information, or an empty string if there is no error.
    """

    mypy_dir = MYPY_DIR
    # Call the mypy command line tool and pass the file path to be checked
    result = subprocess.run([mypy_dir, file_path], capture_output=True, text=True,
                            encoding=TEST_FILE_ENCODING)
    return result.stdout

if __name__ == '__main__':
    file_to_check = TYPE_CHECK_FILE_DIR
    errors = check_types(file_to_check)
    print(errors)
