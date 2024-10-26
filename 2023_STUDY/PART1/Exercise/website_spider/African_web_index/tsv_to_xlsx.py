#  Copyright (c) 2023. Generated by Gu.
#  -*- coding=utf-8 -*-
import os
import time

import pandas as pd
import xlwings as xw


class TsvToXlsx:
    def __init__(self, tsv_folder='./tsv', xlsx_folder='./xlsx'):
        # 定义输入文件夹和输出文件夹的路径
        self.tsv_folder = tsv_folder
        self.xlsx_folder = xlsx_folder

    def tsv_to_xlsx(self):
        # 确保输出文件夹存在，如果不存在则创建它
        os.makedirs(self.xlsx_folder, exist_ok=True)
        # 获取输入文件夹中的所有.tsv文件
        tsv_files = [f for f in os.listdir(self.tsv_folder) if f.endswith('.tsv')]

        # 循环处理每个.tsv文件
        for tsv_file in tsv_files:
            print("正在进行:", tsv_file)
            # 构建完整的输入文件路径和输出文件路径
            tsv_file_path = os.path.join(self.tsv_folder, tsv_file)
            xlsx_file_path = os.path.join(self.xlsx_folder, os.path.splitext(tsv_file)[0] + '.xlsx')
            # 读取.tsv文件到pandas DataFrame
            df = pd.read_csv(tsv_file_path, sep='\t')
            wb = xw.Book()  # 创建一个新的Excel工作簿
            sheet = wb.sheets['Sheet1']  # 选择默认的Sheet
            sheet.range('A1').value = df.values  # 将DataFrame写入Excel工作簿
            wb.save(xlsx_file_path)  # 保存Excel文件为.xlsx格式
            wb.close()  # 关闭工作簿
            time.sleep(0.3)
        print("转换完成！")

    def main(self):
        self.tsv_to_xlsx()


if __name__ == '__main__':
    TsvToXlsx('African_website/tsv', 'African_website/xlsx').main()
