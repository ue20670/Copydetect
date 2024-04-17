import cProfile
import pstats
import io

import Config
from Config import *


def check_performance_issues(file_path: str) -> str:
    """
         Use the cProfile module to check performance issues of the specified Python file and return an error message string.

         :param file_path: The path of the Python file to check.
         :return: A string containing performance problem information, or an empty string if no problem is detected.
    """
    # Import and run the target Python file
    module_name = 'test'
    import_statement = f'import {module_name}'
    with open(file_path, 'r', encoding=TEST_FILE_ENCODING) as file:
        script = file.read()

        # Execute the code in a temporary namespace so we can import and execute it
    globals_dict = {}
    exec(f'{import_statement}\n{script}', globals_dict)

    # Use cProfile to run and analyze code performance
    profiler = cProfile.Profile()
    # What is detected is the main method in the target file
    profiler.runctx(f'{module_name}.main(45)', globals_dict, locals())

    # Collect and format analysis results
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats('cumulative') # Sort by cumulative time
    # stats.print_linear_hist('time')  # print histogram
    performance_issues = stream.getvalue()

    # Return performance problem report
    return performance_issues if performance_issues else ""


if __name__ == '__main__':
    file_to_check = Config.test_file
    issues = check_performance_issues(file_to_check)
    if issues:
        print("Detected performance issues:")
        print(issues)
    else:
        print("No significant performance issues detected.")