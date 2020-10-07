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

    def count(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next
        print("Linked list has {} elements.".format(count))

    def count_recursive(self):
        print("Linked list has {} elements.".format(self._get_count_rec(self.head)))

    def _get_count_rec(self, node):
        if node is None:
            return 0
        return 1 + self._get_count_rec(node.next)

    def search(self, item):
        current = self.head
        while current:
            if current.data == item:
                print("Found {} in linked list".format(item))
                return True
            current = current.next

        print("Not Found {} in linked list".format(item))
        return False

    def search_recursive(self, item):
        found = self._search_rec(item, self.head, found=False)
        if not found:
            print("Not Found rec {} in linked list".format(item))

        return found

    def _search_rec(self, item, node, found):
        if node is None:
            return found

        if node.data == item:
            print("Found rec {} in linked list".format(item))
            return True

        return found or self._search_rec(item, node.next, found)

    def middle(self):
        if not self.head:
            print("Empty list")

        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            print("Pointers at slow {}, fast {}".format(slow.data, fast.data))
            fast = fast.next.next
            slow = slow.next

        print("Middle is at {}.\n".format(slow.data))


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

    print("\nCount")
    ll.print_list()
    ll.count()

    ll.count_recursive()

    print("\nSearch")
    ll.print_list()
    ll.search(1)
    ll.search(9)

    ll.search_recursive(1)
    ll.search_recursive(11)

    print("\nFind middle of inked list")
    ll.print_list()
    ll.middle()

    ll.insert(10)
    ll.print_list()
    ll.middle()

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
