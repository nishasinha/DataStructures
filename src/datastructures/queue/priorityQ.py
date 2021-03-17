"""
Priority Queues are used to operate the FIFO with given priority.
- Every item has a priority.
- At dequeue, item with highest priority is removed.
    If many elements have same priority, FIFo is followed.

* Operations:
1. insert(item, priority) - O(1)
2. getHighestPriority() - O(n) in array
3. deleteHighestPriority() - O(n) in array

* Using heaps:
Heaps is another data structure that can maintain order of iterables (order from the elements itself).
Heaps are used to implement priority Q.

1. insert - O(Log n)
2. delete - O(Log n)
3. getHighestPriority - O(1)

* Applications:
1. CPU scheduling of processes
2. Dijkstra shortest path, Prims MST algo

"""
import heapq


class PriorityQ:
    def __init__(self, capacity):
        self.capacity = capacity
        self.q = [] * self.capacity
        heapq.heapify(self.q)
        self.size = 0

    def _is_empty(self):
        return self.size == 0

    def _is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self._is_full():
            print("Overflow!")
            return

        heapq.heappush(self.q, item)
        self.size = self.size + 1
        print("Enqueued {}.".format(item))

    def dequeue(self):
        if self._is_empty():
            print("Underflow!")
            return

        item = heapq.heappop(self.q)
        self.size = self.size - 1
        print("Dequeued {}.".format(item))

    def print_q(self):
        print("Priority Queue is: {}".format(list(self.q)))


if __name__ == "__main__":
    print("Priority Queue")

    pq = PriorityQ(5)
    pq.print_q()

    print("***** Enqueue *********")
    pq.enqueue('a')
    pq.enqueue('z')
    pq.print_q()

    pq.enqueue('c')
    pq.print_q()
    pq.enqueue('x')
    pq.print_q()
    pq.enqueue('d')
    pq.print_q()

    pq.enqueue('e')

    print("***** Dequeue *********")

    pq.print_q()
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    pq.print_q()

    pq.dequeue()
    pq.dequeue()
    pq.print_q()
    pq.dequeue()
