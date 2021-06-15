from Node import Node


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    """This function determines whether the LinkedList is empty or not"""

    def is_empty(self):
        if self.first is None:
            return True
        else:
            return False

    """This function inserts the node at the beginning of the LinkedList"""

    def add_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node

    """This function inserts the node at the beginning of the LinkedList"""

    def add_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = self.last = node
            # self.last = self.first
        else:
            self.last.next = node
            self.last = node

    """"This function deletes the node from the beginning of the LinkedList"""

    def delete_first(self):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        node = self.first
        self.first = self.first.next
        node.next = None

    """This function deletes the node from the end of the LinkedList"""

    def delete_last(self):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        node = self.first
        while node.next.next is not None:
            node = node.next
        node.next = None
        self.last = node

    """This function determines whether the given number is present in the LinkedList or not."""

    def contains(self, data):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        node = self.first
        while node is not None:
            if node.value == data:
                print(f"The Linked List contains {data}.")
                return
            node = node.next
        print(f"{data} is not present in the LinkedList.")

    """This function finds the index of the given element"""

    def index_of(self, data):
        if self.is_empty():
            print("The LinkedList is empty!")
            return

        node = self.first
        index = 0
        while node is not None:
            if node.value == data:
                return index
            node = node.next
            index += 1
        print(f"{data} is not present in the LinkedList.")
        return -1
