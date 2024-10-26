#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import time

from student import Student2


class StudentManagerController:
    """学生逻辑控制器(数据模型类): 定义要处理的数据类型"""

    def __init__(self):
        self.__docs = []  # 此列表用于存储所有学生的信息

    @property
    def docs(self):
        return self.__docs[:]

    @docs.setter
    def docs(self, values):
        self.__docs.append(values)

    @staticmethod
    def __input_check(msg, method):
        while True:
            try:
                return method(input(msg))
            except ValueError:
                print('请重新输入！')

    def add_student(self, name, age, score, address):
        """
        添加学生
        :param name:姓名
        :param age: 年龄
        :param score: 成绩
        :param address: 地址
        :return: None
        """
        num = self.__generate_num()
        stu = Student2(name, age, score, address, num)
        self.__docs.append(stu)
        # return self.__docs

    def __generate_num(self):
        """
        输出序号:新编号，自动编号
        :return: 序号
        """
        return self.__docs[-1].num + 1 if len(self.__docs) > 0 else 1

    @staticmethod
    def __output_students(lst: list):
        """
        输出学生信息
        :param lst: 学生信息表
        :return: None
        """
        print("+-------+-----------+--------+---------+---------------+")
        print("|  num  |   name    +  age   +  score  +    address    +")
        print("+-------+-----------+--------+---------+---------------+")
        for stu in lst:
            info = "| %-5s | %-9s | %-6s | %-7s | %-12s |" % stu.get_infos()
            print(info)
        print("+-------+-----------+--------+---------+---------------+")
        time.sleep(2)

    def list_all_students(self):
        """列表所有学生信息的方法供其它模块调用"""
        self.__output_students(self.__docs)

    def del_student(self):
        """
        删除学生
        :return: 显示学生信息
        """
        student = input("请输入学生姓名：")
        index = 0
        for stu in self.__docs:
            if stu.name == student:
                self.__docs.pop(index)
            index += 1
        self.list_all_students()

    def modify_student(self, num, name, age, score, address):
        """
        学生信息更新
        :param num:序号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        :param address: 地址
        :return: True/False
        """
        for stu in self.__docs:
            if stu.num == num:
                stu.name = name
                stu.sex = age
                stu.score = score
                stu.address = address
                return True
        return False

    def change_score(self):
        """学生成绩更改"""
        name = input("请输入学生姓名：").strip()
        score = self.__input_check("请输入学生新成绩：", float)
        for stu in self.__docs:
            if name == stu.get_name():
                stu.score = score
        self.list_all_students()

    def change_address(self):
        """学生地址更改"""
        name = input("请输入学生姓名：")
        address = input("请输入学生新地址：")
        for stu in self.__docs:
            if name == stu.get_name():
                stu.address = address
        self.list_all_students()

    def list_order_by_score_desc(self):
        """成绩降序"""
        ls = sorted(self.__docs,
                    key=lambda stu: stu.get_score(),
                    reverse=True)
        self.__output_students(ls)

    def list_order_by_score_asc(self):
        """成绩升序"""
        ls = sorted(self.__docs, key=lambda stu: stu.get_score())
        self.__output_students(ls)

    def list_order_by_age_desc(self):
        """年龄降序"""
        ls = sorted(self.__docs,
                    key=lambda stu: stu.get_age(),
                    reverse=True)
        self.__output_students(ls)

    def list_order_by_age_asc(self):
        """年龄升序"""
        ls = sorted(self.__docs, key=lambda stu: stu.get_age())
        self.__output_students(ls)

    def save_to_file(self):
        """将学生信息保存至文件"""
        try:
            with open('stu.txt', 'wt', encoding='utf8') as f:
                for stu in self.__docs:
                    stu.write_to_file(f)
            print('保存成功!')
            time.sleep(1)
        except IOError:
            print('保存失败!')
            time.sleep(1)

    def read_from_file(self):
        """从文件载入学生信息"""
        try:
            with open('stu.txt', 'rt', encoding='utf8') as f:
                while True:
                    con = f.readline().strip().split(',')
                    if [''] == con:
                        break
                    self.add_student(con[1], con[2], con[3], con[4])
            self.list_all_students()
        except IOError:
            print('打开失败')
            time.sleep(2)


if __name__ == '__main__':
    s1 = StudentManagerController()
    s1.read_from_file()
    s1.list_all_students()
