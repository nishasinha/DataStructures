"""
Doubly Ended Queue:
A queue that can support insert and remove from both the ends.

* Operations:
1. insertRear()
2. insertFront()
3. removeFront()
4. removeRear()

5. getFront()
6. getRear()
7. isFull()
8. isEmpty()

* Implementation:
1. Doubly linked list
2. Circular Array
3. Python collections 'deque' data structure.

They all allow the first 4 operations in O(1) time.
"""
from collections import deque

if __name__ == "__main__":
    print("Double ended Queue!")

    dq = deque([1, 2, 3])
    print(dq)

    dq.append(4)
    dq.append(5)
    print(dq)

    dq.appendleft(0)
    dq.appendleft(-1)
    print(dq)

    dq.pop()
    print(dq)
    dq.popleft()
    print(dq)

    print("***************")
    dq.insert(2, 10)
    dq.insert(10, 11)
    print(dq)

    dq.insert(-1, 12)
    print(dq)
    print("***************")

    dq.remove(1)
    print(dq)

    dq.reverse()
    print(dq)

    print(dq.count(12))

    dq.extend([21, 23, 22])
    print(dq)

    dq.extendleft([-11, -12, -13])
    print(dq)

    print("**** Rotate ***********")
    dq.rotate(5)
    print(dq)

    dq.rotate(-5)
    print(dq)
