for m in range(1, 17):  # 男50/3约为17
    for f in range(1, 25):  # 女50/2=25
        c = 30 - m - f
        qs = 3 * m + 2 * f + c  # 总钱数
        if qs == 50:
            print("男人有{}人，女人有{}人，小孩有{}人".format(m, f, c))
