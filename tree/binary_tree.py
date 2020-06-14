from collections import deque

__author__ = "akhtar"


class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.left = right

    def get_right(self):
        return self.right


class Tree:
    @staticmethod
    def inorder(node):
        """ Inorder traversal of a binary tree. """
        if not node:
            return

        Tree.inorder(node.left)
        print(node.data, end=" ")
        Tree.inorder(node.right)

    @staticmethod
    def insert(node, data):
        """ Insert into a binary tree. """
        queue = deque([])
        queue.append(node)
        new_node = TreeNode(data)

        # Do level order traversal until we find an empty place.
        while len(queue):
            node = queue.popleft()

            if not node.left:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            if not node.right:
                node.right = new_node
                break
            else:
                queue.append(node.right)
