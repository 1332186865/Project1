# 二叉树结构的基本操作(添加元素,先序、中序、后序、层次遍历)非递归实现(from CSDN)
class TreeNode:
    # 定义树的结点内容（数据、左右孩子）
    def __init__(self, _telem, _lchild=None, _rchild=None, _flag=0):
        self._telem = _telem
        self._lchild = _lchild
        self._rchild = _rchild
        self._flag = _flag


class Tree:
    # 初始化一个根结点,定义一个列表存储数的结点地址
    def __init__(self, _root=None):
        self._root = _root

    # 非递归创建树并且添加元素
    def tree_add(self, _elem):
        # 实例化需要添加元素的结点
        node = TreeNode(_elem)
        # 如果树是空的，则对根节点赋值
        if self._root is None:
            self._root = node
        else:
            # 定义一个判断列表
            queue = [self._root]

            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                # 判断那一个结点的哪一个孩子为空，为空则将新添加的结点的元素赋值给孩子为空的位置
                if cur._lchild is None:
                    cur._lchild = node
                    return
                elif cur._rchild is None:
                    cur._rchild = node
                    return
                else:
                    # 如果左右子树都不为空，往判断列表加入子树，循环进行子树的判断
                    queue.append(cur._lchild)
                    queue.append(cur._rchild)

    # 非递归先序遍历(其利用栈的特性，先将根结点入栈，然后出栈；之后找其右子树结点入栈，出栈；左子树入栈，出栈)
    @staticmethod
    def non_recursion_preorder(_root):
        # 判断空
        if _root is None:
            return
        else:
            # 定义一个列表模仿栈的操作
            stack = [_root]
            # 将传入的结点添加进栈中
            # 栈不为空
            while stack:
                # 弹出栈的元素
                node = stack.pop()
                # 打印弹出元素的内容
                print(node._telem, end=' ')
                # 判断是否存在其右子树是否存在，存在则入栈，否则器左子树入栈
                if node._rchild is not None:
                    stack.append(node._rchild)
                if node._lchild is not None:
                    stack.append(node._lchild)

    # 非递归中序遍历(通过操作栈先将左节点压入栈直到左节点为空，出栈顶元素，打印，当没有左结点时，将当前节点的右孩子赋值给_root，依次循环)
    @staticmethod
    def non_recursion_inorder(_root):
        # 判空
        if _root is None:
            return
        # 定义一个列表进行栈的操作
        stack = []
        # 循环结束条件:栈不为空，或者结点不为空
        while stack or _root is not None:
            while _root is not None:
                # 压栈操作，继续将其左子树结点压栈
                stack.append(_root)
                _root = _root._lchild
            # 进行到该位置，则说明其左结点已经不存在其左子树了；栈不为空进行出栈顶打印操作
            if stack:
                data = stack.pop()
                _root = data._rchild
                print(data._telem, end=" ")

    # 非递归后序遍历(使用表示量)
    @staticmethod
    def non_recursion_postorder1(_root):
        # 判空
        if _root is None:
            return
        # 创建一个栈
        # 对结点的左子树压栈
        stack = [_root]
        # 变换指针（一直想左孩子往下走）
        node_root = _root._lchild
        # 栈不为空或者结点存在
        while stack or node_root:
            # 结点存在
            while node_root is not None:
                # 结点存在则继续压栈
                stack.append(node_root)
                # 继续向左子树走
                node_root = node_root._lchild
            # 左子树找完之后，出栈
            node_root = stack.pop()
            # 判断其右子树是否存在，并判断是否被访问过(默认为0为访问，1为已访问)
            if node_root._rchild is not None and node_root._flag == 0:
                # 进栈
                stack.append(node_root)
                # 标识是否访问的标识量改变，避免重复访问
                node_root._flag = 1
                # 继续找其右子树
                node_root = node_root._rchild
            else:
                # 如果右结点被访问过，则打印当前结点数据
                print(node_root._telem, end=' ')
                # 当前已访问到叶子结点（重置结点实现回溯过程）
                node_root = None

    # 非递归后序遍历(使用两个栈实现，即使非递归前序遍历的出栈顺序在进一次栈，之后弹出)
    @staticmethod
    def non_recursion_postorder2(_root):
        # 判断空
        if _root is None:
            return
        # 定义两个栈
        stack1 = []
        stack2 = []
        # 将结点加入第一个栈中
        stack1.append(_root)
        # 第一个栈不为空
        while stack1:
            _root = stack1.pop()
            if _root._lchild is not None:
                stack1.append(_root._lchild)
            if _root._rchild is not None:
                stack1.append(_root._rchild)
            stack2.append(_root)

        while stack2:
            data = stack2.pop()
            print(data._telem, end=' ')

    # 层次遍历
    def level_traversal(self, _root):
        # 判断空
        if _root is None:
            return
        # 定义一个列表存储树的结点
        queue = [self._root]
        # 列表不为空则一直拿取
        while queue:
            # 抛出列表第一个元素
            node = queue.pop(0)
            # 打印
            print(node._telem, end=' ')
            # 当前结点的左右结点不为空则将其添加到列表中，继续循环拿取，为空调出while循环
            if node._lchild is not None:
                queue.append(node._lchild)
            if node._rchild is not None:
                queue.append(node._rchild)


if __name__ == '__main__':
    tree = Tree()
    for i in range(ord('A'), ord('Z') + 1):
        tree.tree_add(chr(i))
    print('非递归实现先序遍历:\n', end=' ')
    tree.non_recursion_preorder(tree._root)

    print('\n\n非递归中序遍历:\n', end=' ')
    tree.non_recursion_inorder(tree._root)

    print('\n\n非递归后序遍历（使用标识量实现）:\n', end=' ')
    tree.non_recursion_postorder1(tree._root)

    print('\n\n非递归后序遍历（使用双栈实现）:\n', end=' ')
    tree.non_recursion_postorder2(tree._root)

    print('\n\n层次遍历（队列实现）:\n', end=' ')
    tree.level_traversal(tree._root)
