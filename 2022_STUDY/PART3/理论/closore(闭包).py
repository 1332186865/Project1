#  Copyright (c) 2022. Generated by Gu.
#  -*- coding=utf-8 -*-
def give_gift_money(money):
    """
    获取压岁钱
    :param money:钱
    :return: 行为
    """
    print('得到了%d压岁钱' % money)

    def child_buy(target, price):
        """
        买东西
        :param target:物品
        :param price: 价格
        :return: 结果
        """
        nonlocal money
        if money >= price:
            money -= price
            print('花了%d钱, 买了%s, 剩下%d钱' % (price, target, money))
        else:
            print('钱不够')

    return child_buy


if __name__ == '__main__':
    action = give_gift_money(10000)
    action('98k', 3500)
    action('炸鸡', 4300)
