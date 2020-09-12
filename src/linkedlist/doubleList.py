"""
Doubly Linked List

* each node has three items:
1. data
2. prev pointer
3. next pointer

Head -> 1
NULL <- 1 <-> 2 <-> 3 <-> NULL

* adv:
- can traverse the list in any direction
- deletion does not need prev pointer specially.
- given the node to delete, deletion is easy.
- given the node to insert, insertion is easy.

* disadv:
- extra pointer at each node.
- extra step in every operation to update the prev pointer
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("NULL")

    def print_rev(self):
        if not self.head:
            print("Empty list")
            return

        last = self.head
        while last.next:
            last = last.next

        while last:
            print(last.data, end="<-")
            last = last.prev
        print("NULL")

    def insert(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def delete(self, item):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        while current:
            if item == current.data:
                print("Found {} to delete".format(item))
                break
            current = current.next

        if current == self.head:
            self.head = current.next
            current.next.prev = None
        elif current is None:
            print("Not Found {} to delete".format(item))
            return
        else:
            current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev


if __name__ == '__main__':
    print("Doubly Linked List")
    cll = DoubleLinkedList()
    cll.print_list()

    print("\nInsert")
    cll.insert(1)
    cll.print_list()
    cll.print_rev()

    cll.insert(2)
    cll.print_list()
    cll.print_rev()

    cll.insert(3)
    cll.print_list()
    cll.print_rev()

    cll.insert(4)
    cll.print_list()
    cll.print_rev()

    cll.insert(5)
    cll.print_list()
    cll.print_rev()

    print("\nDelete")

    print("\n- delete head = 1")
    cll.delete(1)  # head
    cll.print_list()
    cll.print_rev()

    print("\n- delete mid = 3")
    cll.delete(3)  # mid
    cll.print_list()
    cll.print_rev()

    print("\n- delete last = 5")
    cll.delete(5)  # last
    cll.print_list()
    cll.print_rev()

    print("\n- delete non existing = 3")
    cll.delete(3)  # not there
    cll.print_list()
    cll.print_rev()
