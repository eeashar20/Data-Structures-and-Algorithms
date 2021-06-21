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
        if self.is_empty():
            return

        previous = self.first
        current = previous.next
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following

        self.last = self.first
        self.last.next = None
        self.first = previous

    """This function returns the value of the kth node from the end."""

    # example Linked list [10 -> 20 -> 30 -> 40 -> 50]
    #                                   *           *
    # k = 1 (50)
    # k = 2 (40)
    # k = 3 (30_
    def get_kth_from_the_end(self, k):
        if self.is_empty():
            print("No data in the Linked List.")
            return

        f_ptr = s_ptr = self.first
        distance = k - 1
        count = 0
        while count < distance:
            s_ptr = s_ptr.next
            print(f"I am count {count}")
            if s_ptr is None:
                raise ValueError("Index can't be greater than the total number of elements in the Linked List")
            count += 1

        while s_ptr.next is not None:
            f_ptr = f_ptr.next
            s_ptr = s_ptr.next

        return f_ptr.value

    """This function prints the middle of the Linked List. If the list has an even number of nodes, there would be 
    two middle nodes. """

    def print_middle(self):
        f_ptr = s_ptr = self.first
        count = 0
        while s_ptr != self.last:
            s_ptr = s_ptr.next
            count += 1

        if (count + 1) % 2 != 0:  # Here this count + 1 represents the whether the Linked List has even no. of nodes or
            # odd no. of nodes.
            for i in range(0, count // 2):
                f_ptr = f_ptr.next
            print(f_ptr.value)

        else:
            for i in range(0, count // 2):
                f_ptr = f_ptr.next
            print(f_ptr.value, f_ptr.next.value)

    """Mosh's Solution"""
    def printMiddle(self):
        a = self.first
        b = self.first
        while b != self.last and b.next != self.last:
            b = b.next.next;
            a = a.next;

        if b == self.last:
            print(a.value);
        else:
            print(f"{a.value} , {a.next.value}")
