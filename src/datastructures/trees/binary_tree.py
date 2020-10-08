"""
Insertion in a Binary Tree in level order.
- Given a binary tree and a key, insert the key into the binary tree at the first position available in level order.


Deletion in a Binary Tree
- Given a binary tree, delete a node from it by making sure that tree shrinks from the bottom
(i.e. the deleted node is replaced by bottom most and rightmost node).
"""

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_level_oder(self, item):
        new_node = Node(item)

        if not self.root:
            self.root = new_node
            return

        q = deque()
        q.append(self.root)
        while len(q):
            temp = q.popleft()

            if not temp.left:
                temp.left = new_node
                return
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = new_node
                return
            else:
                q.append(temp.right)

    def print_level_order(self):
        if self.root is None:
            print("Tree is empty!")
            return

        q = deque()
        q.append(self.root)

        while len(q):
            temp = q.popleft()
            print(temp.data, end="->")

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        print("DONE")

    def _delete_node(self, last_node):
        if not self.root:
            return

        q = deque()
        q.append(self.root)
        while len(q):
            temp = q.popleft()

            if temp.left and temp.left is last_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

            if temp.right and temp.right is last_node:
                temp.right = None
                return
            else:
                q.append(temp.right)

    def delete(self, item):
        if not self.root:
            print("Underflow!")
            return

        # Find last node, replace data with key node, delete last node
        q = deque()
        q.append(self.root)

        node_to_delete = None
        last_node = None
        while len(q):
            temp = q.popleft()

            if temp.data == item:
                node_to_delete = temp

            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)

            last_node = temp

        if node_to_delete:
            print("Found the node to delete.")
            print("Replacing node {} with {}".format(node_to_delete.data, last_node.data))
            self._delete_node(last_node)
            node_to_delete.data = last_node.data
        else:
            print("Not Found the node to delete.")

    # def _inorder(self, node):

    def print_in_order(self, node):
        # LNR
        if not node:
            return

        self.print_in_order(node.left)
        print(node.data, end=" ")
        self.print_in_order(node.right)

    def print_post_order(self):
        if not self.root:
            print("Tree is empty!")
            return

        # LRN
        print("Post order traversal")
        self._post_order(self.root)
        print("DONE")

    def _post_order(self, node):
        if not node:
            return

        self._post_order(node.left)
        self._post_order(node.right)
        print(node.data, end="->")


if __name__ == '__main__':
    print("Binary Tree")
    tree = BinaryTree()
    tree.print_level_order()

    tree.insert_level_oder(1)
    tree.print_level_order()

    tree.insert_level_oder(2)
    tree.insert_level_oder(3)
    tree.insert_level_oder(4)
    tree.print_level_order()

    tree.root.right = None
    tree.print_level_order()

    tree.insert_level_oder(5)
    tree.print_level_order()

    tree.insert_level_oder(6)
    tree.insert_level_oder(7)
    tree.print_level_order()

    tree.delete(5)
    tree.print_level_order()
    tree.delete(10)
    tree.print_level_order()

    tree.print_in_order(tree.root)
    tree.print_post_order()
