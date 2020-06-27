from collections import deque

__author__ = "akhtar"


def find_size_recursive(node):
    """
    Find the size of a binary tree.

    :param BTreeNode node: The root of the tree.
    :return: the tree size.
    :rtype: int
    """
    
    if node is None:
        return 0
    else:
        return find_size_recursive(node.left) + 1 + find_size_recursive(node.right)


def find_size_iterative(root):
    """
    Find the size of a binary tree.

    :param BTreeNode root: The root of the tree.
    :return: the tree size.
    :rtype: int
    """
    
    if root is None:
        return 0
    
    queue = deque([])
    queue.append(root)
    
    count = 0
    while len(queue):
        node = queue.popleft()
        count += 1
        
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
            
    return count
