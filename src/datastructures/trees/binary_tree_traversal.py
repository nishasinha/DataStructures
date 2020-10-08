"""
Two types:
1. Breadth First - Level Order - O(n)
- Extra space = O(w), w is the width of tree.
    - Worst case space = O(2 ** h), perfect binary tree where maximum nodes are at the leaves.
    - Occurs when tree is more balanced.
- To be used for any problem where the nodes are close to root.

2. Depth First - O(n)
- Types:
Pre order
Post order
In order

- Extra space = O(h)
    Worst case = O(n), for skewed tree
- To be used for problems where the nodes near the leaf are to be visited first.

"""