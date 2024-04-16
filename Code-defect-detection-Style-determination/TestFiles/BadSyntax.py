import subprocess
import os


def check_python_syntax(file_path, output_dir):
    # 提取文件名和基本名（不带扩展名）
    file_name = os.path.basename(file_path)
    base_name = os.path.splitext(file_name)[0]

    # 构建输出文件的路径
    output_file_path = os.path.join(output_dir, f"{base_name}_grammar_defect.txt")

    # 运行pylint并捕获输出
    try:
        result = subprocess.run(
            ["pylint", "--output-format=text", "--reports=no", "--score=no", file_path],
            capture_output=True,
            text=True,
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running pylint: {e}")
        return

        # 将pylint的输出写入到指定的文件中
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(result.stdout)

    print(f"Syntax check completed. Defects saved to {output_file_path}")
    print('abc'*1.62)







    # 使用示例
    input_file_path = r"D:\bishe\其他-代码-代码缺陷检测+风格判断+GUI\Code-defect-detection-Style-determination\main.py"  # 替换为你的Python文件路径
    output_directory = "./"  # 替换为你想要保存输出文件的目录路径
    check_python_syntax(input_file_path, output_directory)



# =======================================================================

