import cProfile
import pstats
import io

from Config import *


def check_performance_issues(file_path: str) -> str:
    """
    使用cProfile模块检查指定Python文件的性能问题，并返回错误信息字符串。

    :param file_path: 要检查的Python文件的路径。
    :return: 包含性能问题信息的字符串，如果没有检测到问题则返回空字符串。
    """
    # 导入并运行目标Python文件
    module_name = 'test'
    import_statement = f'import {module_name}'
    with open(file_path, 'r', encoding=TEST_FILE_ENCODING) as file:
        script = file.read()

        # 在一个临时的命名空间中执行代码，以便我们可以导入并执行它
    globals_dict = {}
    exec(f'{import_statement}\n{script}', globals_dict)

    # 使用cProfile来运行并分析代码性能
    profiler = cProfile.Profile()
    # 检测的是目标文件中的main方法
    profiler.runctx(f'{module_name}.main(45)', globals_dict, locals())

    # 收集并格式化分析结果
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.sort_stats('cumulative')  # 按累计时间排序
    # stats.print_linear_hist('time')  # 打印直方图
    performance_issues = stream.getvalue()

    # 返回性能问题报告
    return performance_issues if performance_issues else ""


if __name__ == '__main__':
    file_to_check = Config.test_file
    issues = check_performance_issues(file_to_check)
    if issues:
        print("Detected performance issues:")
        print(issues)
    else:
        print("No significant performance issues detected.")