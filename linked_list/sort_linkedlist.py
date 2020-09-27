from linked_list.Linked_list import LinkedList

l1 = LinkedList()
for i in range(10, 5, -1):
    l1.add_last(i)
for i in range(1, 6):
    l1.add_last(i)
l1.print_list()
print("After Sorting")
l1.sort_list()
l1.print_list()

# Here Sorting Method uses Selection Sort
