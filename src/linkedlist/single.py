"""
Single Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return

        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")

    def insert(self, item, after=None):
        new_node = Node(item)
        temp = self.head

        if after is None:
            # Append at start
            new_node.next = self.head
            self.head = new_node
            return

        while temp:
            if temp.data == after:
                print("Found")
                break
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def delete(self, item):
        if self.head.data == item:
            self.head = self.head.next
            return

        prev = self.head
        temp = self.head.next

        while temp:
            if temp.data == item:
                print("Found item {} in linked list".format(temp.data))
                break
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next
            temp = None
        else:
            print("NOT Found item {} in linked list".format(item))

    def delete_list(self):
        self.head = None


if __name__ == '__main__':
    ll = LinkedList()
    ll.print_list()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.print_list()

    print("\nInsertion in linked list")
    ll.insert(4, 2)
    ll.print_list()

    ll.insert(5)
    ll.print_list()

    ll.insert(7, 3)
    ll.print_list()

    ll.insert(0)
    ll.print_list()

    print("\nDeletion in linked list")
    ll.delete(0)
    ll.print_list()

    ll.delete(2)
    ll.print_list()

    ll.delete(2)
    ll.print_list()

    ll.delete(7)
    ll.print_list()

    ll.delete(1)
    ll.print_list()

    ll.delete_list()
    ll.print_list()
    ll.delete_list()
    ll.print_list()
