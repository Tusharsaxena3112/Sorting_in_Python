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
        if self.first == self.last:
            self.first = self.last = None
        elif self.first is None and self.last is None:
            print('No Entry is list. Kindly add first before deleting')
        else:
            temp = self.first.next
            self.first.next = None
            self.first = temp

    def delete_last(self):
        if self.first == self.last:
            self.first = self.last = None
        elif self.first is None and self.last is None:
            print('No Entry is list. Kindly add first before deleting')
        else:
            temp = self.first
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.last = temp


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
