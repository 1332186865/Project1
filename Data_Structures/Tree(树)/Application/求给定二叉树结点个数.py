from BTree import BTree, BTNode


def NodeCount1(bt):  # 基于先序遍历求结点个数
    return _NodeCount1(bt.b)


def _NodeCount1(t):
    if t is None:  # 空树结点个数为0
        return 0
    k = 1  # 根结点计数1，相当于访问根结点
    m = _NodeCount1(t.lchild)  # 遍历求左子树的结点个数
    n = _NodeCount1(t.rchild)  # 遍历求右子树的结点个数
    return k + m + n


def NodeCount2(bt):  # 基于中序遍历求结点个数
    return _NodeCount2(bt.b)


def _NodeCount2(t):
    if t is None:  # 空树结点个数为0
        return 0
    m = _NodeCount2(t.lchild)  # 遍历求左子树的结点个数
    k = 1  # 根结点计数1，相当于访问根结点
    n = _NodeCount2(t.rchild)  # 遍历求右子树的结点个数
    return k + m + n


def NodeCount3(bt):  # 基于后序遍历求结点个数
    return _NodeCount3(bt.b)


def _NodeCount3(t):
    if t is None:  # 空树结点个数为0
        return 0
    m = _NodeCount3(t.lchild)  # 遍历求左子树的结点个数
    n = _NodeCount3(t.rchild)  # 遍历求右子树的结点个数
    k = 1  # 根结点计数1，相当于访问根结点
    return k + m + n


def NodeCount4(bt):  # 递归求解
    return _NodeCount4(bt.b)


def _NodeCount4(t):
    if t is None:
        return 0  # 空树结点个数为0
    else:
        return _NodeCount4(t.lchild) + _NodeCount4(t.rchild) + 1


# 主程序
b = BTNode('A')
p1 = BTNode('B')
p2 = BTNode('C')
p3 = BTNode('D')
p4 = BTNode('E')
p5 = BTNode('F')
p6 = BTNode('G')
b.lchild = p1
b.rchild = p2
p1.lchild = p3
p3.rchild = p6
p2.lchild = p4
p2.rchild = p5
bt = BTree()
bt.set_root(b)
print("bt:", end=' ')
print(bt.disp_b_tree())
print("算法1 bt中结点个数:%d" % NodeCount1(bt))
print("算法2 bt中结点个数:%d" % NodeCount2(bt))
print("算法3 bt中结点个数:%d" % NodeCount3(bt))
print("算法4 bt中结点个数:%d" % NodeCount4(bt))
