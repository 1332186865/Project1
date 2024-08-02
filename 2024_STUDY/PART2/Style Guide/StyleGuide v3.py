#  -*- coding=utf-8 -*-
import re


class StyleGuide:
    def __init__(self, file_dir_1, file_dir_2):
        self.original_dir = file_dir_1
        self.final_dir = file_dir_2
        self.data = None
        self.load_file()

    def load_file(self):
        """加载文件"""
        with open(self.original_dir, 'r', encoding="utf-8") as file_1:
            self.data = file_1.read()

    def save_file(self):
        """保存修改后的文件"""
        with open(self.final_dir, 'w', encoding="utf-8") as file_2:
            file_2.write(self.data)

    def correct_spaces(self):
        target_pattern = re.compile(r"<target([^>]*)>(.*?)</target>", re.M | re.S)

        matches = re.finditer(target_pattern, self.data)
        modified_data = self.data

        for match in matches:
            target_tag = match.group(1)
            target_content = match.group(2)
            original_content = target_content

            parts = re.split(r"(<[^>]+>)", target_content, re.S + re.M)
            processed_parts = []
            for part in parts:  # 通过<tag>分割<target>的内容
                part = part.strip(r" ")
                if not re.match(r"<[^>]+>", part):  # 删去<tag>之间的空格
                    if part.strip(r" ") == "":
                        continue

                    part = re.sub(r"([\u4E00-\u9FA5])([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])", r"\1 \2", part)
                    part = re.sub(r"([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])([\u4E00-\u9FA5])", r"\1 \2", part)
                processed_parts.append(part)

            text = ''.join(processed_parts)
            # 将空格统一加在字母/数字前
            text = re.sub(r"([\u4E00-\u9FA5])(<.*?>)([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])", r"\1\2 \3", text, re.S + re.M)
            text = re.sub(r"([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])(<.*?>)([\u4E00-\u9FA5])", r"\1 \2\3", text, re.S + re.M)
            # 处理<tag>前后都是字母/数字的情况
            new_target_content = re.sub(r"([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])(<.*?>)([A-Za-z0-9\u00C0-\u00FF\u0100-\u02AF®-])",
                                        r"\1\2 \3", text, re.S + re.M)
            modified_data = modified_data.replace(match.group(0), f"<target{target_tag}>{new_target_content}</target>")

        self.data = modified_data

    def correct_brackets(self):
        """处理中文译文中不规范的括号，只针对<target>标签内的内容，同时保留任何属性"""
        target_pattern = re.compile(r'(<target[^>]*>)(.*?)(</target>)', re.M | re.S)
        brackets_pattern = re.compile(r"""(\([^（）]*?\))    #()
                                          |(（[^()]*?）)      #（）
                                          |(\([^（）]*?）)    #(）
                                          |(（[^()]*?\))      #（)
                                          """, re.S | re.M | re.X)
        english_pattern = re.compile(r"^[A-Za-z0-9®\u00C0-\u00FF\u0100-\u02AF\-\s]+$", re.S | re.M)
        chinese_pattern = re.compile(r"[\u4E00-\u9FA5\s]+", re.S | re.M)

        matches = re.finditer(target_pattern, self.data)
        modified_data = self.data

        for match in matches:
            start_tag = match.group(1)
            target_text = match.group(2)
            end_tag = match.group(3)
            original_text = target_text  # 保存原始内容，用于最后的替换

            for item in re.finditer(brackets_pattern, target_text):
                original_content = item.group(0)
                content = original_content.strip("()（）")

                if chinese_pattern.search(content):
                    corrected_content = f'（{content}）'
                    target_text = target_text.replace(original_content, corrected_content)
                elif english_pattern.search(content):
                    corrected_content = f' ({content}) '
                    target_text = target_text.replace(original_content, corrected_content)

            # 删除英文括号两边多余的空格
            target_text = re.sub(r"(\s+)(\s[()])", r"\2", target_text, re.S | re.M)
            target_text = re.sub(r"([()]\s)(\s+)", r"\1", target_text, re.S | re.M)
            # 删除中文标点符号两段的空格
            target_text = re.sub(r"([ \r\f\v]+)([，。！？：；“”（）《》、])", r"\2", target_text, re.M)
            target_text = re.sub(r"([，。！？：；“”（）《》、])([ \r\f\v]+)", r"\1", target_text, re.M)

            # 替换完所有括号后，替换原始数据中的这部分
            modified_data = modified_data.replace(f"{start_tag}{original_text}{end_tag}", f"{start_tag}{target_text}{end_tag}")

        self.data = modified_data
        # self.correct_spaces()  # 删除以上步骤产生的多余空格

    def action(self, action):
        if action == "1":
            self.correct_spaces()
        elif action == "2":
            self.correct_brackets()
        elif action == "3":
            self.correct_spaces()
            self.correct_brackets()
        else:
            raise SystemExit

    def main(self):
        """主函数"""
        action = input("输入数字选择操作：\n1.空格处理\n2.括号处理\n3.全部处理\n")
        self.action(action)
        self.save_file()
        print("Done!")


if __name__ == '__main__':
    file = "./test.txlf"
    output = "./test_output.txlf"
    StyleGuide(file, output).main()
