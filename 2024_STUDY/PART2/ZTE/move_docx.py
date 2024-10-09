#  移动生成的bilingual docx文件
#  -*- coding=utf-8 -*-
import os
import shutil


def copy_docx_files(src_directory, dest_directory):
    for root, dirs, files in os.walk(src_directory):
        for file in files:
            if file.endswith('.docx'):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, src_directory)
                dest_path = os.path.join(dest_directory, rel_path)
                if not os.path.exists(dest_path):
                    os.makedirs(dest_path)

                shutil.copy2(src_path, os.path.join(dest_path, file))
                os.remove(src_path)
                print(f"Copied {src_path} to {os.path.join(dest_path, file)}")


if __name__ == '__main__':
    source = './output'
    target = './bilingual_tables'
    copy_docx_files(source, target)
