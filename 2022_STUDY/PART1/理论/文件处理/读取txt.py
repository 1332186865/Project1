try:
    f = open("mydoc.txt", "r")
    hangshu = 0
    zifushu = 0
    wb = f.readlines()  # 读取文件内容，结果为列表
    for i in wb:  # 遍历列表元素
        hangshu += 1  # 统计行数
        zifushu += len(i)  # 统计字符数
        print(i)  # 输出文本内容
    print("文本行数是{}行，共计{}字符。".format(hangshu, zifushu))
    f.close()
except FileNotFoundError:  # 处理文件找不到的异常
    print("文件找不到")
else:  # 处理其他异常
    print("文件操作有错误")

# f = open("mydoc.txt", "r")
# hangshu = 0
# zifushu = 0
# while True:  # 若输入为空，则结束。
#     a = f.readline()  # 文本字符串添加换行，构成写入的数据
#     if a != "":
#         hangshu += 1  # 统计行数
#         zifushu += len(a)  # 统计字符数
#         print(a)  # 输出文本内容
#     else:  # 若文本内容为空结束循环
#         break
# print("文本行数是{}行，共计{}字符。".format(hangshu, zifushu))
# f.close()
