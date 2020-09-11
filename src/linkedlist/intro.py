"""
Linked List

* linear data structure
* each element is called Node, having data and pointer to next node

* why?:
- in array the size should be known before hand.
- insertion and deletion is hard in array as shifting required.

* advantages:
- dynamic insertion and deletion allowed and
- only the required space is taken.

* disadvantage:
- random access as in array not allowed,
accessing any element takes theta(i), where i represents the position of element in linked list.
- extra space needed in each elemnt to store the next address.

* types:
1. Singly
head -> first node -> second node -> ...... last node -> null

2. Doubly
head <-> first <-> second <-> third ..... <-> last -> null
can traverse in both direction

3. Circular (Singly or Doubly)
head ->
first node -> second node -> ...... last node -> first node

head <->
first <-> second <-> third ..... <-> last <-> first

* Time complexity
1. Traverse O(n)
2. Search O(n)
3. Insert O(n), O(1) if the node to insert at given
4. Delete On(n), O(1) if node to delete at given


"""