from LinkedList import LinkedList
from Node import Node

llist = LinkedList()
llist.add_first(4)
llist.add_first(7)
llist.add_first(5)
llist.add_first(9)
llist.add_last(12)
print(llist.first.value)
print(llist.last.value)
# llist.delete_last()
# print(llist.last.value)
# llist.delete_first()
# print(llist.first.value)
print(llist.contains(7))
print(llist.index_of(12))


