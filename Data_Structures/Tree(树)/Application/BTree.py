# 二叉树基本运算算法及其实现
# 先序、中序和后序遍历

from collections import deque


class BTNode:
    """二叉链中结点类"""

    def __init__(self, d=None):  # 构造方法
        self.data = d  # 结点值
        self.lchild = None  # 左孩子指针
        self.rchild = None  # 右孩子指针


class BTree:
    """二叉树类"""

    def __init__(self, d=None):  # 构造方法
        self.b = None  # 根结点指针

    def set_root(self, r):
        """设置根结点为r"""
        self.b = r

    def disp_b_tree(self):
        """返回二叉链的括号表示串"""
        return self._disp_b_tree1(self.b)

    def _disp_b_tree1(self, t):
        """被DispBTree方法调用"""
        if t is None:  # 空树返回空串
            return ""
        else:
            bstr = t.data  # 输出根结点值
            if t.lchild is not None or t.rchild is not None:
                bstr += "("  # 有孩子结点时输出"("
                bstr += self._disp_b_tree1(t.lchild)  # 递归输出左子树
                if t.rchild is not None:
                    bstr += ","  # 有右孩子结点时输出","
                bstr += self._disp_b_tree1(t.rchild)  # 递归输出右子树
                bstr += ")"  # 输出")"
            return bstr

    def find_node(self, x):
        """查找值为x的结点算法"""
        return self._find_node1(b, x)

    def _find_node1(self, t, x):
        """被FindNode方法调用"""
        if t is None:
            return None  # t为空时返回null
        elif t.data == x:
            return t  # t所指结点值为x时返回t
        else:
            p = self._find_node1(t.lchild, x)  # 在左子树中查找
            if p is not None:
                return p  # 在左子树中找到p结点，返回p
            else:
                return self._find_node1(t.rchild, x)  # 返回在右子树中查找结果

    def height(self):
        """求二叉树高度的算法"""
        return self._height1(b)

    def _height1(self, t):
        """被Height方法调用"""
        if t is None:
            return 0  # 空树的高度为0
        else:
            lh = self._height1(t.lchild)  # 求左子树高度lchildh
            rh = self._height1(t.rchild)  # 求右子树高度rchildh
            return max(lh, rh) + 1


def pre_order(bt):
    """先序遍历的递归算法"""
    pre_order1(bt.b)


def pre_order1(t):
    """被PreOrder方法调用"""
    if t is not None:
        print(t.data, end=' ')  # 访问根结点
        pre_order1(t.lchild)  # 先序遍历左子树
        pre_order1(t.rchild)  # 先序遍历右子树


def in_order(bt):
    """中序遍历的递归算法"""
    in_order1(bt.b)


def in_order1(t):
    """被InOrder方法调用"""
    if t is not None:
        in_order1(t.lchild)  # 中序遍历左子树
        print(t.data, end=' ')  # 访问根结点
        in_order1(t.rchild)  # 中序遍历右子树


def post_order(bt):
    """后序遍历的递归算法"""
    post_order1(bt.b)


def post_order1(t):
    """被PostOrder方法调用"""
    if t is not None:
        post_order1(t.lchild)  # 后序遍历左子树
        post_order1(t.rchild)  # 后序遍历右子树
        print(t.data, end=' ')  # 访问根结点


def level_order(bt):
    """层次遍历的算法"""
    qu = deque()  # 将双端队列作为普通队列qu
    qu.append(bt.b)  # 根结点进队
    while len(qu) > 0:  # 队不空循环
        p = qu.popleft()  # 出队一个结点
        print(p.data, end=' ')  # 访问p结点
        if p.lchild is not None:  # 有左孩子时将其进队
            qu.append(p.lchild)
        if p.rchild is not None:  # 有右孩子时将其进队
            qu.append(p.rchild)


if __name__ == '__main__':
    b = BTNode('A')  # 建立各个结点
    p1 = BTNode('B')
    p2 = BTNode('C')
    p3 = BTNode('D')
    p4 = BTNode('E')
    p5 = BTNode('F')
    p6 = BTNode('G')
    b.lchild = p1  # 建立结点之间的关系
    b.rchild = p2
    p1.lchild = p3
    p3.rchild = p6
    p2.lchild = p4
    p2.rchild = p5

    bt = BTree()
    bt.set_root(b)

    print("bt:", end=' ')
    print(bt.disp_b_tree())
    x = 'X'
    p = bt.find_node(x)
    if p is not None:
        print("bt中存在" + x)
    else:
        print("bt中不存在" + x)
    print("bt的高度=%d" % (bt.height()))
    print("先序序列:", end=' ')
    pre_order(bt)
    print()
    print("中序序列:", end=' ')
    in_order(bt)
    print()
    print("后序序列:", end=' ')
    post_order(bt)
    print()
    print("层次序列:", end=' ')
    level_order(bt)
    print()
