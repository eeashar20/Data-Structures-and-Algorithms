from LinkedList import LinkedList
from Node import Node

llist = LinkedList()
print(llist.size())

llist.add_first(4)
print(llist.size())

llist.add_first(7)
llist.add_first(5)
print(llist.size())

llist.add_first(9)
print(llist.size())

llist.add_last(12)
print(llist.size())

# print(llist.first.value)
# print(llist.last.value)

llist.delete_last()
print(llist.size())

# print(llist.last.value)

llist.delete_first()
print(llist.size())

# print(llist.first.value)



