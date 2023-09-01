#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
"""
    学生管理器系统
"""


class Student:
    """学生数据模型类: 此模块用来描述学生对象"""

    def __init__(self, name: str, age: int, score: float, num: int = 0):
        """
        学生对象
        :param name: 名字
        :param age: 年龄
        :param score: 成绩
        :param num: 序号
        """
        self.num = num
        self.name = name
        self.age = age
        self.score = score

    def get_infos(self):
        return self.__num, self.__name, self.__age, self.__score

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    def get_num(self):
        return self.__num

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_score(self):
        return self.__score

    def write_to_file(self, f):
        f.write('%s' % self.__num)
        f.write(',')
        f.write('%s' % self.__name)
        f.write(',')
        f.write('%s' % self.__age)
        f.write(',')
        f.write('%s' % self.__score)
        # f.write('\n')


class Student2(Student):
    """逻辑控制类: 负责存储学生信息"""

    def __init__(self, name: str, age: int, score: float, address: str, num: int):
        super().__init__(name, age, score, num)
        self.__address = address

    def get_infos(self):
        return self.get_num(), self.get_name(), self.get_age(), self.get_score(), self.__address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def write_to_file(self, f):
        """
        写入文档
        :param f: 数据
        :return: None
        """
        f.write('%s' % self.get_num())
        f.write(',')
        f.write('%s' % self.get_name())
        f.write(',')
        f.write('%s' % self.get_age())
        f.write(',')
        f.write('%s' % self.get_score())
        f.write(',')
        f.write('%s' % self.__address)
        f.write('\n')

    def __str__(self):
        return "我的编号是%-s号, 名字是%-s, 年龄是%-s岁, 成绩是%-s分, 地址是%-s。" % self.get_infos()

    def __repr__(self):
        return "Student2(num=%d, name='%s', age=%d, score=%d, address='%s')" % self.get_infos()


if __name__ == '__main__':
    stu1 = Student2('小明', 12, 89, '北京', 1)
    print(stu1)
    stu2 = eval(stu1.__repr__())
    stu1.age = 120
    print()
    print(stu1)
    print(stu2)
