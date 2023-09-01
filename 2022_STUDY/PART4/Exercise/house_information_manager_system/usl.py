"""
    用户显示层
"""
from bll import HouseManagerController


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1键显示所有房源信息")
        print("2键显示总价最高的房源信息")
        print("3键显示面积最小的房源信息")
        print("4键根据总价升序显示房源信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__show_houses()
        elif item == "2":
            self.__show_house_by_max_total_price()
        elif item == "3":
            self.__show_house_by_min_area()
        elif item == "4":
            self.__show_houses_by_ascending_total_price()

    def __show_houses(self):
        for house in self.__controller.list_houses:
            # 直接打印对象,由对象的__str__方法决定打印风格
            print(house)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_house_by_max_total_price(self):
        house = self.__controller.get_house_by_max_total_price()
        print(house)

    def __show_house_by_min_area(self):
        house = self.__controller.get_house_by_min_area()
        print(house)

    def __show_houses_by_ascending_total_price(self):
        self.__controller.ascending_by_total_price()
        self.__show_houses()




