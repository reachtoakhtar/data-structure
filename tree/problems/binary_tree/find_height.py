__author__ = "akhtar"

from collections import deque


def find_height_recursive(node):
    """
    Find the height of a binary tree.

    :param BTreeNode node: The root of the tree.
    :return: height of the tree.
    :rtype: int
    """

    if node is None:
        return 0
    
    left_height = find_height_recursive(node.left)
    right_height = find_height_recursive(node.right)
    return max(left_height, right_height) + 1


def find_height_iterative(root):
    """
    Find the height of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: height of the tree.
    :rtype: int
    """

    if root is None:
        return 0
    
    q = deque([])
    q.append(root)
    height = 0
    
    while True:
        nodecount = len(q)
        if nodecount == 0:
            return height
        
        height += 1
        
        while nodecount > 0:
            node = q.popleft()
            
            if node.left is not None:
                q.append(node.left)
            
            if node.right is not None:
                q.append(node.right)
                
            nodecount -= 1
