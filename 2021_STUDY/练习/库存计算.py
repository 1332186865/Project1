n = input("请输入商品名称：")
m = float(input("请输入商品库存量："))
if m == 0:
    print("告罄，急需进货")
elif m < 50:
    print("库存不足")
elif m < 400:
    print("库存正常")
else:
    print("滞销")
