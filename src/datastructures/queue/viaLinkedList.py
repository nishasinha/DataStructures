class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def _is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self._is_empty():
            self.rear = self.front = new_node
            return

        self.rear.next = new_node
        self.rear = new_node
        print("Enqueued {}".format(item))

    def dequeue(self):
        if self._is_empty():
            print("Underflow!")
            return
        to_delete = self.front
        self.front = self.front.next
        print("Dequeued {}".format(to_delete.data))

    def print_q(self):
        if self._is_empty():
            print("Empty Queue!")
            return

        temp = self.front
        while temp != self.rear:
            print(temp.data, end="->")
            temp = temp.next

        print(self.rear.data, end="->")
        print("END")


if __name__ == "__main__":
    print("Queue via Linked List")

    q = Queue()
    q.print_q()

    q.enqueue('a')
    q.print_q()

    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')
    q.print_q()

    q.dequeue()
    q.print_q()

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.print_q()

    q.dequeue()
    q.print_q()

    q.enqueue('f')
    q.enqueue('g')
    q.print_q()
    q.dequeue()
    q.print_q()
