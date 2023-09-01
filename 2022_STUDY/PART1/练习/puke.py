import random


def get_new_poker():
    kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
    numbers = ['A']
    numbers += [str(x) for x in range(2, 11)]
    numbers += ['J', 'Q', 'K']
    ls = [k + n for k in kinds for n in numbers]
    ls += ['大王', '小王']
    return ls


def play():
    poker = get_new_poker()
    random.shuffle(poker)
    input("按任意键发第一个人的牌")
    print("第一个人的牌是：", poker[:17])
    input("按任意键发第二个人的牌")
    print("第二个人的牌是：", poker[17:34])
    input("按任意键发第三个人的牌")
    print("第三个人的牌是：", poker[34:51])
    input("按任意键看底牌")
    print("底牌是：", poker[51:])


play()
