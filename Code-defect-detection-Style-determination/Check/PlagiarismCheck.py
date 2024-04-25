import difflib

import Config
from Config import *

def calculate_similarity(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        code1 = f1.read()
        code2 = f2.read()

    similarity = difflib.SequenceMatcher(None, code1, code2).ratio()
    return similarity


def check_plagiarism(file1_path, file2_path, similarity_threshold=0.7):
    similarity = calculate_similarity(file1_path, file2_path)
    if similarity >= similarity_threshold:
        print(f"警告：两份代码之间的相似度为 {similarity:.2f}，可能存在抄袭。")
        return True
    else:
        print(f"两份代码之间的相似度为 {similarity:.2f}，抄袭的可能性较低。")
        return False

    # 使用示例


file1 = Config.PLAGIARISM_CHECK_FILE1_DIR
file2 = Config.PLAGIARISM_CHECK_FILE2_DIR
file3 = Config.PLAGIARISM_CHECK_FILE3_DIR
check_plagiarism(file1, file2)

check_plagiarism(file1, file3)
