class SStack:
    """
    基于顺序表实现的栈
    """
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    # 查看栈顶元素
    def top(self):
        if not self._elems:
            raise Exception('栈为空')
        return self._elems[-1]

    # 入栈
    def push(self,elem):
        self._elems.append(elem)

    # 出栈
    def pop(self):
        if not self._elems:
            raise Exception('栈为空')
        return self._elems.pop()


class LNode:
    """
    单链表的结点类
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LStack:
    """
    基于单链表实现的栈
    """
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise Exception('栈为空')
        return self._top.elem

    def push(self,elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise Exception('栈为空')
        p = self._top
        self._top = p.next
        return p.elem