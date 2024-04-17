import subprocess
import sys
from Config import *

def check_style(file_path):
    """
         Use pylint to check the code style of Python files and return an error message string.

         :param file_path: The path of the Python file to check.
         :return: Error message string, if there is no error, an empty string is returned.
         """
    # try:
    # Use pylint to check code style and get output through stdout
    result = subprocess.run(
        [PYLINT_DIR, '--msg-template="{line}:{column}: {msg} ({symbol})"', file_path],
        capture_output=True, text=True, encoding=TEST_FILE_ENCODING)

    return result.stdout
    # except subprocess.CalledProcessError as e:
    # # If the pylint command fails to execute, return an error message
    # return str(e)
    # except FileNotFoundError:
    # # If pylint is not found, return an error message
    # return "pylint not found. Please make sure pylint is installed and available in your PATH."
    # except Exception as e:
    # # Return other exception information
    # return str(e)

    # Usage example: Check the code style of the test.py file

if __name__ == '__main__':
    file_path = STYLE_CHECK_FILE_DIR
    error_messages = check_style(file_path)
    if error_messages:
        print("Code style errors found:")
        print(error_messages)
    else:
        print("No code style errors found.")