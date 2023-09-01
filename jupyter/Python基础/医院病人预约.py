# 在这个问题中，我们将为医院建立一个超级小的工具来管理病人的预约。
# (a)一个病人是一个有名字和出生日期的对象。建立一个病人类，其构造函数接收姓名和出生日期（选择一种方式来表示日期）。在该类中添加正确的方法，以便在打印病人对象时，显示："病人{姓名}，出生{出生日期}"。
# (b)同样地，医生是一个有名字和相关部门的对象。制作一个带有构造函数的类，将这两个信息作为参数。
# (c)一个预约是一个日期、时间、病人、医生和期限之间的关联。为预约制作一个类。
# (d)一个议程是一个约会的集合。为议程创建一个类。添加一个方法来存储一个给定的病人、医生、日期、时间和持续时间的约会。该方法应该只在约会不与同一医生的任何其他约会重叠时添加。

class Patient:
    def __init__(self, name, birth):
        self.name = name
        self.birth = birth

    def __repr__(self):
        return "病人{}，出生{}".format(self.name, self.birth)


class Doctor:
    def __init__(self, name, department):
        self.name = name
        self.department = department


class Appointment:
    def __init__(self, date, time, patient, doctor, duration):
        self.date = date
        self.time = time
        self.patient = patient
        self.doctor = doctor
        self.duration = duration
        self.lst = [date, time, patient, doctor, duration]

    def get_data(self):
        return self.lst


class Agenda:
    def __init__(self):
        self.lst = []

    def store_data(self, appointment):
        if appointment not in self.lst:
            self.lst.append(appointment)
