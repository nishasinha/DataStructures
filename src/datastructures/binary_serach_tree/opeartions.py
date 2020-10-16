class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BST:
    @staticmethod
    def in_order(root):
        if not root:
            return

        # LNR
        BST.in_order(root.left)
        print(root.data, end=" ")
        BST.in_order(root.right)

    @staticmethod
    def insert(root, key):
        if root is None or key == root.data:
            root = TreeNode(key)

        elif key < root.data:
            root.left = BST.insert(root.left, key)

        elif key > root.data:
            root.right = BST.insert(root.right, key)

        return root

    @staticmethod
    def find(root, key):
        if root is None:
            return False

        if key == root.data:
            return True
        elif key < root.data:
            return BST.find(root.left, key)
        else:
            return BST.find(root.right, key)

    @staticmethod
    def pre_order(root):
        if not root:
            return

        # NLR
        print(root.data, end=" ")
        BST.pre_order(root.left)
        BST.pre_order(root.right)

    @staticmethod
    def post_order(root):
        if not root:
            return

            # LRN
        BST.post_order(root.left)
        BST.post_order(root.right)
        print(root.data, end=" ")


if __name__ == '__main__':
    print("Binary Search Tree")

    r = TreeNode(10)
    print("\nIn order after root")
    BST.in_order(r)

    r = BST.insert(r, 1)
    print("\nIn order after 1")
    BST.in_order(r)

    r = BST.insert(r, 11)
    r = BST.insert(r, 12)
    r = BST.insert(r, 7)
    r = BST.insert(r, 4)
    print("\nIn order")
    BST.in_order(r)

    print("\nFound 1 in bst: ", BST.find(r, 1))
    print("\nFound 5 in bst: ", BST.find(r, 5))

    print("\nPre order")
    BST.pre_order(r)

    print("\nPost order")
    BST.post_order(r)
