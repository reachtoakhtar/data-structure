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
    def preorder_iterative(root):
        if root is None:
            return

        stack = []
        stack.append(root)

        while len(stack):
            node = stack.pop()
            print(node.data, end=" ")

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    @staticmethod
    def preorder_recursive(node):
        if node is None:
            return

        print(node.data, end=" ")
        Tree.preorder_recursive(node.left)
        Tree.preorder_recursive(node.right)

    @staticmethod
    def inorder_iterative(root):
        if root is None:
            return

        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif len(stack):
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right
            else:
                break

    @staticmethod
    def inorder_recursive(node):
        if node is None:
            return

        Tree.inorder_recursive(node.left)
        print(node.data, end=" ")
        Tree.inorder_recursive(node.right)

    @staticmethod
    def postorder_iterative(root):
        if root is None:
            return

        stack1 = []
        stack2 = []
        stack1.append(root)

        while len(stack1):
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while len(stack2):
            node = stack2.pop()
            print(node.data, end=" ")

    @staticmethod
    def postorder_recursive(node):
        if node is None:
            return

        Tree.postorder_recursive(node.left)
        Tree.postorder_recursive(node.right)
        print(node.data, end=" ")

    @staticmethod
    def levelorder(root):
        if root is None:
            return

        queue = deque([])
        queue.append(root)

        while len(queue):
            node = queue.popleft()
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    @staticmethod
    def preorder(node):
        Tree.preorder_recursive(node)

    @staticmethod
    def inorder(node):
        Tree.inorder_recursive(node)

    @staticmethod
    def postorder(node):
        Tree.postorder_recursive(node)

    @staticmethod
    def insert(node, data):
        queue = deque([])
        queue.append(node)
        new_node = TreeNode(data)

        # Do level order traversal until we find an empty place.
        while len(queue):
            node = queue.popleft()

            if node.left is None:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            if node.right is None:
                node.right = new_node
                break
            else:
                queue.append(node.right)
