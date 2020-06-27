__author__ = "akhtar"

from collections import deque


def find_deepest_node(root):
    """
    Find the deepest node in a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: the deepest node.
    :rtype: BTreeNode
    """
    if root is None:
        return

    q = deque([])
    q.append(root)
    node = None
    
    while len(q):
        node = q.popleft()
        
        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)
    
    return node
