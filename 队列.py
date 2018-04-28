class LNode:
    """
    单链表的结点类
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LQueue:
    """
    基于有尾部指针的单链表实现的队列
    """
    def __init__(self):
        self._head = None
        self._end = None

    def is_empty(self):
        return self._head is None

    def peak(self):
        if self._head is None:
            raise Exception('队列为空')
        return self._head.elem

    # 入队
    def enqueue(self, elem):
        p = LNode(elem)
        if self._head is None:
            self._head = p
            self._end = p
        else:
            self._end.next = p
            self._end = p
    # 出队
    def dequeue(self):
        if self._head is None:
            return Exception('队列为空')
        p = self._head
        self._head = p.next
        return p.elem


class SQueue:
    """
    基于顺序表实现的队列
    """
    def __init__(self, init_len=8):
        # len是队列容量，elems是队列容器，_head是队列顶部元素，_num是队列元素个数
        # 当len = _num时，就扩充队列容量
        self.len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise Exception('队列为空')
        return self._elems[self._head]

    def enqueue(self, elem):
        if self.len == self._num:
            self._extend()
        self._elems[(self._head+self._num)%self.len] = elem
        self._num += 1

    def dequeue(self):
        if self._num == 0:
            raise Exception('队列为空')
        e = self._elems[self._head]
        self._head = (self._head+1) % self.len
        self._num -= 1
        return e

    def _extend(self):
        old_len = self.len
        self.len *= 2
        new_elems = [0] * self.len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head+i) % old_len]  # 将旧队列元素放进新队列中
        self._elems, self._head = new_elems, 0