from Node import Node


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.len = 0

    """This function determines whether the LinkedList is empty or not"""

    def is_empty(self):
        return self.first is None

    """This function inserts the node at the beginning of the LinkedList"""

    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

        self.len += 1

    """This function inserts the node at the beginning of the LinkedList"""

    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

        self.len += 1

    """"This function deletes the node from the beginning of the LinkedList"""

    def delete_first(self):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        if self.first == self.last:
            self.first = self.last = None
        else:
            node = self.first
            self.first = self.first.next
            node.next = None

        self.len -= 1

    """This function deletes the node from the end of the LinkedList"""

    def delete_last(self):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        if self.first == self.last:
            self.first = self.last = None
        else:
            node = self.first
            while node.next.next is not None:
                node = node.next
            node.next = None
            self.last = node

        self.len -= 1

    """This function determines whether the given number is present in the LinkedList or not."""

    def contains(self, data):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        return self.index_of(data) != -1

    """This function finds the index of the given element"""

    def index_of(self, data):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        current = self.first
        index = 0
        while current is not None:
            if current.value == data:
                return index
            current = current.next
            index += 1
        return -1

    """This function returns the size of the Linked List i.e. the number of elements in it."""

    def size(self):
        return self.len

    """This function converts the Linked List into an Array"""

    def to_array(self):
        array = list()
        current_node = self.first
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next

        return array

    """This function reverses the Linked List without making its copy"""
    def reverse(self):
        previous = self.first
        current = previous.next
        previous.next = None
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following

        tmp = self.first
        self.first = self.last
        self.last = tmp


