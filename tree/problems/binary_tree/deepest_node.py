__author__ = "akhtar"

from collections import deque


def find_deepest_node(root):
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
    
    return node.data
