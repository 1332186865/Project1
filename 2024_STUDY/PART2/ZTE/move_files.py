#  根据文件中的LP移动文件
#  -*- coding=utf-8 -*-
import os
import re
import shutil


def move_files_by_language_pair(source_directory):
    # 确保源目录存在
    if not os.path.exists(source_directory):
        print(f"源目录 {source_directory} 不存在。")
        return

    # 遍历源目录中的所有文件
    for filename in os.listdir(source_directory):
        match = re.search(r'_([a-zA-Z]{2,3}(?:-[a-zA-Z]{2,3})?)\.txt\.txlf$', filename)
        if match:
            language_pair = match.group(1)
            target_directory = os.path.join(source_directory, language_pair)
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            source_file = os.path.join(source_directory, filename)
            target_file = os.path.join(target_directory, filename)

            shutil.move(source_file, target_file)
            print(f"文件 {filename} 已移动到 {target_directory}")
        else:
            print(f"文件 {filename} 不包含有效的语言对标识。")


if __name__ == '__main__':
    source = r'./data/DeepL'
    move_files_by_language_pair(source)
