"""
Queue:
- linear data structure
- FIFO order followed, that is the item which was first inserted will be removed first.

* use case
- any consumer queue like, on bus stop or train ticket queue
- disk scheduling/ cpu scheduling
- sending data asynchronously.

* maintains 2 pointers:
1. front
2. rear

* operations:
1. enqueue - O(1) - insert an element at the rear end of queue.
2. deque - O(1) - remove an element from the front of queue.
3. isEmpty - O(1)
4. isFull - O(1)

* types:
1. Queue
2. Circular queue, saves the space which may get wasted in normal queue.
3. De-queue, doubly ended queue
4. Priority queue

* implemented via:
1. array
2. linked list
"""