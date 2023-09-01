# 使用列表推导式删除该列表中第0位、第4位、第5位的数据并输出新列表。
# [12, 24, 35, 70, 88, 120, 155] --> [24, 35, 70, 155]
# ls = [12, 24, 35, 70, 88, 120, 155]
# ls1 = [ls[i] for i in range(len(ls)) if i not in [5, 4, 0]]
# print(ls1)
# # 生成一个字典,其键为0到20的所有整数,其值为键的平方。
# dict = {x: x ** 2 for x in range(21)}
# print(dict)
# def decimal_to_binary(num):
#     s = []
#     binary = ""
#     while num > 0:
#         remainder = num % 2
#         s.append(remainder)
#         num //= 2
#     while len(s) > 0:
#         binary = binary + str(s.pop())
#     print(binary)
#
#
# decimal_to_binary(20)
# 实现一个函数remove_dups(astr),输入一个由逗号分隔的英文单词组成的字符串,请删除字符串中的重复
# 出现的单词,并对单词按照字母表顺序进行排序并输出。
# 例如:
# >>>remove_dups('without,hello,bad,world,hello')
# ['bad', 'hello', 'without', 'world']

# def remove_dups(astr):
#     temp = set(astr.split(','))
#     temp = [i for i in temp]
#     temp = sorted(temp)
#     print(temp)
#
#
# remove_dups('without,hello,bad,world,hello')

# 在做了一系列的实验之后,我们得到了探测到某些亚原子粒子的概率。粒子的名字是字典的键,概率是:
# ('neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14]。编写一个函数,将
# 这种类型的单个字典作为输入,并返回最不可能被观察到的粒子。例如,给定前面显示的字典,函数将返
# 回'meson'。min(dict, key=dict.get)

def min_dict_value(dict):
    return min(dict, key=dict.get)


dict1 = {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07, 'neutrino': 0.14}
print(min_dict_value(dict1))
