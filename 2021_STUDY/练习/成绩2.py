c = float(input("请输入成绩："))
if 90 <= c <= 100:
    print("A")
elif 80 <= c < 90:
    print("B")
elif 70 <= c < 80:
    print("C")
elif 60 <= c < 70:
    print("D")
elif 0 <= c < 60:
    print("E")
elif not (0 <= c <= 100):
    print("成绩有误")
