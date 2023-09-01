# 文件movies.txt给出了一百多部热榜电影的信息,请从所有主演(actors)的名单中找出参演电影数量最多
# 的10名演员姓名。
actor_list = []
with open('movies.txt', encoding='utf-8') as f:
    while True:
        temp = f.readline()
        actor_list.append(temp.get('actor'))
        if temp == '':
            break

print(actor_list)
