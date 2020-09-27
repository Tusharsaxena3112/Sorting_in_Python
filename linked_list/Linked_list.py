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

    def delete_first(self):
        pop = None
        if self.first == self.last:
            pop = self.first
            self.first = self.last = None
        elif self.first is None and self.last is None:
            print('No Entry is list. Kindly add first before deleting')
        else:
            pop = self.first
            temp = self.first.next
            self.first.next = None
            self.first = temp
        return pop.data

    def delete_last(self):
        pop = None
        if self.first == self.last:
            pop = self.last
            self.first = self.last = None
        elif self.first is None and self.last is None:
            print('No Entry is list. Kindly add first before deleting')
        else:
            pop = self.last
            temp = self.first
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.last = temp
        return pop.data

    def sort_list(self):
        current = self.first
        index = None
        while current is not None:
            index = current
            m = current.data
            i = index
            while index is not None:
                if index.data < m:
                    m = index.data
                    i = index
                index = index.next
            current.data, i.data = i.data, current.data
            current = current.next

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
    l.delete_first()
    l.delete_last()
    l.print_list()
