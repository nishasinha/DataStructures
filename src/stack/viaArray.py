
class Stack:
    def __init__(self):
        self.stack = None

    def create(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def print_stack(self):
        if self.stack is None:
            print("Stack not created yet!")
            return

        if stack.is_empty():
            print("Cannot print! Stack is empty.")
            return

        print("Stack top to bottom")
        last = len(self.stack) - 1
        while last >= 0:
            print(self.stack[last])
            last = last-1
        print("Stack ends!\n")

    def pop(self):
        if self.is_empty():
            print("Can't pop! Stack is empty.")
            return float("-inf")

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            print("Can't peek! Stack is empty.")
            return

        print("Stack top is {}". format(self.stack[len(self.stack) - 1]))


if __name__ == '__main__':
    print("Stack using array")

    stack = Stack()
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

