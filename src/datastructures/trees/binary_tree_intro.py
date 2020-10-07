"""
* Binary Tree
a hierarchical data structure,
can either be empty or have nodes such that each node has:
- a data value
- a link to left binary tree
- a link to right binary tree


* Why?
- maintain sorted list of items with frequent inserts and deletes:
search/ access faster than linked list
insertion/ deletion faster than array

- problems which have hierarchical nature eg:
filesystem,
business chess,
router algorithms

* Time:
search, insert, delete - O(n)

* Traversal:
Breadth First = Level Order
Depth First = In order (LNR), Pre order (NLR), Post order (LRN)

"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


if __name__ == '__main__':
    print("Binary tree")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print(root)


"""
Properties:
1. Level of root = 0.
2. Height of root = 1.

3. Maximum number of nodes at level l = (2 ** l)

level = 0, max nodes = 2 ** 0 = 1
level = 1, max nodes = 2 ** 1 = 2
level = 2, max nodes = 2 ** 2 = 4

4. Maximum number of nodes in tree of height h = (2 ** h - 1)

height = 1, max nodes = 1 (2 ** 1 -1)
height = 2, max nodes = 3 (2 ** 2 -1)
height = 3, max nodes = 1+2+4 = 7 = (2**3 -1)

5. In 'n' nodes' tree, maximum height = log2 (n+1)

n = 1, height = log2 (1+1) =  1

6. In tree with 'l' leaves, max level = log2(l) + 1

7.In tree which has 0 or 2 children only,
number of leaf nodes = number of nodes with 2 children + 1

* Handshaking lemma may be used to prove this.
"""


"""
Binary Tree Types:
1. Full
Binary tree in which every node has 2 or 0 children.
 Nodes with 0 children are leaf nodes. 
 All other nodes have 2 children.

Number of leaf = Number of internal nodes + 1 

2. Complete
Binary tree in which all levels are full and the last level has leaf nodes which are as left as possible.
Eg: Binary Heap

3. Perfect
Binary tree in which all levels are full including the last level, 
 ie complete binary tree with last level full.
 nodes = 2**h -1
Eg: Family tree

4. Balanced
Binary tree which maintains its height at O(log2 n), n is number of nodes.
Used for efficient search, inserts or deletes task.
Eg: 
AVL (difference in height of left and right subtrees is 1)
Red Black (no red nodes are adjacent, number of black nodes in all root to leaf path is same)

5. Pathological/ Degenerate tree = linked list.

"""