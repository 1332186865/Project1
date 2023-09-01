file1 = open('women_labor.csv', 'r')
data = {}
with open("women_labor.csv", 'r', encoding='utf-8') as reader:
    reader.readline()
    for line in reader:
        data[line.strip('\n').split(',')[1]] = line.strip('\n').split(',')[8]
data1 = sorted(data.items(), key=lambda x: x[1], reverse=True)
print("前五个国家为：")
for i in range(5):
    print(data1[i][0], end=',')
print("\n后五个国家为：")
for i in range(5):
    print(data1[-1 - i][0], end=',')
a = str(data.get('China'))
china = data1.index(('China', a))
print('\n中国位置为：', china)
