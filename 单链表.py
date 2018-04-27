class LNode:
    """
    定义实现单链表的数据结构
    """
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class MyList:
    """
    定义实现单链表操作类
    """

    def __init__(self):
        # 因为单链表的查找方式是从表头开始，所以只需要定义一个
        # 链接头结点的域即可，初始化为None代表建立的是一个空表
        self._head = None

    def is_empty(self):
        # 判断链表是否为空
        return self._head is None

    def prepend(self, elem):
        # 往表头插入数据
        self._head = LNode(elem, self._head)

    def lpop(self):
        # 删除表头结点,并返回
        if self._head is None:
            raise Exception('链表为空，不能执行该操作')
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        if self._head is None:        # 如果结点为空，则新增结点为头结点
            self._head = LNode(elem)
            return
        p = self._head        # 头结点不为空，则新增结点为最后结点的next域
        if p.next:
            p = p.next
        p.next = LNode(elem)

    def rpop(self):
        # 删除最后结点
        if self._head is None:
            raise Exception('链表为空，不能执行该操作')
        p = self._head
        if p.next is None:   # 链表只有一个结点
            e = p.elem
            self._head = None
            return e
        while p.next.next:   # 当p.next.next为空时，代表找到倒数第二个结点
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, val):
        # 这里假设链表储存的数据为字符串,查找符合条件的结点, 没有找到返回None
        p = self._head
        while p:
            if p.elem == val:
                return p
            p = p.next


class MyCList:
    """
    定义循环单链表类
    """
    def __init__(self):
        # 循环单链表是尾结点的next域指向头结点，为了实现头尾结点的删除操作都为
        # O(1)时间，只要创建一个链接尾结点的域即可
        self._end = None

    def is_empty(self):
        return self._end is None

    def prepend(self, elem):
        # 头部插入
        p = LNode(elem)
        if self._end is None:  # 空链表插入结点
            p.next = p          # 因为只有一个结点，所以next域指向自己
            self._end = p
        else:
            p.next = self._end.next
            self._end.next = p

    def append(self, elem):
        # 尾端插入
        self.prepend(elem)   # 因为循环单链表内部是一个环，头尾是人为定义的，所以可以先往头部插入新增结点
        self._end = self._end.next   # 然后将self._end指向头部结点，这时头部结点即为尾部结点

    def lpop(self):
        # 头部弹出
        if self._end is None:
            raise Exception('链表为空')
        p = self._end.next
        if self._end is p:   # 只有一个结点
            self._end = None
        else:
            self._end.next = p.next
        return p.elem