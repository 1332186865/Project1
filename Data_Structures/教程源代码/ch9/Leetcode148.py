class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # def sortList(self, head: ListNode) -> ListNode:
    def sortList(self, head):
        p = head
        while p.next is not None:  # 查找尾结点p
            p = p.next
        # print(head.val,p.val)
        res = self.MergeSort(head, p)
        return res[0]

    def MergeSort(self, h, t):  # 对首尾结点分别为h,t的单链表排序
        if h == t: return [h, t]  # 只有一个结点时返回
        if h.next == t:  # 只有两个结点的情况
            if h.val > t.val:  # 反序时交换结点值
                h.val, t.val = t.val, h.val
            return [h, t]
        slow = h
        fast = h
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        h1 = h
        t1 = slow
        h2 = slow.next
        t1.next = None
        # print("H1:",end=' ')
        # disp(h1)
        # print("H2:",end=' ')
        $disp(h2)

        if fast.next is not None:
            t2 = fast.next
        else:
            t2 = fast
        res1 = self.MergeSort(h1, t1)
        res2 = self.MergeSort(h2, t2)
        return self.Merge(res1, res2)

    def Merge(self, res1, res2):
        h = ListNode(0)
        t = h
        p = res1[0]
        q = res2[0]
        while p is not None and q is not None:
            if p.val < q.val:
                t.next = p
                t = p
                p = p.next
            else:
                t.next = q
                t = q
                q = q.next
        t.next = None
        if p is not None:
            t.next = p
        else:
            t.next = q
        return [h.next, t]


def Create(a):
    h = ListNode(0)
    t = h
    for i in range(len(a)):
        s = ListNode(a[i])
        t.next = s
        t = s
    t.next = None
    return h.next


def disp(h):
    while h is not None:
        print(h.val, end=' ')
        h = h.next
    print()


a = [-1, 5, 3, 4, 0]
h = Create(a)
print("h:", end=' ')
disp(h)
obj = Solution()
L = obj.sortList(h)
print("L:", end=' ')
disp(L)
