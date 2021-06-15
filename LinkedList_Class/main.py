from LinkedList import LinkedList
from Node import Node

llist = LinkedList()

llist.add_first(4)
llist.add_first(7)
llist.add_first(5)
llist.add_first(9)
llist.add_last(12)
llist.add_last(18)

array = llist.to_array()
print(array)



