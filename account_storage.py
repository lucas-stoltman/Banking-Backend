# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

# TODO BST to store accounts
# class AccountStorage:

# A utility class that represents
# an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A utility function to insert
    # a new node with the given key

    def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root

    # A utility function to do inorder tree traversal

    def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)

    # Driver program to test the above functions
    # Let us create the following BST
    # 50
    # /	 \
    # 30	 70
    # / \ / \
    # 20 40 60 80

    # A utility function to search a given key in BST
    def search(root, key):

        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return root

        # Key is greater than root's key
        if root.val < key:
            return search(root.right, key)

        # Key is smaller than root's key
        return search(root.left, key)