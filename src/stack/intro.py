"""
Stack:
- Last In First Out (LIFO) or
- First In Last Out (FILO)

It is like stack of plates. The last inserted plate would be the first one to be out.

* top - a pointer to the last added element.

* operations:
1. push: add an item to stack, overflow error if stack is full
2. pop: take out the last inserted element, underflow error if stack is empty.
3. peek: return the element at top.
4. isEmpty: true if stack empty.

any operation takes O(1) time.

* use case:
1. balanced parenthesis
2. infix to postfix or prefix
3. N queen problem.
4. tower of hanoi
5. redo, undo features in browsers and editors.

* implementation:
- via array
- via linked list, allows dynamic sizing
"""