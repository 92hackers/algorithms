# 链表
# 支持基本的增删改查操作

class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.size = None
        self.build_list(*args)

    def build_list(self, *args):
        head = None
        tail = None

        for i in args:
            new_node = ListNode(i)
            if tail:
                tail.next = new_node
                new_node.prev = tail
            else:
                head = new_node
            tail = new_node

        self.head = head
        self.tail = tail
        self.get_size() # calculate the list size

    def insert(self, value, index):
        # return new size of the list
        max_index = self.size - 1
        if index < 0 or index > max_index:
            raise Exception('index out of range')

        new_node = ListNode(value)
        self.size += 1

        # insert as the new head
        if index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            return self.size

        target = self.head.next
        current_index = 1
        while current_index < max_index + 1:
            if current_index == index:
                prev_node = target.prev
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = target
                target.prev = new_node
                return self.size
            else:
                current_index += 1
                target = target.next

    def push(self, value):
        new_node = ListNode(value)

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1
        return self.size

    def pop(self):
        # 从链表中去除该元素
        if self.size == 0:
            return

        if self.size == 1:
            result = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return result

        self.size -= 1
        target = self.tail.prev
        target.next = None
        # 返回
        result = self.tail.data
        self.tail = target
        return result

    def delete(self, value):
        if value == self.head.data:
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.size -= 1
            return self.size

        if value == self.tail.data:
            next_tail = self.tail.prev
            next_tail.next = None
            self.tail.prev = None
            self.tail = next_tail
            self.size -= 1
            return self.size

        target = self.head.next
        while target is not None:
            if value == target.data:
                prev_node = target.prev
                next_node = target.next
                prev_node.next = next_node
                next_node.prev = prev_node
                self.size -= 1
                return self.size
            else:
                target = target.next

        raise Exception(value + ' not found in the linked list')


    def indexOf(self, value):
        # get index of a value in list
        target = self.head
        count = 0

        while target is not None:
            if target.data == value:
                return count
            target = target.next
            count += 1

        return -1

    def get_size(self):
        if self.size is not None:
            return self.size

        count = 0
        target = self.head
        while target is not None:
            count += 1
            target = target.next
        self.size = count
        return count

    def get_list(self):
        target = self.head
        arr = []

        while target is not None:
            arr.append(target.data)
            target = target.next

        return arr

    def get_reversed(self):
        target = self.tail
        arr = []

        while target is not None:
            arr.append(target.data)
            target = target.prev

        return arr

a = LinkedList(23, 19, 0, 34, 29)

print(a.get_list())

a.push(99)
print(a.get_list())

a.pop()
print(a.get_list())

print(a.indexOf(10))

a.insert(555, 4)
print(a.get_list())

a.insert(999, 0)
print(a.get_list())
print(a.get_reversed())

a.insert(66666, a.get_size() - 1)
print(a.get_list())
print(a.get_reversed())

a.delete(555)
print(a.get_list())
print(a.get_reversed())
