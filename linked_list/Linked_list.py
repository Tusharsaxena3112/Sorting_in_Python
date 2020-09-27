class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        if self.first is None and self.last is None:
            return True
        else:
            return False

    def add_last(self, element):
        node = Node(element)
        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def add_first(self, element):
        node = Node(element)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

    def print_list(self):
        temp = self.first
        while temp is not None:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    l = LinkedList()
    # print(l.is_empty())
    l.add_last(5)
    l.add_last(10)
    l.add_last(15)
    l.add_first(3)
    l.print_list()
