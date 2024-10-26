#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
import time

from student_info import StudentManagerController as Smc


class StudentManagerView:
    """
        界面视图类: 负责处理界面逻辑
    """

    def __init__(self):
        self.__controller = Smc()  # 创建逻辑控制器对象

    @staticmethod
    def __show_menu():
        """
            菜单界面
        """
        print("+-----------------------------+")
        print("| 1)添加学生信息                |")
        print("| 2)显示所有学生的信息           |")
        print("| 3)删除学生信息                |")
        print("| 4)修改学生信息                |")
        print("| 5)更新学生成绩                |")
        print("| 6)更新家庭住址                |")
        print("| 7)按学生成绩降序显示学生信息     |")
        print("| 8)按学生成绩升序显示学生信息     |")
        print("| 9)按学生年龄降序显示学生信息     |")
        print("|10)按学生年龄升序显示学生信息     |")
        print("|11)保存学生信息到文件(stu.txt)  |")
        print("|12)从文件中载入数据(stu.txt)    |")
        print("| q)退出                       |")
        print("+-----------------------------+")

    def __display(self):
        """
            菜单操作
        """
        self.__show_menu()
        s = input("请选择: ")
        if s == 'q':
            print('诶嘿!')
            raise SystemExit
        if s == '1':
            self.__input_student()
        elif s == '2':
            self.__controller.list_all_students()
        elif s == '3':
            self.__controller.del_student()
        elif s == '4':
            self.__modify_student()
        elif s == '5':
            self.__controller.change_score()
        elif s == '6':
            self.__controller.change_address()
        elif s == '7':
            self.__controller.list_order_by_score_desc()  # 降序
        elif s == '8':
            self.__controller.list_order_by_score_asc()  # 升序
        elif s == '9':
            self.__controller.list_order_by_age_desc()  # 降序
        elif s == '10':
            self.__controller.list_order_by_age_asc()  # 升序
        elif s == '11':
            self.__controller.save_to_file()
        elif s == '12':
            self.__controller.read_from_file()
        else:
            print('请检查输入!')
            time.sleep(2)

    @staticmethod
    def __input_check(msg, method):
        while True:
            try:
                return method(input(msg))
            except ValueError:
                print('请重新输入！')

    def __input_student(self):
        """
        学生导入
        """
        while True:
            n = input("请输入姓名：")
            if not n:
                break
            a = self.__input_check("请输入年龄：", int)
            s = self.__input_check("请输入成绩：", float)
            ad = input("请输入地址：")
            self.__controller.add_student(n, a, s, ad)

    def __modify_student(self):
        """
            修改学生信息
        :return: None
        """
        try:
            num = int(input("请输入学生ID："))
            n = input("请输入姓名：")
            a = self.__input_check("请输入年龄：", int)
            s = self.__input_check("请输入成绩：", float)
            ad = input("请输入地址：")
            if self.__controller.modify_student(num, n, a, s, ad):
                print('修改成功！')
                time.sleep(2)
            else:
                print('更新失败，请检查输入!')
                time.sleep(2)
        except ValueError:
            print('请检查输入！')

    def main(self):
        """
            界面入口方法
        """
        while True:
            self.__display()
