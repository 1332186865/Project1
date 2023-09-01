import copy

from BTree import BTree, BTNode

minpath = []  # 全局变量，存放最短路径
minsum = 0x3f3f3f3f  # 全局变量，存放最短路径长度,初始为∞


def Shortpath(bt):  # 求二叉树bt中的最短路径
    r = bt.b  # 根结点为r
    if r is not None:
        path = [r.data]  # 将根结点u添加的path中
        sum = int(r.data)  # 当前路径长度为r.data
        Shortpath1(r, path, sum)


def Shortpath1(t, path, sum):  # 被Shortpath函数调用
    global minsum
    global minpath
    if t.lchild is None and t.rchild is None:  # 找到一个叶子结点
        if sum < minsum:
            minsum = sum
            minpath = copy.deepcopy(path)
        return
    if t.lchild is not None:  # 结点t存在左孩子结点
        path.append(t.lchild.data)  # 将左孩子结点值添加到path
        sum += int(t.lchild.data)  # 将左孩子结点值累计到sum
        Shortpath1(t.lchild, path, sum)  # 从左孩子出发搜索
        path.pop()  # 从左孩子回退到t
        sum -= int(t.lchild.data)
    if t.rchild is not None:  # 结点t存在右孩子结点
        path.append(t.rchild.data)  # 将右孩子结点值添加到path
        sum += int(t.rchild.data)  # 将右孩子结点值累计到sum
        Shortpath1(t.rchild, path, sum)  # 从右孩子出发搜索
        path.pop()  # 从右孩子回退到t
        sum -= int(t.rchild.data)


# 主程序
b = BTNode('2')
p1 = BTNode('5')
p2 = BTNode('3')
p3 = BTNode('7')
p4 = BTNode('4')
p5 = BTNode('6')
p6 = BTNode('1')
b.lchild = p1
b.rchild = p2
p1.lchild = p3
p2.lchild = p4
p2.rchild = p5
p4.lchild = p6
bt = BTree()
bt.SetRoot(b)
print("bt:", end='  ')
print(bt.DispBTree())
print("求解结果")
Shortpath(bt)
print("  最短路径: ", minpath)
print("  路径长度:  %d" % minsum)
