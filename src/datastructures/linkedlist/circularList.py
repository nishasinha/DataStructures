"""
Circular Linked List
- singular or
- double

Head ->
1 -> 2-> 3-> 1

* adv:
- can traverse the whole ist given any node
- queue implementation - keep the pointer to last inserted node as rear, front = rear.next
- used in OS to distributes computer resources to applications
- Fibonacci heap uses double circular linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if not self.head:
            print("Empty List")
            return

        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
            if temp == self.head:
                break

        print("End->{}".format(self.head.data))

    def insert(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            if temp.next == self.head:
                break
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def delete(self, item):
        if not self.head:
            print("Empty list")
            return

        temp = self.head
        prev = self.head
        while temp.next != self.head:
            if item == temp.data:
                print("Found {} to delete".format(temp.data))
                break
            prev = temp
            temp = temp.next

        if temp.next == self.head:
            print("Not Found {} to delete".format(item))
            return

        # print("prev {}, temp {}".format(prev.data, temp.data))
        if temp == self.head:
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = prev.next
            last.next = self.head
        else:
            prev.next = temp.next


if __name__ == '__main__':
    print("Circular Linked List")
    cll = CircularLinkedList()
    cll.print_list()

    print("\nInsert")
    cll.insert(1)
    cll.print_list()

    cll.insert(2)
    cll.print_list()

    cll.insert(3)
    cll.print_list()

    cll.insert(4)
    cll.print_list()

    cll.insert(5)
    cll.print_list()

    print("\nDelete")

    print("\n- delete head = 1")
    cll.delete(1)  # head
    cll.print_list()

    print("\n- delete mid = 3")
    cll.delete(3)  # mid
    cll.print_list()

    print("\n- delete last = 5")
    cll.delete(5)  # last
    cll.print_list()

    print("\n- delete non existing = 3")
    cll.delete(3)  # not there
    cll.print_list()
