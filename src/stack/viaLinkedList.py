"""
via linked list:

* create:
NULL

* push
1 = top -> 1 -> NULL
2 = top -> 2 -> 1 -> NUll
3 = top -> 3 -> 2 -> 1 -> NUll

* pop:
pop() = 3, top -> 2 -> 1 -> NUll
pop() = 2, top -> 1 -> NUll
pop() = 1, top -> NUll




"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None

    def print_stack(self):
        if not self.top:
            print("Stack is empty.")
            return

        current = self.top
        print("Stack from top to bottom")
        while current:
            print(current.data)
            current = current.next

        print("Stack ends!")

    def create(self):
        pass

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.top = new_node
            return
        new_node.next = self.top
        self.top = new_node

    def peek(self):
        if self.is_empty():
            print("can't peek! Stack is empty.")
            return

        print("Stack top is at {}".format(self.top.data))

    def pop(self):
        if self.is_empty():
            print("Can't pop! Stack is empty.")
            return

        print("Popping out {} from stack".format(self.top.data))
        old = self.top
        self.top = self.top.next
        old = None

if __name__ == '__main__':
    print("Stack using linked list")

    stack = StackLinkedList()
    stack.print_stack()

    print("\nCreate")
    stack.create()
    stack.print_stack()
    print("Is stack empty? {}".format(stack.is_empty()))

    print("\nPush")
    stack.push(1)
    stack.print_stack()

    stack.push(2)
    stack.push(3)
    stack.print_stack()

    print("\nPeek")
    stack.peek()

    print("\nPop")
    stack.pop()
    stack.print_stack()

    stack.pop()
    stack.print_stack()

    stack.pop()
    stack.print_stack()

    stack.pop()
    stack.peek()