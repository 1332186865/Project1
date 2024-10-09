#  将./MT/LP的结构更改为./LP/MT的结构
#  -*- coding=utf-8 -*-
import os
import shutil


def reorganize_files(root_directory):
    language_mapping = {}

    # 遍历根目录下的翻译引擎文件夹
    for translator in os.listdir(root_directory):
        translator_path = os.path.join(root_directory, translator)
        if os.path.isdir(translator_path):
            # 遍历每个翻译引擎下的语言文件夹
            for language in os.listdir(translator_path):
                language_path = os.path.join(translator_path, language)
                if os.path.isdir(language_path):
                    if language not in language_mapping:
                        language_mapping[language] = {}
                    language_mapping[language][translator] = language_path

    # 为每个语言对创建新的文件夹结构，并移动文件
    for language, translators in language_mapping.items():
        for translator, path in translators.items():
            target_directory = os.path.join(root_directory, language, translator)
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)
            for file in os.listdir(path):
                src_file = os.path.join(path, file)
                dest_file = os.path.join(target_directory, file)
                shutil.move(src_file, dest_file)
                print(f"Moved {file} from {src_file} to {dest_file}")

    # 可选：删除原来的文件夹结构
    for translator in os.listdir(root_directory):
        translator_path = os.path.join(root_directory, translator)
        if os.path.isdir(translator_path):
            try:
                os.rmdir(translator_path)
            except OSError:
                print(f"Directory {translator_path} is not empty and was not removed.")


if __name__ == '__main__':
    root = './data'
    reorganize_files(root)
