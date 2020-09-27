from linked_list.Linked_list import LinkedList

# This is a program to reverse a linklist

l1 = LinkedList()
l2 = LinkedList()
l1.add_last(10)
l1.add_last(20)
l1.add_last(30)
l1.print_list()
print("After Reverse")
for i in range(3):
    l2.add_first(l1.delete_first())
l2.print_list()
