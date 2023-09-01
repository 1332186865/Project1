location = [0, 0]
while True:
    command = input('请输入移动方向和移动单位,并用空格隔开:').split(' ')
    if command[0] == 'UP':
        location[1] += int(command[1])
    elif command[0] == 'DOWN':
        location[1] -= int(command[1])
    elif command[0] == 'LEFT':
        location[0] -= int(command[1])
    elif command[0] == 'RIGHT':
        location[0] += int(command[1])
    else:
        distance = location[0] ** 2 + location[1] ** 2
        print('距离原点坐标为:', distance ** 0.5)
        break
