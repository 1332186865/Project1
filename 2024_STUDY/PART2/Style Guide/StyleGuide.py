#  -*- coding=utf-8 -*-
import re


class StyleGuide:
    def __init__(self, file_dir_1, file_dir_2):
        self.orig_dir = file_dir_1
        self.final_dir = file_dir_2
        self.data = None
        self.load_file()

    def load_file(self):
        """加载文件"""
        with open(self.orig_dir, 'r', encoding="utf-8") as file_1:
            self.data = file_1.read()

    def save_file(self):
        """保存修改后的文件"""
        with open(self.final_dir, 'w', encoding="utf-8") as file_2:
            file_2.write(self.data)

    def correct_space(self):
        """处理中文译文中不规范的空格"""
        pattern = re.compile(r"<target.*?>(.*?)</target>")
        for item in re.finditer(pattern, self.data):
            # 替换中文和英文/数字之间没有空格的情况
            orig = item.group(1)
            text = re.sub(r'([\u4e00-\u9fa5])([A-Za-z0-9])', r'\1 \2', orig)
            text = re.sub(r'([A-Za-z0-9])([\u4e00-\u9fa5])', r'\1 \2', text)
            # 替换中文和英文/数字之间多个空格的情况
            text = re.sub(r'([\u4e00-\u9fa5])\s+([A-Za-z0-9])', r'\1 \2', text)
            text = re.sub(r'([A-Za-z0-9])\s+([\u4e00-\u9fa5])', r'\1 \2', text)
            # 删去中文标点符号两段的空格
            text = re.sub(r'(\s+)([，。！？：；“”（）《》、])', r'\2', text)
            data = re.sub(r'([，。！？：；“”（）《》、])(\s+)', r'\1', text)

            # print(f"原始译文：\t{orig}\n修改后译文：\t{data}\n")
            self.data = self.data.replace(orig, data)

    def correct_brackets(self):
        """处理中文译文中不规范的括号"""
        brackets_pattern = r'(\(.*?\))|（.*?）'
        english_pattern = re.compile(r'^[A-Za-z0-9\s]+$')
        chinese_pattern = re.compile(r'[\u4e00-\u9fa5\s]+')

        matches = re.finditer(brackets_pattern, self.data)
        for match in matches:
            original_content = match.group(0)
            content = original_content.strip("()（）")

            if english_pattern.match(content):
                if original_content.startswith('（'):
                    corrected_content = f' ({content}) '
                    self.data = self.data.replace(original_content, corrected_content)
            elif chinese_pattern.match(content):
                if original_content.startswith('('):
                    corrected_content = f'（{content}）'
                    self.data = self.data.replace(original_content, corrected_content)
            self.data = re.sub(r'(\s+)([，。！？：；“”（）《》、])', r'\2', self.data)
            self.data = re.sub(r'([，。！？：；“”（）《》、])(\s+)', r'\1', self.data)

    def main(self):
        action = input("输入数字选择操作：\n1.空格处理\n2.括号处理\n3.全部处理\n")
        if action == "1":
            self.correct_space()
            self.save_file()
        elif action == "2":
            self.correct_brackets()
            self.save_file()
        elif action == "3":
            self.correct_space()
            self.correct_brackets()
            self.save_file()
        else:
            raise SystemExit


if __name__ == '__main__':
    file = "./test.txlf"
    output = "./test_output.txlf"
    StyleGuide(file, output).main()
