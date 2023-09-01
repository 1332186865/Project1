# 一个直方图是由许多矩形组成的，要求在给定的直方图中找出最大的矩形面积。假定直方图矩形数量不超出1000个。
# 假定所有矩形的宽度都为1个单位 。如下图所示的直方图中有7个矩形，高度分别是6，2，5，4，5，1，6，其中连续的矩形能组成的最大的矩形面积是12。
# 第一行输入直方图中矩形的数量。 第二行输入一组直方图的高度，每个高度用空格符间隔。 输出连续矩形能组成的最大矩形面积。
# 7
# 6 2 5 4 5 1 6 [2,1,5,6,2,3]
# 12  10
class Sqstack:
    def __init__(self):
        self.data = []

    def empty(self):  # 判断栈是否为空
        if len(self.data) == 0:
            return True
        return False

    def push(self, e):  # 进栈
        self.data.append(e)

    def pop(self):  # 出栈
        assert not self.empty()
        return self.data.pop()

    def gettop(self):  # 取栈顶元素
        assert not self.empty()
        return self.data[-1]


# 存在问题！！
def MaxArea(height, n):
    sq = Sqstack()
    max_area = 0
    for i in range(n):
        while not sq.empty() and sq.gettop() > int(height[i]):
            top = sq.gettop()
            sq.pop()
            max_area = max(max_area, (int(height[top]) * (i if sq.empty() else (i - sq.gettop() - 1))))
        sq.push(i)
    return max_area


a = int(input())
b = input().split(' ')
print(MaxArea(b, a))

# python参考
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n, heights, st, ans = len(heights), [0] + heights + [0], [], 0
#         for i in range(n + 2):
#             while st and heights[st[-1]] > heights[i]:
#                 ans = max(ans, heights[st.pop(-1)] * (i - st[-1] - 1))
#             st.append(i)
#         return ans
