class Person:
    """描述人类"""
    counter = 0

    def __init__(self, pname, pgender):
        """
        构造函数；
        对类进行实例化时调用；
        """
        self.name = pname
        self.gender = pgender
        self.counter += 1

    def greet(self, other):
        """
        方法
        """
        if isinstance(other, Person):
            print(f"Hello,{other.name}!")
        else:
            print("Hello,Python!")

    def set_name(self, new_name):
        """
        修改姓名
        """
        self.name = new_name

    def recount(self):
        """计数归零"""
        Person.counter = 0

    def show_info(self):
        print(f"我是{self.name},我是一个{self.gender}的")


class Student(Person):

    def __init__(self, sname, sgender, stu_id):
        super().__init__(sname, sgender)
        self.s_id = stu_id

    def show_info(self):
        print(f"我是{self.name},我是一个{self.gender}学生，我的学号是{self.s_id}。")

    def is_classmates(self, other):
        """
        根据学号的第5位判断两个学生是否同班。
        other指另一个学生对象；
        """
        return self.s_id[4] == other.s_id[4]

    def __repr__(self):
        return f"身份：学生\t姓名：{self.name}\t学号:{self.s_id}"

    def __str__(self):
        return f"我是{self.name},我是一个{self.gender}学生，我的学号是{self.s_id}。"


class Tutor(Person):

    def __init__(self, tname, tgender, t_id):
        super(Tutor, self).__init__(tname, tgender)
        self.t_id = t_id
        self.stu_lst = []

    def add_student(self, s):
        if not isinstance(s, Student):
            return
        if s in self.stu_lst:
            return
        self.stu_lst.append(s)

    def show_info(self):
        super().show_info()
        print(f"我是一名老师，工号是{self.t_id}")

    def show_students(self):
        print("我的学生名单".center(28, '*'))
        for s in self.stu_lst:
            print(f"姓名：{s.name}\t学号：{s.s_id}")
