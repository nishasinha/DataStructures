"""
Binary Search Tree:
a tree is called a binary search tree if
1. all nodes in the left subtree are lesser than the root.
2. all nodes in the right subtree are bigger than the root.
3. the left and the right subtrees are also binary search tress.


* Traversal:
In order - sorted list comes out.
Pre order
Post order
Level order

* Operations:
For balanced BST, that is the difference in the height of left and right subtree is 1.

1. Insert - O(Log n)
Start from root, if element is at root, return root.
If element > rot, go right,
else go left.
Insert at leaf!

2. Search - O(Log n)

3. Delete - O(Log n)
Case a:
Node to delete has 0 children - just drop the node

Case b:
Node to delete has 1 children - replace node with that child node, delete the child node.

Case c:
Node to delete has 2 children - find the in order successor node, replace the node with the in order successor,
delete the in order successor node.

Tree may be skewed in that case all operations take O(n).

* Use case:
1. Need sorted result for a dynamically growing list.
2. To perform closest, maximum, min, or range queries.
3. To customize the BST for the problem.
"""