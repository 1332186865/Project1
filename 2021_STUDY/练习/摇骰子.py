from random import randint


def roll_dice(n=2):
    total = 0
    for i in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())
