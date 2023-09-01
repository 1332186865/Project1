s = [9, 7, 8, 3, 2, 1, 5, 6]
for i in s:
    a = s.index(i)
    if i % 2 == 0:
        s[a] = i ** 2
print(s)
