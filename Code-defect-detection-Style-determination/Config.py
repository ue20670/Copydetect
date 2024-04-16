def get_dir(dir1, dir2):
    import os
    return os.path.join(dir1, dir2)
# 测试文件编码
TEST_FILE_ENCODING = 'utf-8'

# Python脚本地址
script_dir = r'D:\Python\Python39\Scripts'

# 测试文件地址
test_file_dir = r'D:\Daily use software\快捷栏位置\桌面\Code-defect-detection-Style-determination\TestFiles'
# test_file = r'D:\bishe\其他-代码-代码缺陷检测+风格判断+GUI\Code-defect-detection-Style-determination\test.py'

# 脚本地址
BANDIT_DIR = get_dir(script_dir, "bandit.exe")
MYPY_DIR = get_dir(script_dir, "mypy.exe")
PYLINT_DIR = get_dir(script_dir, "pylint.exe")
FLAKE8_DIR = get_dir(script_dir, 'flake8.exe')

# 测试文件地址
TYPE_CHECK_FILE_DIR = get_dir(test_file_dir, 'TypeError.py')
SYNTAX_CHECK_FILE_DIR = get_dir(test_file_dir, 'BadSyntax.py')
INSECURE_CHECK_FILE_DIR = get_dir(test_file_dir, 'InsecureCode.py')
LOGIC_CHECK_FILE_DIR = get_dir(test_file_dir, 'BadSyntax.py')
COMPATALITY_CHECK_FILE_DIR = get_dir(test_file_dir, 'BadCompatality.py')
STYLE_CHECK_FILE_DIR = get_dir(test_file_dir, 'BadStyle.py')
