from LinkedList import LinkedList

llist = LinkedList()

# llist.add_first(4)
# llist.add_first(7)
# llist.add_first(5)
# llist.add_first(9)
# llist.add_last(12)
# llist.add_last(18)
# llist.add_first(42)
# llist.add_last(789)

# llist.reverse()
# # print(llist)
# array = llist.to_array()
# print(array)

llist.add_last(10)
llist.add_last(20)
llist.add_last(30)
node = llist.last
llist.add_last(40)
llist.add_last(50)
llist.last.next = node # This line is here to make a loop to the third node from the last node.
# llist.add_last(60)
# llist.add_last(70)
# llist.add_last(80)
print(llist.has_loop())






