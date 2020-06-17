from collections import deque

from tree.binary_tree import TreeNode

__author__ = "akhtar"


def reverse_level_order(node):
    """
    Print the reverse level order data for a given binary tree.

    :param TreeNode node: The node of the tree.
    :return: reverse level order data.
    :rtype: list
    """
    queue = deque([])
    queue.append(node)
    stack = []
    
    while len(queue):
        node = queue.popleft()
        
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
        
        stack.append(node)
    
    while len(stack):
        node = stack.pop()
        print(str(node.data) + " ", end=" ")
