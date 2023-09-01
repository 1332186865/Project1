plaincode = input("请输入原文：")
n = len(plaincode)
for i in range(n):
    x = plaincode[i]
    if "A" <= x <= "Z":
        k = ord("A") + ((ord(x) - ord("A")) + 3) % 26
        y = chr(k)
        print(y, end="")
    else:
        print(x, end="")
