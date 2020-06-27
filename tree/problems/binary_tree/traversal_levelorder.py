__author__ = "akhtar"

from collections import deque


def levelorder(root):
    """
    Levelorder traversal of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: nothing.
    :rtype: None
    """
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
