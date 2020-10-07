"""
Implementing circular queue via Array.
The next index is obtained via modulo operator.

Eg: If size = 5, then,
0 % 5 = 0
1 % 5 = 1
2 % 5 = 2
3 % 5 = 3
4 % 5 = 4
and all indices are covered.

Then,
5 % 5 = 0
6 % 5 = 1
7 % 5 = 2

and the indices are repeated in (0,1,2,3,4) for modulo of 5.

"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.front = 0
        self.rear = -1
        self.Q = [None] * self.capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def print_q(self):
        if self.is_empty():
            print("Queue is empty!")
            return

        i = self.front
        while i != self.rear:
            print(self.Q[i], end="->")
            i = (i + 1) % self.capacity

        print(self.Q[self.rear], end="->")
        print("END")

    def enqueue(self, item):
        if self.is_full():
            print("Overflow!")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("Enqueued '{}' at position '{}'.".format(item, self.rear))

    def dequeue(self):
        if self.is_empty():
            print("Underflow!")
            return

        item = self.Q[self.front]
        print("Dequeued '{}' at position '{}'.".format(item, self.front))
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1


if __name__ == '__main__':
    print("Queue via array")
    q = Queue(5)

    print("\n********* Enqueue ***********")
    q.print_q()

    q.enqueue('a')
    q.print_q()

    q.enqueue('b')
    q.print_q()

    q.enqueue('c')
    q.enqueue('d')
    q.enqueue('e')
    q.print_q()
    q.enqueue('f')

    print("\n********* Dequeue ***********")
    q.print_q()

    q.dequeue()
    q.print_q()

    q.dequeue()
    q.dequeue()
    q.print_q()

    q.enqueue('f')
    q.print_q()
    q.enqueue('g')
    q.enqueue('h')
    q.print_q()

    q.enqueue('i')
