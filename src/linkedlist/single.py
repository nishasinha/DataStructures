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

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
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


if __name__ == '__main__':
    ll = LinkedList()

    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    ll.head.next = second
    second.next = third

    ll.printList()

    ll.insert(4, 2)
    ll.printList()

    ll.insert(5)
    ll.printList()

    ll.insert(7, 3)
    ll.printList()
