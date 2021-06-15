from Node import Node


class LinkedList:
    def __init__(self):
        self.first: Node = None
        self.last: Node = None

    """This function inserts the node at the beginning of the LinkedList"""

    def add_first(self, data):
        if self.first is None:
            self.first = Node(data)
            self.last = self.first
            return
        else:
            node: Node = self.first
            self.first = Node(data)
            self.first.next = node

    """This function inserts the node at the beginning of the LinkedList"""

    def add_last(self, data):
        if self.first is None:
            self.first = Node(data)
            self.last = self.first
            return
        else:
            node: Node = self.last
            self.last = Node(data)
            node.next = self.last

    """"This function deletes the node from the beginning of the LinkedList"""

    def delete_first(self):
        if self.first is None:
            print("The LinkedList is empty!")
            return
        
        node = self.first
        self.first = self.first.next
        node.next = None

    """This function deletes the node from the end of the LinkedList"""

    def delete_last(self):
        if self.first is None:
            print("The LinkedList is empty!")
            return

        node = self.first
        while node.next.next is not None:
            node = node.next
        node.next = None
        self.last = node
