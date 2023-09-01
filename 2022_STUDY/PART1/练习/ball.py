# 1.一个球从100米高度落下,每次落地后反弹高度为原高度的一半
# 1)写程序算出皮球从第10次落地后反弹高度是多少?
# 2)球共经过多少米路径？
def ball_last_height(height, times):
    for _ in range(times):
        height /= 2
    return height


def ball_distance(height: int, times: int) -> float:
    """
    求球移动的总距离
    :param height: 高度
    :param times: 次数
    :return : 距离
    """
    meter = 0
    for _ in range(times):
        meter += height
        height /= 2
        meter += height
    return meter


height = ball_last_height(100, 10)
print("最终的高度是：", height)
meter = ball_distance(100, 10)
print("球经历的路径是：", meter)
