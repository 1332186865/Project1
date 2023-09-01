f = open("mydox.txt", "w")  # 打开文件
a = input("请输入一行文本")
while a != "":  # 若输入为空，则结束。
    f.writelines(a)
    f.writelines('\n')  # 字符串换行
    a = input("请输入一行文本")  # 继续输入文本
f.close()  # 关闭文件
