# Created by Lucas Stoltman
# Program 6
# May 19th, 2022
# CSS 340 A, Dimpsey
# Version: 1.0

# TODO BST to store accounts
# key = account number
# value = account object
class Node:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        return self.left_child is None and self.right_child is None

    # debug function
    def print(self):
        print("Value:", self.value)
        print("Left:", self.left_child)
        print("Right:", self.right_child)

    def __str__(self):
        return str(self.key) + " [" + str(self.value) + "]"


class BST:
    def __init__(self):
        self._count = 0
        self._root = None

    def get(self, key):
        current_node = self._root
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            elif current_node.key > key:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return None

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        if self.is_empty():
            self._root = Node(key, value)
            self._count = 1
            return True
        current_node = self._root
        while True:
            if current_node.key == key:
                current_node.value = value
                return False
            elif current_node.key > key:
                if current_node.left_child is None:
                    new_node = Node(key, value)
                    current_node.left_child = new_node
                    break
                else:
                    current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    new_node = Node(key, value)
                    current_node.right_child = new_node
                    break
                else:
                    current_node = current_node.right_child
        self._count += 1
        return True

    def __setitem__(self, key, data):
        self.put(key, data)

    def remove(self, key):
        # First Handle Empty Tree node
        if self._root is None:
            return False
        # Handle removal of root
        if self._root.key == key:
            self._count -= 1
            if self._root.left_child is None:
                self._root = self._root.right_child
            elif self._root.right_child is None:
                self._root = self._root.left_child
            else:
                replace_node = self.get_remove_right_small(self._root)
                self._root.key = replace_node.key
                self._root.value = replace_node.value
        # Find node which holds key by having current node stop at parent of node
        else:
            current_node = self._root
            while current_node is not None:
                # Following code deal with the case where left child has key
                if current_node.left_child and current_node.left_child == key:
                    found_node = current_node.left_child
                    if found_node.is_leaf():
                        current_node.left_child = None
                    elif found_node.right_child is None:
                        current_node.left_child = found_node.left_child
                    elif found_node.left_child is None:
                        current_node.left_child = found_node.right_child
                    else:
                        replace_node = self.get_remove_right_small(found_node)
                        found_node.key = replace_node.key
                        found_node.value = replace_node.value
                        self._count -= 1
                        return True

    def size(self):
        return self._count

    def is_empty(self):
        return self._count == 0
