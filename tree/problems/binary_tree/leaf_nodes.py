__author__ = "akhtar"

from collections import deque


def find_leaf_nodes(root):
    """
    Find the number of leaf nodes in a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: the count of leaf nodes.
    :rtype: int
    """
    if root is None:
        return

    q = deque([])
    q.append(root)
    count = 0
    
    while len(q):
        node = q.popleft()
        
        if node.left is None and node.right is None:
            count += 1
        if node.left is not None:
            q.append(node.left)
        
        if node.right is not None:
            q.append(node.right)
    
    return count
